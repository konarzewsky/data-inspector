import pandas as pd

from dash import no_update, callback_context, dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from pathlib import Path

from src.utils import prepare_logger
from src.functions import (
    generate_pdf,
    send_email,
)

logger = prepare_logger()


def init_callbacks_tab_report(app):
    @app.callback(
        Output("email-error", "displayed"),
        Output("email-error", "message"),
        Output("download-pdf", "data"),
        Input("download-pdf-button", "n_clicks"),
        Input("send-email-button", "n_clicks"),
        State("email-input", "value"),
    )
    def generate_report(n_clicks_download, n_clicks_send, email):
        if n_clicks_download is None and n_clicks_send is None:
            raise PreventUpdate
        logger.info("Generating report - in progress...")
        report = generate_pdf()
        logger.info("Generating report - done")
        if "download-pdf-button" in str(callback_context.triggered):
            pdf_path = Path(__file__).resolve().parents[1] / "pdf" / "data-inspector-report.pdf"
            logger.info("Downloading pdf report")
            return False, "", dcc.send_file(pdf_path)
        else:
            show, message = send_email(email, report)
            return show, message, None
