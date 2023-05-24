from django.urls import path
from pertandingan.views import *

app_name = 'pertandingan'

urlpatterns = [
    path('<str:key>/', pertandingan, name='pertandingan'),
]


