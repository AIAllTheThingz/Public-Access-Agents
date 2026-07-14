---
name: platforms
description: Apply this repository's platform engineering standards to design, implementation, review, validation, deployment planning, troubleshooting, or migration work involving containers, Kubernetes, Terraform or OpenTofu, Microsoft Azure, Amazon Web Services, or Google Cloud Platform. Use when Codex must select and compose platform packages, create advanced secure infrastructure or deployment code, or reason about identity, networking, data, state, observability, resilience, recovery, capacity, and cost.
---

# Advanced Platform Engineering

Build platform definitions that are secure, reproducible, reviewable, observable, recoverable, and cost-aware. Platform code may change real identities, networks, data, state, availability, and spending; distinguish local source edits from execution against an environment.

## Establish authority and target identity

1. Read the adopting repository's root and nearest scoped `AGENTS.md` files.
2. Read [`PLATFORM_SELECTION_GUIDE.md`](PLATFORM_SELECTION_GUIDE.md), [`SHARED_RESPONSIBILITY_MODEL.md`](SHARED_RESPONSIBILITY_MODEL.md), [`PLATFORM_CHANGE_LIFECYCLE.md`](PLATFORM_CHANGE_LIFECYCLE.md), and [`PLATFORM_DECISION_MATRIX.md`](PLATFORM_DECISION_MATRIX.md) as applicable.
3. Inspect platform definitions, state configuration, deployment automation, policies, identities, networks, data, secrets, observability, recovery, tests, and CI.
4. Identify the authoritative account, subscription, project, cluster, registry, backend, region, environment, and acting identity before any external mutation.
5. Classify risk, blast radius, reversibility, public exposure, privilege, data sensitivity, availability, and cost impact.
6. Confirm explicit authorization and recovery readiness before privileged, destructive, public, or production-affecting execution.

Do not infer authorization from repository access, a passing plan, an available credential, or this skill.

## Select platform packages

Select every material platform boundary. Real systems commonly require multiple packages.

| Platform evidence | Package |
|---|---|
| Dockerfiles, Containerfiles, image builds, registries, image provenance, or container runtime behavior | [`containers/`](containers/) |
| Kubernetes manifests, Helm, Kustomize, operators, RBAC, policies, services, ingress, storage, or workloads | [`kubernetes/`](kubernetes/) |
| Terraform or OpenTofu modules, providers, backends, state, plans, imports, moves, applies, or destroys | [`terraform/`](terraform/) plus [`../languages/terraform-opentofu/`](../languages/terraform-opentofu/) |
| Azure tenants, subscriptions, resource groups, identities, policy, networking, data, or deployments | [`azure/`](azure/) |
| AWS Organizations, accounts, IAM, policies, networking, data, resources, or deployments | [`aws/`](aws/) |
| Google Cloud organizations, folders, projects, IAM, networking, data, resources, or deployments | [`gcp/`](gcp/) |

For each selected package:

1. Read its `README.md`, `AGENTS.md`, and `MANIFEST.md`.
2. Read the standards relevant to the target and requested behavior.
3. Apply the underlying language, framework, project-profile, and discipline packages.
4. Use adoption, review, and evidence templates when durable change records are needed.
5. Treat examples as fictitious composition guidance, never as environment configuration.

Verify provider-specific behavior against current official documentation when service behavior, defaults, limits, support, or security guidance may have changed. Record edition, region, version, feature, or compatibility constraints when material.

## Work through safe phases

1. **Discover:** identify current state, target, ownership, dependencies, drift, and constraints without mutation.
2. **Validate:** check syntax, schemas, policy, identity, target selection, credentials, prerequisites, and state access.
3. **Render or plan:** produce the exact image, manifest, diff, plan, change set, or preview for review.
4. **Assess:** evaluate destructive actions, privilege, exposure, data movement, downtime, cost, quotas, and recovery.
5. **Authorize:** obtain accountable approval for the exact reviewed scope and target when execution is consequential.
6. **Execute:** use bounded, observable, idempotent steps with stop conditions.
7. **Verify actual state:** test required and denied paths, health, policy, telemetry, data, recovery, and drift.
8. **Observe and close:** monitor outcomes, retain evidence, assign follow-up, and disclose residual risk.

Do not skip directly from source code to production execution. A dry run or successful plan is evidence of proposed behavior, not proof of actual state.

## Engineer the platform definition

Apply the selected package standards and, as relevant:

- pin and verify tool, provider, module, chart, base-image, and dependency sources
- use short-lived workload identity and least privilege; avoid embedded credentials and broad wildcard permissions
- make public exposure, ingress, egress, DNS, firewall, routing, and administrative paths explicit
- keep secrets, keys, certificates, state, plans, logs, and build artifacts out of source and unsafe output
- use immutable, reproducible, minimal artifacts with provenance, scanning, and promotion controls
- define health, readiness, startup, shutdown, resource, scaling, disruption, and failure behavior
- define encryption, retention, deletion, backup, restore, failover, rollback, and recreation responsibilities
- provide logs, metrics, traces, audit history, alerts, dashboards, retention, and accountable operational ownership
- handle imports, moves, replacement, drift, partial failure, retries, concurrency, and idempotency deliberately
- define budgets, tags or labels, quotas, capacity, lifecycle, data transfer, and anomaly handling
- separate reusable modules from environment-specific composition and keep outputs minimally sensitive
- encode policy and validation close to the change without treating automated policy as human approval

Prefer declarative, reviewable definitions over undocumented console changes. Do not hide destructive behavior behind convenience wrappers or unreviewed automation.

## Validate before execution

Run applicable offline and non-mutating checks first:

- formatting, syntax, schema, manifest, and configuration validation
- Dockerfile, image, Kubernetes, Helm, Kustomize, Terraform, OpenTofu, Bicep, CloudFormation, or provider-native linting
- policy-as-code and admission-policy tests
- static security, secret, dependency, image, and infrastructure scans
- unit, module, rendering, contract, and integration tests
- target, identity, backend, state, and credential verification
- plan or preview review with destructive and sensitive-output inspection
- cost, quota, compatibility, and migration analysis

After authorized execution, verify actual resources and both allowed and denied behavior. Do not report production readiness solely from local validation or a successful CLI exit code.

## Report completion evidence

Report:

- selected platform packages and authoritative target boundaries
- acting identity class and authorization status without exposing credentials
- source and actual-state changes
- plan, destructive, privilege, exposure, data, availability, recovery, and cost effects
- exact validation and verification commands with results
- rollback, roll-forward, restore, or recreation readiness
- checks not run and why
- limitations, residual risks, operational owners, and required reviewers

Distinguish planned, implemented, applied, verified, observed, and production-approved states.
