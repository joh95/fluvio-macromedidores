import sqlite3
from db.config_db import init_db


if __name__ == '__main__':
    database_path = r"./db/fluvio.db"
    conn = sqlite3.connect(database_path)
    init_db()

    print("Conection Succesfull ... ")

    #TODO: Iniciar el proceso de llenado de la DB

    #TODO: Iniciar el proceso de calculos
    ##TODO: En el proceso de comparación que pasa si no hay un mes anterior ??
    ##TODO: Definir que tipo de Alertas se realizaran}
    ##TODO: Como se validan las lecturas mensuales ?
    ##TODO: En el proceso de comparación que pasa si no hay un mes anterior ??
    ##TODO: Si se cuenta con toda la información de los macromedidores


    #TODO: Generar reportes --> de que forma? en que formato? 

