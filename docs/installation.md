# Installation Guide

This guide walks through setting up **PathofJewel-PoE-2** for local development and usage.

## Prerequisites

- Python 3.10 or newer
- Git
- Terminal (PowerShell on Windows, bash/zsh on macOS/Linux)

## 1. Clone repository

```bash
git clone https://github.com/JoshauDerival/PathofJewel-PoE-2.git
cd PathofJewel-PoE-2
```

## 2. Create virtual environment

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Upgrade pip toolchain

```bash
python -m pip install --upgrade pip setuptools wheel
```

## 4. Install dependencies

If `requirements.txt` is present:

```bash
pip install -r requirements.txt
```

If development requirements are present:

```bash
pip install -r requirements-dev.txt
```

## 5. Verify environment

```bash
python --version
pip --version
```

## 6. Run tests (if available)

```bash
pytest -q
```

## Common setup issues

### Command not found: python

Try `python3` (macOS/Linux) or `py` (Windows).

### PowerShell script execution policy blocks activation

Run PowerShell as admin and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Build failures on dependency install

Ensure pip/setuptools/wheel are up to date, then retry.
