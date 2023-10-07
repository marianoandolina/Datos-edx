import os
import sqlite3

# Identificamos el directorio de trabajo actual 
print(os.getcwd())

# Se cambia el directorio de trabajo a una carpeta especifica
# La r al comienzo de la escritura de la ruta es escencial para que interprete las barras de la direccion de manera literal y no como un salto de linea
os.chdir(r"C:\Users\maria\Desktop\Programacion\python\datos_python_edx\db")

# Comprobamos que se halla cambiado el directorio de trabajo
print(os.getcwd())

# Se establece una coneccion con la base de datos "peliculas.db"
sqlite3.connect("peliculas.db")

# Se guardan los datos de coneccion en una variable llamada "conexion"
conexion = sqlite3.connect("peliculas.db")

# Ya tendria que estar creada la base de datos luego de ejecutar este archivo


