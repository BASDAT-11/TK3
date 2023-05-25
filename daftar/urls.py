from django.urls import path
from daftar.views import *

app_name = 'daftar'

urlpatterns = [
    path('atlet', daftar_atlet, name='daftar_atlet'),
    path('list_atlet', list_atlet, name='list_atlet'),
    path('event', daftar_event, name='daftar_event'),
    path('event_per_stadium/<str:nama>', event_per_stadium, name='event_per_stadium'),
    path('pilihan_kategori/<str:nama>/<int:tahun>/', pilihan_kategori, name='pilihan_kategori'),
]