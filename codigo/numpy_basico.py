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


