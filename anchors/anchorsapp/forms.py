from django import forms
from .models import Video
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=['url']
class RegistrationForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']