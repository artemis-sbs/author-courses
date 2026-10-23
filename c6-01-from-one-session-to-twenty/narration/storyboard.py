"""Storyboard for c6-01-from-one-session-to-twenty: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and shown
by the Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Class 5 Lecture 5 leaves it (c5-05's example, with the
page's small rewordings of three landmark lines and without one paragraph of The Third Colony:
state "prep", all of it made before the video begins). The steps are typed in the video's order,
each state one step on the one before: "k1" (campaign.md: premise, pressure, loop), "k2" (the page
whole, its table empty), "w1" (The Wren), "w2" (One of Five: the page's own example, `same_as`),
"k3" (the table filled in with the page's measured values).

NOT SHOWN AS WRITTEN: Scene 1 and 7 name the Quest Log beside campaign.md and a Continue round
trip; scene 1 is drawn as the title card and campaign.md, scene 7 as the page's numbered steps and
its measured table (cards, no game). Scene 4's "I tried, with a page made to look exactly like a
record" is an act, not a screen: campaign.md stays up. Scene 7 fills the table at the end only
(k3), not column by column.

GAME STILLS. TAKEN 2026-10-23 in the engine (exe of 10-22 16:09); probe help (faces re-sent, ship beside a far landmark, steps completed or revealed, kills reported) in the session log. Planned here, taken by hand. NEVER start the engine for them from
this file: Open Universe rewrites the player's save. One game still, on the sandbox probe:
`python game.py c6-01-from-one-session-to-twenty start --state w2 --consoles server,helm`
Marks are left off every game still.
  1. Helm, at once, the handheld icon, Quests: game_c61_log4 (the four Class 5 leads, all open).
Never caption a face or a clock time.
"""
LECTURE = "c6-01-from-one-session-to-twenty"
TITLE = ("Class 6, Lecture 1", "From one session to twenty", "A campaign, and what the game remembers")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
CAMP = "campaign.md"
_EX = "c6-01-from-one-session-to-twenty/example"

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
                          "c5-05-the-map/example")},
       {FILE: _read("c5-05-the-map/example/" + FILE)})

_F = _read(_EX + "/" + FILE)
_C = _read(_EX + "/" + CAMP)
_CAMP1 = _C[:_C.index("## Three evenings written by hand")].rstrip("\n") + "\n"
_FILLED = (_C.replace("| Where the ship is | | |", "| Where the ship is | Kestrel Relay, (0, 0) | The same |")
           .replace("| Credits | | |", "| Credits | 400 | 400 |")
           .replace("| Standing with Hollin | | |", "| Standing with Hollin | 20 | 20 |")
           .replace("| The lead, One of Five | | |", "| The lead, One of Five | Done | Done |")
           .replace("| The job in hand | | |", "| The job in hand | Hollin Compact: Escort, Active | The same |")
           .replace("| Charted Locations | | |", "| Charted Locations | Kestrel Relay, The Wren | The same |"))
assert _FILLED != _C

_WS = _F.index("### [The Wren](the_wren)")
_WE = _F.index("\n## [", _WS)
_WREN = "\n" + _F[_WS:_WE].rstrip("\n") + "\n"
_LS = _F.index("### [The Long Count: One of Five](s01_go)")
_LE = _F.index("## [Dialogue](dialogue)")
_LEAD = _F[_LS:_LE]
_GO = "There is a place at (-4, -3) the Gleaners will not talk about. Go armed.\n"
_BONE = "Where the Gleaners stack what they cannot sell. They do not like it looked at.\n"

_chain("start", [
    ("prep", [("The last relay anyone keeps lit. Past it is rumor.", "The last relay anyone still maintains. Everything past it is rumor."),
              ("Where the Deepwell weighs its ore. Nothing leaves uncounted.", "Where the Deepwell weighs what it digs. Nothing leaves this system uncounted."),
              ("The third colony's ship, circling where she never landed.", "The third colony's ship, still in orbit over the place it never landed."),
              ("The Gleaners' dump. They do not like it looked at.", _BONE.rstrip("\n")),
              ("She was the third colony ship, and the last one out. Nobody has been to look in forty years.\n\n", "")]),
    ("k1", [("write", CAMP, _CAMP1)]),
    ("k2", [("write", CAMP, _C)]),
    ("w1", [(_BONE, _BONE + _WREN)]),
    ("w2", [(_GO + "\n## [Dialogue]", _GO + "\n" + _LEAD + "## [Dialogue]")]),
    ("k3", [("write", CAMP, _FILLED)]),
])
_same("w2", FILE, CAMP)

# ---- the stills
_E("e_camp_a", "k1", "## Premise", file=CAMP, off=4)
_E("e_camp_loop", "k1", "5. They carry what", file=CAMP, off=-4)
_E("e_camp_end", "k3", "| Charted Locations", file=CAMP, off=-2)
_E("e_wren", "w1", "### [The Wren](the_wren)", off=3)
_E("e_lead", "w2", "### [The Long Count: One of Five](s01_go)", off=3)
_E("e_leadt", "w2", "The Tern carried five boats", off=3)
_term("t_lint", "w2")

_game("game_c61_log4", "Helm, the handheld icon then Quests: the four Class 5 leads, all open, and The Long Count: One of Five beside them")

