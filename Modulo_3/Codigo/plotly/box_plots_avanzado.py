import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# leemos el data frame con pandas
df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\iris.csv")

# extraemos los datos del data frame que vamos a usar en nuestro grafico
# cada variable trace corresponde a un tipo de dato especifico que va a tener nuestro grafico
# almacenamos los datos en la varieble data
data = [go.Box(y=df[df['variety'] == flor]['sepal.length'],
               name=flor,
               boxpoints='all')
        for flor in df['variety'].unique()]

# creamos el layout o los titulos del grafico y los ejes
layout = go.Layout(title='Grafica de cajas: longitud de Sepalo',
                   xaxis=dict(title='Tipo de Flor'))

# pasamos todo lo que necesitamos para el grafico en la variable fig
fig = go.Figure(data= data, layout= layout)

# finalmente creamos el grafico y pasamos por parametro todos los graficos y el nombre del archivo html que va a representar graficamente los datos
pyo.plot(data, filename='box_plot_avanzado.html')

"""
TIRA UN ERROR DIRECTO DE PANDAS QUE NO SE CUAL ES
"""
