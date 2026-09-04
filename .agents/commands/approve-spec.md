# Approve Spec Command

Use this workflow for `/approve-spec <spec-slug>`.

## Goal

Record explicit human acceptance of a complete, analyzed SDD package so that
implementation may begin.

## Workflow

1. Read project context, all three package artifacts, and the exact report linked
   by `Latest spec analysis`. Approval must be an explicit user request; do not
   infer it from silence or from creation of the package.
2. Stop unless the analysis result is `Pass`, blocking findings are absent,
   warnings have dispositions, questions and blockers say `None`, required
   placeholders are resolved, and the package remains within one reviewable
   change boundary.
3. Present a concise approval summary: goals, non-goals, material contracts,
   data/security impact, quality targets, delivery risks, and skipped items.
4. Record `Approval: Approved`, the provided approver identity or
   `Human user (interactive approval)`, and the approval date in `spec.md`. Set
   `spec.md`, `plan.md`, and `task.md` to `Ready` and link the approved spec from
   the plan.
5. Mark only the analysis and approval items in the task readiness gate. Leave
   branch, inspection, and other runtime checks unchanged until verified.
6. Report the approved package, analysis report, approver record, and next action
   `/execute <spec-slug>`.

## Approval Invalidation

Any later material change to scope, requirements, acceptance criteria,
architecture, contracts, data, security, quality targets, operations,
validation, or user-visible behavior must set `Approval: Invalidated`, return all
three artifacts to `Draft`, and require a new analysis and approval cycle.

## Stop Conditions

Stop for non-passing analysis, unresolved decisions, stale analysis, ambiguous
approver authority under project rules, or package changes made after analysis.
