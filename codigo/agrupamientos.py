import os
import sqlite3
from sqlite3 import Error

print(os.getcwd())

def conectar():
    try:
        # conexion = sqlite3.connect(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\db\mydatabase.db") # direccion pc escritorio
        conexion = sqlite3.connect(r'C:\Users\maria\OneDrive\Escritorio\Programacion\Python\Datos-edx\db\mydatabase.db') # direccion lenovo
        conexion.execute("PRAGMA foreing_keys = ON")
        print("Conexion establecida")
        return conexion
    except:
        print(Error)

"""
La sintaxis correcta para realizar agrupamientos de registros de las bases de datos es la siguiente:
"SELECT columna FROM nombre de la tabla WHERE [las condiciones] GROUP BY columna"
"""

def consultas(conexion):
    cursor = conexion.cursor()

    # trae los nombres y los salarios
    consulta1 = "SELECT nombre, SUM(salario) FROM empresa GROUP BY nombre"

    # trae los nombres y los salarios ordenados de manera descendente
    consulta2 = "SELECT nombre, SUM(salario) FROM empresa GROUP BY nombre ORDER BY salario DESC"
    
    # trae los nombres u los salarios ordenados de manera ascendente
    consulta3 = "SELECT nombre, SUM(salario) FROM empresa GROUP BY nombre ORDER BY salario ASC"

    cursor.execute(consulta1)

    filas = cursor.fetchall()
    
    for fila in filas:
        print(fila)

con = conectar()
consultas(con)


