from dash import dcc
from dash import html
from src.layout import main_tab_content_style


def upload_tab_layout():
    return html.Div(
        [
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    [
                        "Drag and drop your file here or ",
                        html.A("select"),
                        html.P("supported types:    csv    xls    xlsx", style={"fontSize":15}),
                    ]
                ),
                style={
                    "width": "90%",
                    "height": "250px",
                    "lineHeight": "150px",
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
    )