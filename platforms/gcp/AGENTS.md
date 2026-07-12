---
id: PLAT-GCP
title: Google Cloud Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - gcp
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Google Cloud Platform Agent Standard

## Requirements

### GCP-ID-001

**Requirement:** Prefer workload identity and short-lived credentials.

### GCP-IAM-002

**Requirement:** Use least-privilege IAM at the narrowest practical scope.

### GCP-NET-003

**Requirement:** Restrict public exposure and define service perimeters or network boundaries where applicable.

### GCP-LOG-004

**Requirement:** Enable appropriate audit and service logging.

### GCP-KEY-005

**Requirement:** Use approved secret and key-management services.

### GCP-POL-006

**Requirement:** Use organization policies and deployment controls where available.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes
