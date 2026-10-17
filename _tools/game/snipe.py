"""Watch a region of the weapons window and click the first bluish blob found there.

    python snipe.py <pid> <x0> <y0> <x1> <y1> <seconds> [--dry]

Coordinates are client pixels. Refuses to click unless the window of <pid> is in front.
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
dry = "--dry" in sys.argv
LEAD = None
if "--lead" in sys.argv:
    i = sys.argv.index("--lead")
    LEAD, TRIG_Y, TX, TY = float(sys.argv[i+1]), int(sys.argv[i+2]), int(sys.argv[i+3]), int(sys.argv[i+4])

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
t_end = time.time() + secs
n = 0
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
    n += 1
    if len(xs) > 25:
        cx = x0 + sum(xs) // len(xs)
        cy = y0 + sum(ys) // len(ys)
        if LEAD is not None:
            if (TRIG_Y >= 0 and cy < TRIG_Y) or (TRIG_Y < 0 and cx > -TRIG_Y):
                continue
            time.sleep(LEAD)
            cx, cy = TX, TY
        print(f"frame {n} t={time.time():.2f} blob at client {cx},{cy} ({len(xs)} px)")
        if not dry:
            fg = u.GetForegroundWindow()
            if fg != h:
                print("REFUSED: window not in front")
                sys.exit(2)
            u.SetCursorPos(ox + cx, oy + cy)
            time.sleep(0.03)
            u.mouse_event(2, 0, 0, 0, 0)
            time.sleep(0.05)
            u.mouse_event(4, 0, 0, 0, 0)
            print("clicked")
            sys.exit(0)
print(f"no blob in {n} frames")
