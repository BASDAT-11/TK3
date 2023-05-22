from django.shortcuts import render
from django.db import connection

query = 'select * from atlet'
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

cursor = connection.cursor()
cursor.execute("set search_path to babadu;")
cursor.execute(query)
res = parse(cursor)

def main_auth(request):
    return render(request, 'main_auth.html')

def user_login(request):
    nama = request.POST.get('nama')
    email = request.POST.get('email')
    return render(request, 'login.html')

def user_register(request):
    return render(request, 'register.html')

    

