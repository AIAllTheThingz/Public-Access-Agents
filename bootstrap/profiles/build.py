#!/usr/bin/env python3
"""Restore, run, and validate the project profile generator."""

from __future__ import annotations

import base64
import hashlib
import lzma
import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path.cwd()
BOOTSTRAP = ROOT / "bootstrap" / "profiles"
PROFILE_ROOT = ROOT / "profiles"
PARTS = [('bootstrap/profiles/generator.part01.b64', 8000, '85737d1fb03c9044d4a38cd401a839c733e6e5ac788fd59b5c2ab4dea50c4f45'), ('bootstrap/profiles/generator.part02.b64', 8000, '546635c1aaaca382b08d1bce93628d42283b08fb6c1d86eb4a4ff0c2d3c05601'), ('bootstrap/profiles/generator.part03.b64', 8000, '31435a6a937bffa9ccb9b0cdc510208fa61ff4ecc5cc990c2bd7ac1b4cec9cc5'), ('bootstrap/profiles/generator.part04.b64', 2408, '667e826c6db3346c9754d76472e6576f50413dbb63f2064c743cf0b0712a586d')]
GENERATOR_SHA256 = "e26e409cf610579941fc7895e1a99bc386a9ec41c0c7b71db57b9c91154ed632"
PROFILE_META = {'WEB_API.md': {'id': 'PROFILE-WEB-API', 'slug': 'web-api', 'required': ['application-security', 'architecture', 'testing', 'api-engineering', 'privacy', 'observability', 'ci-cd', 'supply-chain', 'release-engineering']}, 'WEB_APPLICATION.md': {'id': 'PROFILE-WEB-APP', 'slug': 'web-application', 'required': ['application-security', 'architecture', 'testing', 'accessibility', 'privacy', 'observability', 'ci-cd', 'supply-chain', 'release-engineering']}, 'WORKER_SERVICE.md': {'id': 'PROFILE-WORKER', 'slug': 'worker-service', 'required': ['architecture', 'testing', 'integration', 'observability', 'sre', 'ci-cd', 'supply-chain', 'release-engineering']}, 'CLI_TOOL.md': {'id': 'PROFILE-CLI', 'slug': 'cli-tool', 'required': ['application-security', 'testing', 'documentation', 'supply-chain', 'release-engineering']}, 'DESKTOP_APPLICATION.md': {'id': 'PROFILE-DESKTOP', 'slug': 'desktop-application', 'required': ['application-security', 'architecture', 'testing', 'accessibility', 'privacy', 'documentation', 'release-engineering']}, 'MOBILE_APPLICATION.md': {'id': 'PROFILE-MOBILE', 'slug': 'mobile-application', 'required': ['application-security', 'architecture', 'testing', 'accessibility', 'privacy', 'supply-chain', 'release-engineering']}, 'SERVERLESS_FUNCTION.md': {'id': 'PROFILE-SERVERLESS', 'slug': 'serverless-function', 'required': ['application-security', 'testing', 'integration', 'observability', 'ci-cd', 'supply-chain']}, 'DATA_PIPELINE.md': {'id': 'PROFILE-DATA-PIPELINE', 'slug': 'data-pipeline', 'required': ['architecture', 'testing', 'integration', 'database', 'data-engineering', 'privacy', 'observability', 'sre']}, 'PUBLIC_LIBRARY.md': {'id': 'PROFILE-LIB', 'slug': 'public-library', 'required': ['architecture', 'testing', 'documentation', 'supply-chain', 'release-engineering']}, 'INTERNAL_AUTOMATION.md': {'id': 'PROFILE-AUTOMATION', 'slug': 'internal-automation', 'required': ['application-security', 'testing', 'documentation', 'observability', 'ci-cd', 'supply-chain']}, 'MULTI_TENANT_SAAS.md': {'id': 'PROFILE-SAAS', 'slug': 'multi-tenant-saas', 'required': ['application-security', 'architecture', 'testing', 'api-engineering', 'database', 'privacy', 'observability', 'sre', 'ci-cd', 'supply-chain', 'release-engineering']}, 'SECURITY_TOOL.md': {'id': 'PROFILE-SECTOOL', 'slug': 'security-tool', 'required': ['application-security', 'architecture', 'testing', 'privacy', 'observability', 'documentation', 'supply-chain', 'release-engineering']}, 'AI_AGENT_APPLICATION.md': {'id': 'PROFILE-AI-AGENT', 'slug': 'ai-agent-application', 'required': ['application-security', 'architecture', 'testing', 'api-engineering', 'privacy', 'observability', 'supply-chain']}}

def run(*args: str) -> None:
    subprocess.run(args, check=True)

