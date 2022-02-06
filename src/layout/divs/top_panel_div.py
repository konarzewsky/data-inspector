from dash import html
import dash_daq as daq
from config.env_config import config


def to_panel_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.H1(
                        [
                            html.P(
                                "DATA INSPECTOR",
                                style={
                                    "fontSize": 45,
                                    "display": "inline-block",
                                },
                            ),
                            html.P(
                                "get to know your data better",
                                style={
                                    "fontSize": 25,
                                    "display": "inline-block",
                                    "margin-left": "20px",
                                },
                            ),
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
                    "width": "90%",
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
            "backgroundColor": "white",
        },
    )
