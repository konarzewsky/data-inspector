import pandas as pd

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.utils import prepare_logger
from src.functions import parse_contents


logger = prepare_logger()


def init_callbacks_tab_upload(app):
    @app.callback(
        Output("uplod-error", "displayed"),
        Output("uplod-error", "message"),
        Output("uploaded-data", "data"),
        Output("tab-view", "disabled"),
        Output("tab-inspect", "disabled"),
        Output("tab-graphs", "disabled"),
        Output("upload-data", "style"),
        Input("upload-data", "contents"),
        State("upload-data", "filename"),
        State("upload-data", "style"),
    )
    def load_data(contents, filename, upload_style):
        if contents is None:
            raise PreventUpdate
        if len(filename) > 1:
            message = "Please upload only one file."
            upload_style["backgroundColor"] = "rgba(255, 0, 0, 0.1)"
            return (
                True,
                message,
                None,
                True,
                True,
                True,
                upload_style,
            )
        logger.info(f"Uploading file {filename} - in progress...")
        data = parse_contents(contents, filename)
        if isinstance(data, pd.DataFrame):
            logger.info(f"Uploading file {filename} - finished")
            upload_style["backgroundColor"] = "rgba(144, 198, 149, 0.4)"
            return (
                False,
                "",
                data.to_dict("records"),
                False,
                False,
                False,
                upload_style,
            )
        else:
            message = "An error occurred while loading the file.\n\n Try another file."
            upload_style["backgroundColor"] = "rgba(255, 0, 0, 0.2)"
            return (
                True,
                message,
                None,
                True,
                True,
                True,
                upload_style,
            )
