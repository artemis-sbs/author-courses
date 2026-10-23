"""Storyboard for c6-08-playtesting: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 5 storyboards. Caption numbers are those of shots.py. The helpers below only build
the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 7 left it (kestrel_verge.amd = c6-07's
example; campaign.md = c6-07's too). The steps are typed in the video's order, each state one
step on the one before: Step 2, the log file playtest.md ("p_log", the page's own example);
Step 4, the Objective line on Her Log ("o_herlog"), then on The Plover's Price ("final", the
page's own example for both files).

NOT SHOWN AS WRITTEN: (1) scene 1 says the clock table is "filled in by hand". The lecture gives
no numbers for it, so it is shown as the page's own blank log: nothing is invented. (2) The save
file is the player's and does not exist in the folder: scene 6 shows the page's quoted lines of
it, and the page's table of `state:` values, as cards. (3) File Explorer deleting and copying the
save (scenes 4 and 7) and the walk in the game (scene 4) are cards in the page's own words. (4)
The bible page in a browser is the command (a terminal) and then the page's table of what to read.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine
for it from this file: Open Universe rewrites the player's save. ONE game, on the sandbox probe:
`python game.py c6-08-playtesting start --state final --consoles server,helm,science,comms`
Marks are left off every game still until it exists. Press order (Step 6 of the page):
  1. Helm, the handheld icon, Quests, Her Log selected: game_c68_order (the step in the Quest
     Log with its order, Scan the Wren from Science, above its description).
Never caption a face or a clock time.
"""
import os
import re

LECTURE = "c6-08-playtesting"
TITLE = ("Class 6, Lecture 8", "Playtesting", "Real people at the table, and what the game wrote down")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
CAMP = "campaign.md"
LOG = "playtest.md"
_EX = "c6-08-playtesting/example"
_PREV = "c6-07-mixing-the-play-styles/example"
_MORE = ("c6-05-campaign-architecture/example", "c6-06-reputation-arcs/example", "c6-07-mixing-the-play-styles/example")


_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_PRIOR = ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example", "c5-05-the-map/example",
          "c6-01-from-one-session-to-twenty/example", "c6-02-what-the-game-remembers/example",
          "c6-03-designing-a-session/example", "c6-04-the-episode/example")


def _read(rel):
    """A file of the course folder, with plain newlines."""
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as _fh:
        return _fh.read().replace("\r\n", "\n")


_TEXT = {}      # state -> {file: text}, kept so marks can find their lines
_OF = {}        # still -> (state, file)
STATES = {}
STILLS = {}


def _chain(base, steps):
    """Each step (name, {file: text}) is one state on the one before it."""
    prev = base
    for name, files in steps:
        texts = dict(_TEXT[prev])
        out = []
        for f, t in files.items():
            texts[f] = t
            out.append(("write", f, t))
        _TEXT[name] = texts
        STATES[name] = {"base": prev, "edits": out}
        prev = name


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


def _tx(still, needle, words=None, nth=1, off=0):
    s, f = _OF[still]
    ln = _L(s, needle, nth, f) + off
    w = words or needle.split("\n")[0]
    assert w in _TEXT[s][f].split("\n")[ln - 1], (still, w)
    return ("text", ln, w)


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


def _term(name, state, cmd=None):
    STILLS[name] = ("terminal", [(state, cmd or ("sbs lint " + MISSION))])


def _game(name, what):
    STILLS[name] = ("game", what)


def _card(name, kind, **opts):
    STILLS[name] = ("card", kind, opts)



_PRIOR = _PRIOR + _MORE
STATES["start"] = {"folder": "c5-02-your-universe-file/example", "over": _PRIOR}
_TEXT["start"] = {FILE: _read(_PREV + "/" + FILE), CAMP: _read(_PREV + "/" + CAMP)}

_FA = _read(_EX + "/" + FILE)
_FL = _read(_EX + "/" + LOG)
_O1 = "Objective: Scan the Wren from Science\n"
_O2 = "Objective: Hail the Assay Office on Comms\n"
assert _FA.count(_O1) == 1 and _FA.count(_O2) == 1
_T_HER = _FA.replace(_O2, "")
assert _T_HER.replace(_O1, "") == _TEXT["start"][FILE], "the base of the amd"

_chain("start", [
    ("p_log", {LOG: _FL}),
    ("o_herlog", {FILE: _T_HER}),
    ("final", {FILE: _FA}),
])
_same("final", FILE, LOG)

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_clock", "p_log", "### The clock", off=8, file=LOG)
_E("e_wrote", "p_log", "### What I wrote down while they played", off=4, file=LOG)
_E("e_rec", "p_log", "### What the game recorded", off=5, file=LOG)
_E("e_three", "p_log", "### What I will change before next week", off=2, file=LOG)
_E("e_herlog", "o_herlog", "Objective: Scan the Wren from Science", off=4)
_E("e_plover", "final", "Objective: Hail the Assay Office on Comms", off=4)
_term("t_lint", "p_log")
_term("t_lint2", "final")
_term("t_bible", "p_log", "sbs docs MyUniverse --lens bible")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c68_order", "Helm, the handheld icon then Quests: Her Log in the Quest Log with its order, Scan the Wren from Science, above the description")

