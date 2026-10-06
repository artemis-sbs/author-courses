"""Read a lecture's shots.py and storyboard.py, and lay the beats on one timeline.

The timeline is the scenes of shots.py end to end: each scene lasts its own "frames".
(captions.srt is laid out differently - at the script's hoped-for scene starts - so make.py
writes a draft.srt that matches the picture.)
"""
import importlib.util
import os

import config


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load(lecture):
    folder = config.lecture_dir(lecture)
    shots = _load(os.path.join(folder, "narration", "shots.py"), "shots")
    sb = _load(os.path.join(folder, "narration", "storyboard.py"), "storyboard")
    return folder, shots, sb


def _frame_of(captions, where):
    """Scene-local frame where a beat starts: caption number, with an optional fraction."""
    i = int(where)
    a, b = captions[i][1], captions[i][2]
    if i == 0 and where == 0:
        return 0
    return int(round(a + (where - i) * (b - a)))


def plan(shots, sb):
    """-> (beats, scenes, total_frames). A beat: scene, n, start, length (global frames),
    still, marks, dim, crop, chip, name (the composed frame's file name, no extension)."""
    beats, scenes, cursor, problems = [], [], 0, []
    for shot in shots.SHOTS:
        sid = shot["id"]
        entry = sb.BOARD.get(sid)
        if not entry:
            problems.append(f"{sid}: no storyboard entry")
            entry = {"step": None, "beats": [{"from": 0, "still": "MISSING_" + sid}]}
        starts = []
        for b in entry["beats"]:
            if int(b["from"]) >= len(shot["captions"]):
                problems.append(f"{sid}: a beat starts on caption {b['from']}, and there are "
                                f"{len(shot['captions'])}")
                continue
            starts.append((_frame_of(shot["captions"], b["from"]), b))
        starts.sort(key=lambda x: x[0])
        if not starts or starts[0][0] != 0:
            problems.append(f"{sid}: the first beat must start on caption 0")
        # A beat placed PART WAY through a sentence ("from": 2.5) is placed by a guessed
        # fraction, and once the real voice re-times that sentence it can come out too
        # short to read. That stopped the whole build. Fold such a beat into the one
        # before it instead (the picture simply holds a little longer) and say so.
        while len(starts) > 1:
            short = None
            for n, (at, b) in enumerate(starts):
                end = starts[n + 1][0] if n + 1 < len(starts) else shot["frames"]
                if end - at < config.MIN_BEAT:
                    short = n
                    break
            if short is None:
                break
            drop = short if short > 0 else 1
            print(f"  note: {sid}: the beat at {starts[drop][1]['from']} was folded into its "
                  f"neighbour (too short to read once timed)")
            del starts[drop]
        for n, (at, b) in enumerate(starts):
            end = starts[n + 1][0] if n + 1 < len(starts) else shot["frames"]
            if end - at < config.MIN_BEAT:
                problems.append(f"{sid} beat {n}: {end - at} frames is too short to read")
            beats.append({
                "scene": sid, "n": n, "start": cursor + at, "length": end - at,
                "still": b["still"], "marks": list(b.get("marks", [])), "dim": bool(b.get("dim")),
                "crop": b.get("crop"), "from": b["from"], "move": b.get("move", True),
                "chip": entry.get("step") if at < 3 * config.FPS else None,
                "name": f"{sid[:3]}_{n:02d}",
            })
        scenes.append({"id": sid, "title": shot["title"], "start": cursor, "frames": shot["frames"],
                       "captions": shot["captions"]})
        cursor += shot["frames"]
    for name in {b["still"] for b in beats}:
        if name not in sb.STILLS and not name.startswith("MISSING_"):
            problems.append(f"still {name} is used and not declared in STILLS")
    return beats, scenes, cursor, problems
