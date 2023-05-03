from django.urls import path
from authentication.views import *

app_name = 'authentication'

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register')
]