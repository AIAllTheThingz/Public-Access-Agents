---
id: TF-OBS-001
status: baseline
title: Terraform and OpenTofu Observability Standard
---

# Observability Standard

- Record run identity, commit, engine version, environment, plan summary, approval, apply result, and verification without exposing secrets.
- Preserve audit trails for production changes.
- Monitor backend locking, failed runs, drift, policy violations, and deployment duration.
- Make created infrastructure emit required operational telemetry through its native configuration.
- Document expected failure signals and escalation paths.
