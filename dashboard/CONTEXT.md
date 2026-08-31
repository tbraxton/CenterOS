# dashboard/ - CONTEXT

## Purpose

Static HTML dashboard shell for CenterOS. This dashboard gives users a simple local interface for linking to workflow-specific dashboard pages they create later.

## Contents

- `CONTEXT.md` - this file.
- `index.html` - default dashboard page.
- `styles.css` - dashboard styling.

## Usage / Trigger Conditions

Use this directory when a user wants a lightweight dashboard for their CenterOS workflows. Open `index.html` in a browser or host the HTML/CSS wherever static files are supported.

## Inputs

- Workflow dashboard page links, added as the user creates workflow dashboards.
- CenterOS logo at `images/centeros-logo-full.png`.

## Outputs

- A static dashboard page with sidebar workflow links and a centered default welcome panel.

## Steps

1. Open `index.html`.
2. Replace placeholder workflow links with real workflow dashboard pages as they are created.
3. Keep paths relative to the repo root.

## Dependencies

- Runtime: N/A.
- Python packages: N/A.
- Node / npm packages: N/A.
- System binaries on PATH: None.
- API keys / env vars: None.
- External accounts / services: None.
- Internal (CenterOS): `images/centeros-logo-full.png` for the sidebar logo.

## Known Issues / Gotchas

- Placeholder workflow links point to `#` until real workflow dashboard pages exist.
- If this dashboard is hosted outside the repo root, update the logo path to match the hosted asset location.

## Related

- `workflows/` - source workflow folders this dashboard is meant to link to.
- `images/` - CenterOS logo assets.

## Revision History

- 2026-08-31 - Created initial static dashboard shell.
