import pandas as pd
import os.path

from db.config_db import add_meter, create_connection


def read_all_sheets(filename):
    """
    Este bloque de codigo se encarga de leer el archivo que
    por medio de Pandas convertir cada una de sus hojas en un DataFrame

    args:
        - filename: -> Path o Ruta del archivo a leer
    """
    if not os.path.isfile(filename):
        return None

    xls = pd.ExcelFile(filename)
    sheets = xls.sheet_names
    results = {}
    for sheet in sheets:
        results[sheet] = xls.parse(sheet)

    xls.close()

    return results, sheets


def populating_data():
    """
    Este bloque de codigo se encarga de llamar la función anterior y recorrer
    sus resultados para crear un diccionario con cada uno de los registros del Dataframe de Pandas
    para posteriormente almacenarlos en la DB de SQLite3.

    No args...
    """
    database = r"./db/fluvio.db"
    # create a database connection
    conn = create_connection(database)

    # TODO: Resolver con Brayan la veracidad de la información en el archivo usuarios.xlsx
    # TODO: Especificar un mismo formato para las celdas de encabezado, de ser posible bajo un estandar. (Idioma - Snake_case o CamelCase)

    file_path = "./utils/usuarios.xlsx"  # Ruta del archivo a cargar en DB
    results, sheets = read_all_sheets(filename=file_path)

    for registry, sheet_name in zip(results.values(), sheets):
        sheet = registry.T.to_dict().values()
        print(f"SHEET: {sheet_name}")
        if sheet_name != "Hoja2":
            for row in sheet:
                """
                    INSERT ORDER --> name, fid, shape, point_x, point_y, point_z, point_m, request, hab
                """
                id_ = add_meter(
                    conn=conn,
                    meter=(
                        row["Name"],
                        row["FID"],
                        row["Shape"],
                        row["POINT_X"],
                        row["POINT_Y"],
                        row["POINT_Z"],
                        row["POINT_M"],
                        row["Demanda"],
                        row["Hab"],
                    ),
                )
                print(id_)
        else:
            print("Hoja de prueba")


populating_data()
