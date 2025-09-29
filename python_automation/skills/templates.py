"""Templates and helpers for building new skills."""

from __future__ import annotations

from ..botcore.context import LoopContext
from . import register_skill
from .base import BaseSkill


@register_skill
class TemplateSkill(BaseSkill):
    """Example skill illustrating the expected lifecycle."""

    name = "template"

    def prepare(self, context: LoopContext) -> None:
        # TODO: Implement setup logic (e.g., focus the game window)
        super().prepare(context)

    def perform_iteration(self, context: LoopContext) -> None:
        # TODO: Implement a single iteration step
        super().perform_iteration(context)

    def teardown(self, context: LoopContext) -> None:
        # TODO: Implement cleanup logic
        super().teardown(context)
