import os
import sqlite3
from sqlite3 import Error

print(os.getcwd())

#  funcion para conectar la base de datos
def conectar():
    try:
        conexion = sqlite3.connect(r'C:\Users\maria\OneDrive\Escritorio\Programacion\Python\Datos-edx\db\mydatabase.db')
        conexion.execute('PRAGMA foreing_keys = ON')
        print('Conexion establecida')
        return conexion
    except:
        print(Error)

# funcion para crear la tabla dentro de la base de datos
def crearTabla(conexion):
    conexion.execute ("CREATE TABLE banderas(pais text not null, colores text not null, escudo text not null, continente text not null)")
    print('Funcion crearTabla ejecutada')

# funcion para insertar registros
def insertarRegistroBanderas(conexion, pais, colores, escudo, continente):
    conexion.execute ("INSERT INTO banderas(pais, colores, escudo, continente) VALUES ('"+pais+"','"+colores+"','"+escudo+"','"+continente+"')")
    conexion.commit()
    print("Funcion insertarRegistroBandera ejecutada")

def updateBandera(conexion):
    conexion.execute("UPDATE banderas SET continente='Africa' WHERE pais='Ghana'")
    conexion.commit()


def eliminarTabla(conexion):
    conexion.execute("DROP TABLE IF EXISTS banderas")
    conexion.commit()
    print("Funcion eliminar tabla ejecutada")


# guardamos la funcion conectar en una variable para pasarla como parametro
con = conectar()

# creamos la tabla
# crearTabla(con)

# ejecutamos la funcion para insertar bandera pasando los valores por parametro
# insertarRegistroBanderas(con, "Colombia", "amarillo, azul, rojo", "si","america del sur")
# insertarRegistroBanderas(con, "Mexico", "verde, blanco, rojo", "si","america del norte")
# insertarRegistroBanderas(con, "Croacia", "rojo, blanco, azul", "si","europa")
# insertarRegistroBanderas(con, "Indonesia", "rojo, blanco", "no","asia")
# insertarRegistroBanderas(con, "Palaos", "azul, amarillo", "no","oceania")
# insertarRegistroBanderas(con, "Nigeria", "verde, blanco", "no","africa")
# insertarRegistroBanderas(con, "Ghana", "rojo, amarillo, verde", "si","asia")
# insertarRegistroBanderas(con, "Canadá", "rojo, blanco, verde", "no","america del norte")

# ejecutamos la funcion para updatear la bandera que querramos pasando los valores por parametro
updateBandera(con)

# eliminamos la tabla
# eliminarTabla(con)








