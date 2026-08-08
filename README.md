# AI SDD Starter

A project-agnostic starter repository for teams that want a repeatable
spec-driven development workflow with AI coding agents.

## What it provides

- A consistent lifecycle: initialize, specify, plan, execute, review, remediate,
  verify, commit, and publish.
- Reusable SDD templates that work for services, clients, data changes,
  integrations, operations, and documentation work.
- Agent workflows with scoped context loading, safety rules, and stable review
  finding IDs.
- A project-context bootstrap so commands do not assume a framework, branch,
  package manager, test command, or ticketing system.
- A tracked workspace skeleton for documentation, project skills, durable memory,
  SDD packages, and templates.

## Start a New Project

1. Copy or use this starter in the new repository.
2. Run `/init-project` and create `.agents/project-context.md` from the included
   template.
3. Confirm the base branch, validation commands, source layout, tracker choice,
   and domain/security invariants.
4. Create the first feature package with `/spec <feature>`.

Read [AGENTS.md](AGENTS.md) for the shared rules and [templates/README.md](templates/README.md)
for the template flow.

## Included Workspace Structure

- `docs/` provides neutral homes for architecture, design, data, setup, and ADRs.
- `skills/` holds optional project-specific agent skills.
- `memory/` holds concise durable project context that does not belong in a spec.
- `specs/` holds SDD packages and their review artifacts.
- `templates/` holds the canonical reusable SDD artifacts.

These folders are intentionally included so repositories created from this GitHub
template begin with the same predictable structure.
