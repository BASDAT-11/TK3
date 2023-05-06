from django.urls import path
from hasil_pertandingan.views import *

app_name = 'hasil_pertandingan'

urlpatterns = [
    path('', hasil_pertandingan, name='hasil-pertandingan'),
]