# Fix Command

Use this workflow for `/fix <issue-or-description>`.

## Goal

Fix a confirmed defect with the smallest defensible change, a reproduction or
trace, targeted regression coverage where practical, and focused validation.

## Workflow

1. Read project context and the supplied tracker reference when tracking is
   enabled. If only a description is supplied, confirm the reported behavior
   with the user or local evidence before making assumptions.
2. Read only the related code, tests, docs, and existing SDD package sections.
   Trace or reproduce the symptom and distinguish evidence from hypotheses.
3. Create or switch to a `fix/` branch from the configured base branch before
   editing. Preserve unrelated local changes.
4. Identify the smallest responsible path. Add a narrow regression test when
   practical; otherwise document the manual verification that covers it.
5. Implement the fix without unrelated refactoring. Preserve project-context
   authorization, validation, sensitive-data, and domain-invariant rules.
6. Run the changed test first, then focused project-context validation. Broaden
   only when the touched boundary warrants it. Update relevant documentation and
   task/package records when behavior or contracts change.
7. Report the reproduction/trace, root cause, changed behavior, validation,
   skipped checks, tracking reference, and remaining risk. Do not automatically
   invoke review, remediation, commit, or PR workflows.

## Stop Conditions

Stop when the defect cannot be reproduced or traced, the fix needs an unstated
product decision, required tracker context is unavailable, local work conflicts,
or validation reveals a broader issue outside the requested fix.
