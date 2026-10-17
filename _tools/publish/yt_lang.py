"""Set the video language to English (United States) for several videos, all by DOM (layout-proof).
The channel-default box is unticked AFTER choosing (choosing re-ticks it) and checked before Confirm.

    python yt_lang.py 1.12 2.1 2.2
"""
import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = int(os.environ["YT_TAB"])  # the Claude-in-Chrome tab id of the Studio tab
ids = {k: v.strip() for k, v in (l.split(None, 1) for l in open("yt_ids.txt", encoding="utf-8").read().split("\n") if l.strip())}

JS = r"""
var sleep = ms => new Promise(r => setTimeout(r, ms));
var vis = sel => [...document.querySelectorAll(sel)].filter(x => x.offsetParent);
var out;
for (let i=0;i<20 && !/Set language|Video language: \w/.test(document.body.innerText);i++) await sleep(500);
if (!/Set language/.test(document.body.innerText)) { out = 'KEY: already set'; }
else {
  const t = vis('ytcp-text-dropdown-trigger, ytcp-dropdown-trigger').find(x => /Set language/.test(x.innerText));
  if (!t) throw new Error('KEY: no trigger');
  t.click(); await sleep(1500);
  const it = vis('tp-yt-paper-item, [role=option]').find(x => x.innerText.trim() === 'English (United States)');
  if (!it) throw new Error('KEY: no English (United States) item');
  it.click(); await sleep(1500);
  const cb = vis('div[role=checkbox]')[0];
  if (!cb) throw new Error('KEY: no checkbox');
  if (cb.getAttribute('aria-checked') === 'true') { cb.click(); await sleep(700); }
  if (cb.getAttribute('aria-checked') !== 'false') throw new Error('KEY: CHANNEL DEFAULT STILL TICKED');
  if (!/English \(United States\)/.test(document.body.innerText)) throw new Error('KEY: language not chosen');
  const b = vis('ytcp-button, button').find(x => x.innerText && x.innerText.trim() === 'Confirm');
  if (!b) throw new Error('KEY: no confirm');
  b.click(); await sleep(4000);
  out = 'KEY: language set';
}
out
"""

a = []
for k in sys.argv[1:]:
    a += [{"name": "navigate", "input": {"url": f"https://studio.youtube.com/video/{ids[k]}/translations", "tabId": T}},
          {"name": "computer", "input": {"action": "wait", "duration": 6, "tabId": T}},
          {"name": "javascript_tool", "input": {"action": "javascript_exec", "tabId": T, "text": JS.replace("KEY", k).strip()}}]
print(json.dumps(a))
