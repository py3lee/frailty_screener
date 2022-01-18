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
            **Question 2 of 5:** | *Physical activity*  
            
            During **the last 7 days**:  

            - on how many days did I walk for at least 10 minutes at a time?
             """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q2a-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Number of days where you walked at least 10 mins"),
                dbc.FormFeedback(
                    "Great! Please answer the next part...",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 7 days",
                    type="invalid"
                )
            ]
        ),
        html.Br(),
        html.Br(),
        dcc.Markdown(
            """ 
            - How much time (in minutes) did I usually spend walking on one of those days?
            """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q2b-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Usual walking time in minutes for one of those days"),
                dbc.FormFeedback(
                    "Great! Click on the button to go to the next question",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 1440 minutes",
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
                    "Next: Exhaustion (Question 3 of 5)", 
                    color="primary",
                    href="#exhausion",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-exhausion"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="activity"
)

#---Callbacks---#
@app.callback(
    [Output("q2a-input", "valid"), Output("q2a-input", "invalid")],
    [Input("q2a-input", "value")]
)
def check_validity_days(num):
    if num:
        result = (num >= 0) & (num <= 7) 
        return result, not result
    return False, False

@app.callback(
    [Output("q2b-input", "valid"), Output("q2b-input", "invalid")],
    [Input("q2b-input", "value")]
)
def check_validity_mins(num):
    if num:
        result = (num >= 0) & (num <= 1440) 
        return result, not result
    return False, False