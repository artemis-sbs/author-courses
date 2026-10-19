"""Storyboard for c5-09-organizing-a-big-universe: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 4 storyboards. Caption numbers are those of shots.py (2026-10-17). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 8 left it (kestrel_verge.amd = c5-08's example,
481 lines). The page's own example\\ is the end of the lecture (six files: kestrel_verge.amd of
289 lines, jobs.amd, lore.amd, dialogue/hollin.amd, deepwell.amd, gleaners.amd), so every state
is BUILT FORWARD from the start and the last must equal them byte for byte ("same_as"). The
steps, in the video's order: Step 2, the jobs ("j_paste" cut and pasted with three hashes,
"j_hash" Replace All to one, "j_note" the note at the top, "j_fence" the chapter's fence);
Step 3, the conversations ("d_paste" the three files by speaker, "d_hash", "d_note", "d_fence");
Step 5, the cast ("l_life" the Lifeforms chapter, "l_scene" Kestrel Traffic's three records at
the end of hollin.amd); Step 6, the lore ("final"). "b_sig" is Step 8's misspelled signal
(`ledger_red`) on the beat, on "final".

NOT SHOWN AS WRITTEN: the four editions, the website and the printed book are made files that
open in a browser and the picture tools have no still for them. The commands are shown as
sessions ("t_docs", "t_site") and the editions as the page's own table ("card_editions"); replace
with a real capture once a still kind exists. The one-line-per-file form of `File:` (scene 4)
is spoken and not drawn: the page does not show it.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine for
them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the
sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-09-organizing-a-big-universe start --state final --consoles server,helm,comms`
Marks are left off every game still until the stills exist. Press order:
  1. Comms: select Hollin Compact: game_c59_hollin (Hail Hollin Compact, Hail Edda Brake, the
     Relay Warden, and Escort (250 cr)).
  2. Hail Hollin Compact, Pay the relay levy. Select the station again: game_c59_levy (Patrol
     240 cr and Escort 300 cr).
  3. Helm: the handheld icon, Library: game_c59_library (the chapter Codex with the lore pages).
Never caption a face or a clock time.
"""
import re

LECTURE = "c5-09-organizing-a-big-universe"
TITLE = ("Class 5, Lecture 9", "Organizing a big universe", "One file becomes six, and the whole world is printed")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-09-organizing-a-big-universe/example"

import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_NS = {"side": False}


def _read(rel):
    """A file of the course folder, with plain newlines."""
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as _fh:
        return _fh.read().replace("\r\n", "\n")


_TEXT = {}      # state -> {file: text}, kept so marks can find their lines
_OF = {}        # still -> (state, file)
STATES = {}
STILLS = {}


def _chain(base, steps):
    """Each step (name, [edits]) is one state on the one before it. An edit is (old, new) on FILE,
    (file, old, new), or ("write", file, text). Every old text must occur exactly once."""
    prev = base
    for name, edits in steps:
        texts = dict(_TEXT[prev])
        out = []
        for e in edits:
            if e[0] == "write":
                texts[e[1]] = e[2]
                out.append(("write", e[1], e[2]))
                continue
            if len(e) == 2:
                e = (FILE, e[0], e[1])
            f, o, n = e
            assert texts[f].count(o) == 1, (name, f, o[:50], texts[f].count(o))
            texts[f] = texts[f].replace(o, n)
            out.append(("replace", f, o, n))
        _TEXT[name] = texts
        STATES[name] = {"base": prev, "edits": out}
        prev = name


def _start(name, spec, texts):
    STATES[name] = spec
    _TEXT[name] = texts


def _same(state, *files):
    """The state must equal these files of the page's example, byte for byte."""
    for f in files:
        assert _TEXT[state][f] == _read(_EX + "/" + f), ("not the example", state, f)
    STATES[state]["same_as"] = tuple(_EX + "/" + f for f in files)


def _L(state, needle, nth=1, file=None):
    t = _TEXT[state][file or FILE]
    i = -1
    for _ in range(nth):
        i = t.find(needle, i + 1)
        assert i >= 0, (state, file, needle[:50], nth)
    return t.count("\n", 0, i) + 1


def _E(name, state, needle, nth=1, off=0, file=None):
    """An editor still centered on the line holding needle (plus off)."""
    line = _L(state, needle, nth, file) + off
    opts = {"side": False}
    if file and file != FILE:
        opts["file"] = file
    STILLS[name] = ("vscode", state, line, "big", opts)
    _OF[name] = (state, file or FILE)


def _tx(still, needle, words=None, nth=1):
    s, f = _OF[still]
    return ("text", _L(s, needle, nth, f), words or needle)


