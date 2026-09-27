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
.greet{font-size:clamp(17px,2.2vw,21px);color:var(--muted);margin:0 0 6px;font-weight:500}
.greet .zh{color:var(--accent);font-weight:700;transition:color var(--swap)}
.role{font-size:clamp(15px,1.9vw,18px);font-weight:600;color:var(--accent);margin:0 0 20px;
  letter-spacing:.01em;transition:color var(--swap)}
.brings{display:grid;gap:0;margin-top:26px;border-top:1px solid var(--line)}
.bring{display:grid;grid-template-columns:38px 1fr;gap:18px;padding:22px 0;border-bottom:1px solid var(--line);
  align-items:start}
.bring .n{font-size:14px;font-weight:700;color:var(--accent);padding-top:2px;transition:color var(--swap);
  font-variant-numeric:tabular-nums}
.bring h4{margin:0 0 6px;font-size:17px;letter-spacing:-.012em}
.bring p{margin:0;color:var(--muted);font-size:15.5px;max-width:640px}
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
.took{border-top:1px solid var(--line);padding-top:13px;font-size:14px;color:#475569;line-height:1.55}
.took span{display:block;font-size:10.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;
  color:var(--accent);margin-bottom:5px;transition:color var(--swap)}
.entry .took{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--gold);
  border-radius:0 10px 10px 0;padding:15px 17px;margin-top:4px}

