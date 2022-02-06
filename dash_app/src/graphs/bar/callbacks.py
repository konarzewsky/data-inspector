from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import bar_plot


logger = prepare_logger()


def init_callbacks_bar(app):
    @app.callback(
        Output("bar-function", "disabled"),
        Output("bar-color", "disabled"),
        Output("bar-mode", "disabled"),
        Input("bar-x", "value"),
    )
    def control_components(x):
        return (False if x else True,) * 3

    @app.callback(
        Output("bar-y", "disabled"),
        Output("bar-y", "value"),
        Input("bar-function", "value"),
    )
    def control_components_2(function):
        if function == "sum":
            return False, no_update
        else:
            return True, None

    @app.callback(
        Output("bar-graph", "figure"),
        Output("bar-message", "children"),
        Input("bar-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("bar-x", "value"),
        State("bar-y", "value"),
        State("bar-function", "value"),
        State("bar-color", "value"),
        State("bar-mode", "value"),
    )
    def plot_bar(n_clicks, data, x, y, function, color, mode):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating bar plot - in progress...")
        if not x:
            logger.warning("Creating bar plot - X-axis variable not selected")
            return no_update, "Select X-axis variable"
        if not function:
            logger.warning("Creating bar plot - function not selected")
            return no_update, "Select aggregate function"
        if function == "sum" and not y:
            logger.warning("Creating bar plot - Y-axis variable not selected")
            return no_update, "Select Y-axis variable to calculate sums"
        figure = bar_plot(data, x, y, function, color, mode)
        logger.info("Creating bar plot - done")
        return figure if figure else no_update, ""
