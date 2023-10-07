import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# en esta parte generamos con numpy los datos numericos para nuestra grafica
np.random.seed(42)

# datos del eje x
random_x = np.random.randint(1,101,100)

# datos del eje y
random_y = np.random.randint(1,101,100)

# con la siguiente funcion guardamos en la variable data todo lo necesario para generar el grafico
data = [go.Scatter(x=random_x, y=random_y,mode='markers')]

# finalmente generamos el grafico
pyo.plot(data, filename='scatter_basico.html')



