---
id: PLAT-IAC
title: Terraform and OpenTofu Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - terraform
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Terraform and OpenTofu Platform Agent Standard

## Requirements

### IAC-STATE-001

**Requirement:** Protect state as sensitive data with access control, encryption, locking, and recovery.

### IAC-PLAN-002

**Requirement:** Review plans before apply and separate planning from privileged execution.

### IAC-MODULE-003

**Requirement:** Pin providers and modules to reviewed versions.

### IAC-SECRET-004

**Requirement:** Do not place secrets in source, variable defaults, plans, or logs.

### IAC-DRIFT-005

**Requirement:** Detect and reconcile drift through an approved process.

### IAC-DESTROY-006

**Requirement:** Require explicit authorization for destructive changes.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes
