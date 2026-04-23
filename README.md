# Midtown Toys

PowerToys-style utilities for IT MSPs.

## Live Site

https://toys.dev.midtowntg.com

## Tools Included

| Tool | Description |
|------|-------------|
| Context Sync | Sync Microsoft 365 to knowledge graph |
| SOP Generator | Screenshots to documentation |
| Quick Capture CLI | Fast capture for Logseq |
| GTD Dashboard CLI | Unified task view |
| Meeting Cost Tracker | Calculate meeting costs |
| Weekly Review | Automated GTD weekly review |

## Deploy to GitHub Pages

1. Create `toys.dev` repo under Midtown-Technology-Group
2. Copy these files to the repo
3. Enable GitHub Pages on `main` branch, `/ (root)` folder
4. Add CNAME file with `toys.dev.midtowntg.com`
5. Configure DNS CNAME: `toys.dev` → `midtown-technology-group.github.io`

## Local Preview

```bash
python -m http.server 8000
```

## License

Site content under MIT. Tool code under AGPL-3.0.
