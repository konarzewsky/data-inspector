import plotly.express as px
import pandas as pd
from src.layout.graph_style import transparent_plot


def bar_plot(data, x, y, function, color, mode):
    df = aggregate_data(pd.DataFrame(data), x, y, color, function).sort_values(by=x)
    return px.bar(
        df,
        x=x,
        y=function,
        color=color,
        barmode=mode,
        text_auto=True,
        title=f"{function} bar plot of {x}",
    ).update_layout(transparent_plot)


def aggregate_data(df, x, y, color, function):
    groups = [color, x] if color else x
    if function == "count":
        df =  df.groupby(groups).agg(count = pd.NamedAgg(x, 'count'))
    elif function == "sum":
        df =  df.groupby(groups).agg(sum = pd.NamedAgg(y, 'sum'))
    return df.reset_index()
