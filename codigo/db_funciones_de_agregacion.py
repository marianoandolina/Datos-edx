import os
import sqlite3
from sqlite3 import Error
from db_creacion_eliminacion_edicion import conectar

print(os.getcwd())

# creamos la tabla para el ejemplo e insertamos los valores

def tabla(conexion):
    conexion.execute("CREATE TABLE clientes(id integer PRIMARY KEY, nombre text, apellido text)")
    conexion.execute("CREATE TABLE ordenes(id integer PRIMARY KEY, cliente_id integer, nombre_producto text, cantidad integer)")
    conexion.execute("INSERT INTO clientes(id, nombre, apellido) VALUES (123, 'Manuel','Ramirez')")
    conexion.execute("INSERT INTO clientes(id, nombre, apellido) VALUES (564, 'Maria','Perez')")
    conexion.execute("INSERT INTO ordenes(cliente_id, nombre_producto, cantidad) VALUES (123, 'arroz', 2), (123, 'frijoles',3), (123, 'leche',5), (123, 'huevos',12)")
    conexion.execute("INSERT INTO ordenes(cliente_id, nombre_producto, cantidad) VALUES (564, 'harina', 2), (564, 'huevos',3), (564, 'azucar',1), (564, 'chocolate', 1)") 
    conexion.commit()

def eliminarTabla(conexion):
    conexion.execute("DROP TABLE IF EXISTS clientes")
    conexion.execute("DROP TABLE IF EXISTS ordenes")
    conexion.commit()

def consultas(conexion):
    cursor = conexion.cursor()
    # trae todos los registros de la tabla clientes
    consulta1 = "SELECT * FROM clientes"

    # trae todos los registros de la tabla ordenes
    consulta2 = "SELECT * FROM ordenes"

    # cuenta el total de registros en la tabla ordenes 
    consulta3 = "SELECT COUNT (*) FROM ordenes"

    # cuenta el total de registros en la tabla clientes
    consulta4 = "SELECT COUNT (*) FROM clientes"

    # trae una suma de la columna cantidad de la tabla ordenes
    consulta5 = "SELECT SUM (cantidad) FROM ordenes"

    # trae el numero maximo de la columna cantidad de la tabla ordenes
    consulta6 = "SELECT MAX (cantidad) FROM ordenes"

    # trae el numero minimo de la columna cantidad de la tabla ordenes
    consulta7 = "SELECT MIN (cantidad) FROM ordenes"
    
    # trael el promedio de la columna cantidad de la tabla ordenes
    consulta8 = "SELECT AVG (cantidad) FROM ordenes"
    
    # trae la cadena de la columna nombre de la tabla clientes en mayusculas
    consulta9 = "SELECT UPPER (nombre) FROM clientes"

    # trae la cadena de la columna nombre de la tabla clientes en minusculas
    consulta10 = "SELECT LOWER (nombre) FROM clientes"
    
    # trae la suma de los caracteres de cada fila de la columna nombre de la tabla clientes
    consulta11 = "SELECT LENGTH (nombre) FROM clientes"

    cursor.execute(consulta11)

    filas = cursor.fetchall()
    for fila in filas:
        print(fila)

con = conectar()

#tabla(con)
#eliminarTabla(con)
consultas(con)

con.close()