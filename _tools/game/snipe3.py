"""Track a bluish blob's centroid in a region; click (tx, ty) the moment the centroid
ENTERS a box (cx0..cx1, cy0..cy1) it was not in the frame before.

    python snipe3.py <pid> <x0> <y0> <x1> <y1> <seconds> <cx0> <cy0> <cx1> <cy1> <tx> <ty> [delay]

Client pixels. Refuses to click unless the window of <pid> is in front.
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
bx0, by0, bx1, by1 = (int(v) for v in sys.argv[7:11])
tx, ty = int(sys.argv[11]), int(sys.argv[12])
delay = float(sys.argv[13]) if len(sys.argv) > 13 else 0.0
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
was_in = True        # must see it OUT of the box once first
t_end = time.time() + secs
while time.time() < t_end:
    img = ImageGrab.grab(bbox=(ox + x0, oy + y0, ox + x1, oy + y1), all_screens=True)
    px = img.load()
    xs, ys = [], []
    for yy in range(0, img.height, 2):
        for xx in range(0, img.width, 2):
            r, g, b = px[xx, yy][:3]
            if b > r + 18 and b > 70:
                xs.append(xx)
                ys.append(yy)
    inside = False
    if len(xs) > 25:
        cx = x0 + sum(xs) // len(xs)
        cy = y0 + sum(ys) // len(ys)
        inside = bx0 <= cx <= bx1 and by0 <= cy <= by1
    if inside and not was_in:
        if delay:
            time.sleep(delay)
        if u.GetForegroundWindow() != h:
            print("REFUSED: window not in front")
            sys.exit(2)
        u.SetCursorPos(ox + tx, oy + ty)
        time.sleep(0.02)
        u.mouse_event(2, 0, 0, 0, 0)
        time.sleep(0.04)
        u.mouse_event(4, 0, 0, 0, 0)
        print(f"centroid {cx},{cy} entered; clicked {tx},{ty}")
        sys.exit(0)
    was_in = inside
print("timed out")
