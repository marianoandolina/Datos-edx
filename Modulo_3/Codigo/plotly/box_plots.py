import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\iris.csv")

trace_0 = go.Box(y=df[df['variety'] == 'Setosa']['sepal.length'], name='Setosa')

trace_1 = go.Box(y=df[df['variety'] == 'Versicolor']['sepal.length'], name='Versicolor')

trace_2 = go.Box(y=df[df['variety'] == 'Virginica']['sepal.length'], name='Virginica')


data = [trace_0, trace_1, trace_2]

layout = go.Layout(title='Grafica de cajas, longitud de Sepalo',
                   xaxis=dict(title='Tipo de Flor'))

fig = go.Figure(data= data, layout= layout)
pyo.plot(fig, filename='box_plot.html')

print(df)
pyo.plot(data, filename='box_plot.html')


