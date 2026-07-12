---
id: TF-AGENT-001
status: baseline
title: Terraform and OpenTofu Agent Standard
---

# Terraform and OpenTofu Agent Standard

## Purpose

Mandatory rules for agents creating, modifying, reviewing, testing, securing, or documenting Terraform or OpenTofu configuration.

> Make the smallest safe, reviewable, reproducible, and well-documented infrastructure change that satisfies the requirement.

## Scope

- HCL configuration, modules, providers, backends, state, plans, policy checks, tests, and deployment documentation

## Runtime baseline

Select Terraform or OpenTofu as the declared engine for each execution path and pin supported versions. Do not assume both engines are interchangeable without validation.

## Required supporting standards

- `standards/TERRAFORM_OPENTOFU_CODING_STANDARD.md`
- `standards/ARCHITECTURE_STANDARD.md`
- `standards/DOCUMENTATION_STANDARD.md`
- `standards/TESTING_STANDARD.md`
- `standards/SECURITY_STANDARD.md`
- `standards/DEPENDENCY_MANAGEMENT_STANDARD.md`
- `standards/OBSERVABILITY_STANDARD.md`
- `standards/COMPLETION_EVIDENCE.md`
- `standards/STATE_BACKEND_STANDARD.md`
- `standards/MODULE_STANDARD.md`
- `standards/PLAN_APPLY_STANDARD.md`
- `standards/PROVIDER_DEPENDENCY_STANDARD.md`

## Non-negotiable rules

- Inspect engine, versions, backend, state ownership, providers, modules, workspaces, policies, and deployment process first.
- Never commit state, sensitive plan files, credentials, private keys, or backend secrets.
- Treat state and plan output as sensitive data.
- Pin providers and external modules using reviewable constraints and immutable sources.
- Validate inputs and avoid hidden environment-specific assumptions.
- Separate planning from applying and require accountable approval for production or destructive changes.
- Review replacements, destroys, unknown values, privilege changes, and data movement explicitly.
- Do not use targeted operations as a normal deployment method.
- Preserve resource addresses unless migration is explicitly planned.
- Verify resulting infrastructure, access, health, and drift after apply.

## Required working method

1. Declare engine, version, backend, environment, and execution identity.
2. Discover state ownership, dependencies, blast radius, and recovery options.
3. Implement the smallest coherent configuration change.
4. Format, initialize safely, validate, lint, test, and produce a reviewed plan.
5. Apply only with authorization and verify results.
6. Report exact plan evidence, approvals, outcomes, limitations, and remaining risk.

## Typical validation

- `terraform fmt -check -recursive` or `tofu fmt -check -recursive`
- `terraform validate` or `tofu validate`
- configured lint, policy, security, and test checks
- reviewed plan output with sensitive data protected
