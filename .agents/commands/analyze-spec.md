# Analyze Spec Command

Use this workflow for `/analyze-spec <spec-slug>`.

## Goal

Check a candidate SDD package for clarity, consistency, traceability, and
readiness before approval. Do not approve the package or modify implementation
code.

## Workflow

1. Read project context and resolve `specs/<spec-slug>/spec.md`, `plan.md`, and
   `task.md`. Stop when an artifact is missing or the package scope is ambiguous.
2. Build an inventory of user stories, `FR-`, `QR-`, `AC-`, and buildable `SC-`
   items. Map each item to plan decisions, planned paths, task IDs, and a stated
   validation method.
3. Check for contradictory or duplicate requirements, vague or untestable
   language, uncovered requirements, orphan tasks, unresolved placeholders,
   unjustified supporting work, missing edge cases, and inconsistent terms.
4. Check applicable security, privacy, data integrity, compatibility,
   accessibility, reliability, operations, rollout, and documentation concerns
   against project context. Do not require irrelevant sections.
5. Classify findings as `Blocking`, `Warning`, or `Note`. Use deterministic IDs
   such as `SA-COVERAGE-FR-001`; use a stable category and sequence when no
   source ID exists. A rerun must retain an existing ID for the same issue.
6. Create `reviews/spec-analysis-<UTC-timestamp>.md` from
   `templates/spec-analysis.md`. Mark the result `Pass` only when there are no
   blocking findings; warnings require an explicit disposition.
7. Update only the `Latest spec analysis` links in `spec.md` and `task.md`. Do
   not change requirements, plan decisions, tasks, approval, or status during
   analysis.
8. Report coverage counts, findings, report path, and the precise next action.
   A passing analysis permits `/approve-spec`; it does not itself grant approval.

## Stop Conditions

Stop for missing artifacts, materially ambiguous scope, conflicting local work,
or analysis that would require secrets or unavailable sensitive data.
