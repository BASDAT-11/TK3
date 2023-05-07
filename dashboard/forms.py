from django import forms
from django.contrib.auth.forms import UserCreationForm

class LoginForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(attrs={'id':'login-nama','placeholder':'Name'}))  
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'id':'login-email','placeholder':'Email'})) 

# To Be Discussed for TK4
class RegisterAtletForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(attrs={'id':'login-nama','placeholder':'Name'}))  
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'id':'login-email','placeholder':'Email'})) 

class RegisterPelatihForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(attrs={'id':'login-nama','placeholder':'Name'}))  
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'id':'login-email','placeholder':'Email'})) 

class LoginUmpireForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(attrs={'id':'login-nama','placeholder':'Name'}))  
    email = forms.CharField(label='email', widget=forms.EmailInput(attrs={'id':'login-email','placeholder':'Email'}))  



  

    