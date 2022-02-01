from dash import dcc
from dash import html
from dash import dash_table

import dash_daq as daq



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
                        'width': '49%',
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
                        'width': '49%',
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
                            value='tab-upload',
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
                                    style={"backgroundColor": "transparent", 'height': '75vh'}
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label='View data',
                            value='tab-view',
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
                                    page_size=50,
                                ),
                            ],
                        ),
                        dcc.Tab(
                            label='Inspect data',
                            value='tab-inspect',
                            children=[],
                        ),
                        dcc.Tab(
                            label='Visualise data',
                            value='tab-graphs',
                            children=[],
                        ),
                    ],
                    # vertical=True,
                ),
            ],
            id="div-upload-file",
            style={
                "height": "90vh",
                "backgroundColor": "yellow"
            },
        ),
        dcc.Store(id='uploaded-data')
    ],
    id="div-all",
    # style={
    #     "height": "100vh",
    # },
)
