"""Make the stills a storyboard asks for: real VS Code windows and real command output.

    python capture.py --setup --tool <folder with sbs.pyz, sbs.bat, __lib__> --ext <extensions dir>
        once per machine: builds the stand-in install and the throwaway VS Code profile
        under config.WORK
    python make.py <lecture> --capture            (the usual way in)

VS Code. One fresh window per still: the THROWAWAY profile (config.VSC_DATA / VSC_EXT, never
the user's), the stand-in's mission folder, the file at the storyboard's line. The window is
sized to 1920x1080, pushed BEHIND every other window, and read with PrintWindow; nothing is
typed and nothing is clicked. A starting window does take the keyboard focus for a moment,
and this hands it back - but do not type a password while it runs.

Where the text is: settings.json paints the cursor's line with config.LINE_TELL. That band
is found in the picture, and since the cursor's line number is known, so is every line's
place. Marks are drawn from that, never from a guess at the layout.

Command Prompt. The command is really run, in the stand-in install, on the state's files;
what it printed is drawn as a console window (cards.prompt). The prompt's path is the
course's stand-in path, not the real one.
"""
import argparse
import ctypes
import json
import os
import shutil
import subprocess
import sys
import time
from ctypes import wintypes

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import cards  # noqa: E402
import config as c  # noqa: E402
import states  # noqa: E402

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
user32.SetProcessDPIAware()
user32.GetForegroundWindow.restype = wintypes.HWND
user32.GetDC.restype = wintypes.HDC
user32.GetDC.argtypes = [wintypes.HWND]
user32.ReleaseDC.argtypes = [wintypes.HWND, wintypes.HDC]
user32.PrintWindow.argtypes = [wintypes.HWND, wintypes.HDC, wintypes.UINT]
user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, ctypes.c_int, ctypes.c_int, ctypes.c_int,
                                ctypes.c_int, wintypes.UINT]
user32.ShowWindow.argtypes = [wintypes.HWND, ctypes.c_int]
user32.SetForegroundWindow.argtypes = [wintypes.HWND]
user32.IsWindowVisible.argtypes = [wintypes.HWND]
user32.GetWindowRect.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.RECT)]
gdi32.CreateCompatibleDC.restype = wintypes.HDC
gdi32.CreateCompatibleDC.argtypes = [wintypes.HDC]
gdi32.CreateCompatibleBitmap.restype = wintypes.HBITMAP
gdi32.CreateCompatibleBitmap.argtypes = [wintypes.HDC, ctypes.c_int, ctypes.c_int]
gdi32.SelectObject.restype = wintypes.HGDIOBJ
gdi32.SelectObject.argtypes = [wintypes.HDC, wintypes.HGDIOBJ]
gdi32.DeleteObject.argtypes = [wintypes.HGDIOBJ]
gdi32.DeleteDC.argtypes = [wintypes.HDC]
gdi32.GetDIBits.argtypes = [wintypes.HDC, wintypes.HBITMAP, wintypes.UINT, wintypes.UINT, ctypes.c_void_p,
                            ctypes.c_void_p, wintypes.UINT]


# ----------------------------------------------------------------- setup -----
def setup(tool_src, ext_src):
    os.makedirs(c.STANDIN_MISSIONS, exist_ok=True)
    for f in ("sbs.pyz", "sbs.bat"):
        shutil.copyfile(os.path.join(tool_src, f), os.path.join(c.STANDIN_MISSIONS, f))
    lib = os.path.join(c.STANDIN_MISSIONS, "__lib__")
    os.makedirs(lib, exist_ok=True)
    n = 0
    for f in os.listdir(os.path.join(tool_src, "__lib__")):
        src = os.path.join(tool_src, "__lib__", f)
        dev_build = f.rsplit(".", 1)[0].endswith("_dev")      # ...v1.4.0_dev.mastlib; NOT cosmos_dev.v1.4.0
        if os.path.isfile(src) and not dev_build and not os.path.exists(os.path.join(lib, f)):
            shutil.copyfile(src, os.path.join(lib, f))
            n += 1
    # lint's compile check imports sbslibs from the install's PyAddons; without it the
    # story "does not compile" and the picture would show an error no student gets
    addons = os.path.join(c.STANDIN, "PyAddons")
    if not os.path.exists(addons):
        shutil.copytree(os.path.join(os.path.dirname(c.SRC_PYRUNTIME), "PyAddons"), addons,
                        ignore=shutil.ignore_patterns("__pycache__"))
    link = os.path.join(c.STANDIN, "PyRuntime")
    if not os.path.exists(link):
        made = subprocess.run(["cmd", "/d", "/c", "mklink", "/J", link, c.SRC_PYRUNTIME], capture_output=True)
        if made.returncode:                           # not a local NTFS drive: a copy does as well
            shutil.copytree(c.SRC_PYRUNTIME, link)
    if os.path.isdir(c.VSC_EXT):
        shutil.rmtree(c.VSC_EXT)
    shutil.copytree(ext_src, c.VSC_EXT)
    listing = os.path.join(c.VSC_EXT, "extensions.json")
    if os.path.exists(listing):                       # it names the folder it was copied FROM
        entries = json.load(open(listing, encoding="utf-8"))
        for e in entries:
            where = os.path.join(c.VSC_EXT, e["relativeLocation"])
            uri = "/" + where.replace("\\", "/")
            e["location"] = {"$mid": 1, "fsPath": where, "_sep": 1, "path": uri, "scheme": "file"}
        json.dump(entries, open(listing, "w", encoding="utf-8"))
    os.makedirs(os.path.join(c.VSC_DATA, "User"), exist_ok=True)
    print(f"stand-in install at {c.STANDIN} ({n} library files copied); VS Code profile at {c.VSC_DATA}")


