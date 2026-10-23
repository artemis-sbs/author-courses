"""Storyboard for c6-04-the-episode: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and shown
by the Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 3 left it (c6-03's example: kestrel_verge.amd and
campaign.md). The steps are typed in the video's order, each state one step on the one before:
"pat" (campaign.md: the pattern and its blank sheet), "sheet2" (campaign.md whole: the Evening 2
sheet), "dun" (The Dunlin on the map), "then2" (`Then: reveal s02_clear` on Two of Five), "recs"
(Bait, Enter It Twice and Three of Five: the page's own examples, `same_as` both files).

NOT SHOWN AS WRITTEN: scene 1's "two columns" is drawn as one table (evening 1 and evening 2,
record by record). Scene 3's pattern block is shown as it sits in campaign.md, in three windows
of the editor (the page's slot table is not drawn: a fenced "## ..." line inside the pattern ends
a heading's section for the picture tool, so the tables after it are drawn as rows in the
board's own words). Scene 5 adds the three records in one state ("recs"), not one at a time.

GAME STILLS. TAKEN 2026-10-23 in the engine (exe of 10-22 16:09); probe help (faces re-sent, ship beside a far landmark, steps completed or revealed, kills reported) in the session log. Planned here, taken by hand. NEVER start the engine for them from
this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the sandbox probe:
`python game.py c6-04-the-episode start --state recs --consoles server,helm,science,weapons`
Marks are left off every game still. Press order:
  1. Helm: play evening 1 to its hook (engage One of Five, Science scans The Wren, engage Enter
     It). Engage The Long Count: Two of Five. On arrival: game_c64_dunlin (the card reading The
     Dunlin, the warning that she is guarded, and Bait in the Quest Log).
  2. Weapons: destroy two of the three guards. Engage Enter It Twice. Home, Quest Log, Charted
     Locations: game_c64_charted (Kestrel Relay, The Wren and The Dunlin).
Never caption a face or a clock time.
"""

LECTURE = "c6-04-the-episode"
TITLE = ("Class 6, Lecture 4", "The episode", "A pattern you fill in twenty times")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
CAMP = "campaign.md"
_EX = "c6-04-the-episode/example"

import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))


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
        if file.endswith(".md"):
            opts["wrap"] = True
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


# ---- the states
_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c6-01-from-one-session-to-twenty/example",
                          "c6-03-designing-a-session/example")},
       {FILE: _read("c6-03-designing-a-session/example/" + FILE),
        CAMP: _read("c6-03-designing-a-session/example/" + CAMP)})

_F = _read(_EX + "/" + FILE)
_C = _read(_EX + "/" + CAMP)
_CPAT = _C[:_C.index("## Evening 2 - Two of Five")].rstrip("\n") + "\n"
_DI = _F.index("### [The Dunlin](the_dunlin)")
_DE = _F.index("\n## [", _DI)
_DUN = _F[_DI:_DE]
_RI = _F.index("### [The Long Count: Bait](s02_clear)")
_RE = _F.index("## [Dialogue](dialogue)")
_RECS = _F[_RI:_RE]
_ROW = "| The Dunlin | (-2, 3) | Something answers on her channel |\n\n## [Dialogue]"

_chain("start", [
    ("pat", [("write", CAMP, _CPAT)]),
    ("sheet2", [("write", CAMP, _C)]),
    ("dun", [("Her davit number can still be read: one of five.\n\n", "Her davit number can still be read: one of five.\n\n" + _DUN + "\n")]),
    ("then2", [("Done when: reach -2, 3\n---\n", "Done when: reach -2, 3\nThen: reveal s02_clear\n---\n")]),
    ("recs", [(_ROW, _ROW.replace("## [Dialogue]", "") + _RECS + "## [Dialogue]")]),
])
_same("recs", FILE, CAMP)


