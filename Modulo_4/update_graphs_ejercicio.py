import pandas as pd
import numpy as np
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv") # ruta para la pc de escritorio
print(df.columns)
df['year'] = df['model_year']
app = dash.Dash()
app.layout= html.Div([html.Div([dcc.Graph(id= 'mpg_scatter',
                                          figure= {'data':[go.Scatter(x=df['year'],
                                                                     y=df['mpg'],
                                                                     text=df['name'],
                                                                     hoverinfo='text',
                                                                     mode='markers')],
                                                   'layout':go.Layout(title='mpg.csv dataset',
                                                                      xaxis={'title':'model year'},
                                                                      yaxis={'title':'miles per galon','rangemode':'tozero'},
                                                                      hovermode='closest')})],
                                 style={'width':'50%', 'display':'inline-block'}),
                      html.Div([dcc.Graph(id= 'mpg_line',
                                          figure={'data':[go.Scatter(x=[0,1],
                                                                     y=[0,1],
                                                                     mode='lines')],
                                                  'layout':go.Layout(title='aceleration',
                                                                     margin={'l':0})}),
                               dcc.Markdown(id='mpg_stats')],
                              style={'width':'20%',
                                     'height':'50%',
                                     'display':'inline-block'})])

@app.callback(
    Output(component_id='mpg_line', component_property='figure'),
    Input(component_id='mpg_scatter', component_property='hoverData'))
def callback_graph(hoverData):
    v_index= hoverData['points'][0]['pointIndex']
    
    fig = {'data':[go.Scatter(x=[0,1],
                              y=[0,60/df.iloc[v_index]['acceleration']],
                              mode='lines',
                              line={'width':2*df.iloc[v_index]['cylinders']})],
           'layout':go.Layout(title=df.iloc[v_index]['name'],
                              xaxis={'visible':False},
                              yaxis={'visible':False,
                                     'range':[0,60/df['aceleration'].min()]},
                              margin= {'l':0},
                              height=300)}
    return fig
                
@app.callback(
             Output(component_id='mpg_stats', component_property='children'),
             Input(component_id='mpg_scatter', component_property='hoverData'))
def callback_stats(hoverData):
    v_index= hoverData['points'][0]['pointIndex']
    stats= """
           {} cylinders\n
           {}cc displacement\n 
           0 to 60 mph in {} seconds""".format(df.iloc[v_index]['cylinders'],
                                               df.iloc[v_index]['displacement'],
                                               df.iloc[v_index]['acceleration'])           
    return stats 

if __name__=='__main__':
    app.run(debug=True, use_reloader=True)