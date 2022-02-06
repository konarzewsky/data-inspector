import plotly.express as px
import pandas as pd
from src.layout.graph_style import transparent_plot


def map_plot(data, lat, lon, style, color, size, hover, token):
    df = pd.DataFrame(data)
    px.set_mapbox_access_token(token)
    if not style:
        style = "streets"
    return px.scatter_mapbox(
        df,
        lat=lat,
        lon=lon,
        mapbox_style=style,
        color=color,
        size=size,
        hover_data=hover,
        title="Interactive map",
    ).update_layout(transparent_plot)
