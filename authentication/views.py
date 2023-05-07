from django.shortcuts import render

def main_auth(request):
    return render(request, 'main_auth.html')

def user_login(request):
    nama = request.POST.get('nama')
    email = request.POST.get('email')
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

    

