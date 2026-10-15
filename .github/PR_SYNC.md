# Profile PR synchronization

The workflow refreshes only the `PR-SYNC` region in the profile README. It runs
daily at 08:17 Asia/Shanghai (00:17 UTC), on relevant configuration changes, or
manually from [Actions](https://github.com/LeslieWylie/LeslieWylie/actions/workflows/sync-prs.yml).
GitHub may delay scheduled runs.

The job uses GitHub's automatic repository token; no personal token or external
service is needed. Local runs use the existing `gh` login:

```sh
python3 scripts/sync_prs.py
```

Only this user's public PRs in repositories owned by others are eligible. Draft,
closed-unmerged, excluded, withdrawn, and superseded proposals are omitted.
Each category considers its 100 most recently updated (merged) or created (open)
search results. The small showcase is selected by merge/creation time, with
featured work first and a per-project cap. New proposals use their live title.
Merged proposals move to the merged candidate pool; the display limit can mean
an older contribution is available through the “all merged” link instead.

Edit `pr-showcase.json` to change display limits, featured PRs, exclusions, or
project names. Featured status never overrides the PR's actual merge/open state.
The initial exclusion is a proposal whose correctness claim was withdrawn.

API errors stop the job before writing. Identical content produces no commit.
Only README.md is staged; unrelated manual edits remain outside the generated
region. A concurrent branch update makes the push fail instead of overwriting it.

GitHub disables public scheduled workflows after 60 days without repository
activity. If that occurs, re-enable this workflow from its Actions page. See
[GitHub's scheduling rules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule).
