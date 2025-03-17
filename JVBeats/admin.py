from django.contrib import admin
from django.forms import Media
from .models import Beat

@admin.register(Beat)
class BeatAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'category')

    class Media:
        js = ('js/admin_others.js',)
