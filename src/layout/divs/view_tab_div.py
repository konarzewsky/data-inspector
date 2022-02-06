from dash import html
from dash import dash_table
from src.layout import main_tab_content_style


def view_tab_layout():
    return html.Div(
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
            html.P(
                [
                    "Filtering syntax ",
                    html.A(
                        "documentation",
                        href="https://dash.plotly.com/datatable/filtering",
                        target="_blank",
                    ),
                ],
            ),
        ],
        style=main_tab_content_style(),
    )
