import pandas as pd
import df2img
import base64
import io
import json
import re
import os
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from fpdf import FPDF
from pathlib import Path

from src.utils import prepare_logger
from src.consts import EMAIL_REGEX, PDF_TITLE, REPORT_EMAIL

logger = prepare_logger()


def parse_contents(contents, filename):
    try:
        content_type, content_string = contents[0].split(",")
        decoded = base64.b64decode(content_string)
        file_type = filename[0].split(".")[-1]
        if "xls" in file_type:
            data = pd.read_excel(io.BytesIO(decoded))
        elif file_type == "csv":
            data = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        return data
    except Exception as e:
        logger.error(e)
        return None


def check_coordinates(data, lat, lon):
    df = pd.DataFrame(data)
    return (
        True
        if df[lat].between(-90, 90).all() and df[lon].between(-180, 180).all()
        else False
    )


def save_figure(figure, file_name, table=False):
    if not table:
        path = Path(__file__).resolve().parents[0] / "pdf" / "plots"
        if not os.path.exists(path):
            os.mkdir(path)
        figure.write_image(path / f"{file_name}.jpeg")
    else:
        path = Path(__file__).resolve().parents[0] / "pdf" / "tables"
        if not os.path.exists(path):
            os.mkdir(path)
        df = pd.DataFrame(figure)
        fig = df2img.plot_dataframe(
            df,
            print_index=False,
            tbl_header=dict(
                align="right",
                fill_color="gainsboro",
                font_color="black",
                font_size=9,
                line_color="darkslategray",
            ),
            tbl_cells=dict(
                align="right",
                font_size=8,
                line_color="darkslategray",
            ),
            row_fill_color=("#ffffff", "#d7d8d6"),
            fig_size=(550, 20*df.shape[0]),
        )
        df2img.save_dataframe(fig=fig, filename=path / f"{file_name}.jpeg")
    

def generate_pdf():
    pdf = FPDF(unit = "pt", format = "legal")

    path = Path(__file__).resolve().parents[0] / "pdf" / "tables"
    pdf.add_page()
    for table in os.listdir(path):
        pdf.image(str((path / table).resolve()), x = None, y = None, w = 0, h = 0, type = '', link = '')

    path = Path(__file__).resolve().parents[0] / "pdf" / "plots"
    pdf.add_page("L")
    for plot in os.listdir(path):
        pdf.image(str((path / plot).resolve()), x = None, y = None, w = 0, h = 0, type = '', link = '')

    path = Path(__file__).resolve().parents[0] / "pdf" 
    pdf.output(path / 'data-inspector-report.pdf', 'F')


def send_email(email, report):
    if re.match(EMAIL_REGEX, email):
        try:
            message = MIMEMultipart()
            message["From"] = REPORT_EMAIL["sender"]
            message["To"] = email
            message["Subject"] = REPORT_EMAIL["subject"]
            message.attach(MIMEText(REPORT_EMAIL["body"], 'plain'))

            pdf_file_name = "data-inspector-report.pdf"
            pdf_file_path = Path(__file__).resolve().parents[0] / "pdf" / pdf_file_name
            binary_pdf = open(pdf_file_path, 'rb')
            payload = MIMEBase('application', 'octate-stream', Name=pdf_file_name)
            payload.set_payload((binary_pdf).read())
            encoders.encode_base64(payload)
            payload.add_header('Content-Decomposition', 'attachment', filename=pdf_file_name)
            message.attach(payload)

            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(REPORT_EMAIL["sender"], REPORT_EMAIL["password"])
            text = message.as_string()

            logger.info(f"Sending email to {email}")
            session.sendmail(REPORT_EMAIL["sender"], email, text)
            session.quit()
            return False, ""
        
        except:
            return True, "An error occurred while sending an email"
    elif len(email)==0:
        return True, "Provide email address"
    else:
        return True, "Invalid email address"
