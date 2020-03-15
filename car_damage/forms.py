from django import forms
from .models import Picupload

class ImageForm(forms.ModelForm):
    class Meta:
        model = Picupload
        fields = ['image_file']
