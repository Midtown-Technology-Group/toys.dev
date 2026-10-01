# Midtown Tools Catalog

Hugo site for Midtown's internal utilities, published at `toys.dev.midtowntg.com`. Catalog entries live in `data/tools.yaml`; `layouts/` and its partials render repeated page chrome; `static/` holds assets and the Pages CNAME. Read [README.md](README.md) and `hugo.toml` before changing catalog links, hosting, or theme behavior.

## Verification

From root, `hugo server` provides the local preview and `hugo --minify` builds the site, matching [.github/workflows](.github/workflows/). The Pages workflow currently installs Hugo `0.161.1`; use that version when reproducing the release build. No application test suite was found in the inspected source.

After editing `data/tools.yaml`, check YAML validity through the Hugo build, inspect the rendered catalog, and verify changed repository/installation/documentation links. Keep anchors stable: listed repositories' homepage links may point directly to their catalog entries. Check mobile layout and keyboard navigation when changing templates or styles.

## Catalog accuracy

Describe each utility's current capabilities, permissions, and distribution based on its own repository evidence. Mail Triage has a read-only `Mail.ReadBasic` baseline; mutations require `Mail.ReadWrite`, sending requires `Mail.Send`, and shared-mailbox actions need the applicable shared scopes. Keep catalog capability claims conditional on those grants. Do not turn a source/MSI release into a claim of successful installation or client consent.

Verify File Finder permissions against its current source and documented operation. Do not infer tenant consent or claim heavier requirements from an old catalog note; identify the concrete scope and action. The pending elevated WinGet client proof is a gap, not completed rollout evidence. Keep site changes separate from changes to the cataloged applications, private package feed, DNS, or live client installations. Pages publishing is a deployment step beyond a successful local build. Site content has its own MIT license; linked tools retain their own licenses.
