---
id: TOOL-PKG-VALIDATE-SKILLS-001-EXAMPLE
title: Validate Skills Tool Examples
version: 1.0.0
status: baseline
---

# Validate Skills Tool Examples

## Commands

Validate repository skills:

```bash
python tools/validate-skills/validate_skills.py
```

Write a JSON result:

```bash
python tools/validate-skills/validate_skills.py \
  --format json \
  --output reports/skills.json
```

Require optional agent UI metadata:

```bash
python tools/validate-skills/validate_skills.py \
  --require-agent-metadata
```

## Expected behavior

The default command reads repository skill entry points and reports structural, routing, registration, local-link, and present metadata findings without modifying repository content.

## Boundary

These examples demonstrate command shape and result handling. They do not prove semantic trigger quality, authorize repository changes, execute routed packages, or establish production readiness.
