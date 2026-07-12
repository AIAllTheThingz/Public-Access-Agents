#!/usr/bin/env python3
"""Build, validate, and commit the framework package set for the pull request branch."""

from __future__ import annotations

import base64
import hashlib
from pathlib import Path
import re
import shutil
import subprocess
import tarfile

PARTS = [
    ("bootstrap/frameworks/part01.b64", 4000, "2a188845d5c2078b9dab190658fed2f886a59712e3739ab207681e3e88375e85"),
    ("bootstrap/frameworks/part02.b64", 4000, "6694d3aa3ec1793164f71776d211f97f395d843c7bf3e43c086ed8ab226b81da"),
    ("bootstrap/frameworks/part03.b64", 4000, "05d57cec38d7db7f161a20185fe5cb441c54c3d29ec807604d9bb5a25fc17edd"),
    ("bootstrap/frameworks/part04.b64", 4000, "1d395b2066620cdb5a52d016329048bd93d56f5ee6a284618face2d24f397128"),
    ("bootstrap/frameworks/part05.b64", 4000, "db364467b5c7611a501deb32f41f8b2b305db106aff7081c752ef0da5c5dff73"),
    ("bootstrap/frameworks/part06.b64", 4000, "6acb7e073c86d854d1f9fc6b524107d2749ef0db45899a3a8deb739b7bf29940"),
    ("bootstrap/frameworks/part07.b64", 712, "b3a08cdc06c1213bfb66aa738927200716119ff6c89abbe3a3f929b0709080ac"),
]
ARCHIVE_SHA256 = "cd6ce2cad989ca9848a2399b4faadaba2b866e2481cb6855192f5035d06598a1"
FRAMEWORKS = ["aspnet-core", "react", "angular", "spring-boot", "fastapi"]

PRESERVED_RULES = {
    "frameworks/aspnet-core/AGENTS.md": [
        "ASPNET-CONFIG-001", "ASPNET-AUTH-002", "ASPNET-HTTP-003",
        "ASPNET-DI-004", "ASPNET-TEST-005",
    ],
    "frameworks/react/AGENTS.md": [
        "REACT-STATE-001", "REACT-A11Y-002", "REACT-SEC-003",
        "REACT-PERF-004", "REACT-TEST-005",
    ],
    "frameworks/angular/AGENTS.md": [
        "ANG-ARCH-001", "ANG-A11Y-002", "ANG-SEC-003",
        "ANG-RX-004", "ANG-TEST-005",
    ],
    "frameworks/spring-boot/AGENTS.md": [
        "SPRING-CONFIG-001", "SPRING-SEC-002", "SPRING-DATA-003",
        "SPRING-OBS-004", "SPRING-TEST-005",
    ],
    "frameworks/fastapi/AGENTS.md": [
        "FASTAPI-MODEL-001", "FASTAPI-AUTH-002", "FASTAPI-ASYNC-003",
        "FASTAPI-ERROR-004", "FASTAPI-TEST-005",
    ],
}


def run(*command: str) -> None:
    subprocess.run(command, check=True)


