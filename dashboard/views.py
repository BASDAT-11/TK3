from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
# @login_required(login_url='/auth/login/')
def base_page(request):
    x = '''request.session['is_atlet'] = False
    request.session['is_pelatih'] = False
    request.session['is_umpire'] = False
    request.session['is_logged_out'] = False'''

    if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire'] :
        print('x')
        return redirect('dashboard/')
        
    return HttpResponseRedirect(reverse("authentication:user_login"))

def dashboard_page(request):
    if not(request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire']):
        return HttpResponseRedirect(reverse("authentication:user_login"))
    return render(request, 'dashboard.html')


