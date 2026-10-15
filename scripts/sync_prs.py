#!/usr/bin/env python3
"""Refresh the profile's public upstream PR showcase with GitHub CLI auth."""

import html
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- PR-SYNC:START -->"
END = "<!-- PR-SYNC:END -->"
QUERY = """
query($search: String!) {
  search(query: $search, type: ISSUE, first: 100) {
    nodes {
      ... on PullRequest {
        title url number state isDraft createdAt mergedAt
        author { login }
        repository { nameWithOwner isPrivate owner { login } }
      }
    }
  }
}
"""


def fetch_prs(author, state):
    search = f"is:pr is:public author:{author} -user:{author} is:{state}"
    search += " sort:updated-desc" if state == "merged" else " draft:false sort:created-desc"
    result = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=json.dumps({"query": QUERY, "variables": {"search": search}}),
        text=True, capture_output=True, timeout=60,
    )
    if result.returncode:
        raise RuntimeError(f"GitHub query failed: {result.stderr.strip()}")
    response = json.loads(result.stdout)
    if response.get("errors"):
        raise RuntimeError("GitHub returned GraphQL errors; README was not changed")
    nodes = response["data"]["search"]["nodes"]
    expected = "MERGED" if state == "merged" else "OPEN"
    for pr in nodes:
        if pr["state"] != expected or pr["author"]["login"].lower() != author.lower():
            raise ValueError("Unexpected PR state or author; README was not changed")
    return nodes


def pr_key(pr):
    return f"{pr['repository']['nameWithOwner']}#{pr['number']}"


def select_prs(prs, config, state):
    author = config["author"].lower()
    excluded = set(config["exclude"])
    featured = set(config["featured"])
    candidates = [pr for pr in prs
                  if not pr["repository"]["isPrivate"]
                  and pr["repository"]["owner"]["login"].lower() != author
                  and not pr["isDraft"]
                  and pr_key(pr) not in excluded
                  and not re.search(r"\b(withdrawn|superseded|do not merge)\b", pr["title"], re.I)]
    timestamp = "mergedAt" if state == "merged" else "createdAt"
    candidates.sort(key=lambda pr: (pr_key(pr) in featured, pr[timestamp] or "", pr["url"]), reverse=True)
    limit = config["limits"][state]
    cap = config["per_project"][state]
    selected, counts = [], Counter()
    for pr in candidates:
        repo = pr["repository"]["nameWithOwner"]
        if counts[repo] < cap:
            selected.append(pr)
            counts[repo] += 1
        if len(selected) == limit:
            break
    return selected


def cell(value):
    value = html.escape(" ".join(value.split()), quote=False)
    return re.sub(r"([\\`*\[\]_])", r"\\\1", value).replace("|", "&#124;")


def search_link(author, state):
    query = f"is:pr author:{author} is:public is:{state} -user:{author}"
    return "https://github.com/pulls?" + urlencode({"q": query})


def table(prs, config, state):
    if not prs:
        return "No public upstream PRs to display in this category."
    heading = "Contribution" if state == "merged" else "Proposed change"
    rows = [f"| Project | {heading} | PR |", "| :--- | :--- | :--- |"]
    for pr in prs:
        repo = pr["repository"]["nameWithOwner"]
        name = config["project_names"].get(repo, repo)
        title = re.sub(r"^(?:\[(?:bugfix|fix|feat|feature|model|kernel|docs)\]\s*)+", "", pr["title"], flags=re.I)
        rows.append(f"| **{cell(name)}** | {cell(title)} | [#{pr['number']}]({pr['url']}) |")
    return "\n".join(rows)


def render(config, merged, opened):
    return "\n\n".join([
        "## Merged PRs",
        table(select_prs(merged, config, "merged"), config, "merged"),
        f"[All merged upstream PRs →]({search_link(config['author'], 'merged')})",
        "## Open PRs",
        "Selected open, non-draft proposals. Titles and status sync from GitHub daily.",
        table(select_prs(opened, config, "open"), config, "open"),
        f"[All open upstream PRs →]({search_link(config['author'], 'open')})",
        "[Automatic PR sync](https://github.com/LeslieWylie/LeslieWylie/actions/workflows/sync-prs.yml) · Daily at 08:17 Beijing time.",
    ])


def main():
    config = json.loads((ROOT / ".github/pr-showcase.json").read_text(encoding="utf-8"))
    readme_path = ROOT / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    if readme.count(START) != 1 or readme.count(END) != 1:
        raise ValueError("README must contain exactly one PR-SYNC marker pair")
    before, current = readme.split(START)
    current, after = current.split(END)
    merged = fetch_prs(config["author"], "merged")
    opened = fetch_prs(config["author"], "open")
    generated = "\n" + render(config, merged, opened) + "\n"
    if current == generated:
        print("PR showcase is unchanged")
        return
    readme_path.write_text(before + START + generated + END + after, encoding="utf-8")
    print("Updated PR showcase; content outside the markers was preserved")


if __name__ == "__main__":
    main()
