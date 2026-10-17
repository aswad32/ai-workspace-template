# Pull Request Command

Use this workflow for `/pr`.

## Goal

Publish the reviewed dedicated branch through the project’s configured hosting
process with an accurate, evidence-based pull or merge request description.

## Workflow

1. Read project context, `templates/pr.md`, branch/status, changed paths, commit
   subjects, and the configured pull-request base branch. Stop on a base branch
   or when no PR host is configured.
2. Inspect only the evidence needed to identify scope, related package, tracker
   references in the spec, plan, task, and optional `issues/index.md`, contracts,
   migration/UI impact, validation, spec-conformance, review/remediation status,
   documentation, risks, and rollout notes. Treat every non-`None` `Tracking
   reference` in `spec.md` as a canonical work item linked to this package,
   even when it is absent from `issues/index.md`. Deduplicate other references.
   Compare each item's scope with the approved spec and verified delivery to
   distinguish completed work from wider or outstanding work; do not infer that
   the spec's work item is unrelated from its title or missing index row.
3. Stop if unrelated changes or suspected secrets are present. For an SDD
   package, require current approval, a passing spec analysis, a passing
   `/verify-spec` report, a current review covering the proposed diff,
   verification of any remediation, and no unresolved must-fix findings.
   Confirm required project-context checks passed or have documented skipped
   reasons.
4. Fill `templates/pr.md` with concrete information and a closure plan for each
   linked work item. Add a tracker-supported automatic closing reference only
   when merging the request reaches the configured delivery completion point and
   fully resolves that item. Otherwise use a non-closing reference and record
   whether `/close-spec` should close it after delivery or leave it open, with
   the specific unfinished work. Do not assume every item in `issues/index.md`
   is resolved. If the spec's tracking item cannot be closed, explain why in
   the closure plan rather than omitting it.
5. Push the dedicated branch to the configured host without force-pushing unless
   the user explicitly authorizes it. Follow the `Draft PR default` recorded in
   project context; if it is not established, prefer a draft when supported.
6. Report the URL, validation, skipped checks, work-item closure plan, missing
   references, and remaining risks.

## Stop Conditions

Stop for an ambiguous base branch/host, missing tracking context or an unclear
work-item scope that affects closure, failed required validation,
authentication/permission errors, or an inaccurate PR scope.
