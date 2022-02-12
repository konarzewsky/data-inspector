from config.env_config import config

PLOT_NAMES = ["scatter", "line", "bar", "histogram", "box", "map", "corr"]

MAP_STYLES = [
    "basic",
    "streets",
    "outdoors",
    "light",
    "dark",
    "satellite",
    "satellite-streets",
]

LINE_AGG_FUNCTIONS = [
    "minimum",
    "5th percentile",
    "1st quartile",
    "average",
    "median",
    "3rd quartile",
    "95th percentile",
    "maximum",
]

BAR_AGG_FUNCTIONS = [
    "count",
    "sum",
]

HISTOGRAM_NORM = [
    "count",
    "percent",
    "probability",
    "density",
    "probability density",
]

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"

PDF_TITLE = 'DATA INSPECTOR get to know your data better'

REPORT_EMAIL = {
    "sender": config["EMAIL_ADDRESS"],
    "password": config["EMAIL_PASSWORD"],
    "body": """
        Hello,

        Please find attached your dataset report generated with Data Inspector app.
    """,
    "subject": "Data Inspector - dataset report"
}
