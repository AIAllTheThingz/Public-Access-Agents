#!/usr/bin/env python3
"""Build and validate the complete platform standards packages."""

from __future__ import annotations

import base64
import hashlib
import re
import shutil
import subprocess
import tarfile
from pathlib import Path

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "platforms"

PARTS = [('archive.part01.bin', 7276, '2601a22aa647c7dc0ad24db98e5dbd4161f78535632970609843a5f905ceeefb'), ('archive.part02.bin', 7276, '90be7658b9fe3ded48e94c82a394a68f339f0bab08deae6433d7df38de0095e5'), ('archive.part03.bin', 7276, '845b6ecf606c8744a58dea6c9b47335f25fcda5c26759afa820e4ece7276e873'), ('archive.part04.bin', 7276, '51793440dd7a22fd4633137a4314fdd4fae435598b26915c538d69c2f4995a8d')]
EXPECTED_ARCHIVE_SHA256 = "1329d084c9d8186075dd1b8aeb4c555a90666b432380918b72c923c6141de83d"
EXPECTED_MEMBER_COUNT = 106
PLATFORMS = ["containers", "kubernetes", "terraform", "azure", "aws", "gcp"]

PRESERVED_RULES = {'containers': ['CONT-BASE-001', 'CONT-USER-002', 'CONT-SECRET-003', 'CONT-HEALTH-004', 'CONT-SCAN-005', 'CONT-SIZE-006'], 'kubernetes': ['K8S-NS-001', 'K8S-POD-002', 'K8S-RBAC-003', 'K8S-NET-004', 'K8S-RES-005', 'K8S-SECRET-006'], 'terraform': ['IAC-STATE-001', 'IAC-PLAN-002', 'IAC-MODULE-003', 'IAC-SECRET-004', 'IAC-DRIFT-005', 'IAC-DESTROY-006'], 'azure': ['AZ-ID-001', 'AZ-RBAC-002', 'AZ-NET-003', 'AZ-LOG-004', 'AZ-POL-005', 'AZ-KEY-006'], 'aws': ['AWS-ID-001', 'AWS-IAM-002', 'AWS-NET-003', 'AWS-LOG-004', 'AWS-ENC-005', 'AWS-ORG-006'], 'gcp': ['GCP-ID-001', 'GCP-IAM-002', 'GCP-NET-003', 'GCP-LOG-004', 'GCP-KEY-005', 'GCP-POL-006']}

REQUIRED_MEMBERS = {
    "CATALOG.md",
    "MANIFEST.md",
    "ROADMAP.md",
    "platforms/README.md",
    "platforms/AGENTS.md",
    "platforms/MANIFEST.md",
    "platforms/PLATFORM_SELECTION_GUIDE.md",
    "platforms/SHARED_RESPONSIBILITY_MODEL.md",
    "platforms/PLATFORM_CHANGE_LIFECYCLE.md",
    "platforms/PLATFORM_DECISION_MATRIX.md",
    "platforms/containers/AGENTS.md",
    "platforms/kubernetes/README.md",
    "platforms/terraform/standards/STATE_BACKEND_STANDARD.md",
    "platforms/azure/templates/EVIDENCE_RECORD_TEMPLATE.md",
    "platforms/aws/examples/ADOPTION_EXAMPLE.md",
    "platforms/gcp/MANIFEST.md",
}

def run(command: list[str]) -> None:
    subprocess.run(command, check=True)

def reconstruct_archive() -> Path:
    archive_parts: list[bytes] = []
    for name, expected_length, expected_sha256 in PARTS:
        path = BOOTSTRAP / name
        if not path.is_file():
            raise RuntimeError(f"Missing platform archive part: {path}")
        content = path.read_bytes()
        if len(content) != expected_length:
            raise RuntimeError(
                f"Invalid length for {path}: expected {expected_length}, received {len(content)}."
            )
        actual = hashlib.sha256(content).hexdigest()
        if actual != expected_sha256:
            raise RuntimeError(
                f"Checksum mismatch for {path}: expected {expected_sha256}, received {actual}."
            )
        archive_parts.append(content)

    archive_bytes = b"".join(archive_parts)
    actual_archive_sha256 = hashlib.sha256(archive_bytes).hexdigest()
    if actual_archive_sha256 != EXPECTED_ARCHIVE_SHA256:
        raise RuntimeError(
            "Platform archive checksum mismatch: "
            f"expected {EXPECTED_ARCHIVE_SHA256}, received {actual_archive_sha256}."
        )

    archive_path = BOOTSTRAP / "platform-packages.tar.xz"
    archive_path.write_bytes(archive_bytes)
    return archive_path


