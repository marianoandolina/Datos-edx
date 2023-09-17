# EJERCICIO CON ARCHIVO CSV CON DATOS DE ANIMALES DEL ZOO

import pandas as pd
import sqlite3
import os

print(os.getcwd())

# realizamos la lectura con Pandas del archivo csv en la variable salida que luego nos permite utilizar los metodos de pandas
salida = pd.read_csv(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\zoo.csv', sep=';' )

# realizamos la coneccion a la base de datos, recordamos que si no existe la db la va a crear
con = sqlite3.connect(r'C:\Users\maria\Desktop\Programacion\python\datos-edx\db\zoo.db')

# el metodo to_sql() es un metodo de pandas que nos permite
salida.to_sql('zoo', con, if_exists='replace', index=False)

