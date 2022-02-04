from config.env_config import config

from src.callbacks.tab_upload import init_callbacks_tab_upload
from src.callbacks.tab_view import init_callbacks_tab_view
from src.callbacks.tab_inspect import init_callbacks_tab_inspect
from src.callbacks.tab_graphs import init_callbacks_tab_graphs
from src.callbacks.theme import init_callbacks_theme

from src.dash_app import dash_app, server
from src.layout.layout import get_layout


dash_app.title = "DATA INSPECTOR"
dash_app.layout = get_layout()

init_callbacks_tab_upload(dash_app)
init_callbacks_tab_view(dash_app)
init_callbacks_tab_inspect(dash_app)
init_callbacks_tab_graphs(dash_app)
init_callbacks_theme(dash_app)

if __name__ == "__main__":
    dash_app.run_server(host="0.0.0.0", debug=True)
