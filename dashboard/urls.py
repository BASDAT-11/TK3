from django.urls import path
from dashboard.views import *

app_name = 'dashboard'

urlpatterns = [
    path('', base_page, name='base'),
    path('dashboard/', dashboard_page, name='dashboard'),
]