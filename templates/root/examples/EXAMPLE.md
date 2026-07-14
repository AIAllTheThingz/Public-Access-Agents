---
id: TEMPLATE-EX-ROOT-001
title: Root Agent Instructions Example
version: 0.3.0
status: baseline
---

# Root Agent Instructions Example

## Example purpose

This fictitious example shows a repository-wide `AGENTS.md` for a small internal reporting service.

## Project identity

- Project: `example-inventory-report`
- Purpose: Produce read-only inventory reports from approved data sources.
- Non-goals: Remediation, production changes, credential management, or user-facing application behavior.

## Selected standards

- Primary profile: `profiles/internal-automation/`
- Secondary profiles: `none`
- Language packages: `languages/python/`
- Discipline packages: `disciplines/application-security/`, `disciplines/testing/`, `disciplines/documentation/`, `disciplines/observability/`
- Framework packages: `none`
- Platform packages: `platforms/containers/`
- Virtualization packages: `none`
- Operating-system packages: `operating-systems/ubuntu/`
- Networking packages: `none`

## Project facts

- Supported runtimes: Python 3.13
- Deployment environments: developer workstation and non-production container job
- Sensitive data: internal asset metadata; no credentials in reports
- Privileged operations: none; the service is read-only
- Compatibility commitments: stable CSV columns within a major release
- Required reviewers: project owner and security reviewer for data-scope changes

## Validation

```bash
python -m pytest
python -m ruff check .
python tools/validate_project_manifest.py
```

## Evidence

`docs/evidence/`

## Boundary

This example is fictitious and does not authorize access to any system.
