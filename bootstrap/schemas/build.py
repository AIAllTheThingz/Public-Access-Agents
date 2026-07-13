#!/usr/bin/env python3
"""Restore and run the schema-system generator from verified source fragments."""

from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "schemas"
PARTS = [('bootstrap/schemas/generator.part01.py', 3961, '370f5e6f6053babf757394468895ccba53f71ad449f4cc481aadd3371485b78f'), ('bootstrap/schemas/generator.part02.py', 3990, '5469ded95fe6e5536728b923e39e6a34c5aeffe9c8bb610b8bfa1881b8a869ef'), ('bootstrap/schemas/generator.part03.py', 3991, '2829dca4a21052eb4247c6dc0bd7f68773c77f1fe1f7dd3c3cf4defc7b79d9fc'), ('bootstrap/schemas/generator.part04.py', 3993, '5428159926847de61745f097fa33036668392c0165e883053a9aaa4b50a7c89c'), ('bootstrap/schemas/generator.part05.py', 3889, '21bf16de1c8c03f1bba1e4a9c30d00f95f839ebe22f52baeb03afe4dce3eca34'), ('bootstrap/schemas/generator.part06.py', 3991, '3345a20802dd4aea5517838af25b2c8863b3089c080d2a7a3e83ff010a947405'), ('bootstrap/schemas/generator.part07.py', 3971, '09b1331cfe5d275dab8b11f01b62922028c0e089001cbab25f9b5cfaec1ae9e7'), ('bootstrap/schemas/generator.part08.py', 3995, '5d65b6d91f7be1c8693d4d99a05dad21403777afccbac5363622c9f407a2d1dd'), ('bootstrap/schemas/generator.part09.py', 3989, '1573ba2689df303dceefd06edba5ccca1c0f98414c1f3784302ccb4335b49ac7'), ('bootstrap/schemas/generator.part10.py', 3997, '3b56745d7347ebaea5516a136c26669e20e05ab04788273d16d519060a799206'), ('bootstrap/schemas/generator.part11.py', 3978, 'ed49a2024a24f95e2ea827707f52d50afe5919d95c9c720cd5949f1d327d43c9'), ('bootstrap/schemas/generator.part12.py', 3983, '593606e60d3142ca0e616e601e3a824fb0a77191f1a5e26c673ecdd60766fa1d'), ('bootstrap/schemas/generator.part13.py', 3808, '58251528ebabb5c6feb00e255ae915e07b8f3496e0fffe93535cf391f65c0814'), ('bootstrap/schemas/generator.part14.py', 3986, 'eaaf84dc06d776312073445ee8d089c19a1012c6c29ff2d5f74f2068d8958264'), ('bootstrap/schemas/generator.part15.py', 3941, '8cd19bb631f37ea870d54272478ec6e6cddffa0671bad2734faaf2573f99dee8'), ('bootstrap/schemas/generator.part16.py', 514, '461192c97a5a4ef0f3476f5fc232aeb9803faf36e1031e731a9fa66946a4b71c')]
SOURCE_SHA256 = "aabc8d29f80985db55aefa258dbdaa5473fb9fd1d60c002db6d312c8f2515d90"

source_parts = []
for path_text, expected_length, expected_sha in PARTS:
    path = ROOT / path_text
    if not path.is_file():
        raise RuntimeError(f"Missing schema generator fragment: {path_text}")
    content = path.read_text(encoding="utf-8")
    if len(content) != expected_length:
        raise RuntimeError(
            f"Invalid length for {path_text}: expected {expected_length}, received {len(content)}"
        )
    actual_sha = hashlib.sha256(content.encode("utf-8")).hexdigest()
    if actual_sha != expected_sha:
        raise RuntimeError(
            f"Checksum mismatch for {path_text}: expected {expected_sha}, received {actual_sha}"
        )
    source_parts.append(content)

source = "".join(source_parts)
actual_source_sha = hashlib.sha256(source.encode("utf-8")).hexdigest()
if actual_source_sha != SOURCE_SHA256:
    raise RuntimeError(
        f"Schema generator checksum mismatch: expected {SOURCE_SHA256}, received {actual_source_sha}"
    )

generator = BOOTSTRAP / "generate_schema_system.py"
generator.write_text(source, encoding="utf-8")
subprocess.run(["python", str(generator)], check=True)

shutil.rmtree(BOOTSTRAP)
bootstrap = ROOT / "bootstrap"
if bootstrap.exists() and not any(bootstrap.iterdir()):
    bootstrap.rmdir()

print("Schema system generated from verified source.")
