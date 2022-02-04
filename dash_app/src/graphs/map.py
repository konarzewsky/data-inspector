from config.env_config import config
import plotly.express as px
import pandas as pd


def map_plot(data, lat, lon, style, color, size, hover):
    df = pd.DataFrame(data)
    px.set_mapbox_access_token(config["MAPBOX_ACCESS_TOKEN"])
    figure = px.scatter_mapbox(
        df,
        lat=lat,
        lon=lon,
        mapbox_style=style,
        color=color,
        size=size,
        hover_data=hover,
    )
    return figure, ""
