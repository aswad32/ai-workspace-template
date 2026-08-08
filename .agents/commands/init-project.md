# Initialize Project Command

Use this workflow when the user says `/init-project` or asks to configure this
SDD starter for a particular project.

## Goal

Establish the project facts that every later SDD workflow needs, without
inventing technical decisions or exposing sensitive information.

## Workflow

1. Inspect the repository at a high level: current branch, project manifests,
   source folders, existing documentation, test/build scripts, and tracker or
   hosting metadata when present.
2. Ask for only the facts that cannot be safely inferred: project purpose, base
   branch, tracker choice, ownership, domain invariants, and required
   integrations.
3. Ensure the starter workspace exists. Create any missing `docs/`, `skills/`,
   `memory/`, `specs/`, and `templates/` directories, preserving existing
   content. Use the starter README files and placeholders when available; do
   not overwrite project documentation or replace a project’s own templates.
   Create `specs/_reviews/` when review reports will be stored locally.
4. Create `.agents/project-context.md` from
   `.agents/project-context.template.md` on a dedicated setup/docs branch unless
   the human explicitly authorizes bootstrap work on the current branch.
5. Replace placeholders with observed or confirmed facts. Use `Not established`,
   `Not available`, or `Not applicable` where a decision has not been made; do
   not guess commands or paths.
6. If optional docs or prompt wrappers are referenced, either create them as
   part of the setup or mark them absent in project context.
7. Inspect the resulting diff and validate Markdown paths and commands against
   the repository. Do not run unavailable commands merely because the template
   lists them.

## Completion Criteria

- The project context has `Status: Ready` only when a base branch, source layout,
  validation approach, tracker choice, and applicable domain/security rules are
  recorded.
- The required workspace folders exist or their project-approved equivalents are
  recorded in project context.
- Future `/spec`, `/execute`, `/fix`, `/commit`, and `/pr` commands can use the
  context without assuming a framework, package manager, tracker, or branch.
