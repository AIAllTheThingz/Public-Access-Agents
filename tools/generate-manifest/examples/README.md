---
id: TOOL-PKG-GENERATE-MANIFEST-001-EXAMPLE
title: Generate Manifest Tool Examples
version: 1.1.0
status: baseline
---

# Generate Manifest Tool Examples

## Commands

```bash
python tools/generate-manifest/generate_manifest.py --name example --profile INTERNAL_AUTOMATION --language python --virtualization kvm-libvirt --operating-system ubuntu --networking cisco-networking --include-profile-required --dry-run
```

```bash
python tools/generate-manifest/generate_manifest.py --config manifest-input.json --manifest-output project-manifest.json
```

## Expected behavior

Examples use fictitious or repository-local inputs. The infrastructure flags are repeatable and map to the three optional schema 1.1 package arrays. Review the command before execution and use dry-run for writing tools.

## Boundary

The examples demonstrate command shape and result handling. They do not authorize changes, select production targets, or provide genuine evidence.
