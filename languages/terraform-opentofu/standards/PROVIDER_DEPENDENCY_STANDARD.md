---
id: TF-PROV-001
status: baseline
title: Terraform and OpenTofu Provider and Dependency Standard
---

# Provider and Dependency Standard

- Declare required providers, sources, and version constraints.
- Commit and review lock-file changes.
- Use official or approved providers and verify provenance.
- Review provider upgrades for state migration, schema changes, new defaults, deprecations, privileges, and replacements.
- Avoid unmaintained providers or forks without documented risk acceptance.
- Test supported engine-provider combinations.
