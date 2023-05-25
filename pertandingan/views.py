from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

from pertandingan.forms import SkorFormQuarter, SkorFormSemi
from pertandingan.query import SQLquarter, show_perempatfinal

# Create your views here.


def pertandingan(request, key):
    url = key.split('-')
    quarter = SQLquarter(url[0], url[1], url[2])
    if quarter[0]['status_kapasitas'] == False:
        return HttpResponseRedirect(reverse("list_event:show_list_event"))
    else:
        all_data = show_perempatfinal(url[0], url[1])
    form = SkorFormQuarter(request.POST)
    print(form.errors)

    print(all_data)
    context = {
        'versus': all_data,
    }
    return render(request, 'pertandingan.html', context)


def show_pertandingan_v2(request, event, tahun, jenis_partai):
    if request.method == 'POST':
        print('mira gaalak')

        print('submit-quarter' in request.POST)
        if 'submit-quarter' in request.POST:
            form = SkorFormQuarter(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                skor_a = form.cleaned_data.get('skor_a')
                skor_b = form.cleaned_data.get('skor_b')
                skor_c = form.cleaned_data.get('skor_c')
                skor_d = form.cleaned_data.get('skor_d')
                skor_e = form.cleaned_data.get('skor_e')
                skor_f = form.cleaned_data.get('skor_f')
                skor_g = form.cleaned_data.get('skor_g')
                skor_h = form.cleaned_data.get('skor_h')
                print(skor_a, skor_b)
                print("pindah")

    context = {
        'skor_form' : SkorFormQuarter()
    }
    return render(request, 'pertandingan_v2.html', context)

def show_pertandingan_semifinal(request, event, tahun, jenis_partai):
    print("semifinal")
    print(request.method)
    if request.method == 'POST':
        print('submit-semi' in request.POST)
        if 'submit-semi' in request.POST:
            form = SkorFormSemi(request.POST)
            print("yuk bisa yuk")

            if form.is_valid():
                skor_a = form.cleaned_data.get('skor_a')
                skor_b = form.cleaned_data.get('skor_b')
                skor_c = form.cleaned_data.get('skor_c')
                skor_d = form.cleaned_data.get('skor_d')
                print(skor_a, skor_b)
                print('OKSEMI')
                return render(request, 'pertandingan_final.html')

    context = {
        'skor_form' : SkorFormSemi()
    }
    return render(request, 'pertandingan_semifinal.html', context)

def show_pertandingan_final(request, event, tahun, jenis_partai):
    if request.method == 'POST':
        if 'submit-final' in request.POST:
            form = SkorFormSemi(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                skor_a3 = form.cleaned_data.get('skor_a3')
                skor_b3 = form.cleaned_data.get('skor_b3')
                skor_a = form.cleaned_data.get('skor_a')
                skor_b = form.cleaned_data.get('skor_b')
                print(skor_a, skor_b)
                return redirect('final/')

    context = {
        'skor_form' : SkorFormSemi()
    }
    return render(request, 'pertandingan_semifinal.html', context)


'''def save_skor_form(request):
    if request.method == 'POST':
        print('kkk')
        print('mira gaalak')

        print('submit-quarter' in request.POST)
        if 'submit-quarter' in request.POST:
            form = SkorForm(request.POST)
            print(form.is_valid())
            print(form.errors)
            if form.is_valid():
                skor_a = form.cleaned_data.get('skor_a')
                skor_b = form.cleaned_data.get('skor_b')
                skor_c = form.cleaned_data.get('skor_c')
                skor_d = form.cleaned_data.get('skor_d')
                skor_e = form.cleaned_data.get('skor_e')
                skor_f = form.cleaned_data.get('skor_f')
                skor_g = form.cleaned_data.get('skor_g')
                skor_h = form.cleaned_data.get('skor_h')
                print(skor_a, skor_b)


    context = {
        'skor_form': SkorForm(request.POST)
    }

    return render(request, 'pertandingan_v2.html', context)'''


def save_quarter(request, key):
    form = SkorForm(request.POST)
    print(form.errors)
    if request.method == 'POST':
        print(form.errors)
        if "submit-quarter" in request.POST:
            print('XXX')
            if form.is_valid():
                skor_a = form.cleaned_data.get('skor_a')
                skor_b = form.cleaned_data.get('skor_b')
                skor_c = form.cleaned_data.get('skor_c')
                skor_d = form.cleaned_data.get('skor_d')
                skor_e = form.cleaned_data.get('skor_e')
                skor_f = form.cleaned_data.get('skor_f')
                skor_g = form.cleaned_data.get('skor_g')
                skor_h = form.cleaned_data.get('skor_h')
                print(skor_a, skor_b)
                return HttpResponseRedirect(reverse("list_event:show_list_event"))
    context = {
        'skor_form': SkorForm()
    }
    return render(request, 'pertandingan.html', context)

# def user_register(request):
#     url = key.split('-')
#     quarter = SQLquarter(url[0], url[1], url[2])
#     if quarter[0]['status_kapasitas'] == False:
#         return HttpResponseRedirect(reverse("list_event:show_list_event"))
#     else:
#         all_data = show_perempatfinal(url[0], url[1])


#     print(request.method)
#     if request.method == 'POST':
#         if "atlet-register" in request.POST:
#             form = SkorForm(request.POST)
#             if form.is_valid():
#                 nama = form.cleaned_data.get('nama')
#                 email = form.cleaned_data.get('email')
#                 negara = form.cleaned_data.get('negara')
#                 tanggal_lahir = form.cleaned_data.get('tanggal_lahir')
#                 play_right = form.cleaned_data.get('play_right')
#                 tinggi_badan = form.cleaned_data.get('tinggi_badan')
#                 jenis_kelamin = form.cleaned_data.get('jenis_kelamin')
#                 register = atlet_register(nama, email, negara, tanggal_lahir, play_right, tinggi_badan, jenis_kelamin)
#                 print(register)
#                 if register['success']:
#                     return HttpResponseRedirect(reverse("authentication:user_login"))
#                 else:
#                     messages.info(request,register['message'])

#     context = {
#         'atlet_form': AtletForm(),
#         'pelatih_form': PelatihForm(),
#         'umpire_form': UmpireForm(),
#     }
#     return render(request, 'register.html', context)

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
