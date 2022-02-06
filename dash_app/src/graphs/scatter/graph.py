import plotly.express as px
import pandas as pd
from pandas.api.types import is_numeric_dtype
from src.layout.graph_style import transparent_plot


def scatter_plot(data, x, y, z, color, size, trendline):
    df = pd.DataFrame(data)
    if all(var is not None for var in [x, y, z]):
        return scatter_3d(df, x, y, z, color, size), ""
    elif x is not None and y is not None:
        return scatter_2d(df, x, y, color, size, trendline), ""
    else:
        return (
            None,
            "Select X-axis and Y-axis variables (and Z-axis variable optionally)",
        )


def scatter_2d(df, x, y, color, size, trendline):
    figure = px.scatter(
        df,
        x=x,
        y=y,
        color=color,
        size=size,
        trendline="ols"
        if (trendline and is_numeric_dtype(df[x]) and is_numeric_dtype(df[y]))
        else None,
        trendline_color_override="black",
        trendline_scope="overall",
        title=f"Scatter plot {x} vs {y}",
    )
    if not size:
        figure.update_traces(marker_size=5)
    return figure.update_layout(transparent_plot)


def scatter_3d(df, x, y, z, color, size):
    figure = px.scatter_3d(
        df,
        x=x,
        y=y,
        z=z,
        color=color,
        size=size,
        title=f"Scatter plot {x} vs {y} vs {z}",
    )
    if not size:
        figure.update_traces(marker_size=5)
    return figure.update_layout(transparent_plot)
