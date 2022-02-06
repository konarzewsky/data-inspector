from dash import dcc
from dash import html
import dash_daq as daq
from src.layout.margins import get_margins
from src.layout.graph_style import component_style


corr_components = html.Div(
    [
        html.Div(
            [
                html.P("Method of correlation"),
                dcc.Dropdown(
                    id="corr-method",
                    options=[
                        {"label": method, "value": method} for method in ["pearson", "kendall", "spearman"]
                    ],
                    value="pearson",
                    clearable=False,
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
