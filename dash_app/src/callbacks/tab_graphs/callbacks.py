import pandas as pd
from pandas.api.types import is_numeric_dtype

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger

from src.callbacks.tab_graphs.scatter import init_callbacks_scatter
from src.callbacks.tab_graphs.map import init_callbacks_map
from src.callbacks.tab_graphs.line import init_callbacks_line
from src.callbacks.tab_graphs.bar import init_callbacks_bar
from src.callbacks.tab_graphs.box import init_callbacks_box
from src.callbacks.tab_graphs.corr import init_callbacks_corr
from src.callbacks.tab_graphs.histogram import init_callbacks_histogram


logger = prepare_logger()


def init_callbacks_tab_graphs(app):

    @app.callback(
        # output: all variables
        Output("scatter-x", "options"),
        Output("scatter-y", "options"),
        Output("scatter-z", "options"),
        Output("scatter-color", "options"),
        Output("map-color", "options"),
        Output("map-hover", "options"),
        Output("line-x", "options"),
        Output("line-color", "options"),
        Output("bar-x", "options"),
        Output("bar-y", "options"),
        Output("bar-color", "options"),
        Output("box-group", "options"),
        Output("box-color", "options"),
        Output("histogram-x", "options"),
        Output("histogram-color", "options"),
        # output: only numeric variables
        Output("scatter-size", "options"),
        Output("map-latitude", "options"),
        Output("map-longitude", "options"),
        Output("map-size", "options"),
        Output("line-y", "options"),
        Output("box-main", "options"),
        # output: set values to None
        Output("scatter-x", "value"),
        Output("scatter-y", "value"),
        Output("scatter-z", "value"),
        Output("scatter-color", "value"),
        Output("scatter-size", "value"),
        Output("map-latitude", "value"),
        Output("map-longitude", "value"),
        Output("map-color", "value"),
        Output("map-size", "value"),
        Output("map-hover", "value"),
        Output("line-x", "value"),
        Output("line-y", "value"),
        Output("line-color", "value"),
        # input: data
        Input("uploaded-data", "data"),
    )
    def prepare_components(data):
        dropdown_options = {
            "all": sorted(
                [
                    {"label": column, "value": column}
                    for column in pd.DataFrame(data).columns
                ],
                key = lambda d: d['label'],
            ),
            "num": sorted(
                [
                    {"label": column, "value": column}
                    for column in pd.DataFrame(data).columns
                    if is_numeric_dtype(pd.DataFrame(data)[column])
                ],
                key = lambda d: d['label'],
            ),
        }
        return (dropdown_options["all"],) * 15 + (dropdown_options["num"],) * 6 + (None,) * 13

    init_callbacks_scatter(app)
    init_callbacks_map(app)
    init_callbacks_line(app)
    init_callbacks_bar(app)
    init_callbacks_box(app)
    init_callbacks_corr(app)
    init_callbacks_histogram(app)
