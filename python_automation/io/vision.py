"""Screen-scraping helpers."""

from __future__ import annotations

from typing import Any, Optional, Tuple
import importlib

pyautogui: Optional[Any]
try:
    pyautogui = importlib.import_module("pyautogui")
except ModuleNotFoundError:  # pragma: no cover - optional dependency
    pyautogui = None

Color = Tuple[int, int, int]


def get_pixel_color(point: Tuple[int, int]) -> Color | None:
    """Return the RGB color at the specified screen coordinate."""

    if pyautogui is None:
        return None
    return pyautogui.screenshot().getpixel(point)
