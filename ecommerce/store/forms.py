from django.contrib.auth.forms import UserCreationForm

from .models import Register_user
from django import forms


class CustomUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2 formborder', 'placeholder': 'Enter username'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control my-2 formborder', 'placeholder': 'Enter email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2 formborder', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control my-2 formborder', 'placeholder': 'Confirm password'}))

    class Meta:
        model = Register_user
        fields = ['username', 'email', 'password1', 'password2']
