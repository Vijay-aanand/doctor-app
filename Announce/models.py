from django.db import models


# Create your models here


class Announce(models.Model):
 # Correctly reference the user model
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True) 
    image = models.ImageField(upload_to='announces/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
 
