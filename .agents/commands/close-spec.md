# Close Spec Command

Use this workflow for `/close-spec <spec-slug>`.

## Goal

Record the terminal outcome of an SDD package after its configured delivery
point, keep the package as immutable change history, and update the package index.

## Workflow

1. Read project context, `specs/index.md`, the package artifacts, the passing
   spec-verification report, review/remediation evidence, delivery evidence, and
   the pull or merge request's work-item closure plan when present. Collect and
   deduplicate tracker references from the spec, plan, task, and optional
   `issues/index.md`. A non-`None` `Tracking reference` in `spec.md` is the
   package's canonical linked work item even if no issue-index row exists;
   never omit it because the PR did not mention it.
2. For `Done`, require package status `Implemented`, no unresolved must-fix
   findings, and objective evidence that the `Delivery completion point` in
   project context was reached. A commit or open PR is not delivery unless the
   project context explicitly defines it that way.
3. For `Done`, inspect each linked work item's current status in the configured
   tracker. Verify any automatic closure promised by the request. Close an item
   still open only when the delivered package fully resolves it; record the tracker
   closure reference alongside delivery evidence. For the spec's tracking item,
   compare its scope with the approved spec and verified delivery before
   deciding it remains open. Leave wider or outstanding items open only with
   the specific unfinished work and next owner or package recorded. If tracker
   access or a required closure fails, leave the package `Implemented` and
   report the blocker.
   When tracking is `None`, do not invent or close an external item.
4. For `Superseded`, require the replacement package reference. For `Abandoned`,
   require a concise reason and confirm that no partial delivery is being
   misrepresented. These outcomes do not require implementation evidence. Do
   not close linked work items merely because the package is terminal; report
   their remaining status and replacement or follow-up reference.
5. If closure happens after merge, create a dedicated `docs/` or `chore/` branch
   from the configured base branch before writing. Preserve unrelated changes.
6. Update status consistently in `spec.md`, `plan.md`, and `task.md`. For `Done`,
   record delivery evidence, work-item closure evidence or open-item disposition,
   and completion date. Update actual tracker statuses in the optional
   `issues/index.md`; do not mark an item closed without verifying it in the
   tracker. Update reciprocal `Supersedes` and `Superseded by` links when
   applicable.
7. Add or update exactly one row in `specs/index.md` with package, outcome,
   approval, verification, delivery evidence, and replacement link.
8. After closure, treat package intent and evidence as immutable history. Permit
   only factual metadata corrections and supersession links; new behavior
   requires a new package.
9. Validate links and report the terminal status, tracker actions and remaining
   open items, evidence, index update, and any follow-up documentation work.

## Stop Conditions

Stop for missing or contradictory delivery evidence, open must-fix findings,
ambiguous terminal outcome, missing replacement reference for supersession,
unavailable tracker access or failed closure for an item the package fully
resolves, unclear scope of the spec's tracking item, or conflicting local
changes.
