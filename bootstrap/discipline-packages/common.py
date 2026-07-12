#!/usr/bin/env python3
"""Generate complete engineering-discipline standards packages."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = Path(__file__).resolve().parent
DISCIPLINES_ROOT = ROOT / "disciplines"


def load_catalog() -> dict[str, dict]:
    result: dict[str, dict] = {}
    for path in sorted(BOOTSTRAP.glob("catalog-*.json")):
        result.update(json.loads(path.read_text(encoding="utf-8")))
    if len(result) != 15:
        raise RuntimeError(f"Expected 15 disciplines, found {len(result)}")
    return result


def frontmatter(identifier: str, title: str, version: str = "0.1.0") -> str:
    return (
        "---\n"
        f"id: {identifier}\n"
        f"title: {title}\n"
        f"version: {version}\n"
        "status: baseline\n"
        "---\n"
    )


def sentence(value: str) -> str:
    return value[:1].upper() + value[1:] if value else value


def standard_identifier(prefix: str, filename: str) -> str:
    stem = filename.removesuffix(".md").replace("_", "-")
    return f"DISC-{prefix}-{stem}"


def render_standard(key: str, data: dict, filename: str, title: str, summary: str) -> str:
    return frontmatter(standard_identifier(data["prefix"], filename), title) + f"""# {title}

## Purpose

This standard defines detailed requirements for one part of the **{data["title"]}** discipline:

> {sentence(summary)}

## Required behavior

- {sentence(summary)}
- Define scope, ownership, inputs, outputs, assumptions, dependencies, and supported operating conditions.
- Use explicit, reviewable configuration and documented defaults rather than hidden environment assumptions.
- Apply controls proportionate to change risk, data sensitivity, trust boundaries, reversibility, and operational impact.
- Define positive behavior, negative behavior, boundary conditions, partial failure, recovery, and safe stopping conditions.
- Keep implementation, configuration, examples, and evidence free of credentials, internal production identifiers, and sensitive data.
- Preserve existing contracts unless an authorized change includes compatibility, migration, and communication work.
- Record exceptions through the repository exception process instead of weakening the standard silently.

## Required evidence

Evidence should be concrete and reproducible. Depending on scope, include:

- design, configuration, contract, diagram, or decision records
- implementation or review evidence tied to the requirement
- positive, negative, boundary, and failure-path tests
- operational, security, privacy, compatibility, or recovery evidence
- commands run, environments used, results, and checks not run
- known limitations, assumptions, unresolved risks, owners, and follow-up work

## Review questions

- Is this standard applicable to the change, and is the chosen scope documented?
- Are ownership and trust boundaries explicit?
- Are unsafe defaults, ambiguity, and hidden coupling avoided?
- Are failure, retry, rollback, recovery, and partial-success behaviors defined where relevant?
- Does the evidence prove the claim rather than merely describe intent?
- Are exceptions approved, time-bounded, and visible?

## Completion gate

Do not report this area complete until the applicable requirements are implemented, evidence is recorded, unsupported claims are removed, and remaining risk is stated plainly.
"""


def render_agents(key: str, data: dict) -> str:
    standards = [item[0] for item in data["standards"]]
    title = f'{data["title"]} Agent Standard'
    text = f"""---
id: {data["agent_id"]}
title: {title}
version: 0.2.0
status: baseline
applies_to:
  - {key}
depends_on:
  - GOV-WORK
  - GOV-RISK
  - GOV-EVIDENCE
---

# {title}

## Purpose

This file defines mandatory agent behavior for work governed by the **{data["title"]}** discipline.

Its objective is to {data["purpose"]}.

> Make the smallest safe, reviewable, testable, and evidence-backed change that satisfies the requirement.

## Scope

This discipline applies to:

"""
    text += "\n".join(f"- {item}" for item in data["scope"])
    text += """

## Instruction priority

When instructions conflict, apply them in this order:

1. explicit user requirements
2. the nearest more-specific `AGENTS.md`
3. this discipline `AGENTS.md`
4. the supporting standards in this package
5. repository conventions
6. general agent preferences

Do not resolve a material conflict silently. Follow the higher-priority instruction and report the conflict.

## Required supporting standards

Read every applicable supporting standard before implementation:

"""
    text += "\n".join(f"- [`standards/{name}`](standards/{name})" for name in standards)
    text += """

