import dash
from dash.dependencies import Input, Output
import dash_core_componenets as dcc
import dash_html_components as html

from pandas_datareader import data as web
from datatime import datetime as dt

app = dash.Dash('Hello World')

app.layout = html.Div([
    dcc.Dropdown(
        id='players'
    ),
    dcc.Graph(id='my-graph')
]   , style={'width': '500'})
     
@app.callback(Output('my-graph', 'figure'))

def update_graph():
    dt = web.DataReader

if __name__=='__main__':
    app.run_server()