import dash_bootstrap_components as dbc
from dash import html, dcc

from app import app

layout = html.Div(
    [
        html.Div(
            [html.Br()]*5
        ), 
        html.Img(src="assets/screener_logo.png",height="200px"),
        dcc.Markdown(
            """
            #### About this project  
            
            This project was conceived as a testing ground to explore the feasibility of developing a web app 
            targeted for clinical use. 

            Further background goes here: 

            --- 

            ##### Feedback  

            Any feedback to improve this app would be greatly appreciated! 
            Please email to: abc@feedback.com  

             """
        ),
        html.Div(
            [html.Br()]*3
        ),
        html.Div(
            [
                dbc.Button(
                    "Let's start", 
                    color="primary",
                    href="#age-gender",
                    external_link=True
                )
            ],
            className="d-grid gap-2",
            id="lets-start"
        ),
        html.Div(
            [html.Br()]*30
        )
    ],
    id="about"
)
