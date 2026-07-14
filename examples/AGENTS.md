---
id: EX-AGENT-001
title: Examples Maintenance Agent Standard
version: 0.1.0
status: baseline
---
# Examples Maintenance Agent Standard

## Purpose

This file governs maintenance of the example compositions under `examples/`.

The examples exist to demonstrate how governance, language, discipline, framework, platform, virtualization, operating-system, networking, profile, schema, evidence, and nested agent instructions can be composed into a project. They are deliberately fictitious and are not production-ready applications.

## Scope

These instructions apply to:

- example `README.md` files
- example root and nested `AGENTS.md` files
- project manifests
- composition rationale
- architecture, risk, testing, operations, and evidence documents
- schema-shaped JSON evidence
- links from examples to repository standards

## Mandatory rules

- Keep every example project-agnostic and free of real production values.
- Use fictitious names, identifiers, endpoints, users, organizations, and data.
- Do not include credentials, tokens, keys, internal host names, or sensitive identifiers.
- Do not represent an example as a deployable or complete application.
- Explain why each profile, language, discipline, framework, platform, virtualization, operating-system, and networking package was selected or omitted.
- Include explicit tailoring decisions, limitations, checks not run, and residual risk.
- Keep root and nested `AGENTS.md` files consistent with the selected packages.
- Validate every JSON document against its intended schema shape.
- Preserve stable front-matter identifiers.
- Update the example README and manifest whenever the file set or composition changes.
- Run repository validation and relative-link checking before completion.

## Required working method

1. Inspect the relevant governance, profile, language, discipline, framework, platform, virtualization, operating-system, networking, template, and schema files.
2. Identify the educational goal of the example.
3. Define the fictitious project facts and risk classification.
4. Select only relevant standards and explain the selection.
5. Create root and nested instructions that demonstrate scope and precedence.
6. Add architecture, risk, testing, operations, and completion evidence.
7. Validate links, identifiers, and JSON.
8. Review for accidental production values, unsupported claims, and unresolved placeholders.
9. Report exact checks and remaining limitations.

## Completion gate

An example change is incomplete until:

- every listed file exists
- relative links resolve
- JSON parses and matches the documented schema shape
- no unresolved placeholders remain
- fictitious values are obvious
- limitations and non-production status are explicit
- repository validation passes
