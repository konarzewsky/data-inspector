from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graph_style import component_style
from src.consts import BAR_AGG_FUNCTIONS


bar_components = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("X-axis variable"),
                        dcc.Dropdown(
                            id="bar-x",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Y-axis variable aggregation"),
                        dcc.Dropdown(
                            id="bar-function",
                            disabled=True,
                            options=[
                                {"label": function, "value": function}
                                for function in BAR_AGG_FUNCTIONS
                            ],
                            value="count",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Y-axis variable"),
                        dcc.Dropdown(
                            id="bar-y",
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
                        html.P("Bar color"),
                        dcc.Dropdown(
                            id="bar-color",
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Bar mode"),
                        dcc.Dropdown(
                            id="bar-mode",
                            disabled=True,
                            options=[
                                {"label": mode, "value": mode}
                                for mode in ["relative", "group", "overlay"]
                            ],
                            value="relative",
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