def restore_generator() -> Path:
    encoded=[]
    for path_text, expected_length, expected_sha in PARTS:
        path=ROOT/path_text
        if not path.is_file():
            raise RuntimeError(f"Missing generator part: {path_text}")
        content="".join(path.read_text(encoding="ascii").split())
        if len(content)!=expected_length:
            raise RuntimeError(f"Invalid length for {path_text}")
        actual=hashlib.sha256(content.encode("ascii")).hexdigest()
        if actual!=expected_sha:
            raise RuntimeError(f"Checksum mismatch for {path_text}")
        encoded.append(content)
    compressed=base64.b64decode("".join(encoded),validate=True)
    actual=hashlib.sha256(compressed).hexdigest()
    if actual!=GENERATOR_SHA256:
        raise RuntimeError("Generator archive checksum mismatch")
    source=lzma.decompress(compressed)
    path=BOOTSTRAP/"generate_profiles.py"
    path.write_bytes(source)
    return path

def validate_profiles() -> None:
    errors=[]
    required_collection=[
        PROFILE_ROOT/"AGENTS.md",
        PROFILE_ROOT/"README.md",
        PROFILE_ROOT/"MANIFEST.md",
        PROFILE_ROOT/"PROFILE_SELECTION_GUIDE.md",
        PROFILE_ROOT/"PROFILE_COMPOSITION_MODEL.md",
        PROFILE_ROOT/"PROFILE_RISK_EVIDENCE_MATRIX.md",
        PROFILE_ROOT/"PROFILE_LIFECYCLE.md",
        PROFILE_ROOT/"PROFILE_DECISION_MATRIX.md",
    ]
    for path in required_collection:
        if not path.is_file():
            errors.append(f"Missing collection file: {path}")

    ids={}
    fm=re.compile(r"^---\n(.*?)\n---",re.DOTALL)
    id_line=re.compile(r"^id:\s*(\S+)",re.MULTILINE)
    placeholder=re.compile(r"\{\{|\}\}|\{data|<TODO>|\bTBD\b",re.IGNORECASE)
    for path in sorted(PROFILE_ROOT.rglob("*.md")):
        text=path.read_text(encoding="utf-8")
        match=fm.match(text)
        if not match:
            errors.append(f"Missing front matter: {path}")
            continue
        id_match=id_line.search(match.group(1))
        if not id_match:
            errors.append(f"Missing ID: {path}")
        else:
            doc_id=id_match.group(1)
            if doc_id in ids:
                errors.append(f"Duplicate ID {doc_id}: {path} and {ids[doc_id]}")
            ids[doc_id]=path
        if placeholder.search(text):
            errors.append(f"Unresolved placeholder: {path}")

    if len(ids)!=190:
        errors.append(f"Expected 190 profile IDs, received {len(ids)}")

    for canonical_name, metadata in PROFILE_META.items():
        canonical=PROFILE_ROOT/canonical_name
        package=PROFILE_ROOT/metadata["slug"]
        required=[
            canonical,
            package/"AGENTS.md",
            package/"README.md",
            package/"MANIFEST.md",
            package/"templates"/"ADOPTION_CHECKLIST.md",
            package/"templates"/"REVIEW_CHECKLIST.md",
            package/"templates"/"EVIDENCE_RECORD_TEMPLATE.md",
            package/"examples"/"ADOPTION_EXAMPLE.md",
        ]
        for path in required:
            if not path.is_file():
                errors.append(f"Missing profile package file: {path}")
        if canonical.is_file():
            text=canonical.read_text(encoding="utf-8")
            if f"id: {metadata['id']}" not in text:
                errors.append(f"Canonical ID not preserved: {canonical}")
            for discipline in metadata["required"]:
                if f"disciplines/{discipline}/AGENTS.md" not in text:
                    errors.append(f"Missing required discipline {discipline} in {canonical}")
        readme=package/"README.md"
        if readme.is_file() and len(readme.read_text(encoding="utf-8").splitlines())<220:
            errors.append(f"README appears incomplete: {readme}")
        standards=list((package/"standards").glob("*.md"))
        if len(standards)!=6:
            errors.append(f"Expected six standards in {package}, received {len(standards)}")

    if errors:
        print("Profile-specific validation failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)
    print(f"Profile-specific validation passed: {len(ids)} unique IDs.")

def cleanup_and_commit() -> None:
    shutil.rmtree(BOOTSTRAP)
    bootstrap=ROOT/"bootstrap"
    if bootstrap.exists() and not any(bootstrap.iterdir()):
        bootstrap.rmdir()
    run("git","config","user.name","github-actions[bot]")
    run("git","config","user.email","41898282+github-actions[bot]@users.noreply.github.com")
    run("git","add","-A")
    status=subprocess.run(["git","diff","--cached","--quiet"],check=False)
    if status.returncode==0:
        print("No profile changes were produced.")
        return
    run("git","commit","-m","Complete project profile packages")
    run("git","push")

def main() -> int:
    if not BOOTSTRAP.exists():
        print("Profile packages are already generated; nothing to do.")
        return 0
    generator=restore_generator()
    run("python",str(generator))
    run("python","tools/validate-standards/validate_repository.py")
    run("python","tools/check-links/check_links.py")
    validate_profiles()
    cleanup_and_commit()
    return 0

if __name__=="__main__":
    raise SystemExit(main())
