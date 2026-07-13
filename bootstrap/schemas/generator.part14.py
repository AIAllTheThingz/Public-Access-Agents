Each complete framework package includes scoped agent instructions, a useful README, a manifest, framework-specific standards, adoption and review templates, an evidence template, and an adoption example.

## Complete platform packages

- `platforms/containers`
- `platforms/kubernetes`
- `platforms/terraform`
- `platforms/azure`
- `platforms/aws`
- `platforms/gcp`

Each complete platform package includes scoped agent instructions, a useful README, a manifest, platform-specific standards, adoption and review templates, an evidence template, and an adoption example.

The platform collection also includes selection, shared-responsibility, change-lifecycle, and decision-matrix guidance.

## Complete project profile packages

- `profiles/web-api`
- `profiles/web-application`
- `profiles/worker-service`
- `profiles/cli-tool`
- `profiles/desktop-application`
- `profiles/mobile-application`
- `profiles/serverless-function`
- `profiles/data-pipeline`
- `profiles/public-library`
- `profiles/internal-automation`
- `profiles/multi-tenant-saas`
- `profiles/security-tool`
- `profiles/ai-agent-application`

Each complete profile package includes scoped agent instructions, a useful README, a manifest, six profile-specific standards, adoption and review templates, an evidence template, and an adoption example. The uppercase canonical profile files remain stable compatibility entry points.

## Complete schema system

- six rolling Draft 2020-12 schemas under `schemas/`
- six version-pinned schemas under `schemas/v1/`
- schema agent instructions and manifest
- schema catalog
- versioning, compatibility, extension, migration, validation, and design guidance
- positive and negative examples for every contract
- executable schema validation tooling under `tools/validate-schemas/`

The six stable rolling filenames remain present. Long-lived consumers should pin the versioned paths.

## Complete composition examples

- `examples/minimal`
- `examples/web-api`
- `examples/worker-service`
- `examples/full-stack`

Each complete example includes root and nested agent instructions, a project manifest, composition rationale, tailoring decisions, architecture, risk, testing, operations, completion evidence, and schema-shaped JSON evidence.

## Baseline supporting standards

- `templates`
- `tools`

## Validation

```bash
python -m pip install -r tools/validate-schemas/requirements.txt
python tools/validate-standards/validate_repository.py
python tools/check-links/check_links.py
python tools/validate-schemas/validate_schemas.py
```
"""
(root/'MANIFEST.md').write_text(manifest_current, encoding='utf-8')

roadmap_current = """# Roadmap

## Completed foundation

- Public repository and contribution model
- Root agent instructions
- Complete governance operating system
- Complete engineering discipline packages
- Complete language packages
- Complete framework packages
- Complete platform packages for:
  - Containers
  - Kubernetes
  - Terraform and OpenTofu
  - Microsoft Azure
  - Amazon Web Services
  - Google Cloud Platform
- Platform selection, shared-responsibility, change-lifecycle, and decision-matrix guidance
- Complete project profile packages for:
  - Web API
  - Web application
  - Worker service
  - Command-line tool
  - Desktop application
  - Mobile application
  - Serverless function
  - Data pipeline
  - Public library
  - Internal automation
  - Multi-tenant SaaS
  - Security tool
  - AI agent application
- Profile selection, composition, risk-and-evidence, lifecycle, and decision-matrix guidance
- Complete schema system:
  - six rolling Draft 2020-12 contracts
  - six version-pinned version 1 contracts
  - versioning and compatibility policy
  - extension and migration guidance
  - positive and negative contract examples
  - executable schema and repository-instance validation
- Templates
- Repository validation tools
- Complete standards-composition examples
- Schema-shaped completion, test, artifact, risk, and exception evidence
