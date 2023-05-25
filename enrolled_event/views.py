from django.contrib import messages
from django.shortcuts import *
from django.shortcuts import redirect
from django.urls import reverse
from enrolled_event.query import *


def show_enrolled_event(request):
    nama = request.session['user']['nama']
    daftar_enrolled_event = show_enrolled_event(nama)
    messages.get_messages(request)

    if daftar_enrolled_event != None:
        return render(request, "enrolled_event.html", {'daftar_enrolled_event' : daftar_enrolled_event,})

    return render(request, "enrolled_event.html")
        

def unenroll(request, nama_event, tahun_event):
    nama_atlet = request.session['user']['nama']
    result = unenroll_event(nama_atlet, nama_event, tahun_event)
    if result != None:
        messages.error(request, result)
        return redirect('/enrolled_event')
    
    return redirect('/enrolled_event')
    