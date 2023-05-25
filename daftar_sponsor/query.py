#SQL QUERY
from uuid import UUID
from django.db import connection

# Fetch function
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def daftar_sponsor(nama_atlet, nama_sponsor, tgl_mulai, tgl_selesai):
    id_atlet = search_id_atlet(nama_atlet)
    id_sponsor = search_id_sponsor(nama_sponsor)
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute('''INSERT INTO ATLET_SPONSOR (id_atlet, id_sponsor, tgl_mulai, tgl_selesai) VALUES (%s, %s, %s, %s);
        ''', (id_atlet, id_sponsor, tgl_mulai, tgl_selesai))

    connection.commit()
    connection.close()

def pilihan_sponsor(nama):
    id_atlet = search_id_atlet(nama)
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT nama_brand FROM SPONSOR WHERE id NOT IN (SELECT id_sponsor FROM ATLET_SPONSOR WHERE id_atlet = '{id_atlet}');''')
    result = parse(cursor)
    return result
    
def list_sponsor(nama):
    id_atlet = search_id_atlet(nama)
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT  S.nama_brand, S.tgl_mulai, S.tgl_selesai
                    FROM SPONSOR S, ATLET_SPONSOR AS, ATLET A
                    WHERE S.id = AS.id_sponsor AND AS.id_atlet = A.id AND A.id = '{id_atlet}';''')
    result = parse(cursor)
    return result

def search_id_atlet(nama):    
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT id FROM MEMBER WHERE nama = '{nama}';''')
    id_atlet = cursor.fetchall()[0][0]
    return id_atlet

def search_id_sponsor(nama):  
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT id FROM SPONSOR WHERE nama_brand = '{nama}';''')
    id_sponsor = cursor.fetchall()[0]
    return id_sponsor
