from django import forms
from .models import guru

class guruform(forms.ModelForm):
    class Meta:
        model=guru
        fields=['name','prof_image'] 