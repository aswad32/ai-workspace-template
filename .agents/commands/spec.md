# Spec Command

Use this workflow for `/spec <feature>`.

## Goal

Create a PR-sized SDD package with scoped requirements, measurable outcomes,
verifiable acceptance criteria, an implementation plan, and a traceable
execution checklist. This command does not approve or implement the package.

## Workflow

1. Read `.agents/project-context.md`; stop and request `/init-project` if it is
   missing or not ready.
2. Inspect only the existing code, docs, contracts, and tests relevant to the
   requested feature. Load UI, data, integration, or security context only when
   those areas are affected.
3. Resolve material scope, quality, data, security, compatibility, integration,
   operations, and user-experience questions. Record assumptions explicitly.
   Keep unresolved questions in `spec.md` and leave the package `Draft`.
4. Split the work when it spans independent review boundaries or cannot fit one
   focused pull request. Prefer a clear contract boundary between dependent
   packages over duplicate implementation detail.
5. Create a dedicated `docs/` or `feature/` branch from the configured base
   branch before writing package files, unless the human explicitly authorizes
   the current branch.
6. Create the next `specs/<number>-<slug>/` directory from `templates/spec.md`,
   `templates/plan.md`, and `templates/task.md`. Add an issue index only when
   the project context enables tracking.
7. If a tracker is configured, link or create the appropriate work item. If it
   is not configured, record `Tracking reference: None`; do not invent one.
8. Fill only applicable change areas. Use stable `FR-`, `QR-`, `AC-`, `SC-`,
   `P-`, and `T-` IDs. Trace every buildable requirement and acceptance
   criterion through the plan and task list; label necessary supporting tasks.
9. Inspect the three artifacts for contradictions, uncovered requirements,
   vague acceptance criteria, unresolved placeholders, and unnecessary scope.
   Leave status `Draft` and approval `Pending`, then direct the user to
   `/analyze-spec <spec-slug>` followed by `/approve-spec <spec-slug>`.

## Stop Conditions

Stop for human direction when a missing decision materially changes scope, a
quality target, data shape, security, compatibility, an external integration,
operations, or user-visible behavior; when a safe split is not evident; or when
the required tracker cannot be accessed and a canonical reference is mandatory.
