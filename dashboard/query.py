#SQL QUERY
from uuid import UUID
from django.db import connection

# Fetch function
def parse(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def SQLprofileAtlet(id):
    id = UUID(id)
    query =  f'''SELECT *
        FROM MEMBER M, ATLET A
        WHERE M.id = '{id}' AND M.id = A.id;
        '''
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def SQLprofilePelatih(id):
    id = UUID(id)
    query =  f'''SELECT *
        FROM MEMBER M, PELATIH P
        
        WHERE M.id = {id} AND M.id = P.id;
        '''
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res

def SQLprofileUmpire(id):
    id = UUID(id)
    query =  f'''SELECT *
        FROM MEMBER M, UMPIRE U
        
        WHERE M.id = {id} AND M.id = U.id;
        '''
             
    cursor = connection.cursor()
    cursor.execute("set search_path to babadu;")
    cursor.execute(query)
    res = parse(cursor)
    return res