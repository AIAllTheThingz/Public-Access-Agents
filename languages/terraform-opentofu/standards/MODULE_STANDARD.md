---
id: TF-MOD-001
status: baseline
title: Terraform and OpenTofu Module Standard
---

# Module Standard

- Give modules a narrow purpose, typed inputs, variable validation, explicit outputs, and documented behavior.
- Avoid hidden provider configuration and environment-specific assumptions.
- Do not embed credentials, account identifiers, or production naming.
- Pin external module sources immutably.
- Document examples, compatibility, upgrades, destructive behavior, and resource-address stability.
- Keep module interfaces smaller than implementation details.
