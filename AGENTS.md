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
- When requested work is complete, self-review it, run relevant checks, commit it with a clear message and push the task branch to GitHub.
- After pushing a completed task branch, use GitHub CLI to create the pull request automatically. Do not require Michaela to open a comparison link manually. Never merge without her explicit approval.
- Finish by reporting the branch, changed files, checks performed, commit, push result, pull-request link and anything requiring review.
