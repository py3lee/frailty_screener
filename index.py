import dash
from dash import (
    dcc,
    html
)
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from pathlib import Path
import pandas as pd
import plotly.express as px

from app import app, server
from app_components import (
    about,
    demographic,
    q1_input,
    q2_input,
    q3_input,
    q4_input,
    q5_input
)

# --- NAV BAR --- #

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(
            "About", 
            href="#about", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "My details", 
            href="#age-gender", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "Slowness", 
            href="#slowness", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "Activity", 
            href="#activity", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "Exhaustion", 
            href="#exhausion", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "Weight loss", 
            href="#weight-loss", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "Weakness", 
            href="#weakness", 
            external_link=True
        )),
        dbc.NavItem(dbc.NavLink(
            "My Results", 
            href="#results", 
            external_link=True
        ))
    ],
    brand="PFP-c",
    color="primary",
    fixed="top",
    fluid=True,
    dark=True
)

# --- APP LAYOUT --- #

app.layout = html.Div(
    id="app-content",
    children =[
        dbc.Container(
            fluid = True, 
            children =[
                navbar,
                about.layout,
                demographic.layout,
                q1_input.layout,
                q2_input.layout,
                q3_input.layout,
                q4_input.layout,
                q5_input.layout
            ]
        )
    ]
)

# --- CALLBACKS --- # 
# TODO: callbacks - preprocess input, 
# pipe into inference pipeline (load pretrained model) and output display

if __name__ == "__main__":
    app.run_server(debug=True)