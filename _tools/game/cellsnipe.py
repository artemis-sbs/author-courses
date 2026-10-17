"""Watch a region for a blob (blue: b > r+18; cyan: g,b > 220, r < 190) and click the CELL it
has just ENTERED, if that cell is in the allowed list. Cells are 50 px; cell (0,0)'s top-left is
at client (gx, gy). The blob's centroid is shifted down by <dy> px (figures are drawn tall).

    python cellsnipe.py <pid> <x0> <y0> <x1> <y1> <seconds> <blue|cyan> <gx> <gy> <dy> <cx,cy> [<cx,cy> ...] [--dry]
"""
import ctypes
import ctypes.wintypes as wt
import sys
import time

from PIL import ImageGrab

u = ctypes.windll.user32
u.SetProcessDPIAware()
args = [a for a in sys.argv[1:] if a != "--dry"]
dry = "--dry" in sys.argv
pid = int(args[0])
x0, y0, x1, y1 = (int(v) for v in args[1:5])
secs = float(args[5])
mode = args[6]
gx, gy, dy = int(args[7]), int(args[8]), int(args[9])
allowed = {tuple(int(v) for v in a.split(",")) for a in args[10:]}
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
prev = "start"
t0 = time.time()
while time.time() - t0 < secs:
    img = ImageGrab.grab(bbox=(ox + x0, oy + y0, ox + x1, oy + y1), all_screens=True)
    px = img.load()
    xs, ys = [], []
    for yy in range(0, img.height, 2):
        for xx in range(0, img.width, 2):
            r, g, b = px[xx, yy][:3]
            if mode == "blue":
                hit = b > r + 18 and b > 70
            else:
                hit = g > 220 and b > 220 and r < 190
            if hit:
                xs.append(xx)
                ys.append(yy)
    if len(xs) < (25 if mode == "blue" else 6):
        cell = None
    else:
        cx = x0 + sum(xs) // len(xs)
        cy = y0 + sum(ys) // len(ys) + dy
        cell = ((cx - gx) // 50, (cy - gy) // 50)
    if cell != prev:
        print(f"{time.time() - t0:6.2f} cell {cell}")
        if prev != "start" and cell in allowed:
            if dry:
                print("  (would click)")
            else:
                if u.GetForegroundWindow() != h:
                    print("REFUSED: window not in front")
                    sys.exit(2)
                tx, ty = gx + cell[0] * 50 + 25, gy + cell[1] * 50 + 25
                u.SetCursorPos(ox + tx, oy + ty)
                time.sleep(0.02)
                u.mouse_event(2, 0, 0, 0, 0)
                time.sleep(0.04)
                u.mouse_event(4, 0, 0, 0, 0)
                print(f"clicked cell {cell} at {tx},{ty}")
                sys.exit(0)
        prev = cell
print("timed out")
