---
id: PY-PKG-001
status: baseline
title: Python Package
---

# Python Language Package

## Status

Baseline package suitable for project adoption and review.

## Contents

- `AGENTS.md`: mandatory agent behavior
- `standards/`: coding, architecture, documentation, testing, security, dependency, observability, evidence, and ecosystem-specific rules
- `templates/`: adoption templates
- `examples/`: composition guidance
- `MANIFEST.md`: package inventory and validation checklist

## Adoption

1. Copy this directory into the target repository or reference it through the organization's composition process.
2. Declare the exact supported runtime, toolchain, platforms, and compatibility constraints.
3. Remove standards that are provably inapplicable only through a documented tailoring decision.
4. Add stricter project-specific rules without weakening inherited controls.
5. Run the repository validator and link checker.
6. Review the resulting `AGENTS.md` with an accountable maintainer.

## Runtime policy

Use a currently supported CPython release declared by the repository. Pin the exact interpreter version in project tooling and do not rely on an unpinned system Python.

## Validation baseline

- `python -m compileall .`
- `python -m pytest`
- `python -m pip check`
