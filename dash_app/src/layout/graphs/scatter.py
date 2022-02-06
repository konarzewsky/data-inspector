from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graphs import component_style


scatter_components = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("X-axis variable"),
                        dcc.Dropdown(
                            id="scatter-x",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Y-axis variable"),
                        dcc.Dropdown(
                            id="scatter-y",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Z-axis variable"),
                        dcc.Dropdown(
                            id="scatter-z",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
            ],
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.P("Marker color"),
                        dcc.Dropdown(
                            id="scatter-color",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Marker size"),
                        dcc.Dropdown(
                            id="scatter-size",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("OLS trendline"),
                        daq.BooleanSwitch(
                            id="scatter-trendline",
                            on=False,
                            disabled=True,
                            color="green",
                        ),
                    ],
                    style=dict(
                        component_style,
                        **{"verticalAlign": "bottom"},
                    ),
                ),
            ],
        ),
    ],
    style=dict(
        {"textAlign": "center"},
        **get_margins(4, "v"),
    ),
)