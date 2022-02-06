import plotly.express as px
import pandas as pd
from src.layout.graphs import transparent_plot


def line_plot(data, x, y, color, function):
    df = aggregate_data(pd.DataFrame(data), x, color, function).sort_values(by=x)
    return px.line(
        df,
        x=x,
        y=y,
        color=color,
    ).update_layout(transparent_plot)


def aggregate_data(df, x, color, function):
    groups = [color, x] if color else x
    if function == "minimum":
        df = df.groupby(groups).agg("min")
    elif function == "5th percentile":
        df = df.groupby(groups).agg(q05)
    elif function == "1st quartile":
        df = df.groupby(xgroups).agg(q25)
    elif function == "average":
        df = df.groupby(groups).agg("mean")
    elif function == "median":
        df = df.groupby(groups).agg(q50)
    elif function == "3rd quartile":
        df = df.groupby(groups).agg(q75)
    elif function == "95th percentile":
        df = df.groupby(groups).agg(q95)
    elif function == "maximum":
        df = df.groupby(groups).agg("max")
    return df.reset_index()


def q05(x):
    return x.quantile(0.05)

def q25(x):
    return x.quantile(0.25)

def q50(x):
    return x.quantile(0.5)

def q75(x):
    return x.quantile(0.75)

def q95(x):
    return x.quantile(0.95)
