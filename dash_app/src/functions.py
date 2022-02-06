import pandas as pd
import base64
import io
import json

from src.utils import prepare_logger

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
    return True if df[lat].between(-90, 90).all() and df[lon].between(-180, 180).all() else False
