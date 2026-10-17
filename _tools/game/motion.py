"""Click (tx, ty) once a region has shown NO motion for <quiet> seconds (after having shown some).

    python motion.py <pid> <x0> <y0> <x1> <y1> <seconds> <quiet> <tx> <ty> [--any]

--any: do not require motion to have been seen first.
"""
import ctypes
import ctypes.wintypes as wt
import sys
import time

from PIL import ImageChops, ImageGrab

u = ctypes.windll.user32
u.SetProcessDPIAware()
pid = int(sys.argv[1])
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
secs, quiet = float(sys.argv[6]), float(sys.argv[7])
tx, ty = int(sys.argv[8]), int(sys.argv[9])
need_seen = "--any" not in sys.argv
found = []


def cb(h, _):
    p = wt.DWORD()
    u.GetWindowThreadProcessId(h, ctypes.byref(p))
    if p.value == pid and u.IsWindowVisible(h):
        found.append(h)
    return True


u.EnumWindows(ctypes.WINFUNCTYPE(ctypes.c_bool, wt.HWND, wt.LPARAM)(cb), 0)
h = found[0]
pt = wt.POINT(0, 0)
u.ClientToScreen(h, ctypes.byref(pt))
ox, oy = pt.x, pt.y
bbox = (ox + x0, oy + y0, ox + x1, oy + y1)
prev = ImageGrab.grab(bbox=bbox, all_screens=True).convert("L")
seen = not need_seen
last_motion = time.time()
t_end = time.time() + secs
while time.time() < t_end:
    time.sleep(0.15)
    cur = ImageGrab.grab(bbox=bbox, all_screens=True).convert("L")
    diff = ImageChops.difference(prev, cur).point(lambda v: 255 if v > 40 else 0)
    n = sum(1 for v in diff.getdata() if v)
    prev = cur
    now = time.time()
    if n > 60:
        if not seen:
            print("motion first seen")
        seen = True
        last_motion = now
    elif seen and now - last_motion >= quiet:
        if u.GetForegroundWindow() != h:
            print("REFUSED: window not in front")
            sys.exit(2)
        u.SetCursorPos(ox + tx, oy + ty)
        time.sleep(0.03)
        u.mouse_event(2, 0, 0, 0, 0)
        time.sleep(0.05)
        u.mouse_event(4, 0, 0, 0, 0)
        print(f"quiet {quiet}s; clicked")
        sys.exit(0)
print("timed out; seen =", seen)
