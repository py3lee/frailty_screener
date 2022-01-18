import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from app import app

layout = html.Div(
    [
        html.Div(
            [html.Br()]*5
        ),
        dcc.Markdown(
            """
            **Question 5 of 5** | *Weakness*  
             What is your hand grip strength?
             """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q5-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Hand grip strength in kilograms"),
                dbc.FormFeedback(
                    "All done! Click below to see your results",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 100",
                    type="invalid"
                )
            ]
        ),
        html.Div(
            [html.Br()]*3
        ),
        html.Div(
            [
                dbc.Button(
                    "SHOW ME MY RESULTS", 
                    color="primary",
                    href="#results",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-results"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="weakness"
)

#---Callbacks---#
@app.callback(
    [Output("q5-input", "valid"), Output("q5-input", "invalid")],
    [Input("q5-input", "value")]
)
def check_validity(num):
    if num:
        result = (num > 0) & (num <= 100) 
        return result, not result
    return False, False