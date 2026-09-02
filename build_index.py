"""
Build the soccer portfolio index page.

    python3 build_index.py <output_dir>

Writes index.html with the three project charts base64-embedded, so the page is
a single self-contained file with no asset paths to break.
"""

import base64
import sys
from pathlib import Path

BASE = Path("/Users/7ang/Desktop/Github Academic Project")

PROJECTS = [
    dict(
        accent="#2E9E5B",
        eyebrow="Major League Soccer · Europe's big five · 2010–2024",
        title="MLS Has More Parity Than Europe's Big Five",
        lede="Fourteen seasons, six leagues, and two definitions of “competitive” "
             "that point in opposite directions.",
        body="On competitive balance, MLS beats every one of Europe's big five on two "
             "independent measures — and the finding survives splitting the conferences "
             "and resampling for league size. A classifier reported at 88–90% accuracy "
             "turned out to be riding an 85.6% majority class; corrected, it reaches "
             "AUC 0.954.",
        stats=[("0.315", "points-per-match spread, lowest of six"),
               ("11 of 14", "seasons MLS is the most equal league"),
               ("25.5 pts", "home advantage, outside the European range")],
        repo="https://github.com/Semin1c/mls-vs-european-leagues",
        chart=BASE / "DSO 579 - MLS vs European League Analysis (2025 Spring)"
                   / "Git Version/figures/competitive_balance.png",
    ),
    dict(
        accent="#A4133C",
        eyebrow="La Liga · 2023–24 · 380 matches",
        title="Home Advantage Is Real — the Crowd Isn't Why",
        lede="Four explanations for the home edge went in. One came out.",
        body="Home sides create 1.484 expected goals to 1.121, but convert at an "
             "identical rate — the advantage is territorial, not finishing. Attendance "
             "predicts home points until you control for who fills big stadiums, then "
             "it is nothing. Referee spread and the club finishing table both sit inside "
             "what chance alone produces.",
        stats=[("+0.364 xG", "home edge, after controlling for club quality"),
               ("p = 0.54", "crowd effect once quality is held constant"),
               ("47%", "of random shuffles match the referee spread")],
        repo="https://github.com/Semin1c/laliga-home-advantage",
        chart=BASE / "DSO 579 - First Goal Scoring Analysis (2025 Spring)"
                   / "Git Version/figures/home_advantage_source.png",
    ),
    dict(
        accent="#00A87E",
        eyebrow="Premier League · 2017–18 to 2024–25 · 160 squads, 4,343 players",
        title="What Follows a Player to a New Club",
        lede="Possession doesn't create chances. And the number clubs scout on "
             "doesn't survive a transfer.",
        body="One variable — touches in the opposition box — matches all 23 possession "
             "metrics combined, and beats them on clubs the model has never seen. At "
             "player level, tracking 168 intra-league transfers, what a player does "
             "carries across a move; what it produced mostly doesn't.",
        stats=[("0.850 vs 0.848", "one variable against all 23 metrics"),
               ("r = 0.71", "final-third touches survive a transfer"),
               ("r = 0.26", "expected goals + assists do not")],
        repo="https://github.com/Semin1c/pl-possession-and-box-entry",
        chart=BASE / "DSO 579 - Premier League Possession Analysis (2025 Spring)"
                   / "Git Version/figures/what_survives_a_transfer.png",
    ),
]

