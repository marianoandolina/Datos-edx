# Importamos las librerias que vamos autilizar. 

import dash
from dash import dcc
from dash import html

# creamos el diccionario de colores con clave y valor
colors = {'background':'#111111',
          'text':'#111111'}

# creamos nuestra app en dash
app = dash.Dash()

# creamos el diseño de nuestra aplicacion
# lo definimos haciendo una llamada a la funcion html.Div() que sirve para hacer una division en nuestro tablero
# como primer elemento dentro de la funcion html.Div() le pasamos children como una lista con un titulo principal 'Hola Dash' 
app.layout = html.Div(children=[html.H1('Hola Dash!', 
                                        style={'textAlign':'center', # alineacion del texto
                                               'color':colors['text']}), # color del texto                         
                      html.Div('Dash: Tableros Web con Python'), # titulo del texto
                      dcc.Graph(id= 'Example', # este es el id del grafico
                                figure={'data':[{'x':[1,2,3], # datos del eje x
                                                 'y':[4,1,2], # datos del eje y 
                                                 'type':'bar', # tipo de grafico
                                                 'name':'SF'}, # nombre de los datos para identificar las barras a las que pertenecen
                                                {'x':[1,2,3], # datos del eje x del segundo conjunto de barras
                                                 'y':[2,4,5], # datos del eje y del segundo conjunto de barras
                                                 'type':'bar', # tipo de graficos que va a mostrar esos datos
                                                 'name':'NYC'}], # nombre de los datos para identificar las barras a las que pertenecen
                                        'layout':{'title':'Graficos de Barras', # titulo del grafico
                                                  'plot_bgcolor':'#000000', # color del plot
                                                  'paper_bgcolor':'#000000', # color del fondo
                                                  'font':{'color':'#808080'}} # color de la fuente
                                        }
                                    )
                                ]
                        )
                    

# estas instrucciones son simplemente para que pongamos a correr el servidor 
# funciona como cuando creamos una app en flask
if __name__ == "__main__":
    app.run_server()

