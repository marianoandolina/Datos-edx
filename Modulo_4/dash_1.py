# Importamos las librerias que vamos autilizar. 

import dash
from dash import dcc
from dash import html

# creamos nuestra app en dash
app = dash.Dash()

# creamos el diseño de nuestra aplicacion
# lo definimos haciendo una llamada a la funcion html.Div() que sirve para hacer una division en nuestro tablero
# como primer elemento dentro de la funcion html.Div() le pasamos children como una lista con un titulo principal 'Hola Dash' 
app.layout = html.Div(children=[html.H1('Hola Dash!'),
                      html.Div('Dash: Tableros Web con Python'),
                      dcc.Graph(id= 'Example',
                                figure={'data':[{'x':[1,2,3],
                                                 'y':[4,1,2],
                                                 'type':'bar',
                                                 'name':'sf'},
                                                {'x':[1,2,3],
                                                 'y':[2,4,5],
                                                 'type':'bar',
                                                 'name':'NYC'}],
                                        'layaut':{'title':'Graficos de Barras'}
                                        }
                                 )
                         ]
                )
                    

# estas instrucciones son simplemente para que pongamos a correr el servidor 
# funciona como cuando creamos una app en flask
if __name__ == "__main__":
    app.run_server()