def _txa(still, anchor, needle, words=None):
    """A text mark on the first `needle` found after the first `anchor` of the still's file."""
    st, f = _OF[still]
    t = _TEXT[st][f]
    j = t.index(needle, t.index(anchor))
    return ("text", t.count(chr(10), 0, j) + 1, words or needle)


# ---- the stills
_E("e_pat1", "pat", "### [PLACE NAME](PLACE_KEY)", file=CAMP, off=8)
_E("e_pat2", "pat", "## The count so far", file=CAMP, off=0)
_E("e_pat3", "pat", "Done when: ENDING", file=CAMP, off=2)
_E("e_pat4", "pat", "Done when: ENDING", file=CAMP, off=10)
_E("e_sheet2", "sheet2", "## Evening 2 - Two of Five", file=CAMP, off=2)
_E("e_dun", "dun", "### [The Dunlin](the_dunlin)", off=4)
_E("e_two", "then2", "Then: reveal s02_clear", off=4)
_E("e_bait", "recs", "### [The Long Count: Bait](s02_clear)", off=5)
_E("e_home", "recs", "### [The Long Count: Enter It Twice](s02_home)", off=5)
_E("e_three", "recs", "## The count so far", nth=2, off=3)
_E("e_two2", "recs", "Done when: destroy 2 enemies", off=3)
_term("t_lint", "recs")

_game("game_c64_dunlin", "Comms on arrival at (-2, 3), the ship's own channel: the Threat line 'The Dunlin is guarded - hostiles on approach.' and the Dunlin charted")
_game("game_c64_charted", "Helm, Quest Log, Charted Locations: Kestrel Relay, The Wren and The Dunlin")

_card("card_title", "title")
_card("card_two", "rows", kicker="Evening 1 and evening 2, record by record", header=["The record", "Evening 1", "Evening 2"],
      rows=[["The place", "The Wren", "The Dunlin"],
            ["The open", "One of Five", "Two of Five"],
            ["The objective", "Her Log", "Bait"],
            ["The way home", "Enter It", "Enter It Twice"],
            ["The hook", "Two of Five", "Three of Five"]])
_card("card_built", "table", heading="Step 1 - What Storm's Beacon learned about patterns", nth=1, kicker="Built once, used by every episode")
_card("card_endings", "rows", kicker="Four endings an objective can have", header=["Done when", "The evening is about", "Who is busy"],
      rows=[["scan 1 derelict", "Finding something out", "Science"],
            ["destroy 2 enemies", "A fight the crew cannot walk away from", "Weapons, Engineering"],
            ["signal WORD", "A conversation", "Comms"],
            ["reach X, Y", "Getting somewhere else, further on", "Helm"]])
