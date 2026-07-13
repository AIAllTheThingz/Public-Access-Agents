"""Common result models used by repository tools."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Finding:
    """A structured tool finding."""

    code: str
    message: str
    severity: str = "error"
    path: str | None = None
    line: int | None = None
    details: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        value: dict[str, Any] = {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
        }
        if self.path is not None:
            value["path"] = self.path
        if self.line is not None:
            value["line"] = self.line
        if self.details:
            value["details"] = self.details
        return value


@dataclass
class ToolResult:
    """A stable machine-readable tool result."""

    tool: str
    version: str
    status: str
    summary: dict[str, Any] = field(default_factory=dict)
    findings: list[Finding] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_findings(
        cls,
        *,
        tool: str,
        version: str,
        findings: list[Finding],
        summary: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
    ) -> "ToolResult":
        status = "failed" if any(item.severity == "error" for item in findings) else "passed"
        return cls(
            tool=tool,
            version=version,
            status=status,
            summary=summary or {},
            findings=findings,
            metadata=metadata or {},
        )

    @classmethod
    def error(cls, *, tool: str, version: str, message: str, code: str="TOOL_ERROR") -> "ToolResult":
        return cls(
            tool=tool,
            version=version,
            status="error",
            findings=[Finding(code=code, message=message, severity="error")],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            "tool": self.tool,
            "version": self.version,
            "status": self.status,
            "summary": self.summary,
            "findings": [item.to_dict() for item in self.findings],
            "metadata": self.metadata,
        }

    def exit_code(self) -> int:
        if self.status == "passed":
            return 0
        if self.status == "failed":
            return 1
        return 3
