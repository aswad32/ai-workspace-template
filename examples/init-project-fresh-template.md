# Fresh Template Initialization Scenario

This regression scenario defines the expected `/init-project` behavior for a
repository created from the reusable starter.

## Given

- `.agents/project-context.md` does not exist.
- The root README and canonical SDD files still describe the starter template.
- Placeholder values such as `[Project Name]` may remain.
- No project-owned application code, manifest, or customized product
  documentation establishes the new project's identity.

## Expected Opening

The agent briefly explains that it detected starter scaffolding and will not use
that boilerplate as the new project's identity. It may also report that no
application runtime or manifest was found, but that observation must not cause
the repository to be classified as an existing application.

## Expected Survey Order

The first question is:

> What name should be used for this project?

After the user answers, ask these separately and in order:

1. What problem does the project solve or outcome does it provide?
2. Who are its primary users or stakeholders?
3. Is this greenfield, an existing application, or a mixture such as a
   migration or modernization?
4. Are there important project boundaries or explicit non-goals?

Only then should the adaptive survey move to ownership, repository workflow,
validation, delivery, documentation, domain constraints, integrations, and UI
guidance. Later questions may be skipped when project-owned evidence or a user
answer establishes them confidently.

## Brownfield Variation

If application code or customized product documentation already exists, use it
as evidence and ask only about gaps or conflicts. An unchanged starter README
must never override that project-owned evidence.
