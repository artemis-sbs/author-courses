"""Stills of windows that are not VS Code's editor: File Explorer, and a web page.

    ("explorer", "data\\missions", {...})    a REAL File Explorer window on that folder of the stand-in
    ("web", "https://...", {...})            a page, drawn by headless Edge (no window at all)
    ("web", "debug", {"state": ..., "map": 0})    the `sbs debug` page of the state's mission

File Explorer. `explorer.exe "<folder>"` starts a window; it is found by being NEW (it was
not there a moment before) and by its title starting with the folder's name; it is sized
with SetWindowPos, read with PrintWindow, and closed by posting WM_CLOSE to that one window.
Nothing is clicked and no key is sent. What it shows is this machine's own File Explorer:
its view, its theme and whether file name extensions are shown are the USER'S and are not
touched. Two things are kept OUT of the picture, because they are the machine owner's and
not the lesson's: the navigation pane (pinned folders, drives, cloud accounts) is cut out
of every still (pane_box, explorer_still), and the window is opened through the junction
config.COURSE_ROOT, so its address bar reads C:\\Cosmos and not the stand-in's real folder.

(VS Code's markdown preview is a "vscode" still with {"beside": "preview"}: see capture.py.)

A web page. Edge's `--headless --screenshot` writes a PNG; `--virtual-time-budget` gives a
page that draws itself time to do it. Edge runs with a throwaway profile of its own.
"""
import ctypes
import json
import os
import shutil
import subprocess
import time
import urllib.request
from ctypes import wintypes

import config as c

user32 = ctypes.windll.user32
user32.GetForegroundWindow.restype = wintypes.HWND
user32.PostMessageW.argtypes = [wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM]
user32.IsWindow.argtypes = [wintypes.HWND]
WM_CLOSE = 0x0010

