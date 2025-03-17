from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    path('', views.index, name='index'),  # Root URL maps to the index view
    path('beat_list/', views.beat_list, name='beat_list'),
    path('beats/<int:beat_id>/', views.beat_detail, name='beat_detail'),

    path('csignup/', views.csignup_view, name='csignup'),  # Combined login and signup
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    # Password reset views
    path('password_reset/', PasswordResetView.as_view(template_name='JVBeats/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(template_name='JVBeats/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='JVBeats/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name= 'JVBeats/password_reset_complete.html'), name='password_reset_complete'),
]
