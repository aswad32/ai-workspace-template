# AI SDD Starter

A project-agnostic starter repository for teams that want a repeatable
spec-driven development workflow with AI coding agents.

Released under the [MIT License](LICENSE).

## What it provides

- A consistent lifecycle: initialize, specify, analyze, approve, execute, verify,
  review, remediate, publish, and close.
- Reusable SDD templates that work for services, clients, data changes,
  integrations, operations, and documentation work.
- Agent workflows with scoped context loading, explicit human approval,
  requirement traceability, spec-conformance checks, safety rules, and stable
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
   routing can use `/init-project` directly. On a fresh template-derived
   repository, initialization treats unchanged starter files as scaffolding and
   begins by asking for the new project's identity.
3. Review the generated `.agents/project-context.md`, correct any inferred
   facts, and commit it when the project's policy permits shared agent context.
4. Ask the agent to follow `.agents/commands/spec.md` for the first feature,
   then analyze and approve the package before implementation.

### Agent Compatibility

The files in `.agents/commands/` are Markdown workflow instructions, not a
universal command-plugin format. If your coding-agent client does not register
repository slash commands, explicitly tell the agent which command file to
follow. Agents that read `AGENTS.md` can use it as the repository entry point.

Read [AGENTS.md](AGENTS.md) for the shared rules and [templates/README.md](templates/README.md)
for the template flow.

### Core Lifecycle

```text
init → spec → analyze → approve → execute ⇄ verify-spec
                                      ↓
                      review → remediate → verify-remediate
                                      ↓
                              commit → PR → close-spec
```

`/analyze-project` can document an existing system before feature work.
`/design-architecture` is a separate, explicit workflow for architecture design;
`/init-project` does not silently create or redesign architecture.

Optional workflow notifications follow the
[low-noise notification contract](.agents/workflow-notifications.md). The
starter announces only newly created issues and specs that have completed
analysis, received explicit human approval, and become ready to implement;
draft creation and analysis remain silent.

### When a Full Package Is Useful

Use a spec package when agreement matters: user-visible behavior, shared
contracts, data or security boundaries, migrations, integrations, operational
risk, or work spanning several coordinated steps. A tiny factual documentation
correction or a confirmed narrow defect can use the direct documentation or
`/fix` path while still following project context, validation, review, and branch
rules. If a supposed fix needs a new product decision, treat it as a new spec.

## Included Workspace Structure

- `docs/` provides neutral homes for architecture, design, data, setup, and ADRs.
- `skills/` holds optional project-specific agent skills.
- `memory/` holds concise durable project context that does not belong in a spec.
- `specs/` holds SDD packages and their review artifacts.
- `templates/` holds the canonical reusable SDD artifacts.
- `examples/` demonstrates a completed package without prescribing a stack.

These folders are intentionally included so repositories created from this GitHub
template begin with the same predictable structure.

## Template Revision and Updates

The current workflow revision is recorded in [TEMPLATE_VERSION](TEMPLATE_VERSION)
and changes are summarized in [CHANGELOG.md](CHANGELOG.md). Repositories created
from this template are independent copies; updates are not applied automatically.
Review the changelog, compare command and template files, and adopt migrations on
a dedicated branch without overwriting project-specific context.

## Contributing and Security

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution expectations,
[SECURITY.md](SECURITY.md) for private vulnerability reporting, and
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for participation standards. GitHub
Actions checks local Markdown links on pull requests and updates to the main
development branches.