_card("card_play", "list", heading="Step 5 - Play it", kicker="Play evening 2")
_card("card_facts", "table", heading="Step 5 - Play it", nth=1, kicker="What you need to know about a pattern")
_card("card_next", "title", kicker="Next", title="Lecture 5", sub="Campaign architecture")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "card_two"),
        _b(1, "card_two", ("part", "r1"), ("part", "r2"), ("part", "r3"), ("part", "r4"), ("part", "r5")),
        _b(2, "card_title")),
    "s02_build_it_once": _sc(1,
        _b(0, "card_built"),
        _b(6, "card_built", ("part", "r1"), ("part", "r2"), ("part", "r3"), ("part", "r4"), ("part", "r5")),
        _b(7, "card_built", ("part", "r1")),
        _b(8, "card_built", ("part", "r2")),
        _b(9, "card_built", ("part", "r3")),
        _b(10, "card_built", ("part", "r4"), ("part", "r5")),
        _b(11, "card_built")),
    "s03_the_pattern": _sc(2,
        _b(0, "e_pat1", _ln("e_pat1", "At: X, Y", 5)),
        _b(1, "e_pat1", _ln("e_pat1", "At: X, Y", 5)),
        _b(2, "e_pat1"),
        _b(3, "e_pat1", _tx("e_pat1", "### [The Long Count: OPEN TITLE](sNN_go)", "sNN_go")),
        _b(4, "e_pat1", _tx("e_pat1", "At: X, Y"), _tx("e_pat1", "Done when: reach X, Y")),
        _b(5, "e_pat1", _tx("e_pat1", "Terrain: COVER"), _tx("e_pat1", "Guards: SHIPS")),
        _b(6, "e_pat3", _tx("e_pat3", "Done when: ENDING")),
        _b(7, "e_pat4", _tx("e_pat4", "Reward: PAY credits")),
        _b(8, "e_pat2", _ln("e_pat2", "## The count so far", 5)),
        _b(10, "e_pat2", _ln("e_pat2", "| BOAT |", 1)),
        _b(11, "e_pat2", _ln("e_pat2", "| BOAT |", 1)),
        _b(12, "e_pat3", _tx("e_pat3", "### [The Long Count: OBJECTIVE TITLE](sNN_DEED)", "OBJECTIVE TITLE"),
           _tx("e_pat3", "### [The Long Count: HOME TITLE](sNN_home)", "HOME TITLE")),
        _b(13, "e_pat3", _tx("e_pat3", "WHAT IS HERE. WHAT TO DO ABOUT IT.")),
        _b(14, "e_pat1")),
    "s04_four_endings": _sc(2,
        _b(0, "card_endings"),
        _b(1, "card_endings", ("part", "r1")),
        _b(2, "card_endings", ("part", "r2")),
        _b(3, "card_endings", ("part", "r3")),
        _b(5, "card_endings", ("part", "r4")),
        _b(7, "card_endings")),
    "s05_evening_two": _sc(3,
        _b(0, "e_sheet2", _ln("e_sheet2", "## Evening 2 - Two of Five", 2)),
        _b(1, "e_dun", _ln("e_dun", "### [The Dunlin](the_dunlin)", 7)),
        _b(2, "e_dun", _txa("e_dun", "### [The Dunlin](the_dunlin)", "Terrain: nebula"), _txa("e_dun", "### [The Dunlin](the_dunlin)", "Guards: torgoth")),
        _b(3, "e_two", _ln("e_two", "Done when: reach -2, 3", 2)),
        _b(6, "e_two", _tx("e_two", "Then: reveal s02_clear")),
        _b(7, "e_bait", _ln("e_bait", "### [The Long Count: Bait](s02_clear)", 12)),
        _b(10, "e_bait", _tx("e_bait", "[](ship://torgoth_destroyer)", "ship://torgoth_destroyer")),
        _b(13, "e_home", _ln("e_home", "### [The Long Count: Enter It Twice](s02_home)", 12)),
        _b(15, "e_three", _ln("e_three", "## The count so far", 6, nth=2)),
        _b(16, "e_three", _tx("e_three", "| The Plover | Sold |", "The Plover")),
        _b(17, "e_three")),
    "s06_two_of_three": _sc(3,
        _b(0, "e_two2", _tx("e_two2", "Done when: destroy 2 enemies")),
        _b(5, "e_dun", _txa("e_dun", "### [The Dunlin](the_dunlin)", "Guards: torgoth")),
        _b(9, "e_two2", _tx("e_two2", "Done when: destroy 2 enemies"))),
    "s07_lint_and_play": _sc(5,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(1, "card_play", ("part", "item1")),
        _b(2, "card_play", ("part", "item2")),
        _b(3, "game_c64_dunlin"),
        _b(4, "card_play", ("part", "item3")),
        _b(6, "card_play", ("part", "item4")),
        _b(8, "game_c64_charted")),
    "s08_close": _sc(5,
        _b(0, "card_facts", ("part", "r2")),
        _b(2, "card_facts", ("part", "r3")),
        _b(6, "card_facts", ("part", "r4")),
        _b(8, "card_next")),
}
