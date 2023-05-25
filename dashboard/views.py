import json
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import connection

from dashboard.query import SQLprofileAtlet, SQLprofilePelatih, SQLprofileUmpire
    
def base_page(request):
    if ('is_atlet' not in request.session) and ('is_pelatih' not in request.session) and ('is_umpire' not in request.session):
        return HttpResponseRedirect(reverse("authentication:main_auth"))
    if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire'] :
        print('x')
        return redirect('dashboard/')
        
    return HttpResponseRedirect(reverse("authentication:user_login"))

def dashboard_page(request):
    cursor = connection.cursor()
    user_logged_in = None
    if ('is_atlet' not in request.session) and ('is_pelatih' not in request.session) and ('is_umpire' not in request.session):
        return HttpResponseRedirect(reverse("authentication:main_auth"))
    if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire']:
        if request.session['user']['role'] =='atlet':
            user_logged_in = SQLprofileAtlet(request.session['user']['id'])
        elif request.session['user']['role'] =='pelatih':
            user_logged_in = SQLprofilePelatih(request.session['user']['id'])
        elif request.session['user']['role'] =='umpire':
            user_logged_in = SQLprofileUmpire(request.session['user']['id'])
        else:
            return HttpResponseRedirect(reverse("authentication:user_login"))
    else:
        return HttpResponseRedirect(reverse("authentication:user_login"))
    
    context = {
        'user_logged_in' : user_logged_in[0]
    }

    if (request.session['is_atlet']):
        email = request.session['user']['email']
        cursor.execute("SELECT id FROM MEMBER WHERE email=%s", (email,))
        id_atlet = cursor.fetchone()

        cursor.execute("INSERT INTO ATLET_NON_KUALIFIKASI (id_atlet) SELECT %s WHERE NOT EXISTS (SELECT 1 FROM ATLET_NON_KUALIFIKASI WHERE id_atlet = %s)", (id_atlet[0], id_atlet[0]))


    return render(request, 'dashboard.html', context)