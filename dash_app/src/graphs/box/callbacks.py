from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import box_plot


logger = prepare_logger()


def init_callbacks_box(app):
    @app.callback(
        Output("box-group", "disabled"),
        Output("box-color", "disabled"),
        Input("box-main", "value"),
    )
    def control_components(main):
        return (False if main else True,) * 2

    @app.callback(
        Output("box-graph", "figure"),
        Output("box-message", "children"),
        Input("box-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("box-main", "value"),
        State("box-group", "value"),
        State("box-color", "value"),
    )
    def plot_box(n_clicks, data, main, group, color):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating box plot - in progress...")
        if not main:
            logger.warning("Creating box plot - variable not selected")
            return no_update, "Select aggregate function"
        figure = box_plot(data, main, group, color)
        logger.info("Creating box plot - done")
        return figure if figure else no_update, ""
