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
    python game.py <lecture> wait  <seconds>            a pause, recorded for the replay
    python game.py <lecture> keep  <shot name> <still name>   a screenshot becomes a still of the lecture
    python game.py <lecture> log   <name>               copies the probe's two logs to <out>/game/<name>.<log> and prints them
    python game.py <lecture> stop                       stops the game and deletes _pic_probe
    python game.py <lecture> steps                      prints what has been recorded
    python game.py <lecture> forget                     empties the recording
    python game.py <lecture> replay [--from N] [--only-keeps]
        runs the recording again, unattended: start, clicks, shots, keeps and stop, with the
        pauses that were left between them

RECORDED. start, click, shot, wait, keep and stop are appended to the lecture's
narration/capture_steps.py as they run (--no-record to leave it alone), with the time since
the step before, so a re-shoot is `replay` instead of another hand session. A scouting
sitting that wanders can `forget` and start again, or the file can be edited by hand: it is
one step per line.

THE SAME GAME EACH TIME. Every launch passes seed=<--seed> (default 7), which the library
applies before the story's first line runs, so faces, names and spawns repeat between the
scouting sitting, the filming sitting and a replay - and the marks placed on a still stay
on what they point at. (Needs an sbs_utils with that, from 2026-10-17; older ones ignore it.)

THE PLAYER'S SAVES ARE NOT TOUCHED. An Open Universe probe (template "ou", or --sandbox)
is made one level down, in data/missions/_sandbox/, so the saves it writes land in
_sandbox/common_data. And on every run, whatever the template, start copies
data/missions/common_data/saves aside and stop puts back any file the run changed, and moves
out any file it made - saying which.

Screenshots land in <out>/game/. eng.ps1 does the looking and the clicking; it REFUSES to
click unless the game's window really is in front. If it refuses, do not fight it.
One game at a time. Every run sets GAME_RESULTS_SAVE false.

