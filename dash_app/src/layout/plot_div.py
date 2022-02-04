from dash import dcc
from dash import html
from src.layout.margins import get_margins
from src.layout.plot_div_components import get_components


def plot_div(plot_name):
    components = get_components(plot_name)
    return html.Div(
        [
            get_components(plot_name),
            html.Div(
                [
                    html.Button(
                        "CREATE",
                        id=f"{plot_name}-button",
                    ),
                    html.P(
                        id=f"{plot_name}-message",
                        style={"color": "red"},
                    ),
                ],
                style={"textAlign": "center"},
            ),
            html.Div(
                [
                    dcc.Graph(
                        id=f"{plot_name}-graph",
                        style={"height": "75vh", "width": "75vw"},
                    ),
                ],
                style=dict(
                    {"textAlign": "center"},
                    **get_margins(4, "v"),
                ),
            ),
        ],
    )
