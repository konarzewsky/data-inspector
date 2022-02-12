from dash import dcc
from dash import html
from src.layout import (
    main_tab_content_style,
    section_style,
)
from src.consts import EMAIL_REGEX


def report_tab_layout():
    return html.Div(
        [
            html.Div(
                [
                    html.P(
                        children=["Generate report containing descriptive statistics of your dataset and created graphs"],
                        style={"fontSize": 25},
                    ),
                ],
                style={
                    "width": "100%",
                    "height": "20vh",
                    "textAlign": "center",
                    'verticalAlign': 'middle',
                    'lineHeight': '20vh',
                },
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.P("Download report as a PDF file"),
                            html.Button(
                                "Download",
                                id="download-pdf-button",
                            ),
                            dcc.Download(
                                id="download-pdf",
                            ),
                        ],
                        style=dict(
                            {
                                'verticalAlign': 'middle',
                                'lineHeight': '8vh',
                            },
                            **section_style(30, 20),
                        ),
                    ),
                    html.Div(
                        [
                            html.P("Send report to email address (only gmail)"),
                            dcc.Input(
                                id="email-input",
                                pattern=EMAIL_REGEX,
                                placeholder="your email address",
                                value="",
                            ),
                            html.Button(
                                "Send",
                                id="send-email-button",
                            ),
                        ],
                        style=dict(
                            {
                                'verticalAlign': 'middle',
                                'lineHeight': '8vh',
                            },
                            **section_style(30, 20),
                        ),
                    ),
                    dcc.ConfirmDialog(
                        id="email-error",
                    ),
                ],
                style={
                    "width": "100%",
                    "height": "20vh",
                    "textAlign": "center",
                },
            ),
        ],
        style=main_tab_content_style(),
    )