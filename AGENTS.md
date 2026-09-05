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
- `.agents/workflow-notifications.md`: optional low-noise event and delivery
  contract for newly created issues and approved specs.
- `templates/`: canonical templates for specs, plans, task lists, issue indexes,
  reports, and pull requests.
- `specs/<number>-<slug>/`: one SDD package per reviewable change.
- `specs/index.md`: active and terminal package lifecycle index.
- `specs/<package>/reviews/`: review, remediation, and verification reports.
- `docs/`: project documentation when the project context declares it.
- `skills/`: optional project-specific agent skills and workflow guidance.
- `memory/`: concise durable context that does not belong in a spec or policy.
- `scripts/validate_sdd.py`: dependency-free workspace and package validation.
- `examples/`: illustrative completed artifacts, never project source of truth.
- `.github/prompts/`: optional GitHub Copilot prompt wrappers; do not assume
  they exist.

## 3. Command Routing

Run the matching workflow when the user invokes one of these commands:

| Command | Workflow |
|---|---|
| `/init-project` | `.agents/commands/init-project.md` |
| `/analyze-project` | `.agents/commands/analyze-project.md` |
| `/design-architecture <scope>` | `.agents/commands/design-architecture.md` |
| `/spec <feature>` | `.agents/commands/spec.md` |
| `/analyze-spec <spec-slug>` | `.agents/commands/analyze-spec.md` |
| `/approve-spec <spec-slug>` | `.agents/commands/approve-spec.md` |
| `/execute <spec-slug>` | `.agents/commands/execute-spec.md` |
| `/verify-spec <spec-slug>` | `.agents/commands/verify-spec.md` |
| `/fix <issue-or-description>` | `.agents/commands/fix.md` |
| `/capture-issues <functionality>` | `.agents/commands/capture-issues.md` |
| `/review` | `.agents/commands/review.md` |
| `/remediate <review-report>` | `.agents/commands/remediate.md` |
| `/verify-remediate <review-report>` | `.agents/commands/verify-remediate.md` |
| `/commit` | `.agents/commands/commit.md` |
| `/pr` | `.agents/commands/pr.md` |
| `/close-spec <spec-slug>` | `.agents/commands/close-spec.md` |

The command files are the source of truth for workflow details. Do not duplicate
their steps here.

## 4. SDD Lifecycle

1. Initialize project context once with `/init-project`.
2. Optionally document an existing project with `/analyze-project`, or design
   new architecture with `/design-architecture <scope>`.
3. Create a PR-sized package with `/spec`, check it with `/analyze-spec`, and
   record explicit human acceptance with `/approve-spec`.
4. Implement the accepted package with `/execute` and compare the result with
   its requirements using `/verify-spec` until it passes.
5. Review the uncommitted work with `/review`.
6. Address must-fix findings with `/remediate <review-report>` and verify them
   with `/verify-remediate <review-report>`.
7. Commit intentional changes with `/commit` and publish with `/pr`.
8. After the configured delivery point is reached, record completion with
   `/close-spec`.

For direct bug work, `/fix` uses the same branch, validation, documentation,
and review standards. It must not silently expand into unrelated feature work.

## 5. Required Preconditions for Changes

- Read the relevant project context, spec, plan, task, and prior reports before
  editing.
- Do not begin implementation while the relevant spec or plan has unresolved
  open questions or blockers, lacks a passing spec analysis, or has not been
  explicitly approved.
- Create or switch to a dedicated branch from the `Base branch` declared in
  project context before writing code, documentation, configuration, migrations,
  dependencies, or spec/task status updates. Never implement directly on that
  base branch unless a human explicitly authorizes it for the current task.
- Keep changes within the accepted scope. Update the spec, plan, and task when a
  discovered requirement changes that scope. A material scope, contract,
  security, data, or user-visible change invalidates prior approval: return the
  package to `Draft`, rerun analysis, and obtain approval again.
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

Package status has consistent meaning:

- `Draft`: incomplete, unresolved, or changed since its last approval.
- `Ready`: a passing spec analysis exists and human approval is recorded.
- `In Progress`: implementation has started from an approved package.
- `Implemented`: `/verify-spec` confirms the implementation satisfies the
  approved package, but the configured delivery point may not be complete.
- `Done`: the delivery point in project context has been reached and
  `/close-spec` recorded the evidence.
- `Superseded` or `Abandoned`: terminal states with a recorded reason and
  replacement reference when applicable.

## 8. Tracker, Hosting, and Notification Integrations

The issue tracker and pull-request host are configured in project context.

- When tracking is `GitHub`, use the linked issue and the project’s PR process.
- When tracking is another system, use its canonical ticket reference.
- When tracking is `None`, keep the reference as `None` rather than inventing a
  ticket.
- Do not claim optional integrations, prompt wrappers, or automation files
  exist unless they are present in the repository.
- Workflow notifications are optional. Emit only configured events after their
  canonical issue creation or spec approval succeeds, and follow
  `.agents/workflow-notifications.md` for readiness, redaction, authorization,
  duplicate suppression, and failure handling.
