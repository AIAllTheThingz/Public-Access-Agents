---
id: PY-EX-001
status: baseline
title: Python Adoption Example
---

# Python Adoption Example

A project should compose standards rather than duplicate them.

```text
project/
├── AGENTS.md
├── standards/
│   └── project-specific.md
├── src/
├── tests/
└── docs/
```

The project `AGENTS.md` should:

1. Reference this language package.
2. Declare exact runtime and toolchain support.
3. Add the applicable project profile, discipline, platform, and framework overlays.
4. Define project-specific commands and evidence.
5. Preserve the security, testing, documentation, dependency, observability, and completion-evidence requirements.

Example completion evidence:

```text
Changed: src/, tests/, docs/
Validation: python -m compileall .
Security impact: reviewed trust boundaries and secret handling
Compatibility: preserved declared runtime baseline
Limitations: list checks not run and why
```