def _ln(still, needle, count=1, nth=1):
    s, f = _OF[still]
    a = _L(s, needle, nth, f)
    return ("lines", a, a + count - 1)


def _b(frm, still, *marks, **extra):
    d = {"from": frm, "still": still}
    if marks:
        d["marks"] = list(marks)
    d.update(extra)
    return d


def _sc(step, *beats):
    return {"step": step, "beats": list(beats)}


def _term(name, state, cmd="sbs lint " + "{M}"):
    STILLS[name] = ("terminal", [(state, cmd.replace("{M}", MISSION))])


def _game(name, what):
    STILLS[name] = ("game", what)


def _card(name, kind, **opts):
    STILLS[name] = ("card", kind, opts)


_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c5-06-jobs/example", "c5-07-narrative-and-goals/example",
                          "c5-08-captains-and-rivals/example")},
       {FILE: _read("c5-08-captains-and-rivals/example/" + FILE)})

_M0 = _TEXT["start"][FILE]
_F = _read(_EX + "/" + FILE)
_x = lambda f: _read(_EX + "/" + f)

# the jobs: the six records as the main file has them, then as the chapter file has them
_J3 = _M0[_M0.index("### [Patrol](patrol)"):_M0.index("## [Regions](regions)")]
_JOBS_PASTED = _J3.rstrip("\n") + "\n"
_JOBS_HASH = re.sub(r"(?m)^### \[", "# [", _JOBS_PASTED)
_JB = _x("jobs.amd")
assert _JB[_JB.index("# [Patrol]"):].rstrip("\n") == _JOBS_HASH.rstrip("\n"), "jobs.amd is not the main file's jobs"

# the conversations, sorted by speaker
_DH = "## [Dialogue](dialogue)"
_DI = _M0.index(_DH)
_BODY = _M0[_DI + len(_DH):]
_SIDE = {"hollin": "hollin", "edda": "hollin", "deepwell": "deepwell", "gleaners": "gleaners", "sable": "gleaners"}
_BK = {"hollin": [], "deepwell": [], "gleaners": []}
for _r in re.split(r"(?m)^(?=### \[)", _BODY):
    if _r.strip():
        _BK[_SIDE[re.search(r"Speaker: (\w+)", _r).group(1)]].append(_r.rstrip("\n") + "\n")
_PASTE = {k: "\n".join(v) for k, v in _BK.items()}
_EXD = {k: _x("dialogue/" + k + ".amd") for k in _BK}
_HASH = {}
_NOTE = {}
for _k, _ex in _EXD.items():
    _cut = _ex.index("# [Kestrel Traffic](traffic_hail)") if _k == "hollin" else len(_ex)
    _NOTE[_k] = _ex[:_cut].rstrip("\n") + "\n"
    _HASH[_k] = _NOTE[_k][_NOTE[_k].index("# ["):]
    assert re.sub(r"(?m)^# \[", "### [", _HASH[_k]).rstrip("\n") == _PASTE[_k].rstrip("\n"), "dialogue/%s.amd is not the main file's records" % _k

_LIFE = _F[_F.index("## [Lifeforms](lifeforms)"):_F.index(_DH)]
_FENCE = _DH + "\n---\nFile: dialogue/hollin.amd, dialogue/deepwell.amd, dialogue/gleaners.amd\n---\n"
_W = lambda d, m: [("write", "dialogue/" + k + ".amd", m[k]) for k in ("hollin", "deepwell", "gleaners")]

