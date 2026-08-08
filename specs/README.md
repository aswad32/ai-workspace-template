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
