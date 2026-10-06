"""Speak a lecture's narration on this machine, with Chatterbox, in the owner's voice.

    R:\\cosmos\\tts\\venv\\Scripts\\python.exe voice_local.py c1-05-the-shape-of-a-record
    ... voice_local.py c1-05-... --redo s04_one_record_three_p_3     # take one piece again
    ... voice_local.py c1-05-... --report                           # what exists, no generating

Run it with the TTS environment's Python (R:\\cosmos\\tts\\venv), not the ordinary one.
No window, no mouse: it can run while the machine is in use.

It reads `<lecture>/narration/shots.py` (make it with narration.py) and writes one WAV per
piece to R:/cosmos/voice_local/<name>/<shot>_<n>.wav. A piece whose text has not changed
is not spoken again. Then:  narration.py <lecture> --from-wavs  re-times the subtitles and
the picture's cut to the real takes.

THE DELIVERY is the one the owner chose by ear on 2026-10-05 ("C1"): exaggeration 0.45,
cfg_weight 0.3 (unhurried), no time-stretch (stretching sounded processed), each piece a
clause or a sentence spoken in one go, and the pauses put in between pieces - not asked of
the model. Each take is trimmed of the model's own leading and trailing silence, and held
under full scale so nothing clips.
"""
import argparse
import hashlib
import importlib.util
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
COURSES = os.path.dirname(HERE)
VOICE_ROOT = "R:/cosmos/voice_local"


def _sample():
    """The voice sample to clone: a WAV of the author speaking, about half a minute. It is
    NOT in the repository. Name it in the COURSE_VOICE_SAMPLE environment variable, or put
    its path on the first line of _tools/voice_sample.txt (which git ignores)."""
    path = os.environ.get("COURSE_VOICE_SAMPLE", "").strip()
    note = os.path.join(HERE, "voice_sample.txt")
    if not path and os.path.isfile(note):
        with open(note, encoding="utf-8") as f:
            path = f.readline().strip()
    if not path or not os.path.isfile(path):
        sys.exit("no voice sample: set COURSE_VOICE_SAMPLE or write its path in "
                 "_tools/voice_sample.txt")
    return path.replace(chr(92), "/")


SAMPLE = _sample()
DELIVERY = dict(exaggeration=0.45, cfg_weight=0.3)
PEAK = 0.89                      # about -1 dBFS


def load_shots(folder):
    path = os.path.join(folder, "narration", "shots.py")
    spec = importlib.util.spec_from_file_location("shots", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def digest(text):
    return hashlib.sha1((text + json.dumps(DELIVERY, sort_keys=True) + SAMPLE)
                        .encode("utf-8")).hexdigest()[:16]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lecture")
    ap.add_argument("--redo", action="append", default=[], metavar="PIECE",
                    help="speak this piece again with a new reading (repeatable)")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    folder = a.lecture if os.path.isabs(a.lecture) else os.path.join(COURSES, a.lecture)
    shots = load_shots(folder)
    out_dir = os.path.join(VOICE_ROOT, shots.NAME)
    os.makedirs(out_dir, exist_ok=True)
    index_path = os.path.join(out_dir, "lines.json")
    index = json.load(open(index_path, encoding="utf-8")) if os.path.exists(index_path) else {}

    todo, keep = [], set()
    for shot in shots.SHOTS:
        for i, (text, _a, _b) in enumerate(shot["captions"]):
            key = f"{shot['id']}_{i}"
            keep.add(key)
            have = (os.path.isfile(os.path.join(out_dir, key + ".wav"))
                    and index.get(key, {}).get("digest") == digest(text))
            if not have or key in a.redo:
                todo.append((key, text))
    total = sum(len(s["captions"]) for s in shots.SHOTS)
    print(f"{shots.NAME}: {total} pieces, {len(todo)} to speak", flush=True)
    if a.report or not todo:
        return

    import numpy as np
    import torch
    import torchaudio
    from chatterbox.tts import ChatterboxTTS
    model = ChatterboxTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
    sr = model.sr
    t0 = time.time()
    for n, (key, text) in enumerate(todo, 1):
        seed = index.get(key, {}).get("seed", 11) + (1 if key in a.redo else 0)
        best = None
        for attempt in range(3):
            torch.manual_seed(seed + attempt * 101)
            x = model.generate(text, audio_prompt_path=SAMPLE, **DELIVERY).cpu().squeeze(0).numpy()
            loud = np.flatnonzero(np.abs(x) > 0.01)
            if loud.size == 0:
                continue
            x = x[max(0, loud[0] - int(0.03 * sr)): min(len(x), loud[-1] + int(0.08 * sr))]
            seconds = len(x) / sr
            # A take far longer than its words is the model wandering (a repeat, noise,
            # a breath held for seconds): take it again.
            expect = max(0.6, len(text.split()) / 2.3)
            if best is None or abs(seconds - expect) < abs(best[1] - expect):
                best = (x, seconds, seed + attempt * 101)
            if 0.45 * expect <= seconds <= 2.2 * expect:
                break
        if best is None:
            print(f"  {key}: NOTHING SPOKEN for {text!r}", flush=True)
            continue
        x, seconds, used = best
        peak = float(np.abs(x).max())
        if peak > PEAK:
            x = x * (PEAK / peak)
        torchaudio.save(os.path.join(out_dir, key + ".wav"), torch.from_numpy(x).unsqueeze(0), sr,
                        encoding="PCM_S", bits_per_sample=16)
        index[key] = {"digest": digest(text), "seed": used, "seconds": round(seconds, 2),
                      "text": text}
        if n % 10 == 0 or n == len(todo):
            json.dump(index, open(index_path, "w", encoding="utf-8"), indent=1)
            print(f"  {n}/{len(todo)} spoken, {time.time() - t0:.0f} s", flush=True)
    for key in [k for k in index if k not in keep]:        # pieces the script no longer has
        index.pop(key)
        stale = os.path.join(out_dir, key + ".wav")
        if os.path.isfile(stale):
            os.remove(stale)
    json.dump(index, open(index_path, "w", encoding="utf-8"), indent=1)
    print("done", flush=True)


if __name__ == "__main__":
    main()
