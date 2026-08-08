# Contributing

Thanks for improving the AI SDD Starter.

## Before You Start

- Open an issue or discussion for changes that alter the workflow, templates,
  or compatibility expectations.
- Keep pull requests small and focused. Avoid project-specific frameworks,
  commands, providers, and organizational policy in the canonical templates.
- Do not include credentials, customer data, private prompts, or local agent
  state in commits or issues.

## Development Approach

1. Branch from the repository's current integration branch.
2. Update the relevant command guide, template, and README documentation when
   a workflow contract changes.
3. Check Markdown links and review the diff for broken formatting, stale paths,
   and unintended scope.
4. Explain the motivation, user impact, and validation in the pull request.

## Proposing a New Workflow

Describe the trigger, required context, safe writes, stop conditions, and
expected output. The workflow must remain project-agnostic and must not require
unavailable tools or external integrations.
