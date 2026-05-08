# Midtown Toys

Small, focused utilities and supporting plumbing for Midtown's internal toy chest.

## Live Site

https://toys.dev.midtowntg.com

## Featured Toys

| Tool | Description |
|------|-------------|
| Calendar Glance | Read-only agenda snapshots |
| Communication Style | Generate local communication style guides from Teams and Sent Items |
| Context Sync | Sync Microsoft 365 into a knowledge graph |
| Detour | Track work detours in daily Markdown notes |
| File Finder | Microsoft 365 file discovery and compact OneDrive actions |
| GTD Dashboard CLI | Unified task view |
| Halo CLI | HaloPSA operator and automation CLI |
| Keeper PowerCommander Vault | Read-only SecretManagement vault backed by Keeper PowerCommander |
| Link Validator | Validate knowledge graph links |
| Mail Triage | Read-only inbox scanning with JSON output |
| Meeting Cost Tracker | Calculate meeting costs |
| Meeting Extractor | Extract action items and decisions from Teams transcripts |
| Quick Capture | Fast capture into notes and workflows |
| SOP Generator | Screenshots to documentation |
| Shared Microsoft Auth | Reusable Windows-first Graph auth foundation |
| Time Tracker | Track time on tasks with low friction |
| Todo | Windows-first Microsoft To Do companion |
| Topic Trends | Analyze knowledge graph topic trends |
| Weekly Review | Automated GTD weekly review |

## Site Notes

- `file-finder` is listed, but its consent story is heavier than the read-only mail/calendar/task toys.
- `todo` now publishes a real MSI release into the private WinGet feed.
- Final `winget source add` / `winget install` proof still needs an elevated client-side pass.
- The site itself is a lightweight GitHub Pages landing page.

## Local Preview

```bash
python -m http.server 8000
```

## License

Site content under MIT. Tool repositories carry their own licenses.
