# Spec Command

Use this workflow for `/spec <feature>`.

## Goal

Create a PR-sized SDD package with accepted scope, non-goals, verifiable
acceptance criteria, an implementation plan, and an execution checklist. This
command does not implement the feature.

## Workflow

1. Read `.agents/project-context.md`; stop and request `/init-project` if it is
   missing or not ready.
2. Inspect only the existing code, docs, contracts, and tests relevant to the
   requested feature. Load UI, data, integration, or security context only when
   those areas are affected.
3. Resolve material scope, data, security, integration, and user-experience
   questions. Record unresolved questions in `spec.md` and leave the package
   `Draft`.
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
8. Fill only the applicable change areas. Define the API, data, UI, processing,
   operations, privacy, and rollout requirements that apply to this feature.
9. Set the package to `Ready` only when its questions and blockers say `None`,
   the work is small enough to review, and the task list has a concrete
   readiness gate and verification plan.

## Stop Conditions

Stop for human direction when a missing decision materially changes scope, data
shape, security, an external integration, or user-visible behavior; when a safe
split is not evident; or when the required tracker cannot be accessed and a
canonical reference is mandatory for the project.
