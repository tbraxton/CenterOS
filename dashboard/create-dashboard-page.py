#!/usr/bin/env python3
"""
Create a CenterOS workflow dashboard page and wire it into the dashboard sidebar.

This script uses only the Python standard library. It is intentionally narrow:
it creates one workflow dashboard page from templates/dashboard-page/page.html
and updates the sidebar links in dashboard/index.html.
"""

from __future__ import annotations

import argparse
import re
import sys
from html import escape
from pathlib import Path


DEFAULT_ICON = "bi-file-earmark-text"
PLACEHOLDER_RE = re.compile(
    r"\n\s*<a class=\"nav-item\" href=\"pages/workflow-placeholder\.html#workflow-\d\" target=\"dashboard-frame\">"
    r".*?"
    r"\n\s*</a>",
    re.DOTALL,
)
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FORBIDDEN_PAGE_PATTERNS = (
    "<aside",
    'class="sidebar"',
    "centeros-logo",
    'class="app-shell"',
    'name="dashboard-frame"',
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a workflow dashboard page from the CenterOS dashboard page template."
    )
    parser.add_argument("slug", help="Workflow slug, for example meeting-summary")
    parser.add_argument("name", help='Workflow display name, for example "Meeting Summary"')
    parser.add_argument("description", help="One sentence describing what the dashboard page shows")
    parser.add_argument(
        "--icon",
        default=DEFAULT_ICON,
        help=f"Bootstrap Icons class without the leading 'bi '. Default: {DEFAULT_ICON}",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing dashboard page for this workflow",
    )
    return parser.parse_args()


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def validate_slug(slug: str) -> None:
    if not SLUG_RE.fullmatch(slug):
        raise ValueError("Slug must be lowercase kebab-case using only letters, numbers, and hyphens.")


def normalize_icon(icon: str) -> str:
    icon = icon.strip()
    if icon.startswith("bi "):
        icon = icon.split(" ", 1)[1]
    if not icon.startswith("bi-"):
        icon = f"bi-{icon}"
    return icon


def render_template(template: str, *, slug: str, name: str, description: str) -> str:
    replacements = {
        "{{PAGE_TITLE}}": escape(f"{name} Dashboard"),
        "{{WORKFLOW_NAME}}": escape(name),
        "{{WORKFLOW_SLUG}}": escape(slug),
        "{{PAGE_DESCRIPTION}}": escape(description),
        "{{BREADCRUMB_CURRENT}}": escape(name),
    }

    rendered = template
    for token, value in replacements.items():
        rendered = rendered.replace(token, value)
    return rendered


def validate_dashboard_page(html: str) -> None:
    lowered = html.lower()
    for pattern in FORBIDDEN_PAGE_PATTERNS:
        if pattern in lowered:
            raise ValueError(f"Generated page contains forbidden dashboard shell markup: {pattern}")
    if 'class="topbar"' not in html:
        raise ValueError('Generated page must include its own topbar: class="topbar"')
    if 'class="dashboard-page"' not in html:
        raise ValueError('Generated page must include a main content section: class="dashboard-page"')


def build_nav_item(*, slug: str, name: str, icon: str) -> str:
    return f'''
        <a class="nav-item" href="workflows/{escape(slug)}/index.html" target="dashboard-frame">
          <span class="nav-icon" aria-hidden="true">
            <i class="bi {escape(icon)}"></i>
          </span>
          <span>{escape(name)}</span>
        </a>'''


def update_sidebar(index_path: Path, *, slug: str, name: str, icon: str) -> bool:
    html = index_path.read_text(encoding="utf-8")
    href = f'href="workflows/{slug}/index.html"'
    nav_item = build_nav_item(slug=slug, name=name, icon=icon)

    if href in html:
        updated = re.sub(
            rf'\n\s*<a class="nav-item" href="workflows/{re.escape(slug)}/index\.html" target="dashboard-frame">.*?\n\s*</a>',
            nav_item,
            html,
            flags=re.DOTALL,
        )
    else:
        placeholder_match = PLACEHOLDER_RE.search(html)
        if placeholder_match:
            updated = html[: placeholder_match.start()] + nav_item + html[placeholder_match.end() :]
        else:
            marker = "        <!-- WORKFLOW_LINKS_END -->"
            if marker not in html:
                raise ValueError("Could not find WORKFLOW_LINKS_END marker in dashboard/index.html.")
            updated = html.replace(marker, nav_item + "\n" + marker, 1)

    if updated == html:
        return False

    index_path.write_text(updated, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    args = parse_args()
    slug = args.slug.strip()
    name = args.name.strip()
    description = args.description.strip()
    icon = normalize_icon(args.icon)

    try:
        validate_slug(slug)
        if not name:
            raise ValueError("Workflow display name is required.")
        if not description:
            raise ValueError("Dashboard description is required.")

        root = repo_root()
        template_path = root / "templates" / "dashboard-page" / "page.html"
        index_path = root / "dashboard" / "index.html"
        target_dir = root / "dashboard" / "workflows" / slug
        target_path = target_dir / "index.html"

        if not template_path.exists():
            raise FileNotFoundError(f"Missing template: {template_path.relative_to(root)}")
        if not index_path.exists():
            raise FileNotFoundError(f"Missing dashboard shell: {index_path.relative_to(root)}")
        if target_path.exists() and not args.force:
            raise FileExistsError(
                f"{target_path.relative_to(root)} already exists. Re-run with --force to overwrite it."
            )

        rendered = render_template(
            template_path.read_text(encoding="utf-8"),
            slug=slug,
            name=name,
            description=description,
        )
        validate_dashboard_page(rendered)

        target_dir.mkdir(parents=True, exist_ok=True)
        target_path.write_text(rendered, encoding="utf-8", newline="\n")
        sidebar_changed = update_sidebar(index_path, slug=slug, name=name, icon=icon)

        print(f"Created dashboard page: {target_path.relative_to(root)}")
        if sidebar_changed:
            print("Updated sidebar link: dashboard/index.html")
        else:
            print("Sidebar link already current: dashboard/index.html")
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
