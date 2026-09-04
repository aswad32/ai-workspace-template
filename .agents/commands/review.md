# Review Command

Use this workflow for `/review`.

## Goal

Review the current uncommitted change set in risk-focused passes without
modifying source files. Create one stable-ID pre-commit report for the related
SDD package, or under `specs/_reviews/` when no package applies.

## Workflow

1. Read project context, current branch, worktree status, and changed paths.
   Review only from a dedicated work branch unless the human explicitly
   authorizes review/report writing on a base branch.
2. Infer the related package from changed paths, the branch, task changes, and
   tracking references. Read only the relevant spec, plan, task, prior-report,
   documentation, and project-context sections.
3. Inspect staged, unstaged, and relevant untracked files. Start with shared
   contracts, configuration, data, security boundaries, dependencies, and
   tracker/prompt files. Escalate only when evidence requires it.
4. Check scope, correctness, regressions, authorization, input validation,
   privacy, domain invariants, tests, documentation, generated noise, local-only
   files, and secrets. Treat a suspected secret as Critical and do not echo it.
5. Classify findings as Critical, High, Medium, or Low. Critical and High are
   `must-fix`; Medium is normally `should-fix`; Low is `could-fix`. Assign IDs
   `PCR-<YYYYMMDDTHHMMSSZ>-<NNN>` using UTC.
6. Create the report from `templates/pre-commit-review.md` at
   `specs/<slug>/reviews/pre-commit-review-<timestamp>.md`, or under
   `specs/_reviews/` for non-package work. Include scope, context, evidence,
   file/line references, remediation, validation gaps, and residual risks. Use
   an unambiguous UTC timestamp. This report is the only permitted write during
   review.
7. Summarize findings, whether must-fix issues block the change, recommended
   focused validation, intentionally skipped broad checks, and the report path.

## Stop Conditions

Stop for a too-broad or unrelated diff, materially ambiguous package context,
uninspectable binary risk, or suspected secrets whose further inspection would
expose values.
