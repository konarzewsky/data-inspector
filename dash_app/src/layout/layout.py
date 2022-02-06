from dash import dcc
from dash import html
from dash import dash_table
from pathlib import Path
import os
import base64
import dash_daq as daq
from config.env_config import config
from src.layout import *
from src.consts import PLOT_NAMES


def get_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H1(
                                [
                                    html.P("DATA INSPECTOR", style={"fontSize":45, "display": "inline-block", }),
                                    html.P("get to know your data better", style={"fontSize":25, "display": "inline-block","margin-left": "20px",}),
                                ],
                                style={
                                    "fontFamily": "courier",
                                    "margin-left": "20px",
                                    "verticalAlign": "middle",
                                },
                            ),
                        ],
                        style={
                            "display": "inline-block",
                            "width": "80%",
                            "backgroundColor": "transparent",
                        },
                    ),
                    html.Div(
                        [
                            daq.ToggleSwitch(
                                id="theme-toggle-switch",
                                labelPosition="top",
                                value=False,
                                style={
                                    "textAlign": "center",
                                    "verticalAlign": "middle",
                                },
                            ),
                        ],
                        style={
                            "display": "inline-block",
                            "width": "10%",
                            "backgroundColor": "transparent",
                        },
                    ),
                    html.Div(
                        [
                            html.A(
                                [
                                    html.Img(
                                        src=config["LINKEDIN_LOGO_URL"],
                                        style={
                                            "height": "40px",
                                            "textAlign": "left",
                                            "verticalAlign": "middle",
                                        },
                                    )
                                ],
                                href=config["LINKEDIN_PROFILE_URL"],
                            ),
                        ],
                        style={
                            "display": "inline-block",
                            "width": "4.5%",
                            "backgroundColor": "transparent",
                        },
                    ),
                    html.Div(
                        [
                            html.A(
                                [
                                    html.Img(
                                        src=config["GITHUB_LOGO_URL"],
                                        style={
                                            "height": "40px",
                                            "textAlign": "center",
                                            "verticalAlign": "middle",
                                        },
                                    )
                                ],
                                href=config["GITHUB_REPO_URL"],
                            ),
                        ],
                        style={
                            "display": "inline-block",
                            "width": "4.5%",
                            "backgroundColor": "transparent",
                        },
                    ),
                ],
                id="div-top-panel",
                style={
                    "backgroundColor": "silver",
                },
            ),
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
                                children=[
                                    html.Div(
                                        [
                                            dcc.Upload(
                                                id="upload-data",
                                                children=html.Div(
                                                    [
                                                        "Drag and drop your files here or ",
                                                        html.A("select"),
                                                    ]
                                                ),
                                                style={
                                                    "width": "90%",
                                                    "height": "250px",
                                                    "lineHeight": "250px",
                                                    "borderWidth": "1px",
                                                    "borderStyle": "dashed",
                                                    "borderRadius": "5px",
                                                    "textAlign": "center",
                                                    "verticalAlign": "middle",
                                                    "margin": "5%",
                                                    "display": "inline-block",
                                                    "fontSize": 20,
                                                    "backgroundColor": "white",
                                                },
                                                multiple=True,
                                            ),
                                            dcc.ConfirmDialog(
                                                id="uplod-error",
                                            ),
                                        ],
                                        style = main_tab_content_style(),
                                    ),
                                ],
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
                                        children=[
                                            html.Div(
                                                [
                                                    dash_table.DataTable(
                                                        id="data-table",
                                                        columns=[],
                                                        sort_action="native",
                                                        filter_action="native",
                                                        style_header={
                                                            "backgroundColor": "lightgrey",
                                                        },
                                                        style_table={
                                                            "overflowY": "auto",
                                                            "padding-top": "10px",
                                                        },
                                                        page_size=12,
                                                    ),
                                                ],
                                                style = main_tab_content_style(),
                                            ),
                                        ],
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
                                children=[
                                    html.Div(
                                        [

                                        ],
                                        style = main_tab_content_style(),
                                    ),
                                ],
                            ),
                            dcc.Tab(
                                label="Visualise",
                                id="tab-graphs",
                                value="tab-graphs",
                                disabled=True,
                                style=main_tab_style,
                                selected_style=main_tab_selected_style,
                                children=[
                                    html.Div(
                                        [
                                            dcc.Tabs(
                                                id="tab-graphs-tabs",
                                                value="tab-graphs-tab-scatter",
                                                vertical=True,
                                                style=dict(
                                                    {"width": "10vw"},
                                                    **plot_tabs_style,
                                                ),
                                                children=[
                                                    dcc.Tab(
                                                        label=plot_name.upper(),
                                                        value=f"tab-graphs-tab-{plot_name}",
                                                        children=[plot_div(plot_name)],
                                                        style=plot_tab_style,
                                                        selected_style=plot_tab_selected_style,
                                                    )
                                                    for plot_name in PLOT_NAMES
                                                ],
                                            ),
                                        ],
                                        style = main_tab_content_style(height=125),
                                    ),
                                ],
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
