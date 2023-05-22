from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.db import connection
from authentication.forms import LoginForm

from authentication.query import SQLlogin


def main_auth(request):
    return render(request, 'main_auth.html')


def user_login(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')

        user = SQLlogin(nama, email)
        request.session['user'] = user

        if len(user) > 0:
            role = user[0]['role']

            if role == 'atlet':
                request.session['is_atlet'] = True
                request.session['is_pelatih'] = False
                request.session['is_umpire'] = False
            if role == 'pelatih':
                request.session['is_atlet'] = False
                request.session['is_pelatih'] = True
                request.session['is_umpire'] = False
            if role == 'umpire':
                request.session['is_atlet'] = False
                request.session['is_pelatih'] = False
                request.session['is_umpire'] = True

            if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire']:
                request.session['is_logged_in'] = True
                response = HttpResponseRedirect(reverse("dashboard:base"))
                return response
        else:
            messages.info(request, 'Username atau Email salah')

    context = {'login_form': LoginForm()}
    return render(request, 'login.html', context)


def user_register(request):
    return render(request, 'register.html')


def register_user(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')
        negara = request.POST.get('negara')
        if request.session['reg_atlet'] == 'atlet':
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            negara = request.POST.get('negara')
        elif request.session['reg_pelatih'] == 'pelatih':
            nama = request.POST.get('nama')
            email = request.POST.get('email')
            negara = request.POST.get('negara')
            nama = request.POST.get('nama')
            email = request.POST.get('email')

        is_user_already_exist = User.objects.filter(username=username).exists()
        if password_1 == password_2 and not is_user_already_exist:
            user = User.objects.create_user(
                username=username, password=password_2)
            if user is not None:
                user.save()
                return redirect('main:login')
            else:
                messages.info(request, 'Ops! something went wrong')
        elif password_1 != password_2:
            messages.info(request, 'Password doesnt match')
        elif is_user_already_exist:
            messages.info(request, 'User already exist')
        else:
            messages.info(request, 'Ops! something went wrong')
    form = {'register_form': RegisterForm()}
    return render(request, 'register.html', form)

