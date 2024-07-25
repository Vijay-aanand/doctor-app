from django.db import models
from django.conf import settings
from onetime.models import CustomUser
from django.contrib.auth.models import User



class Folder(models.Model):
    name=models.CharField(max_length=100)
                                                                      
    def _str_(self):
        return self.name  

class Plan(models.Model):    
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def _str_(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()

    def _str_(self):
        return f"{self.user.username} - {self.plan.name}"

 
class QBank(models.Model):
    title = models.CharField(max_length=100) 
    image=models.ImageField(upload_to='QBank/', blank=True, null=True)
    content = models.TextField()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
    def _str_(self):
        return self.title
   
class Test(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def _str_(self):
        return self.title
    
class Video(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    folder=models.ForeignKey(Folder,related_name='videos',on_delete=models.CASCADE)

    def _str_(self):
        return self.title
    
class SavedVideo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} saved {self.video.title}"
    

    



