# Metadata conventions

Project and discussion pages use `metadata.yaml` as their source of structured
information. The canonical field definitions are maintained in:

- `schemas/project.schema.json`
- `schemas/discussion.schema.json`

## Discussion identity

A discussion directory is derived from four metadata values:

```text
YYYY-MM-DD-<leader.short_name>-<topic_slug>
```

Example:

```yaml
title: Streaming Video Generation with Force Control
date: 2026-07-18
topic_slug: streaming-control
leader:
  name: Peiyuan Zhu
  short_name: peiyuan
  github: SoftPointer
status: before-meeting
summary: A discussion of controllable streaming video generation.
tags:
  - video-generation
  - streaming-generation
  - controllable-generation
related_projects:
  - long-video-generation
```

This produces:

```text
discussions/2026-07-18-peiyuan-streaming-control/
```

The full leader name is for display. `short_name` is the stable, URL-safe name
used in the directory. If short names ever collide, group members must agree on
a unique short name before the entry is created.

The approved leader names and URL short names are maintained in
`data/people.yaml`:

| Full name | Short name |
| --- | --- |
| Peiyuan Zhu | `peiyuan` |
| Yifan Shen | `yifan` |
| Jinyuan Hu | `jinyuan` |
| Yuxin Wang | `yuxin` |
| Yichang Jian | `yichang` |

## Project identity

A project directory must exactly match its `slug`:

```yaml
title: Causal Video Editing
slug: causal-video-editing
status: active
summary: Research on causally grounded, temporally consistent video editing.
leaders:
  - name: Peiyuan Zhu
    short_name: peiyuan
    github: SoftPointer
tags:
  - video-editing
  - causal-generation
links: {}
```

This produces:

```text
projects/causal-video-editing/
```

## Slug rules

Slugs and tags must:

- contain lowercase ASCII letters, digits, and single hyphens only;
- not start or end with a hyphen;
- remain stable after a page has been published.

## Status values

Discussion statuses:

```text
planned -> before-meeting -> after-meeting -> archived
```

Project statuses:

```text
planned -> active -> published -> archived
```

## Public-data rule

Metadata and every file published by this repository are public. Do not include
unpublished proposals, private experiment plans, negative results intended for
internal use, credentials, or access-controlled URLs.
