---
id: TF-SEC-001
status: baseline
title: Terraform and OpenTofu Security Standard
---

# Security Standard

- Never commit credentials, state, private keys, sensitive plans, or backend secrets.
- Use short-lived workload identity and least privilege where available.
- Encrypt state and transport, enable locking, and restrict state access.
- Review IAM, network exposure, public access, encryption, logging, and data retention changes explicitly.
- Treat provider and module code as supply-chain execution.
- Redact secrets from plans, logs, outputs, and CI artifacts.
