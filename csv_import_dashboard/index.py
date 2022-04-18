import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import import_data

# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,   
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar = html.Div(
    [
        html.H2("Sidebar", className="display-3"),
        html.Hr(),  
        html.P(
            "Data Exploration", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Import Data", href="/", active="exact"),
                dbc.NavLink("Page 2", href="/p2", active="exact"),
                dbc.NavLink("Page 3", href="/p3", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    # "padding": "1rem 1rem",
    "height":"100vh"
    
}

app.layout = dbc.Container([
    dcc.Location(id='url', refresh=False),
    sidebar,
    html.Div(id='page-content', style=CONTENT_STYLE)    
], fluid=True)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == "/":
        return [
                import_data.layout,
                # html.H1('Dashboard for visualizing data',
                #         style={'textAlign':'center'}),
                ]
    elif pathname == "/p2":
        return [
                html.H1('Page 2 can be used for another app',
                        style={'textAlign':'center'}),
                ]
    elif pathname == "/p3":
        return [
                html.H1('Page 3 can be used for another app',
                        style={'textAlign':'center'}),
                ]
    # If the user tries to reach a different page, return a 404 message
    return "404 Page Error! Please choose a link"


if __name__ == '__main__':
    app.run_server(debug=False)