_chain("start", [
    ("j_paste", [(_J3, ""), ("write", "jobs.amd", _JOBS_PASTED)]),
    ("j_hash", [("write", "jobs.amd", _JOBS_HASH)]),
    ("j_note", [("write", "jobs.amd", _JB)]),
    ("j_fence", [("## [Jobs](jobs)\n", "## [Jobs](jobs)\n---\nFile: jobs.amd\n---\n")]),
    ("d_paste", [(_M0[_DI:], _DH + "\n")] + _W(0, _PASTE)),
    ("d_hash", _W(0, _HASH)),
    ("d_note", _W(0, _NOTE)),
    ("d_fence", [(_DH + "\n", _FENCE)]),
    ("l_life", [(_FENCE, _LIFE + _FENCE)]),
    ("l_scene", [("write", "dialogue/hollin.amd", _EXD["hollin"])]),
    ("final", [("write", "lore.amd", _x("lore.amd"))]),
])
_same("final", FILE, "jobs.amd", "lore.amd", "dialogue/hollin.amd", "dialogue/deepwell.amd", "dialogue/gleaners.amd")
_chain("final", [("b_sig", [("Done when: signal ledger_read", "Done when: signal ledger_red")])])

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_long", "start", "## [Jobs](jobs)", off=10)
STILLS["e_tree"] = ("vscode", "final", 1, "mid", {"file": "jobs.amd"})      # the Side Bar shown: the file list
_OF["e_tree"] = ("final", "jobs.amd")
_E("e_fence", "j_fence", "## [Jobs](jobs)", off=3)
_E("e_main_gone", "j_paste", "## [Jobs](jobs)", off=3)
_E("e_jobs_paste", "j_paste", "### [Patrol](patrol)", off=0, file="jobs.amd")
_E("e_jobs_hash", "j_hash", "# [Patrol](patrol)", off=0, file="jobs.amd")
_E("e_dlg0", "j_fence", _DH, off=8)
_E("e_hollin_d", "d_paste", "### [Hollin Hail](hollin_hail)", off=8, file="dialogue/hollin.amd")
_E("e_edda_d", "d_paste", "### [Edda Brake](edda_hail)", off=4, file="dialogue/hollin.amd")
_E("e_fence_d", "d_fence", "File: dialogue/hollin.amd", off=-2)
_E("e_sig_k", "d_fence", "Done when: signal ledger_read")
_E("e_sig_d", "d_fence", "signal ledger_read", file="dialogue/deepwell.amd", off=2)
_E("e_sig_bad", "b_sig", "Done when: signal ledger_red")
_E("e_life", "l_life", "## [Lifeforms](lifeforms)", off=6)
_E("e_scene", "l_scene", "# [Kestrel Traffic](traffic_hail)", off=8, file="dialogue/hollin.amd")
_E("e_lore0", "final", "# [The Kestrel Verge](verge)", off=0, file="lore.amd")
_E("e_lore", "final", "| Colony | Landed | Now |", file="lore.amd")
_E("e_lore2", "final", "## What it is for", file="lore.amd", off=-3)

_term("t_split", "d_fence")
_term("t_final", "final")
_term("t_sig", "b_sig")
STILLS["t_docs"] = ("session", ['sbs docs MyUniverse --title "The Kestrel Verge" --lens all'], {"state": "final"})
STILLS["t_site"] = ("session", ["sbs site MyUniverse --emit site"], {"state": "final"})

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c59_hollin", "Comms, Hollin Compact selected: the buttons Hail Hollin Compact, Hail Edda Brake the Relay Warden, and Escort (250 cr)")
_game("game_c59_levy", "Comms, Hollin Compact selected after the levy: Patrol (240 cr) and Escort (300 cr)")
_game("game_c59_library", "Helm, the handheld icon then Library: the chapter Codex with the lore pages in it")

# drawn
_card("card_rules", "rows", kicker="Three rules for a chapter file", header=["Rule", "What it says"],
      rows=[["One hash", "Every record in a chapter file starts with one hash, not three"],
            ["Commas, and a slash", "File: names every file of the chapter, with commas, and a folder joined with /"],
            ["Files or records", "A chapter reads from files, or it holds records. Keep to one"]])
_card("card_count", "rows", kicker="Replace All", header=["Change", "Count"],
      rows=[["### [ becomes # [ in jobs.amd", "6 changes, one for each job"]])
