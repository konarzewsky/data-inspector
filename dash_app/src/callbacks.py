import pandas as pd

from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from src.dash_app import dash_app
from src.utils import prepare_logger
from src.functions import parse_contents

logger = prepare_logger()

THEME = {
    "light": {
        "fontColor": "black",
        "backgroundColor": "white",
    },
    "dark": {
        "fontColor": "white",
        "backgroundColor": "black",
    },
}


@dash_app.callback(
    Output("div-top-panel", 'style'),
    Output("div-upload-file", 'style'),
    Input('theme-toggle-switch', 'value'),
)
def switch_theme(switch_value):
    if switch_value:
        return (
            {
                'backgroundColor': 'black',
            },
            {
                'backgroundColor': 'dimgray',
            }
        )
    else:
        return (
            {
                'backgroundColor': 'lightgrey',
            },
            {
                'backgroundColor': 'white',
            }
        )


@dash_app.callback(
    Output('tabs', 'value'),
    Output('uplod-error', 'displayed'),
    Output('uplod-error', 'message'),
    Output('uploaded-data', 'data'),
    Output('tab-view', 'disabled'),
    Output('tab-inspect', 'disabled'),
    Output('tab-graphs', 'disabled'),
    Input('upload-data', 'contents'),
    State('upload-data', 'filename'),
)
def load_data(contents, filename):
    if contents is None:
        raise PreventUpdate
    if len(filename) > 1:
        message = 'Please upload only one file.'
        return (
            'tab-upload',
            True,
            message,
            None,
            True,
            True,
            True,
        )
    logger.info(f"Uploading file {filename} - in progress...")
    data = parse_contents(contents, filename)
    if isinstance(data, pd.DataFrame):
        logger.info(f"Uploading file {filename} - finished")
        return (
            'tab-view',
            False,
            "",
            data.to_dict("records"),
            False,
            False,
            False,
        )
    else:
        message = 'An error occurred while loading the file.\n\n Try another file.'
        return (
            'tab-upload',
            True,
            message,
            None,
            True,
            True,
            True,
        )


@dash_app.callback(
    Output('data-table', 'data'),
    Output('data-table', 'columns'),
    Input('uploaded-data', 'data'),
)
def display_datatable(data):
    cols = pd.DataFrame(data).columns
    columns = [
        {"name": i, "id": i, "presentation": "markdown", "hideable": True} for i in cols
    ]
    return data, columns
    