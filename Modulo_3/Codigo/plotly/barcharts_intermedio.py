import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

"""
Tenemos un dataset .csv que contiene los datos de las medalallas conseguidas en los juegos Olimpicos de 2018 por cada pais. 
Vamos a crear un grafico que contenga 1 barra para cada tipo de medalla que obtuvieron los paises
"""

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2018WinterOlympics.csv")
#print(df.head())




# creamos la variable las 3 barras que vamos a mostrar con cada pais
# notar que a diferencia del archivo barcharts_basico.py las variables que crean las barras estan sin corchetes
# esto se debe a que al pasar la data vamos a pasarla como una lista con las 3 barras

trace_1 = go.Bar(x=df['NOC'],
               y=df['Gold'],
               name='Oro',
               marker={'color':'#FFD700'})

trace_2 = go.Bar(x=df['NOC'],
               y=df['Silver'],
               name='Plata',
               marker={'color':'#9EA0A1'})

trace_3 = go.Bar(x=df['NOC'],
               y=df['Bronze'],
               name='Bronce',
               marker={'color':'#CD7F32'})

# pasamos la data como una lista con los datos de las 3 barras
data = [trace_1, trace_2, trace_3]

# el titulo del grafico
# este layout muestra una barra para cada medalla
#layout = go.Layout(title='Medallas por pais')

# este layout muestra los 3 tipos de medallas con sus respectivos colores en una sola barra
layout = go.Layout(title='Medallas por pais', barmode='stack')

# creamos la figura
fig = go.Figure(data= data, layout= layout)

# mostramos el grafico y colocamos el nombre
pyo.plot(fig, filename='bar_chart_intermedio.html')