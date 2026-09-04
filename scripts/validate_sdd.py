#!/usr/bin/env python3
"""Validate the portable SDD workspace without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
VALID_STATUSES = {
    "Draft",
    "Ready",
    "In Progress",
    "Implemented",
    "Done",
    "Superseded",
    "Abandoned",
}
REQUIRED_COMMANDS = {
    "init-project",
    "analyze-project",
    "design-architecture",
    "spec",
    "analyze-spec",
    "approve-spec",
    "execute-spec",
    "verify-spec",
    "fix",
    "capture-issues",
    "review",
    "remediate",
    "verify-remediate",
    "commit",
    "pr",
    "close-spec",
}
REQUIRED_TEMPLATES = {
    "spec.md",
    "plan.md",
    "task.md",
    "pr.md",
    "issues-index.md",
    "spec-analysis.md",
    "spec-verification.md",
    "pre-commit-review.md",
    "remediation.md",
    "verification.md",
}
ACTIVE_OR_LATER = {"Ready", "In Progress", "Implemented", "Done"}
IMPLEMENTED_OR_LATER = {"Implemented", "Done"}


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )


def check_local_links(errors: list[str]) -> None:
    link_pattern = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
    for document in markdown_files():
        text = document.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>").split(" ", 1)[0]
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "<" in target
                or ">" in target
            ):
                continue
            path_part = unquote(target.split("#", 1)[0])
            resolved = (document.parent / path_part).resolve()
            if not resolved.exists():
                errors.append(
                    f"{document.relative_to(ROOT)}: missing local link target {target}"
                )


def check_workspace_contract(errors: list[str]) -> None:
    commands_dir = ROOT / ".agents" / "commands"
    templates_dir = ROOT / "templates"
    command_names = {path.stem for path in commands_dir.glob("*.md")}
    template_names = {path.name for path in templates_dir.glob("*.md")}

    for name in sorted(REQUIRED_COMMANDS - command_names):
        errors.append(f"missing command workflow: .agents/commands/{name}.md")
    for name in sorted(REQUIRED_TEMPLATES - template_names):
        errors.append(f"missing artifact template: templates/{name}")

    agents_text = (ROOT / "AGENTS.md").read_text(encoding="utf-8")
    for name in sorted(REQUIRED_COMMANDS):
        command_path = f".agents/commands/{name}.md"
        if command_path not in agents_text:
            errors.append(f"AGENTS.md does not route to {command_path}")

    version = (ROOT / "TEMPLATE_VERSION")
    if not version.exists() or not version.read_text(encoding="utf-8").strip():
        errors.append("TEMPLATE_VERSION is missing or empty")


def artifact_status(path: Path, errors: list[str]) -> str | None:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^- Status:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    if not match:
        errors.append(f"{path.relative_to(ROOT)}: missing '- Status:' metadata")
        return None
    status = match.group(1).strip()
    if status not in VALID_STATUSES:
        errors.append(
            f"{path.relative_to(ROOT)}: invalid status {status!r}; "
            f"expected one of {sorted(VALID_STATUSES)}"
        )
        return None
    return status


def duplicate_definition_ids(text: str, prefix: str) -> list[str]:
    if prefix == "T":
        pattern = r"^\s*- \[[ xX]\]\s+(T-\d{3})\b"
    else:
        pattern = rf"^\s*-\s+({re.escape(prefix)}-\d{{3}}):"
    ids = re.findall(pattern, text, flags=re.MULTILINE)
    return sorted({item for item in ids if ids.count(item) > 1})


def check_packages(errors: list[str]) -> None:
    specs_dir = ROOT / "specs"
    packages = [
        path
        for path in specs_dir.iterdir()
        if path.is_dir() and re.match(r"^\d+-", path.name)
    ]
    number_groups: dict[str, list[str]] = {}
    for package in packages:
        number = package.name.split("-", 1)[0]
        number_groups.setdefault(number, []).append(package.name)
    for number, names in sorted(number_groups.items()):
        if len(names) > 1:
            errors.append(f"duplicate spec number {number}: {', '.join(sorted(names))}")

    for package in sorted(packages):
        required = {name: package / name for name in ("spec.md", "plan.md", "task.md")}
        for name, path in required.items():
            if not path.exists():
                errors.append(f"{package.relative_to(ROOT)}: missing {name}")
        if not all(path.exists() for path in required.values()):
            continue

        statuses = {name: artifact_status(path, errors) for name, path in required.items()}
        known_statuses = {status for status in statuses.values() if status is not None}
        if len(known_statuses) > 1:
            errors.append(
                f"{package.relative_to(ROOT)}: inconsistent artifact statuses {statuses}"
            )

        spec_text = required["spec.md"].read_text(encoding="utf-8")
        plan_text = required["plan.md"].read_text(encoding="utf-8")
        task_text = required["task.md"].read_text(encoding="utf-8")
        for prefix in ("FR", "QR", "AC", "SC", "AS"):
            duplicates = duplicate_definition_ids(spec_text, prefix)
            if duplicates:
                errors.append(
                    f"{required['spec.md'].relative_to(ROOT)}: duplicate IDs "
                    f"{', '.join(duplicates)}"
                )
        task_duplicates = duplicate_definition_ids(task_text, "T")
        if task_duplicates:
            errors.append(
                f"{required['task.md'].relative_to(ROOT)}: duplicate task IDs "
                f"{', '.join(task_duplicates)}"
            )

        status = statuses["spec.md"]
        if status in ACTIVE_OR_LATER:
            if "- Approval: Approved" not in spec_text:
                errors.append(f"{package.relative_to(ROOT)}: {status} package is not approved")
            if re.search(r"- Latest spec analysis:\s*(?:Not run|<)", spec_text):
                errors.append(
                    f"{package.relative_to(ROOT)}: {status} package lacks spec analysis"
                )
            unresolved = re.findall(r"<[^>\n]+>", spec_text)
            if unresolved:
                errors.append(
                    f"{required['spec.md'].relative_to(ROOT)}: unresolved placeholders "
                    f"in {status} package"
                )

            source_ids = set(re.findall(r"\b(?:FR|QR|AC)-\d{3}\b", spec_text))
            unplanned = sorted(source_id for source_id in source_ids if source_id not in plan_text)
            if unplanned:
                errors.append(
                    f"{package.relative_to(ROOT)}: source IDs absent from plan.md: "
                    f"{', '.join(unplanned)}"
                )
            untasked = sorted(source_id for source_id in source_ids if source_id not in task_text)
            if untasked:
                errors.append(
                    f"{package.relative_to(ROOT)}: source IDs absent from task.md: "
                    f"{', '.join(untasked)}"
                )

        if status in IMPLEMENTED_OR_LATER:
            if re.search(r"- Latest spec verification:\s*(?:Not run|<)", task_text):
                errors.append(
                    f"{package.relative_to(ROOT)}: {status} package lacks spec verification"
                )
        if status == "Done" and re.search(
            r"- Delivery evidence:\s*(?:Not delivered|<)", spec_text
        ):
            errors.append(f"{package.relative_to(ROOT)}: Done package lacks delivery evidence")


def main() -> int:
    errors: list[str] = []
    check_local_links(errors)
    check_workspace_contract(errors)
    check_packages(errors)

    if errors:
        print("SDD validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("SDD validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
