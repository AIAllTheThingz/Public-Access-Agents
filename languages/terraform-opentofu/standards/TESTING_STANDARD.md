---
id: TF-TEST-001
status: baseline
title: Terraform and OpenTofu Testing Standard
---

# Testing Standard

- Run formatting and validation on every change.
- Use lint, policy, security, and native or external tests proportionate to risk.
- Test module inputs, validation, outputs, conditionals, and supported versions.
- Generate plans in isolated non-production environments where practical.
- Verify create, update, replacement, destroy, and idempotency behavior for high-risk modules.
- Keep tests isolated and protect plan and state artifacts.
