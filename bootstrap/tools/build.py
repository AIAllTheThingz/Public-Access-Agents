#!/usr/bin/env python3
"""Restore, validate, and install the complete repository toolchain."""

from __future__ import annotations

import base64
import hashlib
import io
import re
import shutil
import tarfile
from pathlib import Path

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "tools"
PARTS = [
    ("archive.part01.b64", 4000, "4a945952d33860a3df4d6e8d47105035150ac4ecaf4576335e99122ca28c202b"),
    ("archive.part02.b64", 4000, "41bc99cf72bf7f2ecaca20df17463040bc7395009d69dabef35266319f0622d3"),
    ("archive.part03.b64", 4000, "69bc53cf570a6dde34df21611682b24b143bbc1c5edb0b76f3c977ccb969586a"),
    ("archive.part04.b64", 4000, "fcecf388b27a06ac67fd1350a8c802abb59550d10b2e4c9cbccfae31d5b3388c"),
    ("archive.part05.b64", 4000, "b45ca614e681da67c8e57601a8cffcec94f210af0f2312d49a7f7d359b2a022e"),
    ("archive.part06.b64", 4000, "0b3a94c70644a55ae098b12ef61f6cee7dfcaa0c03dd643bbd4eed2ad1ffc424"),
    ("archive.part07.b64", 4000, "121acac3e16adc76cbd8913a79b1f0628b0d0adae84284fbe7a1a6244c8ff768"),
    ("archive.part08.b64", 4000, "e93192349fc510d5db413aee45157294355c518d36f95f6d6147b2ce1700463c"),
    ("archive.part09.b64", 2024, "ed7add39258e0af50d81ed206c1e44cb979ccdb2f127c2df7cfc654601149f1b"),
]
ARCHIVE_SHA256 = "4a808f4537f62342f9661a07419ae9a26f929482fd5bd8beab5412d41fe7ccd5"


def restore_archive() -> bytes:
    encoded_parts: list[str] = []
    for name, expected_length, expected_sha in PARTS:
        path = BOOTSTRAP / name
        if not path.is_file():
            raise RuntimeError(f"Missing toolchain archive fragment: {path.relative_to(ROOT)}")
        content = "".join(path.read_text(encoding="ascii").split())
        if len(content) != expected_length:
            raise RuntimeError(
                f"Invalid length for {path.relative_to(ROOT)}: expected {expected_length}, received {len(content)}"
            )
        actual_sha = hashlib.sha256(content.encode("ascii")).hexdigest()
        if actual_sha != expected_sha:
            raise RuntimeError(
                f"Checksum mismatch for {path.relative_to(ROOT)}: expected {expected_sha}, received {actual_sha}"
            )
        encoded_parts.append(content)

    archive = base64.b64decode("".join(encoded_parts), validate=True)
    actual_archive_sha = hashlib.sha256(archive).hexdigest()
    if actual_archive_sha != ARCHIVE_SHA256:
        raise RuntimeError(
            f"Toolchain archive checksum mismatch: expected {ARCHIVE_SHA256}, received {actual_archive_sha}"
        )
    return archive


def safe_extract(archive: bytes) -> None:
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:xz") as tar:
        members = tar.getmembers()
        if not members:
            raise RuntimeError("Toolchain archive is empty.")
        for member in members:
            path = Path(member.name)
            if path.is_absolute() or ".." in path.parts:
                raise RuntimeError(f"Unsafe archive member: {member.name}")
            if not path.parts or path.parts[0] != "tools":
                raise RuntimeError(f"Archive member is outside tools/: {member.name}")
            if member.issym() or member.islnk():
                raise RuntimeError(f"Archive links are not allowed: {member.name}")

        target = ROOT / "tools"
        if target.exists():
            shutil.rmtree(target)
        tar.extractall(ROOT, members=members, filter="data")


def update_catalog() -> None:
    path = ROOT / "CATALOG.md"
    text = path.read_text(encoding="utf-8")
    section = """## Repository toolchain

The executable toolchain validates repository structure, links, schemas, templates, and tool packages; generates project manifests; composes traceable standards bundles; and provides a unified validation runner.

- [Toolchain index](tools/README.md)
- [Tool catalog](tools/TOOL_CATALOG.md)
- [Command and result contract](tools/TOOL_CONTRACT.md)
- [Development guide](tools/DEVELOPMENT_GUIDE.md)
- [Testing guide](tools/TESTING_GUIDE.md)
- [Security boundaries](tools/SECURITY_BOUNDARIES.md)

Stable entry points are preserved for the existing validators. `compose-agents` and `generate-manifest` are now executable rather than planned placeholders. Permanent CI invokes the unified validation runner.
"""
    if "## Repository toolchain" not in text:
        marker = "## Composition examples"
        if marker not in text:
            raise RuntimeError("Cannot locate Composition examples section in CATALOG.md")
        text = text.replace(marker, section + "\n" + marker, 1)
    path.write_text(text, encoding="utf-8")


def update_manifest() -> None:
    path = ROOT / "MANIFEST.md"
    text = path.read_text(encoding="utf-8")
    section = """## Complete repository toolchain

- repository structure validation
- relative Markdown link and anchor validation
- Draft 2020-12 schema and instance validation
- reusable template package validation
- tool package and executable-entry validation
- deterministic project-manifest generation
- traceable agent-standards composition
- unified validation aggregation
- shared result library and JSON result contract
- central unit tests and fixtures
- tool selection, development, testing, security, troubleshooting, and compatibility guidance

The stable validator entry paths remain present. All executable tools support text and JSON results, common exit-code semantics, and offline operation. Writing tools support dry-run and refuse replacement without explicit `--force`.

"""
    if "## Complete repository toolchain" not in text:
        baseline = re.compile(r"## Baseline supporting standards\n\n- `tools`\n\n", re.MULTILINE)
        text, count = baseline.subn(section, text, count=1)
        if count == 0:
            marker = "## Validation"
            if marker not in text:
                raise RuntimeError("Cannot locate Validation section in MANIFEST.md")
            text = text.replace(marker, section + marker, 1)
    path.write_text(text, encoding="utf-8")


def update_roadmap() -> None:
    path = ROOT / "ROADMAP.md"
    text = path.read_text(encoding="utf-8")
    replacement = """- Complete repository toolchain:
  - repository structure, link, schema, template, and tool validation
  - deterministic project-manifest generation
  - traceable standards-bundle composition
  - shared JSON result and exit-code contract
  - unified validation runner
  - central unit-test suite
  - permanent CI integration
  - tool development, security, troubleshooting, and compatibility guidance"""
    if "- Complete repository toolchain:" not in text:
        if "- Repository validation tools" not in text:
            raise RuntimeError("Cannot locate repository tools roadmap entry")
        text = text.replace("- Repository validation tools", replacement, 1)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    archive = restore_archive()
    safe_extract(archive)
    update_catalog()
    update_manifest()
    update_roadmap()
    shutil.rmtree(BOOTSTRAP)
    bootstrap_root = ROOT / "bootstrap"
    if bootstrap_root.exists() and not any(bootstrap_root.iterdir()):
        bootstrap_root.rmdir()
    print("Toolchain restored, documentation updated, and bootstrap removed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
