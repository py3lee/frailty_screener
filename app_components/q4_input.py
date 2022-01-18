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
            **Question 4 of 5:** | *Weight loss*  
            
            What is my height and weight?
             """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q4a-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Height in metres"),
                dbc.FormFeedback(
                    "Great! Please answer the next part...",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 3m",
                    type="invalid"
                )
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="q4b-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("Weight in kilograms"),
                dbc.FormFeedback(
                    "Great! Click on the button to go to the next question",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 200kg",
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
                    "Next: Weakness (Question 5 of 5)", 
                    color="primary",
                    href="#weakness",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-weakness"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="weight-loss"
)

#---Callbacks---#
@app.callback(
    [Output("q4a-input", "valid"), Output("q4a-input", "invalid")],
    [Input("q4a-input", "value")]
)
def check_validity_height(num):
    if num:
        result = (num >= 0) & (num <= 3) 
        return result, not result
    return False, False

@app.callback(
    [Output("q4b-input", "valid"), Output("q4b-input", "invalid")],
    [Input("q4b-input", "value")]
)
def check_validity_weight(num):
    if num:
        result = (num >= 0) & (num <= 200) 
        return result, not result
    return False, False