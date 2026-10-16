"""Stills of the REAL game, for the few scenes that show it. Not part of make.py --capture:
it starts the engine, and its clicks need the game's window in front, so a person should
know it is running.

    python game.py <lecture> start [--state final] [--patch "old=>new"] [--consoles server,helm,science]
        makes the probe mission _pic_probe from the template (sbs create), lays EVERY file of
        the state over it (subfolders too: a tile map's ground\\), applies any --patch to its
        story.mast, and starts the game on it
    python game.py <lecture> build [--state final] [--patch ...]
        the same probe, and nothing started (nor stopped): to look at what start would run
    python game.py <lecture> list                       the game's windows and their process ids
    python game.py <lecture> shot  <window> <name>      screenshot a window (helm, science, server)
    python game.py <lecture> click <window> <x> <y> <name>    click at a fraction of the window, then screenshot
    python game.py <lecture> keep  <shot name> <still name>   a screenshot becomes a still of the lecture
    python game.py <lecture> log   <name>               copies the probe's two logs to <out>/game/<name>.<log> and prints them
    python game.py <lecture> stop                       stops the game and deletes _pic_probe

Screenshots land in <out>/game/. eng.ps1 does the looking and the clicking; it REFUSES to
click unless the game's window really is in front. If it refuses, do not fight it.
One game at a time. Every run sets GAME_RESULTS_SAVE false.

The template is the storyboard's TEMPLATE ("amd", "away"), or else "away" when the state has
a tile map or a tileset in it, and "amd" when it has not. `-t away` brings the art packs a
tile map is drawn with (story.json's shared_media, settings.yaml's TILE_ART); the state's own
files are laid over it, so the probe is the student's folder, art and all.
"""
import argparse
import os
import shutil
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import board  # noqa: E402
import config as c  # noqa: E402
import states  # noqa: E402

MISSIONS = os.environ.get("PICTURE_GAME_MISSIONS", r"E:\a\Cosmos-dev\data\missions")
PROBE = "_pic_probe"
PY = os.path.join(MISSIONS, "..", "..", "PyRuntime", "python.exe")
ENV = dict(os.environ, COSMOS_SETTINGS='{"GAME_RESULTS_SAVE": false}')


def eng(*args):
    out = subprocess.run(["powershell", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File",
                          os.path.join(HERE, "eng.ps1"), *[str(a) for a in args]],
                         capture_output=True, text=True).stdout
    return out


def windows():
    """{title: process id} for the game's windows."""
    found = {}
    for ln in eng("-Action", "list").splitlines():
        parts = ln.split()
        if len(parts) >= 4 and parts[0].isdigit():
            found[parts[-1].lower()] = int(parts[0])
    return found


def stop_game():
    subprocess.run(["taskkill", "/IM", "Artemis3-x64-release.exe", "/F"], capture_output=True)


def template_of(sb, files):
    """The `sbs create -t` template a lecture's probe is made from."""
    named = getattr(sb, "TEMPLATE", None)
    if named:
        return named
    return "away" if any(f.endswith((".tiles", ".tileset")) for f in files) else "amd"


