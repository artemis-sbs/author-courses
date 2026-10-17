"""Regenerate a lecture's narration and move storyboard beats to the captions they belonged to.

    python renarrate.py <lecture>

Old captions are matched to new ones per scene with difflib; a beat's "from" (whole or
fractional) moves with its caption. Prints every beat that moved.
"""
import difflib
import importlib.util
import os
import re
import subprocess
import sys

ROOT = r"E:\a\author_courses"


def load(path):
    spec = importlib.util.spec_from_file_location("m", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def main():
    lec = sys.argv[1]
    shots = os.path.join(ROOT, lec, "narration", "shots.py")
    old = {s["id"]: [c[0] for c in s["captions"]] for s in load(shots).SHOTS}
    subprocess.run([sys.executable, os.path.join(ROOT, "_tools", "narration.py"), lec], check=True,
                   cwd=ROOT, stdout=subprocess.DEVNULL)
    new = {s["id"]: [c[0] for c in s["captions"]] for s in load(shots).SHOTS}
    sbp = os.path.join(ROOT, lec, "narration", "storyboard.py")
    text = open(sbp, encoding="utf-8", newline="").read()
    for sid in new:
        if sid not in old or old[sid] == new[sid]:
            continue
        mapping = {}
        sm = difflib.SequenceMatcher(None, old[sid], new[sid])
        for tag, a0, a1, b0, b1 in sm.get_opcodes():
            for k in range(a1 - a0):
                mapping[a0 + k] = b0 + min(k, max(b1 - b0 - 1, 0))
        start = text.index('"%s"' % sid)
        nxt = re.search(r'\n    "s\d\d_', text[start + 1:])
        end = start + 1 + nxt.start() if nxt else len(text)
        block = text[start:end]

        def bump(m):
            v = float(m.group(1))
            base = int(v)
            frac = v - base
            nb = mapping.get(base, base + (len(new[sid]) - len(old[sid])))
            nv = nb + frac
            out = str(int(nv)) if nv == int(nv) else str(nv)
            if out != m.group(1):
                print("  %s: beat %s -> %s" % (sid, m.group(1), out))
            return '{"from": ' + out + ","

        text = text[:start] + re.sub(r'\{"from": ([0-9.]+),', bump, block) + text[end:]
    open(sbp, "w", encoding="utf-8", newline="").write(text)


if __name__ == "__main__":
    main()
