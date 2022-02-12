from src.layout import get_margins

main_tab_style = {
    "backgroundColor": "whitesmoke",
    "border-color": "gainsboro",
}

main_tab_selected_style = {
    "backgroundColor": "white",
}

plot_tabs_style = {
    "margin-top": "10px",
    "margin-bottom": "10px",
    "margin-left": "10px",
}

plot_tab_style = {
    "backgroundColor": "white",
}

plot_tab_selected_style = {
    "backgroundColor": "whitesmoke",
}


def main_tab_content_style(height=75):
    return {
        "border-style": "solid",
        "border-width": "2px",
        "border-color": "gainsboro",
        "backgroundColor": "white",
        "height": f"{height}vh",
    }


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