def build(lecture, state, patches, amd_patches=()):
    """Make _pic_probe for the state: the template, then every file of the state over it.
    -> the probe's folder. Starts and stops nothing."""
    _, _, sb = board.load(lecture)
    probe = os.path.join(MISSIONS, PROBE)
    if os.path.isdir(probe):
        shutil.rmtree(probe)
    files = states.files_of(sb, state)
    template = template_of(sb, files)
    made = subprocess.run([PY, "sbs.pyz", "create", PROBE, "-t", template, "--title", "Picture Probe", "-y"],
                          cwd=MISSIONS, env=ENV, capture_output=True, text=True)
    if not os.path.isdir(probe):
        sys.exit("sbs create did not make the probe:\n" + made.stdout + made.stderr)
    print(f"probe made from the '{template}' template")
    if patches and "story.mast" not in files:
        sys.exit("--patch: the state has no story.mast")
    for f in sorted(files):                           # the lecture's whole folder; the rest stays the template's
        text = files[f]
        want = patches if f == "story.mast" else amd_patches if f == states.key(sb.FILE) else ()
        for p in want:
            old, new = p.split("=>", 1)
            if text.count(old) != 1:
                sys.exit(f"patch {old!r} is in {f} {text.count(old)} times, wanted once")
            text = text.replace(old, new)
            print(f"PROBE-ONLY change to {f}: {old!r} -> {new!r}")
        dest = os.path.join(probe, *f.split("/"))
        before = None
        if os.path.exists(dest):
            with open(dest, encoding="utf-8", newline="") as fh:
                before = fh.read().replace("\r\n", "\n")
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
        said = "as the template has it" if before == text else "the state's" if before is not None else "the state's (new)"
        print(f"  {f:30} {said}")
    for root, _dirs, names in os.walk(probe):         # what only the template has
        for n in names:
            rel = states.key(os.path.relpath(os.path.join(root, n), probe))
            if rel in files or "__pycache__" in rel:
                continue
            if n.endswith((".tiles", ".tileset")):     # another area would join the mission's map
                os.remove(os.path.join(root, n))
                print(f"  {rel:30} the template's, REMOVED (not in the state)")
            else:
                print(f"  {rel:30} the template's, kept (not in the state)")
    return probe


def start(lecture, state, patches, consoles, wait, amd_patches=()):
    stop_game()
    build(lecture, state, patches, amd_patches)
    subprocess.Popen([PY, "sbs.pyz", "run", consoles, "-m", PROBE, "map=0"], cwd=MISSIONS, env=ENV,
                     stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(wait)
    print(eng("-Action", "list"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lecture")
    ap.add_argument("op")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--state", default="final")
    ap.add_argument("--patch", action="append", default=[])
    ap.add_argument("--patch-amd", action="append", default=[],
                    help="the same, for the fact sheet; like --patch, a PROBE-ONLY change, and it is printed")
    ap.add_argument("--consoles", default="server,helm,science")
    ap.add_argument("--wait", type=int, default=45)
    a = ap.parse_args()
    out = c.out_dir(a.lecture)
    shots = os.path.join(out, "game")
    os.makedirs(shots, exist_ok=True)
    if a.op == "start":
        start(a.lecture, a.state, a.patch, a.consoles, a.wait, a.patch_amd)
    elif a.op == "build":
        build(a.lecture, a.state, a.patch, a.patch_amd)
    elif a.op == "list":
        print(eng("-Action", "list"))
    elif a.op in ("shot", "click"):
        pid = windows().get(a.args[0].lower())
        if not pid:
            sys.exit(f"no game window titled {a.args[0]}: {windows()}")
        if a.op == "shot":
            print(eng("-Action", "shot", "-ProcId", pid, "-Name", a.args[1], "-OutDir", shots))
        else:
            print(eng("-Action", "click", "-ProcId", pid, "-FracX", a.args[1], "-FracY", a.args[2],
                      "-Name", a.args[3], "-OutDir", shots))
    elif a.op == "keep":
        src = os.path.join(shots, a.args[0] + ".png")
        dst = os.path.join(out, "stills", a.args[1] + ".png")
        shutil.copyfile(src, dst)
        print("kept", dst)
    elif a.op == "log":                               # what the game wrote, kept before stop deletes the probe
        for f in ("mast.runtime.log", "mast.compile.log"):
            src = os.path.join(MISSIONS, PROBE, f)
            if os.path.exists(src):
                dst = os.path.join(shots, f"{a.args[0]}.{f}")
                shutil.copyfile(src, dst)
                print(f"{f}: {os.path.getsize(src)} bytes -> {dst}")
                print(open(src, encoding="utf-8", errors="replace").read())
            else:
                print(f"{f}: not there")
    elif a.op == "stop":
        stop_game()
        time.sleep(2)
        probe = os.path.join(MISSIONS, PROBE)
        log = os.path.join(probe, "mast.runtime.log")
        if os.path.exists(log):
            print("mast.runtime.log bytes:", os.path.getsize(log))
        if os.path.isdir(probe):
            shutil.rmtree(probe)
        print("game stopped;", PROBE, "deleted:", not os.path.isdir(probe))
    else:
        sys.exit(f"unknown op {a.op}")


if __name__ == "__main__":
    main()
