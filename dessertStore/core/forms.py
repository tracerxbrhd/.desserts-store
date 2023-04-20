from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username'
    }))

    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Email'
    }))
    
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password'
    }))

    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Repeat Password',
        'type': 'password'
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username'
    }))

    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Password',
        'type': 'password'
    }))