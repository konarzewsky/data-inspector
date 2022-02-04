import pandas as pd

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger


logger = prepare_logger()


def init_callbacks_tab_view(app):
    @app.callback(
        Output("data-table", "data"),
        Output("data-table", "columns"),
        Input("uploaded-data", "data"),
    )
    def display_datatable(data):
        logger.info("Preparing table - in progress...")
        columns = [
            {"name": i, "id": i, "presentation": "markdown", "hideable": True}
            for i in pd.DataFrame(data).columns
        ]
        logger.info("Preparing table - done")
        return data, columns