EDGE = c._p("EDGE", r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
HOLD = os.path.join(c.WORK, "_hold")                   # where a folder waits while a still must not show it


# ------------------------------------------------------------ File Explorer -----
def _explorer_windows():
    """{hwnd: title} of every File Explorer window on the desktop."""
    found = {}
    proto = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

    def each(hwnd, _):
        cls = ctypes.create_unicode_buffer(64)
        user32.GetClassNameW(hwnd, cls, 64)
        if cls.value == "CabinetWClass" and user32.IsWindowVisible(hwnd):
            n = user32.GetWindowTextLengthW(hwnd)
            buf = ctypes.create_unicode_buffer(n + 1)
            user32.GetWindowTextW(hwnd, buf, n + 1)
            found[hwnd] = buf.value
        return True

    user32.EnumWindows(proto(each), 0)
    return found


class hidden:
    """While a still is made, some folders of the stand-in's missions are not there (a
    lecture that comes BEFORE the student makes MyMission must not show it). They wait in
    WORK\\_hold and are always put back; whatever was made under their names meanwhile is
    thrown away."""

    def __init__(self, names):
        self.names, self.moved = tuple(names or ()), []

    def __enter__(self):
        os.makedirs(HOLD, exist_ok=True)
        for n in self.names:
            src, dst = os.path.join(c.STANDIN_MISSIONS, n), os.path.join(HOLD, n)
            if os.path.exists(dst):
                raise RuntimeError(f"{dst} is already there: put it back by hand first")
            if os.path.exists(src):
                shutil.move(src, dst)
                self.moved.append((src, dst))
            else:
                self.moved.append((src, None))
        return self

    def __exit__(self, *exc):
        for src, dst in self.moved:
            if os.path.isdir(src):                     # made meanwhile: it is the stray
                shutil.rmtree(src, ignore_errors=True)
            elif os.path.exists(src):
                os.remove(src)
            if dst:
                shutil.move(dst, src)
        return False


def local_path(path):
    """A folder on a drive that is only a name for \\\\localhost\\X$\\... , by its real local
    path: File Explorer then shows a disk, not a network share."""
    import re
    drive = os.path.splitdrive(path)[0]
    out = subprocess.run(["net", "use", drive], capture_output=True, text=True).stdout if drive else ""
    m = re.search(r"Remote name\s+\\\\(?:localhost|127\.0\.0\.1)\\([A-Za-z])\$(\S*)", out)
    return (m.group(1).upper() + ":" + m.group(2) + path[len(drive):]) if m else path


def course_root():
    """The stand-in by the course's own name (config.COURSE_ROOT, a junction to it): what File
    Explorer is opened on, so that its address bar shows the lesson's path and not this
    machine's. No junction, or one that leads somewhere else, stops the run: a still with
    the real path on it must never be made by accident."""
    real = os.path.normcase(os.path.realpath(local_path(c.STANDIN)))
    if not os.path.isdir(c.COURSE_ROOT) or os.path.normcase(os.path.realpath(c.COURSE_ROOT)) != real:
        raise RuntimeError(f"{c.COURSE_ROOT} is not a junction to the stand-in. Make it once: "
                           f"mklink /J {c.COURSE_ROOT} \"{local_path(c.STANDIN)}\"")
    return c.COURSE_ROOT


def listed(folder):
    """The folder's names in File Explorer's own order: folders first, each group sorted as
    Explorer sorts names (numbers by value). Hidden files are left out, as they are there."""
    import functools
    cmp = ctypes.windll.shlwapi.StrCmpLogicalW
    cmp.argtypes = [wintypes.LPCWSTR, wintypes.LPCWSTR]
    attrs = ctypes.windll.kernel32.GetFileAttributesW
    attrs.argtypes = [wintypes.LPCWSTR]
    names = [n for n in os.listdir(folder) if not (attrs(os.path.join(folder, n)) & 2)]
    key = functools.cmp_to_key(lambda a, b: cmp(a, b))
    dirs = sorted([n for n in names if os.path.isdir(os.path.join(folder, n))], key=key)
    files = sorted([n for n in names if not os.path.isdir(os.path.join(folder, n))], key=key)
    return dirs + files


NAV_FALLBACK = (372, 170, 32)      # at 1280x720: the pane's right edge, its top, and the status bar's height


def pane_box(hwnd, size):
    """Where the navigation pane is in the window's picture: (right edge, top, bottom), found
    from the window itself (the rectangle of its tree control, among its child windows).
    (0, top, bottom) when the window has no pane. When the tree cannot be found and the file
    list cannot be found either, a fixed box, wide enough for the pane as Windows first shows it."""
    import capture
    found = {}
    proto = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

    def each(h, _):
        cls = ctypes.create_unicode_buffer(64)
        user32.GetClassNameW(h, cls, 64)
        if cls.value in ("SysTreeView32", "NamespaceTreeControl", "SHELLDLL_DefView") and user32.IsWindowVisible(h):
            r = wintypes.RECT()
            user32.GetWindowRect(h, ctypes.byref(r))
            found.setdefault(cls.value, (r.left, r.top, r.right, r.bottom))
        return True

    user32.EnumChildWindows(hwnd, proto(each), 0)
    w = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(w))
    left, top, _r, _b = capture.insets(hwnd)
    ox, oy = w.left + left, w.top + top
    tree = found.get("SysTreeView32") or found.get("NamespaceTreeControl")
    view = found.get("SHELLDLL_DefView")
    if tree and tree[2] - tree[0] > 8:
        return (tree[2] - ox, tree[1] - oy, tree[3] - oy)
    if view:                                           # no tree: the list says where the pane would end
        return (max(0, view[0] - ox) if view[0] - ox > 40 else 0, view[1] - oy, view[3] - oy)
    return (NAV_FALLBACK[0], NAV_FALLBACK[1], size[1] - NAV_FALLBACK[2])


