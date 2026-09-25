"""Render a self-hosted GitHub statistics card (light + dark) for the profile README.

Uses only the GitHub GraphQL API, so the card never depends on a third-party
image service. Run by .github/workflows/profile-assets.yml.

    GITHUB_TOKEN=... python3 scripts/build_github_stats.py <output-dir>
"""
import json
import os
import sys
import urllib.request
from collections import Counter
from pathlib import Path

LOGIN = "UsmanGhias"
FONT = "'Segoe UI', -apple-system, BlinkMacSystemFont, Helvetica, Arial, sans-serif"
# Notebook and markup bytes would drown out the application languages.
IGNORED_LANGUAGES = {"Jupyter Notebook", "HTML", "CSS", "SCSS", "Less", "Makefile", "Dockerfile", "Shell", "Fluent"}
# Vendored upstream source (a full Odoo checkout) is not my own code.
EXCLUDED_REPOS = {"odoo"}

THEMES = {
    "light": dict(bg="#FAF7FB", line="#E8E1E8", ink="#202124", muted="#5F6368", track="#EFE7EE",
                  langs=["#714B67", "#9333EA", "#168BD2", "#22C7C7", "#F5B800", "#94A3B8"], g1="#714B67", g2="#9333EA", g3="#168BD2"),
    "dark": dict(bg="#161B22", line="#30363D", ink="#F0F6FC", muted="#9DA7B3", track="#21262D",
                 langs=["#C58DB8", "#C084FC", "#58B4EE", "#22C7C7", "#F5B800", "#94A3B8"], g1="#D9A6CC", g2="#C084FC", g3="#58B4EE"),
}

QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection {
      contributionCalendar { totalContributions }
      totalCommitContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
    }
    repositoriesContributedTo(first: 1, contributionTypes: [COMMIT, PULL_REQUEST],
                              includeUserRepositories: false) { totalCount }
    repositories(first: 100, after: $cursor, ownerAffiliations: OWNER, isFork: false,
                 privacy: PUBLIC) {
      totalCount
      pageInfo { hasNextPage endCursor }
      nodes {
        name
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name } }
        }
      }
    }
  }
}
"""


def graphql(token, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {token}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if "errors" in body:
        raise RuntimeError(body["errors"])
    return body["data"]["user"]


def collect(token):
    cursor, langs, first = None, Counter(), None
    while True:
        user = graphql(token, {"login": LOGIN, "cursor": cursor})
        first = first or user
        repos = user["repositories"]
        for repo in repos["nodes"]:
            if repo["name"] in EXCLUDED_REPOS:
                continue
            for edge in repo["languages"]["edges"]:
                if edge["node"]["name"] not in IGNORED_LANGUAGES:
                    langs[edge["node"]["name"]] += edge["size"]
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    cc = first["contributionsCollection"]
    return {
        "metrics": [
            (f'{cc["contributionCalendar"]["totalContributions"]:,}', "Contributions (last year)"),
            (f'{cc["totalCommitContributions"]:,}', "Commits (last year)"),
            (f'{cc["totalPullRequestContributions"]:,}', "Pull requests (last year)"),
            (f'{first["repositoriesContributedTo"]["totalCount"]}', "External repos contributed to"),
            (f'{first["repositories"]["totalCount"]}', "Public repositories"),
            (f'{first["followers"]["totalCount"]}', "Followers"),
        ],
        "languages": langs.most_common(6),
    }


def card(data, t):
    w, h = 1280, 250
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
           f'role="img" aria-label="GitHub statistics for {LOGIN}">',
           f'<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{t["g1"]}"/>'
           f'<stop offset=".55" stop-color="{t["g2"]}"/><stop offset="1" stop-color="{t["g3"]}"/></linearGradient></defs>',
           f'<rect x=".5" y=".5" width="{w - 1}" height="{h - 1}" rx="18" fill="{t["bg"]}" stroke="{t["line"]}"/>',
           f'<g font-family="{FONT}">',
           f'<text x="40" y="52" font-size="18" font-weight="700" fill="{t["ink"]}">GitHub activity</text>',
           f'<text x="700" y="52" font-size="18" font-weight="700" fill="{t["ink"]}">Most used languages</text>',
           f'<line x1="660" y1="36" x2="660" y2="214" stroke="{t["line"]}"/>']
    # 3 x 2 metric grid on the left
    for i, (value, label) in enumerate(data["metrics"]):
        x, y = 40 + (i % 3) * 205, 110 + (i // 3) * 82
        out.append(f'<text x="{x}" y="{y}" font-size="30" font-weight="800" fill="url(#g)">{value}</text>'
                   f'<text x="{x}" y="{y + 24}" font-size="13" font-weight="600" fill="{t["muted"]}">{label}</text>')
    # stacked language bar + legend on the right
    langs = data["languages"]
    total = sum(size for _, size in langs) or 1
    bar_x, bar_w, x = 700, 540, 700.0
    out.append(f'<rect x="{bar_x}" y="78" width="{bar_w}" height="12" rx="6" fill="{t["track"]}"/>')
    out.append(f'<clipPath id="bar"><rect x="{bar_x}" y="78" width="{bar_w}" height="12" rx="6"/></clipPath><g clip-path="url(#bar)">')
    for i, (_, size) in enumerate(langs):
        seg = bar_w * size / total
        out.append(f'<rect x="{x:.1f}" y="78" width="{seg:.1f}" height="12" fill="{t["langs"][i]}"/>')
        x += seg
    out.append('</g>')
    for i, (name, size) in enumerate(langs):
        lx, ly = 700 + (i % 2) * 270, 132 + (i // 2) * 34
        out.append(f'<circle cx="{lx + 6}" cy="{ly - 5}" r="6" fill="{t["langs"][i]}"/>'
                   f'<text x="{lx + 20}" y="{ly}" font-size="15" font-weight="600" fill="{t["ink"]}">{name}'
                   f'<tspan fill="{t["muted"]}" font-weight="500">  {100 * size / total:.1f}%</tspan></text>')
    out.append('</g></svg>\n')
    return "".join(out)


def main():
    out_dir = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    out_dir.mkdir(parents=True, exist_ok=True)
    data = collect(os.environ["GITHUB_TOKEN"])
    for name, theme in THEMES.items():
        (out_dir / f"github-stats-{name}.svg").write_text(card(data, theme))
    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()
