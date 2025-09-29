"""Logging helpers for the automation platform."""

from __future__ import annotations

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

DEFAULT_LOG_DIR = Path(__file__).resolve().parents[2] / "logs"
DEFAULT_LOG_FILE = DEFAULT_LOG_DIR / "automation.log"


def ensure_log_dir(log_dir: Path | None = None) -> Path:
    """Ensure the logging directory exists and return it."""

    target = log_dir or DEFAULT_LOG_DIR
    target.mkdir(parents=True, exist_ok=True)
    return target


def configure_logging(*, log_dir: Path | None = None) -> logging.Logger:
    """Configure the root logger with a rotating file handler."""

    ensure_log_dir(log_dir)
    log_path = (log_dir or DEFAULT_LOG_DIR) / DEFAULT_LOG_FILE.name
    handler = RotatingFileHandler(log_path, maxBytes=1_000_000, backupCount=5)
    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )
    handler.setFormatter(formatter)

    logger = logging.getLogger("python_automation")
    logger.setLevel(logging.INFO)
    if not any(isinstance(h, RotatingFileHandler) for h in logger.handlers):
        logger.addHandler(handler)
    return logger
