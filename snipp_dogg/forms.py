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
            'description': forms.Textarea(),
            'body': forms.Textarea(attrs={'autofocus': 'autofocus'})
        }
        fields = [
            'title',
            'language',
            'body',
            'description',
        ]

class SearchForm(forms.Form):
    CHOICES = [ ('language', 'language'),
                ('title', 'title'),
                ('description', 'description')]
    search_choice = forms.ChoiceField(choices=CHOICES)
    search_text = forms.CharField(max_length=255)