"""Make the picture for one lecture: a silent draft video cut to its narration.

    python make.py c1-05-the-shape-of-a-record              compose, assemble, encode, contact sheet
    python make.py c1-05-the-shape-of-a-record --capture    first make the stills that are missing
                                                            (opens a throwaway VS Code window; see README)
    python make.py <lecture> --capture --redo ed_top term1  make those stills again
    python make.py <lecture> --capture --redo all
    python make.py <lecture> --plan                         print the beats and stop
    python make.py <lecture> --no-video                     frames and contact sheet only (seconds)

Reads <lecture>/narration/shots.py (the narration, from narration.py) and storyboard.py
(what is on screen for each caption). Writes R:/cosmos/courses/<c1_05>/: stills/, frames/,
contact.png, draft.mp4, draft.srt, draft.blend.
"""
import argparse
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import board  # noqa: E402
import compose  # noqa: E402
import config as c  # noqa: E402
import states  # noqa: E402


def stamp(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def write_srt(folder, out, scenes):
    """The written sentences, timed to THIS picture (captions.srt is timed to the script's
    hoped-for scene starts, which the picture does not follow)."""
    written = {}
    path = os.path.join(folder, "narration", "lines.txt")
    if os.path.exists(path):
        for ln in open(path, encoding="utf-8"):
            if "\t" in ln:
                k, v = ln.rstrip("\n").split("\t", 1)
                written[k] = v
    rows, n = [], 0
    for sc in scenes:
        for i, (spoken, a, b) in enumerate(sc["captions"]):
            n += 1
            text = written.get(f"{sc['id']}_{i}", spoken)
            rows.append(f"{n}\n{stamp((sc['start'] + a) / c.FPS)} --> {stamp((sc['start'] + b) / c.FPS)}\n{text}\n")
    with open(os.path.join(out, "draft.srt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(rows))


def sounds_for(lecture, scenes):
    folder = os.path.join(c.VOICE_ROOT, c.short_name(lecture))
    out = []
    for sc in scenes:
        for i, (_, a, _b) in enumerate(sc["captions"]):
            wav = os.path.join(folder, f"{sc['id']}_{i}.wav")
            if os.path.exists(wav):
                out.append({"name": f"{sc['id']}_{i}", "file": wav, "start": sc["start"] + a})
    return out


def blender(edl_path, op):
    cmd = [c.BLENDER, "-b", "--factory-startup", "--python", os.path.join(HERE, "blend_assemble.py"),
           "--", edl_path, op]
    proc = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    lines = (proc.stdout + proc.stderr).splitlines()
    for ln in lines:
        if ln.startswith("ASSEMBLE") or "Error" in ln or ln.startswith(("Traceback", "  File ")):
            print("  " + ln)
    if proc.returncode:
        print("\n".join(lines[-25:]))
        sys.exit(f"blender exited {proc.returncode}")


def frame_matches(rendered, b):
    """Is the frame Blender rendered the frame we gave it? b is the picture expected there
    (pushed in as far as the edit says it is by then). -> (ok, what was measured)"""
    from PIL import Image, ImageChops, ImageStat
    if not os.path.exists(rendered):
        return False, "no file"
    a = Image.open(rendered).convert("RGB")
    if a.size != b.size:
        return False, f"size {a.size}"
    spread = sum(ImageStat.Stat(a).stddev) / 3
    diff = sum(ImageStat.Stat(ImageChops.difference(a, b)).mean) / 3
    return (spread > 4 and diff < 4), f"spread {spread:.1f}, difference from the expected frame {diff:.2f}"


def sheets(out, beats, paths):
    from PIL import Image, ImageDraw
    import cards
    tw, th, label, cols, per = 480, 270, 34, 6, 42
    made = []
    for old in os.listdir(out):
        if old.startswith("contact") and old.endswith(".png"):
            os.remove(os.path.join(out, old))
    for page, at in enumerate(range(0, len(beats), per)):
        chunk = beats[at:at + per]
        rows = (len(chunk) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * tw, rows * (th + label)), (16, 16, 18))
        d = ImageDraw.Draw(sheet)
        f = cards.font(c.FONT_TEXT, 20)
        for i, b in enumerate(chunk):
            x, y = (i % cols) * tw, (i // cols) * (th + label)
            sheet.paste(Image.open(paths[b["name"]]).resize((tw - 4, th - 4), Image.LANCZOS), (x + 2, y + 2))
            d.text((x + 6, y + th + 4), f"{b['scene'][:22]} #{b['n']}  {b['start'] / c.FPS:.1f}s +{b['length'] / c.FPS:.1f}",
                   font=f, fill=(210, 210, 210))
        path = os.path.join(out, "contact.png" if page == 0 else f"contact{page + 1}.png")
        sheet.save(path)
        made.append(path)
    return made


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lecture")
    ap.add_argument("--capture", action="store_true", help="make missing stills first (opens windows)")
    ap.add_argument("--redo", nargs="*", default=[], help="with --capture: stills to make again, or 'all'")
    ap.add_argument("--plan", action="store_true")
    ap.add_argument("--no-video", action="store_true")
    ap.add_argument("--allow-missing", action="store_true", help="encode even with placeholder stills")
    a = ap.parse_args()

    t0 = time.time()
    folder, shots, sb = board.load(a.lecture)
    out = c.out_dir(a.lecture)
    os.makedirs(os.path.join(out, "stills"), exist_ok=True)
    states.check(sb)                                   # every edit applies, the final file is the page's
    beats, scenes, total, problems = board.plan(shots, sb)
    print(f"{os.path.basename(folder)}: {len(scenes)} scenes, {len(beats)} beats, {total} frames "
          f"({total / c.FPS:.1f}s)")
    if a.plan:
        for b in beats:
            print(f"  {b['name']} {b['start'] / c.FPS:7.1f}s +{b['length'] / c.FPS:5.1f}s  {b['still']:16} "
                  f"{len(b['marks'])} marks")
    for p in problems:
        print("  PROBLEM", p)
    if a.plan:
        return
    if problems:
        sys.exit("the storyboard does not fit the narration; mend it first")

    if a.capture:
        import capture
        capture.run(a.lecture, sb, out, redo=a.redo)
        print(f"  capture took {time.time() - t0:.0f}s")

    t1 = time.time()
    paths, problems, missing = compose.compose(sb, folder, out, beats)
    for p in problems:
        print("  PROBLEM", p)
    if missing:
        print("  NOT MADE YET (placeholders):", ", ".join(missing))
    made = sheets(out, beats, paths)
    write_srt(folder, out, scenes)
    print(f"  composed {len(paths)} frames, {len(made)} contact sheet(s) in {time.time() - t1:.0f}s -> {out}")
    if problems:
        sys.exit("a mark does not fit its still; mend the storyboard or capture again")
    if a.no_video:
        return
    if missing and not a.allow_missing:
        sys.exit("some stills are placeholders: run with --capture, or pass --allow-missing for a rough cut")

    t2 = time.time()
    edl = compose.fades(out, beats, paths)
    print(f"  {sum(1 for s in edl if s['name'].endswith('_x'))} picture changes (cross-fades) in {len(beats)} beats")
    covered = sum(s["length"] for s in edl)
    if covered != total:
        sys.exit(f"the edit covers {covered} frames and the narration is {total}")
    probes = [beats[0], beats[len(beats) // 2], beats[-1]]
    moving = [b for b in beats if b.get("push")]
    if moving:                                         # and one that is pushing in, to see that it does
        probes.append(max(moving, key=lambda b: b["length"]))
    n_holds = len({b["push"][0] for b in moving})
    doc = {
        "fps": c.FPS, "size": [c.W, c.H], "frames": total, "strips": edl,
        "sounds": sounds_for(a.lecture, scenes),
        "markers": [{"name": s["id"], "start": s["start"]} for s in scenes],
        "blend": os.path.join(out, "draft.blend"), "mp4": os.path.join(out, "draft.mp4"),
        "checks": [[b["start"] + b["length"] // 2, os.path.join(out, "frames", "x", f"check_{i}.png")]
                   for i, b in enumerate(probes)],
    }
    edl_path = os.path.join(out, "edl.json")
    with open(edl_path, "w", encoding="utf-8") as f:
        json.dump(doc, f, indent=1)
    blender(edl_path, "check")
    for (frame, png), b in zip(doc["checks"], probes):
        ok, what = frame_matches(png, compose.frame_at(b, paths[b["name"]], frame))
        print(f"  check frame {frame} ({b['name']}, pushed in x{compose.scale_at(b, frame):.3f}): "
              f"{'ok' if ok else 'WRONG'} - {what}")
        if not ok:
            sys.exit("Blender did not render the edit (blank or wrong frame); nothing was encoded")
    print(f"  {len(doc['sounds'])} voice lines laid in" if doc["sounds"] else "  no voice files: the draft is silent")
    print(f"  {n_holds} hold(s) push in slowly; every other picture is still")
    blender(edl_path, "encode")
    size = os.path.getsize(doc["mp4"]) / 1e6 if os.path.exists(doc["mp4"]) else 0
    print(f"  encoded {doc['mp4']} ({size:.1f} MB, {total / c.FPS:.1f}s) in {time.time() - t2:.0f}s")


if __name__ == "__main__":
    main()
