from .database import get_table_object, db_session, engine
import hashlib


def db_query_list(table_name, row_params=None):
    table_obj = get_table_object(table_name)
    if row_params:
        rows = db_session.query(table_obj).filter_by(**row_params).all()
    else:
        rows = db_session.query(table_obj).all()
    return [row.get_dict() for row in rows]


def db_insert_new_row(table_name, row_params):
    con = engine.connect()
    sql = get_table_object(table_name).__table__.insert().values({**row_params})
    con.execute(sql)


def db_query_one(table_name, row_params):
    row = db_session.query(get_table_object(table_name)).filter_by(**row_params).first()
    return row.get_dict() if row else None


def db_update_row(table_name, row_id, row_params):
    table_obj = get_table_object(table_name)
    con = engine.connect()
    sql = table_obj.__table__.update().where(table_obj.id == row_id).values({**row_params})
    con.execute(sql)


def check_password(hashed_password, no_hashed_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha256(salt.encode() + no_hashed_password.encode()).hexdigest()
