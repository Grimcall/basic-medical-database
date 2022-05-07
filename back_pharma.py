import sqlite3
import pandas as pd

"""
ATRIBUTOS DE DB:

-ci = CEDULA
-nombre = NOMBRE
-numero = numero telefonico
-direccion
-fecha 
-correo
-tipo de sangre
-comentarios

METODOS:

*Ver todos
*Agregar
*Borrar
*Modificar
*Cerrar
*Exportar a csv.


"""
class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = sqlite3.cursor(db)
        self.cur.execute("CREATE TABLE IF NOT EXISTS Clientes (ci INTEGER PRIMARY KEY, nombre TEXT, numero INTEGER, direccion TEXT, fecha TEXT, correo TEXT, sangre TEXT, comentarios TEXT")
        self.conn.commit()