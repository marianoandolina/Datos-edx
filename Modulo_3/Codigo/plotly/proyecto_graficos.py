"""
    Iniciamos el proyecto Graficos

Este proyecto finaliza el modulo 3 de Graficos con Plotly
"""

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

np.random.seed(42)
x_values = np.linspace(0, 1, 100)
y_values = np.random.randn(100)

# print(x_values)
# print(y_values)

y_avg = y_values.mean()
x_avg = x_values.mean()
y_max = y_values.max()
x_y_max = x_values[y_values.argmax()]

# print(type(y_avg))
# print(type(x_avg))
# print(y_max)
# print(x_y_max)

trace_1 = go.Scatter(x=x_values, 
                     y=y_values, 
                     name="Datos", 
                     mode="lines")

trace_2 = go.Scatter(x=[0,1],
                     y=[y_avg, y_avg],
                     name='Promedio',
                     mode='lines',
                     line={'dash':'dot'}
                    )

data = [trace_1, trace_2]
layout = go.Layout(title="Grafica de linea")
fig = go.Figure(data=data, layout=layout)

fig.add_annotation(x=x_y_max,
                   y=y_max,
                   text='En x = {:.2f} alcanzo su valor maximo de {:.2f}'.format(x_y_max, y_max),
                   showarrow= True,
                   arrowhead=5,
                   )

fig.add_annotation(axref='x',
                   ayref='y',
                   x=0.6,
                   y=y_avg,
                   ax=0.5,
                   ay=0.2,
                   text='El promedio de los valores es {:.2f}'.format(0.4),
                   showarrow=True,
                   arrowhead=5
                    )
pyo.plot(fig, filename="Proyecto Lineas")
