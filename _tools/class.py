"""Run one production step over every lecture of a class.

    python class.py 4 narrate        narration.py: shots, captions and lines from the scripts
    python class.py 4 plan           make.py --plan: does each storyboard fit its narration
    python class.py 4 capture        make.py --capture --no-video: editor and terminal stills
                                     (opens VS Code windows - not while the machine is in use)
    python class.py 4 stale          make.py --stale: stills that no longer show their lecture
    python class.py 4 voice          voice_local.py, then narration.py --from-wavs (no window,
                                     no mouse; hours - the overnight step)
    python class.py 4 build          make.py: compose, check and encode draft.mp4
    python class.py 4 night          voice then build, one lecture after another
    python class.py 4 report         what each lecture has: storyboard, stills, voice, draft

    --only 3,5      just those lectures (by number)
    --keep-going    a failed lecture does not stop the rest (default for voice/build/night)

Each lecture's output goes to <OUT_ROOT>/_class<N>_<step>.log as well as the screen, and a
summary table ends the run. A step whose lecture has no storyboard yet is skipped, not failed.
"""
import argparse
import glob
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "picture"))

import config as c  # noqa: E402

TTS_PY = os.environ.get("COURSE_TTS_PYTHON", r"R:\cosmos\tts\venv\Scripts\python.exe")
PY = sys.executable
NEEDS_BOARD = ("plan", "capture", "stale", "build")
KEEP_GOING = ("voice", "build", "night", "stale", "report")


def lectures(n, only=None):
    found = sorted(os.path.basename(p) for p in glob.glob(os.path.join(c.COURSES, f"c{n}-*"))
                   if os.path.isdir(p))
    if only:
        want = {int(x) for x in only.split(",")}
        found = [f for f in found if int(f.split("-")[1]) in want]
    return found


def has_board(lecture):
    return os.path.exists(os.path.join(c.lecture_dir(lecture), "narration", "storyboard.py"))


def commands(step, lecture):
    """[(argv, cwd)] for one lecture's step."""
    pic = os.path.join(HERE, "picture")
    if step == "narrate":
        return [([PY, "narration.py", lecture], HERE)]
    if step == "plan":
        return [([PY, "make.py", lecture, "--plan"], pic)]
    if step == "capture":
        return [([PY, "make.py", lecture, "--capture", "--no-video", "--allow-missing"], pic)]
    if step == "stale":
        return [([PY, "make.py", lecture, "--stale"], pic)]
    if step == "voice":
        return [([TTS_PY, "voice_local.py", lecture], HERE),
                ([PY, "narration.py", lecture, "--from-wavs"], HERE)]
    if step == "build":
        return [([PY, "make.py", lecture], pic)]
    if step == "night":
        return commands("voice", lecture) + commands("build", lecture)
    raise SystemExit(f"unknown step {step}")


def report_one(lecture):
    out = c.out_dir(lecture)
    stills = len(glob.glob(os.path.join(out, "stills", "*.png")))
    voice = len(glob.glob(os.path.join(c.VOICE_ROOT, c.short_name(lecture), "*.wav")))
    draft = os.path.join(out, "draft.mp4")
    steps = os.path.join(c.lecture_dir(lecture), "narration", "capture_steps.py")
    return (f"board {'yes' if has_board(lecture) else 'NO '}  stills {stills:3}  voice {voice:3}  "
            f"steps {'yes' if os.path.exists(steps) else 'no '}  "
            f"draft {time.strftime('%m-%d %H:%M', time.localtime(os.path.getmtime(draft))) if os.path.exists(draft) else '-'}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("klass", type=int)
    ap.add_argument("step")
    ap.add_argument("--only")
    ap.add_argument("--keep-going", action="store_true")
    a = ap.parse_args()
    todo = lectures(a.klass, a.only)
    if not todo:
        sys.exit(f"no lectures for class {a.klass}")
    if a.step == "report":
        for lec in todo:
            print(f"{lec:45} {report_one(lec)}")
        return
    keep_going = a.keep_going or a.step in KEEP_GOING
    os.makedirs(c.OUT_ROOT, exist_ok=True)
    log_path = os.path.join(c.OUT_ROOT, f"_class{a.klass}_{a.step}.log")
    results = []
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"\n===== class {a.klass} {a.step} {time.strftime('%Y-%m-%d %H:%M')} =====\n")
        for lec in todo:
            if a.step in NEEDS_BOARD and not has_board(lec):
                results.append((lec, "skipped", "no storyboard", 0))
                continue
            t0 = time.time()
            verdict, last = "ok", ""
            for argv, cwd in commands(a.step, lec):
                head = f"--- {lec}: {' '.join(os.path.basename(x) if i == 0 else x for i, x in enumerate(argv))}"
                print(head, flush=True)
                log.write(head + "\n")
                proc = subprocess.Popen(argv, cwd=cwd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                        text=True, encoding="utf-8", errors="replace")
                for line in proc.stdout:
                    print(line, end="", flush=True)
                    log.write(line)
                    if line.strip():
                        last = line.strip()
                if proc.wait() != 0:
                    verdict = "FAILED"
                    break
            log.flush()
            results.append((lec, verdict, last[:70], time.time() - t0))
            if verdict == "FAILED" and not keep_going:
                print("stopping: pass --keep-going to carry on past a failed lecture")
                break
    print(f"\n{'lecture':45} {'result':8} {'secs':>6}  last line")
    for lec, verdict, last, secs in results:
        print(f"{lec:45} {verdict:8} {secs:6.0f}  {last}")
    print("log:", log_path)
    if any(v == "FAILED" for _, v, _, _ in results):
        sys.exit(1)


if __name__ == "__main__":
    main()
