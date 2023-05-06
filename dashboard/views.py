from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='/auth/login/')
def base_page(request):
    request.session['is_atlet'] = False
    request.session['is_pelatih'] = False
    request.session['is_umpire'] = True
    if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire'] :
        return redirect('dashboard/')
    return render(request, 'index.html')

def dashboard_page(request):
    return render(request, 'dashboard.html')


