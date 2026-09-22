"""
Build the portfolio site.

Five real pages (index, about, experience, projects, contact), each carrying both
identities. The visitor's mode is read from ?mode=, falls back to what they chose
last, then to analyst. Nav links carry the mode so it survives navigation even
with JavaScript disabled.

    python3 build_site.py            -> writes into this folder
    python3 build_site.py <out_dir>  -> writes elsewhere
"""

import base64
import shutil
import sys
from pathlib import Path

from content import SHARED, MODES

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
ASSETS = OUT / "assets"

PAGES = [("index", "Home"), ("about", "About"), ("experience", "Experience"),
         ("projects", "Projects"), ("contact", "Contact")]


# --------------------------------------------------------------------- assets
def copy_figures():
    ASSETS.mkdir(parents=True, exist_ok=True)
    seen = {}
    for mode in MODES.values():
        for p in mode["projects"]:
            src = p.get("fig")
            if not src:
                p["img"] = None
                continue
            src = Path(src)
            if not src.exists():
                print(f"  ! missing figure: {src.name}")
                p["img"] = None
                continue
            name = f"{mode['key']}_{src.stem}{src.suffix}"
            if src not in seen:
                shutil.copy2(src, ASSETS / name)
                seen[src] = name
            p["img"] = f"assets/{seen[src]}"
    print(f"  copied {len(seen)} figures")


