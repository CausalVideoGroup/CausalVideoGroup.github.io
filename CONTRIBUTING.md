# Contributing to CausalVideoGroup.github.io

All public website changes go through a pull request. Do not push topic content
directly to `main` after branch protection is enabled.

## Before publishing anything

This repository is public. Do not include unpublished proposals, private
experiment plans, credentials, access-controlled links, or results that have not
been approved for public release.

## Create a discussion

1. Create a branch such as `discussion/2026-07-13-yifan-forcing-ar-video-distillation`.
2. Generate the entry:

   ```bash
   python3 scripts/new_discussion.py \
     --date 2026-07-13 \
     --leader yifan \
     --topic forcing-ar-video-distillation \
     --title "Forcing Series: The Evolution of AR Video Distillation"
   ```

3. Complete the summary, idea map, references, and metadata.
4. Rebuild and validate:

   ```bash
   python3 scripts/build_site.py
   python3 scripts/validate_site.py
   python3 -m unittest discover -s tests -v
   ```

5. Preview with `python3 -m http.server 8000` and inspect the changed pages.
6. Open a pull request at least one day before the meeting.

## Before-meeting quality bar

- Metadata, summary, idea map, and references are complete.
- At least three important references are analyzed, not merely listed.
- At least five open questions are provided.
- Central claim, hidden assumption, failure boundary, connection, concrete
  experiment, and discussion seed are explicit.
- Large videos are externally hosted; committed previews stay below 10 MiB.
- Public links and claims have been checked by the author.

## After the meeting

Update `meeting-note.md` and `action-items.md` within 48 hours. Record changed
views, insights, critiques, project connections, research opportunities, and
concrete experiments. Do not publish a raw transcript.

Change the metadata status from `before-meeting` to `after-meeting`, rebuild the
indexes, validate, and open a follow-up pull request.

## Review expectations

Reviewers check both correctness and research usefulness. A page should not be
approved merely because it is comprehensive; it should identify assumptions,
boundaries, connections, and testable ideas.

At least one CODEOWNER approval and all required automated checks should pass
before merge.