_card("card_editions", "table", heading="Step 7 - Print the world", nth=1, kicker="Four editions")
_card("card_split", "table", heading="Step 8 - What can go wrong in a split", nth=2, kicker="What lint does not catch after a split")
_card("card_exercise", "list", heading="Exercise", kicker="Split it, voice it, print it")
_card("card_next", "title", kicker="Next", title="Lecture 10", sub="A boarding site on the map")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "e_long", _ln("e_long", "## [Jobs](jobs)", 20)),
        _b(2, "e_long"),
        _b(3, "e_tree", _ln("e_tree", "# [Patrol](patrol)", 3)),
        _b(5, "e_tree"),
        _b(6, "card_editions")),
    "s02_a_chapter_that_reads_from_a_": _sc(1,
        _b(0, "e_fence", _ln("e_fence", "## [Jobs](jobs)", 4)),
        _b(1, "e_fence", _tx("e_fence", "## [Jobs](jobs)"), _tx("e_fence", "---\nFile: jobs.amd", "---")),
        _b(2, "e_fence", _tx("e_fence", "File: jobs.amd")),
        _b(3, "e_fence", _ln("e_fence", "## [Jobs](jobs)", 4)),
        _b(5, "e_fence", _ln("e_fence", "## [Jobs](jobs)", 4)),
        _b(7, "card_rules")),
    "s03_move_the_jobs": _sc(2,
        _b(0, "e_jobs_paste", _tx("e_jobs_paste", "### [Patrol](patrol)")),
        _b(1, "e_main_gone", _ln("e_main_gone", "## [Jobs](jobs)", 1)),
        _b(2, "card_rules", ("part", "r1")),
        _b(3, "e_jobs_paste", _tx("e_jobs_paste", "### [Patrol](patrol)", "###")),
        _b(5, "e_jobs_paste", _tx("e_jobs_paste", "### [Patrol](patrol)", "###")),
        _b(6, "e_jobs_hash", _tx("e_jobs_hash", "# [Patrol](patrol)", "# [")),
        _b(7, "card_count"),
        _b(9, "e_fence", _ln("e_fence", "## [Jobs](jobs)", 4))),
    "s04_move_the_conversations": _sc(3,
        _b(0, "e_dlg0", _ln("e_dlg0", _DH, 1)),
        _b(1, "e_hollin_d", _tx("e_hollin_d", "### [Hollin Hail](hollin_hail)")),
        _b(3, "e_edda_d", _tx("e_edda_d", "### [Edda Brake](edda_hail)")),
        _b(5, "e_fence_d", _ln("e_fence_d", _DH, 4)),
        _b(6, "e_fence_d", _tx("e_fence_d", "File: dialogue/hollin.amd, dialogue/deepwell.amd, dialogue/gleaners.amd")),
        _b(7, "card_rules", ("part", "r2"))),
    "s05_check_it": _sc(4,
        _b(0, "t_split", ("part", "run1:clean")),
        _b(1, "t_split", ("part", "run1:clean")),
        _b(3, "e_sig_d", _tx("e_sig_d", "signal ledger_read")),
        _b(4, "e_sig_k", _tx("e_sig_k", "Done when: signal ledger_read", "signal ledger_read")),
        _b(6, "t_split", ("part", "run1:clean")),
        _b(8, "e_sig_bad", _tx("e_sig_bad", "Done when: signal ledger_red", "ledger_red")),
        _b(9, "t_sig", ("out", 1, 1)),
        _b(10, "card_rules", ("part", "r3"))),
    "s06_a_voice_from_anywhere": _sc(5,
        _b(0, "e_life", _ln("e_life", "## [Lifeforms](lifeforms)", 10)),
        _b(2, "e_life", _tx("e_life", "### [Kestrel Traffic](kestrel_traffic)")),
        _b(4, "e_life", _tx("e_life", "Face: terran"+chr(10)+"Roles: hollin", "Face: terran"), _tx("e_life", "Color: #44aa66"+chr(10)+"---"+chr(10)+"The relay", "Color: #44aa66")),
        _b(5, "e_life", _tx("e_life", "Scene: traffic_hail")),
        _b(6, "e_scene", _ln("e_scene", "# [Kestrel Traffic](traffic_hail)", 3)),
        _b(7, "e_scene", _ln("e_scene", "% Kestrel Traffic. The lamp is lit", 2)),
        _b(8, "e_scene", _ln("e_scene", "% Kestrel Traffic. The lamp is lit", 2))),
    "s07_lore": _sc(6,
        _b(0, "e_lore0", _tx("e_lore0", "# [The Kestrel Verge](verge)")),
        _b(1, "e_lore0", _ln("e_lore0", "# [The Kestrel Verge](verge)", 3)),
        _b(3, "e_lore0", _ln("e_lore0", "Past the last relay", 1)),
        _b(4, "game_c59_library"),
        _b(6, "e_lore", _ln("e_lore", "| Colony | Landed | Now |", 5)),
        _b(8, "e_lore2", _tx("e_lore2", "## What it is for")),
        _b(10, "e_lore2", _ln("e_lore2", "Every message into or out of the Verge", 1))),
    "s08_print_the_world": _sc(7,
        _b(0, "t_docs"),
        _b(1, "t_docs", ("cmd", 1, "--lens all")),
        _b(3, "card_editions", ("part", "r1")),
        _b(4, "card_editions", ("part", "r2")),
        _b(5, "card_editions", ("part", "r3")),
        _b(7, "card_editions", ("part", "r4")),
        _b(10, "t_site", ("cmd", 1, "sbs site")),
        _b(13, "t_site")),
    "s09_still_the_same_game": _sc(9,
        _b(0, "game_c59_hollin"),
        _b(2, "game_c59_levy"),
        _b(3, "game_c59_library"),
        _b(4, "card_split"),
        _b(6, "card_split", ("part", "r1"))),
    "s10_your_turn": _sc(None,
        _b(0, "card_exercise"),
        _b(1, "card_exercise", ("part", "item1")),
        _b(2, "card_exercise", ("part", "item3")),
        _b(3, "card_exercise", ("part", "item4")),
        _b(4, "card_exercise", ("part", "item5")),
        _b(6, "card_next")),
}
