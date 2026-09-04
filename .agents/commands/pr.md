# Pull Request Command

Use this workflow for `/pr`.

## Goal

Publish the reviewed dedicated branch through the project’s configured hosting
process with an accurate, evidence-based pull-request description.

## Workflow

1. Read project context, `templates/pr.md`, branch/status, changed paths, commit
   subjects, and the configured pull-request base branch. Stop on a base branch
   or when no PR host is configured.
2. Inspect only the evidence needed to identify scope, related package, tracker
   reference, contracts, migration/UI impact, validation, spec-conformance,
   review/remediation status, documentation, risks, and rollout notes.
3. Stop if unrelated changes or suspected secrets are present. For an SDD
   package, require current approval, a passing spec analysis, a passing
   `/verify-spec` report, a current review covering the proposed diff,
   verification of any remediation, and no unresolved must-fix findings.
   Confirm required project-context checks passed or have documented skipped
   reasons.
4. Fill `templates/pr.md` with concrete information. Add a closing reference
   only when the configured tracker supports it and the PR fully completes the
   referenced work.
5. Push the dedicated branch to the configured host without force-pushing unless
   the user explicitly authorizes it. Follow the `Draft PR default` recorded in
   project context; if it is not established, prefer a draft when supported.
6. Report the URL, validation, skipped checks, missing references, and remaining
   risks.

## Stop Conditions

Stop for an ambiguous base branch/host, missing tracking context that affects a
closing reference, failed required validation, authentication/permission errors,
or an inaccurate PR scope.
