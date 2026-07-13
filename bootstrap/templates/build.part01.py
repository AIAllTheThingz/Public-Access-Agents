#!/usr/bin/env python3
"""Restore, extract, and finalize the complete template library."""

from __future__ import annotations

import base64
import hashlib
import io
import re
import shutil
import tarfile
from pathlib import Path, PurePosixPath

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "templates"
PARTS = [('bootstrap/templates/archive.part01.b64', 4000, '7b243e3b8db16eca75cbe52a773c79a75bdbb1938cf43a370f73fcbbdbe90194'), ('bootstrap/templates/archive.part02.b64', 4000, 'b7ce67cfef803fd9cbecb2341c67c8258563088a5912bd719044e2670b9f694b'), ('bootstrap/templates/archive.part03.b64', 4000, 'a02932307f3ddfbe4912e439da5cd7e428f104940e60e5d4dfa0ebe822d9b98a'), ('bootstrap/templates/archive.part04.b64', 4000, 'beb26f6ac1c205261252e42635f2270bf831d579ece925de5b1bd68cf347e0c3'), ('bootstrap/templates/archive.part05.b64', 4000, '19659c87bd6573bd8a26a172b34c60101a82262add27257961b1c75bc504f445'), ('bootstrap/templates/archive.part06.b64', 4000, '9b897832a65cf4fd4dfddf23e03308d75b5827139fdcac66220b38a41b43cdd2'), ('bootstrap/templates/archive.part07.b64', 4000, 'c4f074337a7223c0548021a92880458ff8849dd0a71af8cb5cc95fe3c3c10298'), ('bootstrap/templates/archive.part08.b64', 4000, 'd672895fdacfdc67981d5ec24fc65711666e432fe1a89285958bd36ba6e43381'), ('bootstrap/templates/archive.part09.b64', 4000, 'cc6389f07e4a832a39a782121b57f95d22bd121f738a3ad85e5cda8cd99875d6'), ('bootstrap/templates/archive.part10.b64', 4000, '045858fd451bcc2e998b58f41df94f71a15f9726fafeb1aa1b9ee36215fde68d'), ('bootstrap/templates/archive.part11.b64', 3888, '26d557b1f550a7bccf092b5a35b0d482d63da70d3cb3371bb69304a3942dc2e8')]
ARCHIVE_SHA256 = "56560d6cbb253559af897a37c16cfc3cecf8f7b89205539286c92a748ff2c832"

encoded_parts: list[str] = []
for path_text, expected_length, expected_sha in PARTS:
    path = ROOT / path_text
    if not path.is_file():
        raise RuntimeError(f"Missing template archive fragment: {path_text}")
    content = "".join(path.read_text(encoding="ascii").split())
    if len(content) != expected_length:
        raise RuntimeError(
            f"Invalid length for {path_text}: "
            f"expected {expected_length}, received {len(content)}"
        )
    actual_sha = hashlib.sha256(content.encode("ascii")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(
            f"Checksum mismatch for {path_text}: "
            f"expected {expected_sha}, received {actual_sha}"
        )
    encoded_parts.append(content)

archive = base64.b64decode("".join(encoded_parts), validate=True)
actual_archive_sha = hashlib.sha256(archive).hexdigest()
if actual_archive_sha != ARCHIVE_SHA256:
    raise RuntimeError(
        f"Template archive checksum mismatch: "
        f"expected {ARCHIVE_SHA256}, received {actual_archive_sha}"
    )

with tarfile.open(fileobj=io.BytesIO(archive), mode="r:xz") as tar:
    members = tar.getmembers()
    if len([m for m in members if m.isfile()]) != 80:
        raise RuntimeError(
            "Template archive file count mismatch: "
            f"expected 80, received {len([m for m in members if m.isfile()])}"
        )

    for member in members:
        path = PurePosixPath(member.name)
        if path.is_absolute() or ".." in path.parts:
            raise RuntimeError(f"Unsafe archive path: {member.name}")
        if not path.parts or path.parts[0] not in {"templates", "tools"}:
            raise RuntimeError(f"Unexpected archive path: {member.name}")
        if path.parts[0] == "tools" and path.parts[:2] != 