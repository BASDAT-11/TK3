from datetime import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import *
from django.urls import reverse
from partai_kompetisi_event.query import *


def show_partai_kompetisi_event(request):
    daftar_partai_kompetisi_event = show_partai_kompetisi_event(request.session['user']['nama'])

    if daftar_partai_kompetisi_event != None:
        return render(request, "partai_kompetisi_event.html", {'daftar_partai_kompetisi_event':daftar_partai_kompetisi_event})
  
    return render(request, "partai_kompetisi_event.html")