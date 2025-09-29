"""Wrappers around GUI automation libraries."""

from __future__ import annotations

from typing import Tuple

from ..botcore import actions

Point = Tuple[int, int]


def move_and_click(point: Point) -> None:
    """Move the cursor and click, preserving existing randomness hooks."""

    actions.move_cursor(point)
    actions.click(point)
