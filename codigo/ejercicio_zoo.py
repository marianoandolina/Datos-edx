# EJERCICIO CON ARCHIVO CSV CON DATOS DE ANIMALES DEL ZOO

import pandas as pd
import sqlite3
import os

print(os.getcwd())

# realizamos la lectura con Pandas del archivo csv en la variable salida que luego nos permite utilizar los metodos de pandas
#salida = pd.read_csv(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\codigo\zoo.csv', sep=',' )

# realizamos la coneccion a la base de datos, recordamos que si no existe la db la va a crear
#con = sqlite3.connect(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\db\zoo.db') # conexion pc-escritorio
con = sqlite3.connect(r'C:\Users\maria\OneDrive\Escritorio\Programacion\Python\Datos-edx\db\zoo.db') # conexion laptop

# el metodo to_sql() es un metodo de pandas que nos permite
#salida.to_sql('zoo', con, if_exists='replace', index=False)

# creamos el objeto cursor para ejecutar sentencias SQLite
cursor = con.cursor()

"""
EN ESTE PUNTO REALIZAMOS LA EJECUCION DEL CODIGO HASTA ACA

* Lectura de archivo csv
* Creacion de base de datos y su conexion
* Paso de datos del csv a la base de datos con el metodo to_sql() de pandas
* Creacion de objeto cursor para ejecutar sentencias SQL
"""
# trae la columna animal_name y la columna legs donde legs=4
consulta1= "SELECT animal_name, legs FROM zoo WHERE legs=4"

# trae la columna animal_name y la columna hair donde hair=1 (*en el caso de la tabla zoo los valores en 0 son "no", y los valores en 1 son "si")
consulta2= "SELECT animal_name, hair FROM zoo WHERE hair=1"

# trae el nombre de los animales que tengan plumas y su respectiva columna
consulta3= "SELECT animal_name, feathers FROM zoo WHERE feathers=1"

# trae los animales que producen leche
consulta4= "SELECT animal_name, milk FROM zoo WHERE milk=1"

# trae los animales que no tienen columna vertebral
consulta5= "SELECT animal_name, backbone FROM zoo WHERE backbone=0"

cursor.execute(consulta5)
filas = cursor.fetchall()
for fila in filas:
    print(fila)

