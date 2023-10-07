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

def CrearTabla(conexion):
    conexion.execute("CREATE TABLE empresa(id integer PRIMARY KEY, nombre text not null, edad integer not null, estudios text not null, salario real)")
    print('Funcion CrearTabla ejecutada')
    conexion.commit()

def InsertarRegistro(conexion):
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (10, 'Andrea', 25, 'profesional', 12000)")
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (11, 'Pablo', 31, 'maestria', 18000)")
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (12, 'Daniel', 30, 'doctorado', 21000)")
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (13, 'Fernanda', 27, 'maestria', 18000)")
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (14, 'Luis', 23, 'profesional', 12000)")
    conexion.execute("INSERT INTO empresa(id, nombre, edad, estudios, salario) VALUES (15, 'Karen', 26, 'maestria', 18000)")
    print('Funcion insertarRegistro(s) ejecutada')
    conexion.commit()

def conjuntos(conexion):
    # para realizar busquedas en la base de datos creamos el objeto cursor 
    cursor = conexion.cursor()

    # relizamos las distintas busquedas a modo de ejemplo DESCOMENTAR LA QUE QUERRAMOS REALIZAR
    
    # ORDER BY

    #cursor.execute("SELECT * FROM empresa ORDER BY edad DESC")
    #cursor.execute("SELECT * FROM empresa ORDER BY edad ASC")
    #cursor.execute("SELECT * FROM empresa ORDER BY salario ASC")
    #cursor.execute("SELECT * FROM empresa ORDER BY salario DESC")

    # WHERE

    #cursor.execute("SELECT * FROM empresa WHERE estudios = 'maestria'")
    #cursor.execute("SELECT * FROM empresa WHERE estudios = 'doctorado'")
    #cursor.execute("SELECT * FROM empresa WHERE edad > 25")
    #cursor.execute("SELECT * FROM empresa WHERE edad < 30")
    #cursor.execute("SELECT * FROM empresa WHERE salario < 20000")

    filas = cursor.fetchall()

    for fila in filas:
        print(fila)

con = conectar()

#CrearTabla(con)
#InsertarRegistro(con)
conjuntos(con)
con.close()



