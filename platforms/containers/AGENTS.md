---
id: PLAT-CONT
title: Container Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - containers
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Container Platform Agent Standard

## Requirements

### CONT-BASE-001

**Requirement:** Use minimal, supported base images from trusted sources and pin them to reviewed versions.

### CONT-USER-002

**Requirement:** Run as a non-root user unless a documented requirement justifies otherwise.

### CONT-SECRET-003

**Requirement:** Do not bake secrets into images or layers.

### CONT-HEALTH-004

**Requirement:** Define appropriate health checks and graceful termination.

### CONT-SCAN-005

**Requirement:** Scan images and dependencies and track remediation.

### CONT-SIZE-006

**Requirement:** Exclude build tools and unnecessary files from runtime images.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes
