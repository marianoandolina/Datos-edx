import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# leemos el archivo y lo convertimos en data frame
df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv")

# creamos la app
app = dash.Dash()


features = df.columns
print(features)

app.layout = html.Div([html.Div([dcc.Dropdown(id='xaxis', 
                                              options=[{'label':col, 'value':col} for col in features], 
                                              value='mpg')], 
                                              style={'width':'45%', 'display':'inline-block'}),
                       html.Div([dcc.Dropdown(id='yaxis',
                                              options=[{'label':col, 'value':col} for col in features], 
                                              value= 'displacement')],
                                 style={'width':'45%', 'display':'inline-block'}),
                       dcc.Graph(id='scatter')],
                       style={'padding':10})
            
@app.callback(Output(component_id= 'scatter',
                     component_property='figure'),
              [Input(component_id= 'xaxis',
                     component_property='value'),
               Input(component_id='yaxis',
                     component_property= 'value')])
def update_graph(x_feature, y_feature):
    return {'data':[go.Scatter(x=df[x_feature],
                               y=df[y_feature],
                               text=df['name'],
                               mode='markers',
                               marker={'size':12})],
            'layout':go.Layout(title='Tablero de MPG',
                               xaxis={'title':x_feature},
                               yaxis={'title':y_feature})}

if __name__ == "__main__":
    app.run_server()






