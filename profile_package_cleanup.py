#!/usr/bin/env python3
"""Finalize generated profile documentation and root catalog references."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path.cwd()
PROFILES = ROOT / "profiles"


def run(*args: str) -> None:
    subprocess.run(args, check=True)


DISPLAY_NAMES = {
    "[Api Engineering](": "[API Engineering](",
    "[Architecture](": "[Architecture and System Design](",
    "[Ci Cd](": "[CI/CD](",
    "[Database](": "[Database Engineering](",
    "[Integration](": "[Integration Engineering](",
    "[Privacy](": "[Privacy and Data Governance](",
    "[Sre](": "[Site Reliability Engineering](",
    "[Supply Chain](": "[Software Supply Chain](",
    "[Testing](": "[Testing and Quality Engineering](",
}

for readme in sorted(PROFILES.glob("*/README.md")):
    text = readme.read_text(encoding="utf-8")
    updated = text
    for old, new in DISPLAY_NAMES.items():
        updated = updated.replace(old, new)
    if updated != text:
        readme.write_text(updated, encoding="utf-8")

catalog = ROOT / "CATALOG.md"
catalog_text = catalog.read_text(encoding="utf-8")
profile_section = """## Project profiles

Project profiles are complete composition packages that select and organize governance, language, discipline, framework, platform, project-decision, evidence, and operational expectations for a project shape. Canonical uppercase files remain stable compatibility entry points; lowercase directories contain the complete packages.

- [Web API](profiles/WEB_API.md) ([complete package](profiles/web-api/))
- [Web application](profiles/WEB_APPLICATION.md) ([complete package](profiles/web-application/))
- [Worker service](profiles/WORKER_SERVICE.md) ([complete package](profiles/worker-service/))
- [Command-line tool](profiles/CLI_TOOL.md) ([complete package](profiles/cli-tool/))
- [Desktop application](profiles/DESKTOP_APPLICATION.md) ([complete package](profiles/desktop-application/))
- [Mobile application](profiles/MOBILE_APPLICATION.md) ([complete package](profiles/mobile-application/))
- [Serverless function](profiles/SERVERLESS_FUNCTION.md) ([complete package](profiles/serverless-function/))
- [Data pipeline](profiles/DATA_PIPELINE.md) ([complete package](profiles/data-pipeline/))
- [Public library](profiles/PUBLIC_LIBRARY.md) ([complete package](profiles/public-library/))
- [Internal automation](profiles/INTERNAL_AUTOMATION.md) ([complete package](profiles/internal-automation/))
- [Multi-tenant SaaS](profiles/MULTI_TENANT_SAAS.md) ([complete package](profiles/multi-tenant-saas/))
- [Security tool](profiles/SECURITY_TOOL.md) ([complete package](profiles/security-tool/))
- [AI agent application](profiles/AI_AGENT_APPLICATION.md) ([complete package](profiles/ai-agent-application/))

See the [profiles index](profiles/README.md) for selection, primary and secondary composition, risk scaling, adoption, evidence, lifecycle, and maintenance guidance."""
pattern = re.compile(r"## Project profiles\n.*?\n## Composition examples", re.DOTALL)
catalog_text, count = pattern.subn(profile_section + "\n\n## Composition examples", catalog_text)
if count != 1:
    raise RuntimeError(f"Expected one Project profiles section in CATALOG.md; replaced {count}.")
catalog.write_text(catalog_text, encoding="utf-8")

manifest = ROOT / "MANIFEST.md"
manifest_text = manifest.read_text(encoding="utf-8")
profile_manifest = """## Complete project profile packages

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

"""
if "## Complete project profile packages" not in manifest_text:
    marker = "## Complete composition examples"
    if marker not in manifest_text:
        raise RuntimeError("Could not locate composition examples section in MANIFEST.md.")
    manifest_text = manifest_text.replace(marker, profile_manifest + marker, 1)
manifest_text = re.sub(r"(?m)^- `?profiles`?\n", "", manifest_text)
manifest.write_text(manifest_text, encoding="utf-8")

roadmap = ROOT / "ROADMAP.md"
roadmap_text = roadmap.read_text(encoding="utf-8")
profile_roadmap = """- Complete project profile packages for:
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
- Profile selection, composition, risk-and-evidence, lifecycle, and decision-matrix guidance"""
if "- Project profiles" in roadmap_text:
    roadmap_text = roadmap_text.replace("- Project profiles", profile_roadmap, 1)
elif "- Complete project profile packages for:" not in roadmap_text:
    raise RuntimeError("Could not locate project profile roadmap entry.")
roadmap.write_text(roadmap_text, encoding="utf-8")

run("python", "tools/validate-standards/validate_repository.py")
run("python", "tools/check-links/check_links.py")

Path(__file__).unlink()
run("git", "config", "user.name", "github-actions[bot]")
run("git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com")
run("git", "add", "-A")
status = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
if status.returncode == 0:
    print("No profile finalization changes were produced.")
    raise SystemExit(0)
run("git", "commit", "-m", "Finalize project profile packages")
run("git", "push")
