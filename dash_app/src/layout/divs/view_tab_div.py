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
        ],
        style=main_tab_content_style(),
    )
