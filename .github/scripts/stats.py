"""Generate an animated GitHub stats card (SVG) using the GraphQL API.

Token: uses PAT (repo secret METRICS_TOKEN) when available, which unlocks private
contributions and private-repo language stats. Falls back to the built-in
GITHUB_TOKEN (public data only) if no PAT is set.

Privacy: only aggregate numbers are drawn. No private repo names, commit messages
or file names ever appear in the output.

Usage: python3 stats.py dist/github-stats.svg
"""
import datetime
import html
import json
import os
import sys
import urllib.request

USER = os.environ.get("GH_USER") or os.environ["GITHUB_REPOSITORY_OWNER"]
TOKENS = [t for t in (os.environ.get("PAT"), os.environ.get("GITHUB_TOKEN")) if t]
TOKEN = None  # set per attempt in main()
OUT = sys.argv[1] if len(sys.argv) > 1 else "dist/github-stats.svg"

PROFILE_Q = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection {
      totalCommitContributions
      totalIssueContributions
      totalPullRequestContributions
      totalPullRequestReviewContributions
      contributionCalendar {
        totalContributions
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}"""

REPOS_Q = """
query($login: String!, $after: String) {
  user(login: $login) {
    repositories(first: 100, after: $after) {
      pageInfo { hasNextPage endCursor }
      nodes {
        isPrivate
        stargazerCount
        forkCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
          edges { size node { name color } }
        }
      }
    }
  }
}"""


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "profile-stats",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        payload = json.load(r)
    if not payload.get("data"):
        raise RuntimeError(payload.get("errors"))
    return payload["data"]


if not TOKENS:
    sys.exit("No token available (set METRICS_TOKEN or provide GITHUB_TOKEN).")


def collect():
    user = gql(PROFILE_Q, {"login": USER})["user"]
    repos, cursor = [], None
    while True:
        page = gql(REPOS_Q, {"login": USER, "after": cursor})["user"]["repositories"]
        repos.extend(page["nodes"])
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]
    return user, repos


# ---------------------------------------------------------------- data
last_error = None
for TOKEN in TOKENS:
    try:
        user, repos = collect()
        break
    except Exception as exc:  # bad scope, expired token, API hiccup...
        last_error = exc
        print(f"Token attempt failed: {exc}", file=sys.stderr)
else:
    sys.exit(f"Could not fetch stats with any token. Last error: {last_error}\n"
             "Check that METRICS_TOKEN is a classic PAT with repo + read:user scopes and has not expired.")

cc = user["contributionsCollection"]
cal = cc["contributionCalendar"]
weeks = cal["weeks"]
days = [d for w in weeks for d in w["contributionDays"]]

stars = sum(r["stargazerCount"] for r in repos)
private = sum(1 for r in repos if r["isPrivate"])

langs, colors = {}, {}
for r in repos:
    for e in r["languages"]["edges"]:
        n = e["node"]["name"]
        langs[n] = langs.get(n, 0) + e["size"]
        if e["node"].get("color"):
            colors[n] = e["node"]["color"]
total_bytes = sum(langs.values()) or 1
top = sorted(langs.items(), key=lambda kv: kv[1], reverse=True)[:6]

# streaks
longest = run = 0
for d in days:
    run = run + 1 if d["contributionCount"] > 0 else 0
    longest = max(longest, run)
current = 0
seq = days[:]
if seq and seq[-1]["contributionCount"] == 0:  # today may not be finished yet
    seq = seq[:-1]
for d in reversed(seq):
    if d["contributionCount"] > 0:
        current += 1
    else:
        break

tiles = [
    ("Contributions", cal["totalContributions"], "#58a6ff"),
    ("Commits", cc["totalCommitContributions"], "#3fb950"),
    ("Pull requests", cc["totalPullRequestContributions"], "#a371f7"),
    ("Issues", cc["totalIssueContributions"], "#d29922"),
    ("Stars earned", stars, "#f2cc60"),
    ("Repositories", len(repos), "#79c0ff"),
    ("Current streak", f"{current} d", "#ff7b72"),
    ("Longest streak", f"{longest} d", "#f778ba"),
]

# ---------------------------------------------------------------- svg
W = 800
palette = ["#58a6ff", "#a371f7", "#3fb950", "#d29922", "#f778ba", "#ff7b72"]
heat = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
peak = max((d["contributionCount"] for d in days), default=0) or 1


def level(c):
    if c == 0:
        return 0
    r = c / peak
    return 1 if r <= 0.25 else 2 if r <= 0.5 else 3 if r <= 0.75 else 4


TILE_Y1, TILE_Y2, TILE_H = 76, 152, 64
HEAT_TITLE_Y, HEAT_Y = 252, 264
LANG_TITLE_Y, LANG_Y = 392, 408
H = LANG_Y + len(top) * 20 + 24

now = datetime.datetime.now(datetime.timezone.utc)
sub = f"@{html.escape(USER)} · last 12 months · updated {now:%Y-%m-%d} UTC"
if private:
    sub += f" · includes {private} private repo{'s' if private != 1 else ''} (aggregate only)"

p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="GitHub stats for {html.escape(USER)}">']
p.append("""<style>
  text { font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; }
  .title { font-size: 18px; font-weight: 600; fill: #e6edf3; }
  .h3    { font-size: 14px; font-weight: 600; fill: #e6edf3; }
  .sub   { font-size: 11px; fill: #7d8590; }
  .num   { font-size: 24px; font-weight: 700; fill: #e6edf3; }
  .lbl   { font-size: 11px; fill: #7d8590; text-transform: uppercase; letter-spacing: .6px; }
  .lang  { font-size: 12px; fill: #c9d1d9; }
  .pct   { font-size: 12px; fill: #7d8590; }
  .tile  { opacity: 0; animation: rise .6s ease-out forwards; }
  .col   { opacity: 0; animation: fade .5s ease-out forwards; }
  .bar   { transform-box: fill-box; transform-origin: left center; transform: scaleX(0); animation: grow 1s cubic-bezier(.2,.8,.2,1) forwards; }
  @keyframes rise { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }
  @keyframes fade { to { opacity: 1; } }
  @keyframes grow { to { transform: scaleX(1); } }
</style>""")
p.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="#0d1117" stroke="#30363d"/>')
p.append('<text class="title" x="30" y="38">GitHub at a glance</text>')
p.append(f'<text class="sub" x="30" y="56">{sub}</text>')

tw = (W - 60 - 3 * 14) / 4
for i, (label, value, accent) in enumerate(tiles):
    row, col = divmod(i, 4)
    x = 30 + col * (tw + 14)
    y = TILE_Y1 if row == 0 else TILE_Y2
    shown = f"{value:,}" if isinstance(value, int) else value
    p.append(f'<g class="tile" style="animation-delay:{i*0.08:.2f}s">')
    p.append(f'<rect x="{x:.1f}" y="{y}" width="{tw:.1f}" height="{TILE_H}" rx="8" fill="#161b22" stroke="#30363d"/>')
    p.append(f'<rect x="{x:.1f}" y="{y+14}" width="3" height="{TILE_H-28}" rx="1.5" fill="{accent}"/>')
    p.append(f'<text class="num" x="{x+18:.1f}" y="{y+34}">{html.escape(str(shown))}</text>')
    p.append(f'<text class="lbl" x="{x+18:.1f}" y="{y+53}">{html.escape(label)}</text>')
    p.append("</g>")

p.append(f'<text class="h3" x="30" y="{HEAT_TITLE_Y}">Contribution calendar</text>')
step = (W - 60) / max(len(weeks), 1)
cell = step - 2
for wi, w in enumerate(weeks):
    p.append(f'<g class="col" style="animation-delay:{wi*0.02:.2f}s">')
    for di, d in enumerate(w["contributionDays"]):
        p.append(
            f'<rect x="{30 + wi*step:.1f}" y="{HEAT_Y + di*step:.1f}" width="{cell:.1f}" height="{cell:.1f}" '
            f'rx="2" fill="{heat[level(d["contributionCount"])]}"><title>{d["date"]}: {d["contributionCount"]}</title></rect>'
        )
    p.append("</g>")

p.append(f'<text class="h3" x="30" y="{LANG_TITLE_Y}">Languages by code volume</text>')
bar_x, bar_w = 170, 510
for i, (name, size) in enumerate(top):
    y = LANG_Y + i * 20
    pct = size / total_bytes * 100
    w = max(4, bar_w * pct / 100)
    color = colors.get(name) or palette[i % len(palette)]
    p.append(f'<text class="lang" x="30" y="{y+11}">{html.escape(name)}</text>')
    p.append(f'<rect x="{bar_x}" y="{y}" width="{bar_w}" height="12" rx="6" fill="#21262d"/>')
    p.append(f'<rect class="bar" x="{bar_x}" y="{y}" width="{w:.1f}" height="12" rx="6" fill="{color}" style="animation-delay:{0.3+i*0.12:.2f}s"/>')
    p.append(f'<text class="pct" x="{bar_x+bar_w+12}" y="{y+11}">{pct:.1f}%</text>')
p.append("</svg>")

os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(p))
print(f"wrote {OUT}: {len(repos)} repos ({private} private), {cal['totalContributions']} contributions, top {[n for n, _ in top]}")