def student_tree(missions=("LegendaryMissions", "SecretMeeting", "WalkTheLine")):
    """Make the stand-in look like a student's game folder, for stills of File Explorer and
    for `dir` and `sbs doctor`: the game's program and its DLLs beside PyRuntime and PyAddons,
    the files and folders of `data` (art, sound, settings), and the missions the game comes
    with. Each mission is the COMMITTED files of the dev install's copy (`git archive HEAD`,
    which reads and writes nothing in that repository). Nothing already there is replaced."""
    import io
    import tarfile
    src = os.path.dirname(c.SRC_PYRUNTIME)
    made = []
    for f in os.listdir(src):                          # the game itself: one program, four DLLs
        keep = f == "Artemis3-x64-release.exe" or (f.lower().endswith(".dll") and not f.lower().endswith("d.dll"))
        if keep and not os.path.exists(os.path.join(c.STANDIN, f)):
            shutil.copy2(os.path.join(src, f), os.path.join(c.STANDIN, f))
            made.append(f)
    data_src, data_dst = os.path.join(src, "data"), os.path.join(c.STANDIN, "data")
    skip = ("game_results", "shipdata - copy", "shipdatabb", "shipdatademo", "shipdatahash", "joystick", ".bak",
            "_old")
    for f in os.listdir(data_src):
        s, d = os.path.join(data_src, f), os.path.join(data_dst, f)
        if os.path.exists(d) or any(k in f.lower() for k in skip):
            continue
        if os.path.isfile(s):
            shutil.copy2(s, d)
            made.append("data\\" + f)
        elif f in ("graphics", "audio", "PaxDefault"):
            shutil.copytree(s, d, ignore=shutil.ignore_patterns("__pycache__"))
            made.append("data\\" + f + "\\")
    for m in missions:
        d = os.path.join(c.STANDIN_MISSIONS, m)
        if os.path.exists(d):
            continue
        tar = subprocess.run(["git", "-C", os.path.join(data_src, "missions", m), "archive", "HEAD"],
                             capture_output=True)
        if tar.returncode:
            print(f"  {m}: not copied ({tar.stderr.decode(errors='replace').strip()})")
            continue
        os.makedirs(d)
        with tarfile.open(fileobj=io.BytesIO(tar.stdout)) as t:
            t.extractall(d)
        # (.gitattributes stays: `sbs doctor` reads it, and reports a problem without it)
        for junk in (".github", ".gitignore", ".vscode", ".claude", ".env"):
            p = os.path.join(d, junk)                  # a download holds the mission, not its repository's own files
            if os.path.isdir(p):
                shutil.rmtree(p)
            elif os.path.exists(p):
                os.remove(p)
        made.append("data\\missions\\" + m + "\\")
    print(f"student tree at {c.STANDIN}: added {len(made)}: " + ", ".join(made))


def ready():
    need = [os.path.join(c.STANDIN_MISSIONS, "sbs.pyz"), os.path.join(c.STANDIN, "PyRuntime", "python.exe"), c.VSC_EXT]
    return [p for p in need if not os.path.exists(p)]


# ---------------------------------------------------------------- VS Code -----
def settings(size):
    return {
        "editor.fontSize": c.EDITOR_FONT[size],
        "editor.lineHeight": c.EDITOR_LINE[size],
        "editor.fontFamily": "Consolas, 'Courier New', monospace",
        "editor.wordWrap": "off",
        "editor.minimap.enabled": False,
        "editor.stickyScroll.enabled": False,          # it would pin a heading over the top lines
        "editor.renderLineHighlight": "line",
        "editor.lineNumbersMinChars": 4,
        "editor.glyphMargin": False,
        "editor.folding": False,
        "editor.cursorBlinking": "solid",
        "editor.occurrencesHighlight": "off",
        "editor.selectionHighlight": False,
        "editor.detectIndentation": False,
        "editor.guides.indentation": False,
        "editor.smoothScrolling": False,
        "editor.overviewRulerBorder": False,
        "editor.inlayHints.enabled": "off",
        "editor.codeLens": False,                      # a "1 reference(s)" row pushes the lines below it down
        "workbench.colorCustomizations": {"editor.lineHighlightBackground": c.LINE_TELL,
                                          "editor.lineHighlightBorder": "#00000000"},
        "breadcrumbs.enabled": False,
        "workbench.startupEditor": "none",
        "workbench.secondarySideBar.defaultVisibility": "hidden",    # the Chat panel
        "chat.commandCenter.enabled": False,
        "chat.disableAIFeatures": True,
        "workbench.layoutControl.enabled": False,
        "workbench.tips.enabled": False,
        "workbench.editor.empty.hint": "hidden",
        "window.commandCenter": False,
        "window.zoomLevel": 0,
        "window.restoreWindows": "none",
        "window.newWindowDimensions": "default",
        "files.hotExit": "off",
        "files.autoSave": "off",
        "git.enabled": False,
        "update.mode": "none",
        "update.showReleaseNotes": False,
        "extensions.autoUpdate": False,
        "extensions.autoCheckUpdates": False,
        "extensions.ignoreRecommendations": True,
        "telemetry.telemetryLevel": "off",
        "security.workspace.trust.enabled": False,
    }


def our_pids():
    """Code.exe processes started with the throwaway profile - and no others."""
    ps = ("Get-CimInstance Win32_Process -Filter \"Name = 'Code.exe'\" | "
          "Where-Object { $_.CommandLine -and $_.CommandLine.Contains('" + c.VSC_DATA + "') } | "
          "ForEach-Object { $_.ProcessId }")
    out = subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, text=True).stdout
    return [int(x) for x in out.split() if x.strip().isdigit()]


