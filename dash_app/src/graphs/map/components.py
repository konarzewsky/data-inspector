from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graph_style import component_style
from src.consts import MAP_STYLES


map_components = html.Div(
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
                            disabled=True,
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
                            disabled=True,
                        ),
                    ],
                    style=component_style,
                ),
                html.Div(
                    [
                        html.P("Marker size"),
                        dcc.Dropdown(
                            id="map-size",
                            disabled=True,
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
