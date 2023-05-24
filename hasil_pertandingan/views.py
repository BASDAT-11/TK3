from django.shortcuts import render


def hasil_pertandingan(request):
    return render(request, 'hasil_pertandingan.html')

def detail_hasil_pertandingan(request):
    return render(request, 'detail_hasil_pertandingan.html')

def hasil_pertandingan(request):
    try:
        if request.method == 'POST':
            pass
    except KeyError:
        pass
