#!/usr/bin/env python3
"""Check in-page anchors, internal targets, and external links in a built site.

Usage:
  python scripts/check_links.py public [--external]

Internal anchors and local files are always checked. External http(s) links are
checked only with --external so the default run stays offline.
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

USER_AGENT = "mtg-toys-link-check/1.0 (+https://toys.dev.midtowntg.com)"
# Statuses that are not evidence of a broken link (auth walls, wrong method,
# rate limits).
IGNORED_STATUS = {403, 405, 429}


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.urls: list[str] = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.urls.append(attrs["href"])
        elif tag in ("link", "script", "img") and (attrs.get("href") or attrs.get("src")):
            self.urls.append(attrs.get("href") or attrs.get("src"))


def parse_html(path: Path) -> LinkParser:
    parser = LinkParser()
    parser.feed(path.read_text(encoding="utf-8"))
    return parser


def resolve_local(site_root: Path, html_file: Path, href: str) -> Path | None:
    target = href.split("#", 1)[0].split("?", 1)[0]
    if not target:
        return None
    if target.startswith("/"):
        return site_root / target.lstrip("/")
    return html_file.parent / target


def check_external(url: str) -> str | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return None if response.status < 400 else f"{url}: HTTP {response.status}"
    except urllib.error.HTTPError as exc:
        return None if exc.code in IGNORED_STATUS else f"{url}: HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001 - report any transport failure
        return f"{url}: {exc}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("site", type=Path, help="built site directory (e.g. public)")
    parser.add_argument("--external", action="store_true", help="also check external http(s) links")
    args = parser.parse_args()

    site_root = args.site.resolve()
    html_files = sorted(args.site.rglob("*.html"))
    if not html_files:
        print(f"error: no HTML found under {args.site}", file=sys.stderr)
        sys.exit(1)

    errors: list[str] = []
    externals: set[str] = set()
    for html_file in html_files:
        parsed = parse_html(html_file)
        for url in parsed.urls:
            if url.startswith("#"):
                fragment = url[1:]
                if fragment and fragment not in parsed.ids:
                    errors.append(f"{html_file}: missing anchor #{fragment}")
                continue
            if url.startswith(("http://", "https://")):
                externals.add(url)
                continue
            if url.startswith(("mailto:", "tel:", "data:", "javascript:")):
                continue
            anchor = url.split("#", 1)[1] if "#" in url else None
            target = resolve_local(site_root, html_file, url)
            if target is not None and not target.exists():
                errors.append(f"{html_file}: missing internal target {url}")
            elif anchor and target is not None and target.suffix == ".html":
                ids = parse_html(target).ids
                if anchor not in ids:
                    errors.append(f"{target}: missing anchor #{anchor} in {url}")

    if args.external:
        for url in sorted(externals):
            problem = check_external(url)
            if problem:
                errors.append(problem)

    if errors:
        for error in errors:
            print(f"error: {error}", file=sys.stderr)
        sys.exit(1)
    print(f"links ok: {len(html_files)} page(s), {len(externals)} external link(s)")


if __name__ == "__main__":
    main()