The supporting standards extend this file. This `AGENTS.md` takes precedence if wording conflicts.

## Mandatory rules

"""
    for rule_id, requirement, evidence in data["core_rules"]:
        text += f"""### {rule_id}

**Requirement:** {requirement}

**Evidence:** {evidence}

"""
    text += """## Non-negotiable behavior

- Inspect existing code, configuration, contracts, tests, documentation, ownership, and operational context before changing anything.
- Do not invent production values, identities, endpoints, schemas, credentials, infrastructure, legal obligations, or compatibility promises.
- Classify risk and identify trust boundaries, sensitive data, state changes, and reversibility.
- Default to safe, narrow, reversible behavior and stop when prerequisites or target identity are ambiguous.
- Do not weaken tests, security, privacy, accessibility, approvals, or evidence requirements to make work appear complete.
- Preserve public behavior unless change is explicitly authorized and migration or compatibility work is included.
- Keep examples fictitious and keep secrets and sensitive data out of source, tests, logs, errors, artifacts, and documentation.
- Record exact commands, results, limitations, assumptions, exceptions, and remaining risk.

## Required working method

1. Determine whether this discipline applies and document the reason.
2. Inspect the current implementation, contracts, evidence, and ownership.
3. Identify risk, trust boundaries, dependencies, failure modes, and affected users or operators.
4. Define acceptance criteria and required evidence before implementation.
5. Make the smallest coherent change.
6. Add or update tests, documentation, runbooks, contracts, diagrams, and evidence as applicable.
7. Run package-specific validation and review the final diff for unrelated or unsafe changes.
8. Report what changed, what was verified, what was not verified, and what risk remains.

## Completion gate

Do not report this discipline complete until:

- applicable mandatory rules are satisfied
- supporting standards were considered
- required evidence is recorded
- checks not run are identified
- limitations, assumptions, exceptions, and remaining risks are stated
"""
    if data.get("ref_urls"):
        text += "\n## References\n\n"
        text += "\n".join(f"- [{name}]({url})" for name, url in data["ref_urls"])
        text += "\n"
    return text


def render_readme(key: str, data: dict, catalog: dict[str, dict]) -> str:
    standards = data["standards"]
    tree_lines = [
        f"disciplines/{key}/",
        "├── AGENTS.md",
        "├── README.md",
        "├── MANIFEST.md",
        "├── standards/",
    ]
    for index, item in enumerate(standards):
        branch = "│   └──" if index == len(standards) - 1 else "│   ├──"
        tree_lines.append(f"{branch} {item[0]}")
    tree_lines.extend(
        [
            "├── templates/",
            "│   ├── ADOPTION_CHECKLIST.md",
            "│   ├── REVIEW_CHECKLIST.md",
            "│   └── EVIDENCE_RECORD_TEMPLATE.md",
            "└── examples/",
            "    └── ADOPTION_EXAMPLE.md",
        ]
    )
    text = frontmatter(f'DISC-PKG-{data["prefix"]}', f'{data["title"]} Discipline Package')
    text += f"""# {data["title"]} Discipline Package

## Purpose

This package provides project-agnostic, language-neutral standards for **{data["title"]}** work.

It exists to {data["purpose"]}. The package converts broad expectations into explicit agent instructions, review questions, required evidence, and completion gates.

This package is a **baseline**, not a claim of universal completeness. The adopting repository remains responsible for selecting applicable obligations, declaring its environment, assigning accountable owners, and adding stricter project or organizational requirements.

## What this package controls

"""
    text += "\n".join(f"- {item}" for item in data["scope"])
    text += """

## When to adopt this package

Adopt this discipline when one or more of the following are true:

"""
    text += "\n".join(f"- {item}" for item in data["apply"])
    text += """

Do not omit the package merely because its controls add work. Omit it only when the discipline is genuinely inapplicable and the tailoring decision is documented.

## What this package does not replace

This package does not replace:

- accountable human review
- organization policy, law, regulation, contractual obligations, or professional judgment
- project-specific architecture, risk, data classification, support, or deployment decisions
- language, framework, platform, and project-profile standards
- product, security, privacy, accessibility, legal, or operational specialists where their review is required

## Package structure

```text
"""
    text += "\n".join(tree_lines)
    text += """
```

## Normative entry point

