# dashboard/ - CONTEXT

## Purpose

Static HTML dashboard shell for CenterOS. This dashboard gives users a simple local interface for linking to workflow-specific dashboard pages while still working when opened directly from disk.

## Contents

- `CONTEXT.md` - this file.
- `create-dashboard-page.py` - deterministic helper that creates a workflow dashboard page from the dashboard page template and updates the sidebar.
- `index.html` - parent dashboard shell. Owns the logo, sidebar links, and iframe container.
- `pages/` - default iframe pages, including the dashboard home page and placeholder workflow page.
- `styles.css` - shared dashboard styling for the shell and iframe pages.
- `workflows/` - future workflow-specific dashboard pages.

## Usage / Trigger Conditions

Use this directory when a user wants a lightweight dashboard for their CenterOS workflows. Open `index.html` directly in a browser. The sidebar lives in `index.html`; each linked page loads inside the iframe and owns its own topbar, breadcrumbs, and content.

## Inputs

- Workflow dashboard page links, added to `index.html` as the user creates workflow dashboards.
- CenterOS logo at `images/centeros-logo-full.png`.

## Outputs

- A static dashboard shell with one maintained sidebar and iframe-loaded dashboard pages.
- Workflow dashboard pages with their own topbars and breadcrumbs.

## Steps

1. Open `index.html`.
2. Use the sidebar links to load pages into the iframe.
3. When a workflow dashboard page is created and Python is available, run `python dashboard/create-dashboard-page.py <workflow-name> "<Workflow Name>" "<description>"`.
4. If Python is unavailable, manually copy `templates/dashboard-page/page.html` to `dashboard/workflows/<workflow-name>/index.html` and replace the placeholders.
5. Add or update only the sidebar link in `dashboard/index.html`.
6. Give each workflow dashboard page its own topbar and breadcrumbs.
7. Keep paths relative to the repo root.

## Dependencies

- Runtime: Browser for the dashboard; Python 3 for the optional helper script.
- Python packages: stdlib only.
- Node / npm packages: N/A.
- System binaries on PATH: None.
- API keys / env vars: None.
- External accounts / services: None.
- Internal (CenterOS): `images/centeros-logo-full.png` for the sidebar logo; `templates/dashboard-page/` for workflow dashboard page scaffolding.

## Known Issues / Gotchas

- Placeholder workflow links point to `pages/workflow-placeholder.html` until real workflow dashboard pages exist.
- Workflow dashboard pages should not include sidebar markup. The sidebar belongs only in `dashboard/index.html`.
- `create-dashboard-page.py` replaces the first placeholder sidebar link when one exists; after placeholders are gone, it appends new links before `WORKFLOW_LINKS_END`.
- If this dashboard is hosted outside the repo root, update the logo path to match the hosted asset location.

## Related

- `workflows/` - source workflow folders this dashboard is meant to link to.
- `images/` - CenterOS logo assets.
- `templates/dashboard-page/` - template for iframe-loaded workflow dashboard pages.

## Revision History

- 2026-08-31 - Created initial static dashboard shell.
- 2026-08-31 - Converted dashboard to an iframe shell with page-owned topbars.
- 2026-08-31 - Added deterministic dashboard page helper script.
