import plotly.express as px
import pandas as pd
from pandas.api.types import is_numeric_dtype
from src.layout.graph_style import transparent_plot


def corr_plot(data, method):
    df = pd.DataFrame(data)
    num_cols = [
        column
        for column in pd.DataFrame(data).columns
        if is_numeric_dtype(pd.DataFrame(data)[column])
    ]
    corr = df[num_cols].corr(method=method).round(2)
    return px.imshow(
        corr,
        text_auto=True,
        aspect="auto",
        title="Correlation matrix",
    ).update_layout(transparent_plot)
