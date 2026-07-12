---
id: PLAT-AZURE
title: Microsoft Azure Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - azure
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Microsoft Azure Platform Agent Standard

## Requirements

### AZ-ID-001

**Requirement:** Prefer managed identities and workload federation over stored credentials.

### AZ-RBAC-002

**Requirement:** Use least-privilege role assignments at the narrowest practical scope.

### AZ-NET-003

**Requirement:** Restrict public exposure and document required network paths.

### AZ-LOG-004

**Requirement:** Enable appropriate diagnostic and security logging.

### AZ-POL-005

**Requirement:** Use policy and deployment controls to enforce required configuration.

### AZ-KEY-006

**Requirement:** Use approved key and secret management services.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes
