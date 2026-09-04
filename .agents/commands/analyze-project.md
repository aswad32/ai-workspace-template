# Analyze Project Command

Use this workflow for `/analyze-project` on an existing, migration,
modernization, or mixed project.

## Goal

Create evidence-backed documentation of the system that exists today and its
established engineering conventions. This workflow describes current state; it
does not redesign architecture or modify application code.

## Workflow

1. Read project context and inspect repository manifests, source boundaries,
   entry points, contracts, data stores, integrations, build/test/deployment
   configuration, and existing documentation progressively.
2. Separate observed facts from inferred relationships and unknowns. Cite paths
   for important claims. Do not treat intended plans as current implementation.
3. Describe major components, ownership, control/data flows, trust boundaries,
   runtime/deployment topology, persistence, external dependencies, failure
   handling, and operational signals only where evidence exists.
4. Extract recurring engineering conventions for layout, dependencies, errors,
   tests, security boundaries, migrations, and documentation. Do not elevate an
   isolated pattern into a standard without user confirmation.
5. Write or update the paths configured for architecture and project standards.
   When none are configured, propose `docs/architecture/current-state.md` and
   `memory/observed-conventions.md`; do not overwrite an existing authoritative
   document without explicit approval.
6. Update the project-context documentation map only with created or confirmed
   authoritative paths. Record unresolved ownership and architecture questions.
7. Validate links and review the diff for secrets, private payloads, unsupported
   claims, and accidental design recommendations.

## Stop Conditions

Stop when project context is missing, the project is purely greenfield, evidence
is too incomplete to support a useful description, authoritative documents
conflict, or the requested output would expose sensitive system details.
