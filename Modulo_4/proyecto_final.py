import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\iris.csv") # ruta de pc de escritorio
print(df.columns)
variables = [{'label': col, 'value': col} for col in ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
marginals = [{'label': m, 'value': m} for m in ['histogram', 'rug', 'box', 'violin']]
app = dash.Dash()

app.layout = html.Div([html.Div([html.H1('Análisis del dataset iris.csv')],
	                               style={'textAlign': 'center'}),
	                      html.Div([html.H3('Configuración de parámetros de la gráfica')],
	                               style={'marginLeft': '5%'}),
	                      html.Div([html.Label('Selecciona la variable del eje X'),
	                                dcc.Dropdown(id='eje-x', options=variables)],
	                               style={'width': '20%',
	                                      'marginRight': '3%',
	                                      'marginLeft': '5%',
	                                      'verticalAlign': 'top',
	                                      'display': 'inline-block'}),
	                      html.Div([html.Label('Selecciona el marginal del eje X'),
	                                dcc.RadioItems(id='marginal-x', options=marginals, labelStyle={'display': 'block'})],
	                               style={'width': '20%',
	                                      'marginRight': '4%',
	                                      'display': 'inline-block'}),
	                      html.Div([html.Label('Seleccionar la variable del eje Y'),
	                                dcc.Dropdown(id='eje-y', options=variables)],
	                               style={'width': '20%',
	                                      'marginRight': '3%',
	                                      'verticalAlign': 'top',
	                                      'display': 'inline-block'}),
	                      html.Div([html.Label('Selecciona el marginal del eje Y'),
	                                dcc.RadioItems(id='marginal-y', options=marginals, labelStyle={'display': 'block'})],
	                               style={'width': '20%',
	                                      'display': 'inline-block'}),
	                      html.Div([dcc.Graph(id='scatter')])])

@app.callback(Output('scatter', 'figure'),
             [Input('eje-x', 'value'),
              Input('marginal-x', 'value'),
              Input('eje-y', 'value'),
              Input('marginal-y', 'value')])
def update_outputs(vx, mx, vy, my):
   fig = px.scatter(df,
                    x= vx,
                    y= vy,
                    color='variety',
                    marginal_x=mx,
                    marginal_y=my,
                    title='Diagrama de dispersión: '+str('eje-x')+' v.s. '+str('eje-y'))
   return fig


if __name__=='__main__':
    app.run(debug=True, use_reloader=True)