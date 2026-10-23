"""Storyboard for c6-10-publishing: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in the
Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22).

The lecture starts from `MyUniverse` as Lecture 8 left it (Class 5's files with c6-01..c6-08's laid
over them). The mission is drawn under its final name, `KestrelVerge` (MISSION): the lecture
renames the folder in scene 4, and every command after that names the new folder. States:
"start" is the folder before the lecture; "desc" is Step 2 (the Description: line, the page's own
description.yaml, `same_as`); "hyphen" and "colon" are the two mistakes of Step 2's table; "note"
adds the host's note (the page's own note.txt, `same_as`) as a file beside the mission, only so
the editor can show it; "clean" is the folder with Step 5's pages and leftovers taken out
(`skip`) - the seven files of the page.

NOT SHOWN AS WRITTEN. (1) Scene 3 runs lint before the folder is renamed; the picture runs it as
`sbs lint KestrelVerge` (one stand-in folder, one name; the answer is the same). (2) Scene 4's
rename in File Explorer is drawn by its result: the folder under its new name. (3) Scene 6's moving
and deleting is drawn by its results: the folder with the leftovers in it, then the seven files;
the page's two tables say what moves and what goes. (4) Scene 7's right-click and compress is
drawn by its result: the zip beside the folder. (5) Scene 9's table is the page's Step 7 table.
(6) The doctor and lint terminals are marked on words the page shows them printing (the library
count may differ by one or two on a machine); check them when the stills are taken.

GAME STILLS. None.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))


def _rd(rel):
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


LECTURE = "c6-10-publishing"
TITLE = ("Class 6, Lecture 10", "Publishing", "Act One as a folder, a zip and a note for the host")
MISSION = "KestrelVerge"
TEMPLATE_BASE = "ou"
TEMPLATE = "ou"
FILE = "description.yaml"
MAST = "story.mast"
_EX = "c6-10-publishing/example"
_NS = {"side": False}

_OVER = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1", "c5-13-battles-part-2",
    "c6-01-from-one-session-to-twenty", "c6-02-what-the-game-remembers", "c6-03-designing-a-session",
    "c6-04-the-episode", "c6-05-campaign-architecture", "c6-06-reputation-arcs",
    "c6-07-mixing-the-play-styles", "c6-08-playtesting"))

_D0 = _rd("c5-02-your-universe-file/example/description.yaml")
_NOTE = _rd(_EX + "/note.txt")
_TEXT = {"start": {FILE: _D0, "note.txt": _NOTE}}
STATES = {"start": {"folder": "c5-02-your-universe-file/example", "over": _OVER}}
# Class 5 Lecture 9 split the universe into jobs.amd, lore.amd and dialogue\*.amd; the Class 6 file holds
# all of it inline (and c5-08's captain is not in it), so those stale split files are taken out.
_JUNK = ["jobs.amd", "lore.amd"] + sorted(
    "dialogue/" + f for f in os.listdir(os.path.join(_ROOT, "c5-09-organizing-a-big-universe", "example", "dialogue")))
STATES["u"] = {"base": "start", "edits": [("delete", f) for f in _JUNK]}
_TEXT["u"] = dict(_TEXT["start"])

_OLD = "Description: The Kestrel Verge"
_LINE = "Description: A campaign for one ship. Act One, five evenings. Version 1."


def _state(name, base, edits, **extra):
    texts = dict(_TEXT[base])
    out = []
    for e in edits:
        if e[0] == "write":
            texts[e[1]] = e[2]
            out.append(e)
            continue
        f, o, n = e
        assert texts[f].count(o) == 1, (name, f, o[:60], texts[f].count(o))
        texts[f] = texts[f].replace(o, n)
        out.append(("replace", f, o, n))
    _TEXT[name] = texts
    STATES[name] = dict({"base": base, "edits": out}, **extra)


def _L(state, needle, nth=1, file=FILE):
    t = _TEXT[state][file]
    i = -1
    for _ in range(nth):
        i = t.find(needle, i + 1)
        assert i >= 0, (state, needle[:50])
    return t.count("\n", 0, i) + 1


_state("desc", "u", [(FILE, _OLD, _LINE)], same_as=(_EX + "/description.yaml",))
assert _TEXT["desc"][FILE] == _rd(_EX + "/description.yaml")
_state("hyphen", "u", [(FILE, _OLD, "Description: A campaign for one ship - Act One")])
_state("colon", "u", [(FILE, _OLD, "Description: Act One: five evenings")])
_state("note", "desc", [("write", "note.txt", _NOTE)], same_as=(_EX + "/description.yaml", _EX + "/note.txt"))
STATES["clean"] = {"base": "desc", "edits": [("delete", "campaign.md"), ("delete", "playtest.md")]}

STILLS = {}


def _E(name, state, needle, off=0, file=FILE):
    opts = dict(_NS)
    opts["file"] = file
    STILLS[name] = ("vscode", state, _L(state, needle, 1, file) + off, "big", opts)


_E("e_desc0", "start", "Description:")
_E("e_desc", "desc", "Description:")
_E("e_note_a", "note", "This is a campaign", off=6, file="note.txt")
_E("e_note_b", "note", "sbs update", off=3, file="note.txt")
_E("e_note_c", "note", "Four things about a campaign", off=6, file="note.txt")

_DIR = "KestrelVerge\\"
STILLS.update({
    "t_lint_hyphen": ("terminal", [("hyphen", "sbs lint KestrelVerge")]),
    "t_lint_colon": ("terminal", [("colon", "sbs lint KestrelVerge")]),
    "t_lint": ("terminal", [("desc", "sbs lint KestrelVerge")]),
    "t_doctor": ("terminal", [("desc", "sbs doctor KestrelVerge")]),
    "x_named": ("explorer", "data\\missions", {"state": "desc"}),
    "x_dirty": ("explorer", "data\\missions\\KestrelVerge", {"state": "desc", "add": {
        _DIR + "__docs__": "dir", _DIR + "__pycache__": "dir",
        _DIR + "mast.compile.log": "file", _DIR + "mast.runtime.log": "file", _DIR + "debug.log": "file"}}),
    "x_seven": ("explorer", "data\\missions\\KestrelVerge", {"state": "clean"}),
    "x_zip": ("explorer", "data\\missions", {"state": "clean", "add": {"KestrelVerge.zip": "zip:KestrelVerge"}}),
    "card_title": ("card", "title", {}),
    "card_four": ("card", "table", {"heading": "Step 1 - What a campaign adds to shipping a mission", "nth": 1,
                                    "kicker": "A mission and a campaign: four differences"}),
    "card_rules": ("card", "table", {"heading": "Step 2 - The line on the mission list", "nth": 1,
                                     "kicker": "The one mistake that stops the game for everybody"}),
    "card_folder": ("card", "points", {"kicker": "Measured about the folder's name", "items": [
        "Nothing inside the files holds it.",
        "The save does not follow the folder. It follows the title.",
        "Two folders with one title are playing the same campaign."]}),
    "card_walk": ("card", "points", {"kicker": "The walk, on a deleted save", "items": [
        "Delete universe_save_the_kestrel_verge_1.yaml.",
        "Walk Act One as in Lecture 8.",
        "Delete the save again afterward."]}),
    "card_out": ("card", "table", {"heading": "Step 5 - Take out what is not the mission", "nth": 1,
                                   "kicker": "Move your own pages out"}),
    "card_del": ("card", "table", {"heading": "Step 5 - Take out what is not the mission", "nth": 2,
                                   "kicker": "Delete what the tools made"}),
    "card_host": ("card", "points", {"kicker": "What the host can still read", "items": [
        "Zip the folder itself, as in Class 1 Lecture 12.",
        "kestrel_verge.amd is plain text, and it is the whole of Act One.",
        "A host who opens it has read the campaign. That is what a host is for.",
        "To be crew in your own campaign, someone else must host it, and read it."]}),
    "card_act2": ("card", "table", {"heading": "Step 7 - Sending Act Two", "nth": 1,
                                    "kicker": "Three rules for sending Act Two"}),
    "card_check2": ("card", "points", {"kicker": "Before you send Act Two", "items": [
        "Copy your own save from the end of Act One into place.",
        "Start the new folder.",
        "See that the first lead of Act Two is in the Quest Log."]}),
    "card_checkpoint": ("card", "points", {"kicker": "A release: a named folder, a clean zip, a note", "items": [
        "description.yaml says which act and which version, with no hyphen and no colon.",
        "The folder has a name of its own, and lint and doctor are happy with it.",
        "The zip has no campaign.md, no playtest.md, no __docs__ and no save in it.",
        "Your note tells the host about Continue, the ship's name, going home, and the copy of the save.",
        "You know how Act Two will reach a crew that has finished Act One."]}),
})


def _tx(still, needle, words=None, nth=1):
    state = STILLS[still][1]
    return ("text", _L(state, needle, nth, STILLS[still][4]["file"]), words or needle)


def _ln(still, needle, count=1):
    state = STILLS[still][1]
    a = _L(state, needle, 1, STILLS[still][4]["file"])
    return ("lines", a, a + count - 1)


def _b(frm, still, *marks):
    d = {"from": frm, "still": still}
    if marks:
        d["marks"] = list(marks)
    return d


_NOTE_ITEMS = ["1. Start it the same way", "2. Leave the ship's name", "3. End each evening", "4. After each evening"]

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        _b(0, "x_zip"),
        _b(1, "e_note_a"),
        _b(2, "card_title"),
        _b(3, "card_four"),
    ]},
    "s02_four_differences": {"step": 1, "beats": [
        _b(0, "card_four", ("part", "r1")),
        _b(1, "card_four", ("part", "r1")),
        _b(2, "card_four", ("part", "r2")),
        _b(3, "card_four", ("part", "r2")),
        _b(4, "card_four", ("part", "r3")),
        _b(5, "card_four", ("part", "r3")),
        _b(6, "card_four", ("part", "r4")),
    ]},
    "s03_the_line_on_the_list": {"step": 2, "beats": [
        _b(0, "e_desc0"),
        _b(1, "e_desc"),
        _b(2, "e_desc", _tx("e_desc", "Description:", _LINE)),
        _b(3, "t_lint_hyphen", ("span", 1, "description-stops-the-game")),
        _b(4, "card_rules", ("part", "r1"), ("part", "r2")),
        _b(5, "t_lint", ("span", 1, "0 error(s), 0 warning(s)")),
        _b(6, "e_desc", _tx("e_desc", "Visible Mission Name:", "Visible Mission Name: The Kestrel Verge")),
    ]},
    "s04_the_folder_s_name": {"step": 3, "beats": [
        _b(0, "x_named"),
        _b(1, "card_folder"),
        _b(2, "card_folder", ("part", "item1")),
        _b(3, "card_folder", ("part", "item2")),
        _b(5, "x_named"),
        _b(6, "card_folder", ("part", "item3")),
    ]},
    "s05_three_checks": {"step": 4, "beats": [
        _b(0, "t_lint"),
        _b(1, "t_lint", ("span", 1, "0 error(s), 0 warning(s)")),
        _b(2, "t_doctor", ("cmd", 1, "sbs doctor KestrelVerge")),
        _b(3, "t_doctor", ("span", 1, "KestrelVerge")),
        _b(4, "t_doctor", ("span", 1, "mastlib")),
        _b(6, "card_walk", ("part", "item2")),
        _b(7, "card_walk", ("part", "item3")),
    ]},
    "s06_take_out_what_isn_t_the_miss": {"step": 5, "beats": [
        _b(0, "x_dirty"),
        _b(1, "card_out"),
        _b(2, "card_out", ("part", "r1")),
        _b(3, "card_out", ("part", "r2")),
        _b(4, "card_out", ("part", "r3")),
        _b(6, "card_del"),
        _b(7, "card_del", ("part", "r1")),
        _b(8, "x_seven"),
    ]},
    "s07_zip_it": {"step": 5, "beats": [
        _b(0, "x_zip"),
        _b(2, "card_host", ("part", "item2")),
        _b(4, "card_host", ("part", "item3")),
        _b(7, "card_host", ("part", "item4")),
    ]},
    "s08_the_note": {"step": 6, "beats": [
        _b(0, "e_note_a", _ln("e_note_a", "This is a campaign", 2)),
        _b(1, "e_note_b", _ln("e_note_b", "sbs update", 3)),
        _b(2, "e_note_c", _tx("e_note_c", "Four things about a campaign")),
        _b(3, "e_note_c", _ln("e_note_c", "1. Start it the same way", 2)),
        _b(4, "e_note_c", _tx("e_note_c", "Never choose New Game")),
        _b(5, "e_note_c", _ln("e_note_c", "2. Leave the ship's name", 2)),
        _b(6, "e_note_c", _ln("e_note_c", "3. End each evening", 1)),
        _b(7, "e_note_c", _ln("e_note_c", "4. After each evening", 3)),
        _b(8, "e_note_c", _tx("e_note_c", "universe_save_the_kestrel_verge_1.yaml")),
    ]},
    "s09_act_two": {"step": 7, "beats": [
        _b(0, "card_act2"),
        _b(2, "card_act2", ("part", "r1")),
        _b(3, "card_act2", ("part", "r2")),
        _b(5, "card_act2", ("part", "r3")),
        _b(7, "card_act2"),
        _b(10, "card_check2", ("part", "item1")),
        _b(11, "card_check2", ("part", "item2")),
        _b(12, "card_check2", ("part", "item3")),
    ]},
    "s10_close": {"step": None, "beats": [
        _b(0, "card_checkpoint"),
        _b(1, "card_checkpoint", ("part", "item2"), ("part", "item3")),
        _b(2, "card_title"),
    ]},
}


def _fit():
    """Every mark of an editor still must be inside the 14 lines it shows (T-10 .. T+3)."""
    rng = {}
    for sc in BOARD.values():
        for b in sc["beats"]:
            if STILLS[b["still"]][0] != "vscode":
                continue
            for m in b.get("marks", []):
                if m[0] == "lines":
                    lo, hi = m[1], m[2]
                elif m[0] == "text":
                    lo = hi = m[1]
                else:
                    continue
                a, z = rng.get(b["still"], (lo, hi))
                rng[b["still"]] = (min(a, lo), max(z, hi))
    for name, (lo, hi) in rng.items():
        t = STILLS[name]
        if lo < t[2] - 6 or hi > t[2] + 5:
            a, z = hi - 5, lo + 6
            assert a <= z, ("marks do not fit one window", name, lo, hi)
            STILLS[name] = t[:2] + (min(max(t[2], a), z),) + t[3:]


_fit()
