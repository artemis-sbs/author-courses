"""Stills of the REAL game, for the few scenes that show it. Not part of make.py --capture:
it starts the engine, and its clicks need the game's window in front, so a person should
know it is running.

    python game.py <lecture> start [--state final] [--patch "old=>new"] [--consoles server,helm,science]
        makes the probe mission _pic_probe from the template (sbs create), lays the state's
        files over it, applies any --patch to its story.mast, and starts the game on it
    python game.py <lecture> list                       the game's windows and their process ids
    python game.py <lecture> shot  <window> <name>      screenshot a window (helm, science, server)
    python game.py <lecture> click <window> <x> <y> <name>    click at a fraction of the window, then screenshot
    python game.py <lecture> keep  <shot name> <still name>   a screenshot becomes a still of the lecture
    python game.py <lecture> log   <name>               copies the probe's two logs to <out>/game/<name>.<log> and prints them
    python game.py <lecture> stop                       stops the game and deletes _pic_probe

Screenshots land in <out>/game/. eng.ps1 does the looking and the clicking; it REFUSES to
click unless the game's window really is in front. If it refuses, do not fight it.
One game at a time. Every run sets GAME_RESULTS_SAVE false.
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


def start(lecture, state, patches, consoles, wait, amd_patches=()):
    _, _, sb = board.load(lecture)
    probe = os.path.join(MISSIONS, PROBE)
    stop_game()
    if os.path.isdir(probe):
        shutil.rmtree(probe)
    made = subprocess.run([PY, "sbs.pyz", "create", PROBE, "-t", "amd", "--title", "Picture Probe", "-y"],
                          cwd=MISSIONS, env=ENV, capture_output=True, text=True)
    if not os.path.isdir(probe):
        sys.exit("sbs create did not make the probe:\n" + made.stdout + made.stderr)
    files = states.files_of(sb, state)
    template_story = open(os.path.join(probe, "story.mast"), encoding="utf-8", newline="").read().replace("\r\n", "\n")
    print("story.mast of the state is the template's:", files.get("story.mast") == template_story)
    for f in (sb.FILE, "story.mast"):                 # the lecture's content; the rest stays the template's
        text = files[f]
        if f in ("story.mast", sb.FILE):
            for p in (patches if f == "story.mast" else amd_patches):
                old, new = p.split("=>", 1)
                if text.count(old) != 1:
                    sys.exit(f"patch {old!r} is in {f} {text.count(old)} times, wanted once")
                text = text.replace(old, new)
                print(f"PROBE-ONLY change to {f}: {old!r} -> {new!r}")
        with open(os.path.join(probe, f), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(text)
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
