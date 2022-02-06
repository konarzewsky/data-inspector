from dash import dcc
from dash import html
from src.layout.margins import get_margins
from src.layout.graph_style import transparent_plot


def get_components(plot_name, components):
    return components[plot_name]


def plot_div(plot_name, components):
    return html.Div(
        [
            get_components(plot_name, components),
            html.Div(
                [
                    html.Button(
                        "CREATE",
                        id=f"{plot_name}-button",
                        style={"backgroundColor": "white"},
                    ),
                    html.P(
                        id=f"{plot_name}-message",
                        style={"color": "red"},
                    ),
                ],
                style={"textAlign": "center"},
            ),
            dcc.Loading(
                id=f"{plot_name}-loading",
                type="graph",
                children=[
                    html.Div(
                        [
                            dcc.Graph(
                                id=f"{plot_name}-graph",
                                figure = {
                                    "layout": transparent_plot,
                                },
                                style={
                                    "height": "75vh",
                                    "width": "75vw",
                                },
                            ),
                        ],
                        style=dict(
                            {"textAlign": "center"},
                            **get_margins(4, "v"),
                        ),
                    ),
                ],
            ),
        ],
        style = {
            'border-style': 'solid',
            'border-width': '2px',
            'border-color': 'gainsboro',
            "backgroundColor": "whitesmoke",
            "margin-top": "10px",
        },
    )
