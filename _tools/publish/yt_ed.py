"""Subtitles through the editor's own Upload file (the Upload manual route fails once ASR exists).

    python yt_ed.py a 1.6     -> open editor, Upload file, Continue, find the file input
    python yt_ed.py b 1.6 REF -> upload the srt, check the first cues, Publish
    python yt_ed.py lang 1.6  -> set the video language (channel default UNticked)
"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = int(os.environ["YT_TAB"])  # the Claude-in-Chrome tab id of the Studio tab
ids = {k: v.strip() for k, v in (l.split(None, 1) for l in open("yt_ids.txt", encoding="utf-8").read().split("\n") if l.strip())}
# The .srt files to upload. The browser only takes files the session can share (its
# scratchpad), not R:/cosmos/upload - so copy them there and point YT_SRT at the folder.
SRT = os.environ.get("YT_SRT") or os.path.join(os.getcwd(), "srt")
srt = {}
for f in os.listdir(SRT):
    c, l = f.split(" - ")[0].replace("Class ", "").split(" Lecture ")
    srt[f"{c}.{int(l)}"] = os.path.join(SRT, f)


def c(action, **kw):
    kw.update(action=action, tabId=T)
    return {"name": "computer", "input": kw}


def js(text):
    return {"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": T, "text": text}}


mode, key = sys.argv[1], sys.argv[2]
nav = [{"name": "navigate", "input": {"url": f"https://studio.youtube.com/video/{ids[key]}/translations", "tabId": T}},
       c("wait", duration=6)]
CHECK_CB = ("(()=>{const cb=[...document.querySelectorAll('div[role=checkbox]')].find(x=>x.offsetParent); "
            "if(!cb) throw new Error('no checkbox'); if(cb.getAttribute('aria-checked')!=='false') throw new Error('CHANNEL DEFAULT IS TICKED'); "
            "return 'channel default unticked';})()")
pre = []
if mode in ("la", "l"):
    only = mode == "l"
    mode = "a"
    pre = nav + [
        js("(()=>{ if(!/Set language/.test(document.body.innerText)) throw new Error('language already set'); return 'needs language'; })()"),
        c("left_click", coordinate=[878, 206], action_summary="Opens the video language list"),
        c("wait", duration=1),
        c("type", text="English", action_summary="Searches the language list for English"),
        c("wait", duration=1),
        c("left_click", coordinate=[848, 615], action_summary="Chooses English (United States)"),
        c("wait", duration=1),
        js("(()=>{const cb=[...document.querySelectorAll('div[role=checkbox]')].find(x=>x.offsetParent); if(!cb) throw new Error('no checkbox'); if(cb.getAttribute('aria-checked')==='true') cb.click(); return 'was '+cb.getAttribute('aria-checked');})()"),
        c("wait", duration=1),
        js(CHECK_CB),
        js("(()=>{ if(!/English \\(United States\\)/.test(document.body.innerText)) throw new Error('language not chosen'); return 'English (United States) chosen'; })()"),
        c("left_click", coordinate=[878, 294], action_summary="Confirms English (United States) as this video's language"),
        c("wait", duration=5),
    ]
if mode == "a" and pre and only:
    a = pre
elif mode == "a":
    a = pre + nav + [
        js("(()=>{ if(/Set language/.test(document.body.innerText)) throw new Error('NEEDS LANGUAGE'); const oc=HTMLInputElement.prototype.click; HTMLInputElement.prototype.click=function(){ if(this.type==='file') return; return oc.call(this); }; return 'ready %s'; })()" % key),
        js("var __b=[...document.querySelectorAll('ytcp-button, button')].find(x=>x.offsetParent&&x.innerText&&x.innerText.trim()==='Edit subtitles'); if(!__b) throw new Error('no Edit subtitles'); __b.click(); 'opening editor'"),
        js(open("yt_open.js", encoding="utf-8").read()),
        {"name": "find", "input": {"query": "file input (input type=file) for subtitles", "tabId": T}},
    ]
elif mode == "b":
    first = open(srt[key], encoding="utf-8").read().split("\n")[2]
    a = [
        {"name": "file_upload", "input": {"ref": sys.argv[3], "paths": [srt[key]], "tabId": T}},
        c("wait", duration=4),
        js("(()=>{const d=[...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].find(x=>x.offsetParent&&/Save draft/.test(x.innerText)); if(!d) throw new Error('NO EDITOR'); const all=d.innerText+' '+[...d.querySelectorAll('textarea,input')].map(t=>t.value).join(' '); if(!all.includes(%s)) throw new Error('first cue NOT found'); return 'FIRST CUE MATCHES';})()" % json.dumps(first.strip())),
    ]
    if "--publish" in sys.argv:
        a += [js("var p=[...document.querySelectorAll('[aria-label=Publish]')].find(x=>x.offsetParent); if(!p) throw new Error('no Publish'); p.click(); 'publish clicked'"), c("wait", duration=5),
              js("[...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].some(x=>x.offsetParent&&/Save draft/.test(x.innerText))?'EDITOR STILL OPEN':'%s published'" % key)]
elif mode == "lang":
    a = nav + [
        c("left_click", coordinate=[788, 250], action_summary="Unticks making the language the channel default"),
        c("left_click", coordinate=[878, 206], action_summary="Opens the video language list"),
        c("wait", duration=1),
        c("type", text="English", action_summary="Searches the language list for English"),
        c("wait", duration=1),
        c("left_click", coordinate=[848, 615], action_summary="Chooses English (United States)"),
        c("wait", duration=1),
        c("zoom", region=[760, 180, 1000, 320], scale=0.4),
    ]
print(json.dumps(a))