Start with [`AGENTS.md`](AGENTS.md). It contains the mandatory agent rules, preserves the discipline's stable rule identifiers, defines instruction precedence, and points to the supporting standards.

[`MANIFEST.md`](MANIFEST.md) defines the package inventory and acceptance checks.

## Supporting standards

| Standard | Purpose |
|---|---|
"""
    for filename, title, summary in standards:
        text += f"| [`{title}`](standards/{filename}) | {sentence(summary)} |\n"
    text += """
## Adoption workflow

1. Read the repository root `AGENTS.md` and governance standards.
2. Confirm that this discipline applies to the project or change.
3. Copy or compose the complete package, not just the README.
4. Preserve the package `AGENTS.md` and stable rule identifiers.
5. Declare project-specific scope, owners, environments, constraints, and required evidence.
6. Select companion language, platform, framework, profile, and discipline packages.
7. Add stricter nested `AGENTS.md` files where directories require more specific controls.
8. Complete the adoption checklist and review checklist.
9. Run the repository validator and relative-link checker.
10. Obtain accountable review before promoting the tailored package for normal use.

## Project tailoring checklist

Before adoption, the project must answer:

- What work, components, data, environments, and users are in scope?
- Who owns implementation, review, approval, operations, exceptions, and follow-up?
- What risk classification applies?
- What trust boundaries, external dependencies, and sensitive data are involved?
- Which requirements are mandatory, conditionally applicable, or provably inapplicable?
- What tools, tests, review methods, environments, and evidence are required?
- What compatibility, migration, rollback, recovery, and support constraints exist?
- What laws, regulations, contracts, organization policies, or external standards apply?
- Where will evidence, decisions, exceptions, and residual risk be recorded?
- What would prevent the work from being reported complete?

## Required evidence

Typical completion evidence includes:

"""
    text += "\n".join(f"- {item}" for item in data["evidence"])
    text += """
- exact validation commands and results
- checks not run and the reason
- affected environments and representative test conditions
- accepted exceptions and expiration or review dates
- known limitations, unresolved risks, owners, and follow-up actions

Evidence must distinguish **planned**, **implemented**, **tested**, **reviewed**, and **operationally verified**. These are not interchangeable states, despite humanity's recurring attempts to treat them as synonyms.

## Validation

Validate the standards repository itself with:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

The adopting project must also define discipline-specific validation commands and review procedures. This package intentionally does not invent tool names, environments, credentials, endpoints, data sets, or production targets.

## Common failure modes

"""
    text += "\n".join(f"- {item}" for item in data["failures"])
    text += """

Other common mistakes include copying only selected controls without documenting omissions, declaring success without evidence, treating a scanner or checklist as proof by itself, and assuming the package removes the need for human accountability.

## Companion disciplines

This package commonly composes with:

"""
    text += "\n".join(
        f"- [`{catalog[item]['title']}`](../{item}/)" for item in data["companions"]
    )
    text += """

Companion disciplines supplement this package. They do not replace its applicable rules.

## Templates and example

- [`ADOPTION_CHECKLIST.md`](templates/ADOPTION_CHECKLIST.md) helps tailor the package to a repository.
- [`REVIEW_CHECKLIST.md`](templates/REVIEW_CHECKLIST.md) supports change and package review.
- [`EVIDENCE_RECORD_TEMPLATE.md`](templates/EVIDENCE_RECORD_TEMPLATE.md) provides a repeatable evidence structure.
- [`ADOPTION_EXAMPLE.md`](examples/ADOPTION_EXAMPLE.md) shows how to compose this discipline with governance and other standards.

Templates are starting points. Replace placeholders with reviewed project facts and never insert production secrets or sensitive identifiers.

## Maturity and maintenance

Status: **baseline**

A baseline package is usable for adoption and review but should be expected to evolve. Changes must:

- preserve stable identifiers unless a documented breaking change is approved
- update the README, manifest, templates, and examples when package behavior changes
- keep requirements specific, testable, risk-proportionate, and evidence-based
- avoid duplicating shared governance when a reference is sufficient
- run repository validation and link checking
- state compatibility, migration, and deprecation impact

## Completion statement

Adopting this package does not prove that {data["title"].lower()} work is complete. Completion requires implementation, verification, evidence, accountable review, and explicit disclosure of remaining limitations.
"""
    return text


