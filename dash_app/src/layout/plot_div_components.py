from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.consts import MAP_STYLES


component_style = dict(
    {
        "width": "30%",
        "display": "inline-block",
    },
    **get_margins(10, "px"),
)

components = {}

components["map"] = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.P("Latitude variable"),
                        dcc.Dropdown(
                            id="map-latitude",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Longitude variable"),
                        dcc.Dropdown(
                            id="map-longitude",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Map style"),
                        dcc.Dropdown(
                            id="map-style",
                            options=[
                                {"label": style, "value": style} for style in MAP_STYLES
                            ],
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
                            id="map-color",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Marker size"),
                        dcc.Dropdown(
                            id="map-size",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Hover data"),
                        dcc.Dropdown(
                            id="map-hover",
                            multi=True,
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

components["line"] = html.Div([])

components["bar"] = html.Div([])

components["pie"] = html.Div([])

components["histogram"] = html.Div([])

components["box"] = html.Div([])

components["scatter"] = html.Div(
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
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Marker size"),
                        dcc.Dropdown(
                            id="scatter-size",
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Add trendline (ols)"),
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

components["cluster"] = html.Div([])


def get_components(plot_name):
    return components[plot_name]
