# YouTube Studio publishing

Class 3's upload scripts. They drive YouTube Studio through Claude in Chrome: each prints
the browser batches to run, against the Studio tab named by the `YT_TAB` environment
variable (its Claude-in-Chrome tab id; a new session has a new tab).

| File | Does |
| --- | --- |
| `yt_c3.py` | compact publish batches for several drafts: `python yt_c3.py 3.4 3.5` |
| `yt_v2.py` | one batch per video for the 1568x753 Studio viewport, playlists first |
| `yt_ed.py` | subtitles through the editor's own Upload file (the manual route fails once ASR exists) |
| `yt_lang.py` | sets the video language to English (United States), by DOM |
| `yt_open.js` | opens a video's details page |
| `yt_meta.json` | titles, descriptions and playlist per lecture |
| `yt_ids.txt` | the video ids YouTube gave each upload |

Rules learned on Class 3: two videos per batch; subtitles through the editor; check each
`.en-US` track after upload. Then `videos.json`, `PUBLISHED` in `_tools/site.py`, the page
stills (`../page_stills_c3.py` is the template), and a push.

`yt_c3.py` and `yt_meta.json` are still Class 3's; generalizing them to
`yt_publish.py <class>` is the next step before Class 4 uploads.
