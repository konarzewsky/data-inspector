from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graphs import component_style
from src.consts import LINE_AGG_FUNCTIONS


line_components = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("X-axis variable"),
                        dcc.Dropdown(
                            id="line-x",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Y-axis variable"),
                        dcc.Dropdown(
                            id="line-y",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Line color"),
                        dcc.Dropdown(
                            id="line-color",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
            ],
        ),
        html.Div(
            [
                html.P("Y-axis variable aggregation"),
                dcc.Dropdown(
                    id="line-agg",
                    disabled=True,
                    options=[
                        {"label": function, "value": function} for function in LINE_AGG_FUNCTIONS
                    ],
                ),
            ],
            style=component_style,
        ),
    ],
    style=dict(
        {"textAlign": "center"},
        **get_margins(4, "v"),
    ),
)
