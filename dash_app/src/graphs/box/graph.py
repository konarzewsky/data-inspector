import plotly.express as px
import pandas as pd
from src.layout.graph_style import transparent_plot


def box_plot(data, main, group, color):
    df = pd.DataFrame(data)
    return px.box(
        df,
        x=group,
        y=main,
        color=color,
        title=f"Box plot of {main}",
    ).update_layout(transparent_plot)
