"""Click (tx, ty) the moment a bluish blob ENTERS a region (it must be seen empty first).

    python snipe2.py <pid> <x0> <y0> <x1> <y1> <seconds> <tx> <ty> [delay]

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
tx, ty = int(sys.argv[7]), int(sys.argv[8])
delay = float(sys.argv[9]) if len(sys.argv) > 9 else 0.0
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
empty_seen = False
t_end = time.time() + secs
while time.time() < t_end:
    img = ImageGrab.grab(bbox=(ox + x0, oy + y0, ox + x1, oy + y1), all_screens=True)
    px = img.load()
    n = 0
    for yy in range(0, img.height, 2):
        for xx in range(0, img.width, 2):
            r, g, b = px[xx, yy][:3]
            if b > r + 18 and b > 70:
                n += 1
    if n <= 25:
        empty_seen = True
        continue
    if not empty_seen:
        continue
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
    print(f"entered ({n} px); clicked {tx},{ty}")
    sys.exit(0)
print("timed out")
