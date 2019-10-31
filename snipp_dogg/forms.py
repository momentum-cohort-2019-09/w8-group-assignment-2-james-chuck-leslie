from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, CodeSnippet

class SnippDogdUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'profile_description',
        ]

class CreateSnippForm(forms.ModelForm):

    class Meta:
        model = CodeSnippet
        widgets = {
            'body': forms.Textarea(attrs={'autofocus': 'autofocus'})
        }
        fields = [
            'title',
            'language',
            'body',
            'description',
        ]