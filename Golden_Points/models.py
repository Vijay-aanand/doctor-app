from django.db import models
from django.conf import settings

class Point(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)  # Add this field

    def __str__(self):
        return f"{self.user} - {self.points} points"
