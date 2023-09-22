from sqlite3 import Error
from connect_to_db import connection, database

def create_table(conn, create_table_sql):
    try:
        with conn:
            conn.execute(create_table_sql)
    except Error as e:
        print(e)

if __name__ == '__main__':
    table_definitions = [
        """DROP TABLE IF EXISTS [grades];""",
        """DROP TABLE IF EXISTS disciplines;""",
        """DROP TABLE IF EXISTS students;""",
        """DROP TABLE IF EXISTS teachers;"""
        """DROP TABLE IF EXISTS groups;""",
        """CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name STRING UNIQUE
        );""",
        """CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        fullname STRING
        );""",
        """CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        fullname STRING,
        group_id REFERENCES groups (id)
        );""",
        """CREATE TABLE IF NOT EXISTS disciplines (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name STRING,
        teacher_id REFERENCES teachers (id)
        );""",
        """CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        discipline_id REFERENCES disciplines (id),
        student_id REFERENCES students (id),
        grade INTEGER,
        date_of DATE
        );"""
    ]

    with connection(database) as conn:
        if conn:
            for table_definition in table_definitions:
                create_table(conn, table_definition)
        else:
            print("Error! cannot create the database connection.")
