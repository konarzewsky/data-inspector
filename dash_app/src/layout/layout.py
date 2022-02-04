from dash import dcc
from dash import html
from dash import dash_table
from pathlib import Path
import os
import base64
import dash_daq as daq
from config.env_config import config
from src.layout import *


def get_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.H1(
                                "DATA INSPECTOR",
                                style={
                                    "fontFamily": "courier",
                                    "margin-left": "20px",
                                    "padding-top": "10px",
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
                    "backgroundColor": "lightgrey",
                    "height": "20vh",
                },
            ),
            html.Div(
                [
                    dcc.Tabs(
                        id="tabs",
                        value="tab-upload",
                        children=[
                            dcc.Tab(
                                label="Upload data",
                                id="tab-upload",
                                value="tab-upload",
                                disabled=False,
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
                                                },
                                                multiple=True,
                                            ),
                                            dcc.ConfirmDialog(
                                                id="uplod-error",
                                            ),
                                        ],
                                        style={
                                            "backgroundColor": "transparent",
                                            "height": "75vh",
                                        },
                                    ),
                                ],
                            ),
                            dcc.Tab(
                                label="View data",
                                id="tab-view",
                                value="tab-view",
                                disabled=True,
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
                                                            "backgroundColor": "lightgrey"
                                                        },
                                                        style_table={
                                                            "overflowY": "auto"
                                                        },
                                                        page_size=25,
                                                    ),
                                                ],
                                                style=get_margins(5, "v"),
                                            ),
                                        ],
                                        style={"padding-top": "15%"},
                                    ),
                                ],
                            ),
                            dcc.Tab(
                                label="Inspect data",
                                id="tab-inspect",
                                value="tab-inspect",
                                disabled=True,
                                children=[],
                            ),
                            dcc.Tab(
                                label="Visualise data",
                                id="tab-graphs",
                                value="tab-graphs",
                                disabled=True,
                                children=[
                                    html.Div(
                                        [
                                            dcc.Tabs(
                                                id="tab-graphs-tabs",
                                                value="tab-graphs-tab-scatter",
                                                vertical=True,
                                                style={"width": "10vw"},
                                                children=[
                                                    dcc.Tab(
                                                        label="SCATTER",
                                                        value="tab-graphs-tab-scatter",
                                                        children=[plot_div("scatter")],
                                                    ),
                                                    dcc.Tab(
                                                        label="LINE",
                                                        value="tab-graphs-tab-line",
                                                        children=[plot_div("line")],
                                                    ),
                                                    dcc.Tab(
                                                        label="BAR",
                                                        value="tab-graphs-tab-bar",
                                                        children=[plot_div("bar")],
                                                    ),
                                                    dcc.Tab(
                                                        label="PIE",
                                                        value="tab-graphs-tab-pie",
                                                        children=[plot_div("pie")],
                                                    ),
                                                    dcc.Tab(
                                                        label="HISTOGRAM",
                                                        value="tab-graphs-tab-histogram",
                                                        children=[
                                                            plot_div("histogram")
                                                        ],
                                                    ),
                                                    dcc.Tab(
                                                        label="BOX",
                                                        value="tab-graphs-tab-box",
                                                        children=[plot_div("box")],
                                                    ),
                                                    dcc.Tab(
                                                        label="MAP",
                                                        value="tab-graphs-tab-map",
                                                        children=[plot_div("map")],
                                                    ),
                                                    dcc.Tab(
                                                        label="CLUSTERING",
                                                        value="tab-graphs-tab-cluster",
                                                        children=[plot_div("cluster")],
                                                    ),
                                                ],
                                            ),
                                        ],
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
        # style={
        #     "height": "100vh",
        # },
    )
