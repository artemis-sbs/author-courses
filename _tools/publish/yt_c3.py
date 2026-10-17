"""Compact publish batches for several drafts, any class: python yt_c3.py 4.1 4.2"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = int(os.environ["YT_TAB"])  # the Claude-in-Chrome tab id of the Studio tab
meta = {f"{m['cls']}.{m['lec']}": m for m in json.load(open("yt_meta.json", encoding="utf-8"))}
ids = dict(l.split(None, 1) for l in open("yt_ids.txt", encoding="utf-8").read().split("\n") if l.strip())

TICK = ("var want=['Cosmos Author Courses','Cosmos Author Courses - Class %d']; var out=[]; for (var w of want) "
        "{ var lab=[...document.querySelectorAll('span, div, label')].filter(x=>x.offsetParent && x.children.length===0 "
        "&& x.innerText && x.innerText.trim()===w)[0]; if(!lab) throw new Error('no playlist '+w); var row=lab.parentElement; "
        "var cb=null; for (var k=0;k<5 && row && !cb;k++){ cb=row.querySelector('[role=checkbox]'); if(!cb) row=row.parentElement; } "
        "if(!cb) throw new Error('no checkbox for '+w); if(cb.getAttribute('aria-checked')!=='true') cb.click(); out.push(w); } "
        "'ticked: '+out.join(' + ')")
COUNT = ("var n=[...document.querySelectorAll('[role=checkbox]')].filter(x=>x.offsetParent && "
         "x.getAttribute('aria-checked')==='true').length; if(n!==2) throw new Error('ticked count '+n); 'two ticked'")
UNL = ("(()=>{const r=document.querySelector('tp-yt-paper-radio-button[name=\"UNLISTED\"]'); if(!r) "
       "throw new Error('no radio'); r.click(); return 'unlisted:'+r.hasAttribute('checked');})()")
DONE = ("(()=>{const t=document.body.innerText; if(/still checking your content/i.test(t)) throw new Error('STILL CHECKING %s'); "
        "if(!/Video published/.test(t)) throw new Error('NOT PUBLISHED %s'); return '%s PUBLISHED';})()")


def c(action, **kw):
    kw.update(action=action, tabId=T)
    return {"name": "computer", "input": kw}


def js(text):
    return {"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": T, "text": text}}


a = []
for key in sys.argv[1:]:
    m = meta[key]
    a += [c("key", text="Escape", action_summary="Closes any open box"),
          {"name": "navigate", "input": {"url": "https://studio.youtube.com/video/%s/edit" % ids[key].strip(), "tabId": T}},
          c("wait", duration=6),
          c("left_click", coordinate=[1524, 66], action_summary="Opens the draft's upload wizard"), c("wait", duration=4),
          c("left_click", coordinate=[552, 654], action_summary="Opens the playlists selector"), c("wait", duration=1),
          js(TICK % m["cls"]), c("wait", duration=1), js(COUNT),
          c("left_click", coordinate=[720, 696], action_summary="Closes the playlists selector"), c("wait", duration=1),
          c("left_click", coordinate=[660, 226], action_summary="Puts the cursor in the title"), c("wait", duration=0.5),
          c("key", text="ctrl+a", action_summary="Selects the whole title"),
          c("type", text=m["title"], action_summary="Types the new title"),
          c("left_click", coordinate=[660, 360], action_summary="Puts the cursor in the description"), c("wait", duration=0.5),
          c("type", text=m["desc"], action_summary="Types the description"), c("wait", duration=1),
          c("zoom", region=[456, 180, 860, 360], scale=0.35)]
    for s in ("Video elements", "Initial check", "Visibility"):
        a += [c("left_click", coordinate=[1110, 690], action_summary="Goes to " + s), c("wait", duration=2)]
    a += [js(UNL), c("wait", duration=1),
          c("left_click", coordinate=[1110, 690], action_summary="Saves the video as Unlisted"), c("wait", duration=6),
          js(DONE % (key, key, key))]
print(json.dumps(a))
