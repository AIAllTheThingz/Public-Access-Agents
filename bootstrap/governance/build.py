#!/usr/bin/env python3
"""Restore, validate, and commit the complete governance operating system."""

from __future__ import annotations

import base64
import hashlib
import json
import re
import shutil
import subprocess
import tarfile
from pathlib import Path

BOOTSTRAP = Path("bootstrap/governance")
ARCHIVE_SHA256 = "a103a656973dfa2c4361192e538ae0e433769a66fc57e76b88a250efcfb75394"
PARTS = [('part01.b64', 4000, 'e12b6e7ece4ceaf11aa6021806d892b4dc06f21586649cb36ddc1292c81789a4'), ('part02.b64', 4000, '188267664fdd4914b39f42ade9c83400045fb748b48d5d0aa240fce75f1074e1'), ('part03.b64', 4000, '7842e39a4b057bee03c17ccabcca84ea52ab9302eb950c119dcefecd2cca426f'), ('part04.b64', 4000, 'feabb1799f673a5f70cbbb87ce778cdbe22c16ef330b769123e5ecc15f8091b3'), ('part05.b64', 4000, '064f9a43070f7bfe8d9657b5032ed0c92e77619976c1076945b3e0c89d5e159d'), ('part06.b64', 4000, '30bd48e4b134fc188b5bff4f4173e01d1471ee78fbec088ef2e956a73bce85ef'), ('part07.b64', 4000, 'ba7bccf57061919d362c3f03737b49d810e22fcb0e02165a7b4cc19b5ad45139'), ('part08.b64', 4000, 'f40933190bf91b113f85b06278202a8f61b182084f3521b15f85efd187627bd3'), ('part09.b64', 2696, '8e39c328bc54c22e4da760f84da8dc06e51ffe55d3c857f09bcfb70a7a8a00ed')]
REQUIRED_MEMBERS = {
    "governance/AGENTS.md",
    "governance/README.md",
    "governance/MANIFEST.md",
    "governance/ORGANIZATION_CONTRACT.md",
    "governance/AGENT_WORKING_METHOD.md",
    "governance/RISK_CLASSIFICATION.md",
    "governance/COMPLETION_EVIDENCE.md",
    "governance/EXCEPTION_PROCESS.md",
    "governance/AI_GENERATED_CODE_POLICY.md",
    "governance/HUMAN_REVIEW_POLICY.md",
    "governance/PRODUCTION_READINESS.md",
    "governance/SECURE_DEVELOPMENT_POLICY.md",
    "governance/THREAT_MODELING_POLICY.md",
    "governance/VULNERABILITY_RESPONSE.md",
    "governance/POLICY_MAP.md",
    "governance/ADOPTION_GUIDE.md",
    "governance/OPERATING_MODEL.md",
    "governance/POLICY_LIFECYCLE.md",
    "governance/CONTROL_EVIDENCE_MODEL.md",
    "governance/GOVERNANCE_DECISION_MATRIX.md",
    "CATALOG.md",
    "MANIFEST.md",
    "ROADMAP.md",
}
POLICY_FILES = [
    "ORGANIZATION_CONTRACT.md",
    "AGENT_WORKING_METHOD.md",
    "RISK_CLASSIFICATION.md",
    "COMPLETION_EVIDENCE.md",
    "EXCEPTION_PROCESS.md",
    "AI_GENERATED_CODE_POLICY.md",
    "HUMAN_REVIEW_POLICY.md",
    "PRODUCTION_READINESS.md",
    "SECURE_DEVELOPMENT_POLICY.md",
    "THREAT_MODELING_POLICY.md",
    "VULNERABILITY_RESPONSE.md",
]
PRESERVED_RULES = {'GOV-CONTRACT': ['GOV-CONTRACT-001', 'GOV-CONTRACT-002', 'GOV-CONTRACT-003', 'GOV-CONTRACT-004', 'GOV-CONTRACT-005'], 'GOV-WORK': ['GOV-WORK-001', 'GOV-WORK-002', 'GOV-WORK-003', 'GOV-WORK-004', 'GOV-WORK-005', 'GOV-WORK-006'], 'GOV-RISK': ['GOV-RISK-001', 'GOV-RISK-002', 'GOV-RISK-003', 'GOV-RISK-004'], 'GOV-EVIDENCE': ['GOV-EVIDENCE-001', 'GOV-EVIDENCE-002', 'GOV-EVIDENCE-003', 'GOV-EVIDENCE-004', 'GOV-EVIDENCE-005'], 'GOV-EXCEPTION': ['GOV-EXCEPTION-001', 'GOV-EXCEPTION-002', 'GOV-EXCEPTION-003', 'GOV-EXCEPTION-004'], 'GOV-AI': ['GOV-AI-001', 'GOV-AI-002', 'GOV-AI-003', 'GOV-AI-004', 'GOV-AI-005'], 'GOV-REVIEW': ['GOV-REVIEW-001', 'GOV-REVIEW-002', 'GOV-REVIEW-003', 'GOV-REVIEW-004'], 'GOV-PROD': ['GOV-PROD-001', 'GOV-PROD-002', 'GOV-PROD-003', 'GOV-PROD-004'], 'GOV-SECDEV': ['GOV-SECDEV-001', 'GOV-SECDEV-002', 'GOV-SECDEV-003', 'GOV-SECDEV-004', 'GOV-SECDEV-005'], 'GOV-THREAT': ['GOV-THREAT-001', 'GOV-THREAT-002', 'GOV-THREAT-003', 'GOV-THREAT-004'], 'GOV-VULN': ['GOV-VULN-001', 'GOV-VULN-002', 'GOV-VULN-003', 'GOV-VULN-004']}


