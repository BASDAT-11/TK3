from django.shortcuts import render

def hasil_pertandingan(request):
    return render(request, 'hasil_pertandingan.html')
