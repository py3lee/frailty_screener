import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from app import app

input_options =[
    {'label':'Rarely or none of the time (<1 day)','value': 1},
    {'label':'Some or a little of the time (1-2 days)','value': 2},
    {'label':'Moderate amount of the time (3-4 days)','value': 3},
    {'label':'Most of the time','value':4}
]

effort_input = dbc.Row(
    [
        dbc.Label(
            "I felt that everything I did was an effort",
            html_for="exhausion-effort",
            width=10
        ),
        dbc.Col(
            dbc.RadioItems(
                id="exhausion-effort",
                options=input_options
            ),
            width=10
        )
    ],
    className="mb-3"
)

going_input = dbc.Row(
    [
        dbc.Label(
            "I could not get going",
            html_for="exhausion-going",
            width=10
        ),
        dbc.Col(
            dbc.RadioItems(
                id="exhausion-going",
                options=input_options
            ),
            width=10
        )
    ],
    className="mb-3"
)

layout = html.Div(
    [
        html.Div(
            [html.Br()]*5
        ),
        dcc.Markdown(
            """
            **Question 3 of 5:** | *Exhausion*  
            
            **How often in the last week did I feel this way**: 
            """
        ),
        effort_input,
        html.Br(),
        going_input,
        html.Div(
            [html.Br()]*3
        ),
        html.Div(
            [
                dbc.Button(
                    "Next: Weight loss (Question 4 of 5)", 
                    color="primary",
                    href="#weight-loss",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-weight-loss"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="exhausion"
)