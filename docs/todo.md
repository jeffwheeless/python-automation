# Project Restructure Todo

## Phase 0 · Baseline Audit
- [x] Inventory all runnable scripts and note their dependencies
- [x] Catalogue image/assets usage and map to existing tasks
- [x] List every external library currently imported anywhere in the repo
- [x] Extract current configuration mechanisms (INI files, hard-coded constants)
- [x] Identify any logs/config files that should be preserved or migrated
## Phase 1 · Core Scaffolding
- [x] Create installable package skeleton `python_automation/`
  - [x] `botcore/` for engine and shared primitives
  - [x] `skills/` for task-specific behaviors
  - [x] `io/` for screen + input adapters
  - [x] `cli/` for entry points
  - [x] `data/` for configs and assets
  - [x] `tests/` for unit/integration tests
- [x] Add top-level `pyproject.toml` with project metadata
- [x] Set up logging directory structure and rotation strategy
- [x] Establish shared constants/config paths in one place

## Phase 2 · Core Engine & Randomness
- [x] Port the main loop from `dunno.py` into `botcore/automation_loop.py`
- [x] Port click/key actions into `botcore/actions.py` (keep randomness hooks)
- [x] Centralize random delay logic in `botcore/randomness.py`
- [x] Move distraction/anti-detection logic into `botcore/detectors.py`
- [x] Write timing/stat tracking utilities in `botcore/stats.py`
- [x] Ensure existing randomness ranges are preserved and documented

## Phase 3 · Skills Migration
- [x] Define a base `Skill` protocol/class with lifecycle hooks
- [ ] Move each existing automation script (fishing, mining, etc.) into `skills/`
  - [x] Fishing
  - [x] Mining
  - [x] Thieving
  - [x] Fletching
  - [ ] Herblore / other utilities
- [ ] Replace global variables with injected config/state objects
- [x] Provide a shared registry for available skills
- [ ] Update scripts to use shared randomness and action helpers

## Phase 4 · IO & Configuration Layer
- [ ] Wrap `pyautogui` interactions in `io/gui.py`
- [ ] Create image/color helpers in `io/vision.py`
- [x] Migrate configuration handling into `io/config.py` (consider `pydantic`/`dataclasses`)
- [x] Introduce profile-based configs stored under `python_automation/data/configs`
- [ ] Add simulation/headless mode for safety testing

## Phase 5 · Command-Line Interface
- [ ] Build `python -m python_automation` entry point in `cli/main.py`
- [ ] Support commands:
  - `list` available skills
  - `run --skill SKILL --profile PROFILE`
  - `dry-run` preview timing without actions
- [ ] Add TUI/GUI hook placeholders for future expansion
- [ ] Wire logging and metrics output to CLI feedback

## Phase 6 · Testing & Quality Gates
- [ ] Configure `pytest` and basic fixtures (mocked `pyautogui`)
- [ ] Write unit tests for randomness boundaries
- [ ] Add integration tests for sample skills (using simulation mode)
- [ ] Set up `pre-commit` with `ruff` + `black`
- [ ] Add optional type-checking via `pyright` or `mypy`
- [ ] Create GitHub Actions workflow (lint + tests)

## Phase 7 · Documentation Expansion
- [ ] Extend `docs/overview.md` with architecture diagrams
- [ ] Add `docs/architecture.md` explaining each layer
- [ ] Document skill creation in `docs/skills.md`
- [ ] Provide Quickstart guide with install/run steps
- [ ] Maintain changelog and philosophy document

## Phase 8 · Migration & Cleanup
- [ ] Update existing scripts to import from new package structure
- [ ] Deprecate/retire old flat scripts after migration
- [ ] Ensure assets/config paths updated and tested
- [ ] Refresh `README.md` to reflect new workflow
- [ ] Archive legacy experiments in a `/legacy` folder if needed

## Phase 9 · Release & Distribution
- [ ] Finalize versioning strategy and CHANGELOG
- [ ] Package executable with `pyinstaller` (optional)
- [ ] Document deployment/usage for end users
- [ ] Tag initial release of the refactored project

## Phase 10 · Stretch Goals
- [ ] Build a terminal UI dashboard (e.g., `textual`)
- [ ] Add metrics dashboard or JSON export
- [ ] Explore plugin system for third-party skills
- [ ] Experiment with machine-learning-driven randomness tuning
