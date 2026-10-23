"""Storyboard for c6-02-what-the-game-remembers: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and shown
by the Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 1 left it (c6-01's example: kestrel_verge.amd and
campaign.md). The steps are typed in the video's order, each state one step on the one before:
"l1" (The Second Colony's `Then: learn` line), "g1" (the Gleaners' new answer), "g2" (The Boats,
at the end of the file), "h1" (the Compact's answer with `if learned`), "h2" (The Report, the
page's own example, `same_as`: kestrel_verge.amd, 306 lines).

NOT SHOWN AS WRITTEN: the save file is not a file of the student's folder the tool can open, so
scene 8 (the last five lines, a step under shared_quests, the search for The Long Count that finds
nothing) and scene 9 (the saves folder, the Save Slot dial) are drawn as rows in the board's own
words, with the page's own lines. The start screen's dial was never seen by anyone (the page says
so); it is the "slots" card. Scenes 6 and 7 are the page's numbered steps and measured table, with
the one game still below at the hail.

GAME STILLS. NOT TAKEN YET: planned here, taken by hand. NEVER start the engine for them from
this file: Open Universe rewrites the player's save. One game still, on the sandbox probe:
`python game.py c6-02-what-the-game-remembers start --state h2 --consoles server,helm,comms`
Marks are left off every game still.
  1. Comms: select Hollin Compact, Hail, Pay the relay levy; Helm: Quest Log, engage The Breaking
     Yard; Comms: select the Gleaners' station, Hail, Ask what became of the Tern's boats; Helm:
     Quest Log, Charted Locations, Kestrel Relay, Engage; Comms: Hail Hollin Compact:
     game_c62_report (the answers, Report what the Gleaners said among them).
Never caption a face or a clock time.
"""
LECTURE = "c6-02-what-the-game-remembers"
TITLE = ("Class 6, Lecture 2", "What the game remembers", "Facts, the save, and slots")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
CAMP = "campaign.md"
_EX = "c6-02-what-the-game-remembers/example"

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
                          "c5-05-the-map/example", "c6-01-from-one-session-to-twenty/example")},
       {FILE: _read("c6-01-from-one-session-to-twenty/example/" + FILE),
        CAMP: _read("c6-01-from-one-session-to-twenty/example/" + CAMP)})

_F = _read(_EX + "/" + FILE)
_BS = _F.index("\n### [The Boats](gleaner_boats)")
_RS = _F.index("\n### [The Report](hollin_report)")
_BOATS = _F[_BS:_RS]
_REPORT = _F[_RS:]
_A_GL = "- [Ask what became of the Tern's boats](gleaner_boats) ; learn the gleaners broke a boat\n"
_A_HO = "- [Report what the Gleaners said](hollin_report) if learned the gleaners broke a boat\n"
_LEARN = "Then: learn the assay office buys salvage\n"

_chain("start", [
    ("l1", [("Done when: reach 3, 1\n---\nThe Deepwell Assembly keeps its books", "Done when: reach 3, 1\n" + _LEARN + "---\nThe Deepwell Assembly keeps its books")]),
    ("g1", [("- [Back away](gleaner_bye) ;", _A_GL + "- [Back away](gleaner_bye) ;")]),
    ("g2", [("% Run along, then.\n", "% Run along, then.\n" + _BOATS)]),
    ("h1", [("- [Sign off](hollin_bye)\n", _A_HO + "- [Sign off](hollin_bye)\n")]),
    ("h2", [("may remember which.\n", "may remember which.\n" + _REPORT)]),
])
_same("h2", FILE)

# ---- the stills
_E("e_then", "l1", "Then: learn the assay office buys salvage", off=3)
_E("e_gans", "g1", "[Ask what became of the Tern's boats]", off=4)
_E("e_boats", "g2", "### [The Boats](gleaner_boats)", off=4)
_E("e_hans", "h1", "[Report what the Gleaners said]", off=3)
_E("e_report", "h2", "### [The Report](hollin_report)", off=5)
_term("t_lint", "h2")

_game("game_c62_report", "Comms with the Hollin Compact selected, Hail: the answers, Report what the Gleaners said among them")

_card("card_title", "title")
_card("card_facts", "table", heading="Step 1 - What a fact is", nth=1, kicker="Learn it, and ask for it")
_card("card_play", "list", heading="Step 6 - Play, stop, and come back", kicker="Play, stop, come back")
_card("card_meas", "table", heading="Step 6 - Play, stop, and come back", nth=1, kicker="What was measured")
_card("card_savetail", "rows", kicker="The last five lines of the save", header=["The save says", "It means"],
      rows=[["state:", "What the game saved"], ["  boarding_facts:", "What the crew has learned"], ["    \"\":", "For the whole game"], ["      - the assay office buys salvage", "A fact"], ["      - the gleaners broke a boat", "A fact"]])
_card("card_savestep", "rows", kicker="A step of the story, in the save", header=["A step is five lines", "It means"],
      rows=[["lead_deepwell:", "The step's key"], ["  authored: true", "Written by you"], ["  state: 99", "Done"], ["  progress: 0", "How far the crew has got"], ["  children: {}", "Nothing under it"]])
_card("card_search", "rows", kicker="Search the save", header=["Looked for", "Found"],
      rows=[["The Long Count", "Nothing found"], ["A step's title or text", "Nothing found"]])
