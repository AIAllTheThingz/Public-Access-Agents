"""Text and JSON output helpers."""

from __future__ import annotations

import json
from pathlib import Path

from .models import ToolResult


def render_text(result: ToolResult) -> str:
    lines = [f"{result.tool}: {result.status}"]
    for key, value in sorted(result.summary.items()):
        lines.append(f"  {key}: {value}")
    for finding in result.findings:
        location = finding.path or ""
        if finding.line is not None:
            location = f"{location}:{finding.line}" if location else f"line {finding.line}"
        prefix = f"[{finding.severity.upper()}] {finding.code}"
        if location:
            prefix += f" {location}"
        lines.append(f"{prefix}: {finding.message}")
    if not result.findings and result.status == "passed":
        lines.append("No findings.")
    return "\n".join(lines) + "\n"


def emit_result(
    result: ToolResult,
    *,
    output_format: str,
    output: Path | None,
    quiet: bool,
) -> None:
    if output_format == "json":
        rendered = json.dumps(result.to_dict(), indent=2, sort_keys=True) + "\n"
    else:
        rendered = render_text(result)

    if output is not None:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")

    if not quiet:
        print(rendered, end="")
