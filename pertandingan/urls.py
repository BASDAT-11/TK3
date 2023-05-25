from django.urls import path
from pertandingan.views import *

app_name = 'pertandingan'

urlpatterns = [
    # path('<str:key>/', pertandingan, name='pertandingan'),
    path('save/<str:key>/', save_quarter, name='save_quarter'),
    # path('save/<:key>/', save_quarter, name='save_quarter'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/', show_pertandingan_v2, name='show-pertandingan'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/semi-final/', show_pertandingan_semifinal, name='show-pertandingan-semifinal'),
    path('<slug:event>/<int:tahun>/<slug:jenis_partai>/final/', show_pertandingan_final, name='show-pertandingan-final'),
]


