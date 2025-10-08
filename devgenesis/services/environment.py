"""Environment checks for external tooling requirements."""

from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from typing import Iterable, List, Sequence


@dataclass
class ToolCheckResult:
    """Represents the outcome of a tool availability check."""

    tool: str
    available: bool
    version: str
    suggestion: str


def _probe_command(command: Sequence[str]) -> tuple[bool, str]:
    """Return (available, version_output) for the given command."""

    executable = command[0]
    if shutil.which(executable) is None:
        return False, ""

    try:
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired):
        return False, ""

    output = completed.stdout.strip() or completed.stderr.strip()
    return True, output


def check_environment() -> List[ToolCheckResult]:
    """Verify the presence of core development tools."""

    tools: Iterable[dict[str, object]] = [
        {
            "tool": "Python",
            "commands": [["python", "--version"], ["python3", "--version"]],
            "suggestion": "Installer Python 3.10+ et l'ajouter au PATH.",
        },
        {
            "tool": "Git",
            "commands": [["git", "--version"]],
            "suggestion": "Installer Git et vérifier la configuration globale.",
        },
        {
            "tool": "Node.js",
            "commands": [["node", "--version"]],
            "suggestion": "Installer Node.js LTS depuis nodejs.org.",
        },
        {
            "tool": "npm",
            "commands": [["npm", "--version"]],
            "suggestion": "Installer npm (fourni avec Node.js) ou vérifier le PATH.",
        },
        {
            "tool": "Docker",
            "commands": [["docker", "--version"]],
            "suggestion": "Installer Docker Desktop et démarrer le service.",
        },
        {
            "tool": "Docker Compose",
            "commands": [["docker", "compose", "version"], ["docker-compose", "--version"]],
            "suggestion": "Installer Docker Compose ou activer la commande 'docker compose'.",
        },
    ]

    results: List[ToolCheckResult] = []

    for spec in tools:
        commands: Iterable[Sequence[str]] = spec["commands"]  # type: ignore[assignment]
        suggestion: str = spec["suggestion"]  # type: ignore[assignment]
        tool_name: str = spec["tool"]  # type: ignore[assignment]

        available = False
        version_output = ""
        for command in commands:
            available, version_output = _probe_command(command)
            if available:
                break

        result = ToolCheckResult(
            tool=tool_name,
            available=available,
            version=version_output.splitlines()[0] if version_output else "",
            suggestion="OK" if available else suggestion,
        )
        results.append(result)

    return results


__all__ = ["ToolCheckResult", "check_environment"]
