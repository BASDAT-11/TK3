from django.db import connection


def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def show_partai_kompetisi_event(nama):
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
        cursor.execute(f'''SELECT E.Nama_Event, E.Tahun, E.Nama_Stadium, PK.Jenis_Partai, E.Kategori_Superseries, E.Tgl_Mulai, E.Tgl_Selesai
                    FROM PARTAI_PESERTA_KOMPETISI PK
                    JOIN EVENT E ON PK.Nama_Event = E.Nama_Event AND PK.Tahun_Event = E.Tahun
                    WHERE PK.nomor_peserta = {nomor_peserta};
            ''')
        result = parse(cursor)
        return result

def search_id_atlet(nama):    
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(f'''SELECT ID FROM MEMBER WHERE Nama = '{nama}';''')
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