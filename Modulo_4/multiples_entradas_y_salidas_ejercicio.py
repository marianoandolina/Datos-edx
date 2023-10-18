import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# leemos el archivo y lo convertimos en data frame
#df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv") # pc de escritorio
df = pd.read_csv(r"C:\Users\Mariano\Desktop\programacioon\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv") # laptop

# creamos la app
app = dash.Dash()

features = df.columns
print(features)

app.layout = html.Div([html.Div([dcc.Dropdown(id='features',
                                    options=[{'label':col, 
                                              'value':col}
                                            for col in features],
                                    value='mpg')]),
                        html.Div(id='stats'),
                        dcc.Graph(id='histogram')],
                      style={'padding':10})

@app.callback(Output(component_id='stats',
                     component_property='children'),
              Output(component_id='histogram',
                     component_property='figure'),
             [Input(component_id='features',
                    component_property='value')])
def update_outputs(feature):
    stats= 'La moda de la variable '+str(feature)+' es '+str(df[feature].mode()[0])
    fig= {'data':[go.Histogram(x=df[feature])],
          'layout':go.Layout(title='Histograma de la variable '+str(feature))}
    return stats, fig

if __name__ == "__main__":
    app.run_server()


