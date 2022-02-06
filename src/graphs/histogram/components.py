from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graph_style import component_style
from src.consts import HISTOGRAM_NORM


histogram_components = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("Variable"),
                        dcc.Dropdown(
                            id="histogram-x",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Color variable"),
                        dcc.Dropdown(
                            id="histogram-color",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Normalization type"),
                        dcc.Dropdown(
                            id="histogram-norm",
                            disabled=True,
                            options=[
                                {"label": norm, "value": norm}
                                for norm in HISTOGRAM_NORM
                            ],
                            value="count",
                            clearable=False,
                        ),
                    ],
                    style=component_style,
                ),
            ],
        ),
        html.Div(
            [
                html.P("Number of bins"),
                dcc.Slider(
                    id="histogram-bins",
                    disabled=True,
                    min=0,
                    max=500,
                    value=200,
                    step=1,
                    marks=None,
                    tooltip={
                        "always_visible": True,
                        "placement": "bottom",
                    },
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
