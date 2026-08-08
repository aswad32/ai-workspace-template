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
   reference, contracts, migration/UI impact, validation, review/remediation
   status, documentation, risks, and rollout notes.
3. Stop if unrelated changes or suspected secrets are present. Confirm that
   required project-context checks have passed or their skipped reasons are
   documented.
4. Fill `templates/pr.md` with concrete information. Add a closing reference
   only when the configured tracker supports it and the PR fully completes the
   referenced work.
5. Push the dedicated branch to the configured host without force-pushing unless
   the user explicitly authorizes it. Create a draft PR by default when the host
   supports drafts.
6. Report the URL, validation, skipped checks, missing references, and remaining
   risks.

## Stop Conditions

Stop for an ambiguous base branch/host, missing tracking context that affects a
closing reference, failed required validation, authentication/permission errors,
or an inaccurate PR scope.
