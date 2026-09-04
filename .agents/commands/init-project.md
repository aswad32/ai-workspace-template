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
2. Run the adaptive survey below. Ask only for facts that remain unknown,
   ambiguous, or conflicting after the repository inspection. Ask one question
   at a time and wait for the user's answer before continuing.
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
   part of the setup or mark them absent in project context. Do not design or
   author an architecture document during initialization unless the user
   explicitly adds that work to the scope.
7. Inspect the resulting diff and validate Markdown paths and commands against
   the repository. Run `python3 scripts/validate_sdd.py` when that script is
   present. Do not run unavailable project commands merely because the template
   lists them.

## Adaptive Survey

### Survey Rules

- Treat the questions below as a conditional question bank, not a mandatory
  questionnaire. Stop when every project-context field is observed, confirmed,
  `Not established`, `Not available`, or `Not applicable`.
- Ask one concise question per turn. Do not combine unrelated topics in a
  single question.
- Do not ask the user to repeat a fact that repository evidence establishes
  confidently. When evidence is ambiguous or conflicting, present the observed
  value and ask the user to confirm it.
- Adapt to the project state:
  - For a greenfield project, collect intended decisions and record undecided
    items as `Not established`; do not invent commands, paths, or conventions.
  - For an existing project, prefer current repository evidence and ask about
    undocumented conventions, constraints, or intended changes.
  - For a mixed, migration, or modernization project, distinguish the current
    state from the intended state and record both when the difference affects
    later work.
- Accept `unknown`, `not decided`, and `not applicable` as valid answers. Do not
  block initialization on optional decisions.
- Never request secrets, tokens, credentials, private payloads, or customer
  data. Record only the integration name and its non-secret constraints.
- Track whether each answer was observed from the repository, confirmed by the
  user, or left unresolved. Summarize the resulting context and ask the user to
  confirm or correct it before creating `.agents/project-context.md`.

### Question Routing

Ask the applicable questions in this order. Each example prompt is a separate
question and should be skipped when its answer is already established.

1. Project identity and purpose
   - What name should be used for this project?
   - What problem does the project solve or outcome does it provide?
   - Who are its primary users or stakeholders?
   - Is this greenfield, an existing application, or a mixture such as a
     migration or modernization?
   - Are there important project boundaries or explicit non-goals?
2. Ownership and decision-making
   - Who owns or maintains the project?
   - Are there teams or people who must approve particular kinds of changes?
   - Where are binding project principles or engineering standards recorded?
   - How are exceptions and consequential architecture decisions approved?
3. Repository and development workflow
   - Which branch is the base branch for new work?
   - What branch-naming convention should later workflows follow?
   - Is this a single repository, a monorepo, or one part of a multi-repository
     system?
   - If the source layout, runtime, framework, or dependency manager is unclear,
     what should be treated as authoritative?
4. Validation expectations
   - Which formatting, linting, type-checking, test, build, migration,
     generation, and security-audit checks are required or available?
   - Are any checks unavailable locally, unusually expensive, destructive, or
     dependent on external services?
   - Are any manual checks required before work is considered complete?
5. Tracking and delivery
   - Which work tracker should be used, or is tracking intentionally absent?
   - Where are pull requests opened, and which branch do they target?
   - Which checks or approvals are required before merging?
   - Should pull requests normally start as drafts?
   - Which environments exist, and are there deployment or release constraints
     that later workflows must respect?
   - What observable event means a change is delivered: merge, deployment,
     release, or another project-specific point?
6. Documentation and architecture
   - Which existing documents are authoritative for architecture, setup, the
     data model, design guidance, and technical decisions?
   - Where should missing documentation live when it is created later?
   - Does an architecture document already exist? If it does, record its path;
     otherwise record `Not established` unless the user explicitly requests a
     separate architecture-document task.
   - What changes require documentation updates?
7. Domain, data, and security invariants
   - What authorization rules must always hold?
   - What data is sensitive, and what handling restrictions apply?
   - What data-integrity rules must never be violated?
   - Are there money, privacy, compliance, audit, or retention requirements?
8. External integrations
   - Which external systems or services are required?
   - What non-secret limitations, environments, ownership, or failure-handling
     constraints apply to each integration?
9. User-interface guidance, when applicable
   - Which UI technology and design system or guidance should be used?
   - What accessibility and responsive-layout expectations apply?

## Completion Criteria

- The project context has `Status: Ready` only when a base branch, source layout,
  validation approach, tracker choice, delivery completion point, applicable
  approval/governance rules, and applicable domain/security rules are recorded.
- The required workspace folders exist or their project-approved equivalents are
  recorded in project context.
- Future `/spec`, `/execute`, `/fix`, `/commit`, and `/pr` commands can use the
  context without assuming a framework, package manager, tracker, or branch.
