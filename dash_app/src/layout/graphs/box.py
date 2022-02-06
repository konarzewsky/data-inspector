from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graphs import component_style


box_components = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("Variable"),
                        dcc.Dropdown(
                            id="box-main",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("X-axis grouping variable"),
                        dcc.Dropdown(
                            id="box-group",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Color grouping variable"),
                        dcc.Dropdown(
                            id="box-color",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
            ],
        ),
    ],
    style=dict(
        {"textAlign": "center"},
        **get_margins(4, "v"),
    ),
)