_card("card_states", "table", heading="Step 7 - Read the save", nth=1, kicker="What a state number means")
_card("card_slots", "rows", kicker="Slots: one universe, up to six campaigns", header=["Save file", "Whose campaign"],
      rows=[["universe_save_the_kestrel_verge_1.yaml", "Slot 1: the Tuesday table"],
            ["universe_save_the_kestrel_verge_2.yaml", "Slot 2: the Thursday table, or your own walks"]])
_card("card_won", "table", heading="Step 10 - A campaign that was won", nth=1, kicker="Continue a won campaign")
_card("card_all", "table", heading="Step 8 - The whole list", nth=1, kicker="Everything the save keeps")
_card("card_exercise", "list", heading="Exercise", kicker="Your turn")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c62_report"),
        _b(3, "card_savetail")),
    "s02_what_a_fact_is": _sc(1,
        _b(0, "card_facts"),
        _b(5, "card_facts", ("part", "r1"), ("part", "r2")),
        _b(7, "card_facts", ("part", "r3"), ("part", "r4"), ("part", "r5")),
        _b(9, "card_facts")),
    "s03_learned_by_finishing_a_step": _sc(2,
        _b(0, "e_then", ("lines", _L("l1", "Then: learn the assay office buys salvage") - 1, _L("l1", "Then: learn the assay office buys salvage"))),
        _b(2, "e_then", _tx("e_then", "Then: learn the assay office buys salvage")),
        _b(3, "e_then", _tx("e_then", "Then: learn the assay office buys salvage", "learn the assay office buys salvage")),
        _b(4, "e_then", _tx("e_then", "Then: learn the assay office buys salvage", "Then:")),
        _b(9, "e_then", _tx("e_then", "Then: learn the assay office buys salvage"))),
    "s04_learned_in_a_hail": _sc(3,
        _b(0, "e_gans", _tx("e_gans", "[Ask what became of the Tern's boats]", "[Ask what became of the Tern's boats](gleaner_boats)")),
        _b(2, "e_gans", _tx("e_gans", "[Ask what became of the Tern's boats]", "Ask what became of the Tern's boats")),
        _b(3, "e_gans", _tx("e_gans", "[Ask what became of the Tern's boats]", ";")),
        _b(4, "e_gans", _tx("e_gans", "[Ask what became of the Tern's boats]", "learn the gleaners broke a boat")),
        _b(5, "e_boats", _ln("e_boats", "### [The Boats](gleaner_boats)", 5))),
    "s05_asking_what_they_know": _sc(4,
        _b(0, "e_hans", _tx("e_hans", "[Report what the Gleaners said]", "[Report what the Gleaners said](hollin_report)")),
        _b(2, "e_hans", _tx("e_hans", "[Report what the Gleaners said]", "if learned the gleaners broke a boat")),
        _b(4, "e_report", _ln("e_report", "### [The Report](hollin_report)", 6)),
        _b(5, "e_report", _tx("e_report", "%{learned the assay office buys salvage} Entered.", "%{learned the assay office buys salvage}")),
        _b(6, "e_report", _tx("e_report", "%{learned the assay office buys salvage < 1}")),
        _b(7, "e_report", _tx("e_report", "%{learned the assay office buys salvage} Entered.", "%{learned the assay office buys salvage}"),
           _tx("e_report", "%{learned the assay office buys salvage < 1}")),
        _b(9, "t_lint", ("part", "run1:clean")),
        _b(10, "t_lint", ("span", 1, "0 error(s), 0 warning(s)"))),
    "s06_play_it": _sc(6,
        _b(0, "card_play"),
        _b(1, "card_play", ("part", "item1")),
        _b(2, "card_play", ("part", "item2")),
        _b(3, "card_play", ("part", "item3")),
        _b(4, "game_c62_report"),
        _b(6, "card_play", ("part", "item4")),
        _b(9, "card_play", ("part", "item5"))),
    "s07_stop_and_come_back": _sc(6,
        _b(0, "card_play", ("part", "item6")),
        _b(1, "card_play", ("part", "item7")),
        _b(2, "card_play", ("part", "item8")),
        _b(4, "card_meas", ("part", "r4c3"), ("part", "r5c3")),
        _b(5, "card_meas", ("part", "r1c3"), ("part", "r2c3"), ("part", "r3c3"))),
    "s08_inside_the_save": _sc(7,
        _b(0, "card_savetail"),
        _b(1, "card_savetail", ("part", "r4"), ("part", "r5")),
        _b(3, "card_savestep"),
        _b(4, "card_savestep", ("part", "r1"), ("part", "r3")),
        _b(5, "card_savestep"),
        _b(6, "card_search", ("part", "r1")),
        _b(8, "card_states"),
        _b(9, "card_savestep")),
    "s09_slots_and_a_campaign_that_wa": _sc(9,
        _b(0, "card_slots"),
        _b(1, "card_slots", ("part", "r1c1")),
        _b(3, "card_slots", ("part", "r1"), ("part", "r2")),
        _b(6, "card_won"),
        _b(7, "card_won", ("part", "r2")),
        _b(8, "card_won", ("part", "r1"))),
    "s10_your_turn": _sc(8,
        _b(0, "card_all"),
        _b(2, "card_exercise"),
        _b(3, "card_exercise", ("part", "item1")),
        _b(5, "card_exercise", ("part", "item2")),
        _b(7, "card_exercise", ("part", "item5"))),
}
