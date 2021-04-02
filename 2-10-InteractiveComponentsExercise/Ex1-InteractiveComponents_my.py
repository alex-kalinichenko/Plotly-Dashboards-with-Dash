#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:

app.layout = html.Div([
    dcc.RangeSlider(id='two_numbers',
                    min=-10,
                    max=10,
                    step=1,
                    marks={i: i for i in range(-10, 11)},
                    value=[-3, 7]),
    html.Div(id='product',
             style={'color': 'green',
                    'border': '2px green solid',
                    'margin': 50,
                    'width': 100}
             ),
])


# Create a Dash callback:
@app.callback(
    Output(component_id='product', component_property='children'),
    [Input('two_numbers', 'value')]
)
def num_mult(value_list):
    return value_list[0] * value_list[1]


# Add the server clause:
if __name__ == '__main__':
    app.run_server()
