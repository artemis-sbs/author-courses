"""Turn a lecture's video script into what the voice step and a subtitle track need.

    python narration.py c1-05-the-shape-of-a-record            # one lecture
    python narration.py --all                                  # every lecture with a script
    python narration.py c1-05-... --from-wavs                  # re-time from the real takes

THE HOUSE RULE FOR NARRATION (the course owner, 2026-10-05, after hearing eight versions):
written for the EAR, and paced like a lecture - unhurried, with the pauses a teacher leaves.
A **Say:** block marks its own pauses:

    |     a breath, 0.45 s     (after a clause)
    ||    a beat, 0.9 s        (after a sentence that carries a point)
    |||   the lecturer looks up, 1.8 s   (after an idea; a few times a scene at most)

    **Say:** "Let's take one apart. || The heading gives it a name. | Then comes what I'll
    call the fence: | two lines of three hyphens, and everything between them. ||"

Each stretch between two marks is ONE PIECE: it is spoken in one go (`voice_local.py`,
Chatterbox, on this machine) and it is one subtitle. Keep a piece a clause or a sentence,
five to twenty-five words. Pieces of a word or two sounded clipped and echoing to the
owner; whole paragraphs lose the pauses. A Say block with no marks is still read: it is cut
at sentence ends with a breath between.

For each lecture this writes, into `<lecture>/narration/`:

  shots.py       SHOTS = [{"id", "captions": [(spoken text, start, end)], "pauses": [...]}].
                 One shot per scene, one caption per piece; frames at 30 a second, local to
                 the scene. `pauses[i]` is the silence after caption i, in seconds.
  captions.srt   the pieces as WRITTEN, timed on the voice's clock. An estimate until the
                 voice exists; with --from-wavs, the real takes laid end to end.
  lines.txt      one line per piece: id, a tab, the text as written.
"""
import argparse
import glob
import os
import re
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
COURSES = os.path.dirname(HERE)
VOICE_ROOT = "R:/cosmos/voice_local"
FPS = 30
WORDS_PER_SECOND = 2.3          # the accepted delivery is unhurried
PAUSE = {"|": 0.45, "||": 0.9, "|||": 1.8}
SCENE_END = 1.2                 # silence after a scene's last piece

# Written -> spoken. Only what a voice gets wrong. A script written for the ear should
# rarely need these: say "the fetch command, with update libs", and let the screen show it.
SPOKEN = {
    "sbs": "S B S",
    ".amd": " dot A M D",
    ".mast": " dot mast",
    ".yaml": " dot yammel",
    ".json": " dot jason",
    ".py": " dot pie",
    ".md": " dot M D",
    ".vsix": " dot V six",
    ".pyz": " dot pie zee",
    ".bat": " dot bat",
    "AMD": "A M D",
    "ePADD": "ee pad",
    "VS Code": "V S Code",
    "itch.io": "itch dot eye oh",
    "->END": "arrow END",
    "--update-libs": "dash dash update libs",
    "--dry-run": "dash dash dry run",
    "--pdf": "dash dash P D F",
    "--title": "dash dash title",
    "--map": "dash dash map",
    "-t": "dash t",
    "-m": "dash m",
    "map=0": "map equals zero",
    "==": "two equals signs",
    "//": "two slashes",
    "---": "three hyphens",
    "####": "four hashes",
    "###": "three hashes",
    "##": "two hashes",
    "%": "percent",
    "_": " ",
}

SCENE = re.compile(r"^###\s+(\d+)\.\s+(.*?)\s*(?:\((\d+):(\d\d)\s*-\s*(\d+):(\d\d)\))?\s*$")


def scenes_of(script_text):
    """[(number, title, say_text)] from a video-script.md."""
    out, cur, saying = [], None, False
    for line in script_text.replace("\r\n", "\n").split("\n"):
        m = SCENE.match(line)
        if m:
            if cur:
                out.append(cur)
            cur = [int(m.group(1)), m.group(2).strip(), []]
            saying = False
            continue
        if cur is None:
            continue
        if line.startswith("## "):                 # a new top-level section ends the scenes
            out.append(cur)
            cur, saying = None, False
            continue
        if line.startswith("**Say:**"):
            saying = True
            cur[2].append(line[len("**Say:**"):].strip())
        elif line.startswith("**") or line.startswith(">"):
            saying = False
        elif line.startswith("|") and not saying:
            pass                                    # a table row outside a Say block
        elif saying and not line.strip():
            # A Say block is ONE paragraph. A plain paragraph under it is a note to
            # whoever builds the picture, and it used to be read aloud (three scripts).
            saying = False
        elif saying:
            cur[2].append(line.strip())
    if cur:
        out.append(cur)
    return [(n, t, " ".join(x for x in say if x).strip()) for n, t, say in out
            if " ".join(say).strip()]


def written(text):
    """A Say block as plain text: no quote marks round it, no markdown. Pause marks stay."""
    text = text.strip()
    text = re.sub(r"\*\[[^\]]*\]\*", " ", text)              # *[a note to the recorder]*
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)     # [words](link) -> words
    text = text.replace("**", "").replace("`", "")
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        text = text[1:-1].strip()
    return text


def sentences(text):
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z\"'(])", text)
    out = []
    for p in parts:
        p = p.strip()
        if not p:
            continue
        if out and len(p.split()) < 3:
            out[-1] = out[-1] + " " + p
        else:
            out.append(p)
    return out


