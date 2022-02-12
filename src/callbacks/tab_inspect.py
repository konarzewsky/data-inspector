import pandas as pd
from dash import no_update
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from src.functions import save_figure
from src.utils import prepare_logger

logger = prepare_logger()


def init_callbacks_tab_inspect(app):
    @app.callback(
        Output("inspect-size", "children"),
        Output("inspect-variables", "children"),
        Input("uploaded-data", "data"),
    )
    def prepare_components(data):
        df = pd.DataFrame(data)
        size = f"{df.shape[0]} observations"
        variables = f"{df.shape[1]} variables"
        return size, variables

    @app.callback(
        Output("inspect-info", "data"),
        Output("inspect-info", "columns"),
        Input("uploaded-data", "data"),
    )
    def prepare_info_table(data):
        df = pd.DataFrame(data)
        logger.info("Preparing info table - in progress...")
        df_info = pd.DataFrame(
            {
                "variable": list(df.columns),
                "type": df.dtypes.astype("str"),
                "missing values": df.count(),
                "unique values": df.nunique(),
            }
        ).reset_index(drop=True)
        df_info["missing values"] = df_info["missing values"].apply(
            lambda x: f"{len(df) - x} ({round(100*(len(df) - x)/len(df), 2)}%)"
        )
        columns = [
            {"name": i, "id": i, "presentation": "markdown"} for i in df_info.columns
        ]
        logger.info("Preparing info table - done")
        save_figure(df_info, "df_info", table=True)
        return df_info.to_dict("records"), columns

    @app.callback(
        Output("inspect-stats", "data"),
        Output("inspect-stats", "columns"),
        Input("uploaded-data", "data"),
    )
    def prepare_stats_table(data):
        df = pd.DataFrame(data)
        logger.info("Preparing stats table - in progress...")
        df_stats = (
            df.describe(include="all")
            .round(2)
            .transpose()
            .reset_index()
            .rename(columns={"index": "variable"})
            .fillna("")
        )
        columns = [
            {"name": i, "id": i, "presentation": "markdown"} for i in df_stats.columns
        ]
        logger.info("Preparing stats table - done")
        save_figure(df_stats, "df_stats", table=True)
        return df_stats.to_dict("records"), columns
