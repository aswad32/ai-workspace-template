# Close Spec Command

Use this workflow for `/close-spec <spec-slug>`.

## Goal

Record the terminal outcome of an SDD package after its configured delivery
point, keep the package as immutable change history, and update the package index.

## Workflow

1. Read project context, `specs/index.md`, the package artifacts, the passing
   spec-verification report, review/remediation evidence, and delivery evidence.
2. For `Done`, require package status `Implemented`, no unresolved must-fix
   findings, and objective evidence that the `Delivery completion point` in
   project context was reached. A commit or open PR is not delivery unless the
   project context explicitly defines it that way.
3. For `Superseded`, require the replacement package reference. For `Abandoned`,
   require a concise reason and confirm that no partial delivery is being
   misrepresented. These outcomes do not require implementation evidence.
4. If closure happens after merge, create a dedicated `docs/` or `chore/` branch
   from the configured base branch before writing. Preserve unrelated changes.
5. Update status consistently in `spec.md`, `plan.md`, and `task.md`. For `Done`,
   record delivery evidence and completion date. Update reciprocal `Supersedes`
   and `Superseded by` links when applicable.
6. Add or update exactly one row in `specs/index.md` with package, outcome,
   approval, verification, delivery evidence, and replacement link.
7. After closure, treat package intent and evidence as immutable history. Permit
   only factual metadata corrections and supersession links; new behavior
   requires a new package.
8. Validate links and report the terminal status, evidence, index update, and
   any follow-up documentation work.

## Stop Conditions

Stop for missing or contradictory delivery evidence, open must-fix findings,
ambiguous terminal outcome, missing replacement reference for supersession, or
conflicting local changes.
