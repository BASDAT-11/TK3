from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.db import connection

from authentication.query import SQLlogin

def main_auth(request):
    return render(request, 'main_auth.html')

def user_login(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        email = request.POST.get('email')

        user = SQLlogin(nama, email)

        if len(user) > 0:
            role = user[0]['role']
            if role == 'atlet':
                request.session['is_atlet'] = True
            if role == 'pelatih':
                request.session['is_pelatih'] = True
            if role == 'umpire': 
                request.session['is_umpire'] = True

            print(request.session['is_atlet'])
            print(request.session['is_pelatih'])
            print(request.session['is_umpire'])

            response = HttpResponseRedirect(reverse("dashboard:base"))
            return response
        else:
            messages.info(request,'Username atau Email salah')

    return render(request,'login.html')

def user_register(request):
    return render(request, 'register.html')


    

