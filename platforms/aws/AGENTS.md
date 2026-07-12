---
id: PLAT-AWS
title: Amazon Web Services Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - aws
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Amazon Web Services Platform Agent Standard

## Requirements

### AWS-ID-001

**Requirement:** Prefer roles and short-lived credentials over long-lived access keys.

### AWS-IAM-002

**Requirement:** Use least-privilege IAM and review resource policies.

### AWS-NET-003

**Requirement:** Minimize public exposure and define security-group and network controls.

### AWS-LOG-004

**Requirement:** Enable appropriate audit, configuration, and service logging.

### AWS-ENC-005

**Requirement:** Use approved encryption and key-management controls.

### AWS-ORG-006

**Requirement:** Apply organization-level guardrails where available.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes
