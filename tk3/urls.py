"""
URL configuration for tk3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('auth/', include('authentication.urls')),
    path('pertandingan/', include('pertandingan.urls')),
    path('hasil-pertandingan/', include('hasil_pertandingan.urls')),
    path('enrolled_event/', include('enrolled_event.urls')),
    path('partai_kompetisi_event/', include('partai_kompetisi_event.urls')),
    path('daftar_sponsor/', include('daftar_sponsor.urls')),
    path('list_event/', include('list_event.urls')),
    path('daftar/', include('daftar.urls')),
    path('tes-kualifikasi/', include('tes_kualifikasi.urls')),
]
