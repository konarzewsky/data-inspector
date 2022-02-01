from dash import Dash
from flask import Flask


external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
server = Flask(__name__)
dash_app = Dash(
    __name__,
    server=server,
    external_stylesheets=external_stylesheets,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1.0, maximum-scale=1.5, minimum-scale=1.0",
        }
    ],
)
