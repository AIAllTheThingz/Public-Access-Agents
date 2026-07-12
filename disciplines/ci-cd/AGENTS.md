---
id: DISC-CICD
title: CI/CD Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - ci-cd
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---
# CI/CD Agent Standard

## Purpose

Secures and stabilizes automated build, test, and deployment workflows.

## Mandatory rules

### CICD-PIN-001

**Requirement:** Pin third-party actions and tools to reviewed versions or immutable references where practical.

**Evidence:** Workflow review.

### CICD-PERM-002

**Requirement:** Grant minimum token and environment permissions.

**Evidence:** Permission review.

### CICD-SECRETS-003

**Requirement:** Use protected secret stores and prevent secret exposure to untrusted code.

**Evidence:** Secret-path review.

### CICD-GATES-004

**Requirement:** Require proportionate tests, security checks, and approvals before promotion.

**Evidence:** Pipeline evidence.

### CICD-ARTIFACT-005

**Requirement:** Preserve provenance, integrity, retention, and traceability for release artifacts.

**Evidence:** Artifact metadata.

## Completion gate

Do not report the discipline work complete until applicable evidence is recorded and remaining limitations are stated.

## References

- https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions
