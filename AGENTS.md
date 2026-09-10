# AGENTS.md

## Operating rules

- GitHub main is the source of truth.
- Inspect the current repository and relevant existing files before starting work.
- Fetch origin before beginning a new task.
- Never edit or commit directly on main.
- Codex branches must use codex/<short-task-name>.
- Claude branches must use claude/<short-task-name>.
- Keep each branch limited to one task.
- Do not alter unrelated files or include temporary, generated, credential or environment files.
- Preserve existing user changes. Never reset, restore, delete, overwrite or merge conflicting work without explicit approval.
- For substantive Business Builder commercial work, read and follow `operating-system/QUALITY_GATE.md` before calling anything finished or ready for Michaela.
- Relevant current product specifications, brand decisions and channel operating files must be inspected before major product, Etsy or Pinterest work. Do not rely on memory when a source of truth exists.
- When requested work is complete, self-review it, run relevant checks, commit it with a clear message and push the task branch to GitHub.
- For substantial commercial deliverables, report the QA status using the receipt defined in `operating-system/QUALITY_GATE.md`. Any check that could not genuinely be performed must be marked NOT VERIFIED.
- After pushing a completed task branch, use GitHub CLI to create the pull request automatically. Do not require Michaela to open a comparison link manually. Never merge without her explicit approval.
- Never publish website content or take another external publishing action without Michaela’s explicit approval.
- Finish by reporting the branch, changed files, checks performed, commit, push result, pull-request link and anything requiring review.
