---
id: DISC-PRIV
title: Privacy and Data Governance Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - privacy
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# Privacy and Data Governance Agent Standard

## Purpose

Requires deliberate handling of personal, sensitive, and regulated data.

## Mandatory rules

### PRIV-INVENTORY-001

**Requirement:** Identify collected data, purpose, owner, classification, location, recipients, and retention.

**Evidence:** Data inventory.

### PRIV-MINIMIZE-002

**Requirement:** Collect and retain only data necessary for the stated purpose.

**Evidence:** Minimization review.

### PRIV-ACCESS-003

**Requirement:** Enforce least privilege and auditable access.

**Evidence:** Access-control evidence.

### PRIV-LOGS-004

**Requirement:** Exclude or redact sensitive data from logs, analytics, errors, and support artifacts.

**Evidence:** Log review.

### PRIV-LIFECYCLE-005

**Requirement:** Define deletion, correction, export, and retention behavior as applicable.

**Evidence:** Lifecycle test evidence.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.
