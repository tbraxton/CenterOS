# dashboard/workflows/ - CONTEXT

## Purpose

Home for workflow-specific dashboard pages that load inside the CenterOS dashboard iframe shell.

## Contents

- `CONTEXT.md` - this file.
- Future `<workflow-name>/` directories, each containing a workflow dashboard page at `index.html`.

## Usage / Trigger Conditions

Use this directory when a CenterOS workflow needs a dashboard page. Each page should be linked from `dashboard/index.html` and loaded into the `dashboard-frame` iframe.

## Inputs

- Workflow outputs, metrics, links, images, files, or status details that need to be shown in the dashboard.
- `templates/dashboard-page/page.html` as the starting template.

## Outputs

- Static workflow dashboard pages that can be opened inside the main dashboard shell.

## Steps

1. Create `dashboard/workflows/<workflow-name>/`.
2. Copy `templates/dashboard-page/page.html` to `dashboard/workflows/<workflow-name>/index.html`.
3. Replace all placeholders.
4. Add or update the sidebar link in `dashboard/index.html` with `target="dashboard-frame"`.
5. Document the page in the workflow's `CONTEXT.md`.

## Dependencies

- Runtime: Browser.
- Python packages: N/A.
- Node / npm packages: N/A.
- System binaries on PATH: None.
- API keys / env vars: None.
- External accounts / services: None.
- Internal (CenterOS): `dashboard/index.html`, `dashboard/styles.css`, `templates/dashboard-page/`, and the related workflow directory.

## Known Issues / Gotchas

- Pages in this directory should include their own topbar and breadcrumbs.
- Pages in this directory must not include sidebar markup, logo markup, or a second dashboard shell.

## Related

- `../index.html` - parent dashboard shell with the sidebar and iframe.
- `../styles.css` - shared dashboard styling.
- `../../templates/dashboard-page/` - dashboard page template.
- `../../workflows/` - source workflow directories.

## Revision History

- 2026-08-31 - Created workflow dashboard page container.
