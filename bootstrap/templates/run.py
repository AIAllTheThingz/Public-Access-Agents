#!/usr/bin/env python3
"""Restore and execute the verified template-library builder."""

from __future__ import annotations

import hashlib
import subprocess
from pathlib import Path

ROOT = Path.cwd()
PARTS = [
    (
        "bootstrap/templates/build.part01.py",
        3500,
        "b2515fa877ed1bb674b279a8f101d27f6db0fb8fa144d33bd51bcfc42c4c2ac6",
    ),
    (
        "bootstrap/templates/build.part02.py",
        3500,
        "5944a1fd3fb600f78c9e202ac9fa4dca51cddb7c53f79017e2bb3457fac53ab9",
    ),
    (
        "bootstrap/templates/build.part03.py",
        2209,
        "8150de5965f8d08cc30f862a274fb24e909caf328f2b0cfbcde40f5e2d2fcbcd",
    ),
]
SOURCE_SHA256 = "889c4bbe7be7d016dedb4da5102a9d0becbfd0788a09a00894b5a92ddfd3931d"

parts: list[str] = []
for path_text, expected_length, expected_sha in PARTS:
    path = ROOT / path_text
    if not path.is_file():
        raise RuntimeError(f"Missing template builder fragment: {path_text}")

    content = path.read_text(encoding="utf-8")
    if len(content) != expected_length:
        raise RuntimeError(
            f"Invalid length for {path_text}: expected {expected_length}, "
            f"received {len(content)}"
        )

    actual_sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(
            f"Checksum mismatch for {path_text}: expected {expected_sha}, "
            f"received {actual_sha}"
        )

    parts.append(content)

source = "".join(parts)
actual_source_sha = hashlib.sha256(source.encode("utf-8")).hexdigest()
if actual_source_sha != SOURCE_SHA256:
    raise RuntimeError(
        f"Template builder checksum mismatch: expected {SOURCE_SHA256}, "
        f"received {actual_source_sha}"
    )

target = ROOT / "bootstrap" / "templates" / "build.py"
target.write_text(source, encoding="utf-8")
subprocess.run(["python", str(target)], check=True)
