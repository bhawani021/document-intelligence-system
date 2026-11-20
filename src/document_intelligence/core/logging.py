"""Centralised application logging configuration"""

import logging
import sys

from src.document_intelligence.config.settings import Settings, get_settings

_HANDLER_MAKER = "_document_intelligence_handler"

def configure_logging(settings: Settings | None = None) -> None:
    """Configure application-wide logging

    The configuration is idempotent: calling this function
    multiple times will not add duplicate application console
    handlers
    """

    application_settings = settings or get_settings()

    log_level_name = application_settings.log_level.upper()
    log_level = getattr(logging, log_level_name, None)

    if not isinstance(log_level, int):
        raise ValueError(f"invalid logging level: {application_settings.log_level}")

    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)

    application_handler_exists = any(
        getattr(handler, _HANDLER_MAKER, False)
        for handler in root_logger.handlers
    )

    if not application_handler_exists:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(log_level)

        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        console_handler.setFormatter(formatter)
        setattr(console_handler, _HANDLER_MAKER, True)

        root_logger.addHandler(console_handler)

def get_logger(name: str) -> logging.Logger:
    """Return a named logger for an application module"""
    return logging.getLogger(name)



