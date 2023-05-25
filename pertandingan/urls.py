from django.urls import path
from pertandingan.views import *

app_name = 'pertandingan'

urlpatterns = [
    path('', show_list_event, name='show-pertandingan'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/', pertandingan, name='show-pertandingan-quarter'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/perempat-final/', show_pertandingan_seperempat_final, name='show-pertandingan-r32'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/semi-final/', show_pertandingan_semifinal, name='show-pertandingan-semifinal'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/final/', show_pertandingan_final, name='show-pertandingan-final'),
]


