from datetime import datetime

from daftar_sponsor.query import *
from django.shortcuts import *
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def show_daftar_sponsor(request):
    pilihan_sponsor_tersedia = pilihan_sponsor(request.session['user']['nama'])

    if request.method == 'POST':
        nama_brand = request.POST['sponsor']
        tgl_mulai = request.POST['mulai']
        tgl_selesai = request.POST['selesai']

        if (nama_brand and tgl_mulai and tgl_selesai):
            daftar_sponsor(request.session['user']['nama'], nama_brand, tgl_mulai, tgl_selesai)
            return redirect('list_sponsor/')
        else:
            error = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu!"
            return render(request, "daftar_sponsor.html", {'pilihan_sponsor_tersedia' : pilihan_sponsor_tersedia, 'error': error})
        
    return render(request, "daftar_sponsor.html", {'pilihan_sponsor_tersedia' : pilihan_sponsor_tersedia})

def show_list_sponsor(request):
    daftar_list_sponsor = list_sponsor(request.session['user']['nama'])
    return render(request, "list_sponsor.html", {'daftar_list_sponsor' : daftar_list_sponsor})