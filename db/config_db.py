import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def add_meter(conn, meter):
    """
    Create a new meter into the meters table
    :param conn:
    :param meter:
    :return: meter id
    """
    sql = """ INSERT INTO meter(name, fid, shape, point_x, point_y, point_z, point_m, request, hab) VALUES(?,?,?,?,?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, meter)
    conn.commit()
    return cur.lastrowid


def add_record(conn, record):
    """
    Create a new record
    :param conn:
    :param record:
    :return:
    """

    sql = """ INSERT INTO record (user, consumption, date, mount, meter_id) VALUES(?,?,?,?,?) """
    cur = conn.cursor()
    cur.execute(sql, record)
    conn.commit()

    return cur.lastrowid


def select_all_meter(conn):
    """
    Query all rows in the meter table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM meter")

    rows = cur.fetchall()

    return rows


def select_all_record(conn):
    """
    Query all rows in the record table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM record")

    rows = cur.fetchall()

    return rows


def select_meter_by_id(conn, id):
    """
    Query meter by id
    :param conn: the Connection object
    :param id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM meter WHERE id=?", (id,))

    row = cur.fetchone()

    return row

def select_record_by_id(conn, id):
    """
    Query record by id
    :param conn: the Connection object
    :param id:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM record WHERE id=?", (id,))

    row = cur.fetchone()

    return row


def init_db():
    database = r"./db/fluvio.db"

    sql_create_meter_table = """ CREATE TABLE IF NOT EXISTS meter (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        fid integer,
                                        shape text,
                                        point_x text,
                                        point_y text,
                                        point_z text,
                                        point_m text,
                                        request float,
                                        hab integer ); """

    sql_create_record_table = """CREATE TABLE IF NOT EXISTS record (
                                    id integer PRIMARY KEY,
                                    user text NOT NULL,
                                    consumption integer,
                                    date text NOT NULL,
                                    mount text NOT NULL,
                                    meter_id integer NOT NULL,
                                    FOREIGN KEY (meter_id) REFERENCES meter (id));"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_meter_table)

        # create record table
        create_table(conn, sql_create_record_table)
    else:
        print("Error! cannot create the database connection.")
