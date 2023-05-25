from django.shortcuts import render, redirect
from django.db import connection
from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib import messages

#Function untuk parse  dlm bentuk json
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

# Create your views here.
from django.shortcuts import render

@transaction.atomic
def daftar_atlet(request):
    if request.session['user'] == None or request.session['is_pelatih'] == False:
         messages.warning(request, "Harus Login terlebih dahulu")
         return HttpResponseRedirect(reverse("authentication:user_login"))

    try:    
        user_id = request.session['user']['id']
        user_id = str(user_id)
        cursor = connection.cursor()
        command1 =  """
                        select * from atlet natural join member;
                    """
        cursor.execute(command1)
        list1 = parse(cursor)
        context = {"list": list1}
    except Exception as e:
        messages.error(request, e)

    if request.method == "POST":
        args = {'id_pelatih':user_id,
                'id_atlet':''}
        command2 =  """
                        insert into atlet_pelatih (id_pelatih, id_atlet)
                        values ('{id_pelatih}', '{id_atlet}');
                    """.format(**args)
        cursor.execute(command2)
        return redirect("daftar:list_atlet")
    return render(request, 'daftar_atlet.html', context)

@transaction.atomic
def daftar_event(request):
    if request.session['user'] == None or request.session['is_atlet'] == False:
        messages.warning(request, "Harus Login terlebih dahulu")
        return HttpResponseRedirect(reverse("authentication:user_login"))
    try:
        cursor = connection.cursor()
        command1 =  "select * from stadium;"
        cursor.execute(command1)
        list = parse(cursor)
        context = {"list": list}
    except Exception as e:
        messages.error(request, e)
    return render(request, 'daftar_event.html', context)

@transaction.atomic
def list_atlet(request):
    if request.session['user'] == None or request.session['is_pelatih'] == False:
        messages.warning(request, "Harus Login terlebih dahulu")
        return HttpResponseRedirect(reverse("authentication:user_login"))
    try:
        user_id = request.session['user']['id']
        user_id = str(user_id)
        cursor = connection.cursor()
        command1 =  """
                        select * from atlet_pelatih ap join atlet a on ap.id_atlet = a.id
                        join member m on a.id = m.id where ap.id_pelatih = '{}';
                    """.format(user_id)
        cursor.execute(command1)
        context = {"list": list}
        print(list)
    except Exception as e:
        messages.error(request, e)
    return render(request, 'list_atlet.html', context)

@transaction.atomic
def event_per_stadium(request, nama):
    try:
        cursor = connection.cursor()
        command1 =  """select * from event where nama_stadium = '{}' 
                    and tgl_mulai >= now();
                    """.format(nama)
        cursor.execute(command1)
        list = parse(cursor)
        print(list)
        context = {"list": list}
    except Exception as e:
        messages.error(request, e)
    return render(request, 'daftar_per_stadium.html', context)

@transaction.atomic
def pilihan_kategori(request, nama, tahun):
    if request.session['user'] == None or request.session['is_pelatih'] == False:
        messages.warning(request, "Harus Login terlebih dahulu")
        return HttpResponseRedirect(reverse("authentication:user_login"))
    try:
        user_id = request.session['user']['id']
        user_id = str(user_id)
        cursor = connection.cursor()
        command_event =  "select * from event where nama_event = '{}' and tahun = {};".format(nama, tahun)
        cursor.execute(command_event)
        event = parse(cursor)
        command_stadium =  "select * from event join nama on nama_event = nama where nama_event = '{}' and tahun = {};".format(nama, tahun)
        cursor.execute(command_stadium)
        stadium = parse(cursor)
        context = {"event": event, "stadium":stadium}
    except Exception as e:
        messages.error(request, e)
    return render(request, 'pilih_kategori.html')