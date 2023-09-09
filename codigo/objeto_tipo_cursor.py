import os
import sqlite3

# Identificamos el directorio de trabajo actual 
print(os.getcwd())

# Se cambia el directorio de trabajo a una carpeta especifica
# La r al comienzo de la escritura de la ruta es escencial para que interprete las barras de la direccion de manera literal y no como un salto de linea
os.chdir(r"C:\Users\maria\Desktop\Programacion\python\datos_python_edx\db")

# Comprobamos que se halla cambiado el directorio de trabajo
print(os.getcwd())

# Se establece conccion con la base de datos peliculas
bdpeliculas = sqlite3.connect("peliculas.db")

# Se crea el objeto de tipo cursor en la variable pcursor
# Con el cursor debidamente creado podemos realizar tareas de busqueda, filtrado, actualizacion, eliminacion etc en la base de datos
pcursor = bdpeliculas.cursor()

# Todos los cambios que realizamos en la base de datos no se actualizan automaticamente, se realiza un commit
# Guardamos todos los datos realizados sobre la base de datos
bdpeliculas.commit()

# Cerramos la coneccion con la base de datos
bdpeliculas.close()

