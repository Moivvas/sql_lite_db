from sqlite3 import connect, Error
from contextlib import contextmanager


database = './hw6.db'

@contextmanager
def connection(db_file):
    conn = None
    try:
        conn = connect(db_file)
        yield conn
        conn.commit()
    except Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()
            