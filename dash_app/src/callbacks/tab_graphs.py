import pandas as pd
from pandas.api.types import is_numeric_dtype

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import *
from src.functions import check_coordinates


logger = prepare_logger()


def init_callbacks_tab_graphs(app):
    @app.callback(
        # all variables
        Output("scatter-x", "options"),
        Output("scatter-y", "options"),
        Output("scatter-z", "options"),
        Output("scatter-color", "options"),
        Output("map-color", "options"),
        Output("map-hover", "options"),
        # only numeric variables
        Output("scatter-size", "options"),
        Output("map-latitude", "options"),
        Output("map-longitude", "options"),
        Output("map-size", "options"),
        Input("uploaded-data", "data"),
    )
    def prepare_components(data):
        dropdown_options = {
            "all": sorted(
                [
                    {"label": column, "value": column}
                    for column in pd.DataFrame(data).columns
                ]
            ),
            "num": sorted(
                [
                    {"label": column, "value": column}
                    for column in pd.DataFrame(data).columns
                    if is_numeric_dtype(pd.DataFrame(data)[column])
                ]
            ),
        }
        return (dropdown_options["all"],) * 6 + (dropdown_options["num"],) * 4

    @app.callback(
        Output("scatter-y", "disabled"),
        Input("scatter-x", "value"),
    )
    def control_components_1(x):
        return False if x else True

    @app.callback(
        Output("scatter-z", "disabled"),
        Output("scatter-trendline", "disabled"),
        Input("scatter-y", "value"),
        Input("scatter-z", "value"),
    )
    def control_components_2(y, z):
        return (False if y else True,) * 2

    @app.callback(
        Output("scatter-graph", "figure"),
        Output("scatter-message", "children"),
        Input("scatter-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("scatter-x", "value"),
        State("scatter-y", "value"),
        State("scatter-z", "value"),
        State("scatter-color", "value"),
        State("scatter-size", "value"),
        State("scatter-trendline", "on"),
    )
    def plot_scatter(n_clicks, data, x, y, z, color, size, trendline):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating scatter plot - in progress...")
        figure, message = scatter_plot(data, x, y, z, color, size, trendline)
        if message == "":
            logger.info("Creating scatter plot - done")
        else:
            logger.warning("Creating scatter plot - failed")
        return (
            figure if figure else no_update,
            message,
        )

    @app.callback(
        Output("map-graph", "figure"),
        Output("map-message", "children"),
        Input("map-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("map-latitude", "value"),
        State("map-longitude", "value"),
        State("map-style", "value"),
        State("map-color", "value"),
        State("map-size", "value"),
        State("map-hover", "value"),
    )
    def plot_map(n_clicks, data, lat, lon, style, color, size, hover):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating map plot - in progress...")
        if not check_coordinates(data, lat, lon):
            logger.warning("Creating scatter plot - failed")
            return None, "Invalid coordinates"
        figure, message = map_plot(data, lat, lon, style, color, size, hover)
        logger.info("Creating map plot - done")
        return (
            figure if figure else no_update,
            message,
        )