def pieces(text):
    """[(words, pause_after_seconds)] for one scene's Say text."""
    if "|" not in text:
        got = sentences(text)
        if not got:
            return []
        return [(s, PAUSE["|"]) for s in got[:-1]] + [(got[-1], SCENE_END)]
    out = []
    parts = re.split(r"\s*(\|{1,3})\s*", text.strip())
    for i in range(0, len(parts), 2):
        words = parts[i].strip().strip('"').strip()
        mark = parts[i + 1] if i + 1 < len(parts) else ""
        if words:
            out.append([words, PAUSE.get(mark, PAUSE["|"])])
    if out:
        out[-1][1] = max(out[-1][1], SCENE_END)
    return [(w, p) for w, p in out]


def spoken(text):
    for word in sorted(SPOKEN, key=len, reverse=True):
        if re.match(r"^\w+$", word):
            text = re.sub(r"\b" + re.escape(word) + r"\b", SPOKEN[word], text)
        elif word.startswith("-") and not word.startswith("---") and word != "->END":
            # an option (`-t`, `--map`) only where one could stand: after a space or at
            # the start. `-t` used to fire inside "thirty-three" ("thirtydash three").
            text = re.sub(r"(?<![\w-])" + re.escape(word) + r"(?![\w-])", SPOKEN[word], text)
        else:
            text = text.replace(word, SPOKEN[word])
    return re.sub(r"\s+", " ", text).strip()


def estimate(text):
    return max(1.0, len(text.split()) / WORDS_PER_SECOND)


def wav_seconds(path):
    with wave.open(path, "rb") as w:
        return w.getnframes() / float(w.getframerate())


def slug(title):
    return re.sub(r"[^a-z0-9]+", "_", title.lower()).strip("_")[:28] or "scene"


def stamp(seconds):
    ms = int(round(seconds * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def short_name(folder):
    return re.sub(r"^(c\d+)-(\d+).*$", r"\1_\2", os.path.basename(folder.rstrip("/\\")))


def build(lecture, from_wavs=False):
    folder = lecture if os.path.isabs(lecture) else os.path.join(COURSES, lecture)
    with open(os.path.join(folder, "video-script.md"), encoding="utf-8") as f:
        scenes = scenes_of(f.read())
    name = short_name(folder)
    wav_dir = os.path.join(VOICE_ROOT, name)
    out_dir = os.path.join(folder, "narration")
    os.makedirs(out_dir, exist_ok=True)

    shots, srt, lines = [], [], []
    clock, count, words, real = 0.0, 0, 0, 0
    for number, title, say in scenes:
        shot_id = f"s{number:02d}_{slug(title)}"
        local, captions, pauses = 0.0, [], []
        for i, (text, pause) in enumerate(pieces(written(say))):
            wav = os.path.join(wav_dir, f"{shot_id}_{i}.wav")
            if from_wavs and os.path.isfile(wav):
                length = wav_seconds(wav)
                real += 1
            else:
                length = estimate(text)
            captions.append((spoken(text), int(round(local * FPS)),
                             int(round((local + length) * FPS))))
            pauses.append(pause)
            count += 1
            words += len(text.split())
            srt.append(f"{count}\n{stamp(clock + local)} --> {stamp(clock + local + length)}\n"
                       f"{text}\n")
            lines.append(f"{shot_id}_{i}\t{text}")
            local += length + pause
        shots.append({"id": shot_id, "title": title, "frames": int(round(local * FPS)),
                      "captions": captions, "pauses": pauses})
        clock += local

    with open(os.path.join(out_dir, "shots.py"), "w", encoding="utf-8", newline="\n") as f:
        f.write(f'"""Narration for {os.path.basename(folder)}: generated by _tools/narration.py '
                f'from video-script.md.\n\nOne caption per spoken piece, in SPOKEN form; '
                f'`pauses[i]` is the silence after caption i.\nDo not edit: change the '
                f'script and run the tool again.\n"""\n')
        f.write(f'NAME = "{name}"\n\nSHOTS = [\n')
        for shot in shots:
            f.write(f'    {{\n        "id": "{shot["id"]}",\n        "title": {shot["title"]!r},\n'
                    f'        "frames": {shot["frames"]},\n        "captions": [\n')
            for text, a, b in shot["captions"]:
                f.write(f"            ({text!r}, {a}, {b}),\n")
            f.write(f'        ],\n        "pauses": {shot["pauses"]!r},\n    }},\n')
        f.write("]\n")
    with open(os.path.join(out_dir, "captions.srt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(srt))
    with open(os.path.join(out_dir, "lines.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")
    kind = f"{real} of {count} from the takes" if from_wavs else "estimated"
    print(f"{os.path.basename(folder):42s} {len(shots):2d} scenes {count:3d} pieces "
          f"{words:5d} words  {int(clock // 60)}:{int(clock % 60):02d} {kind}  -> {name}")
    return name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("lecture", nargs="?")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--from-wavs", action="store_true",
                    help=f"time each piece from its take under {VOICE_ROOT}/<name>/")
    a = ap.parse_args()
    if a.all:
        for script in sorted(glob.glob(os.path.join(COURSES, "c*-*", "video-script.md"))):
            build(os.path.dirname(script), a.from_wavs)
    else:
        build(a.lecture, a.from_wavs)


if __name__ == "__main__":
    main()
