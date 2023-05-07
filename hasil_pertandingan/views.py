from django.shortcuts import render


def hasil_pertandingan(request):
    return render(request, 'hasil_pertandingan.html')

def detail_hasil_pertandingan(request):
    return render(request, 'detail_hasil_pertandingan.html')
