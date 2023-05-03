from django.urls import path
from dashboard.views import *

app_name = 'main'

urlpatterns = [
    path('', dashboard_page, name='dashboard'),
]