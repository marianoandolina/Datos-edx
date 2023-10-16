import dash
from dash import html 
from dash import dcc

app = dash.Dash()

app.layout = html.Div([html.Label('Dropdown'), 
             dcc.Dropdown(options=[{'label':'New York City', 'value':'NYC'},
                                   {'label':'Montreal', 'value':'MTL'},
                                   {'label':'San Francisco', 'value':'SF'}],
                          value='MTL',
                          multi=True),
             html.Label('Slider'),
             dcc.Slider(min=-10,
                        max=5,
                        step=0.5,
                        value=-3,
                        marks={i:i for i in range(-10,11)}),
             html.Label('Radio Items'),
             dcc.RadioItems(options=[{'label':'New York City', 'value':'NYC'},
                                     {'label':'Montreal', 'value':'MTL'},
                                     {'label':'San Francisco', 'value':'SF'}],              
                            value='NYC',
                            labelStyle={'display':'block'}
                            )
                       ]
                      )

if __name__ == '__main__':
    app.run_server()

