from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, MusicFile

class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']

class MusicFileForm(forms.ModelForm):
    class Meta:
        model = MusicFile
        fields = ['title', 'file', 'visibility', 'allowed_emails']