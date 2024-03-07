import sqlite3
from db.config_db import init_db


if __name__ == '__main__':
    database_path = r"./db/fluvio.db"
    conn = sqlite3.connect(database_path)
    init_db()

    print("Conection Succesfull ... ")

    #TODO: Iniciar el proceso de llenado de la DB

    #TODO: Iniciar el proceso de calculos

    #TODO: Generar reportes --> de que forma? en que formato? 

