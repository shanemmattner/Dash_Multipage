# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 08:20:26 2021

@author: shane
"""
import dash
import dash_bootstrap_components as dbc

# Meta tags make the app mobile friendly
app = dash.Dash(__name__, suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.BOOTSTRAP],
                meta_tags=[{'name': 'viewport',
                            'content':'width=device-width, initial-scale=1.0'}])

server = app.server
