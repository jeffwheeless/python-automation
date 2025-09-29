"""Configuration loading and validation utilities."""

from __future__ import annotations

import configparser
import json
from pathlib import Path
from typing import Any, Dict, Iterable

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parent.parent / "data" / "configs"
SUPPORTED_EXTENSIONS = (".json", ".ini")


def load_ini(path: Path | None = None) -> configparser.ConfigParser:
    """Load an INI configuration file, defaulting to the shared config directory."""

    parser = configparser.ConfigParser()
    target_path = path or DEFAULT_CONFIG_PATH / "default.ini"
    if target_path.exists():
        parser.read(target_path)
    return parser


def list_available_configs(pattern: str = "*.ini") -> Dict[str, Path]:
    """Return available config files keyed by stem matching ``pattern``."""

    configs: Dict[str, Path] = {}
    if not DEFAULT_CONFIG_PATH.exists():
        return configs
    for config_file in DEFAULT_CONFIG_PATH.glob(pattern):
        configs[config_file.stem] = config_file
    return configs


def skill_config_dir(skill: str) -> Path:
    """Return the directory containing configs for the given skill."""

    return DEFAULT_CONFIG_PATH / skill


def list_skill_profiles(skill: str) -> Iterable[str]:
    """Yield available profile names for a skill."""

    directory = skill_config_dir(skill)
    if not directory.exists():
        return []
    return sorted(p.stem for p in directory.glob("*.json"))


def _load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def load_skill_config(
    skill: str,
    profile: str = "default",
    *,
    file_path: Path | None = None,
) -> Dict[str, Any]:
    """Load a configuration mapping for ``skill``.

    Configurations are stored under ``data/configs/<skill>/<profile>.json`` by
    default. Passing ``file_path`` allows overriding with an absolute path.
    """

    if file_path is not None:
        target = Path(file_path).expanduser().resolve()
    else:
        directory = skill_config_dir(skill)
        target = directory / f"{profile}.json"

    if not target.exists():
        return {}

    if target.suffix == ".json":
        return _load_json(target)
    if target.suffix == ".ini":
        parser = configparser.ConfigParser()
        parser.read(target)
        return {section: dict(parser[section]) for section in parser.sections()}

    raise ValueError(f"Unsupported config format: {target.suffix}")


def load_from_file(path: Path) -> Dict[str, Any]:
    """Load a configuration mapping from any supported file."""

    return load_skill_config(skill="", profile="", file_path=path)
