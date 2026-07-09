# Contributing Guide

Thanks for your interest in contributing to **PathofJewel-PoE-2**.

## Ground rules

- Keep pull requests focused and small when possible.
- Include tests for behavior changes.
- Update documentation when behavior or setup changes.

## Branch naming

Use descriptive prefixes:

- `feat/<short-name>`
- `fix/<short-name>`
- `docs/<short-name>`
- `chore/<short-name>`

## Local quality checks

Run before opening a PR:

```bash
ruff check .
black .
pytest -q
```

If type checking is enabled:

```bash
mypy src
```

## Pull request checklist

- [ ] Code builds/runs locally
- [ ] Linting passes
- [ ] Tests added/updated and passing
- [ ] Docs updated
- [ ] PR description includes what changed and why

## Commit message guidance

Use conventional prefixes:

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation
- `test:` tests
- `refactor:` internal restructuring
- `chore:` maintenance
