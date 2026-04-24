# Midtown Toys

Small, focused utilities and supporting plumbing for Midtown's internal toy chest.

## Live Site

https://toys.dev.midtowntg.com

## Featured Toys

| Tool | Description |
|------|-------------|
| Todo | Windows-first Microsoft To Do companion |
| Quick Capture | Fast capture into notes and workflows |
| Mail Triage | Read-only inbox scanning with JSON output |
| Calendar Glance | Read-only agenda snapshots |
| Context Sync | Sync Microsoft 365 into a knowledge graph |
| Shared Microsoft Auth | Reusable Windows-first Graph auth foundation |

## Site Notes

- `file-finder` is currently parked as a prototype because `Files.Read` prompts for tenant consent.
- `todo` now publishes a real MSI release into the private WinGet feed.
- Final `winget source add` / `winget install` proof still needs an elevated client-side pass.
- The site itself is a lightweight GitHub Pages landing page.

## Local Preview

```bash
python -m http.server 8000
```

## License

Site content under MIT. Tool repositories carry their own licenses.