def run(*args: str) -> None:
    subprocess.run(args, check=True)


def restore_archive() -> None:
    encoded_parts: list[str] = []
    for filename, expected_length, expected_sha256 in PARTS:
        path = BOOTSTRAP / filename
        if not path.is_file():
            raise RuntimeError(f"Missing governance archive part: {path}")
        content = "".join(path.read_text(encoding="ascii").split())
        if len(content) != expected_length:
            raise RuntimeError(
                f"Invalid length for {path}: expected {expected_length}, "
                f"received {len(content)}."
            )
        actual_sha256 = hashlib.sha256(content.encode("ascii")).hexdigest()
        if actual_sha256 != expected_sha256:
            raise RuntimeError(
                f"Checksum mismatch for {path}: expected {expected_sha256}, "
                f"received {actual_sha256}."
            )
        encoded_parts.append(content)

    archive_bytes = base64.b64decode("".join(encoded_parts), validate=True)
    actual_archive_sha256 = hashlib.sha256(archive_bytes).hexdigest()
    if actual_archive_sha256 != ARCHIVE_SHA256:
        raise RuntimeError(
            "Governance archive checksum mismatch: "
            f"expected {ARCHIVE_SHA256}, received {actual_archive_sha256}."
        )

    archive_path = BOOTSTRAP / "restored-governance-package.tar.xz"
    archive_path.write_bytes(archive_bytes)

    with tarfile.open(archive_path, "r:xz") as archive:
        members = archive.getmembers()
        names = {member.name for member in members}
        if len(members) != 47:
            raise RuntimeError(
                f"Unexpected governance archive member count: expected 47, "
                f"received {len(members)}."
            )
        missing = sorted(REQUIRED_MEMBERS - names)
        if missing:
            raise RuntimeError(
                "Governance archive missing required files: " + ", ".join(missing)
            )
        for member in members:
            member_path = Path(member.name)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise RuntimeError(f"Unsafe archive member path: {member.name}")
        archive.extractall(path=".", filter="data")

    shutil.rmtree(BOOTSTRAP)
    bootstrap_root = Path("bootstrap")
    if bootstrap_root.exists() and not any(bootstrap_root.iterdir()):
        bootstrap_root.rmdir()