CSS = """
:root{--ink:#0F1B2A;--muted:#5A6675;--line:#E3E7EC;--bg:#FFFFFF;--panel:#F7F9FB;}
@media (prefers-color-scheme:dark){
  :root{--ink:#E8EDF3;--muted:#9AA7B5;--line:#243040;--bg:#0D141C;--panel:#141C26;}
}
*{box-sizing:border-box;}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16.5px/1.7 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;}
.wrap{max-width:860px;margin:0 auto;padding:4.5rem 1.5rem 6rem;}
header{border-bottom:1px solid var(--line);padding-bottom:2.4rem;margin-bottom:1rem;}
h1{font-size:2.5rem;line-height:1.15;letter-spacing:-.025em;margin:0 0 .7rem;font-weight:760;}
.sub{font-size:1.12rem;color:var(--muted);margin:0 0 1.5rem;max-width:60ch;}
.meta{display:flex;flex-wrap:wrap;gap:.5rem 1.4rem;font-size:.94rem;color:var(--muted);}
.meta a{color:inherit;text-decoration:none;border-bottom:1px solid var(--line);}
.meta a:hover{color:var(--ink);border-color:var(--ink);}
.note{font-size:.94rem;color:var(--muted);margin:2.6rem 0 0;padding-top:1.6rem;
  border-top:1px solid var(--line);}
article{padding:3.4rem 0;border-bottom:1px solid var(--line);}
.eyebrow{font-size:.79rem;letter-spacing:.09em;text-transform:uppercase;font-weight:680;
  margin:0 0 .75rem;}
h2{font-size:1.62rem;line-height:1.25;letter-spacing:-.015em;margin:0 0 .6rem;font-weight:730;}
.lede{font-size:1.08rem;margin:0 0 1.1rem;max-width:62ch;}
.body{color:var(--muted);margin:0 0 1.7rem;max-width:64ch;}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1.2rem;
  margin:0 0 1.9rem;padding:1.3rem 1.4rem;background:var(--panel);border-radius:10px;}
.stat b{display:block;font-size:1.32rem;line-height:1.2;letter-spacing:-.01em;
  font-variant-numeric:tabular-nums;margin-bottom:.22rem;}
.stat span{font-size:.87rem;color:var(--muted);line-height:1.45;display:block;}
img{display:block;width:100%;height:auto;border:1px solid var(--line);border-radius:9px;
  margin:0 0 1.8rem;}
.cta{display:inline-flex;align-items:center;gap:.5rem;font-weight:640;font-size:.97rem;
  text-decoration:none;padding:.62rem 1.15rem;border-radius:8px;color:#fff;}
.cta:hover{filter:brightness(1.08);}
footer{padding-top:2.8rem;font-size:.94rem;color:var(--muted);}
footer a{color:inherit;}
@media(max-width:560px){.wrap{padding:3rem 1.15rem 4rem;}h1{font-size:2rem;}h2{font-size:1.4rem;}}
"""


def embed(path: Path) -> str:
    return "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode()


def main():
    out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    out.mkdir(parents=True, exist_ok=True)

    cards = []
    for p in PROJECTS:
        stats = "\n".join(
            f'<div class="stat"><b style="color:{p["accent"]}">{v}</b>'
            f'<span>{label}</span></div>' for v, label in p["stats"])
        cards.append(f"""
<article>
  <p class="eyebrow" style="color:{p['accent']}">{p['eyebrow']}</p>
  <h2>{p['title']}</h2>
  <p class="lede">{p['lede']}</p>
  <p class="body">{p['body']}</p>
  <div class="stats">{stats}</div>
  <img src="{embed(p['chart'])}" alt="{p['title']}">
  <a class="cta" style="background:{p['accent']}" href="{p['repo']}">
    View the analysis &rarr;</a>
</article>""")

    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Xingyang (Simon) Chen — Soccer Analytics</title>
<meta name="description" content="Three soccer analytics projects: competitive balance
across MLS and Europe's big five, where home advantage comes from in La Liga, and which
possession metrics survive a transfer.">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header>
  <h1>Xingyang (Simon) Chen</h1>
  <p class="sub">Soccer analytics — competitive balance, home advantage, and what
  possession data can and cannot tell you about a player.</p>
  <div class="meta">
    <span>MS Business Analytics, USC Marshall</span>
    <a href="mailto:xingyang@marshall.usc.edu">xingyang@marshall.usc.edu</a>
    <a href="https://github.com/Semin1c">github.com/Semin1c</a>
  </div>
  <p class="note">Three projects. Each one rebuilt from its raw data, with the code and
  every figure reproducible from the repository. In all three the original headline
  number turned out to be an artefact — of class imbalance, of a mislabelled column, of
  a preprocessing choice — and finding that is most of what the work is.</p>
</header>
{"".join(cards)}
<footer>
  <p>Built from coursework at USC Marshall and rebuilt independently. Data from FBref
  and Sports Reference.</p>
</footer>
</div>
</body>
</html>
"""
    (out / "index.html").write_text(html, encoding="utf-8")
    size = (out / "index.html").stat().st_size / 1024
    print(f"wrote {out / 'index.html'} ({size:.0f} KB)")


if __name__ == "__main__":
    main()
