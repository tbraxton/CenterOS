# dashboard/pages/ - CONTEXT

## Purpose

Default iframe pages for the CenterOS dashboard shell. These pages load inside `dashboard/index.html`.

## Contents

- `CONTEXT.md` - this file.
- `home.html` - default dashboard welcome page.
- `workflow-placeholder.html` - temporary destination for starter workflow links.

## Usage / Trigger Conditions

Use these pages when opening `dashboard/index.html` directly from disk. The parent dashboard shell owns the sidebar, while each page in this directory owns its own topbar and content.

## Inputs

- Shared dashboard stylesheet at `../styles.css`.

## Outputs

- Static HTML pages that render inside the dashboard iframe.

## Steps

1. Open `dashboard/index.html`.
2. Use the sidebar to load one of these pages into the dashboard iframe.
3. Replace placeholder workflow pages with real pages under `dashboard/workflows/<workflow-name>/` as workflows are created.

## Dependencies

- Runtime: Browser.
- Python packages: N/A.
- Node / npm packages: N/A.
- System binaries on PATH: None.
- API keys / env vars: None.
- External accounts / services: None.
- Internal (CenterOS): `dashboard/styles.css`.

## Known Issues / Gotchas

- These pages are meant to be loaded inside the iframe shell. They can open directly, but they will not show the sidebar when opened alone.

## Related

- `../index.html` - parent dashboard shell.
- `../styles.css` - shared dashboard styling.
- `../workflows/` - workflow-specific dashboard pages.

## Revision History

- 2026-08-31 - Created default iframe pages for the dashboard shell.
