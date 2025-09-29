# Python Automation Bot Project

## Overview
This project is a collection of Python scripts and modules designed to automate repetitive tasks in a deliberately inefficient and unpredictable way. The goal is to create a "dumb bot" that mimics human randomness and inefficiency, making it difficult for automated bot detectors to identify its behavior.

## Philosophy
- **Intentionally Inefficient:** The bot is not optimized for speed or resource usage. Instead, it introduces random delays, unnecessary steps, and unpredictable actions to appear more human-like.
- **Undetectable:** By avoiding patterns and optimizing logic, the bot aims to evade detection by anti-bot systems that look for regularity and efficiency.
- **Modular Design:** While the core logic remains intentionally "messy," supporting code is organized into modules for maintainability and reuse.

## Structure
- `python_automation/`
	- `botcore/`: Core loop, randomness, stats, and anti-detection helpers.
	- `skills/`: Skill definitions built on top of the shared loop.
	- `io/`: Wrappers around GUI automation and configuration IO.
	- `cli/`: Entry points for command-line control.
	- `data/`: Configuration files and assets.
- `dunno.py`: Legacy script showcasing the intentionally "dumb" logic (to be migrated).
- `modules/`, `utilities/`: Historical helpers slated for gradual migration into the new package.
- `docs/`: Project documentation.

## Usage
1. Install dependencies (see README.md).
2. List available skills:

```bash
python -m python_automation list
```

3. Run the intentionally inefficient skill (replace iterations as needed):

```bash
python -m python_automation run dumb_clicker --iterations 100
```

4. Skills can load profile-driven configs from `python_automation/data/configs`. For example, to run the migrated fishing routine with its default profile:

```bash
python -m python_automation run fishing --profile default
```

Use `--config-file /path/to/custom.json` to override built-in profiles.

5. The mining automation is now available as a skill as well:

```bash
python -m python_automation run mining --profile default
```

Tune parameters by editing `python_automation/data/configs/mining/default.json` or supplying a custom profile.

6. Thieving automation has joined the lineup:

```bash
python -m python_automation run thieving --profile default
```

Adjust bonus-click behaviour and timing with `python_automation/data/configs/thieving/default.json`.

7. Fletching automation is now available with configurable banking and inventory routes:

```bash
python -m python_automation run fletching --profile default
```

Tune banking, item combination, and inventory clearing paths via `python_automation/data/configs/fletching/default.json`.

7. Legacy scripts such as `dunno.py` remain available while migration continues.

## Contributing
Contributions are welcome, but please preserve the core philosophy of unpredictability and inefficiency in the main bot logic.
