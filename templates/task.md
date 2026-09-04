# Task Breakdown: <Feature Name>

## Status

- Status: Draft | Ready | In Progress | Implemented | Done | Superseded | Abandoned
- Owner: <name or team>
- Source spec: <relative link to spec.md>
- Source plan: <relative link to plan.md>
- Latest spec analysis: <relative report link or `Not run`>
- Latest spec verification: <relative report link or `Not run`>
- Tracking reference: <ticket URL/ID, or `None`>

## Readiness Gate

Before implementation, confirm all items below.

- [ ] Project context is present and relevant sections were read.
- [ ] Spec and plan are accepted and their `Open Questions` sections say `None`.
- [ ] Plan and task `Blockers` sections say `None`.
- [ ] The latest `/analyze-spec` report passes without blocking findings.
- [ ] Explicit human approval is recorded in `spec.md`.
- [ ] Tracking decision is recorded (`ticket` or `None`).
- [ ] Dedicated branch was created from the configured base branch.
- [ ] Existing implementation and directly related documentation were inspected.

## Implementation Tasks

Include only applicable task groups. Assign stable IDs without renumbering
existing tasks. Add source references for buildable work and exact paths when
known. Use `[supporting]` only for work that has no direct requirement, and state
why it is necessary.

### <Task Group>

- [ ] T-001 [`FR-001`, `AC-001`] <implementation task and path>
- [ ] T-002 [`FR-001`, `AC-001`] <test or validation task and path>

### Documentation and Operations

- [ ] T-003 [supporting] <documentation/configuration/rollout task and reason, or remove this group>

## Verification

- [ ] Run focused checks from project context: <command(s)>.
- [ ] Run broader checks when the risk/changed boundary requires them: <command(s) or `Not applicable`>.
- [ ] Perform required manual verification: <scenario(s) or `Not applicable`>.
- [ ] Record skipped checks and the reason.

### Acceptance Evidence

| Source ref | Evidence | Result |
|---|---|---|
| AC-001 | <test, command, screenshot, or manual observation> | <Pass / Fail / Not run> |

## Review Preparation

- [ ] Review the diff for scope, unrelated changes, secrets, and local-only files.
- [ ] Confirm tests and documentation match the actual behavior.
- [ ] Run `/verify-spec <spec-slug>` and resolve or schedule every reported gap.
- [ ] Prepare the tracker/PR summary required by project context.

## Decisions

| Date | Decision | Reason |
|---|---|---|
| <YYYY-MM-DD> | <decision> | <reason> |

## Blockers

- None

## Completion Gate

- `Implemented` requires a passing `/verify-spec` report.
- `Done` requires `/close-spec` and evidence that the delivery completion point
  configured in project context was reached.
