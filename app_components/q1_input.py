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
            **Question 1 of 5** | *Slowness*  
             How long did I take to walk 10 meters?
             """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q1-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Walking time in seconds"),
                dbc.FormFeedback(
                    "Great! Click on the button to go to the next question",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 50",
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
                    "Next: Physical Activity (Question 2 of 5)", 
                    color="primary",
                    href="#activity",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-activity"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="slowness"
)

#---Callbacks---#
@app.callback(
    [Output("q1-input", "valid"), Output("q1-input", "invalid")],
    [Input("q1-input", "value")]
)
def check_validity(num):
    if num:
        result = (num > 0) & (num <= 50) 
        return result, not result
    return False, False