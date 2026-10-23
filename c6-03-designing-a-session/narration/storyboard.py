"""Storyboard for c6-03-designing-a-session: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and shown
by the Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 1 left it (c6-01's kestrel_verge.amd, and its
campaign.md with the measured table filled in: state "prep", made before the video begins). The
steps are typed in the video's order, each state one step on the one before: "sheet" (campaign.md
with the Evening 1 section), "open" (`Then: reveal s01_scan` on One of Five), "obj" (Her Log),
"clim" (`Guards: torgoth` on The Wren), "hook" (Enter It and Two of Five: the page's own
examples, `same_as` both files).

NOT SHOWN AS WRITTEN: the sheet is shown whole, not typed row by row. Scene 7's "select the text
of Two of Five, then the table" is two marks on the one still. Scene 8 plays the evening: the
page's numbered steps are a card, with two game stills (the Wren's arrival, the Quest Log at the
end). Nobody has seen the scan in the real game (the page says so).

GAME STILLS. TAKEN 2026-10-23 in the engine (exe of 10-22 16:09); probe help (faces re-sent, ship beside a far landmark, steps completed or revealed, kills reported) in the session log. Planned here, taken by hand. NEVER start the engine for them from
this file: Open Universe rewrites the player's save. ONE game, TWO windows, on the sandbox probe:
`python game.py c6-03-designing-a-session start --state hook --consoles server,helm,science`
Marks are left off every game still. Press order:
  1. Helm, Quest Log: Engage The Long Count: One of Five. On arrival: game_c63_wren (the card
     reading The Wren, and the warning that she is guarded).
  2. Science: scan The Wren. Helm: Engage The Long Count: Enter It. Home, Quest Log:
     game_c63_end (Two of Five open, three steps of The Long Count under Done).
Never caption a face or a clock time.
"""

LECTURE = "c6-03-designing-a-session"
TITLE = ("Class 6, Lecture 3", "Designing a session", "Open, objective, climax, hook")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
CAMP = "campaign.md"
_EX = "c6-03-designing-a-session/example"

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
_C = _read(_EX + "/" + CAMP)
_CPRE = _C[:_C.index("## Evening 1 - One of Five")].rstrip("\n") + "\n"
_LOGI = _F.index("### [The Long Count: Her Log](s01_scan)")
_HOMEI = _F.index("### [The Long Count: Enter It](s01_home)")
_DIALI = _F.index("## [Dialogue](dialogue)")
_LOGB = _F[_LOGI:_HOMEI]
_HOMEB = _F[_HOMEI:_DIALI]

_chain("start", [
    ("prep", [("write", CAMP, _CPRE)]),
    ("sheet", [("write", CAMP, _C)]),
    ("open", [("Done when: reach 2, 2\n---\n", "Done when: reach 2, 2\nThen: reveal s01_scan\n---\n")]),
    ("obj", [("be there before they are.\n\n## [Dialogue]", "be there before they are.\n\n" + _LOGB + "## [Dialogue]")]),
    ("clim", [("Terrain: asteroids\n---\nA lifeboat off the Tern", "Terrain: asteroids\nGuards: torgoth\n---\nA lifeboat off the Tern")]),
    ("hook", [("before they strip it.\n\n## [Dialogue]", "before they strip it.\n\n" + _HOMEB + "## [Dialogue]")]),
])
_same("hook", FILE, CAMP)

# ---- the stills
_E("e_sheet", "sheet", "| Climax", file=CAMP, off=0)
_E("e_open", "open", "Then: reveal s01_scan", off=4)
_E("e_obj", "obj", "### [The Long Count: Her Log](s01_scan)", off=5)
_E("e_clim", "clim", "Guards: torgoth", off=3)
_E("e_home", "hook", "### [The Long Count: Enter It](s01_home)", off=6)
_E("e_two", "hook", "### [The Long Count: Two of Five](s02_go)", off=8)
_term("t_lint", "hook")

_game("game_c63_wren", "Comms on arrival at (2, 2), the ship's own channel: the Threat line 'The Wren is guarded - hostiles on approach.', the Wren charted, and Sensors flagging the derelict")
_game("game_c63_end", "Helm, Quest Log at the end of the evening: Two of Five open, three steps of The Long Count under Done")

_card("card_parts", "table", heading="Step 1 - The four parts of an evening", nth=1, kicker="Open, objective, climax, hook")
_card("card_nogame", "table", heading="Step 1 - The four parts of an evening", nth=2, kicker="What the game has no idea of")
_card("card_play", "list", heading="Step 8 - Play it", kicker="Play the evening")
_card("card_facts", "table", heading="Step 8 - Play it", nth=1, kicker="What you need to know about an evening")
_card("card_next", "title", kicker="Next", title="Lecture 4", sub="The episode")

