import numpy as np

# creamos una lista en python que luego convertiremos en numpy array
mi_lista = [1,2,3,4,]

# creamos el array de numpy mediante la lista creada con python
mi_array = np.array(mi_lista)

# mostramos la lista de python y el tipo
print(mi_lista)
print(type(mi_lista))

# mostramos el array de np y el tipo
print(mi_array)
print(type(mi_array))

# creamos un nparray a partir de un rango (arange) y lo mostramos por pantalla y cual es le tipo de dato que creamos.
a = np.arange(0,10)
print(a)
print(type(a))

# creamos una matriz de unos con 2 filas y 3 columnas
o = np.ones((2,3))
print(o)
print(type(o))

# creamos una matriz de ceros con 2 filas y 3 columnas
z = np.zeros((2,3))
print(z)
print(type(z))

# generar un numero aleatorio
num_alea  = np.random.randint(0,100)
print(num_alea)

# crea una matriz de numeros aleatorios entre 0 y 100 en 2 filas y 3 columnas 
num_alea2 = np.random.randint(0,100, (2,3))
print(num_alea2)

# generar numeros espaciados, es como hacer la divicion por el numero que le indiquemos en el rango
# en la siguiente secuencia le indicamos que nos devuelva 4 numeros perfectamente espaciados entre 0 y 10
ne = np.linspace(0,10,4) # retorna 0, 3.33, 6.66 y 10 
print(ne)

# definir una una semilla aleatoria mediante la funcion randomseed
# lo que hace es devolver los mismos numeros para la misma secuencia de random
# inclusive devuelve los mismos numeros si varia la cantidad de numeros pedidos
np.random.seed(101)
randomseed = np.random.randint(0,100,8)
print(randomseed)

np.random.seed(101)
randomseed2 = np.random.randint(0,100,8)
print(randomseed2)

# volvemos a setear la semilla en None para que nos devuelva siempre un array diferente 
np.random.seed(seed=None)

# creamos un ndarray de 10 numeros con un rango entre 0 y 100
my_array = np.random.randint(0,100,10)
print(my_array)

# de ese ndarray creado le pedimos que nos muestre el numero mas alto
print(my_array.max())

# le pedimos que nos muestre el valor minimo
print(my_array.min())

# le pedimos que nos muestre el promedio
print(my_array.mean())

# nos muestra el index o posicion del numero maximo en my_array
print(my_array.argmax())

# nos muestra el index o posicion del numero minimo en my_array
print(my_array.argmin())

# nos modifica la dimendion de nuestro array siempre respetando la cantidad de elementos que tiene nuestro array (10 en este caso)
# le pedimos que muestre nuestro array en 2 filas y 5 columna
# si queremos hacer que nos muestre mas elementos que los que tenemos en nuestro array nos va a dar error ej: (2,6) o (3,4)
print(my_array.reshape(2,5))

# creamos en una sola instruccion un array con numeros del 0 al 100 en 10 columnas y 10 filas
mat = np.arange(0,100).reshape(10,10)
# ahora lo mostramos
print(mat)

# para acceder a un valor 43
# recordemos que las posiciones las empezamos a contar desde 0
# el 43 se encuentra en la la fila 4 en la columna 3
print(mat[4,3])

# para acceder a filas o colunas completas usamos :
# columna 3 completa
print(mat[:,3])
# fila 9 completa
print(mat[9,:])

# filtrar valores
# hacemos una comparacion del valor 39 con todos los valores de la tabla y nos devuelve una tabla con valores booleanos
# donde cada valor es el resultado de comprar 39 con ese valor donde False son los numeros que no son mayores a 39 y True son los numeros mayores a 39 
print(mat>39)
# poemos pasarle a la matriz original la misma orden de manera que podamos hacer un filtro y nos muestre todos los valores mayor a 39
print(mat[mat>39])

