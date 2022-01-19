import dash
import dash_bootstrap_components as dbc

# App instance
app = dash.Dash(
    name = "frailty_screener", 
    external_stylesheets=[dbc.themes.MATERIA],
    title = "Frailty Screener",
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ]
)

server = app.server