from django.db import connection


def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def show_enrolled_event(nama):
    id_atlet = search_id_atlet(nama)

    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT EXISTS(
                    SELECT 1 FROM peserta_kompetisi WHERE id_atlet_kualifikasi = '{id_atlet}') AS cek_peserta_kompetisi;
                    ''')
    peserta_kompetisi = cursor.fetchall()[0][0]
        
    if peserta_kompetisi is True:
        nomor_peserta = search_nomor_peserta(id_atlet)
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute( f'''SELECT * FROM peserta_mendaftar_event P
                            JOIN event E ON P.nama_event = E.nama_event AND P.tahun = E.tahun
                            WHERE P.nomor_peserta = {nomor_peserta};
                        ''')
        result = parse(cursor)
        return result

def search_id_atlet(nama):    
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT id FROM MEMBER WHERE nama = '{nama}';''')
    id_atlet = cursor.fetchall()[0][0]
    return id_atlet

def search_nomor_peserta(id_atlet):
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT nomor_peserta
        FROM PESERTA_KOMPETISI
        WHERE id_atlet_kualifikasi = '{id_atlet}';
        ''')
    nomor_peserta = cursor.fetchall()[0][0]
    return nomor_peserta

def unenroll_event(nama_atlet, nama_event, tahun_event):
    nomor_peserta = search_nomor_peserta(nama_atlet)
    error = ''

    try:
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(f'''DELETE FROM PESERTA_MENDAFTAR_EVENT WHERE nomor_peserta = {nomor_peserta} AND nama_event = '{nama_event}' AND tahun = '{tahun_event}';''')
        connection.commit()
        
    except Exception as e:
        error += str(e).split('.')[0]

    return error
    
