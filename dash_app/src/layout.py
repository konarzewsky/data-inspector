from dash import dcc
from dash import html
from dash import dash_table
from pathlib import Path
import os
import base64
import dash_daq as daq
from src.dash_app import dash_app
from config.env_config import config


layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H1('DATA INSPECTOR'),
                    ],
                    style={
                        'display': 'inline-block',
                        'width': '60%',
                        'backgroundColor': 'transparent',
                    },
                ),
                html.Div(
                    [
                        daq.ToggleSwitch(
                            id="theme-toggle-switch",
                            label='Light/dark theme switch',
                            labelPosition='top',
                            value=False,
                        ),
                    ],
                    style={
                        'display': 'inline-block',
                        'width': '20%',
                        'backgroundColor': 'transparent',
                    },
                ),
                html.Div(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=config['LINKEDIN_LOGO_URL'],
                                    style={
                                        'height': '60px',
                                        'float' : 'right',
                                        'position' : 'relative',
                                        'padding-top' : 0,
                                        'padding-right' : 0
                                    },
                                )
                            ], href=config['LINKEDIN_PROFILE_URL']
                        ),
                    ],
                    style={
                        'display': 'inline-block',
                        'width': '9%',
                        'backgroundColor': 'transparent',
                    },
                ),
                html.Div(
                    [
                        html.A(
                            [
                                html.Img(
                                    src=config['GITHUB_LOGO_URL'],
                                    style={
                                        'height': '60px',
                                        'float' : 'right',
                                        'position' : 'relative',
                                        'padding-top' : 0,
                                        'padding-right' : 0
                                    },
                                )
                            ], href=config['GITHUB_REPO_URL']
                        ),
                    ],
                    style={
                        'display': 'inline-block',
                        'width': '9%',
                        'backgroundColor': 'transparent',
                    },
                ),
            ],
            id="div-top-panel",
            style={
                'backgroundColor': 'lightgrey',
                'height': '20vh',
            },
        ),
        html.Div(
            [
                dcc.Tabs(
                    id="tabs",
                    value='tab-upload',
                    children=[
                        dcc.Tab(
                            label='Upload data',
                            id='tab-upload',
                            value='tab-upload',
                            disabled=False,
                            children=[
                                html.Div(
                                    [
                                        dcc.Upload(
                                            id='upload-data',
                                            children=html.Div(
                                                [
                                                    'Drag and drop your files here or ',
                                                    html.A('select'),
                                                ]
                                            ),
                                            style={
                                                'width': '90%',
                                                'height': '250px',
                                                'lineHeight': '250px',
                                                'borderWidth': '1px',
                                                'borderStyle': 'dashed',
                                                'borderRadius': '5px',
                                                'textAlign': 'center',
                                                'verticalAlign': 'middle',
                                                'margin': '5%',
                                                'display': 'inline-block',
                                                'fontSize': 20,
                                            },
                                            multiple = True,
                                        ),
                                        dcc.ConfirmDialog(
                                            id='uplod-error',
                                        ),
                                    ],
                                    style={
                                        "backgroundColor": "transparent",
                                        'height': '75vh'
                                    },
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label='View data',
                            id='tab-view',
                            value='tab-view',
                            disabled=True,
                            children=[
                                dcc.Loading(
                                    id="table-loading",
                                    type="circle",
                                    children=[
                                        dash_table.DataTable(
                                            id="data-table",
                                            columns=[],
                                            sort_action="native",
                                            filter_action="native",
                                            style_header={
                                                "backgroundColor": "lightgrey"
                                            },
                                            style_table={"overflowY": "auto"},
                                            page_size=25,
                                        ),
                                    ],
                                    style={
                                        'padding-top':'15%'
                                    }
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label='Inspect data',
                            id='tab-inspect',
                            value='tab-inspect',
                            disabled=True,
                            children=[],
                        ),
                        dcc.Tab(
                            label='Visualise data',
                            id='tab-graphs',
                            value='tab-graphs',
                            disabled=True,
                            children=[
                                html.Div(
                                    [
                                        dcc.Tabs(
                                            id="tab-graphs-tabs",
                                            value='tab-graphs-tab-scatter',
                                            vertical=True,
                                            style={
                                                "width": "10vw"
                                            },
                                            children=[
                                                dcc.Tab(
                                                    label='SCATTER',
                                                    value='tab-graphs-tab-scatter',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-scatter",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='LINE',
                                                    value='tab-graphs-tab-line',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-line",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='BAR',
                                                    value='tab-graphs-tab-bar',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-bar",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='PIE',
                                                    value='tab-graphs-tab-pie',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-pie",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='HISTOGRAM',
                                                    value='tab-graphs-tab-histogram',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-histogram",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='BOX',
                                                    value='tab-graphs-tab-box',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-box",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='MAP',
                                                    value='tab-graphs-tab-map',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-map",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='CLUSTERING',
                                                    value='tab-graphs-tab-cluster',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-cluster",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                dcc.Tab(
                                                    label='ML',
                                                    value='tab-graphs-tab-ml',
                                                    children=[
                                                        html.Div(
                                                            [
                                                                dcc.Graph(
                                                                    id="graph-ml",
                                                                    style={
                                                                        "height": "75vh",
                                                                        "width": "85vw"
                                                                    },
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
                        ),
                    ],
                ),
            ],
            id="div-upload-file",
            style={
                "height": "90vh",
            },
        ),
        dcc.Store(id='uploaded-data')
    ],
    id="div-all",
    # style={
    #     "height": "100vh",
    # },
)
