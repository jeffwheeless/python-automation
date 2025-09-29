"""Shared constants used across the automation package."""

from __future__ import annotations

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
CONFIG_DIR = DATA_DIR / "configs"
ASSET_DIR = DATA_DIR / "assets"
LOG_DIR = BASE_DIR.parent / "logs"