The template is the storyboard's TEMPLATE ("amd", "away", "ou"), or else "away" when the
state has a tile map or a tileset in it, and "amd" when it has not. `-t away` brings the art
packs a tile map is drawn with (story.json's shared_media, settings.yaml's TILE_ART); the
state's own files are laid over it, so the probe is the student's folder, art and all.
"""
import argparse
import ast
import json
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
#: Written into every probe this tool makes. A probe can be named after the STUDENT's
#: mission (`--as-mission`, so the end screen does not read "_pic_probe" on film), and a
#: folder of that name could be somebody's real mission - this tool deletes only a folder
#: carrying its own mark.
PROBE_MARK = ".pic_probe"
SANDBOX = "_sandbox"
PY = os.path.join(MISSIONS, "..", "..", "PyRuntime", "python.exe")
ENV = dict(os.environ, COSMOS_SETTINGS='{"GAME_RESULTS_SAVE": false}')
SAVES = os.path.join(MISSIONS, "common_data", "saves")
STATE = os.path.join(MISSIONS, f"{PROBE}.json")      # where the running probe is, for stop
SANDBOX_TEMPLATES = ("ou",)
GAP_MIN, GAP_MAX = 1.0, 90.0                         # a replay's pause between two steps


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


def probe_name(sandbox):
    """The probe as `sbs` names it: a folder of data/missions, or one level down."""
    return f"{SANDBOX}/{PROBE}" if sandbox else PROBE


def probe_dir(sandbox):
    return os.path.join(MISSIONS, *probe_name(sandbox).split("/"))


def probe_remove(probe):
    """Delete a probe folder - only one this tool made (its mark, or the stock name)."""
    if not os.path.isdir(probe):
        return
    if os.path.basename(probe) != "_pic_probe" and \
            not os.path.exists(os.path.join(probe, PROBE_MARK)):
        sys.exit(f"{probe} is not a probe this tool made (no {PROBE_MARK}) - not deleting it")
    try:
        shutil.rmtree(probe)
    except OSError:
        # A running game holds a log open, and rmtree has already taken the mark with
        # the files it got to - put it back, or the next run refuses its own probe.
        if os.path.isdir(probe):
            open(os.path.join(probe, PROBE_MARK), "w").close()
        raise


def wants_sandbox(lecture, asked, state="final"):
    """--sandbox / --no-sandbox, else on for a template that writes saves. Judged on the
    state being run: not every lecture has a "final" (C4-01's last state is "pasted")."""
    if asked is not None:
        return asked
    _, _, sb = board.load(lecture)
    return template_of(sb, states.files_of(sb, state)) in SANDBOX_TEMPLATES


# --- the player's saves --------------------------------------------------------------------

def saves_backup_dir(lecture):
    return os.path.join(c.out_dir(lecture), "game", "_saves_backup")


def saves_snapshot():
    """{file: (size, mtime)} of data/missions/common_data/saves, recursively."""
    seen = {}
    for root, _dirs, names in os.walk(SAVES):
        for n in names:
            p = os.path.join(root, n)
            st = os.stat(p)
            seen[os.path.relpath(p, SAVES)] = (st.st_size, st.st_mtime_ns)
    return seen


def saves_guard_begin(lecture):
    """Copy the player's saves aside before the game can write to them."""
    back = saves_backup_dir(lecture)
    if os.path.isdir(back):
        shutil.rmtree(back)
    os.makedirs(back)
    if os.path.isdir(SAVES):
        shutil.copytree(SAVES, os.path.join(back, "saves"))
    with open(os.path.join(back, "snapshot.json"), "w", encoding="utf-8") as fh:
        json.dump(saves_snapshot(), fh)
    print(f"player saves copied aside: {len(saves_snapshot())} files")


def saves_guard_end(lecture):
    """Put back any save the run changed, and move out any it made. -> what was undone."""
    back = saves_backup_dir(lecture)
    snap = os.path.join(back, "snapshot.json")
    if not os.path.exists(snap):
        print("player saves: no copy from start to compare with - CHECK", SAVES, "by hand")
        return []
    with open(snap, encoding="utf-8") as fh:
        before = {k: tuple(v) for k, v in json.load(fh).items()}
    now = saves_snapshot()
    if os.environ.get("PIC_KEEP_SAVES"):
        # A TWO-SITTING STILL (Class 5, Lecture 16's Continue): keep what THIS game wrote,
        # so the next start can lay it back with PIC_RESUME_SAVES. The player's own saves
        # are still put back below either way.
        kept = os.path.join(back, "..", "_run_saves")
        if os.path.isdir(kept):
            shutil.rmtree(kept)
        for rel, stamp in now.items():
            if before.get(rel) != stamp:
                dest = os.path.join(kept, rel)
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                shutil.copy2(os.path.join(SAVES, rel), dest)
                print(f"kept the run's save {rel} for the next sitting")
    undone = []
    for rel, stamp in now.items():
        if rel not in before:
            dest = os.path.join(back, "made_by_the_run", rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.move(os.path.join(SAVES, rel), dest)
            undone.append(f"{rel} (new - moved to {dest})")
        elif stamp != before[rel]:
            shutil.copy2(os.path.join(back, "saves", rel), os.path.join(SAVES, rel))
            undone.append(f"{rel} (changed - put back)")
    for rel in before:
        if rel not in now:
            shutil.copy2(os.path.join(back, "saves", rel), os.path.join(SAVES, rel))
            undone.append(f"{rel} (deleted - put back)")
    if undone:
        print("PLAYER SAVES THE RUN TOUCHED, undone:")
        for u in undone:
            print("  ", u)
    else:
        print("player saves: untouched")
    return undone


# --- the probe -----------------------------------------------------------------------------

def sandbox_lib():
    """_sandbox/__lib__ as a junction to data/missions/__lib__. The engine's loader looks for
    the libraries beside the mission's folder (PyAddons/sbslibs.py: <parent>/__lib__), so a
    mission one level down finds none without it."""
    link = os.path.join(MISSIONS, SANDBOX, "__lib__")
    if os.path.isdir(link):
        return
    made = subprocess.run(["cmd", "/c", "mklink", "/J", link, os.path.join(MISSIONS, "__lib__")],
                          capture_output=True, text=True)
    if not os.path.isdir(link):
        sys.exit("could not make the sandbox's __lib__ junction:\n" + made.stdout + made.stderr)
    print(f"{SANDBOX}/__lib__ -> __lib__ (junction)")


def build(lecture, state, patches, amd_patches=(), sandbox=False):
    """Make _pic_probe for the state: the template, then every file of the state over it.
    -> the probe's folder. Starts and stops nothing."""
    _, _, sb = board.load(lecture)
    probe = probe_dir(sandbox)
    probe_remove(probe)
    os.makedirs(os.path.dirname(probe), exist_ok=True)
    if sandbox:
        sandbox_lib()
    files = states.files_of(sb, state)
    template = template_of(sb, files)
    source = getattr(sb, "PROBE_FROM", None)
    if source:
        # A COPY OF A SHIPPED MISSION (Class 5, Lecture 14's AdmiralLab is a copy of
        # OpenUniverse): its committed files, then the state over them. No template would
        # register the mission's own maps.
        os.makedirs(probe, exist_ok=True)
        arch = subprocess.run(["git", "-C", os.path.join(MISSIONS, source), "archive", "HEAD"],
                              capture_output=True)
        if arch.returncode != 0:
            sys.exit(f"PROBE_FROM {source}: git archive failed: {arch.stderr.decode()[-400:]}")
        subprocess.run(["tar", "-x", "-C", probe], input=arch.stdout, check=True)
        what = f"a copy of {source}"
    else:
        made = subprocess.run([PY, "sbs.pyz", "create", probe_name(sandbox), "-t", template,
                               "--title", "Picture Probe", "-y"],
                              cwd=MISSIONS, env=ENV, capture_output=True, text=True)
        if not os.path.isdir(probe):
            sys.exit("sbs create did not make the probe:\n" + made.stdout + made.stderr)
        what = f"the '{template}' template"
    open(os.path.join(probe, PROBE_MARK), "w").close()
    print(f"probe made from {what}" + (f" in {SANDBOX}/" if sandbox else ""))
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


def start(lecture, state, patches, consoles, wait, amd_patches=(), sandbox=False, seed=7):
    stop_game()
    saves_guard_begin(lecture)
    kept = os.path.join(saves_backup_dir(lecture), "..", "_run_saves")
    if os.environ.get("PIC_RESUME_SAVES"):
        # The second sitting: the saves the first one kept (PIC_KEEP_SAVES), laid in AFTER
        # the player's own were copied aside, so the stop still puts the player's back.
        if not os.path.isdir(kept):
            sys.exit("PIC_RESUME_SAVES: no kept saves - stop the first sitting with PIC_KEEP_SAVES=1")
        for root, _dirs, names in os.walk(kept):
            for n in names:
                rel = os.path.relpath(os.path.join(root, n), kept)
                os.makedirs(os.path.dirname(os.path.join(SAVES, rel)), exist_ok=True)
                shutil.copy2(os.path.join(root, n), os.path.join(SAVES, rel))
                print(f"resumed the kept save {rel}")
    build(lecture, state, patches, amd_patches, sandbox)
    with open(STATE, "w", encoding="utf-8") as fh:
        json.dump({"lecture": lecture, "sandbox": sandbox, "state": state, "probe": PROBE}, fh)
    args = [PY, "sbs.pyz", "run", consoles, "-m", probe_name(sandbox), "map=0"]
    if seed:
        args.append(f"seed={seed}")
    subprocess.Popen(args, cwd=MISSIONS, env=ENV, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(wait)
    print(eng("-Action", "list"))


def running_state():
    """The state the running probe was started on, as start recorded it."""
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            return json.load(fh).get("state", "final")
    return "final"


def stop(lecture):
    stop_game()
    time.sleep(2)
    global PROBE
    sandbox = False
    if os.path.exists(STATE):
        with open(STATE, encoding="utf-8") as fh:
            st = json.load(fh)
        sandbox = st.get("sandbox", False)
        PROBE = st.get("probe") or PROBE
        os.remove(STATE)
    probe = probe_dir(sandbox)
    log = os.path.join(probe, "mast.runtime.log")
    if os.path.exists(log):
        print("mast.runtime.log bytes:", os.path.getsize(log))
    probe_remove(probe)
    print("game stopped;", probe_name(sandbox), "deleted:", not os.path.isdir(probe))
    saves_guard_end(lecture)


# --- the recording -------------------------------------------------------------------------

def steps_file(lecture):
    return os.path.join(c.lecture_dir(lecture), "narration", "capture_steps.py")


HEADER = '''"""The game stills of this lecture, as game.py made them - `game.py <lecture> replay`
makes them again. One step per line; `gap` is the pause before it, in seconds."""
'''


def steps_load(lecture):
    p = steps_file(lecture)
    if not os.path.exists(p):
        return []
    with open(p, encoding="utf-8") as fh:
        text = fh.read()
    return ast.literal_eval(text.split("STEPS = ", 1)[1]) if "STEPS = " in text else []


def steps_save(lecture, steps):
    lines = [HEADER, "STEPS = ["]
    lines += [f"    {s!r}," for s in steps]
    lines.append("]")
    with open(steps_file(lecture), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")


def record(lecture, step):
    steps = steps_load(lecture)
    last = os.path.join(c.out_dir(lecture), "game", "_last_step_time")
    now = time.time()
    gap = 0.0
    if steps and os.path.exists(last) and step["op"] != "start":
        with open(last) as fh:
            gap = round(min(GAP_MAX, max(0.0, now - float(fh.read() or now))), 1)
    step = dict(step, gap=gap)
    steps.append(step)
    steps_save(lecture, steps)
    with open(last, "w") as fh:
        fh.write(str(now))


def run_step(lecture, step, shots, out):
    """Do one recorded step. -> True when it worked."""
    op = step["op"]
    if op == "start":
        start(lecture, step.get("state", "final"), step.get("patch", []), step.get("consoles", "server,helm,science"),
              step.get("wait", 45), step.get("patch_amd", []), step.get("sandbox", False), step.get("seed", 7))
    elif op == "stop":
        stop(lecture)
    elif op == "wait":
        time.sleep(float(step["seconds"]))
    elif op in ("shot", "click"):
        pid = windows().get(step["window"].lower())
        if not pid:
            print(f"no game window titled {step['window']}: {windows()}")
            return False
        if op == "shot":
            print(eng("-Action", "shot", "-ProcId", pid, "-Name", step["name"], "-OutDir", shots))
        else:
            said = eng("-Action", "click", "-ProcId", pid, "-FracX", step["x"], "-FracY", step["y"],
                       "-Name", step["name"], "-OutDir", shots)
            print(said)
            if "refus" in said.lower():
                return False
    elif op == "keep":
        src = os.path.join(shots, step["shot"] + ".png")
        dst = os.path.join(out, "stills", step["still"] + ".png")
        if not os.path.exists(src):
            print("no screenshot", src)
            return False
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        shutil.copyfile(src, dst)
        print("kept", dst)
        _, _, sb = board.load(lecture)
        spec = sb.STILLS.get(step["still"])
        if spec:                                      # what it shows, for make.py --stale
            import stale
            stale.stamp(sb, os.path.dirname(dst), step["still"], spec, running_state())
        else:
            print(f"  (not in the storyboard's STILLS: {step['still']})")
    else:
        print("unknown step", step)
        return False
    return True


def replay(lecture, shots, out, first=0, only_keeps=False):
    steps = steps_load(lecture)
    if not steps:
        sys.exit(f"nothing recorded in {steps_file(lecture)}")
    failed = []
    started = False
    try:
        for i, step in enumerate(steps):
            if i < first:
                continue
            started = started or step["op"] == "start"
            if only_keeps and step["op"] != "keep":
                continue
            if step.get("gap") and step["op"] != "start" and not only_keeps:
                time.sleep(min(GAP_MAX, max(GAP_MIN, step["gap"])))
            print(f"[{i}] {step}")
            if not run_step(lecture, step, shots, out):
                failed.append(i)
                if step["op"] in ("start", "click"):  # the rest would land on the wrong screen
                    print(f"step {i} failed; stopping the replay")
                    break
    finally:
        if started and steps[-1]["op"] != "stop" and not only_keeps:
            stop(lecture)
    print("replay done" + (f"; FAILED steps {failed}" if failed else ""))
    return not failed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lecture")
    ap.add_argument("op")
    ap.add_argument("args", nargs="*")
    ap.add_argument("--state", default="final")
    ap.add_argument("--as-mission", action="store_true",
                    help="name the probe after the lecture's MISSION (for filming: the end screen)")
    ap.add_argument("--patch", action="append", default=[])
    ap.add_argument("--patch-amd", action="append", default=[],
                    help="the same, for the fact sheet; like --patch, a PROBE-ONLY change, and it is printed")
    ap.add_argument("--consoles", default="server,helm,science")
    ap.add_argument("--wait", type=int, default=45)
    ap.add_argument("--seed", type=int, default=7, help="seed= on the launch line; 0 for none")
    ap.add_argument("--sandbox", dest="sandbox", action="store_true", default=None,
                    help=f"make the probe in {SANDBOX}/ (default: on for an Open Universe template)")
    ap.add_argument("--no-sandbox", dest="sandbox", action="store_false")
    ap.add_argument("--no-record", action="store_true", help="do not add this step to capture_steps.py")
    ap.add_argument("--from", dest="first", type=int, default=0, help="replay: start at this step")
    ap.add_argument("--only-keeps", action="store_true",
                    help="replay: only copy the screenshots already taken into stills")
    a = ap.parse_args()
    if a.as_mission or os.environ.get("PIC_AS_MISSION"):
        # THE STUDENT'S NAME ON THE PROBE: the end screen names the mission folder, and on
        # film it must read what the student's reads (the storyboard's MISSION).
        global PROBE
        _, _, sb = board.load(a.lecture)
        PROBE = getattr(sb, "MISSION", None) or PROBE
    out = c.out_dir(a.lecture)
    shots = os.path.join(out, "game")
    os.makedirs(shots, exist_ok=True)
    rec = not a.no_record
    if a.op == "start":
        sandbox = wants_sandbox(a.lecture, a.sandbox, a.state)
        step = {"op": "start", "state": a.state, "patch": a.patch, "patch_amd": a.patch_amd,
                "consoles": a.consoles, "wait": a.wait, "sandbox": sandbox, "seed": a.seed}
        run_step(a.lecture, step, shots, out)
        if rec:                                       # after: the wait is not a gap
            record(a.lecture, step)
    elif a.op == "build":
        build(a.lecture, a.state, a.patch, a.patch_amd, wants_sandbox(a.lecture, a.sandbox, a.state))
    elif a.op == "list":
        print(eng("-Action", "list"))
    elif a.op in ("shot", "click", "wait", "keep", "stop"):
        if a.op == "shot":
            step = {"op": "shot", "window": a.args[0], "name": a.args[1]}
        elif a.op == "click":
            step = {"op": "click", "window": a.args[0], "x": float(a.args[1]), "y": float(a.args[2]),
                    "name": a.args[3]}
        elif a.op == "wait":
            step = {"op": "wait", "seconds": float(a.args[0])}
        elif a.op == "keep":
            step = {"op": "keep", "shot": a.args[0], "still": a.args[1]}
        else:
            step = {"op": "stop"}
        ok = run_step(a.lecture, step, shots, out)
        if rec and ok:
            record(a.lecture, step)
        if not ok:
            sys.exit(1)
    elif a.op == "log":                               # what the game wrote, kept before stop deletes the probe
        sandbox = False
        if os.path.exists(STATE):
            with open(STATE, encoding="utf-8") as fh:
                sandbox = json.load(fh).get("sandbox", False)
        for f in ("mast.runtime.log", "mast.compile.log"):
            src = os.path.join(probe_dir(sandbox), f)
            if os.path.exists(src):
                dst = os.path.join(shots, f"{a.args[0]}.{f}")
                shutil.copyfile(src, dst)
                print(f"{f}: {os.path.getsize(src)} bytes -> {dst}")
                print(open(src, encoding="utf-8", errors="replace").read())
            else:
                print(f"{f}: not there")
    elif a.op == "steps":
        for i, s in enumerate(steps_load(a.lecture)):
            print(f"[{i}] {s}")
    elif a.op == "forget":
        steps_save(a.lecture, [])
        print("recording emptied:", steps_file(a.lecture))
    elif a.op == "replay":
        sys.exit(0 if replay(a.lecture, shots, out, a.first, a.only_keeps) else 1)
    else:
        sys.exit(f"unknown op {a.op}")


if __name__ == "__main__":
    main()
