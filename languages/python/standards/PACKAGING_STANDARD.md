---
id: PY-S1-001
status: baseline
title: Python Packaging and Environment Standard
---

# Packaging and Environment Standard

## Requirements

- Use `pyproject.toml` as the primary project metadata file.
- Use isolated environments; never install project dependencies into an unmanaged global interpreter.
- Pin direct dependencies intentionally and lock transitive dependencies when reproducibility matters.
- Build distributions with standards-based tooling and test installation from the built artifact.
- Keep runtime, development, documentation, and test dependencies separated.

## Review evidence

Document relevant configuration, commands, tests, compatibility assumptions, and remaining risk.
