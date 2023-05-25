from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from dashboard.query import SQLprofileAtlet

from list_event.query import SQLlistevent
import re

# Create your views here.

def show_list_event(request):
    if request.session['user']['role'] =='umpire':
        list_event = SQLlistevent()
        events = []
        for item in list_event:
            events.append((item, f"{slugify(item['nama_event'])}/{item['tahun']}/{slugify(item['jenis_partai'])}"))
    else:
        return HttpResponseRedirect(reverse("authentication:user_login"))

    context = {
        'list_event' : events
    }
    return render(request, "list_events.html", context)



def slugify(text):
    # Convert the text to lowercase
    slug = text.lower()
    # Replace non-alphanumeric characters with dashes
    slug = re.sub(r'[^a-zA-Z0-9-]', '-', slug)
    # Remove any leading or trailing dashes
    slug = slug.strip('-')
    # Replace multiple consecutive dashes with a single dash
    slug = re.sub(r'--+', '-', slug)
    return slug



# def dashboard_page(request):
#     user_logged_in = None
#     if request.session['is_atlet'] or request.session['is_pelatih'] or request.session['is_umpire']:
#         if request.session['user']['role'] =='atlet':
#             user_logged_in = SQLprofileAtlet(request.session['user']['id'])
#         elif request.session['user']['role'] =='pelatih':
#             user_logged_in = SQLprofilePelatih(request.session['user']['id'])
#         elif request.session['user']['role'] =='umpire':
#             user_logged_in = SQLprofileUmpire(request.session['user']['id'])
#         else:
#             return HttpResponseRedirect(reverse("authentication:user_login"))
#     else:
#         return HttpResponseRedirect(reverse("authentication:user_login"))

#     context = {
#         'user_logged_in' : user_logged_in[0]
#     }
#     print(context)
#     return render(request, 'dashboard.html', context)
