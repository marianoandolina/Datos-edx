import os
import sqlite3
from sqlite3 import Error

print(os.getcwd())

# creamos la funcion que va a crear la base de datos y establecer la conexion
def conectar():
    try:
        conexion = sqlite3.connect(r'C:\Users\maria\Desktop\Programacion\python\datos_python_edx\db\mydatabase.db')
        conexion.execute('PRAGMA foreing_keys = ON')
        print('Conexion establecida')
        return conexion
    except:
        print(Error)

# creamos la funcion que va a crear las tablas dentro de la base de datos con sus columnas y filas
def CrearTabla(conexion):
    conexion.execute('CREATE TABLE estudiante(matricula integer PRIMARY KEY, nombre text not null, apellido text not null, fecha de inicio text not null, promedio real)')
    conexion.execute('CREATE TABLE carrera (id integer PRIMARY KEY, nombre text not null, estudiante integer)')
    conexion.execute('CREATE TABLE datosContacto(ide integer PRIMARY KEY, estudiante integer, telefono1 text, telefono2 text, correo text, CONSTRAIN fk_contactoEstudiante FOREING KEY (estudiante) REFERENCES estudiante (matricula))')

def modificarTabla(conexion):
    conexion.execute('ALTER TABLE estudiante ADD COLUMN carrera text not null') # Agregamos la columna carrera
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grado integer not null') # Agregamos la columna grado
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grupo text not null') # Agregamos la columna grupo
    conexion.commit() # commiteamos o guardamos los campos

# creamos la funcion que va a eliminar una tabla
def eliminarTabla(conexion):
    # si existe eliminamos la tabla 'carrera' 
    conexion.execute('DROP TABLE IF EXISTS carrera') 
    # guardamos o comiteamos los cambios realizados
    conexion.commit()

con = conectar()
# CrearTabla(con) # comentamos este campo una vez que ya creamos las tablas porque no pueden ser creadas 2 veces
# modificamos la tabla usando la funcion modificarTabla()
# modificarTabla(con) # una vez que ya modificamos la tabla comentamos la funcion para executar el ejemplo de eliminar tabla

# eliminamos la tabla con la funcion que creamos anteriormente
eliminarTabla(con)

# por ultimo al terminar cerramos la conexion con la base de datos
con.close()







