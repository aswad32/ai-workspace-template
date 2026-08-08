# Feature Spec: <Feature Name>

## Status

- Status: Draft | Ready | In Progress | Done
- Owner: <name or team>
- Created: <YYYY-MM-DD>
- Tracking reference: <ticket URL/ID, or `None`>
- Project context: `.agents/project-context.md`

## Summary

Describe the user problem, intended outcome, and why it matters.

## Goals

- <goal>

## Non-Goals

- <explicitly out-of-scope work>

## Users and Use Cases

| User | Need | Success outcome |
|---|---|---|
| <persona> | <need> | <observable outcome> |

## Current Behavior

Describe relevant current behavior, constraints, and existing paths. Use `New
capability` when there is no existing behavior.

## Proposed Behavior

Describe the user-visible or system outcome after the change.

## Functional Requirements

- FR-1: <requirement>

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

## Security, Privacy, and Domain Rules

- Authorization impact: <rule or `None`>
- Input validation: <rule or `None`>
- Sensitive-data handling: <rule or `None`>
- Logging/audit restrictions: <rule or `None`>
- Project-context invariants affected: <list or `None`>

## Acceptance Criteria

- AC-1: Given <context>, when <action>, then <verifiable outcome>.

## Edge Cases

- <edge case and expected behavior>

## Dependencies and Rollout

- Dependencies: <prerequisite, integration, or `None`>
- Rollout/rollback considerations: <details or `None`>

## Open Questions

- None

Implementation must not start while this section contains unresolved questions.
