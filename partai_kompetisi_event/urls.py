from django.urls import path
from partai_kompetisi_event.views import show_partai_kompetisi_event

urlpatterns = [
    path('', show_partai_kompetisi_event, name='show_partai_kompetisi_event'),
]