# drawn
_card("card_spine", "table", heading="Step 1 - Three checks before anybody arrives", nth=1, kicker="Read only reached from and leads to")
_card("card_delete", "rows", kicker="Walk it, then delete the save", header=["Do this", "Why"],
      rows=[["Walk the spine alone, as fast as you can", "Engage down the steps to see they are joined"],
            ["Delete universe_save_the_kestrel_verge_1.yaml in common_data\\saves", "This is the one people forget"],
            ["Leave no save behind", "A crew that sits down to a walked save starts at the end of your act"]])
_card("card_rules", "points", kicker="Five rules at the table", items=[
    "Say what the game is, and nothing about the story.",
    "Do not answer questions. Write them down.",
    "Write the time at each Done.",
    "Do not stop them leaving the spine.",
    "End it yourself."])
_card("card_log", "points", kicker="The runtime log", items=[
    "Open mast.runtime.log in your mission folder.",
    "It should be empty."])
_card("card_rep", "rows", kicker="Under the ship's name, in the save", header=["In the save", "What it holds"],
      rows=[["reputation: hollin", "honesty 10, generosity 50"],
            ["reputation: deepwell", "temperament -20"],
            ["reputation: gleaners", "method 35"],
            ["side_credits: tsn", "2870"]])
_card("card_state", "table", heading="Step 3 - Read what the game recorded", nth=1, kicker="Every step of your story has a state")
_card("card_copy", "rows", kicker="Keep a copy", header=["Do this", "Because"],
      rows=[["Copy the save to Documents as evening_01.yaml", "Name it for the evening"],
            ["Do it before New Game on the start screen", "New Game replaces the save without asking. A copy every week is the only undo"],
            ["Keep it where the crew does not look", "It holds every hidden step, word for word"]])
_card("card_changes", "table", heading="Step 4 - Compare, and change three things", nth=1, kicker="The usual first three")
_card("card_pt", "table", heading="Step 6 - Play it again", nth=1, kicker="What you need to know about a playtest")
_card("card_next", "title", kicker="Next", title="Lecture 9", sub="Revising between sessions")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "e_clock", _ln("e_clock", "| Part | Planned |", 8)),
        _b(2, "e_clock", _tx("e_clock", "| Part | Planned |", "Played")),
        _b(3, "e_wrote", _tx("e_wrote", "Questions the crew asked out loud:", "Questions the crew asked out loud:")),
        _b(4, "e_wrote", _tx("e_wrote", "Things they never found:", "Things they never found:")),
        _b(6, "e_rec", _ln("e_rec", "| From the save file |", 6)),
        _b(7, "e_three", _ln("e_three", "1.\n2.\n3.", 3))),
    "s02_lint_first": _sc(1,
        _b(0, "t_lint"),
        _b(3, "t_lint", ("part", "run1:clean"))),
    "s03_read_the_spine": _sc(1,
        _b(0, "t_bible"),
        _b(1, "card_spine"),
        _b(3, "card_spine", ("part", "head")),
        _b(4, "card_spine", ("part", "r1")),
        _b(5, "card_spine", ("part", "r2")),
        _b(6, "card_spine", ("part", "r3")),
        _b(7, "card_spine", ("part", "r5"))),
    "s04_walk_then_delete": _sc(1,
        _b(0, "card_delete"),
        _b(1, "card_delete", ("part", "r1")),
        _b(2, "card_delete", ("part", "r2")),
        _b(6, "card_delete", ("part", "r3"))),
    "s05_at_the_table": _sc(2,
        _b(0, "card_rules"),
        _b(2, "card_rules", ("part", "item1")),
        _b(3, "card_rules", ("part", "item2")),
        _b(6, "card_rules", ("part", "item3")),
        _b(7, "card_rules", ("part", "item4")),
        _b(10, "card_rules", ("part", "item5"))),
    "s06_read_the_save": _sc(3,
        _b(0, "card_log"),
        _b(2, "card_rep"),
        _b(4, "card_rep", ("part", "r1"), ("part", "r2"), ("part", "r3")),
        _b(5, "card_rep", ("part", "r4")),
        _b(6, "card_state"),
        _b(8, "card_state", ("part", "r1"), ("part", "r2")),
        _b(9, "card_state", ("part", "r3")),
        _b(10, "card_state", ("part", "r1"))),
    "s07_keep_a_copy": _sc(3,
        _b(0, "card_copy", ("part", "r1")),
        _b(2, "card_copy", ("part", "r2")),
        _b(5, "card_copy", ("part", "r3"))),
    "s08_three_changes": _sc(4,
        _b(0, "card_changes"),
        _b(3, "card_changes", ("part", "r2")),
        _b(5, "e_herlog", _ln("e_herlog", "Objective: Scan the Wren from Science", 5)),
        _b(6, "e_herlog", _tx("e_herlog", "Objective: Scan the Wren from Science", "Objective:")),
        _b(7, "e_herlog", _tx("e_herlog", "Objective: Scan the Wren from Science", "from Science")),
        _b(8, "e_herlog", _tx("e_herlog", "Objective: Scan the Wren from Science")),
        _b(9, "e_plover", _tx("e_plover", "Objective: Hail the Assay Office on Comms"))),
    "s09_again_with_new_people": _sc(6,
        _b(0, "t_lint2", ("part", "run1:clean")),
        _b(1, "card_delete", ("part", "r2")),
        _b(2, "game_c68_order"),
        _b(3, "card_pt", ("part", "r4")),
        _b(6, "card_pt", ("part", "r4"))),
    "s10_close": _sc(6,
        _b(0, "card_pt", ("part", "r1")),
        _b(1, "card_pt", ("part", "r2")),
        _b(3, "card_pt", ("part", "r5")),
        _b(4, "card_next")),
}
