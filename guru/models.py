from django.db import models

# Create your models here.
class guru(models.Model):
    prof_image=models.ImageField()
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

