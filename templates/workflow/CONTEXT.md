# {{WORKFLOW_NAME}} - CONTEXT

## Purpose

{{ONE_LINE_PURPOSE}}

## Contents

- `CONTEXT.md` - this file.
- `LOG.md` - append-only journal of actions and runs for this workflow.
- If applicable, `<skill-name>/` - workflow-scoped skill directory. Each skill directory contains its own `SKILL.md`.
- If requested, `../../dashboard/workflows/{{WORKFLOW_NAME}}/index.html` - optional iframe-loaded dashboard page for this workflow.

## Usage / Trigger Conditions

When to run this workflow, and who or what triggers it.

## Inputs

What this workflow needs to run: files, parameters, context, prerequisite state.

## Outputs

What this workflow produces: files, side effects, status, downstream state changes.

If requested, this workflow may also produce an optional workflow dashboard page under `dashboard/workflows/{{WORKFLOW_NAME}}/`. The page must load inside `dashboard/index.html`, include its own topbar and breadcrumbs, and never include sidebar markup.

## Steps

1. First step.
2. Next step.
3. Continue as needed.
4. If the user requests a dashboard page, use `dashboard/create-dashboard-page.py` when Python is available. Otherwise copy `templates/dashboard-page/page.html` to `dashboard/workflows/{{WORKFLOW_NAME}}/index.html`, replace all placeholders, link to `../../styles.css`, add or update the sidebar link in `dashboard/index.html` with `target="dashboard-frame"`, and document the dashboard page in this file's Outputs and Related sections.
5. Append an entry to `LOG.md`.

## Dependencies

List everything a fresh machine needs to run this workflow. Explicitly say "None" for a category if it does not apply so cold-start readers know the question was considered, not skipped. Pip installs, npm packages, and system binaries do not ride with synced files; a new machine must reinstall them.

- **Runtime**: Python / Node / Bun version required, or "N/A" for pure text workflows.
- **Python packages**: exact install command, "stdlib only", or "N/A".
- **Node / npm packages**: exact install command or "N/A".
- **System binaries on PATH**: for example `ffmpeg`, `ffprobe`, `git`, or "None".
- **API keys / env vars**: name, purpose, source URL, approximate cost, or "None".
- **External accounts / services**: services requiring signup, or "None".
- **Internal (CenterOS)**: other workflows, wikis, skills, templates, or MCPs this relies on. List each with relative path and a short note, or "None".
- **Dashboard (optional)**: `../../dashboard/`, `../../dashboard/create-dashboard-page.py`, and `../../templates/dashboard-page/` if this workflow includes a dashboard page, or "None".

## Known Issues / Gotchas

- Things that have broken before or that future sessions should watch out for. Start empty; append as issues arise.

## Related

- Pointers to related workflows, wikis, or parent directories.
- If this workflow has a dashboard page, link `../../dashboard/workflows/{{WORKFLOW_NAME}}/`.

## Revision History

- **{{DATE}}** - Created. Initial version.