def _settled(hwnd, size, settle, timeout, front=None):
    """The window's picture once three looks in a row are the same."""
    import capture
    last, same, t1 = None, 0, time.time()
    while time.time() - t1 < timeout:
        if front and user32.GetForegroundWindow() == hwnd:
            user32.SetForegroundWindow(front)          # in front, it draws a focus box round its first row
        time.sleep(settle / 2)
        img = capture.grab(hwnd)
        data = img.resize((160, 90)).tobytes()
        same = same + 1 if data == last else 0
        last = data
        if same >= 2:
            if img.size != tuple(size):
                raise RuntimeError(f"the window came out {img.size}, not {tuple(size)}")
            return img
    raise RuntimeError("the File Explorer window never stopped changing")


def explorer_still(folder, size=(1280, 720), settle=4.0, timeout=30):
    """A real File Explorer window on folder. -> (image, how far the file list moved left).
    The image is the window as PrintWindow sees it, without the invisible resize border and
    WITHOUT its navigation pane (see pane_box): that pane lists the machine owner's own
    folders, drives and accounts, and none of that belongs in a lesson. The window is this
    function's own from start to WM_CLOSE: a File Explorer window the user already has open
    is never touched, and neither is any setting of File Explorer."""
    import capture
    if not os.path.isdir(folder):
        raise RuntimeError(f"not a folder: {folder}")
    before = set(_explorer_windows())
    front = user32.GetForegroundWindow()
    subprocess.Popen(["explorer.exe", folder])
    name = os.path.basename(folder.rstrip("\\/"))
    hwnd, t0 = None, time.time()
    try:
        while time.time() - t0 < timeout and hwnd is None:
            time.sleep(0.5)
            for h, title in _explorer_windows().items():
                if h not in before and (title == name or title.startswith(name + " ")):
                    hwnd = h
        if hwnd is None:
            raise RuntimeError(f"no new File Explorer window titled {name!r} appeared (it may have opened "
                               f"as a tab of a window that was already there)")
        left, top, right, bottom = capture.insets(hwnd)
        user32.ShowWindow(hwnd, 4)
        user32.SetWindowPos(hwnd, 1, 40 - left, 40 - top, size[0] + left + right, size[1] + top + bottom, 0x0010)
        if front:
            user32.SetForegroundWindow(front)          # hand the keyboard back
        img = _settled(hwnd, size, settle, timeout, front)
        cut, p_top, p_bottom = pane_box(hwnd, size)
        if cut <= 0:
            return img, 0
        # The pane is cut out and the file list moved left into its place. So that the list
        # still fills the window, the window is made wider by the pane's width and looked at
        # again: the rows between the toolbar and the status bar come from that wider look,
        # everything else (title, tabs, address bar, toolbar, status bar) from the first.
        wide = (size[0] + cut, size[1])
        user32.SetWindowPos(hwnd, 1, 40 - left, 40 - top, wide[0] + left + right, wide[1] + top + bottom, 0x0010)
        img2 = _settled(hwnd, wide, settle, timeout, front)
        cut2, t2, b2 = pane_box(hwnd, wide)
        if (cut2, t2, b2) != (cut, p_top, p_bottom):
            raise RuntimeError(f"the navigation pane moved between two looks: {(cut, p_top, p_bottom)} then {(cut2, t2, b2)}")
        edge = img.crop((0, p_top, 1, p_bottom))       # the window's own left border
        img.paste(img2.crop((cut, p_top, cut + size[0], p_bottom)), (0, p_top))
        img.paste(edge, (0, p_top))
        return img, cut
    finally:
        if hwnd is not None and user32.IsWindow(hwnd):
            user32.PostMessageW(hwnd, WM_CLOSE, 0, 0)  # that window, and no other
            for _ in range(20):
                time.sleep(0.25)
                if not user32.IsWindow(hwnd):
                    break


