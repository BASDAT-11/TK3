from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

def daftar_atlet(request):
    if request.method == "POST":
        return redirect("daftar:list_atlet")
    return render(request, 'daftar_atlet.html')

def daftar_event(request):
    return render(request, 'daftar_event.html')

def list_atlet(request):
    return render(request, 'list_atlet.html')

def event_per_stadium(request):
    return render(request, 'daftar_per_stadium.html')

def pilihan_kategori(request):
    return render(request, 'pilih_kategori.html')