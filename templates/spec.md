# Feature Spec: <Feature Name>

## Status

- Status: Draft | Ready | In Progress | Implemented | Done | Superseded | Abandoned
- Change type: Feature | Refactor | Migration | Operations | Documentation | Research | Other
- Owner: <name or team>
- Created: <YYYY-MM-DD>
- Last updated: <YYYY-MM-DD>
- Approval: Pending | Approved | Invalidated
- Approved by: <name, team, or `Not approved`>
- Approved on: <YYYY-MM-DD or `Not approved`>
- Approval notification: Not evaluated | Not configured | Disabled | Not subscribed | Pending setup: <missing prerequisites> | Not sent: <date and reason> | Sent: <date and non-secret reference> | Failed: <date and reason> | Delivery uncertain: <date and reason>
- Latest spec analysis: <relative report link or `Not run`>
- Tracking reference: <ticket URL/ID, or `None`>
- Project context: `.agents/project-context.md`
- Supersedes: <spec link(s) or `None`>
- Superseded by: <spec link or `None`>
- Delivery evidence: <PR, release, deployment, or `Not delivered`>

## Summary

Describe the user problem, intended outcome, and why it matters.

## Goals

- <goal>

## Non-Goals

- <explicitly out-of-scope work>

## Users and Use Cases

Use priority only when it helps define an independently deliverable slice.

| ID | Priority | User or stakeholder | Need | Independent success outcome |
|---|---|---|---|---|
| US-001 | P1 | <persona> | <need> | <observable, independently testable outcome> |

## Current Behavior

Describe relevant current behavior, constraints, and existing paths. Use `New
capability` when there is no existing behavior.

## Proposed Behavior

Describe the user-visible or system outcome after the change.

## Functional Requirements

- FR-001: <testable requirement>

## Quality Attributes

Add only applicable, measurable constraints. Consider performance, scale,
reliability, availability, observability, accessibility, localization,
compatibility, recovery, and maintainability.

- QR-001: <measurable quality requirement or `Not applicable`>

## Applicable Change Areas

Mark each area `Applicable` or `Not applicable`, then add only the detail needed
for applicable areas.

| Area | Status | Requirements / contract |
|---|---|---|
| API or service | <Applicable / Not applicable> | <endpoint, contract, validation, authorization> |
| Data or storage | <Applicable / Not applicable> | <model, migration, compatibility, retention> |
| UI or client | <Applicable / Not applicable> | <states, accessibility, responsive behavior> |
| Background processing | <Applicable / Not applicable> | <queue, schedule, retries, observability> |
| External integration | <Applicable / Not applicable> | <provider, failure handling, data exchanged> |
| Setup or operations | <Applicable / Not applicable> | <configuration, deployment, rollout> |
| Shared library or contract | <Applicable / Not applicable> | <consumer impact, versioning, compatibility> |
| Repository or infrastructure | <Applicable / Not applicable> | <CI/CD, build, hosting, cross-repository impact> |

## Security, Privacy, and Domain Rules

- Authorization impact: <rule or `None`>
- Input validation: <rule or `None`>
- Sensitive-data handling: <rule or `None`>
- Logging/audit restrictions: <rule or `None`>
- Project-context invariants affected: <list or `None`>

## Acceptance Criteria

Each criterion must reference the requirement or user story it proves.

- AC-001 (`FR-001`, `US-001`): Given <context>, when <action>, then <verifiable outcome>.

## Success Measures

Record observable product or operational outcomes separately from build
acceptance. Use `Not applicable` when delivery itself is the only measure.

- SC-001: <measurable outcome, owner, and observation window>

## Edge Cases

- <edge case and expected behavior>

## Assumptions

- AS-001: <assumption, default, or `None`>

## Dependencies and Rollout

- Dependencies: <prerequisite, integration, or `None`>
- Compatibility/consumer impact: <breaking or non-breaking impact, or `None`>
- Rollout/rollback considerations: <details or `None`>

## Open Questions

- None

Implementation must not start while this section contains unresolved questions.

## Approval Gate

The package may become `Ready` only after `/analyze-spec` passes and
`/approve-spec` records explicit human approval. Material changes to scope,
requirements, acceptance criteria, contracts, data, security, or user-visible
behavior reset `Approval` to `Invalidated` and `Status` to `Draft`.
