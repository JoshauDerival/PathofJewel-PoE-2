# PathofJewel-PoE-2

A Python project for Path of Exile 2–related tooling and workflows.

> This repository currently has a Python-only codebase. This documentation establishes a complete baseline and can be refined as features evolve.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Development](#development)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)

## Overview

**PathofJewel-PoE-2** is a Python repository intended to support Path of Exile 2 workflows, automation, or analysis use cases.

Because the project is actively evolving, this README focuses on practical setup and contributor guidance so you can:

1. Clone and run the project quickly.
2. Understand where code and assets belong.
3. Contribute safely with consistent standards.

## Features

Current baseline capabilities:

- Python-based project foundation.
- Clear local setup workflow.
- Standardized development and contribution guidance.
- Troubleshooting references for common environment issues.

As implementation matures, replace this section with concrete feature bullets mapped to actual modules.

## Project Structure

A typical structure for this repository should look like:

```text
PathofJewel-PoE-2/
├─ src/                  # Main application/package source code
├─ tests/                # Test suite
├─ docs/                 # Extended documentation
├─ scripts/              # Helper scripts (build/dev/maintenance)
├─ requirements.txt      # Runtime dependencies (optional)
├─ requirements-dev.txt  # Development dependencies (optional)
├─ pyproject.toml        # Preferred Python project metadata/config
└─ README.md             # Project documentation
```

If your current structure differs, keep this section aligned with the real tree over time.

## Requirements

- **Python**: 3.10+ recommended
- **Git**: latest stable release
- (Optional) **venv** or **conda** for environment isolation

## Installation

### 1) Clone the repository

```bash
git clone https://github.com/JoshauDerival/PathofJewel-PoE-2.git
cd PathofJewel-PoE-2
```

### 2) Create and activate a virtual environment

#### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3) Install dependencies

If a `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

If using `pyproject.toml` (setuptools/poetry/hatch/pdm), use the tool configured by the repo.

## Configuration

Create a local environment file if needed:

```bash
cp .env.example .env
```

Typical values:

- API keys/tokens
- Logging level
- Local paths
- Feature flags

Never commit secrets. Ensure `.env` is listed in `.gitignore`.

## Usage

Run the project using one of the following common patterns (depending on repository setup):

```bash
python -m src
```

or

```bash
python main.py
```

or

```bash
python scripts/run.py
```

If your repo exposes a CLI entrypoint, document it here with real commands and examples.

## Development

### Code style

Recommended tooling:

- **Black** for formatting
- **Ruff** for linting
- **isort** for import ordering

Example:

```bash
ruff check .
black .
```

### Type checking (optional but recommended)

```bash
mypy src
```

### Pre-commit hooks (recommended)

```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files
```

## Testing

Use `pytest` as the default test runner:

```bash
pytest -q
```

With coverage:

```bash
pytest --cov=src --cov-report=term-missing
```

Add at least one test for every bug fix and meaningful feature change.

## Troubleshooting

### Virtual environment activation fails

- Recreate the environment:
  - `rm -rf .venv` (macOS/Linux)
  - Remove `.venv` folder manually (Windows)
- Re-run setup commands.

### Dependency installation errors

- Upgrade build tools:

```bash
python -m pip install --upgrade pip setuptools wheel
```

- Reinstall dependencies afterward.

### Import errors when running scripts

- Confirm you are in repository root.
- Confirm virtual environment is active.
- Prefer module execution (`python -m ...`) over direct file execution where appropriate.

## Contributing

1. Fork the repository.
2. Create a feature branch:

```bash
git checkout -b feat/short-description
```

3. Make focused, well-scoped commits.
4. Run linting and tests locally.
5. Open a pull request with:
   - clear summary
   - test evidence
   - screenshots/logs when relevant

### Commit message style

Suggested conventional prefixes:

- `feat:` new functionality
- `fix:` bug fix
- `docs:` documentation updates
- `refactor:` code changes without behavior change
- `test:` test-related changes
- `chore:` maintenance

## Roadmap

Suggested near-term roadmap:

- Document concrete application architecture.
- Add reproducible local dev bootstrap (`Makefile`/task runner).
- Add CI pipeline for lint + tests.
- Expand usage examples with real PoE2 workflows.

## License

If not already present, add a `LICENSE` file and reference it here (e.g., MIT, Apache-2.0, GPL-3.0).
