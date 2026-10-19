"""Which of a lecture's stills no longer show what the lecture says.

make.py --capture KEEPS a still that already exists, which is right for a re-run and wrong
after a fix: on Class 3 a retake "did nothing" because every still it should have replaced
was still there. So every still made from now on gets a FINGERPRINT beside it,
`<still>.src.json`: a hash of what it is a picture of, taken when it is made.

* a vscode still: the file it shows, in its state, and where it is scrolled to;
* a terminal / session still: every file of its states, its commands, and sbs.pyz;
* a game still: every file of the state the game was started on - and, kept apart, the
  sbs_utils library and LegendaryMissions' mastlib the game ran.

A still is STALE when its inputs hash differs now. A game still whose library changed is
only reported (LIBRARY): most library changes do not touch what a given still shows, so
deleting on every rebuild would re-shoot the whole class each day. Look, then --delete-library
if it does.

    python make.py <lecture> --stale                    list
    python make.py <lecture> --stale --delete           delete the stale ones, so --capture (or
                                                        game.py replay) makes them again
    python make.py <lecture> --stale --delete-library   ... and the LIBRARY ones too

A still with no fingerprint (made before 2026-10-17, or a card) is listed as UNKNOWN and
never deleted.
"""
import glob
import hashlib
import json
import os

import config as c
import states

MISSIONS = os.environ.get("PICTURE_GAME_MISSIONS", r"E:\a\Cosmos-dev\data\missions")
FINGERPRINTED = ("vscode", "terminal", "session", "game")


def _sha(*parts):
    h = hashlib.sha256()
    for p in parts:
        h.update(p if isinstance(p, bytes) else repr(p).encode("utf-8"))
        h.update(b"\0")
    return h.hexdigest()[:16]


def _file_sha(path):
    if not os.path.exists(path):
        return "absent"
    with open(path, "rb") as fh:
        return _sha(fh.read())


def _lib(pattern):
    found = sorted(glob.glob(os.path.join(MISSIONS, "__lib__", pattern)))
    return [_file_sha(p) for p in found]


def library_sha():
    return _sha(_lib("*.sbs_utils.*.sbslib"), _lib("*LegendaryMissions*.mastlib"))


def _state_sha(sb, state):
    # A lecture that only PLAYS a shipped mission (C5-01) has no states: nothing to hash.
    files = states.files_of(sb, state) if sb.STATES else {}
    return _sha(sorted(files.items()))


def inputs_sha(sb, name, spec, state=None):
    """The hash of what a still is a picture of, or None for a kind that has none."""
    kind = spec[0]
    if kind == "vscode":                             # as capture.make_vscode reads it
        opts = spec[4] if len(spec) > 4 else {}
        key = states.key(opts.get("file", sb.FILE))
        if opts.get("folder"):                       # a file of another mission, as it is on disk
            shown = _file_sha(os.path.join(c.STANDIN_MISSIONS, opts["folder"], key.replace("/", os.sep)))
        else:
            shown = states.files_of(sb, spec[1]).get(key)
        return _sha(kind, spec[1:4], sorted(opts.items(), key=str), shown)
    if kind in ("terminal", "session"):
        steps = spec[1] if isinstance(spec[1], (list, tuple)) else [spec[1]]
        parts = [kind, repr(spec[1:]), _file_sha(os.path.join(MISSIONS, "sbs.pyz"))]
        for step in steps:                           # (state, command) pairs; a state may be None
            st = step[0] if isinstance(step, (list, tuple)) and step else None
            if isinstance(st, str) and st in sb.STATES:
                parts.append(_state_sha(sb, st))
        return _sha(*parts)
    if kind == "game":
        return _sha(kind, _state_sha(sb, state or "final"))
    return None


def _src_path(stills_dir, name):
    return os.path.join(stills_dir, name + ".src.json")


def stamp(sb, stills_dir, name, spec, state=None):
    """Write a still's fingerprint beside it. Call right after making the still."""
    sha = inputs_sha(sb, name, spec, state)
    if sha is None:
        return
    doc = {"inputs": sha, "state": state}
    if spec[0] == "game":
        doc["library"] = library_sha()
    with open(_src_path(stills_dir, name), "w", encoding="utf-8") as fh:
        json.dump(doc, fh)


def stale(sb, out):
    """[(still, kind, verdict, reason)] - verdict STALE, LIBRARY or UNKNOWN."""
    stills = os.path.join(out, "stills")
    lib = None
    found = []
    for name, spec in sb.STILLS.items():
        kind = spec[0]
        if kind not in FINGERPRINTED or not os.path.exists(os.path.join(stills, name + ".png")):
            continue
        src = _src_path(stills, name)
        if not os.path.exists(src):
            found.append((name, kind, "UNKNOWN", "no fingerprint"))
            continue
        with open(src, encoding="utf-8") as fh:
            was = json.load(fh)
        try:
            now = inputs_sha(sb, name, spec, was.get("state"))
        except Exception as e:                       # a state that no longer applies
            found.append((name, kind, "STALE", f"its state no longer builds: {e}"))
            continue
        if now != was.get("inputs"):
            found.append((name, kind, "STALE", "what it shows changed"))
        elif kind == "game":
            lib = lib or library_sha()
            if lib != was.get("library"):
                found.append((name, kind, "LIBRARY", "sbs_utils or LegendaryMissions rebuilt since"))
    return found


def report(sb, out, delete=False, delete_library=False):
    found = stale(sb, out)
    if not found:
        print("  every fingerprinted still is current")
        return found
    gone = []
    for name, kind, verdict, why in found:
        print(f"  {verdict:8} {name:20} {kind:8} {why}")
        if (verdict == "STALE" and (delete or delete_library)) or (verdict == "LIBRARY" and delete_library):
            for p in (os.path.join(out, "stills", name + ".png"), _src_path(os.path.join(out, "stills"), name)):
                if os.path.exists(p):
                    os.remove(p)
            gone.append((name, kind))
    if gone:
        games = sum(1 for _n, k in gone if k == "game")
        print(f"  deleted {len(gone)}; make them again with --capture"
              + (f" and game.py replay ({games} game)" if games else ""))
    return found


def lecture_report(lecture, delete=False, delete_library=False):
    import board
    _folder, _shots, sb = board.load(lecture)
    return report(sb, c.out_dir(lecture), delete, delete_library)
