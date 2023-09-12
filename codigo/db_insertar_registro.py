""" 
Sentencias vistas en este documento 

PRAGMA
CREATE TABLE
ALTER TABLE
DROP TABLE 
INSERT INTO 
VALUES
CONSTRAINT
"""

import os
import sqlite3
from sqlite3 import Error

print(os.getcwd())

# creamos la funcion que va a crear la base de datos y establecer la conexion
def conectar():
    try:
        conexion = sqlite3.connect(r'C:\Users\maria\OneDrive\Escritorio\Programacion\Python\Datos-edx\db\mydatabase.db')
        conexion.execute('PRAGMA foreing_keys = ON')
        print('Conexion establecida')
        return conexion
    except:
        print(Error)

# creamos la funcion que va a crear las tablas dentro de la base de datos con sus columnas y filas
def CrearTabla(conexion):
    conexion.execute('CREATE TABLE estudiante(matricula integer PRIMARY KEY, nombre text not null, apellido text not null, fechaInicio text not null, promedio real)')
    conexion.execute('CREATE TABLE carrera (id integer PRIMARY KEY, nombre text not null, estudiante integer)')
    conexion.execute('CREATE TABLE datosContacto(ide integer PRIMARY KEY, estudiante integer, telefono1 text, telefono2 text, correo text, CONSTRAINT fk_contactoEstudiante FOREIGN KEY (estudiante) REFERENCES estudiante (matricula))')
    print('Tabla(s) Creadas')

# creamos la funcion para modificar la tabla
def modificarTabla(conexion):
    conexion.execute('ALTER TABLE estudiante ADD COLUMN carrera text not null') # Agregamos la columna carrera
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grado integer not null') # Agregamos la columna grado
    conexion.execute('ALTER TABLE estudiante ADD COLUMN grupo text not null') # Agregamos la columna grupo
    conexion.commit() # commiteamos o guardamos los campos
    print('Tabla modificada')

# creamos la funcion que va a eliminar una tabla
def eliminarTabla(conexion):
    # si existe eliminamos la tabla 'carrera' 
    conexion.execute('DROP TABLE IF EXISTS carrera') 
    conexion.execute('DROP TABLE IF EXISTS estudiante') 
    conexion.execute('DROP TABLE IF EXISTS datosContacto') 
    
    # guardamos o comiteamos los cambios realizados
    conexion.commit()
    print('Tabla eliminada')

# creamos la funcion para insertar un registro
def insertarRegistro(conexion):
    # conexion.execute("INSERT INTO estudiante (nombre, apellido, fechaInicio, promedio, carrera, grado, grupo) VALUES('Jose','Rodriguez Perez','2021-06-09','8.75','Ingenieria industrial', 1, 'G')")
    conexion.execute("INSERT INTO estudiante (nombre, apellido, fechaInicio, promedio, carrera, grado, grupo) VALUES('Maria','Cruz Velazquez','2018-01-15','9.72','Licenciatura en Enfermeria', 6, 'B')")
    # conexion.execute("INSERT INTO estudiante (nombre, apellido, fechaInicio, promedio, carrera, grado, grupo) VALUES('David','Sanchez Torrez','2021-06-09','7.5','Ingenieria Industrial', 1, 'G')")
    # conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (1, '8331234567', '1552334455', 'micorreo@gmail.com')") 
    # conexion.execute("INSERT INTO datosContacto (estudiante, telefono1, telefono2, correo) VALUES (2, '0554563567', '1111234167', 'correoejemplo@gmail.com')")
    conexion.commit()
    print('Registro(s) insertado')

# creamos la funcion para modificar un registro
def  modificarRegsitro(conexion, matricula, nombre, telefono):
    conexion.execute("UPDATE estudiante SET nombre = '"+nombre+"' WHERE matricula = "+str(matricula))
    conexion.execute("UPDATE datosContacto SET telefono1 = '"+telefono+"' WHERE estudiante = "+str(matricula))
    conexion.commit()

def eliminarRegistro(conexion):
    conexion.execute("DELETE FROM datosContacto WHERE estudiante = 1")
    conexion.execute("DELETE FROM datosContacto WHERE estudiante = 2")
    conexion.execute("DELETE FROM estudiante WHERE matricula = 2")
    conexion.commit()
    print("Funcion eliminarRegistro ejecutada")
        
con = conectar()
# CrearTabla(con) # comentamos este campo una vez que ya creamos las tablas porque no pueden ser creadas 2 veces
# modificamos la tabla usando la funcion modificarTabla()
# modificarTabla(con) # una vez que ya modificamos la tabla comentamos la funcion para executar el ejemplo de eliminar tabla

# eliminamos la tabla con la funcion que creamos anteriormente
# eliminarTabla(con)

# llamamos a la funcion para inseratar un registro
# insertarRegistro(con)

# modificarRegsitro(con, 2, 'Joaquina', '47530102')

# eliminarRegistro(con)

# por ultimo al terminar cerramos la conexion con la base de datos
#con.close()