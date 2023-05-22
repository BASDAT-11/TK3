#SQL QUERY
from django.db import connection

# Fetch function
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def SQLlogin(nama, email):
    query =  '''SELECT M.nama, M.email,
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
        
        WHERE M.nama =%s AND M.email =%s;
        '''
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query, (nama, email))
    res = parse(cursor)
    return res

def session_setter(request, role):
    if role == 'atlet':
        request.session['is_atlet'] = True
    if role == 'pelatih':
        request.session['is_pelatih'] = True
    if role == 'umpire': 
        request.session['is_umpire'] = True