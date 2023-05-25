# SQL QUERY
from django.db import connection, DatabaseError


def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def SQLlistevent():
    query = f'''SELECT E.nama_event, E.tahun, E.nama_stadium,
        PPK.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai, 
        S.kapasitas, COUNT(PPK.nama_event) as kapasitas_terisi

        FROM PARTAI_PESERTA_KOMPETISI PPK 
        JOIN EVENT E ON PPK.nama_event = E.nama_event
        and PPK.tahun_event = E.tahun
        JOIN STADIUM S ON E.nama_stadium = S.nama
        GROUP BY E.nama_event, E.tahun, E.nama_stadium,
        PPK.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai, 
        S.kapasitas;
        
        '''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def SQLfilter(event, tahun, partai):
    event = event.replace('-', ' ')
    query = f'''SELECT E.nama_event, E.tahun, E.nama_stadium,
        PPK.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai, 
        S.kapasitas, COUNT(PPK.nama_event) as kapasitas_terisi,

       CASE
        WHEN S.kapasitas = COUNT(PPK.nama_event)
        THEN True
        ELSE True
        END AS status_kapasitas

        FROM PARTAI_PESERTA_KOMPETISI PPK 
        JOIN EVENT E ON PPK.nama_event = E.nama_event
        and PPK.tahun_event = E.tahun
        JOIN STADIUM S ON E.nama_stadium = S.nama
        
        WHERE LOWER(E.nama_event) = '{event}' AND E.tahun = '{tahun}' 
        AND LOWER(PPK.jenis_partai) = '{partai}'

        GROUP BY E.nama_event, E.tahun, E.nama_stadium,
        PPK.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai, 
        S.kapasitas;;
        '''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def count_competitors(event, tahun):
    query = f'''SELECT distinct PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasi,

        CASE
        WHEN PEK.id_atlet_ganda IS NULL
        THEN 'tunggal'
        WHEN PEK.id_atlet_kualifikasi IS NULL
        THEN 'ganda'
        ELSE NULL
        END AS role

        FROM PESERTA_KOMPETISI PEK
        JOIN PARTAI_PESERTA_KOMPETISI PPK ON
        PEK.nomor_peserta = PPK.nomor_peserta

        WHERE PPK.nama_event = '{event}' AND PPK.tahun_event = '{tahun}' 

        ORDER BY PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasI
        LIMIT 8;'''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def perempat_final(event, tahun):
    event = event.replace('-', ' ')
    query = f'''SELECT distinct PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasi,

        CASE
        WHEN PEK.id_atlet_ganda IS NULL
        THEN 'tunggal'
        WHEN PEK.id_atlet_kualifikasi IS NULL
        THEN 'ganda'
        ELSE NULL
        END AS role

        FROM PESERTA_KOMPETISI PEK
        JOIN PARTAI_PESERTA_KOMPETISI PPK ON
        PEK.nomor_peserta = PPK.nomor_peserta

        WHERE LOWER(PPK.nama_event) = '{event}' AND PPK.tahun_event = '{tahun}' 

        ORDER BY PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasI
        LIMIT 8;'''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def semi_final(event, tahun):
    event = event.replace('-', ' ')
    query = f'''SELECT distinct PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasi,

        CASE
        WHEN PEK.id_atlet_ganda IS NULL
        THEN 'tunggal'
        WHEN PEK.id_atlet_kualifikasi IS NULL
        THEN 'ganda'
        ELSE NULL
        END AS role

        FROM PESERTA_KOMPETISI PEK
        JOIN PARTAI_PESERTA_KOMPETISI PPK ON
        PEK.nomor_peserta = PPK.nomor_peserta

        WHERE LOWER(PPK.nama_event) = '{event}' AND PPK.tahun_event = '{tahun}' 

        ORDER BY PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasI
        LIMIT 4;'''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def final(event, tahun):
    event = event.replace('-', ' ')
    query = f'''SELECT distinct PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasi,

        CASE
        WHEN PEK.id_atlet_ganda IS NULL
        THEN 'tunggal'
        WHEN PEK.id_atlet_kualifikasi IS NULL
        THEN 'ganda'
        ELSE NULL
        END AS role

        FROM PESERTA_KOMPETISI PEK
        JOIN PARTAI_PESERTA_KOMPETISI PPK ON
        PEK.nomor_peserta = PPK.nomor_peserta

        WHERE LOWER(PPK.nama_event) = '{event}' AND PPK.tahun_event = '{tahun}' 

        ORDER BY PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasI
        LIMIT 4;'''
    
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res



def show_perempatfinal(event, tahun):
    query = f'''SELECT distinct PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasi,

        CASE
        WHEN PEK.id_atlet_ganda IS NULL
        THEN 'tunggal'
        WHEN PEK.id_atlet_kualifikasi IS NULL
        THEN 'ganda'
        ELSE NULL
        END AS role

        FROM PESERTA_KOMPETISI PEK
        JOIN PARTAI_PESERTA_KOMPETISI PPK ON
        PEK.nomor_peserta = PPK.nomor_peserta

        WHERE PPK.nama_event = '{event}' AND PPK.tahun_event = '{tahun}' 

        ORDER BY PPK.jenis_partai,PPK.nama_event, PPK.tahun_event, 
        PPK.nomor_peserta, PEK.id_atlet_ganda, PEK.id_atlet_kualifikasI
        LIMIT 8;'''

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def cari_atlet_tunggal(id):
    query = f'''SELECT M.nama, M.id
    FROM ATLET A, MEMBER M
    WHERE A.id = '{id}' AND A.id = M.id;'''
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def cari_atlet_ganda(id):
    query = f'''SELECT STRING_AGG(M.nama || ' ' || M.nama, ', ') as nama, AG.id_atlet_ganda as id
    FROM ATLET A
    JOIN MEMBER M ON A.id = M.id 
    JOIN ATLET_GANDA AG ON AG.id_atlet_kualifikasi = M.id
    OR AG.id_atlet_kualifikasi_2 = M.id 
    WHERE AG.id_atlet_ganda = '{id}' AND (AG.id_atlet_kualifikasi = A.id 
    OR AG.id_atlet_kualifikasi_2 = A.id) AND A.id = M.id
    group by id_atlet_ganda;'''
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def insert_match(jenis_babak, tanggal, waktu_mulai, total_durasi, nama_event, tahun_event, id_umpire):
    try:
        query = f'''INSERT INTO MATCH (jenis_babak, tanggal, waktu_mulai, total_durasi, nama_event, tahun_event, id_umpire)
            VALUES ('{jenis_babak}', '{tanggal}', '{waktu_mulai}', '{total_durasi}', '{nama_event}', '{tahun_event}', '{id_umpire}');
            '''
        
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        print(query)
        cursor.execute(query)

        connection.commit()
        connection.close()
    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }

def insert_peserta_match(jenis_babak, tanggal, waktu_mulai, nomor_peserta, status_menang):
    try:
        query = f'''INSERT INTO PESERTA_MENGIKUTI_MATCH (jenis_babak, tanggal, waktu_mulai, nomor_peserta, status_menang)
            VALUES ('{jenis_babak}', '{tanggal}', '{waktu_mulai}', '{nomor_peserta}', '{status_menang}');
            '''
        
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        print(query)
        cursor.execute(query)
        print(jenis_babak, tanggal, waktu_mulai, nomor_peserta, status_menang)

        connection.commit()
        connection.close()
    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }
