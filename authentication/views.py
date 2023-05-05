from django.shortcuts import render

def user_login(request):
    nama = request.POST.get('nama')
    email = request.POST.get('email')
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

