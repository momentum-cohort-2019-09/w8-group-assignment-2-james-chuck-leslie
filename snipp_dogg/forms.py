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
            'language': forms.Select(attrs={'id': 'lingo-field'}),
            'title': forms.TextInput(attrs={'autocomplete': 'off', 'id': 'snipp-title'}),
            'description': forms.Textarea(attrs={'id': 'desc-field'}),
            'body': forms.Textarea(attrs={'autofocus': 'autofocus', 'id': 'codebox'}),
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
    search_choice = forms.ChoiceField(
        choices=CHOICES,
        widget = forms.Select(attrs={'id': "search-choice"}))
    search_text = forms.CharField(
        max_length=255,
        widget = forms.TextInput(attrs={'autocomplete': 'off', 'id': "search-field"}))