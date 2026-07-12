---
id: TF-ARCH-001
status: baseline
title: Terraform and OpenTofu Architecture Standard
---

# Architecture Standard

- Separate reusable modules from environment composition and deployment configuration.
- Keep state boundaries aligned to ownership, blast radius, lifecycle, and access control.
- Avoid monolithic states and excessive cross-state coupling.
- Make provider, account, subscription, project, region, and identity boundaries explicit.
- Document dependency direction, recovery, migration, and operational ownership.
