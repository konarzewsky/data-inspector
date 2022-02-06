from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import map_plot
from src.functions import check_coordinates
from config.env_config import config


logger = prepare_logger()


def init_callbacks_map(app):
    @app.callback(
        Output("map-style", "disabled"),
        Output("map-color", "disabled"),
        Output("map-size", "disabled"),
        Output("map-hover", "disabled"),
        Input("map-latitude", "value"),
        Input("map-longitude", "value"),
    )
    def control_components(lat, lon):
        return (False if lat and lon else True,) * 4

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
        if not lat or not lon:
            logger.warning("Creating map plot - coordinates not provided")
            return no_update, "Select latitude and longitude variables"
        if not check_coordinates(data, lat, lon):
            logger.warning("Creating map plot - invalid coordinates")
            return no_update, "Invalid coordinates"
        figure = map_plot(
            data, lat, lon, style, color, size, hover, config["MAPBOX_ACCESS_TOKEN"]
        )
        logger.info("Creating map plot - done")
        return figure if figure else no_update, ""
