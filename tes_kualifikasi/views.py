from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection

def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def tes_kualifikasi(request):
    return redirect('/dashboard/')

def soal_tes_kualifikasi(request):
    cursor = connection.cursor()
    context = request.session.get('my_context')
    
    cursor.execute('SELECT (SELECT MAX(world_rank) FROM ATLET_KUALIFIKASI) AS max_world_rank, (SELECT MAX(world_tour_rank) FROM ATLET_KUALIFIKASI) AS max_world_tour_rank;')
    atlet_kualifikasi= cursor.fetchone()

    result_tes = 0
    if request.method == 'POST':

        jawaban_soal1 = request.POST.get('default-radio-1')  # Mendapatkan jawaban soal 1 dari request
        jawaban_soal2 = request.POST.get('default-radio-2')  # Mendapatkan jawaban soal 2 dari request
        jawaban_soal3 = request.POST.get('default-radio-3')  # Mendapatkan jawaban soal 2 dari request
        jawaban_soal4 = request.POST.get('default-radio-4')  # Mendapatkan jawaban soal 2 dari request
        jawaban_soal5 = request.POST.get('default-radio-5')  # Mendapatkan jawaban soal 2 dari request

        # Proses jawaban dan bandingkan dengan jawaban yang benar
        if jawaban_soal1 == 'a':
            # Jawaban soal 1 benar
            # Lakukan operasi yang sesuai
            result_tes += 1
            

        if jawaban_soal2 == 'c':
            # Jawaban soal 2 benar
            # Lakukan operasi yang sesuai
            result_tes += 1
            
        if jawaban_soal3 == 'd':
            # Jawaban soal 2 benar
            # Lakukan operasi yang sesuai
            result_tes += 1
            
        if jawaban_soal4 == 'b':
            # Jawaban soal 2 benar
            # Lakukan operasi yang sesuai
            result_tes += 1
            
        if jawaban_soal5 == 'a':
            # Jawaban soal 2 benar
            # Lakukan operasi yang sesuai
            result_tes += 1


        email = request.session['user']['email']
        cursor.execute("SELECT id FROM MEMBER WHERE email=%s", (email,))
        id_atlet = cursor.fetchone()

        if result_tes >= 4:
            cursor.execute("INSERT INTO ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI (id_atlet, tahun, batch, tempat, tanggal, hasil_lulus) SELECT %s, %s, %s, %s, %s, %s WHERE NOT EXISTS (SELECT 1 FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI WHERE id_atlet = %s AND tahun = %s AND batch = %s AND tempat = %s AND tanggal = %s)",
               [id_atlet[0], context['tahun'], context['batch'], context['tempat'], context['tanggal'], True, id_atlet[0], context['tahun'], context['batch'], context['tempat'], context['tanggal']])

            
            cursor.execute("INSERT INTO ATLET_KUALIFIKASI (id_atlet, world_rank, world_tour_rank) SELECT %s, %s, %s WHERE NOT EXISTS (SELECT 1 FROM ATLET_KUALIFIKASI WHERE id_atlet = %s)", (id_atlet[0], atlet_kualifikasi[0]+1, atlet_kualifikasi[1]+1, id_atlet[0]))

        else:
            cursor.execute("INSERT INTO ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI (id_atlet, tahun, batch, tempat, tanggal, hasil_lulus) SELECT %s, %s, %s, %s, %s, %s WHERE NOT EXISTS (SELECT 1 FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI WHERE id_atlet = %s AND tahun = %s AND batch = %s AND tempat = %s AND tanggal = %s)",
               [id_atlet[0], context['tahun'], context['batch'], context['tempat'], context['tanggal'], False, id_atlet[0], context['tahun'], context['batch'], context['tempat'], context['tanggal']])

        
        cursor.execute('SELECT * FROM ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI')
        return redirect('/tes-kualifikasi/riwayat/')

    return render(request, 'soal_tes_kualifikasi.html')

def create_tes_kualifikasi(request):
    cursor = connection.cursor()
    if (request.method == 'POST'):
        if (request.POST['tahun'] == "" or request.POST['batch'] == "" or request.POST['tempat-pelaksanaan'] == '' or
            request.POST['tanggal-pelaksanaan'] == '' ):
            message = "Data yang diisikan belum lengkap, silahkan lengkapi data terlebih dahulu"
            return render (request, 'create_tes_kualifikasi.html', {'message':message})
        
        else:
            cursor.execute("INSERT INTO UJIAN_KUALIFIKASI VALUES (%s, %s, %s, %s)", 
                           [request.POST['tahun'], request.POST['batch'], request.POST['tempat-pelaksanaan'], request.POST['tanggal-pelaksanaan']])
            
            cursor.execute('SELECT * FROM UJIAN_KUALIFIKASI')
            result = parse(cursor)
                    
            return render(request, 'list_tes_kualifikasi.html', {'result': result, 'role': request.session['is_atlet']})
        
    return render(request, 'create_tes_kualifikasi.html')

def list_tes_kualifikasi(request):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM UJIAN_KUALIFIKASI')
    result = parse(cursor)

    if (request.method == 'POST'):
        tahun= request.POST['tahun']
        batch= request.POST['batch']
        tempat= request.POST['tempat']
        tanggal= request.POST['tanggal']

        context = {
            'tahun': tahun,
            'batch': batch,
            'tempat': tempat,
            'tanggal': tanggal
        }

        print(context)
        request.session['my_context'] = context
        return redirect('/tes-kualifikasi/soal/')
            
    return render(request, 'list_tes_kualifikasi.html', {'result': result, 'role': request.session['is_atlet']})

def riwayat_tes_kualifikasi(request):
    cursor = connection.cursor()
    cursor.execute('SELECT nama,tahun,batch,tempat,tanggal, hasil_lulus FROM MEMBER, ATLET_NONKUALIFIKASI_UJIAN_KUALIFIKASI WHERE id_atlet = id')
    result = parse(cursor)
    print (result)

    return render(request, 'riwayat_tes_kualifikasi.html', {'result': result, 'role': request.session['is_umpire']})