---
id: TF-PLAN-001
status: baseline
title: Terraform and OpenTofu Plan and Apply Standard
---

# Plan and Apply Standard

- Separate planning from applying and preserve reviewed plan evidence when risk warrants it.
- Require human approval for production and destructive changes.
- Review creates, updates, replacements, destroys, unknown values, sensitive values, permissions, and data movement.
- Do not apply a plan produced from different source, variables, credentials, or state.
- Use targeted operations only for recovery or documented exceptions.
- Verify infrastructure health, access, state, and drift after apply.