def verify_and_extract() -> None:
    encoded_parts: list[str] = []
    for path_text, expected_length, expected_sha256 in PARTS:
        path = Path(path_text)
        if not path.is_file():
            raise RuntimeError(f"Missing framework archive part: {path}")

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
            f"Framework archive checksum mismatch: expected {ARCHIVE_SHA256}, "
            f"received {actual_archive_sha256}."
        )

    archive_path = Path("bootstrap/frameworks/framework-packages.tar.xz")
    archive_path.write_bytes(archive_bytes)

    required_members = {
        "frameworks/README.md",
        "frameworks/AGENTS.md",
        "frameworks/MANIFEST.md",
        "frameworks/aspnet-core/AGENTS.md",
        "frameworks/react/README.md",
        "frameworks/angular/MANIFEST.md",
        "frameworks/spring-boot/standards/SECURITY_STANDARD.md",
        "frameworks/fastapi/templates/EVIDENCE_RECORD_TEMPLATE.md",
        "CATALOG.md",
        "MANIFEST.md",
        "ROADMAP.md",
    }

    with tarfile.open(archive_path, mode="r:xz") as archive:
        members = archive.getmembers()
        names = {member.name for member in members}
        if len(members) != 82:
            raise RuntimeError(
                f"Unexpected framework archive member count: expected 82, "
                f"received {len(members)}."
            )
        missing = sorted(required_members - names)
        if missing:
            raise RuntimeError("Missing required framework files: " + ", ".join(missing))
        for member in members:
            member_path = Path(member.name)
            if member_path.is_absolute() or ".." in member_path.parts:
                raise RuntimeError(f"Unsafe archive member path: {member.name}")
        archive.extractall(path=".", filter="data")


def correct_nested_links() -> None:
    for path in Path("frameworks").glob("*/templates/ADOPTION_CHECKLIST.md"):
        text = path.read_text(encoding="utf-8")
        path.write_text(
            text.replace("(../../languages/", "(../../../languages/"),
            encoding="utf-8",
        )

    for path in Path("frameworks").glob("*/examples/ADOPTION_EXAMPLE.md"):
        text = path.read_text(encoding="utf-8")
        text = text.replace("(../../languages/", "(../../../languages/")
        text = text.replace("(../../disciplines/", "(../../../disciplines/")
        text = text.replace("a Angular application", "an Angular application")
        text = text.replace("a ASP.NET Core application", "an ASP.NET Core application")
        path.write_text(text, encoding="utf-8")


def validate_frameworks() -> None:
    run("python", "tools/validate-standards/validate_repository.py")
    run("python", "tools/check-links/check_links.py")

    errors: list[str] = []
    framework_root = Path("frameworks")
    for name in FRAMEWORKS:
        package = framework_root / name
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
                errors.append(f"Missing required framework file: {path}")

        readme = package / "README.md"
        if readme.is_file() and len(readme.read_text(encoding="utf-8").splitlines()) < 180:
            errors.append(f"Framework README appears incomplete: {readme}")

        if len(list((package / "standards").glob("*.md"))) < 8:
            errors.append(f"Framework package has too few standards: {package}")

    for path_text, rule_ids in PRESERVED_RULES.items():
        text = Path(path_text).read_text(encoding="utf-8")
        for rule_id in rule_ids:
            if rule_id not in text:
                errors.append(f"Missing preserved rule {rule_id} in {path_text}")

    patterns = [
        re.compile(r"\{\{"),
        re.compile(r"\}\}"),
        re.compile(r"\{data"),
        re.compile(r"<TODO>", re.IGNORECASE),
    ]
    for path in framework_root.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for pattern in patterns:
            if pattern.search(text):
                errors.append(f"Unresolved placeholder in {path}: {pattern.pattern}")

    if errors:
        raise RuntimeError("Framework validation failed:\n- " + "\n- ".join(errors))


def cleanup_and_commit() -> None:
    shutil.rmtree("bootstrap/frameworks")
    bootstrap = Path("bootstrap")
    if bootstrap.exists() and not any(bootstrap.iterdir()):
        bootstrap.rmdir()

    run("git", "config", "user.name", "github-actions[bot]")
    run(
        "git",
        "config",
        "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )
    run("git", "add", "-A")

    status = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        check=False,
    )
    if status.returncode == 0:
        print("No framework changes were produced.")
        return
    if status.returncode != 1:
        raise RuntimeError("Unable to inspect staged framework changes.")

    run("git", "commit", "-m", "Complete framework standards packages")
    run("git", "push")


def main() -> None:
    verify_and_extract()
    correct_nested_links()
    validate_frameworks()
    cleanup_and_commit()


if __name__ == "__main__":
    main()