def stop_vscode():
    pids = our_pids()
    for pid in pids:
        subprocess.run(["taskkill", "/PID", str(pid), "/F"], capture_output=True)
    return len(pids)


def window_of(pids):
    found = []
    proto = ctypes.WINFUNCTYPE(ctypes.c_bool, wintypes.HWND, wintypes.LPARAM)

    def each(hwnd, _):
        pid = wintypes.DWORD()
        user32.GetWindowThreadProcessId(hwnd, ctypes.byref(pid))
        if pid.value in pids and user32.IsWindowVisible(hwnd):
            n = user32.GetWindowTextLengthW(hwnd)
            buf = ctypes.create_unicode_buffer(n + 1)
            user32.GetWindowTextW(hwnd, buf, n + 1)
            r = wintypes.RECT()
            user32.GetWindowRect(hwnd, ctypes.byref(r))
            if buf.value and r.right - r.left > 400:
                found.append((hwnd, buf.value))
        return True

    user32.EnumWindows(proto(each), 0)
    return found[0] if found else (None, "")


def insets(hwnd):
    """The invisible resize border Windows adds round a window: (left, top, right, bottom)."""
    r, f = wintypes.RECT(), wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(r))
    if ctypes.windll.dwmapi.DwmGetWindowAttribute(wintypes.HWND(hwnd), 9, ctypes.byref(f), ctypes.sizeof(f)):
        return (0, 0, 0, 0)
    return (f.left - r.left, f.top - r.top, r.right - f.right, r.bottom - f.bottom)


def place(hwnd):
    """Size the window so that what can be SEEN of it is exactly the frame. -> True when it is."""
    left, top, right, bottom = insets(hwnd)
    want = (c.W + left + right, c.H + top + bottom)
    r = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(r))
    if (r.right - r.left, r.bottom - r.top) == want:
        return True
    user32.ShowWindow(hwnd, 4)                                          # restored, not activated
    user32.SetWindowPos(hwnd, 1, -left, -top, want[0], want[1], 0x0010)  # HWND_BOTTOM, no activate
    return False


def grab(hwnd):
    img = grab_window(hwnd)
    left, top, right, bottom = insets(hwnd)
    return img.crop((left, top, img.width - right, img.height - bottom))


def grab_window(hwnd):
    from PIL import Image
    r = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(r))
    w, h = r.right - r.left, r.bottom - r.top
    screen = user32.GetDC(None)
    mem = gdi32.CreateCompatibleDC(screen)
    bmp = gdi32.CreateCompatibleBitmap(screen, w, h)
    old = gdi32.SelectObject(mem, bmp)
    user32.PrintWindow(hwnd, mem, 2)                   # 2 = render the full content, even when covered
    head = (ctypes.c_uint32 * 10)(40, w, ctypes.c_uint32(-h & 0xFFFFFFFF).value, 1 | (32 << 16), 0, 0, 0, 0, 0, 0)
    buf = ctypes.create_string_buffer(w * h * 4)
    gdi32.GetDIBits(mem, bmp, 0, h, buf, head, 0)
    gdi32.SelectObject(mem, old)
    gdi32.DeleteObject(bmp)
    gdi32.DeleteDC(mem)
    user32.ReleaseDC(None, screen)
    return Image.frombuffer("RGBA", (w, h), buf, "raw", "BGRA", 0, 1).convert("RGB")


