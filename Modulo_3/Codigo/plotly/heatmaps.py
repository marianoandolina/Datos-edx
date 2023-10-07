import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

"""
Los data sets que usamos para este caso son de las temperaturas por hora y dia en una semana de 3 ciudades diferentes.
"""

df1 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010YumaAZ.csv")
df2 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010SitkaAK.csv")
df3 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010SantaBarbaraCA.csv")

data = [go.Heatmap(x=df1['DAY'],
                    y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'].values.tolist()
                    )]
                    
layout = go.Layout(title='Yuma: Temperaturas promedios por dias y horas')

fig = go.Figure(data = data, layout= layout)

pyo.plot(fig, filename='heatmaps.html')





