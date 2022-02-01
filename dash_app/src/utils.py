import sys
import logging


def prepare_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    if not logger.handlers:
        lh = logging.StreamHandler(sys.stdout)
        lh.setFormatter(formatter)
        logger.addHandler(lh)
    return logger
    