def make_explorer(sb, name, spec, stills_dir):
    """("explorer", "data\\missions", {opts}): a folder of the stand-in, in a real File Explorer.
    opts: "without" (folders of data\\missions that are not there meanwhile), "size" (default
    1280x720: it fills the frame at one and a half times, so the names are easy to read),
    "state" (the mission's files first), "root" (another folder to start from: a full path).
    Parts a storyboard can mark: "row:<name>" for each listed name, "rows", "address", "tab".
    The rows are placed for the Details view at 1280x720, which is how File Explorer opens a
    plain folder on this machine; LOOK at the frame when you mark one."""
    rel, opts = spec[1], (spec[2] if len(spec) > 2 else {})
    root = opts.get("root") or course_root()
    folder = os.path.join(root, rel) if rel else root
    size = tuple(opts.get("size", (1280, 720)))
    made, renamed = [], []
    with hidden(opts.get("without")):
        try:
            # "rename": {old: new} - a folder of data\missions under another name while the still is made
            for old, new in (opts.get("rename") or {}).items():
                os.rename(os.path.join(c.STANDIN_MISSIONS, old), os.path.join(c.STANDIN_MISSIONS, new))
                renamed.append((old, new))
            # "add": {path under data\missions: "file" | "dir" | "zip:<folder>"} - things that are there
            # meanwhile (the logs a run leaves, a zip of the folder); taken away again after
            for rel_path, what in (opts.get("add") or {}).items():
                p = os.path.join(c.STANDIN_MISSIONS, rel_path)
                if os.path.exists(p):
                    continue
                if what == "dir":
                    os.makedirs(p)
                elif what.startswith("zip:"):
                    import zipfile
                    src = os.path.join(c.STANDIN_MISSIONS, what[4:])
                    with zipfile.ZipFile(p, "w", zipfile.ZIP_DEFLATED) as z:
                        for f in sorted(os.listdir(src)):
                            if os.path.isfile(os.path.join(src, f)):
                                z.write(os.path.join(src, f), what[4:] + "/" + f)
                else:
                    open(p, "w").close()
                made.append(p)
            img, cut = explorer_still(folder, size=size)
            names = listed(folder)
        finally:
            for p in reversed(made):
                shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else os.remove(p)
            for old, new in reversed(renamed):
                os.rename(os.path.join(c.STANDIN_MISSIONS, new), os.path.join(c.STANDIN_MISSIONS, old))
    img.save(os.path.join(stills_dir, name + ".png"))
    parts = {"address": [254, 62, 968, 100], "tab": [12, 14, 310, 48]}
    top, pitch = 208, 37                               # Details view, 100% text, a 125% screen
    shown = []
    for i, n in enumerate(names):
        if top + (i + 1) * pitch < size[1] - 34:
            parts["row:" + n] = [392 - cut, top + i * pitch, 1144 - cut, top + (i + 1) * pitch]
            shown.append(n)
    if shown:
        parts["rows"] = [392 - cut, top, 1144 - cut, parts["row:" + shown[-1]][3]]
    meta = {"kind": "explorer", "folder": folder, "parts": parts, "names": names,
            "without": list(opts.get("without", ()))}
    json.dump(meta, open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
    return f"{img.size[0]}x{img.size[1]}, {len(names)} names, {folder}"


# -------------------------------------------------------------------- web -----
def web_still(url, png, size=(1920, 1080), budget=8000, scale=1.0):
    """Headless Edge draws url and writes png. No window. -> the image."""
    from PIL import Image
    if os.path.exists(png):
        os.remove(png)
    profile = os.path.join(c.WORK, "edge_profile")     # a throwaway profile: never the user's Edge
    cmd = [EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
           f"--user-data-dir={profile}", f"--window-size={int(size[0] / scale)},{int(size[1] / scale)}",
           f"--force-device-scale-factor={scale}", f"--virtual-time-budget={budget}",
           f"--screenshot={png}", url]
    subprocess.run(cmd, capture_output=True, timeout=120)
    if not os.path.exists(png):
        raise RuntimeError(f"Edge wrote no screenshot of {url}")
    return Image.open(png).convert("RGB")


def web_still_live(url, png, size=(1920, 1080), wait=12.0, scale=1.0, port=9237):
    """For a page that keeps drawing itself from its server (the `sbs debug` page): headless
    Edge opens it, REAL seconds pass, and then Edge is asked for a screenshot over its own
    DevTools connection. No window. -> the image."""
    import base64
    import socket
    import struct
    from PIL import Image
    profile = os.path.join(c.WORK, "edge_profile")
    proc = subprocess.Popen([EDGE, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--no-first-run",
                             f"--user-data-dir={profile}", f"--remote-debugging-port={port}",
                             "--remote-allow-origins=*",
                             f"--window-size={int(size[0] / scale)},{int(size[1] / scale)}",
                             f"--force-device-scale-factor={scale}", url],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        target, t0 = None, time.time()
        while time.time() - t0 < 30 and target is None:
            time.sleep(0.5)
            try:
                pages = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=2).read())
                target = next((p for p in pages if p.get("type") == "page"), None)
            except Exception:
                pass
        if target is None:
            raise RuntimeError("headless Edge never answered on its DevTools port")
        time.sleep(wait)                               # the page talks to its server and draws
        path = target["webSocketDebuggerUrl"].split(f":{port}", 1)[1]
        s = socket.create_connection(("127.0.0.1", port), timeout=30)
        key = base64.b64encode(os.urandom(16)).decode()
        s.sendall((f"GET {path} HTTP/1.1\r\nHost: 127.0.0.1:{port}\r\nUpgrade: websocket\r\n"
                   f"Connection: Upgrade\r\nSec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n\r\n").encode())
        buf = b""
        while b"\r\n\r\n" not in buf:
            buf += s.recv(4096)
        buf = buf.split(b"\r\n\r\n", 1)[1]
        body = json.dumps({"id": 1, "method": "Page.captureScreenshot", "params": {"format": "png"}}).encode()
        mask = os.urandom(4)
        head = bytes([0x81]) + (bytes([0x80 | len(body)]) if len(body) < 126 else bytes([0x80 | 126]) + struct.pack(">H", len(body)))
        s.sendall(head + mask + bytes(b ^ mask[i % 4] for i, b in enumerate(body)))

        def need(n):
            nonlocal buf
            while len(buf) < n:
                more = s.recv(1 << 16)
                if not more:
                    raise RuntimeError("Edge closed the DevTools connection")
                buf += more
            out, buf = buf[:n], buf[n:]
            return out

        data = b""
        while True:                                    # read frames until our answer is whole
            b0, b1 = need(2)
            n = b1 & 0x7F
            if n == 126:
                n = struct.unpack(">H", need(2))[0]
            elif n == 127:
                n = struct.unpack(">Q", need(8))[0]
            data += need(n)
            if b0 & 0x80:
                msg = json.loads(data.decode("utf-8"))
                data = b""
                if msg.get("id") == 1:
                    break
        s.close()
        with open(png, "wb") as f:
            f.write(base64.b64decode(msg["result"]["data"]))
    finally:
        subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
    return Image.open(png).convert("RGB")


