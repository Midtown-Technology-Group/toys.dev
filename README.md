# Midtown Tools Catalog

Small, focused utilities and supporting plumbing for Midtown's internal tools catalog.

## Live Site

https://toys.dev.midtowntg.com

## Catalog

<!-- catalog:start -->
| Tool | Group | Description |
| --- | --- | --- |
| Todo | Microsoft 365 and PSA | A Microsoft To Do companion built on our shared auth, using WAM sign-in and delegated task scopes. |
| Mail Triage | Microsoft 365 and PSA | Scans the inbox and prints compact JSON you can route into notifications and follow-ups. |
| Calendar Glance | Microsoft 365 and PSA | Read-only snapshots of your agenda for short-range planning and meeting context. |
| Communication Style | Microsoft 365 and PSA | Build a local style guide from your sent mail and Teams chats, sliced by time period or participant. |
| File Finder | Microsoft 365 and PSA | Search Microsoft 365 files and run focused folder and file actions through delegated Graph. |
| Halo CLI | Microsoft 365 and PSA | A standalone HaloPSA CLI and MCP server for safe operator and automation work. |
| Meeting Cost Tracker | Microsoft 365 and PSA | Work out what a Teams meeting really costs, from participant time and hourly rates. |
| Quick Capture | Workflow, Notes, and Reporting | Capture tasks, ideas, notes, and logs into your Logseq daily notes. |
| Detour | Workflow, Notes, and Reporting | Log unplanned detours in your daily Markdown notes so side work stays visible. |
| SOP Generator | Workflow, Notes, and Reporting | Record a browser workflow, review the draft, and publish a Halo KB article. |
| Time Tracker | Workflow, Notes, and Reporting | Track billable time on tasks with almost no friction, for MSP work logs and daily-note evidence. |
| GTD Dashboard | Workflow, Notes, and Reporting | One task view across your Logseq notes and Microsoft 365 work context, including how long items have been waiting. |
| Weekly Review | Workflow, Notes, and Reporting | Build your GTD weekly review from daily notes and work context. |
| Shared Microsoft Auth | Shared Plumbing | A reusable, WAM-first auth package for Graph tools, with shared token caching. |
| Context Sync | Shared Plumbing | Sync Microsoft 365 mail, calendar, and chats into a Logseq graph, with calendar timeblocking. |
| Keeper PowerCommander Vault | Shared Plumbing | A PowerShell SecretManagement vault backed by Keeper PowerCommander, with no Secrets Manager required. |
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
