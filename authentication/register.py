import uuid

from psycopg2 import InternalError

from authentication.query import SQLRegisterAtlet, SQLRegisterMember, SQLRegisterPelatih


def atlet_register(nama, email, negara, tanggal_lahir, play_right, tinggi_badan, jenis_kelamin):
    try:
        id = uuid.uuid4()
        SQLRegisterMember(id, nama, email)
        SQLRegisterAtlet(id, tanggal_lahir, negara,
                         play_right, tinggi_badan, 0, jenis_kelamin)
    except InternalError as e:
        return {
            'success': False,
            'message': str(e.args)
        }
    else:
        return {
            'success': True,
        }
    
def pelatih_register(nama, email, tanggal_mulai):
    try:
        id = uuid.uuid4()
        SQLRegisterMember(id, nama, email)
        SQLRegisterPelatih(id, tanggal_mulai)
    except InternalError as e:
        return {
            'success': False,
            'message': str(e.args)
        }
    else:
        return {
            'success': True,
        }
    
def umpire_register(nama, email, tanggal_mulai):
    try:
        id = uuid.uuid4()
        SQLRegisterMember(id, nama, email)
        SQLRegisterPelatih(id, tanggal_mulai)
    except InternalError as e:
        return {
            'success': False,
            'message': str(e.args)
        }
    else:
        return {
            'success': True,
        }
