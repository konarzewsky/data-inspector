import plotly.express as px
import pandas as pd
from src.layout.graphs import transparent_plot


def box_plot(data, main, group, color):
    df = pd.DataFrame(data)
    return px.box(
        df,
        x=group,
        y=main,
        color=color,
    ).update_layout(transparent_plot)
