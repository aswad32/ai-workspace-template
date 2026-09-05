# Project Context: [Project Name]

Copy this file to `.agents/project-context.md` during `/init-project`. Replace
bracketed values. Keep this file concise, factual, and free of secrets.

## Setup Status

- Status: Draft | Ready
- Last updated: <YYYY-MM-DD>
- Template revision: <revision from `TEMPLATE_VERSION` or `Not established`>
- Maintainer: <name or team>
- Project state: Greenfield | Existing | Migration | Modernization | Mixed | Not established
- Context evidence: <repository paths and user confirmations, or `Not established`>

## Product and Repository

- Project purpose: <one or two sentences>
- Primary users: <users or `Not defined`>
- Primary stakeholders: <teams or people, or `Not defined`>
- Project boundaries and non-goals: <constraints or `Not established`>
- Base branch: <branch or `Not established`>
- Branch naming: <convention or `Not established`>
- Source layout: <key directories, or `Not established`>
- Repository topology: <single repository, monorepo, or related repositories>

## Technology and Commands

- Runtime/framework: <technology or `Not established`>
- Package/dependency manager: <tool or `Not established`>
- Formatting/lint command: <command or `Not available`>
- Type-check command: <command or `Not available`>
- Focused test command: <command or `Not available`>
- Full test command: <command or `Not available`>
- Production build command: <command or `Not available`>
- End-to-end test command: <command or `Not available`>
- Migration/generation command: <command or `Not applicable`>
- Dependency/security audit command: <command or `Not available`>
- Validation constraints: <slow, destructive, remote-only, or `None`>
- Required manual validation: <checks or `Not applicable`>

## Documentation Map

| Topic | Location | Update when |
|---|---|---|
| Architecture | <path or `Not established`> | <trigger> |
| Setup | <path or `Not established`> | <trigger> |
| Data model | <path or `Not established`> | <trigger> |
| Design system | <path or `Not established`> | <trigger> |
| Decisions | <path or `Not established`> | <trigger> |

## Tracking and Delivery

- Work tracker: GitHub | Linear | Jira | Other: <name> | None
- Tracker project/repository: <reference or `None`>
- Pull-request host: GitHub | GitLab | Bitbucket | Other: <name> | None
- Pull-request base branch: <normally the base branch>
- Required PR checks: <checks or `Not established`>
- Required approvals: <people, teams, or rules; or `Not established`>
- Draft PR default: Yes | No | Not applicable
- Delivery environments: <local, test, staging, production, or `Not established`>
- Delivery completion point: <merged, deployed, released, or another observable event>
- Deployment/release constraints: <rules or `Not applicable`>

## Workflow Notifications

- Notification status: Disabled | Planned | Ready
- Provider: Slack | Teams | Other: <name> | None
- Delivery method: Agent connector | Webhook | Repository automation | None
- Destination: <non-secret channel/team identifier or `Not configured`>
- Credential reference: <connected-account or secret reference, never its value; or `Not configured`>
- Enabled events: `issue.created`, `spec.approved`, both, or `None`
- Send policy: Preview first | Automatic | Not applicable
- Automatic sending authorized by: <name, date, and scope; or `Not authorized`>
- Setup owner: <person or team, or `Not established`>
- Setup requirements: <non-secret prerequisites still needed or `Complete`>
- Setup guide: <path/URL or `Not available`>
- Last verified: <date and result, or `Never`>
- Failure policy: Warn and continue | Require delivery | Not applicable
- Message content restrictions: <rules or `None`>

## Governance and Decisions

- Decision owners: <people or teams, or `Not established`>
- Project principles/standards: <path or `Not established`>
- Architecture decision process: <ADR path/process or `Not established`>
- Exception/escalation process: <rule or `Not established`>

## Domain and Security Invariants

- Authorization model: <rules or `Not established`>
- Sensitive-data rules: <rules or `Not established`>
- Data integrity rules: <rules or `Not established`>
- Money, audit, retention, or compliance rules: <rules or `Not applicable`>
- External integrations and constraints: <list or `None`>

## UI Guidance

- UI technology: <technology or `Not applicable`>
- Design guidance location: <path or `Not applicable`>
- Accessibility/responsive expectations: <requirements or `Not applicable`>
