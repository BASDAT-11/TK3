from django.shortcuts import render

# Create your views here.
def pertandingan(request):
    return render(request, 'pertandingan.html')
