from django import forms
from django.contrib.auth.forms import UserCreationForm


class LoginForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'login-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'login-email', 'placeholder': 'Email'}))


class AtletForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'register-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'register-email', 'placeholder': 'Email'}))
    negara = forms.CharField(label='negara', widget=forms.TextInput(
        attrs={'id': 'register-negara', 'placeholder': 'Negara'}))
    tanggal_lahir = forms.DateField(label='tanggal-lahir', widget=forms.DateInput(
        attrs={'type': 'date'}))
    play_right = forms.CharField(label='play-right', widget=forms.RadioSelect(
        choices=[
            (True, 'Right'), 
            (False, 'Left')
            ]))
    tinggi_badan = forms.IntegerField(label='tanggal-lahir', widget=forms.NumberInput(
        attrs={'id': 'register-tinggi-badan', 'placeholder': 'Tinggi Badan'}))
    jenis_kelamin = forms.CharField(label='jenis-kelamin', widget=forms.RadioSelect(
        choices=[
            (True, 'Laki-laki'), 
            (False, 'Perempuan')
            ]))


class PelatihForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'register-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'register-email', 'placeholder': 'Email'}))
    negara = forms.CharField(label='negara', widget=forms.TextInput(
        attrs={'id': 'register-negara', 'placeholder': 'Negara'}))
    kategori = forms.CharField(label='kategori', widget=forms.CheckboxSelectMultiple(
        choices=[
            ('tunggal-putra', 'Tunggal Putra'), 
            ('tunggal-putri', 'Tunggal Putri'),
            ('ganda-putra', 'Ganda Putra'),
            ('ganda-putri', 'Ganda Putri'),
            ('ganda-campuran', 'Ganda campuran')
            ]))
    tanggal_mulai = forms.DateField(label='tanggal-mulai', widget=forms.DateInput(
        attrs={'type': 'date'}))


class UmpireForm(UserCreationForm):
    nama = forms.CharField(label='nama', widget=forms.TextInput(
        attrs={'id': 'register-nama', 'placeholder': 'Name'}))
    email = forms.CharField(label='email', widget=forms.EmailInput(
        attrs={'id': 'register-email', 'placeholder': 'Email'}))
    negara = forms.CharField(label='negara', widget=forms.TextInput(
        attrs={'id': 'register-negara', 'placeholder': 'Negara'}))
