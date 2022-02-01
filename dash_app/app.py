import numpy as np
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration
from src.env import ENVIRONMENT, SENTRY_DSN

import src.callbacks

from src.dash_app import dash_app, server
from src.layout import layout

dash_app.title = "My Dash App"
dash_app.layout = layout

if __name__ == "__main__":
    dash_app.run_server(host="0.0.0.0", debug=True)
    