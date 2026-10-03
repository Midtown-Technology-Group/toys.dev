# Midtown Tools Catalog

Small, focused utilities and supporting plumbing for Midtown's internal tools catalog.

## Live Site

https://toys.dev.midtowntg.com

## Catalog

<!-- catalog:start -->
| Tool | Group | Description |
| --- | --- | --- |
| Todo | Microsoft 365 and PSA | Microsoft To Do companion built on shared auth, live-verified with WAM and delegated task scopes. |
| Mail Triage | Microsoft 365 and PSA | Inbox triage with compact JSON output for notification and follow-up workflows. |
| Calendar Glance | Microsoft 365 and PSA | Read-only agenda snapshots for short-range planning and meeting context. |
| Communication Style | Microsoft 365 and PSA | Build local style guides from Teams and Sent Items, including era and participant-focused cuts. |
| File Finder | Microsoft 365 and PSA | Microsoft 365 file discovery and focused OneDrive actions through delegated Graph. |
| Halo CLI | Microsoft 365 and PSA | Standalone HaloPSA command line workflows for safe operator and automation use. |
| Meeting Cost Tracker | Microsoft 365 and PSA | Calculate the real cost of Teams meetings from participant time and hourly rates. |
| Meeting Extractor | Microsoft 365 and PSA | Extract decisions and action items from Microsoft Teams transcripts. |
| Quick Capture | Workflow, Notes, and Reporting | Fast capture into notes and workflows with short command aliases intact. |
| Detour | Workflow, Notes, and Reporting | Track work detours in daily Markdown notes so side work stays visible. |
| SOP Generator | Workflow, Notes, and Reporting | Turn Greenshot screenshot runs into step-by-step IT documentation. |
| Time Tracker | Workflow, Notes, and Reporting | Track task time with low friction for MSP work logs and daily-note evidence. |
| GTD Dashboard | Workflow, Notes, and Reporting | Unified task view across Logseq notes, including waiting-for aging analysis. |
| Link Validator | Workflow, Notes, and Reporting | Validate knowledge graph links and catch broken wiki-link references. |
| Topic Trends | Workflow, Notes, and Reporting | Analyze knowledge notes for topics that are heating up, cooling down, or expanding. |
| Weekly Review | Workflow, Notes, and Reporting | Generate GTD weekly reviews from daily notes and work context. |
| Shared Microsoft Auth | Shared Plumbing | Reusable WAM-first auth package for Graph tools with common cache behavior. |
| Context Sync | Shared Plumbing | Mature graph-connected reference implementation for shared Microsoft 365 auth. |
| Keeper PowerCommander Vault | Shared Plumbing | PowerShell SecretManagement vault backed by Keeper PowerCommander. |
<!-- catalog:end -->

This table is generated from `data/tools.yaml` by `scripts/catalog.py readme --write`. Do not edit it by hand; CI fails when it is stale.

## Site Notes

- The site is built with Hugo and deployed to GitHub Pages from Actions. `main` is the default branch; pull requests run build, catalog, and link checks.
- Catalog entries live in `data/tools.yaml`. Each tool has a stable `id` used for its `#toy-<id>` anchor; listed repositories point their GitHub homepage at that anchor, so keep ids stable.
- Install examples live in `data/install.yaml`; the local theme is intentionally tiny, with page chrome and repeated catalog pieces in `layouts/partials/`.
- `file-finder` is listed, but its consent story is heavier than the read-only mail/calendar/task toys.
- `todo` now publishes a real MSI release into the private WinGet feed.
- Final `winget source add` / `winget install` proof still needs an elevated client-side pass.

## Local Preview

```bash
hugo server
```

Validate catalog data and check links before opening a pull request:

```bash
python scripts/catalog.py validate
python scripts/catalog.py readme --check
hugo --minify
python scripts/check_links.py public --external
```

CI runs the same checks on pull requests (external links are checked after merge), and `python scripts/check_links.py public` works offline without `--external`.

The scripts need Python 3 with `pip install -r scripts/requirements.txt`.

## License

Site content in this repository is licensed under the MIT License (see [LICENSE](LICENSE)).
The listed tool repositories carry their own licenses; several are AGPL-3.0. This repository does not relicense them.
