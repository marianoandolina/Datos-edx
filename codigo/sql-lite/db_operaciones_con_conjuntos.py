"""
INNER JOIN 
Encuentra coincidencias entre la tabla A y la tabla B

LEFT OUTER JOIN
Trae todo lo de una tabla A y las coincidencias con la tabla B

RIGTH OUTER JOIN
Trae todo lo de la tabla B y las coincidencias con la tabla A

FULL OUTER JOIN
Trae todo de la tabla A y la tabla B
"""
import os
import sqlite3
from sqlite3 import Error

print(os.getcwd())

# creamos la funcion que va a establecer la conexion
def conectar():
    try:
        conexion = sqlite3.connect(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\db\mydatabase.db') # direccion pc escritorio
        # conexion = sqlite3.connect(r'C:\Users\maria\OneDrive\Escritorio\Programacion\Python\Datos-edx\db\mydatabase.db') # direccion lenovo
        conexion.execute('PRAGMA foreing_keys = ON')
        print('Conexion establecida')
        return conexion
    except:
        print(Error)

def conjuntos(conexion):
    cursor = conexion.cursor()
    # realizamos la busqueda 
    #cursor.execute("SELECT nombre, apellido FROM estudiante JOIN datosContacto ON estudiante.matricula = datosContacto.estudiante")

    """
    EXPLICACION DE LA BUSQUEDA
    ("SELECT nombre, apellido FROM estudiante JOIN datosContacto ON estudiante.matricula = datosContacto.estudiante")

    Selecciona el nombre y apellido de la tabla estudiante donde en la tabla datosContacto la columna matricula de la tabla estudiante sea igual a la columna estudiante
    de la tabla datosContacto
    """

    # realizamos la busqueda desde la tabla de datosContacto
    cursor.execute("SELECT estudiante FROM datosContacto LEFT JOIN estudiante ON datosContacto.estudiante = estudiante.matricula")
    
    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

con = conectar()

conjuntos(con)

