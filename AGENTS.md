# AGENTS.md

This file is the default entry point for AI coding agents working on
`[Project Name]`. It defines a reusable spec-driven development (SDD) workflow;
project-specific facts belong in `.agents/project-context.md`.

## 0. Start Here

Before planning, editing, testing, reviewing, committing, or opening a pull
request, read the relevant sections of `.agents/project-context.md`.

- If it does not exist, run `/init-project` first. Do not infer the stack,
  source layout, base branch, tracker, validation commands, or domain rules.
- The checked-in `.agents/project-context.template.md` is the starting point for
  that setup document. Keep secrets, tokens, and customer data out of both
  files.

## 1. Context Budget Rule

Load context progressively. Start with the command input, changed-path list,
active task group, finding IDs, report summaries, or branch purpose. Read only
what is needed for the current decision. Broaden the read only when focused
context is insufficient or a concrete safety risk requires it.

## 2. Repository Shape

- `.agents/commands/`: reusable agent workflows.
- `.agents/project-context.md`: project-specific configuration and invariants
  (created during setup; not a template source of truth).
- `templates/`: canonical templates for specs, plans, task lists, issue indexes,
  and pull requests.
- `specs/<number>-<slug>/`: one SDD package per reviewable change.
- `specs/<package>/reviews/`: review, remediation, and verification reports.
- `docs/`: project documentation when the project context declares it.
- `skills/`: optional project-specific agent skills and workflow guidance.
- `memory/`: concise durable context that does not belong in a spec or policy.
- `.github/prompts/`: optional GitHub Copilot prompt wrappers; do not assume
  they exist.

## 3. Command Routing

Run the matching workflow when the user invokes one of these commands:

| Command | Workflow |
|---|---|
| `/init-project` | `.agents/commands/init-project.md` |
| `/spec <feature>` | `.agents/commands/spec.md` |
| `/execute <spec-slug>` | `.agents/commands/execute-spec.md` |
| `/fix <issue-or-description>` | `.agents/commands/fix.md` |
| `/capture-issues <functionality>` | `.agents/commands/capture-issues.md` |
| `/review` | `.agents/commands/review.md` |
| `/remediate` | `.agents/commands/remediate.md` |
| `/verify-remediate` | `.agents/commands/verify-remediate.md` |
| `/commit` | `.agents/commands/commit.md` |
| `/pr` | `.agents/commands/pr.md` |

The command files are the source of truth for workflow details. Do not duplicate
their steps here.

## 4. SDD Lifecycle

1. Initialize project context once with `/init-project`.
2. Create an accepted, PR-sized package with `/spec`.
3. Implement the accepted package with `/execute`.
4. Review the uncommitted work with `/review`.
5. Address must-fix findings with `/remediate` and verify them with
   `/verify-remediate`.
6. Commit intentional changes with `/commit` and publish with `/pr`.

For direct bug work, `/fix` uses the same branch, validation, documentation,
and review standards. It must not silently expand into unrelated feature work.

## 5. Required Preconditions for Changes

- Read the relevant project context, spec, plan, task, and prior reports before
  editing.
- Do not begin implementation while the relevant spec or plan has unresolved
  open questions or blockers.
- Create or switch to a dedicated branch from the `Base branch` declared in
  project context before writing code, documentation, configuration, migrations,
  dependencies, or spec/task status updates. Never implement directly on that
  base branch unless a human explicitly authorizes it for the current task.
- Keep changes within the accepted scope. Update the spec, plan, and task when a
  discovered requirement changes that scope.
- Update affected documentation and targeted tests with behavior, API, data,
  setup, or user-visible changes.

## 6. Universal Safety Rules

- Preserve unrelated local changes and do not use destructive Git commands
  unless a human explicitly requests them.
- Keep secrets, credentials, private payloads, and `.env` files out of source,
  tests, reports, commits, and tracker tickets.
- Enforce authorization and validate important inputs on the server or trusted
  boundary; client-side checks are not sufficient.
- Follow the project context’s domain invariants for data, privacy, audit,
  compliance, money, retention, and external integrations.
- Avoid unrelated refactors, formatting churn, dependency upgrades, generated
  files, and automatic audit fixes.

## 7. Verification and Documentation

Use the commands and documentation map declared in project context. Start with
focused validation and broaden only when a changed shared contract, shared
component, build/deployment setup, schema, security boundary, or dependency
requires it. For documentation-only changes, inspect the rendered or textual
diff and state why executable validation was not run.

## 8. Tracker and Hosting Integrations

The issue tracker and pull-request host are configured in project context.

- When tracking is `GitHub`, use the linked issue and the project’s PR process.
- When tracking is another system, use its canonical ticket reference.
- When tracking is `None`, keep the reference as `None` rather than inventing a
  ticket.
- Do not claim optional integrations, prompt wrappers, or automation files
  exist unless they are present in the repository.
