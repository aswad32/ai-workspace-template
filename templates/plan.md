# Technical Plan: <Feature Name>

## Status

- Status: Draft | Ready | In Progress | Implemented | Done | Superseded | Abandoned
- Owner: <name or team>
- Created: <YYYY-MM-DD>
- Last updated: <YYYY-MM-DD>
- Source spec: <relative link to spec.md>
- Package approval: <link to approved spec metadata or `Pending`>
- Tracking reference: <ticket URL/ID, or `None`>
- Project context: `.agents/project-context.md`

## Summary and Scope

Summarize the approach and restate only the implementation boundary relevant to
this plan.

In scope:

- <item>

Out of scope:

- <item>

## Architecture and Change Map

Describe the affected boundaries and the data/control flow only when they change.

| Area | Existing path or owner | Planned change | Source refs | Risk |
|---|---|---|---|---|
| <area> | <path/team or `New`> | <Add / Update / Delete> | <FR/QR/AC IDs> | <low/medium/high> |

## Alternatives and Decisions

Record alternatives only when a decision affects architecture, compatibility,
security, operations, or future cost.

| Decision | Selected approach | Alternatives rejected | Reason / ADR |
|---|---|---|---|
| <decision> | <approach> | <alternatives or `None`> | <reason or ADR link> |

## Contracts and Data

- API/service contract: <change or `Not applicable`>
- Data/storage schema and compatibility: <change or `Not applicable`>
- Migration/backfill plan: <command and order, or `Not applicable`>
- External integration contract: <change or `Not applicable`>
- Backward compatibility/versioning: <strategy or `Not applicable`>

## Requirement Traceability

Every buildable requirement and acceptance criterion must have a planned owner
and validation method before approval.

| Source ref | Planned component/path | Validation approach |
|---|---|---|
| FR-001 / AC-001 | <component or path> | <automated or manual evidence> |

## Implementation Steps

1. P-001 (`FR-001`, `AC-001`): <small, reviewable step>
2. P-002: <small supporting step and reason>

## Testing and Verification

- Focused validation: <command(s) from project context>
- Broader validation required: <command(s), or `No — reason`>
- Manual verification: <scenario(s), or `Not applicable`>
- Security/privacy validation: <check, or `Not applicable`>
- Spec-conformance validation: `/verify-spec <spec-slug>`

## Documentation and Operations

- Documentation updates: <paths from project context, or `None`>
- Runtime/configuration changes: <details or `None`>
- Rollout and rollback: <details or `Not applicable`>

## Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| <risk> | <impact> | <mitigation> |

## Blockers

- None

## Open Questions

- None

Implementation must not start while blockers or open questions remain unresolved.

Material changes to this plan after approval invalidate package approval unless
they are non-behavioral clarifications that do not alter scope, contracts, data,
security, operations, validation, or user-visible behavior.
