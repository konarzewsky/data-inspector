import pandas as pd

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger


logger = prepare_logger()


def init_callbacks_theme(app):
    @app.callback(
        Output("div-top-panel", "style"),
        Output("div-upload-file", "style"),
        Input("theme-toggle-switch", "value"),
    )
    def switch_theme(switch_value):
        if switch_value:
            return (
                {
                    "backgroundColor": "black",
                },
                {
                    "backgroundColor": "dimgray",
                },
            )
        else:
            return (
                {
                    "backgroundColor": "lightgrey",
                },
                {
                    "backgroundColor": "white",
                },
            )
