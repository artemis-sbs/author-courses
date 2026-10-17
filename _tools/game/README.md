# Timing helpers for game stills

Class 3's one-off helpers, kept because they caught moments a plain `game.py click` could
not: a blob crossing a line, a screen that has stopped moving, a button that only exists
for a second. Each one watches a region of a real engine window and clicks at the right
instant. They drive the REAL mouse: hand the screen over first, and check the target
window is in front.

| Script | Clicks when |
| --- | --- |
| `snipe.py` | the first bluish blob appears in a region of the weapons window |
| `snipe2.py` | a bluish blob ENTERS a region (seen empty first) |
| `snipe3.py` | a tracked blob's centroid crosses a line |
| `vanish.py` | a blob that was in a region has gone |
| `cellsnipe.py` | a blob shows, clicking the CELL it is in |
| `motion.py` | a region has shown no motion for N seconds, after some |
| `burst.py` | (optionally clicks, then) grabs the client area every N ms |
| `btn.py` | clicks a live scene button in the xESS column |
| `walkcheck.py` | not a clicker: re-does the library's "well clear of the sentry" rule offline, to check a taught route before filming |

Prefer `../picture/game.py` with a recorded `capture_steps.py`; use these only when a
replay cannot catch the moment.
