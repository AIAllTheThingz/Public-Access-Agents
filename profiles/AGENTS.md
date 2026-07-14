---
id: PROFILE-AGENT-001
title: Project Profile Agent Instructions
version: 0.2.0
status: baseline
---
# Project Profile Agent Instructions

## Purpose

These instructions govern agents that create, modify, review, or document project profiles and profile packages.

Profiles affect package selection, risk assumptions, required decisions, evidence, and completion gates across adopting repositories. Treat profile changes as composition changes, not decorative documentation.

## Scope

These instructions apply to:

- canonical top-level profile files
- complete profile package directories
- profile selection and composition guidance
- profile manifests, standards, templates, and examples
- root catalog, manifest, roadmap, and example references

## Instruction precedence

1. Applicable legal, contractual, safety, security, and governance obligations
2. Explicit authorized user requirements
3. Root repository `AGENTS.md`
4. Governance policies
5. This profile collection `AGENTS.md`
6. The canonical profile and package being modified
7. Repository conventions
8. General agent preferences

Nested profile-package instructions may specialize this collection for their directory. They may not weaken governance or shared controls.

## Required reading

Before changing profiles:

- [README.md](README.md)
- [PROFILE_SELECTION_GUIDE.md](PROFILE_SELECTION_GUIDE.md)
- [PROFILE_COMPOSITION_MODEL.md](PROFILE_COMPOSITION_MODEL.md)
- [PROFILE_RISK_EVIDENCE_MATRIX.md](PROFILE_RISK_EVIDENCE_MATRIX.md)
- [PROFILE_LIFECYCLE.md](PROFILE_LIFECYCLE.md)
- [PROFILE_DECISION_MATRIX.md](PROFILE_DECISION_MATRIX.md)
- the affected canonical profile file
- the affected complete package README and manifest

## Non-negotiable rules

- Preserve canonical profile IDs and filenames unless a reviewed migration is approved.
- Keep canonical profile selections synchronized with package documentation.
- Do not invent project facts, risk, owners, environments, commands, or evidence.
- Distinguish required, conditional, and optional packages.
- Do not imply that profile selection replaces architecture or risk assessment.
- Do not weaken governance through profile wording.
- Keep examples fictitious and explicitly non-production.
- Do not treat typical risk as an approved classification.
- Update links, manifests, templates, examples, and root catalog documentation together.
- Record checks not run and limitations.

## Required working method

1. Identify the project shape and decisions controlled by the profile.
2. Inspect the canonical profile, package, and downstream examples.
3. Classify the change as editorial, additive, behavior-changing, breaking, or risk-changing.
4. Define acceptance criteria and migration impact.
5. Make the smallest coherent change.
6. Preserve stable IDs and links.
7. Update package selection, decisions, standards, templates, and examples together.
8. Run structural and link validation.
9. Review for hidden weakening, contradictory package selection, unsupported risk claims, and unresolved placeholders.
10. Record evidence and limitations.

## Profile quality requirements

A complete profile should define:

- purpose and applicability
- non-applicable shapes
- typical starting risk and escalation factors
- required governance
- required and conditional disciplines
- language, framework, platform, virtualization, operating-system, and networking selection considerations
- architecture and trust boundaries
- security and privacy decisions
- testing and validation
- operations and release
- nested instruction scopes
- completion evidence
- common failure modes
- adoption and review procedures
- non-production boundary

## Stable entry points

The top-level profile file is a stable compatibility entry point. The package directory provides the complete implementation.

Do not delete or repurpose the canonical file merely because the package directory is more detailed. Standards repositories should not require consumers to discover migration by broken link.

## Validation

Run:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
```

Also review manually for:

- inconsistent required packages
- contradictory risk language
- incorrect profile selection
- stale links
- unsupported architecture assumptions
- duplicated or diverging requirements
- hidden weakening
- false completion or production claims

## Completion gate

Profile work is incomplete until IDs, links, manifests, canonical files, package READMEs, standards, templates, examples, root catalog entries, and validation evidence agree.
