from django.contrib import admin
from .models import Question,UserResponse

# Register your models here.

admin.site.register(Question)
admin.site.register(UserResponse)