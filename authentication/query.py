#SQL QUERY
from django.db import connection, DatabaseError

# Fetch function
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]



def SQLlogin(nama, email):
    query =  f'''SELECT M.id, M.nama, M.email,
        CASE
        WHEN A.play_right IS NULL AND P.tanggal_mulai IS NULL
        THEN 'umpire'
        WHEN P.tanggal_mulai IS NOT NULL
        THEN 'pelatih'
        WHEN A.play_right IS NOT NULL
        THEN 'atlet'
        ELSE NULL
        END AS role

        FROM MEMBER M
        FULL OUTER JOIN ATLET A ON M.id = A.id
        FULL OUTER JOIN PELATIH P ON M.id = P.id
        FULL OUTER JOIN UMPIRE U ON M.id = U.id
        
        WHERE M.nama = '{nama}' AND M.email = '{email}';
        '''
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def SQLRegisterMember(id, nama, email):
    try:
        query =  f'''INSERT INTO MEMBER (id, nama, email)
            VALUES ('{id}', '{nama}', '{email}');
            '''
                
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(query)
        
        connection.commit()
        connection.close()
    
    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }


def SQLRegisterAtlet(id, tgl_lahir, negara_asal, play_right, height, world_rank, jenis_kelamin):
    try:
        query =  f'''INSERT INTO ATLET (id, tgl_lahir, negara_asal, play_right, height, world_rank, jenis_kelamin)
            VALUES ('{id}', '{tgl_lahir}', '{negara_asal}', '{play_right}', '{height}', '{world_rank}', '{jenis_kelamin}');
            '''
                
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(query)

        connection.commit()
        connection.close()

    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }



def SQLRegisterPelatih(id, tanggal_mulai, negara):
    try:
        query =  f'''INSERT INTO PELATIH (id, tanggal_mulai, negara)
            VALUES ('{id}', '{tanggal_mulai}', '{negara}');
            '''
                
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(query)
        
        connection.commit()
        connection.close()
    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }

def SQLRegisterSpesialisasi(id, kategori):
    for item in kategori:
        print(item)
        print(type(item))
        
        query =  f'''INSERT INTO PELATIH_SPESIALISASI (id_pelatih, id_spesialisasi)
            SELECT '{id}', S.id
            FROM SPESIALISASI S, PELATIH P
            WHERE S.spesialisasi = '{item}'
            AND P.id = '{id}';
            '''
                
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(query)
    
        connection.commit()
        connection.close()

def SQLRegisterUmpire(id, negara):
    try:
        query =  '''INSERT INTO UMPIRE (id, negara)
            VALUES (%s, %s);
            '''
                
        cursor = connection.cursor()
        cursor.execute("set search_path to babadu;")
        cursor.execute(query, (id, negara))
        
        connection.commit()
        connection.close()
    except DatabaseError as d:
        return {
            'success': False,
            'message': str(d)
        }

x = f'''
    CREATE OR REPLACE FUNCTION check_email()
    RETURNS trigger AS
    $$
    BEGIN
    IF (NEW.email = (SELECT email FROM MEMBER WHERE email = NEW.email))
    THEN
    RAISE EXCEPTION 'Email % telah terdaftar', NEW.email;
    END IF;
    RETURN NEW.email;
    END;
    $$
    LANGUAGE plpgsql;

    CREATE TRIGGER check_mail
    BEFORE INSERT OR UPDATE OF email
    ON MEMBER
    FOR EACH ROW EXECUTE PROCEDURE check_email();

    INSERT INTO MEMBER (id, nama, email)
    VALUES ('de1f98a1-3c74-4c39-95aa-c821b2c2e7ba', 'Tove Gaughan', 'tgaughanp@cafepress.com');
'''



