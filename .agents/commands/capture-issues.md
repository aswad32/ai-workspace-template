# Capture Issues Command

Use this workflow for `/capture-issues <functionality>`.

## Goal

Capture a tester’s evidence in the project’s configured tracker and optionally
index that work item in each affected SDD package. This command investigates and
records a problem; it does not implement a fix.

## Workflow

1. Read project context and resolve the impacted SDD package(s) from the tested
   functionality and relevant paths. Stop if the intended behavior is too
   ambiguous to describe accurately.
2. Reproduce the behavior when practical, or trace the relevant flow. Separate
   facts from hypotheses and redact secrets, tokens, private payloads, and
   sensitive customer data.
3. If the project tracker is `None`, prepare a structured local issue note and
   ask whether the user wants an external ticket. Do not create an unconfigured
   external issue.
4. Otherwise search the configured tracker for duplicates, then create or
   update the canonical work item with environment, preconditions, reproduction,
   expected and actual behavior, impact, evidence, related package files, and
   next action.
5. Before modifying an issue index, create or switch to a temporary `chore/`
   branch from the configured base branch. Update
   `specs/<slug>/issues/index.md` only when tracker use is enabled and preserve
   existing rows.
6. Verify the tracker reference, index uniqueness, Markdown links, and diff.
   For an index-only change, run textual checks rather than unrelated code tests.

## Output

Report the canonical tracker reference (or the local-note decision), impacted
packages, reproduction/trace result, branch, validation, redactions, and
remaining uncertainty.
