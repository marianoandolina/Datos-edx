import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# en esta parte generamos con numpy los datos numericos para nuestra grafica
np.random.seed(42)

# datos del eje x
random_x = np.random.randint(1,101,100)

# datos del eje y
random_y = np.random.randint(1,101,100)

data = [go.Scatter(x=random_x,
                   y=random_y,
                   mode='markers',
                   marker=dict(
                        size=12,
                        color='rgb(254,89,0)',
                        symbol='cross',
                        line={'width':1}
                   ))]

layout = go.Layout(title='Grafica de dispersion',
                   xaxis={'title':'Eje X'},
                   yaxis=dict(title='Eje Y'), 
                   hovermode='closest')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='scatter1.html')