def validate_governance() -> None:
    run("python", "tools/validate-standards/validate_repository.py")
    run("python", "tools/check-links/check_links.py")

    root = Path("governance")
    errors: list[str] = []

    entry_points = [
        "AGENTS.md",
        "README.md",
        "MANIFEST.md",
        "POLICY_MAP.md",
        "ADOPTION_GUIDE.md",
        "OPERATING_MODEL.md",
        "POLICY_LIFECYCLE.md",
        "CONTROL_EVIDENCE_MODEL.md",
        "GOVERNANCE_DECISION_MATRIX.md",
    ]
    for filename in entry_points:
        if not (root / filename).is_file():
            errors.append(f"Missing governance entry point: {filename}")

    for filename in POLICY_FILES:
        path = root / filename
        if not path.is_file():
            errors.append(f"Missing governance policy: {filename}")
        elif len(path.read_text(encoding="utf-8").splitlines()) < 100:
            errors.append(f"Governance policy appears incomplete: {filename}")

    readme = root / "README.md"
    if readme.is_file() and len(readme.read_text(encoding="utf-8").splitlines()) < 200:
        errors.append("Governance README appears incomplete.")

    if len(list((root / "templates").glob("*.md"))) < 13:
        errors.append("Governance template set is incomplete.")
    if len(list((root / "examples").glob("*.md"))) < 8:
        errors.append("Governance example set is incomplete.")
    if len(list((root / "examples/evidence").glob("*.json"))) < 3:
        errors.append("Governance JSON evidence set is incomplete.")

    id_pattern = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
    by_id: dict[str, tuple[Path, str]] = {}
    for path in root.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = id_pattern.search(text)
        if match:
            by_id[match.group(1)] = (path, text)

    for document_id, rule_ids in PRESERVED_RULES.items():
        if document_id not in by_id:
            errors.append(f"Missing preserved governance document ID: {document_id}")
            continue
        path, text = by_id[document_id]
        for rule_id in rule_ids:
            if rule_id not in text:
                errors.append(f"Missing preserved rule {rule_id} in {path}")

    placeholder_patterns = [
        re.compile(r"\{\{"),
        re.compile(r"\}\}"),
        re.compile(r"\{data"),
        re.compile(r"<TODO>", re.IGNORECASE),
    ]
    for path in root.rglob("*"):
        if path.is_file() and path.suffix in {".md", ".json"}:
            text = path.read_text(encoding="utf-8")
            for pattern in placeholder_patterns:
                if pattern.search(text):
                    errors.append(
                        f"Unresolved placeholder in {path}: {pattern.pattern}"
                    )

    evidence_checks = [
        (
            root / "examples/evidence/risk-classification.example.json",
            {"level", "rationale", "factors"},
        ),
        (
            root / "examples/evidence/exception-record.example.json",
            {
                "id", "ruleId", "owner", "reason", "risk",
                "compensatingControls", "expiresOn", "status",
            },
        ),
        (
            root / "examples/evidence/completion-result.example.json",
            {"status", "summary", "filesChanged", "validation", "limitations"},
        ),
    ]
    for path, required_fields in evidence_checks:
        if not path.is_file():
            errors.append(f"Missing governance evidence example: {path}")
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        missing_fields = sorted(required_fields - payload.keys())
        for field in missing_fields:
            errors.append(f"{path} is missing required field {field}")

    if errors:
        print("Governance-specific validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print("Governance-specific validation passed.")


def commit_changes() -> None:
    run("git", "config", "user.name", "github-actions[bot]")
    run(
        "git",
        "config",
        "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )
    run("git", "add", "-A")
    diff = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        check=False,
    )
    if diff.returncode == 0:
        print("No governance changes were produced.")
        return
    run("git", "commit", "-m", "Complete governance operating system")
    run("git", "push")


def main() -> None:
    if not (BOOTSTRAP / "part01.b64").is_file():
        print("Governance system is already generated; nothing to do.")
        return
    restore_archive()
    validate_governance()
    commit_changes()


if __name__ == "__main__":
    main()
