#!/usr/bin/env python3
"""Sync official icons from the Iconify API, then rebuild the icon-based buttons.

* Icons are listed in .github/icons.json (name -> "prefix:icon").
* Each run downloads fresh copies into assets/icons/. If the network or API is
  unavailable the committed copies stay in place, so the profile never breaks.
* Buttons (contact, call-to-action, live-app pills, tech strip) are assembled from
  those icons into assets/*.svg and are served from the repo itself.

Standard library only. Set ICONS_OFFLINE=1 to skip the download step.
"""
import html
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CFG = json.load(open(os.path.join(ROOT, ".github", "icons.json"), encoding="utf-8"))
ICON_DIR = os.path.join(ROOT, "assets", "icons")
ASSET_DIR = os.path.join(ROOT, "assets")
ACCENT = CFG.get("accent", "58a6ff")
MONO = {"lucide", "simple-icons", "tabler", "mdi", "fa6-brands", "ph"}   # single-colour sets
API = "https://api.iconify.design"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONOFONT = "'SF Mono','Fira Code',Consolas,'Liberation Mono',monospace"


# ------------------------------------------------------------------ sync
def parse_spec(spec):
    base, _, color = spec.partition("|")
    prefix, _, name = base.partition(":")
    return prefix, name, (color or ACCENT)


def fetch(prefix, name, color):
    url = f"{API}/{prefix}/{name}.svg"
    if prefix in MONO:
        url += "?color=" + urllib.parse.quote("#" + color)
    last = None
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "profile-icon-sync"})
            with urllib.request.urlopen(req, timeout=15) as r:
                text = r.read().decode("utf-8")
            if text.lstrip().startswith("<svg") and "</svg>" in text and len(text) < 60000:
                return text
            last = ValueError("response was not an SVG")
        except Exception as exc:
            last = exc
        time.sleep(attempt + 1)
    raise RuntimeError(last)


def sync():
    os.makedirs(ICON_DIR, exist_ok=True)
    if os.environ.get("ICONS_OFFLINE") == "1":
        print("ICONS_OFFLINE=1: skipping download, using committed icons")
        return
    ok = bad = streak = 0
    for name, spec in CFG["icons"].items():
        if streak >= 3:  # API looks unreachable: stop early and keep the cached set
            bad += 1
            continue
        prefix, icon, color = parse_spec(spec)
        try:
            svg = fetch(prefix, icon, color)
            with open(os.path.join(ICON_DIR, f"{name}.svg"), "w", encoding="utf-8") as f:
                f.write(svg)
            ok += 1
            streak = 0
        except Exception as exc:
            bad += 1
            streak += 1
            print(f"  keeping cached {name}.svg ({spec}): {exc}", file=sys.stderr)
    print(f"icons refreshed: {ok}, kept cached: {bad}")


# ------------------------------------------------------------------ helpers
_uid = [0]


def place(name, x, y, size, recolor=None):
    """Inline an icon file as a nested <svg>, with its ids namespaced."""
    path = os.path.join(ICON_DIR, f"{name}.svg")
    if not os.path.exists(path):
        return ""
    svg = open(path, encoding="utf-8").read()
    vb = re.search(r'viewBox="([^"]+)"', svg).group(1)
    inner = svg[svg.index(">", svg.index("<svg")) + 1: svg.rindex("</svg>")]
    if recolor:
        inner = re.sub("#" + ACCENT, recolor, inner, flags=re.I)
    _uid[0] += 1
    uid = f"i{_uid[0]}"
    for old in set(re.findall(r'\bid="([^"]+)"', inner)):
        new = f"{uid}-{old}"
        inner = (inner.replace(f'id="{old}"', f'id="{new}"')
                      .replace(f"url(#{old})", f"url(#{new})")
                      .replace(f'href="#{old}"', f'href="#{new}"'))
    return f'<svg x="{x}" y="{y}" width="{size}" height="{size}" viewBox="{vb}">{inner}</svg>'


def text_w(s, px, mono=False, bold=False):
    return len(s) * px * (0.61 if mono else (0.6 if bold else 0.56))


