# Python Automation Bot

Automation playground for intentionally "dumb" mouse/keyboard routines. The legacy flat scripts are being migrated into the installable package under `python_automation/`, where each behaviour lives as a **skill** with JSON-driven configuration.

## Quickstart

1. Create and activate a Python 3.10+ environment.
2. Install the package in editable mode along with its dependencies:

	```bash
	pip install -e .
	```

3. See the available skills:

	```bash
	python -m python_automation list
	```

4. Run a skill (replace `fishing` with any other registered name):

	```bash
	python -m python_automation run fishing --profile default
	```

	Add `--dry-run` to exercise the loop without real clicks/keypresses.

## Available Skills

| Skill | Description | Default Profile |
| --- | --- | --- |
| `dumb_clicker` | Replays the intentionally inefficient click/key rotation from the original `dunno.py`. | `python_automation/data/configs/dumb_clicker/default.json` |
| `fishing` | Casts and banks fish with randomized timing and optional hotkeys. | `python_automation/data/configs/fishing/default.json` |
| `mining` | Mines ore with bag handling, bonus clicks, and bank runs. | `python_automation/data/configs/mining/default.json` |
| `thieving` | Steals from NPCs with progressive bonus actions. | `python_automation/data/configs/thieving/default.json` |
| `fletching` | Automates banking, combining, and inventory clearing for fletching. | `python_automation/data/configs/fletching/default.json` |

Use `python -m python_automation run <skill> --profile default` to start any of them.

### Profiles & Overrides

- **Profiles:** Located under `python_automation/data/configs/<skill>/`. These JSON files match the config fields parsed in each skill’s `SkillConfig.from_mapping` method.
- **Custom Config:** Supply `--config-file /path/to/custom.json` to run with your own settings without editing the bundled defaults.
- **Dry Runs:** Append `--dry-run` to execute loops without moving the mouse or pressing keys—ideal for verifying timing tweaks.

## Project Layout

- `python_automation/botcore/` – Loop engine, randomness, stats, and action helpers.
- `python_automation/skills/` – Skill implementations registered via `@register_skill`.
- `python_automation/io/` – Placeholders and wrappers for GUI/config handling (in progress).
- `python_automation/data/` – Built-in profiles and assets consumed by skills.
- `docs/` – Architecture notes, progress tracker, and migration log.
- `tests/` – Pytest suite (currently focused on randomness utilities).

## Adding a New Skill

Skills live in `python_automation/skills/` and plug into the shared automation loop. Follow this checklist to add one:

1. **Create the skill module** at `python_automation/skills/<your_skill>.py` using the starter pattern below. Customize the config dataclass and iteration logic for your scenario.

	```python
	from __future__ import annotations

	import time
	from dataclasses import dataclass, field
	from typing import Any, Mapping, Sequence

	from ..botcore.context import LoopContext
	from . import register_skill
	from .base import BaseSkill, SkillConfig

	@dataclass
	class MySkillConfig(SkillConfig):
		 actions: Sequence[tuple[int, int]] = field(default_factory=list)

		 @staticmethod
		 def from_mapping(payload: Mapping[str, Any]) -> "MySkillConfig":
			  actions = payload.get("actions", [])
			  return MySkillConfig(actions=[tuple(item) for item in actions])

	@register_skill
	class MySkill(BaseSkill):
		 name = "my_skill"

		 def __init__(self, config: MySkillConfig | None = None) -> None:
			  super().__init__(config or MySkillConfig())

		 def prepare(self, context: LoopContext) -> None:
			  super().prepare(context)
			  overrides = context.metadata.get("config") if context.metadata else None
			  if isinstance(overrides, Mapping):
					self.config = MySkillConfig.from_mapping(overrides)
			  print(f"Loaded {len(self.config.actions)} actions for MySkill")

		 def perform_iteration(self, context: LoopContext) -> None:
			  super().perform_iteration(context)
			  start = time.time()
			  # TODO: perform your automation work here
			  duration = max(time.time() - start, 0.0)
			  context.stats.record_iteration(duration=duration, dry_run=context.dry_run)

		 def teardown(self, context: LoopContext) -> None:
			  super().teardown(context)
			  print("MySkill finished.")
	```

2. **Register the module** by adding its filename (without extension) to `_BUILTIN_MODULES` in `python_automation/skills/__init__.py`. This ensures the loader imports your skill at runtime.

3. **Add a configuration profile** under `python_automation/data/configs/<your_skill>/default.json`. Match the keys your `SkillConfig.from_mapping` reads. Example:

	```json
	{
	  "iterations": 0,
	  "actions": [
		 [1800, 900],
		 [1820, 920]
	  ]
	}
	```

4. **Document the new skill** (optional but recommended): update `docs/overview.md` and `docs/todo.md` so others know it exists and what remains.

5. **Sanity check the package** after your edits:

	```bash
	python -m compileall python_automation
	```

6. **Try it out** once configuration is ready:

	```bash
	python -m python_automation run my_skill --profile default
	```

	Use `--dry-run` to validate timing without sending real input.

## Development Tips

- Run the bytecode check after edits:

	```bash
	python -m compileall python_automation
	```

- Execute the test suite (requires `pytest`):

	```bash
	pytest
	```

- When extending randomness or IO helpers, mirror existing patterns to preserve the project’s intentionally messy human-like behaviour.

## Further Reading

- `docs/overview.md` – High-level philosophy, usage walkthrough, and migration notes.
- `docs/baseline.md` – Snapshot of the legacy scripts and migration status.
- `docs/todo.md` – Phase-by-phase roadmap for the ongoing refactor.

## Legacy Scripts

Older one-off scripts still live at the repo root and inside `specificUses/`. They remain runnable (`python3 some_script.py`) while migration continues, but new work should target the skill framework.