_card("card_title", "title")
_card("card_loop", "table", heading="Step 1 - Read a campaign that shipped", nth=1, kicker="Five decisions Storm's Beacon wrote down")
_card("card_three", "table", heading="Step 2 - Count what you have for one evening", nth=1, kicker="One evening, or twenty")
_card("card_steps", "list", heading="Step 6 - Play one evening, stop, and come back", kicker="Play, stop, come back")
_card("card_meas", "table", heading="Step 6 - Play one evening, stop, and come back", nth=1, kicker="Six things, before and after")
_card("card_keep", "table", heading="Step 6 - Play one evening, stop, and come back", nth=2, kicker="What the game keeps")
_card("card_notkeep", "table", heading="Step 6 - Play one evening, stop, and come back", nth=3, kicker="What the game does not keep")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "card_title"),
        _b(3, "e_camp_a", _ln("e_camp_a", "## Premise", 4))),
    "s02_a_campaign_that_shipped": _sc(1,
        _b(0, "card_loop"),
        _b(3, "card_loop", ("part", "r1")),
        _b(6, "card_loop", ("part", "r2")),
        _b(8, "card_loop", ("part", "r3")),
        _b(9, "card_loop")),
    "s03_one_evening_s_worth": _sc(2,
        _b(0, "game_c61_log4"),
        _b(4, "card_three"),
        _b(5, "card_three", ("part", "r1")),
        _b(6, "card_three", ("part", "r2")),
        _b(7, "card_three", ("part", "r3"))),
    "s04_the_premise": _sc(3,
        _b(0, "e_camp_a"),
        _b(3, "e_camp_a", _ln("e_camp_a", "## Premise", 4)),
        _b(5, "e_camp_a", _ln("e_camp_a", "## The pressure", 3)),
        _b(7, "e_camp_loop", _ln("e_camp_loop", "## The loop", 8)),
        _b(8, "e_camp_loop"),
        _b(10, "e_camp_loop")),
    "s05_the_first_lead": _sc(4,
        _b(0, "e_wren", _ln("e_wren", "### [The Wren](the_wren)", 7)),
        _b(2, "e_lead", _ln("e_lead", "### [The Long Count: One of Five](s01_go)", 5)),
        _b(4, "e_lead"),
        _b(5, "e_leadt", ("lines", _L("w2", "The Tern carried five boats") + 3, _L("w2", "The Tern carried five boats") + 3)),
        _b(8, "e_wren", _ln("e_wren", "A lifeboat off the Tern", 1)),
        _b(10, "e_lead", _tx("e_lead", "### [The Long Count: One of Five](s01_go)", "The Long Count")),
        _b(12, "e_lead", _tx("e_lead", "### [The Long Count: One of Five](s01_go)", "s01_go"))),
    "s06_lint": _sc(5,
        _b(0, "t_lint", ("span", 1, "0 error(s), 0 warning(s)")),
        _b(2, "t_lint", ("span", 1, "1 amd + 1 mast file(s)")),
        _b(3, "t_lint", ("span", 1, "1 amd + 1 mast file(s)"))),
    "s07_play_stop_come_back": _sc(6,
        _b(0, "card_steps"),
        _b(1, "card_steps", ("part", "item1")),
        _b(2, "card_steps", ("part", "item2")),
        _b(3, "card_steps", ("part", "item3"), ("part", "item4"), ("part", "item5")),
        _b(4, "card_meas", ("part", "head")),
        _b(5, "card_meas", ("part", "r1c2"), ("part", "r2c2"), ("part", "r3c2")),
        _b(6, "card_meas", ("part", "r4c2"), ("part", "r5c2")),
        _b(7, "card_meas", ("part", "r6c2")),
        _b(8, "card_steps", ("part", "item7")),
        _b(9, "card_steps", ("part", "item8")),
        _b(10, "card_meas", ("part", "r1c3")),
        _b(11, "card_meas", ("part", "r2c3"), ("part", "r3c3")),
        _b(12, "card_meas", ("part", "r4c3")),
        _b(13, "card_meas", ("part", "r5c3")),
        _b(14, "card_meas", ("part", "r6c3"))),
    "s08_what_the_game_keeps": _sc(6,
        _b(0, "card_keep"),
        _b(1, "card_keep", ("part", "r1")),
        _b(2, "card_keep", ("part", "r2")),
        _b(3, "card_keep", ("part", "r3")),
        _b(4, "card_keep", ("part", "r4")),
        _b(6, "card_keep", ("part", "r5")),
        _b(7, "card_keep", ("part", "r6")),
        _b(8, "card_keep")),
    "s09_what_it_does_not": _sc(6,
        _b(0, "card_notkeep"),
        _b(2, "card_notkeep", ("part", "r1")),
        _b(3, "card_notkeep", ("part", "r2")),
        _b(5, "card_keep", ("part", "r7"), ("part", "r8")),
        _b(6, "card_keep", ("part", "r7")),
        _b(7, "card_keep", ("part", "r8")),
        _b(8, "card_keep", ("part", "r9"))),
    "s10_close": _sc(None,
        _b(0, "e_camp_end", _ln("e_camp_end", "| What I checked", 8)),
        _b(2, "e_camp_end"),
        _b(4, "card_title")),
}
