# Verify Remediate Command

Use this workflow for `/verify-remediate <review-report>`.

## Goal

Verify each original pre-commit finding after remediation, check remediation-
touched areas for new regressions, and create a report without modifying source.

## Workflow

1. Resolve the explicit `<review-report>` path. Read project context, current
   worktree, that source review, remediation reports linked to it, and only the
   status sections of prior verification reports. If the path is missing or
   ambiguous, stop rather than selecting a report by timestamp alone.
2. Map each original finding ID to its evidence, requested fix, remediation
   disposition, changed files, and current implementation.
3. Inspect only the finding-specific paths and direct dependencies. Check
   project-context invariants, relevant tests, contracts, and documentation.
4. Classify original findings as `resolved`, `partially resolved`, `unresolved`,
   or `no longer applicable`. Report any new regression as
   `VR-<YYYYMMDDTHHMMSSZ>-<NNN>` using UTC without replacing original IDs.
5. Run read-safe focused validation when relevant; do not run commands known to
   rewrite snapshots, generated files, locks, or migrations without approval.
6. Create `verify-remediate-<timestamp>.md` beside the source report from
   `templates/verification.md`, with each status, evidence, validation, skipped
   checks, new regressions, and risks. Record exact links to the source review
   and remediation report. This report is the only permitted write during
   verification.
7. Summarize statuses, new regressions, validation, and next steps.

## Stop Conditions

Stop when reports cannot be mapped to findings, validation needs unsafe writes,
or verification requires unrelated broad reads or unavailable sensitive data.
