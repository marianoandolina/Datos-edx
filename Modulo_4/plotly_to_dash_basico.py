import dash
from dash import dcc
from dash import html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# creamos los datos que vamos a usar en el grafico
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

app.layout = html.Div([html.H1('Dash + Plotly', style={'textAlign':'center', 'color':'#0000FF'}),
                       dcc.Graph(id='scatterplot1',
                                 figure={'data':[go.Scatter(x=random_x,
                                                            y=random_y,
                                                            mode='markers')],
                                         'layout':go.Layout(title='Scatter Plot')
                                         }
                                 )
                        ]
                       )

if __name__ == '__main__':
    app.run_server()