def _txa(still, anchor, needle, words=None):
    """A text mark on the first `needle` found after the first `anchor` of the still's file."""
    st, f = _OF[still]
    t = _TEXT[st][f]
    j = t.index(needle, t.index(anchor))
    return ("text", t.count(chr(10), 0, j) + 1, words or needle)


BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c63_end")),
    "s02_four_parts": _sc(1,
        _b(0, "card_parts"),
        _b(1, "card_parts", ("part", "r1")),
        _b(2, "card_parts", ("part", "r2")),
        _b(3, "card_parts", ("part", "r3")),
        _b(4, "card_parts", ("part", "r4")),
        _b(6, "card_parts", ("part", "r1c4"), ("part", "r2c4"), ("part", "r3c4"), ("part", "r4c4"))),
    "s03_what_the_game_does_not_know": _sc(1,
        _b(0, "card_nogame"),
        _b(2, "card_nogame", ("part", "r1")),
        _b(3, "card_nogame", ("part", "r2")),
        _b(4, "card_nogame", ("part", "r3")),
        _b(5, "card_nogame"),
        _b(7, "card_nogame", ("part", "r1")),
        _b(8, "card_nogame", ("part", "r2")),
        _b(9, "card_nogame", ("part", "r3"))),
    "s04_the_sheet": _sc(2,
        _b(0, "e_sheet", _ln("e_sheet", "## Evening 1 - One of Five", 2)),
        _b(2, "e_sheet", _ln("e_sheet", "| Part | What happens", 6)),
        _b(3, "e_sheet", _ln("e_sheet", "- **The crew learns:**", 5)),
        _b(4, "e_sheet", _ln("e_sheet", "- **The crew learns:**", 3)),
        _b(5, "e_sheet", _ln("e_sheet", "- **It ends when:**", 1)),
        _b(6, "e_sheet", _tx("e_sheet", "- **The crew learns:**", "The crew learns:"))),
    "s05_open_and_objective": _sc(3,
        _b(0, "e_open", _ln("e_open", "Done when: reach 2, 2", 2)),
        _b(2, "e_open", _tx("e_open", "Then: reveal s01_scan")),
        _b(4, "e_obj", _ln("e_obj", "### [The Long Count: Her Log](s01_scan)", 9)),
        _b(5, "e_obj", _tx("e_obj", "Done when: scan 1 derelict")),
        _b(7, "e_obj", _tx("e_obj", "The Wren is here, and so are ships with cutting gear.", "Get Science close enough")),
        _b(9, "e_obj", _ln("e_obj", "The Wren is here, and so are ships with cutting gear.", 1)),
        _b(10, "e_obj", _ln("e_obj", "### [The Long Count: Her Log](s01_scan)", 6))),
    "s06_the_climax": _sc(5,
        _b(0, "e_clim", _ln("e_clim", "### [The Wren](the_wren)", 5)),
        _b(2, "e_clim", _txa("e_clim", "### [The Wren](the_wren)", "Guards: torgoth")),
        _b(4, "e_obj", _tx("e_obj", "Done when: scan 1 derelict")),
        _b(6, "e_clim", _txa("e_clim", "### [The Wren](the_wren)", "Guards: torgoth"))),
    "s07_the_hook": _sc(6,
        _b(0, "e_home", _ln("e_home", "### [The Long Count: Enter It](s01_home)", 7)),
        _b(1, "e_home", _txa("e_home", "### [The Long Count: Enter It](s01_home)", "Done when: reach 0, 0")),
        _b(2, "e_home", _txa("e_home", "### [The Long Count: Enter It](s01_home)", "Reward: 300 credits")),
        _b(5, "e_home", _txa("e_home", "### [The Long Count: Enter It](s01_home)", "Then: reveal s02_go")),
        _b(6, "e_two", _ln("e_two", "The Wren's log gives the next boat's last bearing", 3)),
        _b(9, "e_two"),
        _b(10, "e_two", _ln("e_two", "## The count so far", 5)),
        _b(13, "e_two", _ln("e_two", "| Boat | Where", 3)),
        _b(14, "e_two", _tx("e_two", "## The count so far", "## The count so far"))),
    "s08_lint_and_play": _sc(8,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(1, "card_play"),
        _b(2, "card_play", ("part", "item1")),
        _b(3, "card_play", ("part", "item2")),
        _b(4, "game_c63_wren"),
        _b(5, "card_play", ("part", "item4")),
        _b(6, "card_play", ("part", "item5")),
        _b(8, "game_c63_end"),
        _b(10, "card_play", ("part", "item7"))),
    "s09_close": _sc(8,
        _b(0, "card_facts"),
        _b(1, "card_facts", ("part", "r1")),
        _b(2, "card_facts", ("part", "r2")),
        _b(4, "card_next")),
}
