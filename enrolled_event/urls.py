from django.urls import path
from enrolled_event.views import show_enrolled_event, unenroll

app_name = 'enrolled_event'

urlpatterns = [
    path('', show_enrolled_event, name='show_enrolled_event'),
    path('unenroll/<str:nama_event>/<str:tahun_event>/', unenroll, name='unenroll'),
]