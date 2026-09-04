# Changelog

This file records reusable workflow and artifact-contract changes. Project code
changes belong in the consuming project's own release notes.

## Unreleased

### Added

- Adaptive greenfield and brownfield project initialization survey.
- Explicit spec analysis and human approval before implementation.
- Requirement-to-plan-to-task traceability and implementation conformance
  verification.
- Evidence-backed project analysis and separately authorized architecture design.
- Canonical analysis, review, remediation, and verification report templates.
- Package closure, supersession metadata, and a durable package index.
- Standard-library SDD structure validator and workflow revision marker.
- Optional provider-neutral workflow notifications for newly created issues and
  approved, implementation-ready specs, including setup readiness guidance,
  preview-first delivery, redaction, and duplicate suppression.

### Changed

- Package lifecycle now distinguishes `Implemented` from delivered `Done`.
- Remediation commands identify their source review explicitly.
- Project context no longer assumes a base branch, branch convention, tracker,
  pull-request host, or delivery point.
- Draft spec creation and analysis remain silent; the spec notification event is
  evaluated only after `/approve-spec` makes the package ready to implement.

### Fixed

- Fresh template-derived repositories no longer treat unchanged starter
  boilerplate as evidence of the new project's identity or lifecycle state.

## Upgrade Notes

Existing adopters should merge these changes on a dedicated branch, rerun
`/init-project` to fill newly introduced context and notification fields, add
`Approval notification: Not evaluated` to active spec metadata when adopting
notifications, and leave active packages `Draft` until they have a passing
analysis and recorded approval.