def write(name, body):
    with open(os.path.join(ASSET_DIR, name), "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n' + body)


# ------------------------------------------------------------------ builders
def contact(fname, icon, title, sub):
    w, h = 252, 52
    t, s = html.escape(title), html.escape(sub)
    write(fname, f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{t}: {s}">
<rect x="1" y="1" width="{w-2}" height="{h-2}" rx="12" fill="#0b1224" stroke="#1e293b" stroke-width="1.5"><animate attributeName="stroke" values="#1e293b;#22d3ee;#1e293b" dur="4s" repeatCount="indefinite"/></rect>
<rect x="8" y="8" width="36" height="36" rx="9" fill="#111a33" stroke="#1e293b"/>
{place(icon, 15, 15, 22)}
<text x="58" y="24" font-family="{SANS}" font-size="15" font-weight="700" fill="#e2e8f0">{t}</text>
<text x="58" y="40" font-family="{MONOFONT}" font-size="10" fill="#94a3b8">{s}</text>
</svg>''')


def cta(fname, icon, title, sub, w, filled):
    h = 68
    t, s = html.escape(title), html.escape(sub)
    tc, sc, rc = ("#04060d", "#04060dcc", "#04060d") if filled else ("#e2e8f0", "#94a3b8", None)
    face = ('<rect x="3" y="3" width="%d" height="%d" rx="14" fill="url(#kg)"/>' % (w - 6, h - 6)) if filled else \
           ('<rect x="3" y="3" width="%d" height="%d" rx="14" fill="#0b1224" stroke="url(#kg)" stroke-width="2"/>' % (w - 6, h - 6))
    write(fname, f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{t}">
<defs>
  <linearGradient id="kg" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#22d3ee"/><stop offset="1" stop-color="#8b5cf6"/></linearGradient>
  <linearGradient id="ks" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".45"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
  <filter id="kb" x="-30%" y="-60%" width="160%" height="220%"><feGaussianBlur stdDeviation="6"/></filter>
  <clipPath id="kc"><rect x="3" y="3" width="{w-6}" height="{h-6}" rx="14"/></clipPath>
</defs>
<rect x="6" y="8" width="{w-12}" height="{h-16}" rx="14" fill="url(#kg)" opacity=".5" filter="url(#kb)"><animate attributeName="opacity" values=".25;.6;.25" dur="2.8s" repeatCount="indefinite"/></rect>
{face}
<g clip-path="url(#kc)"><rect x="-120" y="0" width="90" height="{h}" fill="url(#ks)" transform="skewX(-20)"><animate attributeName="x" from="-160" to="{w+80}" dur="3.6s" repeatCount="indefinite"/></rect></g>
{place(icon, 22, 22, 24, rc)}
<text x="60" y="31" font-family="{SANS}" font-size="17" font-weight="800" letter-spacing="2" fill="{tc}">{t}</text>
<text x="60" y="51" font-family="{MONOFONT}" font-size="12" fill="{sc}">{s}</text>
<g><animateTransform attributeName="transform" type="translate" values="0 0;7 0;0 0" dur="1.4s" repeatCount="indefinite"/>{place("arrow", w-52, 20, 28, rc)}</g>
</svg>''')


def tech(fname):
    items = [("AGPL-3.0", "license"), ("Python", "python"), ("FastAPI", "fastapi"),
             ("LangGraph", "langgraph"), ("Docker", "docker")]
    h, gap, x, parts = 36, 10, 0, []
    for label, icon in items:
        w = int(14 + 18 + 8 + text_w(label, 13, bold=True) + 16)
        parts.append(f'<rect x="{x+.5}" y=".5" width="{w-1}" height="{h-1}" rx="10" fill="#0b1224" stroke="#1e293b"/>'
                     f'{place(icon, x+14, 9, 18)}'
                     f'<text x="{x+40}" y="23" font-family="{SANS}" font-size="13" font-weight="600" fill="#e2e8f0">{html.escape(label)}</text>')
        x += w + gap
    total = x - gap
    write(fname, f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total} {h}" width="{total}" height="{h}" role="img" aria-label="AGPL-3.0, Python, FastAPI, LangGraph, Docker">' + "".join(parts) + "</svg>")


LIVE = [("IntelAI", "intelai"), ("DocIntel", "docintel"), ("RAGeval", "rageval"),
        ("AgentKit", "agentkit"), ("StreamPulse", "streampulse"), ("VoiceFlow", "voiceflow")]


def live(name, slug):
    h = 40
    w = int(14 + 16 + 8 + text_w(name, 14, bold=True) + 14 + 5 + 8 + text_w("LIVE", 10, mono=True) + 16)
    nx = 38
    dx = nx + text_w(name, 14, bold=True) + 14
    write(f"live-{slug}.svg", f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Open {html.escape(name)} live">
<rect x=".75" y=".75" width="{w-1.5}" height="{h-1.5}" rx="10" fill="#0b1224" stroke="#22d3ee" stroke-opacity=".45" stroke-width="1.5"/>
{place("external", 14, 12, 16)}
<text x="{nx}" y="25" font-family="{SANS}" font-size="14" font-weight="700" fill="#e2e8f0">{html.escape(name)}</text>
<circle cx="{dx+3:.1f}" cy="21" r="3" fill="#3fb950"><animate attributeName="opacity" values="1;.25;1" dur="1.8s" repeatCount="indefinite"/></circle>
<text x="{dx+11:.1f}" y="25" font-family="{MONOFONT}" font-size="10" letter-spacing="1" fill="#3fb950">LIVE</text>
</svg>''')


def build():
    contact("contact-email.svg", "email", "Email", "contact@yacineseybousiddo.me")
    contact("contact-linkedin.svg", "linkedin", "LinkedIn", "in/yacineseybousiddoai")
    contact("contact-portfolio.svg", "portfolio", "Portfolio", "yacineseybousiddo.me")
    cta("cta-portfolio.svg", "portfolio", "VIEW PORTFOLIO", "yacineseybousiddo.me", 330, False)
    cta("cta-contact.svg", "email", "GET IN TOUCH", "contact@yacineseybousiddo.me", 360, True)
    tech("tech-stack.svg")
    for name, slug in LIVE:
        live(name, slug)
    print("buttons rebuilt")


if __name__ == "__main__":
    sync()
    build()