# ------------------------------------------------------------------------ css
CSS = """
*{box-sizing:border-box}
html{scroll-behavior:smooth}
:root{
  --accent:#990000;--accent-soft:#9900001a;--gold:#FFCC00;
  --ink:#0F172A;--muted:#64748B;--line:#E2E8F0;--bg:#fff;--card:#F8FAFC;
  --swap:380ms cubic-bezier(.4,0,.2,1);
}
body{margin:0;background:var(--bg);color:var(--ink);
  font:16px/1.65 -apple-system,BlinkMacSystemFont,'Segoe UI',Inter,Helvetica,Arial,sans-serif;
  -webkit-font-smoothing:antialiased;
  padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
img{max-width:100%}
.wrap{max-width:1040px;margin:0 auto;padding:0 24px}
a{color:var(--accent)}

header{position:sticky;top:env(safe-area-inset-top,0px);z-index:60;
  background:rgba(255,255,255,.85);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.bar{display:flex;align-items:center;gap:20px;height:66px}
.logo{font-weight:700;letter-spacing:-.02em;font-size:17px;white-space:nowrap;text-decoration:none;color:var(--ink)}
.logo b{color:var(--accent);transition:color var(--swap)}
nav{display:flex;gap:20px;margin-left:auto}
nav a{color:var(--muted);text-decoration:none;font-size:14.5px;font-weight:500;position:relative;padding:4px 0}
nav a::after{content:"";position:absolute;left:0;right:100%;bottom:0;height:2px;background:var(--gold);
  transition:right .25s ease,background var(--swap)}
nav a:hover{color:var(--ink)}nav a:hover::after,nav a.on::after{right:0}
nav a.on{color:var(--ink);font-weight:600}

.modes{display:flex;gap:2px;background:var(--card);border:1px solid var(--line);
  border-radius:999px;padding:3px;position:relative;flex-shrink:0}
.modes a{appearance:none;border:0;background:transparent;cursor:pointer;text-decoration:none;
  font:600 13px/1 inherit;color:var(--muted);padding:9px 15px;border-radius:999px;
  position:relative;z-index:2;transition:color 220ms ease;white-space:nowrap}
.modes a[aria-current="true"]{color:#fff}
.pill{position:absolute;top:3px;bottom:3px;border-radius:999px;background:var(--accent);
  transition:left var(--swap),width var(--swap),background var(--swap);z-index:1}

[data-swap]{transition:opacity 190ms ease,transform 190ms ease}
body.swapping [data-swap]{opacity:0;transform:translateY(7px)}

.hero{padding:82px 0 56px}
.eyebrow{display:inline-block;font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--accent);background:var(--accent-soft);padding:6px 13px;border-radius:999px;margin-bottom:22px;
  transition:color var(--swap),background var(--swap)}
h1{font-size:clamp(33px,5.2vw,54px);line-height:1.08;letter-spacing:-.033em;margin:0 0 18px;font-weight:700}
.rule{width:58px;height:5px;border-radius:3px;background:var(--gold);margin:0 0 22px;transition:background var(--swap)}
.lede{font-size:clamp(17px,2.05vw,19.5px);color:var(--muted);max-width:640px;margin:0 0 30px}
.cta{display:flex;gap:12px;flex-wrap:wrap}
.btn{display:inline-block;padding:12px 22px;border-radius:10px;text-decoration:none;font-weight:600;font-size:14.5px;
  transition:background var(--swap),border-color var(--swap),color var(--swap),transform .16s ease}
.btn:hover{transform:translateY(-1px)}
.btn-primary{background:var(--accent);color:#fff}
.btn-ghost{border:1px solid var(--line);color:var(--ink)}
.btn-ghost:hover{border-color:var(--accent);color:var(--accent)}

section{padding:52px 0;border-top:1px solid var(--line)}
.kicker{font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin-bottom:13px}
h2{font-size:clamp(23px,3vw,30px);letter-spacing:-.022em;margin:0 0 15px;font-weight:700}
h3{letter-spacing:-.015em}
.prose{font-size:17px;color:#334155;max-width:700px}
.prose p{margin:0 0 15px}

.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:18px;margin-top:24px}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:22px;
  display:flex;flex-direction:column;position:relative;overflow:hidden;text-decoration:none;color:inherit;
  transition:transform .2s ease,box-shadow .2s ease,border-color var(--swap)}
.card::before{content:'';position:absolute;top:0;left:0;right:100%;height:3px;background:var(--gold);
  transition:right .3s ease,background var(--swap)}
.card:hover::before{right:0}
.card:hover{transform:translateY(-3px);box-shadow:0 10px 26px -12px rgba(15,23,42,.24);border-color:var(--accent)}
.card .tag{font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--accent);
  margin-bottom:9px;transition:color var(--swap)}
.card h3{font-size:17.5px;margin:0 0 9px;line-height:1.3}
.card p{font-size:14.5px;color:var(--muted);margin:0 0 16px;flex:1}
.stat{font-size:25px;font-weight:700;color:var(--accent);letter-spacing:-.02em;transition:color var(--swap)}
.stat small{display:block;font-size:12px;font-weight:500;color:var(--muted);letter-spacing:0;margin-top:3px}

.entry{border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:26px;background:#fff}
.entry .shot{background:var(--card);border-bottom:1px solid var(--line);padding:20px;text-align:center}
.entry .shot img{border-radius:8px;display:block;margin:0 auto}
.entry .meat{padding:24px}
.entry h3{font-size:21px;margin:0 0 8px}
.entry .stack{font-size:12.5px;color:var(--muted);margin-bottom:14px}
.entry p{margin:0 0 16px;color:#334155}
.entry .figures{display:flex;gap:26px;flex-wrap:wrap;align-items:flex-end;margin-bottom:18px}

.xp{border-left:2px solid var(--line);padding-left:22px;margin-top:22px}
.xp-item{margin-bottom:28px;position:relative}
.xp-item::before{content:"";position:absolute;left:-28px;top:6px;width:11px;height:11px;border-radius:50%;
  background:var(--gold);border:2px solid var(--accent);transition:border-color var(--swap),background var(--swap)}
.xp-item h4{margin:0 0 2px;font-size:16.5px}
.xp-item .meta{font-size:13.5px;color:var(--muted);margin-bottom:9px}
.xp-item ul{margin:0;padding-left:18px}
.xp-item li{margin-bottom:7px;color:#334155;font-size:15px}

.grid2{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:20px;margin-top:22px}
.mini h4{margin:0 0 5px;font-size:15.5px}
.mini p{margin:0;font-size:14.5px;color:var(--muted)}

.note{margin-top:24px;padding:15px 17px;background:var(--card);border-left:3px solid var(--accent);
  border-radius:0 8px 8px 0;font-size:14.5px;color:#475569;transition:border-color var(--swap)}
footer{padding:38px 0 54px;color:var(--muted);font-size:14px;border-top:1px solid var(--line)}
footer a{color:var(--muted)}
.rows{margin-top:20px}
.row{display:flex;gap:16px;padding:13px 0;border-bottom:1px solid var(--line);font-size:15px;flex-wrap:wrap}
.row span:first-child{min-width:150px;color:var(--muted);font-weight:600}

@media(max-width:760px){
  nav{display:none}
  .bar{gap:12px}
  .modes a{padding:8px 11px;font-size:12px}
  .hero{padding:48px 0 38px}
}
"""

