from django import forms
from django.contrib.auth.forms import UserCreationForm

# To Be Discussed for TK4


class RegisterAtletForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'login-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'login-email', 'placeholder': 'Email'}))
    negara = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'login-negara', 'placeholder': 'Negara'}))


class RegisterPelatihForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'login-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'login-email', 'placeholder': 'Email'}))


class LoginUmpireForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'login-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'login-email', 'placeholder': 'Email'}))
