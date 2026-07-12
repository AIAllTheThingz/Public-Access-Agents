---
id: TF-DEP-001
status: baseline
title: Terraform and OpenTofu Dependency Management Standard
---

# Dependency Management Standard

- Declare engine and provider version constraints.
- Commit the dependency lock file for the declared engine and supported platforms as required.
- Pin external modules to immutable versions or commits.
- Review provider and module upgrades for schema, state, behavior, permission, and replacement changes.
- Verify provenance and checksums; do not weaken integrity controls.
- Remove unused providers, modules, variables, and outputs.
