from config.env_config import config

import src.callbacks

from src.dash_app import dash_app, server
from src.layout import layout


dash_app.title = "DATA INSPECTOR"
dash_app.layout = layout

if __name__ == "__main__":
    dash_app.run_server(host="0.0.0.0", debug=True)
    