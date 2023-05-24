from django.urls import path
from tes_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('', tes_kualifikasi, name='tes-kualifikasi'),
    path('soal/', soal_tes_kualifikasi, name='soal-tes-kualifikasi'),

    path('create/', create_tes_kualifikasi, name='create-tes-kualifikasi'),
    path('list/', list_tes_kualifikasi, name='list-tes-kualifikasi'),
    path('riwayat/', riwayat_tes_kualifikasi, name='riwayat-tes-kualifikasi'),
]