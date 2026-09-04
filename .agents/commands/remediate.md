# Remediate Command

Use this workflow for `/remediate <review-report>`.

## Goal

Resolve open must-fix findings and approved should-fix findings from the latest
pre-commit review, then record the disposition of every finding without
rewriting the original report.

## Workflow

1. Resolve the explicit `<review-report>` path. Read project context, current
   branch/worktree, and that report. If the path is omitted and exactly one open
   pre-commit report applies, present it and ask the user to confirm; otherwise
   stop rather than guessing. Work only on a dedicated branch.
2. Fix all open must-fix findings unless current evidence proves them false,
   duplicated, obsolete, or no longer applicable. Fix should-fix findings only
   with explicit approval or when necessary for a must-fix change.
3. Read only the finding-specific code, documentation, tests, and package
   context. Make the smallest change that resolves each selected finding and
   preserves project-context invariants.
4. Run focused validation for remediation-touched areas; broaden only when the
   changed risk boundary warrants it. Record unavailable or skipped checks.
5. Create `remediation-<timestamp>.md` beside the source review report from
   `templates/remediation.md`, retaining the original finding IDs and marking
   each as fixed, partially fixed, false positive, duplicate, no longer
   applicable, deferred, or not approved. Record the exact source-report link.
6. Summarize changed files, validation, remaining risks, and findings requiring
   human approval or follow-up.

## Stop Conditions

Stop for a missing or ambiguous review report, a shared/base branch, unapproved
should-fix work, scope decisions beyond the accepted package, conflicting local
work, or broader validation failures.