def find_tell(img):
    """Find the cursor line's band. -> dict(y, h, x0, top, bottom, right) in pixels, or None."""
    tell = tuple(int(c.LINE_TELL[i:i + 2], 16) for i in (1, 3, 5))
    px = img.load()
    w, h = img.size

    def is_tell(p):
        return all(abs(p[i] - tell[i]) <= 2 for i in range(3))

    # the far right first; then the left half, for a window whose right half is a preview
    for x in [w - 90, w - 140, w - 200] + list(range(w // 2 - 22, w // 4, -23)):
        rows = [y for y in range(h) if is_tell(px[x, y])]
        if len(rows) >= 8 and rows[-1] - rows[0] == len(rows) - 1:
            y0, band = rows[0], len(rows)
            left = next(xx for xx in range(w) if is_tell(px[xx, y0 + 1]))
            if x < w - 200:                             # found in the left half: text may cross this column,
                run = left                              # so measure the editor's height just inside its right edge
                while run + 1 < w and is_tell(px[run + 1, y0 + 1]):
                    run += 1
                x = run - 24
            # the editor's own background is above the band or below it - whichever runs
            # further (the band may be the first line or the last)
            best = (y0, y0 + band)
            for bg in {px[x, max(0, y0 - 2)], px[x, min(h - 1, y0 + band + 2)]}:
                top = y0
                while top > 0 and px[x, top - 1] == bg:
                    top -= 1
                bottom = y0 + band
                while bottom < h - 1 and px[x, bottom] == bg:
                    bottom += 1
                if bottom - top > best[1] - best[0]:
                    best = (top, bottom)
            top, bottom = best
            right = left
            while right < w and is_tell(px[right, y0 + 1]):    # the band's own run (a preview beside it has none)
                right += 1
            return {"y": y0, "h": band, "x0": left, "top": top, "bottom": bottom, "right": right}
    return None


def side_bar(folder, show):
    """Show or hide the Side Bar for the next window on this folder. There is no setting
    for it: VS Code keeps it in the folder's own state, in the (throwaway) profile. That
    state exists once the folder has been opened once; before that the Side Bar shows.
    -> True when the state was written."""
    import sqlite3
    import urllib.parse
    want = "file:///" + urllib.parse.quote(folder.replace(os.sep, "/"), safe="/").lower()
    root = os.path.join(c.VSC_DATA, "User", "workspaceStorage")
    for d in (os.listdir(root) if os.path.isdir(root) else []):
        ws = os.path.join(root, d, "workspace.json")
        db = os.path.join(root, d, "state.vscdb")
        if not (os.path.exists(ws) and os.path.exists(db)):
            continue
        if json.load(open(ws, encoding="utf-8")).get("folder", "").lower() != want:
            continue
        con = sqlite3.connect(db)
        con.execute("INSERT OR REPLACE INTO ItemTable (key, value) VALUES ('workbench.sideBar.hidden', ?)",
                    ("false" if show else "true",))
        con.commit()
        con.close()
        return True
    return False


HELPER = "course.picture-helper-0.0.1"
HELPER_JS = """// Lives ONLY in the picture pipeline's throwaway VS Code profile. When a window has finished
// starting, it runs the VS Code commands listed in the file named by PICTURE_DO, in order.
// That is how a still shows the markdown preview beside its file, or a panel, with no key pressed.
const vscode = require('vscode');
const fs = require('fs');
exports.activate = async function () {
    const file = process.env.PICTURE_DO;
    if (!file || !fs.existsSync(file)) { return; }
    let steps = [];
    try { steps = JSON.parse(fs.readFileSync(file, 'utf8')); } catch (e) { return; }
    const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
    await sleep(1500);
    for (const step of steps) {
        if (typeof step === 'number') { await sleep(step); continue; }
        try { await vscode.commands.executeCommand(step[0], ...step.slice(1)); } catch (e) { }
        await sleep(700);
    }
    try { fs.writeFileSync(file + '.done', 'ok'); } catch (e) { }
};
exports.deactivate = function () { };
"""


def helper_extension():
    """Put the helper extension into the THROWAWAY extensions folder (once). -> its folder."""
    folder = os.path.join(c.VSC_EXT, HELPER)
    os.makedirs(folder, exist_ok=True)
    manifest = {"name": "picture-helper", "publisher": "course", "version": "0.0.1", "displayName": "Picture helper",
                "description": "Runs listed commands at startup, for stills. Throwaway profile only.",
                "engines": {"vscode": "^1.80.0"}, "main": "./extension.js",
                "activationEvents": ["onStartupFinished"], "capabilities": {
                    "untrustedWorkspaces": {"supported": True}}}
    with open(os.path.join(folder, "package.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1)
    with open(os.path.join(folder, "extension.js"), "w", encoding="utf-8", newline="\n") as f:
        f.write(HELPER_JS)
    listing = os.path.join(c.VSC_EXT, "extensions.json")
    entries = json.load(open(listing, encoding="utf-8")) if os.path.exists(listing) else []
    if not any(e.get("identifier", {}).get("id") == "course.picture-helper" for e in entries):
        uri = "/" + folder.replace("\\", "/")
        entries.append({"identifier": {"id": "course.picture-helper"}, "version": "0.0.1",
                        "location": {"$mid": 1, "fsPath": folder, "_sep": 1, "path": uri, "scheme": "file"},
                        "relativeLocation": HELPER,
                        "metadata": {"installedTimestamp": int(time.time() * 1000), "pinned": True, "source": "vsix"}})
        json.dump(entries, open(listing, "w", encoding="utf-8"))
    return folder


def workspace_state(folder, key, value=None, delete=False):
    """Read, write or delete one key of the folder's own state in the THROWAWAY profile
    (the same store side_bar() writes). -> the value before, or None when the folder has
    never been opened with this profile."""
    import sqlite3
    import urllib.parse
    want = "file:///" + urllib.parse.quote(folder.replace(os.sep, "/"), safe="/").lower()
    root = os.path.join(c.VSC_DATA, "User", "workspaceStorage")
    for d in (os.listdir(root) if os.path.isdir(root) else []):
        ws = os.path.join(root, d, "workspace.json")
        db = os.path.join(root, d, "state.vscdb")
        if not (os.path.exists(ws) and os.path.exists(db)):
            continue
        if json.load(open(ws, encoding="utf-8")).get("folder", "").lower() != want:
            continue
        con = sqlite3.connect(db)
        row = con.execute("SELECT value FROM ItemTable WHERE key = ?", (key,)).fetchone()
        if delete:
            con.execute("DELETE FROM ItemTable WHERE key = ?", (key,))
        elif value is not None:
            con.execute("INSERT OR REPLACE INTO ItemTable (key, value) VALUES (?, ?)", (key, value))
        con.commit()
        con.close()
        return row[0] if row else ""
    return None


def vscode_still(folder, file, line, size, settle=7.0, timeout=60, side=True, wrap=False, preview=False,
                 trust=True, extra=None, do=None, plain=False):
    """Open the folder and the file at a line in a fresh throwaway window, and read it.
    side=False hides the Side Bar (the file list); wrap=True wraps long lines, for a log.
    preview=True opens a .md file in VS Code's built-in markdown preview instead of as text
    (by a setting of the throwaway profile, so no key is pressed); there is no cursor line
    in a preview, so the window is read once it has stopped changing, and geometry is None.
    trust=False starts WITHOUT --disable-workspace-trust and with Workspace Trust on: the
    folder opens in Restricted Mode, as a student's does the first time.
    extra: more settings for this one still.
    plain=True: what is in front is not a text editor (the Workspace Trust page, say), so
    there is no cursor line to find: the window is read once it has stopped changing.
    do: VS Code commands the helper extension runs once the window is up, in order: a list
    of [command, args...] (a number is a wait in milliseconds). For example
    [["markdown.showPreviewToSide"], ["workbench.action.focusFirstEditorGroup"]].
    -> (image, geometry dict) ; raises if the window never shows the file."""
    stop_vscode()
    # A window that was closed with unsaved typing in it (a still that shows the dot on a
    # tab) leaves a backup, and the next window would open that file again, still unsaved.
    shutil.rmtree(os.path.join(c.VSC_DATA, "Backups"), ignore_errors=True)
    if not side_bar(folder, side) and not side:
        raise RuntimeError("the Side Bar cannot be hidden before this folder has been opened once")
    if preview:
        # VS Code reopens the editors a folder had last time; a remembered TEXT editor of this
        # file would win over the preview. Forget them (throwaway profile, this folder only).
        workspace_state(folder, "memento/workbench.parts.editor", delete=True)
    user = os.path.join(c.VSC_DATA, "User")
    os.makedirs(user, exist_ok=True)
    with open(os.path.join(user, "settings.json"), "w", encoding="utf-8") as f:
        st = dict(settings(size), **({"editor.wordWrap": "on"} if wrap else {}))
        if preview:
            st["workbench.editorAssociations"] = {"*.md": "vscode.markdown.preview.editor"}
            st["markdown.preview.fontSize"] = c.EDITOR_FONT[size]
            st["markdown.preview.lineHeight"] = 1.6
        if not trust:
            st["security.workspace.trust.enabled"] = True
            st["security.workspace.trust.startupPrompt"] = "never"      # the band and the Status Bar, not the dialog
            st["security.workspace.trust.banner"] = "always"
        st.update(extra or {})
        json.dump(st, f, indent=2)
    env = {k: v for k, v in os.environ.items() if not k.startswith(("VSCODE_", "ELECTRON_"))}
    do_file = os.path.join(c.VSC_DATA, "picture_do.json")
    for f in (do_file, do_file + ".done"):
        if os.path.exists(f):
            os.remove(f)
    if do:
        helper_extension()
        # editors remembered from the last window on this folder would open beside the new ones
        workspace_state(folder, "memento/workbench.parts.editor", delete=True)
        with open(do_file, "w", encoding="utf-8") as f:
            json.dump(do, f)
        env["PICTURE_DO"] = do_file
        settle = max(settle, 9.0)
    front = user32.GetForegroundWindow()
    target = [os.path.join(folder, file)] if preview else ["--goto", f"{os.path.join(folder, file)}:{line}:1"]
    subprocess.Popen([c.VSCODE, f"--user-data-dir={c.VSC_DATA}", f"--extensions-dir={c.VSC_EXT}", "--new-window",
                      "--skip-welcome", "--skip-release-notes"] + (["--disable-workspace-trust"] if trust else [])
                     + [folder] + target, env=env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    t0, hwnd, seen, last = time.time(), None, None, None
    try:
        while time.time() - t0 < timeout:
            time.sleep(1.0)
            if hwnd is None:
                hwnd, _title = window_of(set(our_pids()))
                if hwnd is None:
                    continue
                place(hwnd)
                if front:
                    user32.SetForegroundWindow(front)                    # hand the keyboard back
                continue
            if not place(hwnd):
                continue
            if preview or plain:                                         # no cursor line to find: wait for stillness
                img = grab(hwnd)
                now = img.resize((192, 108)).tobytes()
                if now == last:
                    if seen is None:
                        seen = time.time()
                    if time.time() - seen >= settle and time.time() - t0 > 14 and (
                            not do or os.path.exists(do_file + ".done")):
                        return img, None
                else:
                    seen = None
                last = now
                continue
            if do and not os.path.exists(do_file + ".done"):
                continue                                                 # the helper has not finished its list
            geo = find_tell(grab(hwnd))
            if geo and geo == last:
                if seen is None:
                    seen = time.time()
                if time.time() - seen >= settle:                         # the add-on's checker has had its time
                    img = grab(hwnd)
                    if img.size != (c.W, c.H):
                        raise RuntimeError(f"the window came out {img.size}, not {(c.W, c.H)}")
                    return img, geo
            else:
                seen = None
            last = geo
        raise RuntimeError(f"VS Code never showed {file} at line {line} (window {'found' if hwnd else 'not found'})")
    finally:
        stop_vscode()


def wrap_starts(line, cols):
    """The column each row of a wrapped line starts at: [0, ...]. Whole words, as many as
    fit in cols; a word longer than a row is cut."""
    import re as _re
    starts, row_start, at = [0], 0, 0
    for m in _re.finditer(r"\S+\s*", line):
        word = m.group(0).rstrip()
        end = m.start() + len(word)
        if end - row_start > cols and m.start() > row_start:
            row_start = m.start()
            starts.append(row_start)
        while end - row_start > cols:                  # one word wider than the window
            row_start += cols
            starts.append(row_start)
    return starts


def make_vscode(sb, name, spec, stills_dir, mission_dir):
    _, state, line, size = spec[:4]
    opts = spec[4] if len(spec) > 4 else {}
    file = opts.get("file", sb.FILE)                   # another file of the folder: a log, story.mast
    if opts.get("folder"):                             # another folder of the stand-in's missions, as it is on disk
        mission_dir = os.path.join(c.STANDIN_MISSIONS, opts["folder"])      # (state is not used: pass None)
        with open(os.path.join(mission_dir, file), encoding="utf-8", newline="") as fh:
            files = {file: fh.read().replace(chr(13) + chr(10), chr(10))}
        if not opts.get("side", True) and workspace_state(mission_dir, "workbench.sideBar.hidden") is None:
            vscode_still(mission_dir, file, line, size)                     # open it once, so its Side Bar can be hidden
    else:
        files = states.materialize(sb, state, mission_dir)
    do = list(opts.get("do", ()))
    if opts.get("beside") == "preview":                # the markdown preview in the right half; the cursor stays left
        do = [["markdown.showPreviewToSide"], ["workbench.action.focusFirstEditorGroup"]] + do
    wrap = opts.get("wrap", False)
    extra = dict(opts.get("settings") or {})
    if opts.get("beside") == "preview":                # the preview's words as large as the editor's
        extra.setdefault("markdown.preview.fontSize", c.EDITOR_FONT[size] + 1)
    img, geo = vscode_still(mission_dir, file, line, size, side=opts.get("side", True), wrap=wrap,
                            trust=opts.get("trust", True), do=do or None, extra=extra,
                            plain=opts.get("plain", False))
    if geo is None:                                    # a page, not a file: a picture with no lines to mark
        img.save(os.path.join(stills_dir, name + ".png"))
        json.dump({"kind": "vscode", "state": state, "parts": {}, "file": file},
                  open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
        return "a page (no lines to mark)"
    if wrap:                                           # the cursor's own line may be folded: its band is then
        rows = max(1, round(geo["h"] / (c.EDITOR_LINE[size] * 1.25)))       # several rows tall (125% screen)
        geo["h"] = geo["h"] / rows
    scale = geo["h"] / c.EDITOR_LINE[size]
    lines = files[file].split("\n")
    char_w = c.EDITOR_FONT[size] * scale * 1126 / 2048                        # Consolas: 1126/2048 em a character
    text = {"lines": lines, "line_h": geo["h"], "x0": geo["x0"], "char_w": char_w,
            "clip": [geo["x0"], geo["top"], geo["right"], geo["bottom"]]}
    if wrap:
        # a wrapped line takes several rows: work out which, as the editor does (whole words,
        # as many as fit), so a mark still lands on its line. "breaks" = the column each row starts at.
        zoom = round(scale * 4) / 4                    # the machine's scaling, 125% here
        cw = c.EDITOR_FONT[size] * zoom * 1126 / 2048
        cols = max(10, int((geo["right"] - geo["x0"] - 14 * zoom) / cw))
        breaks = [wrap_starts(ln, cols) for ln in lines]
        row_of, n = [], 0
        for b in breaks:
            row_of.append(n)
            n += len(b)
        y1 = geo["y"] - row_of[line - 1] * geo["h"]
        on = [i + 1 for i in range(len(lines))
              if y1 + row_of[i] * geo["h"] >= geo["top"] - 1
              and y1 + (row_of[i] + len(breaks[i])) * geo["h"] <= geo["bottom"] + 1]
        first, last = (on[0], on[-1]) if on else (line, line)
        text.update({"char_w": cw, "row_of": row_of, "breaks": breaks, "cols": cols})
    else:
        y1 = geo["y"] - (line - 1) * geo["h"]
        first = max(1, int((geo["top"] - y1 + geo["h"] - 1) // geo["h"]) + 1)
        last = min(len(lines), int((geo["bottom"] - y1) // geo["h"]))
    text.update({"y_line1": y1, "visible": [first, last]})
    meta = {"kind": "vscode", "state": state, "line": line, "size": size, "scale": scale, "parts": {},
            "file": file, "side": opts.get("side", True), "text": text}
    if opts.get("beside") == "preview":
        tabs = geo["top"] - int(45 * scale)
        meta["parts"] = {"source": [geo["x0"] - 60, geo["top"], geo["right"], img.height - 40],
                         "preview": [geo["right"] + 2, geo["top"], img.width - 4, img.height - 40],
                         "preview_tab": [geo["right"] + 2, tabs, geo["right"] + 250, geo["top"]]}
    img.save(os.path.join(stills_dir, name + ".png"))
    json.dump(meta, open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
    return f"lines {first}-{last} on screen"


# --------------------------------------------------------- Command Prompt -----
def run_command(command):
    # this harness's shell sets a switch that hides sbs.bat from cmd; a student's shell does not
    env = {k: v for k, v in os.environ.items() if k.upper() != "NODEFAULTCURRENTDIRECTORYINEXEPATH"}
    env["COSMOS_SETTINGS"] = '{"GAME_RESULTS_SAVE": false}'
    env.pop("PYTHONPATH", None)
    p = subprocess.run(["cmd", "/d", "/c", command], cwd=c.STANDIN_MISSIONS, env=env, capture_output=True,
                       text=True, errors="replace", timeout=300)
    out = (p.stdout + p.stderr).replace("\r\n", "\n")
    if "is not recognized as an internal or external command" in out:
        raise RuntimeError(f"{command!r} did not run in {c.STANDIN_MISSIONS}: {out.strip()}")
    return out


def course_paths(text):
    """The stand-in's real folder, however it was printed, written as the course writes it:
    C:\\Cosmos. (The drawn prompt has always said so; now what the tool prints agrees.)"""
    import re as _re
    real = [c.STANDIN]
    drive = os.path.splitdrive(c.STANDIN)[0]
    if drive:                                          # a mapped drive is printed by Python as its \\\\server\\share
        out = subprocess.run(["net", "use", drive], capture_output=True, text=True).stdout
        m = _re.search(r"Remote name\s+(\S+)", out)
        if m:
            real.append(m.group(1) + c.STANDIN[len(drive):])
    for r in sorted(real, key=len, reverse=True):
        text = _re.sub(_re.escape(r), lambda _m: "C:\\Cosmos", text, flags=_re.I)
        text = _re.sub(_re.escape(r.replace("\\", "/")), "C:/Cosmos", text, flags=_re.I)
    if drive:                                          # `dir` names the drive on its first line
        text = text.replace(f"Volume in drive {drive[0].upper()} ", "Volume in drive C ")
    return text


BANNER = []


def run_session(commands, cwd=None, shell="cmd", timeout=900):
    """Type the commands into ONE real cmd.exe, one after another, and keep everything the
    window would show. -> ([(command, output, prompt before it)], the last prompt).
    The prompt changes when a command changes folder, as it does for a student."""
    import re as _re
    env = {k: v for k, v in os.environ.items() if k.upper() != "NODEFAULTCURRENTDIRECTORYINEXEPATH"}
    env["COSMOS_SETTINGS"] = '{"GAME_RESULTS_SAVE": false}'
    env.pop("PYTHONPATH", None)
    cwd = cwd or c.STANDIN_MISSIONS
    if shell == "powershell":                          # one command a process; PowerShell does not echo a piped prompt
        runs = []
        for cmd in commands:
            p = subprocess.run(["powershell", "-NoProfile", "-NoLogo", "-Command", cmd], cwd=cwd, env=env,
                               capture_output=True, text=True, errors="replace", timeout=timeout)
            runs.append((cmd, course_paths((p.stdout + p.stderr).replace("\r\n", "\n")),
                         "PS " + course_paths(cwd) + "> "))
        return runs, "PS " + course_paths(cwd) + "> "
    # the window reads what is typed in code page 1252, so a long dash pasted from a word
    # processor arrives as the long dash it is (this line is not one of the session's commands)
    # A command may be (command, [answers]): the answers are typed after it, for a tool that
    # stops to ask a question ("" is the Enter key). The window shows a new line after an
    # answer; a pipe does not, so one is put in after a question's "]: ".
    # (The answers reach the tool from a file: a tool that reads its answer from the pipe
    # the commands come down takes the rest of the commands with it. The window is drawn
    # with the command as the student types it.)
    typed, commands, as_typed = [], list(commands), {}
    for i, cmd in enumerate(commands):
        if isinstance(cmd, (tuple, list)):
            answers = os.path.join(c.WORK, f"_answers_{i}.txt")
            with open(answers, "w", encoding="cp1252", newline="\r\n") as f:
                f.write("".join(a + "\n" for a in cmd[1]))
            commands[i] = cmd[0]
            as_typed[cmd[0]] = f'{cmd[0]} <"{answers}"'
            typed.append(as_typed[cmd[0]])
        else:
            typed.append(cmd)
    feed = ("chcp 1252>nul\r\n" + "".join(t + "\r\n" for t in typed)).encode("cp1252", errors="replace")
    p = subprocess.run(["cmd", "/d"], cwd=cwd, env=env, input=feed, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT, timeout=timeout)     # one stream, so an error stays in its place
    raw = p.stdout.decode("cp1252", errors="replace").replace("\r\n", "\n")
    raw = _re.sub(r"(\[[Yy]/[Nn]\]: ?)(?=\S)", lambda m: m.group(1).rstrip() + "\n", raw)
    text = course_paths(raw)
    lines = text.split("\n")
    runs, at = [], 0
    BANNER.clear()                                     # what the new window said before its first prompt
    for ln in lines:
        if _re.match(r"^[A-Za-z]:\\[^>]*>", ln):
            break
        BANNER.append(ln)
    while BANNER and not BANNER[-1].strip():
        BANNER.pop()
    if not commands:
        return [], course_paths(cwd) + ">"
    for cmd in commands:
        shown = as_typed.get(cmd, cmd).encode("cp1252", errors="replace").decode("cp1252")
        hit = None
        for i in range(at, len(lines)):
            m = _re.match(r"^([A-Za-z]:\\[^>]*>)(.*)$", lines[i])
            if m and m.group(2).strip() == shown.strip():
                hit = (i, m.group(1))
                break
        if hit is None:
            raise RuntimeError(f"the session never showed the command {cmd!r}:\n{text[-800:]}")
        if runs:
            runs[-1][1] = "\n".join(lines[runs[-1][3] + 1:hit[0]])
        runs.append([cmd, "", hit[1], hit[0]])
        at = hit[0] + 1
    tail = lines[runs[-1][3] + 1:]
    while tail and not tail[-1].strip():
        tail.pop()
    last_prompt = runs[-1][2]
    if tail and _re.match(r"^[A-Za-z]:\\[^>]*>$", tail[-1].strip()):
        last_prompt = tail.pop().strip()
    runs[-1][1] = "\n".join(tail)
    return [(r[0], r[1].strip("\n"), r[2]) for r in runs], last_prompt


SESSIONS = {}


def make_session(sb, name, spec, stills_dir, mission_dir):
    """("session", [commands], {opts}): the commands typed into one real cmd.exe in the stand-in.
    opts: "state" (the mission's files first), "without" (folders of data\\missions that are not
    there meanwhile; whatever the commands make under those names is thrown away after),
    "cwd" (a folder of the stand-in, default data\\missions), "shell": "powershell",
    "show": (first, last) to draw only those commands of the session (1 is the first),
    "keep": {name: folder} copies a folder the session made into <out>\\made\\<name> before it is thrown away."""
    import wincap
    commands, opts = list(spec[1]), (spec[2] if len(spec) > 2 else {})
    cwd = os.path.join(c.STANDIN, opts["cwd"]) if opts.get("cwd") else c.STANDIN_MISSIONS
    key = (tuple(commands), cwd, opts.get("shell", "cmd"), opts.get("state"), tuple(opts.get("without", ())))
    if key not in SESSIONS:                            # several stills may show parts of one session: run it once
        with wincap.hidden(opts.get("without")):
            if opts.get("state"):
                states.materialize(sb, opts["state"], mission_dir)
            for f in opts.get("touch", ()):            # an empty file that must be there (a slip the page describes)
                open(os.path.join(c.STANDIN_MISSIONS, f), "w").close()
            try:
                runs, last = run_session(commands, cwd=cwd, shell=opts.get("shell", "cmd"))
            finally:
                for f in opts.get("touch", ()):
                    if os.path.exists(os.path.join(c.STANDIN_MISSIONS, f)):
                        os.remove(os.path.join(c.STANDIN_MISSIONS, f))
            for keep, folder in (opts.get("keep") or {}).items():
                src = os.path.join(c.STANDIN_MISSIONS, folder)
                dst = os.path.join(os.path.dirname(stills_dir), "made", keep)
                if os.path.isdir(dst):
                    shutil.rmtree(dst)
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
        SESSIONS[key] = (runs, last, list(BANNER))
    runs, last, banner = SESSIONS[key]
    full = runs
    if opts.get("show"):
        a, b = opts["show"]
        runs = runs[a - 1:b]
        if b < len(full):
            last = full[b][2]
    title = "Windows PowerShell" if opts.get("shell") == "powershell" else "Command Prompt"
    img, meta = cards.prompt(runs, title=title, last_prompt=last.rstrip() if opts.get("shell") != "powershell" else last,
                             banner=banner if opts.get("banner") else None, tail=opts.get("tail"),
                             head=opts.get("head"),
                             px_max=opts.get("px", 38))
    meta["runs"] = [{"command": r[0], "output": r[1], "prompt": r[2]} for r in full]
    img.save(os.path.join(stills_dir, name + ".png"))
    json.dump(meta, open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
    with open(os.path.join(stills_dir, name + ".txt"), "w", encoding="utf-8") as f:    # the transcript, to read
        for r in full:
            f.write(r[2] + r[0] + "\n" + r[1] + "\n\n")
    return f"{len(full)} command(s), {sum(len(r[1].splitlines()) for r in full)} lines of output"


def make_terminal(sb, name, spec, stills_dir, mission_dir, cache):
    runs = []
    for state, command in spec[1]:
        if (state, command) not in cache:
            if state is not None:
                states.materialize(sb, state, mission_dir)
            cache[(state, command)] = course_paths(run_command(command))
        runs.append((command, cache[(state, command)]))
    img, meta = cards.prompt(runs)
    meta["runs"] = [{"state": s, "command": cmd, "output": out} for (s, cmd), (_, out) in zip(spec[1], runs)]
    img.save(os.path.join(stills_dir, name + ".png"))
    json.dump(meta, open(os.path.join(stills_dir, name + ".json"), "w", encoding="utf-8"), indent=1)
    return f"{len(runs)} run(s), {sum(len(o.splitlines()) for _, o in runs)} lines of output"


def run(lecture, sb, out, redo=()):
    missing = ready()
    if missing:
        sys.exit("capture is not set up (python capture.py --setup ...): missing " + ", ".join(missing))
    stills_dir = os.path.join(out, "stills")
    mission_dir = os.path.join(c.STANDIN_MISSIONS, getattr(sb, "MISSION", "MyMission"))
    cache, todo = {}, []
    for name, spec in sb.STILLS.items():
        have = os.path.exists(os.path.join(stills_dir, name + ".png"))
        if spec[0] in ("vscode", "terminal", "session", "explorer", "web") and (
                not have or "all" in redo or name in redo):
            todo.append((name, spec))
        elif spec[0] == "game" and not have:
            print(f"  {name:16} a game still: not made here (see the lecture's game script)")
    todo.sort(key=lambda x: ("terminal", "session", "web", "explorer", "vscode").index(x[1][0]))
    for name, spec in todo:
        t = time.time()
        try:
            if spec[0] == "terminal":
                what = make_terminal(sb, name, spec, stills_dir, mission_dir, cache)
            elif spec[0] == "session":
                what = make_session(sb, name, spec, stills_dir, mission_dir)
            elif spec[0] == "explorer":
                import wincap
                if spec[2].get("state") if len(spec) > 2 else None:
                    states.materialize(sb, spec[2]["state"], mission_dir)
                what = wincap.make_explorer(sb, name, spec, stills_dir)
            elif spec[0] == "web":
                import wincap
                what = wincap.make_web(sb, name, spec, stills_dir, mission_dir)
            else:
                what = make_vscode(sb, name, spec, stills_dir, mission_dir)
            print(f"  {name:16} {spec[0]:8} {what}  ({time.time() - t:.0f}s)")
        except Exception as e:                              # one bad still must not lose the others
            print(f"  {name:16} FAILED: {e}")
    if sb.STATES:
        states.materialize(sb, list(sb.STATES)[0], mission_dir)
    print(f"  throwaway VS Code processes left running: {len(our_pids())}")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--tool", default=c.SRC_TOOL)
    ap.add_argument("--ext", default=c.SRC_VSC_EXT)
    ap.add_argument("--stop", action="store_true", help="close any throwaway VS Code window")
    ap.add_argument("--student", action="store_true",
                    help="make the stand-in look like a student's game folder (Lectures 1 to 4)")
    a = ap.parse_args()
    if a.stop:
        print("stopped", stop_vscode())
    if a.setup:
        setup(a.tool, a.ext)
    if a.student:
        student_tree()
