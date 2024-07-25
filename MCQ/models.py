from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=100)
    option_2 = models.CharField(max_length=100)
    option_3 = models.CharField(max_length=100)
    option_4 = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=100)

    def __str__(self):
        return self.question_text

class UserResponse(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    select_option = models.CharField(max_length=100)
    is_correct = models.BooleanField()

    def save(self, *args, **kwargs):
        self.is_correct = self.select_option == self.question.correct_option
        super().save(*args, **kwargs) 
