import logging
import sys

from config import settings


def get_console_handler() -> logging.StreamHandler:
    console_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        "%(asctime)s — %(name)s — %(levelname)s — %(message)s"
    )
    console_handler.setFormatter(formatter)

    return console_handler


def get_logger(
    name: str = __name__, log_level: int = settings.logging_level
) -> logging.Logger:

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    logger.addHandler(get_console_handler())
    logger.propagate = False

    return logger
