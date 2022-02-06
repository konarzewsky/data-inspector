from src.layout.margins import get_margins


component_style = dict(
    {
        "width": "30%",
        "display": "inline-block",
    },
    **get_margins(10, "px"),
)

transparent_plot = {
    'plot_bgcolor': 'rgba(0,0,0,0)',
    'paper_bgcolor': 'rgba(0,0,0,0)',
}