JS = """
const ACCENTS=%(accents)s;
function applyMode(m,animate){
  const c=ACCENTS[m]; if(!c) return;
  const go=()=>{
    document.documentElement.style.setProperty('--accent',c.accent);
    document.documentElement.style.setProperty('--accent-soft',c.accent+'1a');
    document.documentElement.style.setProperty('--gold',c.gold);
    document.querySelectorAll('[data-mode-block]').forEach(el=>{
      el.hidden = el.dataset.modeBlock!==m;
    });
    document.querySelectorAll('.modes a').forEach(a=>{
      const on=a.dataset.mode===m;
      a.setAttribute('aria-current',on);
      if(on) movePill(a);
    });
    document.querySelectorAll('a[data-keepmode]').forEach(a=>{
      try{const u=new URL(a.href,location.href);u.searchParams.set('mode',m);
          a.href=u.pathname.split('/').pop()+u.search;}catch(e){}
    });
    document.title=document.title.replace(/ — .*$/,'') + ' — ' + c.title;
    try{localStorage.setItem('mode',m)}catch(e){}
    try{const u=new URL(location.href);u.searchParams.set('mode',m);
        history.replaceState({},'',u);}catch(e){}
  };
  if(!animate){go();return;}
  document.body.classList.add('swapping');
  setTimeout(()=>{go();requestAnimationFrame(()=>document.body.classList.remove('swapping'))},190);
}
function movePill(a){const p=document.querySelector('.pill');if(!p)return;
  p.style.left=a.offsetLeft+'px';p.style.width=a.offsetWidth+'px';}
document.querySelector('.modes').addEventListener('click',e=>{
  const a=e.target.closest('a[data-mode]'); if(!a) return;
  e.preventDefault(); applyMode(a.dataset.mode,true);
});
let start=null;
try{start=new URL(location.href).searchParams.get('mode')}catch(e){}
if(!ACCENTS[start]){try{start=localStorage.getItem('mode')}catch(e){}}
applyMode(ACCENTS[start]?start:'analyst',false);
addEventListener('resize',()=>{const a=document.querySelector('.modes a[aria-current="true"]');if(a)movePill(a)});
"""


# ----------------------------------------------------------------- components
def nav(active):
    out = []
    for slug, label in PAGES:
        href = "index.html" if slug == "index" else f"{slug}.html"
        cls = ' class="on"' if slug == active else ""
        out.append(f'<a href="{href}"{cls} data-keepmode>{label}</a>')
    return "".join(out)


def switch():
    a = []
    for k, m in MODES.items():
        a.append(f'<a href="?mode={k}" data-mode="{k}">{m["label"]}</a>')
    return f'<div class="modes"><span class="pill"></span>{"".join(a)}</div>'


def shell(title, active, body):
    accents = "{" + ",".join(
        f'"{k}":{{accent:"{m["accent"]}",gold:"{m["gold"]}",title:"{m["nav_tag"].replace("&amp;", "&")}"}}'
        for k, m in MODES.items()) + "}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{SHARED['name']} — {title}</title>
<meta name="description" content="{SHARED['name']} — analytics portfolio.">
<style>{CSS}</style>
</head>
<body>
<header><div class="wrap bar">
  <a class="logo" href="index.html" data-keepmode>Simon <b>Chen</b></a>
  <nav>{nav(active)}</nav>
  {switch()}
</div></header>
<main class="wrap">
{body}
</main>
<footer class="wrap">
  <div>&copy; 2026 {SHARED['name']} ·
  <a href="{SHARED['github']}">GitHub</a> ·
  <a href="{SHARED['linkedin']}">LinkedIn</a> ·
  <a href="mailto:{SHARED['email']}">{SHARED['email']}</a></div>
</footer>
<script>{JS % {"accents": accents}}</script>
</body>
</html>"""


def per_mode(render):
    """Render a block once per mode; only the active one is shown."""
    return "".join(
        f'<div data-mode-block="{k}" hidden>{render(m)}</div>' for k, m in MODES.items())


def card(p):
    return f"""<a class="card" href="{p['repo']}">
  <div class="tag">{p['tag']}</div>
  <h3>{p['title']}</h3>
  <p>{p['desc']}</p>
  <div class="stat">{p['stat']}<small>{p['label']}</small></div>
</a>"""


def entry(p):
    shot = f'<div class="shot"><img src="{p["img"]}" alt="{p["title"]}"></div>' if p.get("img") else ""
    return f"""<div class="entry">{shot}
  <div class="meat">
    <div class="tag" style="font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--accent);margin-bottom:8px">{p['tag']}</div>
    <h3>{p['title']}</h3>
    <div class="stack">{p['stack']}</div>
    <div class="figures"><div class="stat">{p['stat']}<small>{p['label']}</small></div></div>
    <p>{p['body']}</p>
    <a class="btn btn-ghost" href="{p['repo']}">View the repository →</a>
  </div>
