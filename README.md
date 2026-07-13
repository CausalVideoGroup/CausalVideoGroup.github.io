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
discussions/2026-07-18-peiyuan-streaming-control/
```

The leader's complete name is stored in the discussion's `metadata.yaml`; only
the agreed short name is used in the public URL.

The metadata specification and examples are documented in
[`docs/METADATA.md`](docs/METADATA.md). Machine-readable schemas live in
[`schemas/`](schemas/).

## Status

The repository structure has been initialized locally. Website pages, content
templates, validation, index generation, and deployment will be added in the
following implementation steps.
