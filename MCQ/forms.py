from django import forms
from .models import UserResponse

class UserResponseForm(forms.ModelForm):
    class Meta:
        model = UserResponse
        fields = ['select_option']
