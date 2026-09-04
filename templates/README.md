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
| [spec-analysis.md](spec-analysis.md) | Pre-approval consistency and traceability report | `specs/<package>/reviews/` |
| [spec-verification.md](spec-verification.md) | Implementation-to-spec evidence | `specs/<package>/reviews/` |
| [pre-commit-review.md](pre-commit-review.md) | Risk-focused change review | `specs/<package>/reviews/` or `specs/_reviews/` |
| [remediation.md](remediation.md) | Finding dispositions and fixes | beside the source review |
| [verification.md](verification.md) | Verification of remediated findings | beside the source review |

Recommended flow:

1. Initialize project context.
2. Create a small feature spec with `/spec <feature>`.
3. Analyze and explicitly approve the package after questions and blockers are
   resolved.
4. Confirm the package is on its dedicated branch from the configured base.
5. Execute and verify the implementation against the package.
6. Review, remediate, verify findings, commit, and open a PR.
7. Close the package after the configured delivery point is reached.

Do not add project-specific frameworks, paths, commands, or tracker rules to
these canonical templates. Put them in `.agents/project-context.md` instead.
