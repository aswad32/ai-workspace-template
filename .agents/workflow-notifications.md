# Workflow Notification Contract

This contract defines optional, low-noise announcements produced by SDD
workflows. Commands must read the `Workflow Notifications` section of project
context before attempting delivery. Notification delivery never replaces the
canonical spec, issue, approval record, or tracker reference.

## Supported Events

| Event | Emitted when | Do not emit when |
|---|---|---|
| `issue.created` | `/capture-issues` verifies a newly created canonical tracker item or accepted local issue note | A duplicate is found, an existing issue is updated, or the issue has not been persisted |
| `spec.approved` | `/approve-spec` records explicit human approval and all package artifacts become `Ready` | The spec is drafted, edited, analyzed, blocked, rejected, invalidated, or already announced for the current approval cycle |

No other event is enabled by this template. Projects may extend the event set in
their own context, but commands must not invent or send additional events.

## Configuration Readiness

- `Disabled`: Do not prepare or send notifications unless the user asks for a
  one-time message.
- `Planned`: The project wants notifications, but one or more prerequisites are
  missing or unverified. Complete the canonical workflow action, do not attempt
  delivery, and report the exact missing setup items with the prepared message.
- `Ready`: Delivery may be attempted only for an enabled event after all
  requirements below are satisfied.

If the `Workflow Notifications` section is absent from an older project context,
treat notifications as `Not configured`: do not attempt delivery, and report a
single adoption action to rerun `/init-project` or add the new context section.

`Ready` requires a provider, delivery method, destination, non-secret credential
or connected-account reference, enabled-event list, send policy, setup owner,
documented setup requirements, failure policy, and a successful connection or
delivery verification. `Automatic` sending additionally requires a recorded
human authorization and its scope. A repository setting alone does not grant a
tool access to an external service.

Never store webhook URLs, tokens, passwords, connection secrets, or private
provider payloads in project context, specs, issue indexes, reports, or logs.

## Delivery Method Requirements

Use these as the minimum setup checklist and add provider-specific requirements
to project context or its linked setup guide.

### Agent Connector

- The provider connection is installed, authenticated, and available to the
  agent running the command.
- The destination resolves unambiguously and the connected identity can post.
- A non-sensitive connection name is recorded and access has been verified.

### Webhook

- The webhook is provisioned in the provider and its value is stored in an
  approved secret store or runtime environment.
- Project context records only the secret-variable or secret-manager reference.
- Destination mapping, network access, payload format, and a safe delivery test
  have been verified.

### Repository Automation

- The automation or workflow exists and subscribes only to configured events.
- Required secret names, permissions, destination mapping, and ownership are
  documented without exposing secret values.
- The workflow has been enabled and verified with a safe test event.

## Delivery Procedure

1. Finish and verify the canonical issue creation or spec approval first.
2. Confirm that the event is enabled and has not already been delivered for the
   same canonical issue or current spec approval cycle.
3. Evaluate readiness. For `Planned` or incomplete configuration, list every
   missing requirement and provide a copy-ready message without attempting to
   send it.
4. Build the minimum payload defined below. Redact secrets, sensitive evidence,
   private customer data, and content restricted by project context.
5. For `Preview first`, show the final destination and message and obtain the
   user's approval before sending. For `Automatic`, verify that recorded human
   authorization covers the current event and destination.
6. Deliver through the configured method and capture a non-secret provider
   reference or verifiable result when available.
7. Report `Sent`, `Not sent`, `Not subscribed`, `Disabled`, `Not configured`,
   `Pending setup`, `Failed`, or `Delivery uncertain` separately from the
   canonical workflow result.

A notification failure must not erase, duplicate, or misrepresent a successfully
created issue or approved spec. If delivery is required by project policy, mark
the command incomplete and provide a retry action, but keep the canonical issue
or approval intact. Never retry an uncertain delivery automatically.

## Setup Diagnostic Output

For `Not configured`, `Planned`, or incomplete setup, report one compact block
containing:

- the event that became eligible;
- the current readiness state;
- the configured provider, method, and destination when known;
- every missing or unverified prerequisite;
- the setup owner and setup-guide reference when known;
- a safe next action; and
- the copy-ready notification message as a fallback.

Describe credential gaps using only the expected connection or secret-reference
name. Never ask the user to paste a token or webhook value into chat or a tracked
file. Do not claim setup is complete merely because a provider name or
destination was supplied.

## Minimum Payloads

### Issue Created

- Event label: `Issue created`
- Canonical issue title and tracker URL/ID or repository-relative local note
- Sanitized impact summary
- Affected SDD package(s), when known
- Suggested next action

Do not include raw reproduction payloads, logs, screenshots, or customer data by
default. A local filesystem URL must not be sent; use a repository-accessible
reference or explain that the note is local-only.

### Spec Approved

- Event label: `Spec approved — ready to implement`
- Spec ID/title and repository-accessible link or relative path
- Concise scope summary
- Approver and approval date
- Tracker reference, when configured
- Suggested next action: `/execute <spec-slug>`

The message must say `Ready to implement`, not imply that implementation has
started or that the change has been delivered.

## Duplicate Suppression

- `issue.created` is emitted only during the run that creates and verifies a new
  canonical issue. Finding or updating an existing item suppresses the event.
- `spec.approved` uses the `Approval notification` field in `spec.md`. `Sent`
  suppresses repeat delivery while the same approval remains valid.
- Material spec changes reset approval and `Approval notification` to
  `Not evaluated`. A later passing analysis and explicit reapproval form a new
  approval cycle that may emit one new notification.
