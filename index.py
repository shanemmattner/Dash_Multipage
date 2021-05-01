# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 08:20:44 2021

@author: shane
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

# Connect to main app.py file
from app import app
from app import server


# Connect to the apps
from apps import app1, app2, hantek_data_parser

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = dbc.Card([
                dbc.CardBody([
                    html.H2("Apps", className="display-4"),
                    html.Hr(), # Horizontal line
                    html.P(
                        "Select a Dash App", className="lead"
                    ),
                    dbc.Nav(
                        [
                            dbc.NavLink("Home", href="/", active="exact"),
                            dbc.NavLink("Bootstrap Example", href="/page-1", active="exact"),
                            dbc.NavLink("Hantek6022BE Plot", href="/page-2", active="exact"),
                        ],
                        vertical=True,
                        pills=True,
                    ),
                    ])
    
    ], color='light', style={'height':'100vh', 'width':'16rem', 'position':'fixed'})


# Div for content
content = html.Div(id="page-content", children=[])


# LAYOUT
# Put everything into a container if you're using Bootstrap
# Organization of Bootstrap layout is Row with multiple columns
app.layout = dbc.Container([
    dcc.Location(id="url", refresh=False, pathname=''), # allows app to read address bar
    dbc.Row([
        dbc.Col(sidebar, width=2),
        dbc.Col(content, width=10, style={'margin-left':'20rem'})
        ])
], fluid=True)



@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
                    html.H1('Multi-Page Dash application',
                            style={'textAlign':'center'}),
                ]
    elif pathname == "/page-1":
        return [
                    app1.layout
                ]
    elif pathname == "/page-2":
        return [
                    hantek_data_parser.layout
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


# Run the application
if __name__ == '__main__':
    app.run_server(debug=False, port=8050)