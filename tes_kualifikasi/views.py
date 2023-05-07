from django.shortcuts import render

def tes_kualifikasi(request):
    return render(request, 'tes_kualifikasi.html')

def soal_tes_kualifikasi(request):
    return render(request, 'soal_tes_kualifikasi.html')
