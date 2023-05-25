from datetime import datetime

from daftar_sponsor.query import *
from django.shortcuts import *
from django.urls import reverse


def show_daftar_sponsor(request):
    nama_atlet = request.session['user']['nama']
    pilihan_sponsor_tersedia = pilihan_sponsor(nama_atlet)

    if request.method == 'POST':
        nama_brand = request.POST['sponsor']
        tgl_mulai = request.POST['mulai']
        tgl_selesai = request.POST['selesai']

        if (nama_brand and tgl_mulai and tgl_selesai):
            daftar_sponsor(nama_atlet, nama_brand, tgl_mulai, tgl_selesai)
            return redirect('list_sponsor/')
        else:
            error = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu!"
            return render(request, "daftar_sponsor.html", {'pilihan_sponsor_tersedia' : pilihan_sponsor_tersedia, 'error': error})
        
    return render(request, "daftar_sponsor.html", {'pilihan_sponsor_tersedia' : pilihan_sponsor_tersedia})

def show_list_sponsor(request):
    nama_atlet = request.session['user']['nama']
    daftar_list_sponsor = list_sponsor(nama_atlet)
    return render(request, "list_sponsor.html", {'daftar_list_sponsor' : daftar_list_sponsor})