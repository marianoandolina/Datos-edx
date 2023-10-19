import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import json

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\wheels.csv") # ruta de la pc de escritorio

app = dash.Dash()

app.layout = html.Div([html.Div([dcc.Graph(id='color-wheels',
                                           figure={'data':[go.Scatter(x=df['color'],
                                                                      y=df['wheels'],
                                                                      dy=1,
                                                                      mode='markers',
                                                                      marker={'size':12, 
                                                                              'color':'rgb(254, 89, 0)',
                                                                              'line':{'width': 2}})],
                                                    'layout':go.Layout(title='Wheels and colors scatterplott',
                                                                       xaxis={'title':'Color'},
                                                                       yaxis={'title':'# of Wheels',
                                                                              'nticks':3},
                                                                       hovermode='closest')})],
                                        style={'widht':'30%',
                                               'float':'left'}),
                        html.Div([html.Pre(id='hover-data',
                                           style={'paddingTop':35})],
                                  style={'width':'30%'})])

@app.callback(Output('hover-data', 'children'),
             [Input('color-wheels', 'clickData')])
def get_hoverinfo(hoverData):
    return json.dumps(hoverData, indent=2)

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader= True)