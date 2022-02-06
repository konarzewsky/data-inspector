from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.graphs import scatter_plot


logger = prepare_logger()


def init_callbacks_scatter(app):

    @app.callback(
        Output("scatter-y", "disabled"),
        Input("scatter-x", "value"),
    )
    def control_y(x):
        return False if x else True

    @app.callback(
        Output("scatter-z", "disabled"),
        Output("scatter-trendline", "disabled"),
        Input("scatter-y", "value"),
        Input("scatter-z", "value"),
    )
    def control_z_trendline(y, z):
        return (False if y else True,) * 2

    @app.callback(
        Output("scatter-color", "disabled"),
        Output("scatter-size", "disabled"),
        Input("scatter-y", "value"),
    )
    def control_color_size(y):
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
