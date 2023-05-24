#SQL QUERY
from django.db import connection, DatabaseError

# Fetch function
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def SQLlistevent():
    query =  f'''SELECT E.nama_event, E.tahun, E.nama_stadium,
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