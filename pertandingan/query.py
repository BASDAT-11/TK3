# SQL QUERY
from django.db import connection, DatabaseError

# Fetch function


def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def SQLquarter(event, tahun, partai):
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
        
        WHERE E.nama_event = '{event}' AND E.tahun = '{tahun}' 
        AND PPK.jenis_partai = '{partai}'

        GROUP BY E.nama_event, E.tahun, E.nama_stadium,
        PPK.jenis_partai, E.kategori_superseries, E.tgl_mulai, E.tgl_selesai, 
        S.kapasitas;;
        '''
    

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
    query = f'''SELECT *
    FROM ATLET A, MEMBER M
    WHERE A.id = '{id}' AND A.id = M.id;'''
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res


def cari_atlet_ganda(id):
    query = f'''SELECT *
    FROM ATLET A, MEMBER M, ATLET_GANDA AG
    WHERE AG.id_atlet_ganda = '{id}' AND (AG.id_atlet_kualifikasi = A.id 
    OR AG.id_atlet_kualifikasi_2 = A.id) AND A.id = M.id;'''
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res
