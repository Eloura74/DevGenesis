from __future__ import annotations

"""Application-wide logging utilities for DevGenesis."""

import logging
from pathlib import Path
from typing import Optional

__all__ = ["get_logger", "LOG_FILE"]

LOG_FILE = Path.home() / ".devgenesis" / "devgenesis.log"


def _configure_logger(logger: logging.Logger, level: int = logging.INFO) -> None:
    """Configure the DevGenesis logger with a persistent file handler."""
    if logger.handlers:
        return

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        "%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)
    handler.setLevel(level)

    logger.setLevel(level)
    logger.addHandler(handler)


def get_logger(name: Optional[str] = None) -> logging.Logger:
    """Return a configured application logger.

    Parameters
    ----------
    name:
        Optional sub-logger name. If provided, a child logger is returned.
    """

    base_logger = logging.getLogger("devgenesis")
    _configure_logger(base_logger)
    return base_logger.getChild(name) if name else base_logger
