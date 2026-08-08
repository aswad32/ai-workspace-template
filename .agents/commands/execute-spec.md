# Execute Spec Command

Use this workflow for `/execute <spec-slug>`.

## Goal

Implement one accepted SDD package while preserving scope, project invariants,
documentation, and proportionate verification.

## Workflow

1. Confirm `specs/<spec-slug>/` contains `spec.md`, `plan.md`, and `task.md`.
   Stop if the package is missing; create one only when the user requests a new
   feature package.
2. Read project context, the active task group, and only the source spec/plan
   sections needed for that task. Inspect the readiness gate, open questions,
   and blockers before making changes.
3. Stop if questions or blockers remain. Check the current branch and create or
   switch to a dedicated branch from the configured base branch before editing.
4. Implement only applicable unchecked tasks. Keep the package’s task list,
   decisions, scope, contracts, and verification notes synchronized with actual
   work. Update spec and plan before extending scope.
5. Follow project-context rules for authorization, validation, sensitive data,
   integrations, data integrity, UI guidance, documentation, and operations.
6. Run the focused project-context checks first. Escalate to broader tests,
   builds, migrations, audits, or end-to-end checks only when the changed risk
   boundary requires them. Record skipped checks and reasons.
7. Inspect the final diff for unrelated work, secrets, local-only files,
   documentation drift, and incomplete task status. Summarize changes, results,
   risks, and rollback notes for review.

## Stop Conditions

Stop for unresolved package readiness, unavailable required credentials,
conflicting local changes, validation failures that need a broader decision, or
work outside the accepted package.
