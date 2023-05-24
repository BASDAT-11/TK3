from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from list_event.query import SQLlistevent

# Create your views here.

def show_list_event(request):
    if request.session['user']['role'] =='umpire':
        list_event = SQLlistevent()
    else:
        return HttpResponseRedirect(reverse("authentication:user_login"))

    context = {
        'list_event' : list_event
    }
    return render(request, "list_pertandingan.html", context)

def pertandingan(request, key):
    if request.method == 'POST':
        print(request.POST)
        if 'All England-2022-WS-WS' in request.POST:
            print('AYO')
        return render(request, 'pertandingan.html')
    

    return render(request, 'pertandingan.html')

def hasil_pertandingan(request, key):
    try:
        if request.method == 'POST':
            pass
    except KeyError:
        pass

'''@login_required(login_url='/login/')
@csrf_exempt
def get_likes(request, key):
    if request.method == 'GET':
        post = PostTech.objects.get(pk=key).likes.all()
        is_like = False
        for like in post:
            if like == request.user:
                is_like = True
                break
        return JsonResponse({
            'error': False, 
            'likes_count': len(post),
            'is_liked': is_like,
        })
    return HttpResponseBadRequest("Bad request")'''