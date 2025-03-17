from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import Beat
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy


def home(request):
    return HttpResponse("Welcome to JVBeatBazaar!")


def index(request):
    beats = Beat.objects.all()  # Assuming you have a Beat model
    return render(request, 'JVBeats/index.html', {'beats': beats})


@login_required
def beat_list(request):
    search_query = request.GET.get('search', None)
    genre_filter = request.GET.get('genre', None)
    category_filter = request.GET.get('category', None)

    beats = Beat.objects.all()

    # Handle Search functionality for the search box
    if search_query:
        beats = beats.filter(title__icontains=search_query)

    # Handle Filter functionality for Apply button
    if not search_query:  # Ensure this doesn't override search results
        if genre_filter:
            beats = beats.filter(genre=genre_filter)
        if category_filter:
            beats = beats.filter(category=category_filter)

    return render(request, 'JVBeats/beat_list.html', {
        'beats': beats,
        'username': request.user.username  # Pass the username for the template
    })


@login_required
def profile(request):
    return render(request, 'JVBeats/profile.html', {'user': request.user})


@login_required
def update_profile(request):
    from .forms import ProfileUpdateForm
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully.')
            return redirect('profile')  # Redirect back to the profile page
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})


def beat_detail(request, beat_id):
    beat = get_object_or_404(Beat, id=beat_id)
    return render(request, 'JVBeats/product.html', {'beat': beat})


# Custom Password Reset Confirm View
class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('login')  # Redirect to login page after successful password reset


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            users = User.objects.filter(email=email)
            for user in users:
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(str(user.pk).encode())
                reset_link = f"{request.scheme}://{get_current_site(request).domain}/reset/{uid}/{token}/"
                message = render_to_string('password_reset_email.html', {
                    'user': user,
                    'reset_link': reset_link,
                })
                send_mail("Password Reset Request", message, None, [user.email])
            messages.success(request, "Password reset email sent. Please check your inbox.")
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()

    return render(request, "password_reset_form.html", {'form': form})


# Updated CSIGNUP View (Handling both signup and login)
def csignup_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'signup':  # Handle signup
            name = request.POST.get('txt')
            email = request.POST.get('email')
            password = request.POST.get('pswd')

            if User.objects.filter(username=name).exists():
                messages.error(request, "Username already in use.")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email already in use.")
            else:
                user = User.objects.create_user(username=name, email=email, password=password)
                user.save()
                messages.success(request, "Account created successfully. Please log in.")
                return redirect('csignup')

        elif action == 'login':  # Handle login
            email = request.POST.get('email')
            password = request.POST.get('pswd')

            try:
                user = User.objects.get(email=email)
                username = user.username
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('beat_list')  # Redirect to beat_list.html
                else:
                    messages.error(request, "Invalid email or password.")
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")

    return render(request, 'JVBeats/csignup.html')
