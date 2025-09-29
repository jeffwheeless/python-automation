# Baseline Audit

_Date: 2025-09-28_

This document captures the current state of the repository before the full restructure.

## Executable Scripts

### Root-Level Automation Scripts
- `all.py`
- `crafting.py`
- `fishing.py`
- `fletch.py`
- `herb.py`
- `interactionTemplate.py`
- `miningIron.py`
- `streamerClick.py`
- `thief.py`
- `thieveing.py`
- `dunno.py`
- `clickClick.py`
- `con.py`
- `regexpTest.py`
- `wip_interactColors.py`

### Utility/Support Scripts (root)
- `run_python.sh`
- `removeScreenShots.sh`
- `text.txt`, `test.txt`, `rename.txt`, `raname.txt`

### `modules/`
- `configHelper.py` (INI parsing)
- `inventory.py` (inventory interactions and logging)
- `mouseAutomation.py` (high-level mouse helpers)

### `utilities/`
- `circularMouseAreaClick.py`
- `clickTime.py`
- `continusMouseLogger.py`
- `distanceBetweenPoints.py`
- `getColorUnderMouse.py`
- `macroLogger.py`
- `mouseLogger.py`

### `specificUses/`
- `autoTyper.py`
- `channelChanger.py`
- `clickClick.py`
- `coder.py`
- `devSlackChecker.py`
- `discordBotBot.py`
- `dropInv.py`
- `hAlch.py`
- `mouseMove.py`
- `nmz.py`
- `numberCopyGenerator.py`
- `profitCalc.py`

## Assets
- `beerGlass.png`
- `bigBones.png`
- `bone2.png`
- `Claimnow.png`
- `floorBigBones.png`
- `fullInv.png`
- `smallBones.png`

These appear to be reference screenshots/templates for screen detection.

## Configuration & Logs
- `configs/configurations.ini`
- `logs/macroLogger.txt`

## External Library Usage
Detected imports beyond the standard library:
- `pyautogui`
- `numpy`
- `PIL` (indirect via `pyautogui`, not imported directly)
- `pytest` _not currently present but planned_

Standard-library modules used heavily:
- `random`, `time`, `datetime`, `math`
- `re`, `os`, `sys`, `pathlib`
- `configparser`, `json`, `logging`

## Observations
- Many scripts duplicate randomness/timing logic.
- Global state is pervasive (e.g., in `dunno.py`).
- Utilities and automation scripts share similar imports and patterns.
- No established package structure or dependency manifest.
- Scripts rely on direct `pyautogui` calls with minimal abstraction.

## Migration Progress Tracker
- ✅ `dumb_clicker` routine migrated into `python_automation/skills/dumb_clicker.py` with JSON-driven profiles.
- ✅ `fishing` automation ported to `python_automation/skills/fishing.py`, preserving randomness and inventory behaviours.
- ✅ `mining` workflow reimplemented in `python_automation/skills/mining.py` with configurable ore spots and banking route.
- ✅ `thieving` loop recreated in `python_automation/skills/thieving.py` with progressive bonus interactions.
- ✅ `fletching` routine migrated into `python_automation/skills/fletching.py` with banking, combine, and inventory variants driven by JSON profiles.
- 🔜 Remaining legacy skills to migrate next: herblore utilities and other bespoke scripts that still rely on the legacy interactive pattern.
