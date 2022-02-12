from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import corr_plot
from src.functions import save_figure


logger = prepare_logger()


def init_callbacks_corr(app):
    @app.callback(
        Output("corr-graph", "figure"),
        Output("corr-message", "children"),
        Input("corr-button", "n_clicks"),
        State("uploaded-data", "data"),
        State("corr-method", "value"),
    )
    def plot_corr(n_clicks, data, method):
        if n_clicks is None:
            raise PreventUpdate
        logger.info("Creating corr plot - in progress...")
        figure = corr_plot(data, method)
        logger.info("Creating corr plot - done")
        if figure:
            save_figure(figure, "corr")
        return figure if figure else no_update, ""