def extract_archive(archive_path: Path) -> None:
    with tarfile.open(archive_path, mode="r:xz") as archive:
        members = archive.getmembers()
        names = {member.name for member in members}
        if len(members) != EXPECTED_MEMBER_COUNT:
            raise RuntimeError(
                f"Unexpected platform archive member count: expected {EXPECTED_MEMBER_COUNT}, "
                f"received {len(members)}."
            )
        missing = sorted(REQUIRED_MEMBERS - names)
        if missing:
            raise RuntimeError("Platform archive is missing required files: " + ", ".join(missing))
        for member in members:
            member_path = Path(member.name)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise RuntimeError(f"Unsafe archive member path: {member.name}")
            if member_path.parts[:2] == (".github", "workflows"):
                raise RuntimeError(f"Workflow file is not allowed in platform archive: {member.name}")
        archive.extractall(path=ROOT, filter="data")

def validate_platforms() -> None:
    errors: list[str] = []
    platform_root = ROOT / "platforms"
    required_root = [
        platform_root / "AGENTS.md",
        platform_root / "README.md",
        platform_root / "MANIFEST.md",
        platform_root / "PLATFORM_SELECTION_GUIDE.md",
        platform_root / "SHARED_RESPONSIBILITY_MODEL.md",
        platform_root / "PLATFORM_CHANGE_LIFECYCLE.md",
        platform_root / "PLATFORM_DECISION_MATRIX.md",
    ]
    for path in required_root:
        if not path.is_file():
            errors.append(f"Missing platform collection file: {path.relative_to(ROOT)}")

    if (platform_root / "README.md").is_file():
        lines = (platform_root / "README.md").read_text(encoding="utf-8").splitlines()
        if len(lines) < 250:
            errors.append("Platform collection README appears incomplete.")

    for name in PLATFORMS:
        package = platform_root / name
        required = [
            package / "AGENTS.md",
            package / "README.md",
            package / "MANIFEST.md",
            package / "templates" / "ADOPTION_CHECKLIST.md",
            package / "templates" / "REVIEW_CHECKLIST.md",
            package / "templates" / "EVIDENCE_RECORD_TEMPLATE.md",
            package / "examples" / "ADOPTION_EXAMPLE.md",
        ]
        for path in required:
            if not path.is_file():
                errors.append(f"Missing required platform file: {path.relative_to(ROOT)}")
        if (package / "README.md").is_file():
            lines = (package / "README.md").read_text(encoding="utf-8").splitlines()
            if len(lines) < 250:
                errors.append(f"Platform README appears incomplete: {package.relative_to(ROOT)}")
        standards = list((package / "standards").glob("*.md"))
        if len(standards) < 9:
            errors.append(f"Platform package has too few standards: {package.relative_to(ROOT)}")
        agent = package / "AGENTS.md"
        if agent.is_file():
            text = agent.read_text(encoding="utf-8")
            for rule_id in PRESERVED_RULES[name]:
                if rule_id not in text:
                    errors.append(f"Missing preserved rule {rule_id} in {agent.relative_to(ROOT)}")

    id_pattern = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
    ids: dict[str, Path] = {}
    placeholder_patterns = [
        re.compile(r"\{\{"),
        re.compile(r"\}\}"),
        re.compile(r"\{data"),
        re.compile(r"<TODO>", re.IGNORECASE),
    ]
    for path in platform_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        match = id_pattern.search(text)
        if match:
            document_id = match.group(1)
            if document_id in ids:
                errors.append(
                    f"Duplicate platform ID {document_id}: "
                    f"{ids[document_id].relative_to(ROOT)} and {path.relative_to(ROOT)}"
                )
            else:
                ids[document_id] = path
        for pattern in placeholder_patterns:
            if pattern.search(text):
                errors.append(f"Unresolved placeholder in {path.relative_to(ROOT)}: {pattern.pattern}")

    if len(ids) < 100:
        errors.append(f"Unexpectedly low platform ID count: {len(ids)}")

    if errors:
        print("Platform-specific validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(f"Platform-specific validation passed: {len(ids)} unique platform IDs.")

def cleanup_and_commit() -> None:
    shutil.rmtree(BOOTSTRAP)
    bootstrap = ROOT / "bootstrap"
    if bootstrap.exists() and not any(bootstrap.iterdir()):
        bootstrap.rmdir()

    run(["git", "config", "user.name", "github-actions[bot]"])
    run(["git", "config", "user.email", "41898282+github-actions[bot]@users.noreply.github.com"])
    run(["git", "add", "-A"])

    quiet = subprocess.run(["git", "diff", "--cached", "--quiet"], check=False)
    if quiet.returncode == 0:
        print("No platform changes were produced.")
        return
    run(["git", "commit", "-m", "Complete platform standards packages"])
    run(["git", "push"])

def main() -> None:
    if not (BOOTSTRAP / "archive.part01.bin").is_file():
        print("Platform packages are already generated; nothing to do.")
        return
    archive = reconstruct_archive()
    extract_archive(archive)
    run(["python", "tools/validate-standards/validate_repository.py"])
    run(["python", "tools/check-links/check_links.py"])
    validate_platforms()
    cleanup_and_commit()

if __name__ == "__main__":
    main()
