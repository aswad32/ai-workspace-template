# Execute Spec Command

Use this workflow for `/execute <spec-slug>`.

## Goal

Implement one accepted SDD package while preserving scope, project invariants,
documentation, and proportionate verification.

## Workflow

1. Confirm `specs/<spec-slug>/` contains `spec.md`, `plan.md`, and `task.md`.
   Stop if the package is missing; create one only when the user requests a new
   feature package.
2. Read project context, approval metadata, the latest spec-analysis result, the
   active task group, and only the source spec/plan sections needed for that
   task. Inspect the readiness gate, open questions, and blockers.
3. Stop unless the package is `Ready` or `In Progress`, its approval is current,
   and its latest spec analysis passed. Check the current branch and create or
   switch to a dedicated branch from the configured base branch before editing.
4. Set the package to `In Progress`. Implement only applicable unchecked tasks
   and preserve task IDs and source references. Keep decisions, acceptance
   evidence, contracts, and verification notes synchronized with actual work.
   If a material requirement or plan change is needed, stop, set the package to
   `Draft` with approval `Invalidated`, update the artifacts, and require a new
   `/analyze-spec` and `/approve-spec` cycle before continuing.
5. Follow project-context rules for authorization, validation, sensitive data,
   integrations, data integrity, UI guidance, documentation, and operations.
6. Run the focused project-context checks first. Escalate to broader tests,
   builds, migrations, audits, or end-to-end checks only when the changed risk
   boundary requires them. Record skipped checks and reasons.
7. Inspect the final diff for unrelated work, secrets, local-only files,
   documentation drift, incomplete tasks, and missing acceptance evidence.
   Leave the package `In Progress` and direct the user to
   `/verify-spec <spec-slug>`; only that workflow may mark it `Implemented`.

## Stop Conditions

Stop for absent or invalidated approval, a missing/passing-analysis mismatch,
unresolved package readiness, unavailable required credentials, conflicting
local changes, validation failures that need a broader decision, or work outside
the accepted package.
