from dash import dcc
from dash import html
from dash import dash_table
from pathlib import Path
import os
import base64
import dash_daq as daq
from config.env_config import config
from src.layout import *
from src.graphs import components


def get_layout():
    return html.Div(
        [
            to_panel_layout(),
            html.Div(
                [
                    dcc.Tabs(
                        id="tabs",
                        value="tab-upload",
                        children=[
                            dcc.Tab(
                                label="Upload",
                                id="tab-upload",
                                value="tab-upload",
                                disabled=False,
                                style=main_tab_style,
                                selected_style=main_tab_selected_style,
                                children=[upload_tab_layout()],
                            ),
                            dcc.Tab(
                                label="View",
                                id="tab-view",
                                value="tab-view",
                                disabled=True,
                                style=main_tab_style,
                                selected_style=main_tab_selected_style,
                                children=[
                                    dcc.Loading(
                                        id="table-loading",
                                        type="circle",
                                        children=[view_tab_layout()],
                                        style={
                                            "padding-top": "15%",
                                            "backgroundColor": "transparent",
                                        },
                                    ),
                                ],
                            ),
                            dcc.Tab(
                                label="Inspect",
                                id="tab-inspect",
                                value="tab-inspect",
                                disabled=True,
                                style=main_tab_style,
                                selected_style=main_tab_selected_style,
                                children=[inspect_tab_layout()],
                            ),
                            dcc.Tab(
                                label="Visualise",
                                id="tab-graphs",
                                value="tab-graphs",
                                disabled=True,
                                style=main_tab_style,
                                selected_style=main_tab_selected_style,
                                children=[graphs_tab_layout(plot_div, components)],
                            ),
                        ],
                    ),
                ],
                id="div-upload-file",
                style={
                    "height": "90vh",
                },
            ),
            dcc.Store(id="uploaded-data"),
        ],
        id="div-all",
    )
