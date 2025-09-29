"""Collection of automation skills."""

from __future__ import annotations

import importlib
from typing import Dict, Type

from ..botcore.automation_loop import Skill

_SKILL_REGISTRY: Dict[str, Type[Skill]] = {}
_BUILTIN_MODULES = (
    "templates",
    "dumb_clicker",
    "fishing",
    "mining",
    "thieving",
    "fletching",
)


def _load_builtin_skills() -> None:
    """Import modules that register built-in skills."""

    for module in _BUILTIN_MODULES:
        importlib.import_module(f"{__name__}.{module}")


def register_skill(skill_cls: Type[Skill]) -> Type[Skill]:
    """Decorator to register a skill class by its declared name."""

    _SKILL_REGISTRY[skill_cls.name] = skill_cls
    return skill_cls


def get_skill(name: str) -> Type[Skill]:
    """Retrieve a registered skill by name."""

    return _SKILL_REGISTRY[name]


def available_skills() -> Dict[str, Type[Skill]]:
    """Return a mapping of registered skills."""

    if not _SKILL_REGISTRY:
        _load_builtin_skills()
    return dict(_SKILL_REGISTRY)
