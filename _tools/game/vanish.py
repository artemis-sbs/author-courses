"""Click (tx, ty) the moment a bluish blob that WAS in a region has gone from it.

    python vanish.py <pid> <x0> <y0> <x1> <y1> <seconds> <tx> <ty>
"""
import ctypes
import ctypes.wintypes as wt
import sys
import time

from PIL import ImageGrab

u = ctypes.windll.user32
u.SetProcessDPIAware()
pid = int(sys.argv[1])
x0, y0, x1, y1 = (int(v) for v in sys.argv[2:6])
secs = float(sys.argv[6])
tx, ty = int(sys.argv[7]), int(sys.argv[8])
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
seen = False
gone = 0
t_end = time.time() + secs
while time.time() < t_end:
    img = ImageGrab.grab(bbox=(ox + x0, oy + y0, ox + x1, oy + y1), all_screens=True)
    px = img.load()
    n = 0
    sx = 0
    for yy in range(0, img.height, 2):
        for xx in range(0, img.width, 2):
            r, g, b = px[xx, yy][:3]
            if b > r + 18 and b > 70:
                n += 1
                sx += xx
    if n > 25:
        if not seen:
            print("seen at x", x0 + sx // n)
        seen = True
        gone = 0
    elif seen:
        gone += 1
        if gone >= 3:
            if u.GetForegroundWindow() != h:
                print("REFUSED: window not in front")
                sys.exit(2)
            u.SetCursorPos(ox + tx, oy + ty)
            time.sleep(0.03)
            u.mouse_event(2, 0, 0, 0, 0)
            time.sleep(0.05)
            u.mouse_event(4, 0, 0, 0, 0)
            print("gone; clicked")
            sys.exit(0)
print("timed out; seen =", seen)
