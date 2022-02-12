from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import line_plot
from src.functions import save_figure


logger = prepare_logger()


def init_callbacks_line(app):
    @app.callback(
        Output("line-y", "disabled"),
        Output("line-color", "disabled"),
        Output("line-agg", "disabled"),
        Input("line-x", "value"),
    )
    def control_components(x):
        return (False if x else True,) * 3

    @app.callback(
        Output("line-graph", "figure"),
        Output("line-message", "children"),
        Input("line-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("line-x", "value"),
        State("line-y", "value"),
        State("line-color", "value"),
        State("line-agg", "value"),
    )
    def plot_line(n_clicks, data, x, y, color, function):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating line plot - in progress...")
        if not x or not y:
            logger.warning("Creating line plot - variables not provided")
            return no_update, "Select X-axis and Y-axis variables"
        if not function:
            logger.warning("Creating line plot - function not selected")
            return no_update, "Select aggregate function"
        figure = line_plot(data, x, y, color, function)
        logger.info("Creating line plot - done")
        if figure:
            save_figure(figure, "line")
        return figure if figure else no_update, ""
