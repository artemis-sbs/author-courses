var sleep = ms => new Promise(r => setTimeout(r, ms));
var dlg = () => [...document.querySelectorAll('tp-yt-paper-dialog, ytcp-dialog')].find(x => x.offsetParent && /Save draft/.test(x.innerText));
var st = '';
for (let i = 0; i < 40; i++) { const d = dlg(); if (d && /Select how you want to add subtitles/.test(d.innerText)) { st = 'EMPTY'; break; } if (d && (d.querySelectorAll('textarea').length || /Edit timings|Edit as text/.test(d.innerText))) { st = 'TRACK'; break; } await sleep(500); }
if (!st) throw new Error('editor did not load');
await sleep(1200);
if (st === 'EMPTY') {
  const el = [...dlg().querySelectorAll('*')].filter(x => x.offsetParent && x.innerText && x.innerText.trim() === 'Upload file').pop();
  if (!el) throw new Error('no Upload file row');
  (el.closest('[role=button],button,tp-yt-paper-item,ytcp-ve,div[tabindex]') || el).click();
} else {
  const o = [...dlg().querySelectorAll('[aria-label=Options]')].find(x => x.offsetParent);
  if (!o) throw new Error('no Options');
  o.click(); await sleep(1000);
  const u = [...document.querySelectorAll('tp-yt-paper-item, [role=menuitem], [role=option]')].find(x => x.offsetParent && x.innerText.trim() === 'Upload file');
  if (!u) throw new Error('no Upload file item');
  u.click();
}
await sleep(1800);
var c = [...document.querySelectorAll('ytcp-button, button')].find(x => x.offsetParent && x.innerText && x.innerText.trim() === 'Continue');
if (!c) throw new Error(st + ': no Continue');
c.click(); await sleep(1000);
st + ': ready for file'
