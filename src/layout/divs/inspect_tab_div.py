from dash import html
from dash import dcc
from dash import dash_table
from src.layout import (
    main_tab_content_style,
    section_style,
)


section_title_style = {"position": "absolute", "margin": "10px"}


def inspect_tab_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Data shape", style=section_title_style),
                            dcc.Loading(
                                id="data-shape-loading",
                                type="circle",
                                children=[
                                    html.Div(
                                        [
                                            html.P(
                                                id="inspect-size",
                                                style={
                                                    "position": "absolute",
                                                    "margin-top": "12vh",
                                                    "fontSize": 25,
                                                    "width": "35vw",
                                                },
                                            ),
                                            html.P(
                                                id="inspect-variables",
                                                style={
                                                    "position": "absolute",
                                                    "margin-top": "20vh",
                                                    "fontSize": 25,
                                                    "width": "35vw",
                                                },
                                            ),
                                        ],
                                        style={
                                            "width": "100%",
                                            "height": "25vh",
                                            "textAlign": "center",
                                        },
                                    ),
                                ],
                                style={
                                    "margin-top": "20vh",
                                    "backgroundColor": "transparent",
                                },
                            ),
                        ],
                        style=section_style(35),
                    ),
                    html.Div(
                        [
                            html.P("Variables info", style=section_title_style),
                            dcc.Loading(
                                id="info-table-loading",
                                type="circle",
                                children=[table_div("info", 51, 13)],
                                style={
                                    "margin-top": "20vh",
                                    "backgroundColor": "transparent",
                                },
                            ),
                        ],
                        style=section_style(55),
                    ),
                ],
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Descriptive statistics", style=section_title_style),
                            dcc.Loading(
                                id="stats-table-loading",
                                type="circle",
                                children=[table_div("stats", 90, 22)],
                                style={
                                    "margin-top": "20vh",
                                    "backgroundColor": "transparent",
                                },
                            ),
                        ],
                        style=section_style(width=94, height=55),
                    ),
                ],
            ),
        ],
        style=dict(
            main_tab_content_style(height=100),
            **{"textAlign": "center"},
        ),
    )


def table_div(name, width, height):
    return html.Div(
        [
            dash_table.DataTable(
                id=f"inspect-{name}",
                columns=[],
                sort_action="native",
                fixed_rows={"headers": True},
                style_header={"backgroundColor": "whitesmoke"},
                style_table={
                    "overflowY": "auto",
                    "margin-top": "6vh",
                    "margin-left": "2vh",
                    "position": "absolute",
                    "width": f"{width}vw",
                    "height": f"{height}vw",
                },
                style_cell={
                    "overflow": "hidden",
                    "textOverflow": "ellipsis",
                    "maxWidth": 0,
                },
            ),
        ],
        style={"position": "absolute"},
    )