def _pid_file(port=8765):
    return os.path.join(os.environ.get("TEMP", ""), f"cosmos_dev_runner_{port}.pid")


def debug_page(mission, map_arg="0", wait=90, size=(1920, 1080), budget=8000, scale=1.0, path="/", after=8):
    """Start `sbs debug <mission> --map <n>` in the stand-in, wait for its page, let Edge draw
    it, and stop it again. -> (image, what the command printed, paths as the course writes them)."""
    import capture
    env = {k: v for k, v in os.environ.items() if k.upper() != "NODEFAULTCURRENTDIRECTORYINEXEPATH"}
    env["COSMOS_SETTINGS"] = '{"GAME_RESULTS_SAVE": false}'
    env.pop("PYTHONPATH", None)
    env["PYTHONUNBUFFERED"] = "1"
    log = os.path.join(c.WORK, "debug_run.txt")
    args = ["cmd", "/d", "/c", "sbs", "debug", mission] + (["--map", str(map_arg)] if map_arg is not None else [])
    with open(log, "w", encoding="utf-8", errors="replace") as out:
        proc = subprocess.Popen(args, cwd=c.STANDIN_MISSIONS, env=env, stdout=out, stderr=subprocess.STDOUT,
                                stdin=subprocess.DEVNULL, creationflags=0x00000200)      # its own process group
    png = os.path.join(c.WORK, "debug_page.png")
    there = set(os.listdir(c.STANDIN_MISSIONS))
    try:
        t0, up = time.time(), False
        while time.time() - t0 < wait and not up:
            time.sleep(1.5)
            if "GUI server started" in open(log, encoding="cp1252", errors="replace").read():
                up = True
            elif proc.poll() is not None:
                break
        if not up:
            raise RuntimeError("`sbs debug` never said its GUI server had started:\n"
                               + open(log, encoding="cp1252", errors="replace").read()[-1500:])
        time.sleep(after)                              # the map starts, the first frames go out
        # what the window says BEFORE the browser is opened: "then it goes quiet"
        quiet = open(log, encoding="cp1252", errors="replace").read()
        img = web_still_live("http://localhost:8765" + path, png, size=size, wait=budget / 1000.0, scale=scale)
    finally:
        subprocess.run(["taskkill", "/PID", str(proc.pid), "/T", "/F"], capture_output=True)
        time.sleep(1)
        if os.path.exists(_pid_file()):
            os.remove(_pid_file())
        for stray in set(os.listdir(c.STANDIN_MISSIONS)) - there:      # the run's own debug.log and common_data
            p = os.path.join(c.STANDIN_MISSIONS, stray)
            shutil.rmtree(p, ignore_errors=True) if os.path.isdir(p) else os.remove(p)
    return img, capture.course_paths(quiet)


