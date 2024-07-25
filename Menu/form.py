from django import forms
from .models import Folder, Video



class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'url','folder']

