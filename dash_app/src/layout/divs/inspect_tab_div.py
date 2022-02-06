from dash import html
from dash import dash_table
from src.layout import main_tab_content_style, get_margins


def section_style(width=45, height=35):
    return dict(
        {
            "display": "inline-block",
            "borderColor": "lightgrey",
            "borderWidth": "2px",
            "borderStyle": "solid",
            "borderRadius": "5px",
            "width": f"{width}%",
            "height": f"{height}vh",
            "textAlign": "center",
        },
        **get_margins(2, "v"),
    )

section_title_style = {"position":"absolute","margin":"10px"}


def inspect_tab_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Data shape", style=section_title_style),
                            html.Div(
                                [
                                    html.P(
                                        id="inspect-size",
                                        style={
                                            "position":"absolute",
                                            "margin-top":"12vh",
                                            "fontSize": 25,
                                            "width": "35vw",
                                        },
                                    ),
                                    html.P(
                                        id="inspect-variables",
                                        style={
                                            "position":"absolute",
                                            "margin-top":"20vh",
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
                        style=section_style(35)
                    ),
                    html.Div(
                        [
                            html.P("Variables info", style=section_title_style),
                            table_div("info", 51, 13),
                        ],
                        style=section_style(55)
                    ),
                ],
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Descriptive statistics", style=section_title_style),
                            table_div("stats", 90, 22)
                        ],
                        style=section_style(width=94, height=55)
                    ),
                ],
            ),
        ],
        style = dict(
            main_tab_content_style(height=100),
            **{"textAlign": "center"},
        )
    )


def table_div(name, width, height):
    return html.Div(
        [
            dash_table.DataTable(
                id=f"inspect-{name}",
                columns=[],
                sort_action="native",
                fixed_rows={'headers': True},
                style_header={"backgroundColor": "whitesmoke"},
                style_table={
                    "overflowY": "auto",
                    "margin-top":"6vh",
                    "margin-left":"2vh",
                    "position":"absolute",
                    "width": f"{width}vw",
                    "height": f"{height}vw",
                },
                style_cell={
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 0
                },
            ),
        ],
        style={"position":"absolute"},
    )
