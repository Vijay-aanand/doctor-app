from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # This should be unique to avoid conflicts
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # This should be unique to avoid conflicts
         blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )
