# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:59:15 2021

Minimal Plotly Express script for time series data having to make the Time axis


TODO:
    * Scan for time axis in the imported dataframe
    * Automatically find the start of the data
    * Import parameters from the txt file
    
@author: shane
"""

import numpy as np
import plotly.io as pio
import plotly.express as px

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
from dash.exceptions import PreventUpdate
import pandas as pd
import math

from app import app
# pio.renderers.default='browser'  #code to display in the browser when plotting directly with PX

SAMPLE_RATE = 1000000 # 1Mhz, get this number from 
SAMPLE_TIME = 1/SAMPLE_RATE
MEM_DEPTH = 130048 # TODO: read the text file and use the found value
TOTAL_TIME = 130048/1000000

df = pd.read_csv('data.txt', skiprows=5, delimiter = "\t")
df.columns=['CH1']
time = np.linspace(0, TOTAL_TIME,MEM_DEPTH-1)
figln = px.line(df,x = time, y='CH1')
# figln.show()  

config={'modeBarButtonsToAdd':['drawline',
                                        'drawopenpath',
                                        'drawclosedpath',
                                        'drawcircle',
                                        'drawrect',
                                        'eraseshape'
                                       ]}
btn1 = dbc.Button("Click me", id="example-button", className="mr-2")
graph_hantek = dcc.Graph(id='graph_hantek', figure = figln, config=config)


# Content for APP 1
layout = dbc.Container([
        # Declare Rows
        dbc.Row([
                dbc.Col([
                        btn1,
                        graph_hantek,
                        html.Div('measurements', id='content')
                        ],
                    width = 12, #define the width of the Column
                    ) 
            ])
], fluid=True) # Fluid = True stretches container to size of columns used (up to 12)




# @app.callback(
#     Output('content', 'children'),
#     [Input('graph', 'graph_hantek'), Input("example-button", "n_clicks")],
#     [State('content', 'children')])
# def shape_added(fig_data, n, content):
#     print(content)
    
#     if fig_data is None:
#         # raise PreventUpdate
#         print("PREVENT UPDATE GRAPH")
#         return 'none'
    
#     if n is None:
#         # raise PreventUpdate
#         print("PREVENT UPDATE BUTTON")
#         return 'none'
    
#     content = "changed!!"
    
#     if 'shapes' in fig_data:
#         print(fig_data['shapes'])
#         line = fig_data['shapes'][-1]
#         length = math.sqrt((line['x1'] - line['x0']) ** 2 +
#                            (line['y1'] - line['y0']) ** 2)
#         content += '%.1f'%length + '\n'
#     return content


# TODO: Bug: dynamic update is not happening with the drawing action, only with the button click
@app.callback(
    Output('content', 'children'), [Input("example-button", "n_clicks"), Input('graph_hantek', 'relayoutData')],
    # State('graph_hantek', 'relayoutData')
)
def on_button_click(n, fig_data):
    
    if n is None:
        raise PreventUpdate
    else:
        if fig_data is None:
            return "no data"
        if 'shapes' in fig_data:
            t_string = ''
            for i in fig_data['shapes']:
                t_string = t_string + str(i)
            t_string = t_string + '\n'
            return html.Div(t_string)
        else:
            return "no shapes"
    
    