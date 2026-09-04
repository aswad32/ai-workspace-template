# Verify Spec Command

Use this workflow for `/verify-spec <spec-slug>`.

## Goal

Compare the current implementation with the approved spec, plan, and task list;
record evidence for every obligation; and identify any remaining work before
general code review.

## Workflow

1. Read project context, the approved package, latest analysis, current branch
   and worktree, changed paths, task state, and existing acceptance evidence.
   Stop if approval is absent or invalidated.
2. Build an intent inventory from every `FR-`, `QR-`, `AC-`, applicable buildable
   `SC-`, material plan decision, and project-context invariant. Preserve the
   source IDs.
3. Inspect the implementation and direct dependencies. Map each source item to
   code, tests, documentation, configuration, migrations, or manual evidence and
   classify it `Satisfied`, `Partial`, `Missing`, `Contradicted`, or
   `Not verifiable`.
4. Run focused, read-safe validation from project context. Run broader checks
   only when the changed boundary requires them. Record skipped or unavailable
   checks without treating them as passes.
5. Create `reviews/spec-verification-<UTC-timestamp>.md` from
   `templates/spec-verification.md`. Use deterministic finding IDs tied to the
   source, such as `SV-FR-001`; retain IDs across reruns for the same gap.
6. If gaps remain, append a new `### Convergence <UTC-timestamp>` group to
   `task.md` with new, never-reused `T-` IDs and exact source references. Do not
   rewrite completed tasks. Keep package status `In Progress`.
7. If all obligations are satisfied and required validation passes, mark all
   three package artifacts `Implemented`, update `Latest spec verification`, and
   synchronize the acceptance-evidence table. This workflow must not mark a
   package `Done`.
8. Report coverage counts, result, appended tasks if any, validation, report
   path, and whether the package may proceed to `/review`.

## Stop Conditions

Stop for invalidated approval, artifacts changed after approval without
re-analysis, uninspectable required evidence, unsafe validation requiring new
authority, or scope too broad to verify reliably.
