# SDD Templates

These templates create one reviewable SDD package per change. Before using them,
configure the repository with `/init-project` and commit
`.agents/project-context.md` if the project’s policy permits it.

| Template | Purpose | Output location |
|---|---|---|
| [spec.md](spec.md) | Product/feature scope and acceptance criteria | `specs/<number>-<slug>/spec.md` |
| [plan.md](plan.md) | Technical approach and validation plan | `specs/<number>-<slug>/plan.md` |
| [task.md](task.md) | Execution checklist and readiness gate | `specs/<number>-<slug>/task.md` |
| [issues-index.md](issues-index.md) | Optional tracker index | `specs/<number>-<slug>/issues/index.md` |
| [pr.md](pr.md) | Pull request summary | pull request body |

Recommended flow:

1. Initialize project context.
2. Create a small feature spec with `/spec <feature>`.
3. Accept the spec, plan, and task after questions and blockers are resolved.
4. Create a dedicated branch from the configured base branch.
5. Execute, review, remediate, verify, commit, and open a PR.

Do not add project-specific frameworks, paths, commands, or tracker rules to
these canonical templates. Put them in `.agents/project-context.md` instead.
