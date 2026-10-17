"""One browser_batch per video for the 1568x753 Studio viewport (playlists first)."""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = int(os.environ["YT_TAB"])  # the Claude-in-Chrome tab id of the Studio tab
key = sys.argv[1]
meta = {f"{m['cls']}.{m['lec']}": m for m in json.load(open("yt_meta.json", encoding="utf-8"))}
ids = dict(l.split(None, 1) for l in open("yt_ids.txt", encoding="utf-8").read().split("\n") if l.strip())
m = meta[key]
vid = ids[key].strip()


def c(action, **kw):
    kw.update(action=action, tabId=T)
    return {"name": "computer", "input": kw}


def js(text):
    return {"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": T, "text": text}}


a = [
    c("key", text="Escape", action_summary="Closes any open box"),
    {"name": "navigate", "input": {"url": f"https://studio.youtube.com/video/{vid}/edit", "tabId": T}},
    c("wait", duration=6),
    c("left_click", coordinate=[1524, 66], action_summary="Opens the draft's upload wizard"),
    c("wait", duration=4),
    c("left_click", coordinate=[552, 654], action_summary="Opens the playlists selector"),
    c("wait", duration=1),
    js("var want=['Cosmos Author Courses','Cosmos Author Courses - Class %d']; var out=[]; "
       "var rows=[...document.querySelectorAll('ytcp-ve, li, tp-yt-paper-item, #items > *')].filter(x=>x.offsetParent); "
       "for (var w of want) { var lab=[...document.querySelectorAll('span, div, label')].filter(x=>x.offsetParent && x.children.length===0 && x.innerText && x.innerText.trim()===w)[0]; "
       "if(!lab) throw new Error('no playlist '+w); var row=lab.parentElement; var cb=null; "
       "for (var k=0;k<5 && row && !cb;k++){ cb=row.querySelector('[role=checkbox]'); if(!cb) row=row.parentElement; } "
       "if(!cb) throw new Error('no checkbox for '+w); if(cb.getAttribute('aria-checked')!=='true') cb.click(); out.push(w); } "
       "'ticked: '+out.join(' + ')" % m["cls"]),
    c("wait", duration=1),
    js("var bad=[...document.querySelectorAll('[role=checkbox]')].filter(x=>x.offsetParent && x.getAttribute('aria-checked')==='true').map(x=>{var r=x; for(var k=0;k<5 && r;k++){ if((r.innerText||'').trim()) break; r=r.parentElement;} return (r&&r.innerText||'').trim().split('\\n')[0];}); var ok=bad.length===2; if(!ok) throw new Error('ticked count '+bad.length); 'two ticked'"),
    c("zoom", region=[460, 420, 760, 500], scale=0.5),
    c("left_click", coordinate=[720, 696], action_summary="Closes the playlists selector"),
    c("wait", duration=1),
    c("left_click", coordinate=[660, 226], action_summary="Puts the cursor in the title"),
    c("wait", duration=0.5),
    c("key", text="ctrl+a", action_summary="Selects the whole title"),
    c("type", text=m["title"], action_summary="Types the new title"),
    c("left_click", coordinate=[660, 360], action_summary="Puts the cursor in the description"),
    c("wait", duration=0.5),
    c("type", text=m["desc"], action_summary="Types the description"),
    c("wait", duration=1),
    c("zoom", region=[456, 180, 860, 360], scale=0.6),
]
if "--publish" in sys.argv:
    for s in ("Video elements", "Initial check", "Visibility"):
        a += [c("left_click", coordinate=[1110, 690], action_summary=f"Goes to {s}"), c("wait", duration=2)]
    a += [
        js("(()=>{const r=document.querySelector('tp-yt-paper-radio-button[name=\"UNLISTED\"]'); if(!r) return 'no radio'; r.click(); return 'unlisted:'+r.hasAttribute('checked');})()"),
        c("wait", duration=1),
        c("left_click", coordinate=[1110, 690], action_summary="Saves the video as Unlisted"),
        c("wait", duration=4),
        js("(()=>{const t=document.body.innerText; if(/still checking your content/i.test(t)) return 'STILL CHECKING'; return /Video published/.test(t)?'PUBLISHED':'unknown';})()"),
    ]
print(json.dumps(a))
