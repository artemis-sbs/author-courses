"""Find the LIVE scene buttons in the xESS column (bg #1c3450 at x=868) and click one.

    python btn.py <pid> <index> [--wait <seconds>] [--count <n>] [--dry]

index counts from the top among live buttons (negative counts from the bottom).
--wait: poll until at least --count (default index+1) live buttons show, up to that long.
Refuses to click unless the window of <pid> is in front.
"""
import ctypes
import ctypes.wintypes as wt
import sys
import time

from PIL import ImageGrab

u = ctypes.windll.user32
u.SetProcessDPIAware()
args = sys.argv[1:]
pid, index = int(args[0]), int(args[1])
wait = float(args[args.index("--wait") + 1]) if "--wait" in args else 0.0
count = int(args[args.index("--count") + 1]) if "--count" in args else (index + 1 if index >= 0 else -index)
dry = "--dry" in args
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


def runs():
    img = ImageGrab.grab(bbox=(ox + 866, oy + 190, ox + 870, oy + 958), all_screens=True)
    px = img.load()
    out, start = [], None
    for y in range(img.height):
        r, g, b = px[2, y][:3]
        hit = abs(r - 0x1c) < 6 and abs(g - 0x34) < 6 and abs(b - 0x50) < 6
        if hit and start is None:
            start = y
        elif not hit and start is not None:
            if y - start > 15:
                out.append((190 + start, 190 + y))
            start = None
    if start is not None and img.height - start > 15:
        out.append((190 + start, 190 + img.height))
    return out


t_end = time.time() + wait
rs = runs()
while len(rs) < count and time.time() < t_end:
    time.sleep(0.15)
    rs = runs()
print("buttons:", rs)
if len(rs) < count:
    print("not enough buttons")
    sys.exit(3)
y0, y1 = rs[index]
if dry:
    sys.exit(0)
if u.GetForegroundWindow() != h:
    print("REFUSED: window not in front")
    sys.exit(2)
u.SetCursorPos(ox + 1000, oy + (y0 + y1) // 2)
time.sleep(0.03)
u.mouse_event(2, 0, 0, 0, 0)
time.sleep(0.05)
u.mouse_event(4, 0, 0, 0, 0)
print("clicked", index, "at y", (y0 + y1) // 2)
