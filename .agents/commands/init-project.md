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
2. Classify each observation as starter scaffolding or project-owned evidence
   before using it to answer survey questions. Follow the evidence rules and
   fresh-template baseline below.
3. Run the adaptive survey below. Ask only for facts that remain unknown,
   ambiguous, or conflicting after the repository inspection. Ask one question
   at a time and wait for the user's answer before continuing.
4. Ensure the starter workspace exists. Create any missing `docs/`, `skills/`,
   `memory/`, `specs/`, and `templates/` directories, preserving existing
   content. Use the starter README files and placeholders when available; do
   not overwrite project documentation or replace a project’s own templates.
   Create `specs/_reviews/` when review reports will be stored locally.
5. Create `.agents/project-context.md` from
   `.agents/project-context.template.md` on a dedicated setup/docs branch unless
   the human explicitly authorizes bootstrap work on the current branch.
6. Replace placeholders with observed or confirmed facts. Use `Not established`,
   `Not available`, or `Not applicable` where a decision has not been made; do
   not guess commands or paths.
7. If optional docs or prompt wrappers are referenced, either create them as
   part of the setup or mark them absent in project context. Do not design or
   author an architecture document during initialization unless the user
   explicitly adds that work to the scope.
8. Inspect the resulting diff and validate Markdown paths and commands against
   the repository. Run `python3 scripts/validate_sdd.py` when that script is
   present. Do not run unavailable project commands merely because the template
   lists them.

## Evidence Classification

Treat unchanged starter content as a starter scaffold, not as facts about the
project that was created from it. Scaffold content can prove that the SDD
workflow is installed, but it must not be used as project evidence for the
project name, purpose, users, lifecycle state, ownership, application stack,
source layout, validation commands, base branch, tracker, or delivery process.

Common scaffold signals include:

- `.agents/project-context.md` is absent while
  `.agents/project-context.template.md` is present;
- the root README still describes an SDD starter or reusable template rather
  than the application being initialized;
- placeholder values such as `[Project Name]` remain;
- canonical workflow content is present in `.agents/commands/`, `templates/`,
  `examples/`, `specs/README.md`, `TEMPLATE_VERSION`, or `CHANGELOG.md`; and
- no project-owned application manifest, source code, or non-placeholder
  product documentation provides a different identity.

Use multiple signals together. A single missing manifest does not prove that a
repository is greenfield, and the current branch name does not establish the
project's intended base branch.

Project-owned evidence includes application manifests and source code,
deliberately customized product documentation, existing project configuration,
and repository metadata that clearly names the target project. Prefer evidence
in this order: facts confirmed by the user, an existing project context,
project-owned code or documentation, repository metadata, then unresolved.
Starter scaffold content is never a fallback source for project identity.

When an uninitialized starter scaffold is detected, use the fresh-template
baseline:

1. Briefly tell the user that starter scaffolding was detected and will not be
   treated as project identity. Mention separately whether application evidence
   was or was not found.
2. Ask all five project-identity questions in order, one per turn, even when the
   starter README appears to answer them.
3. After identity is established, resume adaptive routing and skip only facts
   supported by project-owned evidence or confirmed by the user.

If the user says they are maintaining the starter template itself, record that
as an explicit answer and continue adaptively. Do not infer template maintenance
merely because the repository contains the canonical scaffold.

## Adaptive Survey

### Survey Rules

- Treat the questions below as a conditional question bank, not a mandatory
  questionnaire. Stop when every project-context field is observed, confirmed,
  `Not established`, `Not available`, or `Not applicable`.
- Ask one concise question per turn. Do not combine unrelated topics in a
  single question.
- Do not ask the user to repeat a fact that repository evidence establishes
  confidently. Starter scaffold content does not meet this standard. When
  evidence is ambiguous or conflicting, identify its source, present the
  observed value, and ask the user to confirm it.
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
question and should be skipped when its answer is already established. For an
uninitialized starter scaffold, the five project-identity questions are a
required baseline and must not be skipped based on starter content.

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
9. Workflow notifications
   - Should workflow notifications be disabled, or configured for newly created
     issues, approved specs, or both?
   - If notifications are disabled, skip the remaining notification questions.
   - Which provider, delivery method, and non-secret destination should be used?
   - What connected-account or secret reference will identify authentication
     without storing the credential value?
   - Should delivery require a preview or use explicitly authorized automatic
     sending?
   - Who owns setup, what non-secret prerequisites remain, and where is the
     setup guide?
   - How will connectivity and posting permission be verified, and should a
     notification failure warn or leave the command incomplete?
10. User-interface guidance, when applicable
   - Which UI technology and design system or guidance should be used?
   - What accessibility and responsive-layout expectations apply?

## Initialization Scenarios

### Fresh Template-Derived Repository

Given no `.agents/project-context.md`, an unchanged starter README and workflow
files, and no project-owned application evidence:

- Do not call the project `AI SDD Starter` or classify it as an existing
  application.
- Explain that the starter scaffold was detected and is being treated as
  scaffolding.
- The first survey question must be: `What name should be used for this
  project?`
- Continue through purpose, users or stakeholders, project state, and boundaries
  one question at a time before routing to ownership and workflow topics.

### Existing or Mixed Application with Starter Files

When project-owned code or customized product documentation exists alongside
starter files, use that evidence to describe what was observed, but still ask
for confirmation wherever identity or lifecycle state is ambiguous. Never let
an unchanged starter README override application evidence.

### Starter Template Maintenance

When the user explicitly confirms that the repository is the reusable starter
itself, its template identity becomes user-confirmed project context. Continue
the remaining survey without assuming that consuming-project runtime or source
layout conventions apply to the starter.

## Completion Criteria

- The project context has `Status: Ready` only when a base branch, source layout,
  validation approach, tracker choice, delivery completion point, applicable
  approval/governance rules, and applicable domain/security rules are recorded.
- The required workspace folders exist or their project-approved equivalents are
  recorded in project context.
- Future `/spec`, `/execute`, `/fix`, `/commit`, and `/pr` commands can use the
  context without assuming a framework, package manager, tracker, or branch.
- Workflow notifications may be `Disabled` or `Planned` without blocking project
  initialization. When they are `Planned`, the context must identify the known
  setup owner and missing prerequisites so later commands can explain why
  delivery is unavailable.
