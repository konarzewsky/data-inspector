import plotly.express as px
import pandas as pd
from src.layout.graph_style import transparent_plot


def histogram_plot(data, x, color, bins, norm):
    df = pd.DataFrame(data)
    figure = px.histogram(
        df,
        x=x,
        color=color,
        nbins=bins,
        histnorm="" if norm == "count" else norm,
        title=f"{norm} histogram of {x}",
    )
    return figure.update_layout(bargap=0.2).update_layout(transparent_plot)
