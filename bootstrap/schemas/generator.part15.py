- Root and nested `AGENTS.md` composition examples

## Next maturity work

- Add automated package-level adoption tests
- Add additional platform packages and platform-specific composition examples
- Add current provider-service compatibility matrices and migration guidance
- Add executable validation templates for containers, Kubernetes, infrastructure as code, and cloud platforms
- Add additional composition examples for data pipelines, internal automation, public libraries, security tools, and AI agent applications
- Add policy-dependency checks
- Add changelog and semantic versioning policy
- Select an open-source license
- Add maintainers and code ownership
- Publish versioned releases
- Add package maturity reviews that promote baseline packages to stable
"""
(root/'ROADMAP.md').write_text(roadmap_current, encoding='utf-8')

tools_readme = """---
id: TOOL-INDEX-001
title: Validation Tools
version: 0.2.0
status: baseline
---

# Validation Tools

## Purpose

The tools validate repository structure, links, schema contracts, examples, and machine-readable evidence.

## Commands

Install the pinned schema-validation dependency:

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
```

Run all validators:

```bash
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-schemas/validate_schemas.py
```

## Tool catalog

- [`validate-standards`](validate-standards/) checks repository structure, identifiers, JSON parsing, and required references.
- [`check-links`](check-links/) checks relative Markdown links.
- [`validate-schemas`](validate-schemas/) checks Draft 2020-12 schemas, versioned equivalence, positive and negative examples, formats, and repository instances.
- [`compose-agents`](compose-agents/) documents agent-instruction composition.
- [`generate-manifest`](generate-manifest/) documents manifest generation.

## Boundary

The tools detect structural and contract problems. They do not prove that a standard is secure, a record is truthful, an approver has authority, evidence is genuine, or a project is production-ready.
"""
(root/'tools'/'README.md').write_text(tools_readme, encoding='utf-8')

print("files", sum(1 for p in root.rglob('*') if p.is_file()))

sources = """# Public Reference Sources

These sources inform the repository. The repository summarizes and operationalizes selected ideas; it does not reproduce or replace the source documents.

## Secure development and application security

- NIST SP 800-218, Secure Software Development Framework (SSDF): https://csrc.nist.gov/pubs/sp/800/218/final
- CISA Secure by Design: https://www.cisa.gov/securebydesign
- OWASP Application Security Verification Standard: https://owasp.org/www-project-application-security-verification-standard/
- OWASP API Security Project: https://owasp.org/www-project-api-security/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/

## Software supply chain and delivery

- OpenSSF SLSA: https://slsa.dev/
- OpenSSF OSPS Baseline: https://baseline.openssf.org/
- GitHub Actions security hardening: https://docs.github.com/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions

## Accessibility

- W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- WAI-ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/

## Containers and Kubernetes

- Kubernetes Security Checklist: https://kubernetes.io/docs/concepts/security/security-checklist/
- Kubernetes Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/

## Observability

- OpenTelemetry documentation: https://opentelemetry.io/docs/

## JSON Schema and validation

- JSON Schema specification and current dialect information: https://json-schema.org/specification
- JSON Schema Draft 2020-12 meta-schema: https://json-schema.org/draft/2020-12/schema
