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

from app import app
# pio.renderers.default='browser'

SAMPLE_RATE = 1000000 # 1Mhz
SAMPLE_TIME = 1/SAMPLE_RATE
MEM_DEPTH = 130048 # TODO: read the text file and use the found value
TOTAL_TIME = 130048/1000000

df = pd.read_csv('data.txt', skiprows=5, delimiter = "\t")
df.columns=['CH1']
time = np.linspace(0, TOTAL_TIME,MEM_DEPTH-1)
# figln.show()  


btn1 = dbc.Button("Click me", id="example-button", className="mr-2")
graph_hantek = dcc.Graph(id='graph_hantek')


# Content for APP 1
layout = dbc.Container([
        # Declare Rows
        dbc.Row([
                dbc.Col([
                        btn1,
                        graph_hantek
                        ],
                    width = 12, #define the width of the Column
                    ) 
            ])
]) # Fluid = True stretches container to size of columns used (up to 12)



@app.callback(
    Output("graph_hantek", "figure"), [Input("example-button", "n_clicks")]
)
def on_button_click(n):
    
    if n is None:
        raise PreventUpdate
    else:
    # df.plot()
        figln = px.line(df,x = time, y='CH1')
        return figln
    
    