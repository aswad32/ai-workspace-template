# Design Architecture Command

Use this workflow for `/design-architecture <scope>` when the user explicitly
requests architecture design or redesign.

## Goal

Produce an accepted architecture decision for a defined greenfield, migration,
modernization, or subsystem scope without implementing it.

## Workflow

1. Read project context, applicable current-state documentation, accepted specs,
   ADRs, constraints, quality targets, trust boundaries, and integration/data
   requirements. Stop if the design scope is materially ambiguous.
2. Ask one high-impact clarification at a time. Resolve expected scale,
   reliability, security, compliance, compatibility, operations, ownership,
   delivery, and cost constraints only when applicable.
3. Present viable alternatives with benefits, costs, risks, reversibility, and
   migration impact. Clearly distinguish evidence from recommendations.
4. Obtain explicit user selection before writing a canonical decision. Do not
   choose a materially different architecture merely because one option is
   conventional.
5. Create or update the configured architecture overview and add ADRs for
   consequential decisions. Include scope, boundaries, components, data/control
   flows, trust boundaries, failure modes, deployment view, observability,
   rollout, rollback, and unresolved risks as applicable.
6. Update project-context documentation paths and invariants only when the user
   confirms they are authoritative. Do not modify code, dependencies,
   infrastructure, schemas, or implementation tasks.
7. Validate links and inspect the documentation diff. Report accepted decisions,
   rejected alternatives, open questions, and implementation prerequisites.

## Stop Conditions

Stop for missing project context, unresolved requirements that would change the
architecture, absent authority for consequential choices, sensitive details
that cannot be documented safely, or a request that silently expands into
implementation.
