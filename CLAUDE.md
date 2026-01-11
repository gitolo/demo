# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python 3.13 project using a virtual environment for isolation.

## Development Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run the application
python main.py

# Format code with Black
black .

# Lint code with Ruff
ruff check .

# Lint and auto-fix
ruff check --fix .

# Run tests
pytest

# Run tests with verbose output
pytest -v

# Run a single test
pytest test_main.py::test_greet -v
```

## Code Style

- Use type hints on all function parameters and return values
- Follow PEP 8 conventions
- Use f-strings for string formatting
