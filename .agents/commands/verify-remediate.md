# Verify Remediate Command

Use this workflow for `/verify-remediate`.

## Goal

Verify each original pre-commit finding after remediation, check remediation-
touched areas for new regressions, and create a report without modifying source.

## Workflow

1. Read project context, current worktree, the source pre-commit review, the
   latest remediation report when present, and only the status sections of prior
   verification reports.
2. Map each original finding ID to its evidence, requested fix, remediation
   disposition, changed files, and current implementation.
3. Inspect only the finding-specific paths and direct dependencies. Check
   project-context invariants, relevant tests, contracts, and documentation.
4. Classify original findings as `resolved`, `partially resolved`, `unresolved`,
   or `no longer applicable`. Report any new regression as
   `VR-<YYYYMMDDHHMM>-<NNN>` without replacing original IDs.
5. Run read-safe focused validation when relevant; do not run commands known to
   rewrite snapshots, generated files, locks, or migrations without approval.
6. Write `verify-remediate-<timestamp>.md` beside the source report with each
   status, evidence, validation, skipped checks, new regressions, and risks.
   This report is the only permitted write during verification.
7. Summarize statuses, new regressions, validation, and next steps.

## Stop Conditions

Stop when reports cannot be mapped to findings, validation needs unsafe writes,
or verification requires unrelated broad reads or unavailable sensitive data.
