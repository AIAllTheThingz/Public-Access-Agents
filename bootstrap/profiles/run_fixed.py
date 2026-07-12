#!/usr/bin/env python3
"""Patch the merged profile builder with verified fragments, then execute it."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "profiles"
SOURCE = BOOTSTRAP / "build.py"
FIXED = BOOTSTRAP / "build.fixed.py"

PARTS = [
    ("bootstrap/profiles/generator.part01a.b64", 2000, "fc4edf4f950b09704cbac66d3d96adc1810ce54d10acb833d50c67071318223b"),
    ("bootstrap/profiles/generator.part01b.b64", 2000, "782e39744df9c45c600188372e9e392c5abd12fffc59db67cf57234ea672326f"),
    ("bootstrap/profiles/generator.part01c.b64", 2000, "4b4debd63cf78944e2aba25752469e57bfaf7792272dc2de1f6eebe63c6508b5"),
    ("bootstrap/profiles/generator.part01d.b64", 2000, "25c409ce5528201f8bdbad99d2acd80e650325d0743643944009704de0fc4401"),
    ("bootstrap/profiles/generator.part02.b64", 8000, "546635c1aaaca382b08d1bce93628d42283b08fb6c1d86eb4a4ff0c2d3c05601"),
    ("bootstrap/profiles/generator.part03.b64", 8000, "31435a6a937bffa9ccb9b0cdc510208fa61ff4ecc5cc990c2bd7ac1b4cec9cc5"),
    ("bootstrap/profiles/generator.part04.b64", 2408, "667e826c6db3346c9754d76472e6576f50413dbb63f2064c743cf0b0712a586d"),
]
GENERATOR_SHA256 = "d6ad3648bd380bbd4b7a0975a71e006c19ea22bb9ec33ed55b22af6802d38dd8"

failure_log = ROOT / "profile-build-failure.log"
if failure_log.exists():
    failure_log.unlink()

text = SOURCE.read_text(encoding="utf-8")
text = re.sub(r"^PARTS = .*?$", f"PARTS = {PARTS!r}", text, flags=re.MULTILINE)
text = re.sub(
    r'^GENERATOR_SHA256 = ".*?"$',
    f'GENERATOR_SHA256 = "{GENERATOR_SHA256}"',
    text,
    flags=re.MULTILINE,
)
FIXED.write_text(text, encoding="utf-8")
subprocess.run(["python", str(FIXED)], check=True)
