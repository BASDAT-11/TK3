from datetime import date, datetime
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from list_event.views import slugify
from django.views.decorators.csrf import csrf_exempt

from pertandingan.forms import SkorFormFinal, SkorFormQuarter, SkorFormR16, SkorFormR32, SkorFormSemi
from pertandingan.forms import ScoreForm
from pertandingan.query import SQLfilter, SQLlistevent, cari_atlet_ganda, cari_atlet_tunggal, final, insert_match, insert_peserta_match, perempat_final, semi_final,show_perempatfinal

# Create your views here.

def show_list_event(request):
    if request.session['user']['role'] =='umpire':
        list_event = SQLlistevent()
        events = []
        for item in list_event:
            events.append((item, f"{slugify(item['nama_event'])}/{item['tahun']}/{slugify(item['jenis_partai'])}/perempat-final/"))
    else:
        return HttpResponseRedirect(reverse("authentication:user_login"))

    context = {
        'list_event' : events
    }
    return render(request, "list_pertandingan.html", context)

def pertandingan(request, event, tahun, jenis_partai):
    return render(request, 'list_pertandingan.html')

@csrf_exempt
def show_pertandingan_seperempat_final(request, event, tahun, jenis_partai):
    atlet = perempat_final(event, tahun)
    nama_event = (event.replace('-', ' ')).title()
    id_umpire = request.session['user']['id']
    extracted = []
    for item in atlet:
        if item['role'] == 'tunggal':
            new_data = cari_atlet_tunggal(str(item['id_atlet_kualifikasi']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)
        else:
            new_data = cari_atlet_ganda(str(item['id_atlet_ganda']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)

    jumlah_peserta = len(extracted)

    scoring_stuff = []

    for i in range(0, jumlah_peserta, 2):
        prefix = f"{extracted[i]['nomor_peserta']}-{extracted[i+1]['nomor_peserta']}"
        scoring_form = ScoreForm(request.POST or None, prefix=prefix)
        scoring_stuff.append((prefix, extracted[i], extracted[i+1], scoring_form))
        
    if request.method == 'POST':
        winner_with_score = []
        insert_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), 100, nama_event, tahun, id_umpire)
        for i in range(0, int(jumlah_peserta/2)):
            form = scoring_stuff[i][3]
            if form.is_valid():
                score_kiri = form.cleaned_data['atlet_score_kiri']
                score_kanan = form.cleaned_data['atlet_score_kanan']
                teams = form.prefix.split('-')
                if score_kiri > score_kanan:
                    winner_with_score.append((teams[0], score_kiri))
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], True)
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], False)
                else:
                    winner_with_score.append((teams[1], score_kanan))
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], True)
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], False)

        print(winner_with_score)   
        return redirect(f'''/pertandingan/{event}/{tahun}/{jenis_partai}/semi-final/''')

    context = {
        'content': scoring_stuff
    }

    return render(request, 'show_pertandingan_seperempat_final.html', context)

@csrf_exempt
def show_pertandingan_semifinal(request, event, tahun, jenis_partai):
    atlet = semi_final(event, tahun)
    nama_event = (event.replace('-', ' ')).title()
    id_umpire = request.session['user']['id']
    extracted = []
    for item in atlet:
        if item['role'] == 'tunggal':
            new_data = cari_atlet_tunggal(str(item['id_atlet_kualifikasi']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)
        else:
            new_data = cari_atlet_ganda(str(item['id_atlet_ganda']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)

    jumlah_peserta = len(extracted)

    scoring_stuff = []

    for i in range(0, jumlah_peserta, 2):
        prefix = f"{extracted[i]['nomor_peserta']}-{extracted[i+1]['nomor_peserta']}"
        scoring_form = ScoreForm(request.POST or None, prefix=prefix)
        scoring_stuff.append((prefix, extracted[i], extracted[i+1], scoring_form))
        
    if request.method == 'POST':
        winner_with_score = []
        insert_match('Semi final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), 100, nama_event, tahun, id_umpire)
        for i in range(0, int(jumlah_peserta/2)):
            form = scoring_stuff[i][3]
            if form.is_valid():
                score_kiri = form.cleaned_data['atlet_score_kiri']
                score_kanan = form.cleaned_data['atlet_score_kanan']
                teams = form.prefix.split('-')
                if score_kiri > score_kanan:
                    winner_with_score.append((teams[0], score_kiri))
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], True)
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], False)
                else:
                    winner_with_score.append((teams[1], score_kanan))
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], True)
                    insert_peserta_match('Perempat final', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], False)

        print(winner_with_score)   
        return redirect(f'''/pertandingan/{event}/{tahun}/{jenis_partai}/semi-final/''')

    context = {
        'content': scoring_stuff
    }

    return render(request, 'show_pertandingan_semifinal.html', context)

