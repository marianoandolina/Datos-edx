import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import subplots

"""
Los data sets que usamos para este caso son de las temperaturas por hora y dia en una semana de 3 ciudades diferentes.
En este caso a diferencia del heatmap anterior estamos mostrando las 3 ciudades a la vez en un solo grafico, para eso importamos el modulo subplots de plotly
"""

df1 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010YumaAZ.csv")
df2 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010SitkaAK.csv")
df3 =  pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\2010SantaBarbaraCA.csv")

trace_0 = go.Heatmap(x=df1['DAY'],
                    y=df1['LST_TIME'],
                    z=df1['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45
                    )

trace_1 = go.Heatmap(x=df2['DAY'],
                    y=df2['LST_TIME'],
                    z=df2['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45
                    )

trace_2 = go.Heatmap(x=df3['DAY'],
                    y=df3['LST_TIME'],
                    z=df3['T_HR_AVG'].values.tolist(),
                    colorscale='Jet',
                    zmin=0,
                    zmax=45
                    )

fig = subplots.make_subplots(rows=1,
                             cols=3,
                             subplot_titles=['Yuma', 'Sitka', 'Santa Barbara'],
                             shared_xaxes=True)

fig.append_trace(trace_0, 1, 1)
fig.append_trace(trace_1, 1, 2)
fig.append_trace(trace_2, 1, 3)

fig.update_layout(title='Mapa de calor de 3 ciudades', title_x=0.5)

pyo.plot(fig, filename='heatmaps_avanzado.html')
