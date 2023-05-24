from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import connection

# Create your views here.
# @login_required(login_url='/auth/login/')

# Email Umpire: eshaweln@ihg.com
# Email Pelatih: mbaribal8@hhs.gov
# Email Atlet: cpollard5@berkeley.edu

def dashboard_page(request):
    cursor = connection.cursor()
    cursor.execute("SET SEARCH_PATH TO babadu")
    email = 'cpollard5@berkeley.edu'
    cursor.execute("SELECT * FROM member WHERE email = %s", [email]) 
    result = cursor.fetchone()
    nama = result[1]
    email_member = result[2]

    if request.session['is_atlet']:
        cursor.execute("SELECT * FROM ATLET WHERE id = %s", [result[0]])
        result_atlet = cursor.fetchone()
        negara=result_atlet[2]
        tanggal_lahir = result_atlet[1]
        play = ''
        if result_atlet[3] == True:
            play = 'Right Hand'
        else:
            play = 'Left Hand'
        
        tinggi_badan = result_atlet[4]

        jenis_kelamin = ''
        if result_atlet[6] == True:
            jenis_kelamin = 'Putra'
        else:
            jenis_kelamin = 'Putri'

        context = {
            'nama': nama,
            'negara': negara,
            'email_member': email_member,
            'tanggal_lahir':tanggal_lahir,
            'play': play,
            'tinggi_badan':tinggi_badan,
            'jenis_kelamin':jenis_kelamin,
            'pelatih': '-',
            'status':'-',
            'world_rank':'-',
            'total_poin': '-'
        }
        return render (request, 'dashboard.html', context)

    elif request.session['is_pelatih']:
        cursor.execute("SELECT * FROM PELATIH WHERE id = %s", [result[0]])
        result_pelatih = cursor.fetchone()
        tanggal_mulai = result_pelatih[1]

        cursor.execute("SELECT id_spesialisasi FROM pelatih_spesialisasi WHERE id_pelatih = %s", [result[0]])
        pelatih_spesialisasi = cursor.fetchone()

        cursor.execute("SELECT spesialisasi FROM SPESIALISASI WHERE id = %s", [pelatih_spesialisasi])
        res_spesialiasi = cursor.fetchone()
        spesialisasi = res_spesialiasi[0]
        

        context = {
            'nama': nama,
            'email_member': email_member,
            'spesialisasi': spesialisasi,
            'tanggal_mulai': tanggal_mulai,
        }
        return render (request, 'dashboard.html', context)

    elif request.session['is_umpire']:
        cursor.execute("SELECT * FROM UMPIRE WHERE id = %s", [result[0]])
        result_umpire = cursor.fetchone()
        negara = result_umpire[1]
        context = {
            'nama': nama,
            'negara': negara,
            'email_member': email_member,
        }
        return render (request, 'dashboard.html', context)
    
def base_page(request):
    request.session['is_atlet'] = True
    request.session['is_pelatih'] = False
    request.session['is_umpire'] = False
    if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire'] :
        return redirect('dashboard/')
    return render(request, 'index.html')

# def dashboard_page(request):
#     return render(request, 'dashboard.html')