import pandas as pd
import sqlite3
import os

print(os.getcwd())

# abrimos nuestro archivo csv con pandas y lo guardamos en la variable salida
salida = pd.read_csv(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\codigo\womendb.csv', sep=';')
#print(salida) 

# creamos la conexion a la base de datos
con = sqlite3.connect(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\db\womens-inter.db')

# con este comando creamos la tabla en base al archivo csv que abrimos en la variable salida
#salida.to_sql('class', con, if_exists='replace', index= False)

# creamos el objeto cursor para ejecutar sentencias de sql
cursor = con.cursor()

# hacemos consultas a la base de datos
#consulta1 = "SELECT * FROM class"
#salida = pd.read_sql(consulta1, con)
#print(salida.columns)

# podemos ahora comenzar a hacer consultas 

consulta1 = "SELECT * FROM class WHERE Country in ('Japan','Greece','Argentina')"
consulta2 = "SELECT * FROM class ORDER BY 'Inflation rate' DESC"
cursor.execute(consulta2)
filas = cursor.fetchall()
for fila in filas:
    print(fila)
con.close()
