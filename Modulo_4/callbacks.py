import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([dcc.Input(id='Txt',
                                value= 'Texto inicial',
                                type= 'text'),
                      html.Div(id= 'div')])


@appcallbacks(Output(component_id='div',
                     component_property='children'),
              [Input(component_id='txt',
                     component_property='value')])

# La estructura del decorador callback es la siguiente
# @appcallbacks(Output(component_id, componen_property),[Input(componen_id,componen_property)])                

def update_div(input_value):
    return "El texto ingresadoes: {}".format(input_value)

if __name__ == "__main__":
    app.run_server()