def make_web(sb, name, spec, stills_dir, mission_dir):
    """("web", url or file, {opts}) or ("web", "debug", {"state": ..., "map": "0", "path": "/"}).
    opts: "size", "scale" (2 draws the page at twice the size: big text), "budget" (ms of the
    page's own time Edge waits)."""
    import states
    what, opts = spec[1], (spec[2] if len(spec) > 2 else {})
    png = os.path.join(stills_dir, name + ".png")
    size, scale = tuple(opts.get("size", (1920, 1080))), opts.get("scale", 1.0)
    meta = {"kind": "web", "parts": {}, "url": what}
    if what == "debug":
        if opts.get("state"):
            states.materialize(sb, opts["state"], mission_dir)
        img, printed = debug_page(getattr(sb, "MISSION", "MyMission"), opts.get("map", "0"), size=size, scale=scale,
                                  budget=opts.get("budget", 8000), path=opts.get("path", "/"),
                                  after=opts.get("after", 8))
        meta["url"] = "http://localhost:8765" + opts.get("path", "/")
        meta["printed"] = printed
        # what the command printed while its page was up, as a Command Prompt with no prompt
        # back yet: the still <name>_term (declare it in STILLS as ("derived", "..."))
        import cards
        command = "sbs debug " + getattr(sb, "MISSION", "MyMission") + " --map " + str(opts.get("map", "0"))
        t_img, t_meta = cards.prompt([(command, printed)], last_prompt=False, tail=opts.get("tail"))
        t_img.save(os.path.join(stills_dir, name + "_term.png"))
        json.dump(t_meta, open(os.path.join(stills_dir, name + "_term.json"), "w", encoding="utf-8"), indent=1)
    else:
        url = what if "://" in what else "file:///" + os.path.abspath(what).replace("\\", "/")
        if opts.get("wait"):                           # real seconds, for a page that loads as it goes
            img = web_still_live(url, png, size=size, wait=opts["wait"], scale=scale)
        else:
            img = web_still(url, png, size=size, budget=opts.get("budget", 8000), scale=scale)
    img.save(png)
    json.dump(meta, open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
    return f"{img.size[0]}x{img.size[1]}, {meta['url']}"
