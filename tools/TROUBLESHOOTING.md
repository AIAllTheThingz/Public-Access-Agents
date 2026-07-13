---
id: TOOL-TROUBLE-001
title: Toolchain Troubleshooting
version: 1.0.0
status: baseline
---

# Toolchain Troubleshooting

## Missing dependency

Install:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

## Wrong repository root

Use:

```bash
python tools/validate-all/run_all.py --root /path/to/repository
```

## JSON output will not parse

Run the tool directly with `--format json` and verify that wrappers are not mixing diagnostic text into stdout.

## Link anchor failure

Confirm the destination heading and GitHub-style slug. Duplicate headings receive numeric suffixes.

## Manifest selection failure

Use exact package directory slugs and a canonical or recognized profile name.

## Output already exists

Review the existing output. Use `--force` only when replacement is intended and reviewed.

## CI differs from local validation

Compare:

- Python version
- installed dependency version
- repository revision
- exact command
- root path
- generated or untracked files

## Internal error

Re-run with the same input, capture JSON output, and review the exception type. Do not convert exit code `3` to success.
