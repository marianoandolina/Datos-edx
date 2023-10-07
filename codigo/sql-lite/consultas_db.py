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

def consulta(conexion):
    # creamos el objeto cursor que nos va a permitir ejecutar sentencias sqlite
    cursor = conexion.cursor() 

    # usamos el objeto cursor y entre parentesis realizamos la busqueda filtrada
    # cursor.execute("SELECT * FROM estudiante WHERE promedio > 9") # Ejemplo de busqueda 1
    # cursor.execute("SELECT * FROM estudiante WHERE promedio > 8 and carrera = 'Ingenieria industrial'") # Ejemplo de busqueda 2 con and


    # guardamos toda la informacion conseguida por el comando anterior en la variable filas
    filas = cursor.fetchall()

    # realizamos un bucle que recorra la informacion guardada en la variable
    for fila in filas:
        print(fila)


con = conectar()

consulta(con)

con.close()