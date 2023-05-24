from django.shortcuts import render

# Create your views here.
def pertandingan(request):
    return render(request, 'pertandingan.html')

def mulai_pertandingan(request, key):
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