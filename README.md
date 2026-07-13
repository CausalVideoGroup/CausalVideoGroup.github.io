# CausalVideoGroup Website

This repository hosts the public website and research discussion archive for
CausalVideoGroup.

Planned website: <https://causalvideogroup.github.io/>

## Content structure

```text
projects/<project-slug>/
discussions/YYYY-MM-DD-<leader-short-name>-<topic-slug>/
```

For example:

```text
projects/causal-video-editing/
discussions/2026-07-13-yifan-forcing-ar-video-distillation/
```

The leader's complete name is stored in the discussion's `metadata.yaml`; only
the agreed short name is used in the public URL.

The metadata specification and examples are documented in
[`docs/METADATA.md`](docs/METADATA.md). Machine-readable schemas live in
[`schemas/`](schemas/).

## Create a discussion

Use an approved short name from `data/people.yaml`:

```bash
python3 scripts/new_discussion.py \
  --date 2026-07-13 \
  --leader yifan \
  --topic forcing-ar-video-distillation \
  --title "Forcing Series: The Evolution of AR Video Distillation"
```

The command creates:

```text
discussions/2026-07-13-yifan-forcing-ar-video-distillation/
```

It refuses to overwrite an existing entry unless `--force` is explicitly used.

## Rebuild indexes

After adding or editing metadata, regenerate the public indexes:

```bash
python3 scripts/build_site.py
```

This updates the generated regions on the homepage and the Discussions, People,
and Tags pages. Do not manually edit content between `GENERATED` markers.

## Validate before a pull request

```bash
python3 scripts/validate_site.py
python3 -m unittest discover -s tests -v
```

Validation fails on inconsistent directory names, unknown leaders, missing
files, incomplete research-quality fields, too few references or questions,
broken local links, malformed metadata URLs, and preview videos over 10 MiB.

See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the pull-request workflow, content
quality bar, public-data policy, and review expectations.

## Continuous integration and deployment

Pull requests run `.github/workflows/validate.yml`. Pushes to `main` rebuild,
validate, test, and deploy the repository through
`.github/workflows/deploy.yml`. In repository settings, GitHub Pages must use
**GitHub Actions** as its source.

## Status

The repository structure has been initialized locally. Website pages, content
templates, validation, index generation, and deployment will be added in the
following implementation steps.
