from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SnippDogdUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'profile_description',
        ]