from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'id': 'email',
        'name': 'email',
        'required': True,
        'class': 'form-input',
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
