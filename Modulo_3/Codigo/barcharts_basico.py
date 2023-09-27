import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

"""
Tenemos un dataset .csv que contiene los datos de las medalallas conseguidas en los juegos Olimpicos de 2018 por cada pais. 
Vamos a crear un grafico que contenga sobre un eje la cantidad de medallas y sobre el otro eje el nombre del pais.
"""


df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2018WinterOlympics.csv")
#print(df.head())

# creamos la variable data como una lista
data = [go.Bar(x=df['NOC'],
               y=df['Total'])]

# con el layout le ponemos el titulo
layout = go.Layout(title='Medallas por pais')        

# en la variable fig pasamos la data y el layout
fig = go.Figure(data=data, layout=layout)

# creamos el grafico con la variable fig como parametro (contiene data y layout) + el nombre del archivo html
pyo.plot(fig, filename='bar_chart_basico.html')

