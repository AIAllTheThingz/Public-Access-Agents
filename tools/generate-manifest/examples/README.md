---
id: TOOL-PKG-GENERATE-MANIFEST-001-EXAMPLE
title: Generate Manifest Tool Examples
version: 1.0.0
status: baseline
---

# Generate Manifest Tool Examples

## Commands

```bash
python tools/generate-manifest/generate_manifest.py --name example --profile WEB_API --language python --include-profile-required --dry-run
```

```bash
python tools/generate-manifest/generate_manifest.py --config manifest-input.json --manifest-output project-manifest.json
```

## Expected behavior

Examples use fictitious or repository-local inputs. Review the command before execution and use dry-run for writing tools.

## Boundary

The examples demonstrate command shape and result handling. They do not authorize changes, select production targets, or provide genuine evidence.
