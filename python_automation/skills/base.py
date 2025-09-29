"""Base classes and utilities for skills."""

from __future__ import annotations

from dataclasses import dataclass

from ..botcore.context import LoopContext


@dataclass
class SkillConfig:
    iterations: int = 0


class BaseSkill:
    """A concrete base class implementing the Skill protocol."""

    name: str = "base"

    def __init__(self, config: SkillConfig | None = None) -> None:
        self.config = config or SkillConfig()
        self.context: LoopContext | None = None

    # The default implementations simply store the context so subclasses can
    # access shared state without re-implementing boilerplate.

    def prepare(self, context: LoopContext) -> None:  # pragma: no cover - override optionally
        """Hook executed before the skill starts."""

        self.context = context

    def perform_iteration(self, context: LoopContext) -> None:  # pragma: no cover - override optionally
        """Run a single iteration of the skill."""

        self.context = context

    def teardown(self, context: LoopContext) -> None:  # pragma: no cover - override optionally
        """Hook executed after the skill finishes."""

        self.context = context
