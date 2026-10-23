"""Storyboard for c6-05-campaign-architecture: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 5 storyboards. Caption numbers are those of shots.py. The helpers below only build
the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 4 left it (kestrel_verge.amd and campaign.md =
c6-04's example). The steps are typed in the video's order, each state one step on the one
before: Step 1, the four acts in campaign.md ("c_acts"); Step 2, the Act One table ("c_act1");
Step 3, the Then line on Three of Five ("s_then"), The Petrel with Four of Five and Five of Five
("s_stubs"), Five Boats ("s_ending"); Step 5, the budget table ("final", the page's own example
for both files).

NOT SHOWN AS WRITTEN: the page's tables inside code blocks (the four acts, Act One, the budget)
are shown as the editor's text in campaign.md; the page's other tables are cards from the page.
The bible page in a browser (scene 7) is shown as the command and then the page's own table of
what it says, as cards: nobody has run it in a browser.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine
for them from this file: Open Universe rewrites the player's save. ONE game, TWO windows, on the
sandbox probe:
`python game.py c6-05-campaign-architecture start --state final --consoles server,helm`
Marks are left off every game still until the stills exist. Press order (Step 7 of the page):
  1. Play evenings 1 and 2 as fast as possible. Engage Three of Five, arrive at (3, 1), Helm,
     Quest Log: game_c65_four (Four of Five in the list at once).
  2. Engage Four of Five, arrive at (4, -2): game_c65_petrel (the card reading The Petrel).
  3. Engage Five of Five, then Five Boats, arrive home. Quest Log: game_c65_done (every line of
     The Long Count under Done, The Second Colony and The Breaking Yard among them).
Never caption a face or a clock time.
"""
import os
import re

LECTURE = "c6-05-campaign-architecture"
TITLE = ("Class 6, Lecture 5", "Campaign architecture", "Twenty evenings on one page, and the first act walked")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
CAMP = "campaign.md"
_EX = "c6-05-campaign-architecture/example"

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


STATES["start"] = {"folder": "c5-02-your-universe-file/example", "over": _PRIOR}
_TEXT["start"] = {FILE: _read("c6-04-the-episode/example/" + FILE), CAMP: _read("c6-04-the-episode/example/" + CAMP)}

_FA = _read(_EX + "/" + FILE)
_FC = _read(_EX + "/" + CAMP)
_THEN = "Then: reveal s04_go\n"
_ip = _FA.index("### [The Petrel](the_petrel)")
_nx = lambda t, i: re.compile(r"\n#{2,3} \[").search(t, i).start()
_PET = _FA[_ip:_nx(_FA, _ip) + 1]
_I4 = _FA.index("\n### [The Long Count: Four of Five](s04_go)")
_IB = _FA.index("\n### [The Long Count: Five Boats](act1_close)")
_IE = _nx(_FA, _IB + 5)
_S_THEN = (_FA[:_I4] + _FA[_IE:]).replace(_PET, "")
assert _S_THEN.replace(_THEN, "") == _TEXT["start"][FILE], "the base of the amd"
_S_STUBS = _FA[:_IB] + _FA[_IE:]

_ia, _il, _ib = _FC.index("\n## The four acts"), _FC.index("\n## Act One - Five Boats"), _FC.index("\n## Budget")
assert _FC[:_ia] == _TEXT["start"][CAMP], "the base of campaign.md"

_chain("start", [
    ("c_acts", {CAMP: _FC[:_il]}),
    ("c_act1", {CAMP: _FC[:_ib]}),
    ("s_then", {FILE: _S_THEN}),
    ("s_stubs", {FILE: _S_STUBS}),
    ("s_ending", {FILE: _FA}),
    ("final", {CAMP: _FC}),
])
_same("final", FILE, CAMP)

_END = "Done when: reach 0, 0\nReward: 1000 credits"
_BOATS = "Scope: shared\nStarts when: revealed\nDone when: reach 0, 0"

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_acts_f", "final", "| 1. Five Boats |", off=2, file=CAMP)
_E("e_budget_f", "final", "| One evening takes me |", off=-2, file=CAMP)
_E("e_acts", "c_acts", "| 1. Five Boats |", off=2, file=CAMP)
_E("e_act1", "c_act1", "| End | Five Boats |", off=-2, file=CAMP)
_E("e_then", "s_then", "Then: reveal s04_go", off=4)
_E("e_four", "s_stubs", "### [The Long Count: Four of Five](s04_go)", off=6)
_E("e_stubs", "s_stubs", "### [The Long Count: Five of Five](s05_go)", off=1)
_E("e_boats", "s_ending", "![](face://ter", off=4)
_E("e_boats_p", "s_ending", "Five boats, and not one body", off=8)
_E("e_budget", "final", "| One evening takes me |", off=-2, file=CAMP)
_term("t_lint", "final")
_term("t_bible", "final", "sbs docs MyUniverse --lens bible")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c65_four", "Helm, Quest Log: Three of Five just finished at the Assay Office, Four of Five in the list at once")
_game("game_c65_petrel", "Helm on arrival at (4, -2): the card reading The Petrel, and Five of Five in the list")
_game("game_c65_done", "Helm, Quest Log after Five Boats: every line of The Long Count under Done, the Class 5 leads finished too, and no new lead")

