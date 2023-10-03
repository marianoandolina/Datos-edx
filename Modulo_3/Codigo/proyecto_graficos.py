"""
    Iniciamos el proyecto Graficos

Este proyecto finaliza el modulo 3 de Graficos con Plotly
"""

import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import numpy as np

np.random.seed(42)
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# print(x_values)
# print(y_values)

y_avg = y_values.mean()
x_avg = x_values.mean()
y_max = y_values.max()
x_y_max = x_values.max()

# print(y_avg)
# print(x_avg)
# print(y_max)
# print(x_y_max)

trace_1 = go.Scatter(x= x_values,
                     y= y_values,
                     name='Datos',
                     mode='lines+markers')
                    
# trace_2 = go.Scatter(x=x_avg,
#                      y=y_avg,
#                      name='Datos',
#                      mode='lines+markers',
#                      line={'dash':'dash'}
#                     )

data = [trace_1]#,trace_2]               
layout = go.Layout(title='Grafica de linea')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Proyecto Lineas')


