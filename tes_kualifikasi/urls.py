from django.urls import path
from tes_kualifikasi.views import *

app_name = 'tes_kualifikasi'

urlpatterns = [
    path('', tes_kualifikasi, name='tes-kualifikasi'),
    path('soal/', soal_tes_kualifikasi, name='soal-tes-kualifikasi'),
]