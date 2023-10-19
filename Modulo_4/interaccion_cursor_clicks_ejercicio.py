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
                                  style={'width':'30%'}),
                        html.Div([html.Pre(id='image-name',
                                           style={'paddingTop': 35})])])

@app.callback(Output('hover-data', 'children'),
              Output('image-name', 'children'),
             [Input('color-wheels', 'clickData')])
def get_hoverinfo(clickData):
    wheel=clickData['points'][0]['y']
    color=clickData['points'][0]['x']
    name=df[(df['wheels']==wheel) & (df['color']==color)]['image'].values[0]
    return json.dumps(clickData, indent=2), name

if __name__ == "__main__":
    app.run_server(debug=True, use_reloader= True)