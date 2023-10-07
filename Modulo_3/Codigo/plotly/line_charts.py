import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

# Creamos los datos numericos que le vamosa pasar al eje x y al eje y
x_values = np.linspace(0,1,100)
y_values = np.random.randn(100)

# creamos el primer grafico de linea
# le indicamos de que variable tomar los datos que van en el eje x 
# le indicamos de que variable tomar los datos que can en el eje y
# le pasamos por parametro el mode del grafico y el name
trace0 = go.Scatter(x= x_values,
                    y= y_values,
                    fill='tozeroy',
                    mode='lines',
                    name='lines')

# creamos otra linea que va a ser parte de nuestro grafico igual que la linea anterior 
trace1 = go.Scatter(x=x_values,
                    y=y_values+5,
                    mode='lines+markers',
                    name='lines+markers')

# creamos la tercera linea que va a ser parte de nuestro grafico de ejemplo
trace2 = go.Scatter(x=x_values,
                    y=y_values-5,
                    mode='markers',
                    name='markers')

# establecemos en que variable va a estar toda nuestra data
# en este caso le pasamos las 3 lineas que queremos que muestre
# puede ser tambien una sola linea
data = [trace0, trace1, trace2]


layout = go.Layout(title='Grafico de lineas')
fig = go.Figure(data= data, layout= layout)
fig.update_yaxes(range=[-8, 8])
pyo.plot(fig, filename='line_chart.html')




