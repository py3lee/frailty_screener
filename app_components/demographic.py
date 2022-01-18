import dash_bootstrap_components as dbc
from dash import html, dcc
from dash.dependencies import Input, Output

from app import app

gender_input = dbc.Row(
    [
        dbc.Label(
            "I am",
            html_for="gender",
            width=10
        ),
        dbc.Col(
            dbc.RadioItems(
                id="gender",
                options=[
                    {'label':'Male', 'value':0},
                    {'label':'Female', 'value':1}
                ]
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
            Before we start, tell us a bit more about yourself 
             """
        ),
        dbc.FormFloating(
            [
                dbc.Input(
                    id="age-input",
                    type="number", 
                    placeholder="",
                    value="",
                    size="lg",
                    valid=True
                ),
                dbc.Label("My age in years"),
                dbc.FormFeedback(
                    "Nice! now let's find out more below",
                    type="valid"
                ),
                dbc.FormFeedback(
                    "Please key in a valid range between 0 - 100",
                    type="invalid"
                )
            ]
        ),
        html.Br(),
        gender_input,
        html.Div(
            [html.Br()]*3
        ),
        html.Div(
            [
                dbc.Button(
                    "Next: Slowness (Question 1 of 5)", 
                    color="primary",
                    href="#slowness",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="next-slowness"
        ),
        html.Div(
            [html.Br()]*10
        )
    ],
    id="age-gender"
)

#---Callbacks---#
@app.callback(
    [Output("age-input", "valid"), Output("age-input", "invalid")],
    [Input("age-input", "value")]
)
def check_validity(num):
    if num:
        result = (num > 0) & (num <= 100) 
        return result, not result
    return False, False