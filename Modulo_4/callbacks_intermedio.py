import pandas as pd
import plotly.graph_objects as go
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

# leemos el data frame con pandas
df = pd.read_csv(r"C:\Users\maria\Desktop\Programacion\python\datos-edx\Modulo_3\Codigo\Datasets\mpg.csv") # ruta de acceso pc escritorio
origin_options = []
for origin in df['origin'].unique():
    origin_options.append({'label':str(origin), 'value':origin})

print(origin_options)

app = dash.Dash()

app.layout = html.Div([dcc.Dropdown(id='origin-picker',
                                   options=origin_options,
                                   value=df['origin'].min()),
                      dcc.Graph(id= 'graph')])

@app.callback(Output(component_id= 'graph',
                    component_property='figure'),
            [Input(component_id='origin-picker',
                   component_property='value')])

def update_graph(origin_value):
    filtered_df = df[df['origin']=='origin_value']
    return {'data':[go.Histogram(x=filtered_df['mpg'],
                                 nbinsx=40)],
            'layout':go.Layout(title='Histograma del origin '+str(origin_value))}

if __name__ == '__main__':
    app.run_server()
