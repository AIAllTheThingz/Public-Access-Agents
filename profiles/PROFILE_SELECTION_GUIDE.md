---
id: PROFILE-SELECT-001
title: Project Profile Selection Guide
version: 0.2.0
status: baseline
---
# Project Profile Selection Guide

## Purpose

Select the primary project profile based on the system's operating shape, users, interfaces, deployment, data, and responsibilities.

## Selection table

| Profile | Typical starting risk | Strong signal | Canonical profile |
|---|---:|---|---|
| Web API | `moderate` | public and internal HTTP APIs | [`WEB_API.md`](WEB_API.md) |
| Web Application | `moderate` | single-page applications | [`WEB_APPLICATION.md`](WEB_APPLICATION.md) |
| Worker Service | `moderate` | message consumers | [`WORKER_SERVICE.md`](WORKER_SERVICE.md) |
| Command-Line Tool | `low` | administrative CLIs | [`CLI_TOOL.md`](CLI_TOOL.md) |
| Desktop Application | `moderate` | native desktop applications | [`DESKTOP_APPLICATION.md`](DESKTOP_APPLICATION.md) |
| Mobile Application | `moderate` | native mobile applications | [`MOBILE_APPLICATION.md`](MOBILE_APPLICATION.md) |
| Serverless Function | `moderate` | HTTP-triggered functions | [`SERVERLESS_FUNCTION.md`](SERVERLESS_FUNCTION.md) |
| Data Pipeline | `high` | batch ETL and ELT | [`DATA_PIPELINE.md`](DATA_PIPELINE.md) |
| Public Library | `moderate` | public packages | [`PUBLIC_LIBRARY.md`](PUBLIC_LIBRARY.md) |
| Internal Automation | `high` | administrative scripts | [`INTERNAL_AUTOMATION.md`](INTERNAL_AUTOMATION.md) |
| Multi-Tenant SaaS | `high` | shared-application multi-tenant SaaS | [`MULTI_TENANT_SAAS.md`](MULTI_TENANT_SAAS.md) |
| Security Tool | `high` | security scanners | [`SECURITY_TOOL.md`](SECURITY_TOOL.md) |
| AI Agent Application | `high` | tool-using AI agents | [`AI_AGENT_APPLICATION.md`](AI_AGENT_APPLICATION.md) |

## Selection rules

1. Choose one primary profile that best describes the main product or system.
2. Add secondary profiles only for distinct additional operating shapes.
3. Do not use a secondary profile merely because a component shares one technical characteristic.
4. Reassess profile selection when architecture or ownership changes.
5. Document why each selected profile applies.
6. Document why apparently relevant profiles do not apply.

## Common combinations

- Web application + Web API
- Web application + Worker service
- Multi-tenant SaaS + Web API + Worker service
- Data pipeline + Worker service
- Internal automation + CLI tool
- Security tool + CLI tool
- AI agent application + Web API
- Public library + CLI tool

## Ambiguous cases

### Script or CLI?

Choose CLI when the tool has a stable command interface for users or automation. Add Internal Automation when it modifies systems or orchestrates privileged operations.

### Worker or serverless?

Choose Worker Service when the project owns a long-running process lifecycle. Choose Serverless Function when a managed runtime controls invocation and scaling. Select both only when the repository contains both shapes.

### Web application or SaaS?

Choose Web Application for the user interface shape. Add Multi-Tenant SaaS when tenant isolation, lifecycle, quotas, billing, or cross-tenant risk are material.

### Data pipeline or internal automation?

Choose Data Pipeline when governed data movement, transformation, quality, lineage, replay, or publication is central. Add Internal Automation when privileged system orchestration is also present.

### AI agent application or ordinary application?

Choose AI Agent Application when model outputs influence tool use, actions, retrieved-content interpretation, generated decisions, or consequential workflows. A cosmetic text-generation feature may not require the full profile, but its risks still require review.

## Risk warning

Typical starting risk is not an approval. Use governance risk classification based on the actual change, target, data, privilege, blast radius, reversibility, exposure, safety, and evidence.

## Completion

Profile selection is complete only when the rationale, selected packages, omitted packages, risk classification, owners, and evidence expectations are recorded.