.entry{border:1px solid var(--line);border-radius:14px;overflow:hidden;margin-bottom:26px;background:#fff}
.entry .shot{background:var(--card);border-bottom:1px solid var(--line);padding:20px;text-align:center}
.entry .shot img{border-radius:8px;display:block;margin:0 auto}
.entry .meat{padding:24px}
.entry h3{font-size:21px;margin:0 0 8px}
.entry .stack{font-size:12.5px;color:var(--muted);margin-bottom:14px}
.entry p{margin:0 0 16px;color:#334155}
.entry .figures{display:flex;gap:26px;flex-wrap:wrap;align-items:flex-end;margin-bottom:18px}

.xp{margin-top:26px}
.job{display:grid;grid-template-columns:132px 1fr;gap:22px;padding:22px;margin:0 -22px 6px;
  border-radius:12px;transition:background .2s ease}
.job:hover{background:var(--card)}
.job .when{font-size:12.5px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;
  color:var(--muted);padding-top:4px}
.job.edu h4 .at{color:var(--muted)}
.affil{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 4px}
.aff{border:1px solid var(--line);border-radius:10px;padding:11px 15px;background:var(--card);
  transition:border-color .2s ease,transform .2s ease}
.aff:hover{border-color:var(--accent);transform:translateY(-2px)}
.aff b{display:block;font-size:14px;letter-spacing:-.01em}
.aff span{font-size:12px;color:var(--muted)}
.now{border:1px solid var(--line);border-radius:14px;padding:26px 28px;background:var(--card);margin-top:26px}
.now .nowhead{display:flex;align-items:baseline;gap:11px;margin-bottom:18px;flex-wrap:wrap}
.now h3{margin:0;font-size:18px;letter-spacing:-.015em}
.now .when{font-size:12px;color:var(--muted)}
.now .dot{width:8px;height:8px;border-radius:50%;background:#16A34A;display:inline-block;
  box-shadow:0 0 0 3px #16A34A22}
.nowlist{display:grid;gap:13px}
.nowrow{display:grid;grid-template-columns:104px 1fr;gap:16px;align-items:baseline}
.nowrow dt{font-size:12.5px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.nowrow dd{margin:0;font-size:15.5px;color:#334155}
.portrait{width:150px;height:150px;border-radius:16px;object-fit:cover;border:1px solid var(--line);
  float:right;margin:0 0 20px 26px;background:var(--card)}
.portrait.ph{display:flex;align-items:center;justify-content:center;font-size:12.5px;color:var(--muted);
  text-align:center;padding:14px;line-height:1.45}
@media(max-width:620px){.nowrow{grid-template-columns:1fr;gap:3px}
  .portrait{float:none;margin:0 0 20px}}
.faq{margin-top:24px;border-top:1px solid var(--line)}
.q{border-bottom:1px solid var(--line)}
.q summary{cursor:pointer;padding:19px 34px 19px 0;font-size:16.5px;font-weight:600;
  list-style:none;position:relative;letter-spacing:-.012em}
.q summary::-webkit-details-marker{display:none}
.q summary::after{content:'+';position:absolute;right:4px;top:17px;font-size:21px;font-weight:400;
  color:var(--accent);transition:transform .25s ease}
.q[open] summary::after{transform:rotate(45deg)}
.q .a{padding:0 30px 20px 0;color:#475569;font-size:15.5px;max-width:680px}
.job h4{margin:0 0 9px;font-size:17px;letter-spacing:-.012em}
.job h4 .at{color:var(--accent);transition:color var(--swap)}
.job p{margin:0 0 13px;color:#475569;font-size:15.5px}
.chips{display:flex;flex-wrap:wrap;gap:7px}
.chip{font-size:12px;font-weight:600;color:var(--accent);background:var(--accent-soft);
  padding:5px 10px;border-radius:999px;transition:color var(--swap),background var(--swap)}
.todo{display:block;background:#FEF9C3;border-left:3px solid #CA8A04;padding:13px 15px;
  border-radius:0 8px 8px 0;font-size:14.5px;color:#713F12;font-style:italic}

/* ---- edit mode: add ?edit=1 to any page ---- */
body.editing [data-ed]{outline:1px dashed #94A3B8;outline-offset:4px;border-radius:3px}
body.editing [data-ed]:hover{outline-color:var(--accent);background:#FFFBEB}
body.editing [data-ed]:focus{outline:2px solid var(--accent);background:#fff}
body.editing [data-ed].dirty{background:#ECFDF5;outline-color:#059669}
#edbar{position:fixed;left:0;right:0;bottom:0;z-index:999;display:flex;align-items:center;gap:14px;
  padding:12px 20px;background:#0F172A;color:#fff;font-size:13.5px;
  padding-bottom:calc(12px + env(safe-area-inset-bottom,0px))}
#edbar b{color:var(--gold)}
#edbar .sp{margin-left:auto;display:flex;gap:9px}
#edbar button{font:600 13px/1 inherit;padding:9px 15px;border-radius:8px;border:0;cursor:pointer}
#edbar .save{background:var(--gold);color:#0F172A}
#edbar .reset{background:transparent;color:#94A3B8;border:1px solid #334155}
.post{display:block;text-decoration:none;color:inherit;padding:22px;margin:0 -22px;
  border-radius:12px;border-bottom:1px solid var(--line);transition:background .2s ease}
.post:hover{background:var(--card)}
.post .head{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-bottom:7px}
.post h3{font-size:19px;margin:0;letter-spacing:-.015em}
.post .status{font-size:11px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;
  color:var(--muted);border:1px solid var(--line);padding:3px 8px;border-radius:999px}
.post p{margin:0;color:var(--muted);font-size:15px;max-width:660px}

/* native web chart — scales crisply, picks up the mode accent, animates in */
.viz{padding:30px 28px;background:var(--card);border-bottom:1px solid var(--line)}
.viz .vtitle{font-size:15px;font-weight:700;letter-spacing:-.01em;margin-bottom:3px}
.viz .vsub{font-size:13px;color:var(--muted);margin-bottom:20px}
.bars{display:grid;gap:11px}
.brow{display:grid;grid-template-columns:118px 1fr 62px;align-items:center;gap:14px}
.brow .bl{font-size:13.5px;color:var(--muted);text-align:right;font-weight:500}
.btrack{background:#E7EBF0;border-radius:5px;height:24px;overflow:hidden}
.bfill{height:100%;border-radius:5px;background:#C3CAD3;width:0;
  transition:width 1.1s cubic-bezier(.22,1,.36,1)}
.brow.hot .bl{color:var(--ink);font-weight:700}
.brow.hot .bfill{background:var(--accent)}
.brow .bv{font-size:15px;font-weight:700;color:var(--muted);font-variant-numeric:tabular-nums}
.brow.hot .bv{color:var(--accent)}
.vnote{margin-top:18px;font-size:13.5px;color:#475569;border-left:3px solid var(--gold);padding-left:12px}
@media(max-width:620px){.brow{grid-template-columns:96px 1fr 54px;gap:9px}.brow .bl{font-size:12px}}

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
  .job{grid-template-columns:1fr;gap:8px;padding:18px;margin:0 0 10px}
  .job .when{padding-top:0}
  .bar{gap:12px}
  .modes a{padding:8px 11px;font-size:12px}
  .hero{padding:48px 0 38px}
}
"""

JS = """
const ACCENTS=__ACCENTS__;
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
    let ed=null; try{ed=new URL(location.href).searchParams.get('edit')}catch(e){}
    document.querySelectorAll('a[data-keepmode]').forEach(a=>{
      try{const u=new URL(a.href,location.href);u.searchParams.set('mode',m);
          if(ed==='1') u.searchParams.set('edit','1');
          a.href=u.pathname.split('/').pop()+u.search;}catch(e){}
    });
    document.title=document.title.replace(/ — .*$/,'') + ' — ' + c.title;
    try{localStorage.setItem('mode',m)}catch(e){}
    try{const u=new URL(location.href);u.searchParams.set('mode',m);
        if(ed==='1') u.searchParams.set('edit','1');
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
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){
  e.target.querySelectorAll('.bfill').forEach((b,i)=>setTimeout(()=>b.style.width=b.dataset.w+'%',i*70));
  io.unobserve(e.target);}}),{threshold:.35});
document.querySelectorAll('.viz').forEach(v=>io.observe(v));

/* ---------------- edit mode ---------------- */
(function(){
  let on=false; try{on=new URL(location.href).searchParams.get('edit')==='1'}catch(e){}
  if(!on) return;
  const PAGE=(location.pathname.split('/').pop()||'index.html').replace('.html','')||'index';
  const INLINE=new Set(['EM','STRONG','B','I','SPAN','A','SMALL','CODE','BR','SUP','SUB','MARK']);
  const SKIP=new Set(['SCRIPT','STYLE','SVG','PATH','IMG','BUTTON']);
  /* key off the original wording, so edits survive layout changes */
  function sig(s){let h=0;s=s.replace(/\s+/g,' ').trim().slice(0,160);
    for(let i=0;i<s.length;i++){h=(h*31+s.charCodeAt(i))|0}return (h>>>0).toString(36);}

  function scan(){
    document.querySelectorAll('[data-mode-block]').forEach(blk=>{
      const m=blk.dataset.modeBlock;
      blk.querySelectorAll('*').forEach(el=>{
        if(el.dataset.ed) return;
        if(SKIP.has(el.tagName)) return;
        if(el.closest('#edbar')) return;
        if(el.classList.contains('btrack')||el.classList.contains('bfill')) return;
        const txt=el.textContent.trim();
        if(!txt) return;
        const blocked=[...el.children].some(c=>!INLINE.has(c.tagName)&&c.textContent.trim());
        if(blocked) return;
        const k='ed:'+PAGE+':'+m+':'+sig(txt);
        el.dataset.ed=k; el.contentEditable='true'; el.spellcheck=true;
        const saved=localStorage.getItem(k);
        if(saved!==null&&saved!==el.innerHTML){el.innerHTML=saved;el.classList.add('dirty');}
        el.addEventListener('input',()=>{localStorage.setItem(k,el.innerHTML);el.classList.add('dirty');});
        el.addEventListener('keydown',e=>{if(e.key==='Enter'&&!e.shiftKey&&el.tagName!=='P'){e.preventDefault();el.blur();}});
      });
    });
  }
  document.body.classList.add('editing'); scan();
  new MutationObserver(scan).observe(document.body,{subtree:true,attributes:true,attributeFilter:['hidden']});

  const bar=document.createElement('div'); bar.id='edbar';
  const n=()=>Object.keys(localStorage).filter(k=>k.startsWith('ed:')).length;
  bar.innerHTML='<span><b>Edit mode</b> — click any text and type. <i id="edn"></i></span>'+
    '<span class="sp"><button class="reset">Discard all</button>'+
    '<button class="save">Download my edits</button></span>';
  document.body.appendChild(bar);
  const tick=()=>document.getElementById('edn').textContent=n()+' edited so far, saved in this browser.';
  tick(); setInterval(tick,1500);
  bar.querySelector('.save').onclick=()=>{
    const out={};
    Object.keys(localStorage).filter(k=>k.startsWith('ed:')).forEach(k=>out[k]=localStorage.getItem(k));
    const a=document.createElement('a');
    a.href=URL.createObjectURL(new Blob([JSON.stringify(out,null,2)],{type:'application/json'}));
    a.download='simon-site-edits.json'; a.click();
  };
  bar.querySelector('.reset').onclick=()=>{
    if(!confirm('Discard every edit saved in this browser?')) return;
    Object.keys(localStorage).filter(k=>k.startsWith('ed:')).forEach(k=>localStorage.removeItem(k));
    location.reload();
  };
})();
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
<script>{JS.replace("__ACCENTS__", accents)}</script>
</body>
</html>"""


def per_mode(render):
    """Render a block once per mode; only the active one is shown."""
    return "".join(
        f'<div data-mode-block="{k}" hidden>{render(m)}</div>' for k, m in MODES.items())


def card(p):
    return f"""<a class="card" href="{p['repo']}">
  <div class="tag">{p['tag']}</div>
  <h3>{p['question']}</h3>
  <p>{p['desc']}</p>
  <div class="took"><span>What I took from it</span>{p['took']}</div>
</a>"""


def entry(p):
    if p.get("viz"):
        shot = barchart(p["viz"])
    elif p.get("img"):
        shot = f'<div class="shot"><img src="{p["img"]}" alt="{p["title"]}"></div>'
    else:
        shot = ""
    return f"""<div class="entry">{shot}
  <div class="meat">
    <div class="tag" style="font-size:11.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--accent);margin-bottom:8px">{p['tag']}</div>
    <h3>{p['question']}</h3>
    <div class="stack">{p['title']} · {p['stack']}</div>
    <p>{p['body']}</p>
    <div class="took"><span>What I took from it</span>{p['took']}</div>
    <a class="btn btn-ghost" href="{p['repo']}">View the repository →</a>
  </div>
</div>"""


def xp_item(e):
    chips = "".join(f'<span class="chip">{c}</span>' for c in e.get("tags", []))
    return f"""<div class="job">
  <div class="when">{e['date']}</div>
  <div>
    <h4>{e['role']} <span class="at">· {e['org']}</span></h4>
    <p>{e['prose']}</p>
    <div class="chips">{chips}</div>
  </div>
</div>"""


def currently():
    rows = "".join(f'<div class="nowrow"><dt>{k}</dt><dd>{v}</dd></div>'
                   for k, v in SHARED["currently"])
    return f"""<div class="now">
  <div class="nowhead"><span class="dot"></span><h3>Currently</h3>
    <span class="when">{SHARED['currently_updated']}</span></div>
  <div class="nowlist">{rows}</div>
</div>"""


def brings(m):
    rows = ""
    for i, (title, body) in enumerate(m["brings"], 1):
        rows += (f'<div class="bring"><div class="n">{i:02d}</div>'
                 f'<div><h4>{title}</h4><p>{body}</p></div></div>')
    return f'<div class="brings">{rows}</div>'


def barchart(v):
    rows = ""
    for label, val, shown, hot in v["rows"]:
        pct = val / v["max"] * 100
        rows += (f'<div class="brow{" hot" if hot else ""}">'
                 f'<div class="bl">{label}</div>'
                 f'<div class="btrack"><div class="bfill" data-w="{pct:.1f}"></div></div>'
                 f'<div class="bv">{shown}</div></div>')
    note = f'<div class="vnote">{v["note"]}</div>' if v.get("note") else ""
    return (f'<div class="viz"><div class="vtitle">{v["title"]}</div>'
            f'<div class="vsub">{v["sub"]}</div>'
            f'<div class="bars">{rows}</div>{note}</div>')


def post(w):
    return f"""<div class="post">
  <div class="head"><h3>{w['title']}</h3><span class="status">{w['status']}</span></div>
  <p>{w['desc']}</p>
</div>"""


# ---------------------------------------------------------------------- pages
def page_index():
    def hero(m):
        pre = m["name_pre"].replace("『Xingyang』", "<span class='zh'>『Xingyang』</span>")
        return f"""<div class="hero">
  <p class="greet">{pre}</p>
  <h1>{m['headline']}</h1>
  <p class="role">{m['role']}</p>
  <div class="rule"></div>
  <p class="lede">{m['lede']}</p>
  <div class="cta">
    <a class="btn btn-primary" href="about.html" data-keepmode>More about me</a>
    <a class="btn btn-ghost" href="projects.html" data-keepmode>Selected work</a>
  </div>
</div>"""

    def what_i_bring(m):
        return (f'<div class="kicker">{m["about_kicker"]}</div>'
                f'<h2>Beyond tools and titles</h2>'
                f'<p class="prose">This is the kind of perspective I bring to the work.</p>'
                f'{brings(m)}')

    def feat(m):
        return f"""<div class="kicker">Selected work</div>
<h2>{m['proj_title']}</h2>
<p class="prose">{m['proj_lede']}</p>
<div class="cards">{''.join(card(p) for p in m['projects'][:3])}</div>
<div class="note">Three here, the rest on <a href="{SHARED['github']}">GitHub</a> —
a portfolio should be read, not scrolled past.</div>"""

    return shell("Analytics Portfolio", "index",
                 per_mode(hero)
                 + "<section>" + per_mode(what_i_bring) + "</section>"
                 + "<section>" + per_mode(feat) + "</section>"
                 + '<section><div class="kicker">Outside the work</div>'
                   '<h2>What I\'m up to right now</h2>' + currently() + "</section>")


def page_about():
    def block(m):
        paras = "".join(f"<p>{p}</p>" for p in m["about"])
        minis = brings(m)
        skills = "".join(
            f'<div class="row"><span>{t}</span><span>{d}</span></div>' for t, d in m["skills"])
        return f"""<div class="hero" style="padding-bottom:30px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['about_title']}</h1>
  <div class="rule"></div>
</div>
<div class="prose">{SHARED['portrait']}{paras}</div>
<section><div class="kicker">{m['about_kicker']}</div><h2>Beyond tools and titles</h2>{minis}</section>
<section><div class="kicker">Skills</div><h2>What I work with</h2><div class="rows">{skills}</div></section>"""


    return shell("About", "about", per_mode(block)
                 + '<section><div class="kicker">Outside the work</div>'
                   '<h2>What I\'m up to right now</h2>' + currently() + "</section>")


def page_experience():
    aff = "".join(f'<div class="aff"><b>{n}</b><span>{r}</span></div>'
                  for n, r in SHARED["affiliations"])
    edu = "".join(f"""<div class="job edu">
  <div class="when">{e['date']}</div>
  <div>
    <h4>{e['degree']} <span class="at">· {e['school'].split(',')[0]}</span></h4>
    <p>{e['note']}</p>
  </div>
</div>""" for e in SHARED["education"])

    def block(m):
        items = "".join(xp_item(e) for e in m["experience"])
        return f"""<div class="hero" style="padding-bottom:26px">
  <span class="eyebrow">{m['eyebrow']}</span>
  <h1 style="font-size:clamp(28px,4vw,42px)">{m['xp_title']}</h1>
  <div class="rule"></div>
</div>
<div class="affil">{aff}</div>
<div class="xp">{items}</div>"""

    return shell("Experience", "experience",
                 per_mode(block)
                 + f'<section><div class="kicker">Education</div><h2>Where I trained</h2>'
                   f'<div class="xp">{edu}</div></section>')


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
    faq = "".join(f'<details class="q"><summary>{q}</summary><div class="a">{a}</div></details>'
                  for q, a in SHARED["faq"])
    return shell("Contact", "contact", per_mode(block) + rows
                 + f'<section><div class="kicker">Questions people ask</div>'
                   f'<h2>Before you write</h2><div class="faq">{faq}</div></section>')


BUILDERS = {"index": page_index, "about": page_about, "experience": page_experience,
            "projects": page_projects, "contact": page_contact}

if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    copy_figures()
    for slug, _ in PAGES:
        (OUT / f"{slug}.html").write_text(BUILDERS[slug]())
        print(f"  wrote {slug}.html")
    print(f"done -> {OUT}")
