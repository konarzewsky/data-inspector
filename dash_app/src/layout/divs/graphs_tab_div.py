from dash import dcc
from dash import html
from src.layout import (
    plot_tabs_style,
    plot_tab_style,
    plot_tab_selected_style,
    main_tab_content_style,
)
from src.consts import PLOT_NAMES


def graphs_tab_layout(plot_div, components):
    return html.Div(
        [
            dcc.Tabs(
                id="tab-graphs-tabs",
                value="tab-graphs-tab-scatter",
                vertical=True,
                style=dict(
                    {"width": "10vw"},
                    **plot_tabs_style,
                ),
                children=[
                    dcc.Tab(
                        label=plot_name.upper(),
                        value=f"tab-graphs-tab-{plot_name}",
                        children=[plot_div(plot_name, components)],
                        style=plot_tab_style,
                        selected_style=plot_tab_selected_style,
                    )
                    for plot_name in PLOT_NAMES
                ],
            ),
        ],
        style = main_tab_content_style(height=125),
    )
