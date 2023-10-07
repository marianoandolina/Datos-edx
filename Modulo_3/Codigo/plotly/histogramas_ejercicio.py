import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px 
import pandas as pd

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv")
# print(df.head())
# print(df.columns)
# print(df['mpg'].describe())

data = px.histogram(x=df['mpg'],
                    color=df['origin'],
                    marginal='box')

layout = go.Layout(title='Histograma')

fig = go.Figure(data= data, layout= layout)

pyo.plot(fig, filename='histogram.html')
