# AI SDD Starter

A project-agnostic starter repository for teams that want a repeatable
spec-driven development workflow with AI coding agents.

Released under the [MIT License](LICENSE).

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

## Quick Start

1. Select **Use this template** on GitHub, or copy this repository into a new
   project repository.
2. Start a coding-agent session and ask it to follow
   `.agents/commands/init-project.md`. Agents that support repository command
   routing can use `/init-project` directly.
3. Create `.agents/project-context.md` from the included template. Record the
   base branch, validation commands, source layout, tracker choice, and
   applicable domain/security invariants.
4. Ask the agent to follow `.agents/commands/spec.md` for the first feature.

### Agent Compatibility

The files in `.agents/commands/` are Markdown workflow instructions, not a
universal command-plugin format. If your coding-agent client does not register
repository slash commands, explicitly tell the agent which command file to
follow. Agents that read `AGENTS.md` can use it as the repository entry point.

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

## Contributing and Security

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution expectations,
[SECURITY.md](SECURITY.md) for private vulnerability reporting, and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation standards. GitHub
Actions checks local Markdown links on pull requests and updates to the main
development branches.