# drawn
_card("card_win", "table", heading="Step 4 - Where the ending goes", nth=1, kicker="What a Win line does to a campaign")
_card("card_bible", "table", heading="Step 5 - The budget", nth=1, kicker="The shape of it")
_card("card_evening", "table", heading="Step 5 - The budget", nth=2, kicker="One ordinary evening")
_card("card_long", "table", heading="Step 5 - The budget", nth=3, kicker="The Long Count")
_card("card_free", "table", heading="Step 5 - The budget", nth=4, kicker="Used once, and there every week")
_card("card_check", "points", kicker="Four acts, one of them walked", items=[
    "campaign.md has four acts, Act One evening by evening, and a budget with your own minutes in it.",
    "sbs lint MyUniverse says clean.",
    "Act One can be walked from its first lead to its ending without a gap.",
    "There is no Win: on any step of Act One.",
    "You can say how many records your campaign needs, and how many you have."])
_card("card_next", "title", kicker="Next", title="Lecture 6", sub="Reputation arcs")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "e_acts_f"),
        _b(2, "e_acts_f", _ln("e_acts_f", "| Act | Evenings |", 6)),
        _b(4, "e_budget_f", _ln("e_budget_f", "## Budget", 10))),
    "s02_acts": _sc(1,
        _b(0, "e_acts"),
        _b(2, "e_acts", _ln("e_acts", "| Act | Evenings |", 6)),
        _b(3, "e_acts", _tx("e_acts", "| 1. Five Boats |", "1 to 5")),
        _b(4, "e_acts", _tx("e_acts", "| 1. Five Boats |", "What happened to the Tern's boats?")),
        _b(5, "e_acts", _tx("e_acts", "| 2. The Buyers |", "Who took forty-one people off five boats?")),
        _b(6, "e_acts", _tx("e_acts", "| 3. The Breakers |", "Where were they taken?")),
        _b(7, "e_acts", _tx("e_acts", "| 4. The Fourth Colony |", "Are they still there, and do they want to be found?")),
        _b(8, "e_acts", _tx("e_acts", "| 1. Five Boats |", "Nobody died in them"), _tx("e_acts", "| 2. The Buyers |", "Who took forty-one people off five boats?")),
        _b(9, "e_acts", _ln("e_acts", "| 4. The Fourth Colony |", 1)),
        _b(10, "e_acts", _tx("e_acts", "| 4. The Fourth Colony |", "The count is closed"))),
    "s03_act_one_as_a_table": _sc(2,
        _b(0, "e_act1", _ln("e_act1", "| Evening | Title |", 8)),
        _b(1, "e_act1", _tx("e_act1", "| 1 | One of Five |", "The Wren, (2, 2)"), _tx("e_act1", "| 2 | Two of Five |", "The Dunlin, (-2, 3)"),
           _tx("e_act1", "| 3 | Three of Five |", "Assay Office, (3, 1)"), _tx("e_act1", "| 4 | Four of Five |", "The Petrel, (4, -2)"),
           _tx("e_act1", "| 5 | Five of Five |", "The Gleaners' yard, (-3, -2)"), _tx("e_act1", "| End | Five Boats |", "Kestrel Relay, (0, 0)")),
        _b(2, "e_act1", _tx("e_act1", "| 3 | Three of Five |", "Assay Office, (3, 1)"), _tx("e_act1", "| 5 | Five of Five |", "The Gleaners' yard, (-3, -2)")),
        _b(3, "e_act1"),
        _b(4, "e_act1", _tx("e_act1", "| 1 | One of Five |", "The Wren, (2, 2)"), _tx("e_act1", "| 4 | Four of Five |", "The Petrel, (4, -2)")),
        _b(6, "e_act1", _tx("e_act1", "| 3 | Three of Five |", "Assay Office, (3, 1)"), _tx("e_act1", "| 5 | Five of Five |", "The Gleaners' yard, (-3, -2)"))),
    "s04_stubs": _sc(3,
        _b(0, "e_then"),
        _b(1, "e_then", _tx("e_then", "Then: reveal s04_go")),
        _b(2, "e_four", _ln("e_four", "### [The Long Count: Four of Five](s04_go)", 9)),
        _b(3, "e_four", _tx("e_four", "Then: reveal s05_go")),
        _b(4, "e_stubs", _tx("e_stubs", "Then: reveal s05_go"), _tx("e_stubs", "Done when: reach -3, -2\nThen: reveal act1_close", "Done when: reach -3, -2")),
        _b(5, "e_then", _tx("e_then", "Then: reveal s04_go")),
        _b(6, "e_four", _ln("e_four", "### [The Long Count: Four of Five](s04_go)", 9)),
        _b(7, "e_four", _tx("e_four", "The Assay Office sold the Plover on", "The Assay Office sold the Plover on")),
        _b(8, "e_four", _tx("e_four", "Done when: reach 4, -2"))),
    "s05_the_act_s_ending": _sc(3,
        _b(0, "e_boats", _tx("e_boats", "Reward: 1000 credits")),
        _b(1, "e_boats", _tx("e_boats", "Five boats, and not one body", "Five boats, and not one body.")),
        _b(2, "e_boats", _ln("e_boats", "![](face://ter", 11)),
        _b(3, "e_boats", _tx("e_boats", "![](face://ter", "![](face://")),
        _b(4, "e_boats", _tx("e_boats", "![](face://ter", "Registrar Amsel, who keeps the Count at Kestrel Relay")),
        _b(5, "e_boats", _tx("e_boats", "![](face://ter", "face://ter #9c7056 0 0;ter #fff 13 6;ter #9c7056 1 1;ter #9c7056 11 2;ter #704025 20 3;")),
        _b(6, "e_boats", _tx("e_boats", "![](face://ter", "ter #704025 20 3;")),
        _b(8, "e_boats", _tx("e_boats", "Five boats, and not one body", "Five boats, and not one body.")),
        _b(9, "e_boats_p", _ln("e_boats_p", "| Boat | Where | What we know |", 7, nth=3)),
        _b(10, "e_boats", _ln("e_boats", _END, 2)),
        _b(14, "e_boats")),
    "s06_where_the_ending_goes": _sc(4,
        _b(0, "card_win"),
        _b(1, "card_win", ("part", "r1")),
        _b(2, "card_win", ("part", "r2")),
        _b(4, "card_win", ("part", "r3")),
        _b(5, "card_win", ("part", "r4"))),
    "s07_the_budget": _sc(5,
        _b(0, "t_bible"),
        _b(1, "card_bible"),
        _b(2, "card_bible", ("part", "r1")),
        _b(3, "card_bible", ("part", "r3")),
        _b(4, "card_evening", ("part", "r1")),
        _b(5, "card_evening", ("part", "r3")),
        _b(6, "card_long", ("part", "r1"), ("part", "r2"), ("part", "r3")),
        _b(7, "card_long", ("part", "r4")),
        _b(8, "card_long", ("part", "r5")),
        _b(9, "e_budget", _tx("e_budget", "| One evening takes me |", "One evening takes me")),
        _b(10, "e_budget", _tx("e_budget", "| The campaign will take me |", "The campaign will take me"))),
    "s08_half_the_evening_is_free": _sc(5,
        _b(0, "card_free"),
        _b(1, "card_free", ("part", "head")),
        _b(2, "card_free", ("part", "r1c2")),
        _b(4, "card_free", ("part", "r2c2"), ("part", "r3c2")),
        _b(5, "card_free"),
        _b(6, "card_free", ("part", "r4c2"))),
    "s09_walk_it": _sc(7,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(2, "game_c65_four"),
        _b(3, "game_c65_petrel"),
        _b(4, "e_stubs", _tx("e_stubs", "Done when: reach -3, -2\nThen: reveal act1_close", "Done when: reach -3, -2")),
        _b(5, "e_boats", _tx("e_boats", _END, "Done when: reach 0, 0")),
        _b(6, "e_boats", _tx("e_boats", "Reward: 1000 credits")),
        _b(7, "game_c65_done")),
    "s10_close": _sc(None,
        _b(0, "card_check", ("part", "item1")),
        _b(1, "card_check", ("part", "item5")),
        _b(4, "card_next")),
}
