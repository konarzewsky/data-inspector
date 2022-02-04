import pandas as pd
import base64
import io
import json

from src.utils import prepare_logger

logger = prepare_logger()


def parse_contents(contents, filename):
    content_type, content_string = contents[0].split(",")
    decoded = base64.b64decode(content_string)
    try:
        file_type = filename[0].split(".")[-1]
        if "xls" in file_type:
            data = pd.read_excel(io.BytesIO(decoded))
        elif file_type == "csv":
            data = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        # TODO allow data type json
        # elif file_type == 'json':
        #     data = pd.read_json(json.dumps(io.BytesIO(decoded)))
        return data
    except Exception as e:
        logger.error(e)
        return None


def check_coordinates(data, lat, lon):
    df = pd.DataFrame(data)
    try:
        min_lat = df[lat].min()
        min_lon = df[lon].min()
        max_lat = df[lat].max()
        max_lon = df[lon].max()
        assert -90 <= min_lat <= max_lat <= 90
        assert -180 <= min_lat <= max_lat <= 180
        return True
    except AssertionError:
        return False
