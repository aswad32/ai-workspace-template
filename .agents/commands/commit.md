# Commit Command

Use this workflow for `/commit`.

## Goal

Commit only reviewed, intentional, cohesive changes with proportionate
validation, no secrets, and an accurate message.

## Workflow

1. Read project context, current branch, status, staged/unstaged/untracked path
   lists, and relevant review/remediation/verification evidence. Stop on the
   configured base branch.
2. Group changes by reviewable intent. Do not stage unrelated changes, local-only
   artifacts, generated noise, or files with suspected secrets.
3. Reuse applicable validation evidence and run focused checks for each intended
   group. Use broader project-context checks only when risk requires them. For
   docs-only work, inspect the textual/rendered diff and record why code checks
   do not apply.
4. Synchronize spec, plan, and task status with actual completion when the group
   includes an SDD package. Do not mark work Done merely because it is being
   committed or proposed for a PR.
5. Stage the approved group, re-check the staged diff, and create an imperative,
   concise commit message with known package/tracker references when useful.
6. Report the commit hash, message, validation, skipped checks, and remaining
   uncommitted files.

## Stop Conditions

Stop on a base branch, suspected secrets, unrelated staged work, ambiguous
grouping, or failed required validation without explicit approval for a clearly
marked work-in-progress commit.
