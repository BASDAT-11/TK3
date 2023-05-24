from daftar_sponsor.views import show_daftar_sponsor
from django.urls import path

app_name = 'daftar_sponsor'

urlpatterns = [
    path('', show_daftar_sponsor, name='show_daftar_sponsor'),
]