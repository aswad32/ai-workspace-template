# SDD Packages

Each reviewable unit of work lives in `specs/<number>-<slug>/` and normally
contains:

- `spec.md`: problem, scope, non-goals, requirements, and acceptance criteria.
- `plan.md`: technical approach, risks, and verification strategy.
- `task.md`: readiness gate and execution checklist.
- `issues/index.md`: optional tracker index.
- `reviews/`: review, remediation, and verification reports.

Create packages through `/spec <feature>` so numbering, scope, and project
context stay consistent. Keep `_reviews/` only for cross-package or template
maintenance reports.

Use [index.md](index.md) as the lifecycle index. Package states are:

- `Draft`: incomplete, unresolved, or changed since approval.
- `Ready`: spec analysis passed and human approval is recorded.
- `In Progress`: implementation or convergence is active.
- `Implemented`: spec verification passed; delivery may still be pending.
- `Done`: the configured delivery point was reached and `/close-spec` recorded
  the evidence.
- `Superseded` or `Abandoned`: closed without representing current delivered
  behavior.

Completed packages remain in place as immutable change history. Do not silently
rewrite them when behavior evolves; create a new package and record reciprocal
supersession links. Durable current-state behavior belongs in the authoritative
documentation paths declared by project context.