</div>"""


def xp_item(e):
    lis = "".join(f"<li>{b}</li>" for b in e["bullets"])
    return f"""<div class="xp-item">
  <h4>{e['org']}</h4>
  <div class="meta">{e['role']} · {e['place']} · {e['date']}</div>
  <ul>{lis}</ul>
</div>"""


# ---------------------------------------------------------------------- pages
def page_index():
    def hero(m):
        return f"""<div class="hero">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1>{m['headline']}</h1>
  <div class="rule"></div>
  <p class="lede">{m['lede']}</p>
  <div class="cta">
    <a class="btn btn-primary" href="projects.html" data-keepmode>Selected work</a>
    <a class="btn btn-ghost" href="about.html" data-keepmode>About me</a>
  </div>
</div>"""

    def feat(m):
        return f"""<div class="kicker">Selected work</div>
<h2>{m['proj_title']}</h2>
<p class="prose">{m['proj_lede']}</p>
<div class="cards">{''.join(card(p) for p in m['projects'][:3])}</div>
<div class="note">Three here, the rest on <a href="{SHARED['github']}">GitHub</a> —
a portfolio should be read, not scrolled past.</div>"""

    return shell("Analytics Portfolio", "index",
                 per_mode(hero) + "<section>" + per_mode(feat) + "</section>")


def page_about():
    def block(m):
        paras = "".join(f"<p>{p}</p>" for p in m["about"])
        minis = "".join(
            f'<div class="mini"><h4>{t}</h4><p>{d}</p></div>' for t, d in m["about_list"])
        skills = "".join(
            f'<div class="row"><span>{t}</span><span>{d}</span></div>' for t, d in m["skills"])
        return f"""<div class="hero" style="padding-bottom:30px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['about_title']}</h1>
  <div class="rule"></div>
</div>
<div class="prose">{paras}</div>
<section><div class="kicker">{m['about_kicker']}</div><div class="grid2">{minis}</div></section>
<section><div class="kicker">Skills</div><h2>What I work with</h2><div class="rows">{skills}</div></section>"""

    edu = "".join(f"""<div class="xp-item">
  <h4>{e['school']}</h4>
  <div class="meta">{e['degree']} · {e['place']} · {e['date']}</div>
  <ul><li>{e['note']}</li></ul>
</div>""" for e in SHARED["education"])

    return shell("About", "about",
                 per_mode(block) +
                 f'<section><div class="kicker">Education</div><h2>Where I trained</h2>'
                 f'<div class="xp">{edu}</div></section>')


def page_experience():
    def block(m):
        items = "".join(xp_item(e) for e in m["experience"])
        return f"""<div class="hero" style="padding-bottom:26px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['xp_title']}</h1>
  <div class="rule"></div>
</div>
<div class="xp">{items}</div>"""

    return shell("Experience", "experience", per_mode(block))


def page_projects():
    def block(m):
        return f"""<div class="hero" style="padding-bottom:26px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['proj_title']}</h1>
  <div class="rule"></div>
  <p class="lede">{m['proj_lede']}</p>
</div>
{''.join(entry(p) for p in m['projects'])}
<div class="note">Every project here has a repository with the code, the data where it can be
shared, and a full write-up. More at <a href="{SHARED['github']}">github.com/Semin1c</a>.</div>"""

    return shell("Projects", "projects", per_mode(block))


def page_contact():
    def block(m):
        return f"""<div class="hero" style="padding-bottom:26px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['contact_title']}</h1>
  <div class="rule"></div>
  <p class="lede">{m['contact_lede']}</p>
</div>"""

    rows = f"""<div class="rows">
  <div class="row"><span>Email</span><span><a href="mailto:{SHARED['email']}">{SHARED['email']}</a></span></div>
  <div class="row"><span>Phone</span><span>{SHARED['phone']}</span></div>
  <div class="row"><span>Location</span><span>{SHARED['location']}</span></div>
  <div class="row"><span>LinkedIn</span><span><a href="{SHARED['linkedin']}">linkedin.com/in/simonxy-chen</a></span></div>
  <div class="row"><span>GitHub</span><span><a href="{SHARED['github']}">github.com/Semin1c</a></span></div>
</div>"""
    return shell("Contact", "contact", per_mode(block) + rows)


BUILDERS = {"index": page_index, "about": page_about, "experience": page_experience,
            "projects": page_projects, "contact": page_contact}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    copy_figures()
    for slug, _ in PAGES:
        (OUT / f"{slug}.html").write_text(BUILDERS[slug]())
        print(f"  wrote {slug}.html")
    print(f"done -> {OUT}")
