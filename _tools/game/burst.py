"""Click a fraction of a window's client rect (optional), then grab the client area every
<step> seconds for <secs> seconds into <outdir>/f00.png ...

    python burst.py <pid> <outdir> <secs> <step> [<fracX> <fracY>]

Refuses to click unless the window is in front. Moves the cursor off the map after a click.
"""
import ctypes
import ctypes.wintypes as wt
import os
import sys
import time

from PIL import ImageGrab

u = ctypes.windll.user32
u.SetProcessDPIAware()
pid = int(sys.argv[1])
out = sys.argv[2]
secs, step = float(sys.argv[3]), float(sys.argv[4])
click = (float(sys.argv[5]), float(sys.argv[6])) if len(sys.argv) > 6 else None
os.makedirs(out, exist_ok=True)
found = []


def cb(h, _):
    p = wt.DWORD()
    u.GetWindowThreadProcessId(h, ctypes.byref(p))
    if p.value == pid and u.IsWindowVisible(h):
        found.append(h)
    return True


u.EnumWindows(ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, wt.LPARAM)(cb), 0)
h = found[0]
r = wt.RECT()
u.GetClientRect(h, ctypes.byref(r))
pt = wt.POINT(0, 0)
u.ClientToScreen(h, ctypes.byref(pt))
ox, oy, w, ht = pt.x, pt.y, r.right, r.bottom
if click:
    if u.GetForegroundWindow() != h:
        print("REFUSED: window not in front")
        sys.exit(2)
    u.SetCursorPos(ox + int(click[0] * w), oy + int(click[1] * ht))
    time.sleep(0.03)
    u.mouse_event(2, 0, 0, 0, 0)
    time.sleep(0.05)
    u.mouse_event(4, 0, 0, 0, 0)
    time.sleep(0.03)
    u.SetCursorPos(ox + int(0.995 * w), oy + int(0.995 * ht))
t0 = time.time()
i = 0
while time.time() - t0 < secs:
    ImageGrab.grab(bbox=(ox, oy, ox + w, oy + ht), all_screens=True).save(os.path.join(out, f"f{i:02d}.png"))
    print(f"f{i:02d} {time.time() - t0:5.2f}")
    i += 1
    time.sleep(step)
