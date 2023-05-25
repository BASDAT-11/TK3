from django.urls import path
from daftar_sponsor.views import show_daftar_sponsor, show_list_sponsor

app_name = 'daftar_sponsor'

urlpatterns = [
    path('', show_daftar_sponsor, name='show_daftar_sponsor'),
    path('list_sponsor/', show_list_sponsor, name='show_list_sponsor'),
]