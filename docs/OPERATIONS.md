# Website operations runbook

This runbook covers routine maintenance for the public CausalVideoGroup site.

## Weekly discussion workflow

Create a branch and generate the discussion:

```bash
git switch -c discussion/YYYY-MM-DD-leader-topic
python3 scripts/new_discussion.py \
  --date YYYY-MM-DD \
  --leader approved-short-name \
  --topic topic-slug \
  --title "Topic title"
```

Complete `metadata.yaml`, `summary.html`, `references.md`, and the idea map.
Use `presentation.html` for a large self-contained slide deck and keep
`summary.html` as the standard research-summary entry point.

Before opening a pull request:

```bash
python3 scripts/build_site.py
python3 scripts/validate_site.py
python3 -m unittest discover -s tests -v
python3 -m http.server 8000
```

## After the meeting

Within 48 hours:

1. Replace the pending notice in `meeting-note.md`.
2. Update `action-items.md` with owners and target dates.
3. Change status from `before-meeting` to `after-meeting`.
4. Rebuild, validate, test, preview, and open a pull request.

## Add a leader

Add the full name and unique short name to `data/people.yaml`. Short names are
public URL identifiers and should remain stable. Then rebuild indexes and add
the member's GitHub username to `.github/CODEOWNERS` when known.

## Add a project

```bash
python3 scripts/new_project.py \
  --slug project-slug \
  --title "Project title" \
  --leader approved-short-name
```

Replace every placeholder, set the correct status and tags, add public links,
then rebuild and validate. Discussion metadata can reference the project slug
through `related_projects`.

## Media policy

Keep committed preview video files below 10 MiB. Store large videos, model
weights, datasets, unpublished results, and internal experiments elsewhere.
Every file in this repository should be treated as public.

## Deployment

Pull requests run `.github/workflows/validate.yml`. A push to `main` runs
`.github/workflows/deploy.yml`, which builds, validates, tests, uploads a Pages
artifact, and deploys it to <https://causalvideogroup.github.io/>.

Check a failed deployment in the repository's Actions tab. Common causes are:

- generated indexes were not committed;
- a discussion fails `validate_site.py`;
- a local link points to a missing file;
- Pages is not configured to use GitHub Actions;
- the `github-pages` environment blocks deployment.

## Rollback

Do not rewrite shared history. Revert the problematic commit:

```bash
git revert <commit-sha>
git push origin main
```

The revert triggers a fresh Pages deployment. Confirm the Actions run succeeds
and check the affected public URL.

## Repository settings checklist

- Pages source: GitHub Actions.
- `main` requires a pull request and one approval.
- CODEOWNER review is required.
- `Validate / validate` is a required status check.
- Force pushes and branch deletion are blocked.
- Only approved organization members have write access.
