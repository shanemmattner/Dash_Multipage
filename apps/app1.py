# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 08:20:13 2021

@author: shane
"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input, State
import pandas as pd
import plotly.express as px


from app import app

# Import data
df = pd.read_csv('assets/stocks.csv')


"""                         

                            LAYOUT

"""

COL1_SIZE = 5
COL2_SIZE = 12-COL1_SIZE
# COMPONENTS

# Title, centerd, blue, and padded with className.  Found the keywords from:
#       Bootstrap Cheatsheet: https://hackerthemes.com/bootstrap-cheatsheet/
title_header = html.H1("Stock Market Dashboard", className='text-center text-primary mb-4 font-weight-bold')
text_prompt = html.P("Select Company Stock:", style={'textDecoration':'underline'}, className='font-weight-bold')


# Dropdown 
options = [{'label':x, 'value':x} for x in sorted(df['Symbols'].unique())]

dd1 = dcc.Dropdown(id='dd1', multi=False, value='AMZN', options=options)
dd2 = dcc.Dropdown(id='dd2', multi=True, value=['PFE', 'BNTX'], options=options)
dd3 = dcc.Dropdown(id='dd3', multi=False, value=['BNTX'], options=options, clearable=False, style={'color':'000000'})


# Checklist
check1 = dcc.Checklist(id='check1', value=['FB', 'GOOGL', 'AMZN'], options = options,
                       labelClassName='mr-3 text-success font-weight-bold') #change spacing, text color

# Graphs
graph1 = dcc.Graph(id='graph1')
graph2 = dcc.Graph(id='graph2')
graph3 = dcc.Graph(id='graph3')



# Card
card1 = dbc.Card([
            dbc.CardBody(
                html.P("We're better together. Help each other out!", className="card-text")
                        ),
            dbc.CardImg(src="https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif", bottom=True),
                ],
                style={"width": "24rem"},
                )


card2 = dbc.Card([
     
         dbc.CardImg(src='https://media.giphy.com/media/Ll0jnPa6IS8eI/giphy.gif', top=True, bottom=False,
                     title='Image title and stuff', alt='Learn Dash bootstrap card'),
         
         dbc.CardBody([
                 html.H4('learn dash with charming data', className='card-title'),
                 html.H6('Lesson 1:', className='card-subtitle'),
                 html.P( 'Choose the year you would like to see on the bubble chart', className='card-text'),
                 dd3   
                 ])
     
     ],
    style={"width": "24rem"},
    color = 'dark',
    # inverse = True,
    outline = True
    
    
    )

# Content for APP 1
layout = dbc.Container([
        # Declare Rows
        dbc.Row([
                dbc.Col([
                        title_header,
                        ],
                    width = 12, #define the width of the Column
                    ) 
            ]),
        dbc.Row([
                dbc.Col([
                        dd1,
                        graph1
                        ],
                    #if the screen size is small then make the column component the entire width of the page
                    xs=12, sm=12, md=12, lg=COL1_SIZE, xl=COL1_SIZE  
                    ),
                dbc.Col([
                        dd2,
                        graph2
                    ],
                    #if the screen size is small then make the column component the entire width of the page
                    xs=12, sm=12, md=12, lg=COL2_SIZE, xl=COL2_SIZE
                    )
            ]),
        dbc.Row([
                dbc.Col([
                        text_prompt,
                        check1,
                        graph3
                    ], 
                    #if the screen size is small then make the column component the entire width of the page
                    xs=12, sm=12, md=12, lg=COL1_SIZE, xl=COL1_SIZE
                    ),
                dbc.Col([
                        card2
                    ],
                    #if the screen size is small then make the column component the entire width of the page
                    xs=12, sm=12, md=12, lg=COL2_SIZE, xl=COL2_SIZE
                    )
                ],
                align = 'center')
], fluid=True) # Fluid = True stretches container to size of columns used (up to 12)



# Callback section: connecting the components
# ************************************************************************
# Line chart - Single
@app.callback(
    Output('graph1', 'figure'),
    Input('dd1', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols']==stock_slctd]
    figln = px.line(dff, x='Date', y='High')
    return figln


# Line chart - multiple
@app.callback(
    Output('graph2', 'figure'),
    Input('dd2', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    figln2 = px.line(dff, x='Date', y='Open', color='Symbols')
    return figln2


# Histogram
@app.callback(
    Output('graph3', 'figure'),
    Input('check1', 'value')
)
def update_graph(stock_slctd):
    dff = df[df['Symbols'].isin(stock_slctd)]
    dff = dff[dff['Date']=='2020-12-03']
    fighist = px.histogram(dff, x='Symbols', y='Close')
    return fighist