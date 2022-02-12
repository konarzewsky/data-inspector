from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import histogram_plot
from src.functions import save_figure


logger = prepare_logger()


def init_callbacks_histogram(app):
    @app.callback(
        Output("histogram-color", "disabled"),
        Output("histogram-bins", "disabled"),
        Output("histogram-norm", "disabled"),
        Input("histogram-x", "value"),
    )
    def control_components(x):
        return (False if x else True,) * 3

    @app.callback(
        Output("histogram-graph", "figure"),
        Output("histogram-message", "children"),
        Input("histogram-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("histogram-x", "value"),
        State("histogram-color", "value"),
        State("histogram-bins", "value"),
        State("histogram-norm", "value"),
    )
    def plot_histogram(n_clicks, data, x, color, bins, norm):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating histogram plot - in progress...")
        if not x:
            logger.warning("Creating histogram plot - variable not selected")
            return no_update, "Select variable"
        figure = histogram_plot(data, x, color, bins, norm)
        logger.info("Creating histogram plot - done")
        if figure:
            save_figure(figure, "histogram")
        return figure if figure else no_update, ""
