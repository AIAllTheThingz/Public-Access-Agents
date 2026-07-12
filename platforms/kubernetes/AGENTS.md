---
id: PLAT-K8S
title: Kubernetes Platform Agent Standard
version: 0.1.0
status: baseline
applies_to:
  - kubernetes
depends_on:
  - GOV-SECDEV
  - GOV-RISK
---
# Kubernetes Platform Agent Standard

## Requirements

### K8S-NS-001

**Requirement:** Use namespaces and workload identities to separate trust domains.

### K8S-POD-002

**Requirement:** Apply Pod Security Standards or stricter controls appropriate to risk.

### K8S-RBAC-003

**Requirement:** Use least-privilege RBAC and avoid broad wildcard permissions.

### K8S-NET-004

**Requirement:** Define network policies for material trust boundaries.

### K8S-RES-005

**Requirement:** Set resource requests, limits, probes, disruption, and rollout behavior.

### K8S-SECRET-006

**Requirement:** Use approved secret management and avoid plaintext manifests.

## Evidence

- Configuration diff
- Security and access review
- Deployment validation
- Rollback or recovery notes

## References

- https://kubernetes.io/docs/concepts/security/security-checklist/
- https://kubernetes.io/docs/concepts/security/pod-security-standards/
