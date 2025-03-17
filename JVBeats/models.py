from django.contrib.auth.models import AbstractUser, User
from django.db import models

class Beat(models.Model):
    GENRE_CHOICES = [
        ('pop', 'Pop'),
        ('folk', 'Folk'),
        ('rock', 'Rock'),
        ('jazz', 'Jazz'),
        ('dance','Dance'),
        ('others', 'Others'),
    ]

    CATEGORY_CHOICES = [
        ('devotional','Devotional'),
        ('remix','Remix'),
        ('movie','Movie'),
        ('independent','Independent'),
        ('others','Others')
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(default="No description available")
    audio_file = models.FileField(upload_to='audio_files/', blank=True, null=True)
    image_file = models.ImageField(upload_to='image_files/', blank=True, null=True)

    # Dropdown fields
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES, default='pop')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='independent')

    # For "Others" input
    custom_genre = models.CharField(max_length=100, blank=True, null=True)
    custom_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title