@csrf_exempt
def show_pertandingan_semifinal(request, event, tahun, jenis_partai):
    atlet = semi_final(event, tahun)
    extracted = []
    for item in atlet:
        if item['role'] == 'tunggal':
            new_data = cari_atlet_tunggal(str(item['id_atlet_kualifikasi']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)
        else:
            new_data = cari_atlet_ganda(str(item['id_atlet_ganda']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)

    jumlah_peserta = len(extracted)

    scoring_stuff = []

    for i in range(0, jumlah_peserta, 2):
        prefix = f"{extracted[i]['nomor_peserta']}-{extracted[i+1]['nomor_peserta']}"
        scoring_form = ScoreForm(request.POST or None, prefix=prefix)
        scoring_stuff.append((prefix, extracted[i], extracted[i+1], scoring_form))
        
    if request.method == 'POST':
        winner_with_score = []
        for i in range(0, int(jumlah_peserta/2)):
            form = scoring_stuff[i][3]
            if form.is_valid():
                score_kiri = form.cleaned_data['atlet_score_kiri']
                score_kanan = form.cleaned_data['atlet_score_kanan']
                teams = form.prefix.split('-')
                if score_kiri > score_kanan:
                    winner_with_score.append((teams[0], score_kiri))
                else:
                    winner_with_score.append((teams[1], score_kanan))

        print(winner_with_score)   
        return redirect(f'''/pertandingan/{event}/{tahun}/{jenis_partai}/final/''')
    
    context = {
        'content': scoring_stuff
    }

    return render(request, 'show_pertandingan_semifinal.html', context)

@csrf_exempt
def show_pertandingan_final(request, event, tahun, jenis_partai):
    atlet = final(event, tahun)
    nama_event = (event.replace('-', ' ')).title()
    id_umpire = request.session['user']['id']
    extracted = []
    for item in atlet:
        if item['role'] == 'tunggal':
            new_data = cari_atlet_tunggal(str(item['id_atlet_kualifikasi']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)
        else:
            new_data = cari_atlet_ganda(str(item['id_atlet_ganda']))
            new_data = new_data[0]
            new_data['nomor_peserta'] = item['nomor_peserta']
            extracted.append(new_data)

    jumlah_peserta = len(extracted)

    scoring_stuff = []

    for i in range(0, jumlah_peserta, 2):
        prefix = f"{extracted[i]['nomor_peserta']}-{extracted[i+1]['nomor_peserta']}"
        scoring_form = ScoreForm(request.POST or None, prefix=prefix)
        scoring_stuff.append((prefix, extracted[i], extracted[i+1], scoring_form))
        
    if request.method == 'POST':
        winner_with_score = []
        insert_match('Juara 3', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), 100, nama_event, tahun, id_umpire)
        insert_match('Juara 1', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), 100, nama_event, tahun, id_umpire)
        for i in range(0, int(jumlah_peserta/2)):
            form = scoring_stuff[i][3]
            if form.is_valid():
                score_kiri = form.cleaned_data['atlet_score_kiri']
                score_kanan = form.cleaned_data['atlet_score_kanan']
                teams = form.prefix.split('-')
                if score_kiri > score_kanan:
                    winner_with_score.append((teams[0], score_kiri))
                    insert_peserta_match('Juara 3', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], True)
                    insert_peserta_match('Juara 3', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], False)
                else:
                    winner_with_score.append((teams[1], score_kanan))
                    insert_peserta_match('Juara 1', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[1], True)
                    insert_peserta_match('Juara 1', date.today().strftime("%Y/%m/%d"), datetime.now().strftime("%H:%M:%S"), teams[0], False)

        print(winner_with_score)   
        return redirect(f'''/pertandingan/''')

    context = {
        'content': scoring_stuff
    }

    return render(request, 'show_pertandingan_final.html', context)

