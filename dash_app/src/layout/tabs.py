from src.layout import get_margins

main_tab_style = {
    'backgroundColor': 'whitesmoke',
    'border-color': 'gainsboro',
}

main_tab_selected_style = {
    'backgroundColor': 'white',
}

plot_tabs_style = {
    "margin-top": "10px",
    "margin-bottom": "10px",
    "margin-left": "10px",
}

plot_tab_style = {
    'backgroundColor': 'white',
}

plot_tab_selected_style = {
    'backgroundColor': 'whitesmoke',
}

def main_tab_content_style(height=75):
    return {
        'border-style': 'solid',
        'border-width': '2px',
        'border-color': 'gainsboro',
        "backgroundColor": "white",
        "height": f"{height}vh",
    }
