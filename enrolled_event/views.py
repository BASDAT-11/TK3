from django.contrib import messages
from django.shortcuts import *
from django.shortcuts import redirect
from django.urls import reverse
from enrolled_event.query import *


def show_enrolled_event(request):
    daftar_enrolled_event = show_enrolled_event(request.session['user']['nama'])
    messages.get_messages(request)

    if daftar_enrolled_event != None:
        return render(request, "enrolled_event.html", {'daftar_enrolled_event' : daftar_enrolled_event,})

    return render(request, "enrolled_event.html")
        

def unenroll(request, nama_event, tahun_event):
    result = unenroll_event(request.session['user']['nama'], nama_event, tahun_event)
    if result != None:
        messages.error(request, result)
        return redirect('/enrolled_event')
    
    return redirect('/enrolled_event')
    