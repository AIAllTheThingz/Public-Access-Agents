---
id: EX-API-SELECT-001
title: Web API Composition Example Standards Selection
version: 0.1.0
status: baseline
---
# Web API Composition Example Standards Selection

## Purpose

This document explains why the example selects each standards package. It prevents `project-manifest.json` from becoming an unexplained shopping list.

## Selection principles

- Select packages based on architecture, users, data, trust boundaries, delivery, and operational obligations.
- Prefer explicit rationale over copying a familiar stack.
- Do not omit a discipline merely because it adds review work.
- Add stricter project-specific rules without weakening shared controls.
- Revisit the selection when architecture or risk changes.

## Selected packages

| Package | Rationale |
|---|---|
| Governance | Organization-wide behavior, risk, evidence, exceptions, security, and review apply to every example. |
| Profile: WEB_API | Defines the project-type overlay and common operational concerns. |
| Language: .NET | Defines implementation, dependency, testing, security, documentation, and completion expectations. |
| Discipline: Application Security | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Architecture and System Design | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Testing and Quality Engineering | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: API Engineering | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Privacy and Data Governance | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Observability | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: CI/CD | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Software Supply Chain | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Documentation | Selected because the fictitious architecture and change surface require this concern. |
| Discipline: Release Engineering | Selected because the fictitious architecture and change surface require this concern. |
| Platform: Containers | Selected because the example is packaged or operated on this platform. |
| Framework: ASP.NET Core | Adds framework-specific implementation and security expectations. |

## Meaningful omissions

- **Database Engineering:** The composition describes a persistence adapter but does not define a concrete schema or migration surface. Add the discipline when a real database is selected.
- **SRE:** Moderate risk and illustrative operations do not establish an on-call service objective. Add SRE when availability and recovery targets exist.
- **Accessibility:** The example exposes an API only and has no user interface.

An omission is valid only for the current fictitious scope. It is not a permanent exemption.

## Selection review questions

- Does the manifest match the actual architecture?
- Are all trust boundaries covered?
- Are data storage and movement concerns represented?
- Are user-facing accessibility obligations represented?
- Are build, dependency, artifact, deployment, and release concerns represented?
- Are availability, recovery, incident, or on-call expectations represented?
- Are documentation and accountable review represented?
- Would adding a real database, identity provider, cloud platform, external API, or regulated data change the selection?

## Change triggers

Reassess the composition when:

- a new component, language, framework, platform, data store, or external system is added
- public contracts or compatibility obligations change
- personal, sensitive, confidential, or regulated data enters scope
- production deployment, on-call, availability, or recovery expectations are introduced
- risk classification changes
- a temporary exception expires
