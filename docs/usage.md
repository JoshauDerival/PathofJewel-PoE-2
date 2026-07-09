# Usage Guide

This document describes common ways to run and work with the project.

## Running the project

Depending on your code layout, one of the following may apply:

```bash
python -m src
```

```bash
python main.py
```

```bash
python scripts/run.py
```

Update this section with the exact command that matches your repository entrypoint.

## Example development workflow

1. Activate environment
2. Pull latest changes
3. Run formatter/linter
4. Run tests
5. Execute app/scripts

## Suggested commands

### Lint

```bash
ruff check .
```

### Format

```bash
black .
```

### Test

```bash
pytest -q
```

## Logging and debugging

- Use environment variables to set log level (e.g. `DEBUG`, `INFO`).
- Keep reproducible command examples for bug reports.

## Output handling

If your workflows generate artifacts (JSON/CSV/logs), document:

- output directory
- naming conventions
- cleanup policy
