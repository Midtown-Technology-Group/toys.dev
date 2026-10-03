# Midtown Tools Catalog

Hugo site for Midtown's internal utilities, published at `toys.dev.midtowntg.com`. `main` is the default branch. Catalog entries live in `data/tools.yaml`; install examples live in `data/install.yaml`; `layouts/` and its partials render repeated page chrome; `static/` holds assets and the Pages CNAME. Read [README.md](README.md) and `hugo.toml` before changing catalog links, hosting, or theme behavior.

## Verification

From root, `hugo server` provides the local preview and `hugo --minify` builds the site, matching [.github/workflows](.github/workflows/). The CI workflow runs on pull requests to `main`: it installs the pinned Hugo with a verified checksum, validates the catalog, checks the generated README is current, builds the site, and checks in-page anchors and internal targets. External links are checked after merge, on push to `main`. The Pages workflow installs Hugo `0.161.1`; use that version when reproducing the release build.

Additional checks (Python 3 plus `pip install -r scripts/requirements.txt`):

- `python scripts/catalog.py validate` — structure, unique group/tool ids, and required fields.
- `python scripts/catalog.py readme --write` (or `--check`) — regenerate or verify the README catalog table.
- `python scripts/check_links.py public --external` — in-page anchors and external links after `hugo --minify`.

Every tool needs a stable `id`; `layouts/partials/tool-row.html` renders it as the `toy-<id>` anchor, and listed repositories point their GitHub homepage at that anchor. After editing `data/tools.yaml`, run the checks above and verify changed repository/installation/documentation links. Keep anchors stable when renaming a tool. Check mobile layout and keyboard navigation when changing templates or styles.

## Catalog accuracy

Describe each utility's current capabilities, permissions, and distribution based on its own repository evidence. Mail Triage has a read-only `Mail.ReadBasic` baseline; mutations require `Mail.ReadWrite`, sending requires `Mail.Send`, and shared-mailbox actions need the applicable shared scopes. Keep catalog capability claims conditional on those grants. Do not turn a source/MSI release into a claim of successful installation or client consent.

Verify File Finder permissions against its current source and documented operation. Do not infer tenant consent or claim heavier requirements from an old catalog note; identify the concrete scope and action. The pending elevated WinGet client proof is a gap, not completed rollout evidence. Keep site changes separate from changes to the cataloged applications, private package feed, DNS, or live client installations. Pages publishing is a deployment step beyond a successful local build. Site content in this repository is MIT-licensed; linked tools retain their own licenses, and several are AGPL-3.0.

## Security

`hugo.toml` denies external executables, remote fetches, and non-`HUGO_` environment access under `[security]`, and disables every embedded third-party template under `[privacy]`. Keep those restrictive unless a feature genuinely needs access; then add the narrowest allowlist entry or checksum instead of widening a rule globally.
