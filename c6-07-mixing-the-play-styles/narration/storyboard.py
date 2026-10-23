"""Storyboard for c6-07-mixing-the-play-styles: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 5 storyboards. Caption numbers are those of shots.py. The helpers below only build
the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 6 left it (kestrel_verge.amd and campaign.md =
c6-06's example). The steps are typed in the video's order, each state one step on the one
before: Step 2, the rotation in campaign.md ("c_rot", the page's own campaign.md); Step 3, Three
of Five's new Then line with The Plover's Price and Enter It Again ("s_talk1"), then the
Deepwell hail with its answers and records ("s_talk2"); Step 4, the Lamp Run job and `lamp_run`
on Hollin's Offers line ("final", the page's own example for both files).

NOT SHOWN AS WRITTEN: the page's tables (the styles, the clocks measured, the interlude) are
cards from the page. In The Plover's Price the briefing's `ship://` line is a picture of the
hull, not a 3D model; it is marked as a line of text. Scene 8 (an evening off the map) is the
page's table and nothing else: no other mission is started.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine
for them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on
the sandbox probe:
`python game.py c6-07-mixing-the-play-styles start --state final --consoles server,helm,comms`
Marks are left off every game still until the stills exist. Press order (Step 7 of the page):
  1. Comms, select the Hollin Compact's station: game_c67_nolamp (its list, no Lamp Run).
  2. Pay the relay levy once, select the station again: game_c67_lamp (Lamp Run on the list).
  3. Take Lamp Run, Helm, engage it, arrive at (2, 2): game_c67_done (the job done and paid).
  4. Engage Three of Five (3, 1). Comms, select the Assay Office, Hail: game_c67_ask (the two
     answers and Sign off). Press an answer. Helm, Quest Log: game_c67_open (The Plover's
     Price done, Enter It Again in the list).
Never caption a face or a clock time.
"""
import os
import re

LECTURE = "c6-07-mixing-the-play-styles"
TITLE = ("Class 6, Lecture 7", "Mixing the play styles", "Whose evening it is, and a race that cannot break the story")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
CAMP = "campaign.md"
_EX = "c6-07-mixing-the-play-styles/example"
_PREV = "c6-06-reputation-arcs/example"
_MORE = ("c6-05-campaign-architecture/example", "c6-06-reputation-arcs/example")


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
_FC = _read(_EX + "/" + CAMP)
_nx = lambda t, i: re.compile(r"\n#{2,3} \[").search(t, i).start()

# Step 4's pieces, taken out of the finished file
_il = _FA.index("### [Lamp Run](lamp_run)")
_LAMP = _FA[_il:_nx(_FA, _il) + 1]
_OFF = ("Offers: patrol, escort, lamp_run", "Offers: patrol, escort")
_NOLAMP = _FA.replace(_LAMP, "").replace(*_OFF)
# Step 3's pieces
_ih = _NOLAMP.index("### [Deepwell Hail](deepwell_hail)")
_jh = _NOLAMP.index("% Assay Office out.\n") + len("% Assay Office out.\n")
_T_TALK1 = _NOLAMP[:_ih - 1] + _NOLAMP[_jh:]
_i3, _i4 = _T_TALK1.index("### [The Long Count: The Plover's Price](s03_ask)"), _T_TALK1.index("### [The Long Count: Four of Five](s04_go)")
assert (_T_TALK1[:_i3] + _T_TALK1[_i4:]).replace("Then: reveal s03_ask", "Then: reveal s04_go") == _TEXT["start"][FILE], "the base of the amd"

_ic = _FC.index("\n## Rotation - Act One")
assert _FC[:_ic] == _TEXT["start"][CAMP], "the base of campaign.md"

_chain("start", [
    ("c_rot", {CAMP: _FC}),
    ("s_talk1", {FILE: _T_TALK1}),
    ("s_talk2", {FILE: _NOLAMP}),
    ("final", {FILE: _FA}),
])
_same("final", FILE, CAMP)

_ANS1 = "- [Pay the search fee for the Plover's bill of sale]"
_ANS2 = "- [Tell the clerk the Compact will hear of a refusal]"

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_rot", "c_rot", "| 1 | One of Five | Search", off=2, file=CAMP)
_E("e_ledger", "final", "| 2 | 30 |", off=0, file=CAMP)
_E("e_then3", "s_talk1", "Then: reveal s03_ask", off=2)
_E("e_ask", "s_talk1", "### [The Long Count: The Plover's Price](s03_ask)", off=6)
_E("e_hail", "s_talk2", _ANS1, off=0)
_E("e_greet", "s_talk2", "%{standing >= 20} Assay Office", off=0)
_E("e_lamp", "final", "### [Lamp Run](lamp_run)", off=7)
_E("e_offers", "final", "Offers: patrol, escort, lamp_run", off=0)
_term("t_lint", "final")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c67_nolamp", "Comms with the Hollin Compact selected, standing 0: its list of jobs with no Lamp Run on it")
_game("game_c67_lamp", "Comms with the Hollin Compact selected after one levy: Lamp Run on the list with its price")
_game("game_c67_done", "Helm on arrival at (2, 2): Lamp Run done and paid")
_game("game_c67_ask", "Comms with the Assay Office selected, hailed: the two ways to ask, and Sign off")
_game("game_c67_open", "Helm, Quest Log: The Plover's Price done, Enter It Again newly in the list")

# drawn
_card("card_styles", "table", heading="Step 1 - What a style is", nth=1, kicker="The styles you can build today")
_card("card_later", "table", heading="Step 1 - What a style is", nth=2, kicker="The styles that wait for a lecture")
_card("card_clock", "table", heading="Step 4 - A race, and where clocks go", nth=1, kicker="A clock on the spine, measured")
_card("card_inter", "table", heading="Step 5 - An evening off the map", nth=1, kicker="An interlude is another save")
_card("card_check", "points", kicker="Every evening has an owner", items=[
    "campaign.md has a rotation for Act One with no style twice running.",
    "sbs lint MyUniverse says clean.",
    "One evening's objective is finished by an answer in a hail, and there are two answers.",
    "A job with a clock is offered only to a trusted crew.",
    "No step with Fails when: has a Then: line."])
_card("card_next", "title", kicker="Next", title="Lecture 8", sub="Playtesting")

_SC = lambda n: ("text", _L("c_rot", "| %s |" % n, 1, CAMP), "")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Science")),
        _b(1, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Science")),
        _b(2, "e_rot", _tx("e_rot", "| 2 | Two of Five | Fight", "Weapons, Engineering")),
        _b(3, "e_rot", _ln("e_rot", "| 3 | Three of Five | Talk", 3)),
        _b(5, "e_rot", _ln("e_rot", "| Evening | Title | Style", 8)),
        _b(6, "e_rot", _tx("e_rot", "| 3 | Three of Five | Talk", "Talk"), _tx("e_rot", "| 4 | Four of Five | Race", "Race"))),
    "s02_what_a_style_is": _sc(1,
        _b(0, "card_styles"),
        _b(1, "card_styles", ("part", "r1c3"), ("part", "r2c3"), ("part", "r3c3"), ("part", "r4c3"), ("part", "r5c3"), ("part", "r6c3")),
        _b(2, "card_styles", ("part", "r1")),
        _b(3, "card_styles", ("part", "r2")),
        _b(4, "card_styles", ("part", "r3")),
        _b(5, "card_styles", ("part", "r4")),
        _b(6, "card_styles", ("part", "r5")),
        _b(7, "card_styles", ("part", "r6")),
        _b(8, "card_styles")),
    "s03_styles_for_later": _sc(1,
        _b(0, "card_later"),
        _b(1, "card_later", ("part", "r1"), ("part", "r2"), ("part", "r3")),
        _b(2, "card_later", ("part", "r4")),
        _b(3, "card_later", ("part", "r1c3"), ("part", "r2c3"), ("part", "r3c3"), ("part", "r4c3")),
        _b(5, "card_later"),
        _b(6, "card_later")),
    "s04_the_rotation": _sc(2,
        _b(0, "e_rot"),
        _b(1, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Search, with a fight they can refuse"), _tx("e_rot", "| 2 | Two of Five | Fight", "Fight"),
           _tx("e_rot", "| 3 | Three of Five | Talk", "Talk"), _tx("e_rot", "| 4 | Four of Five | Race", "Race"), _tx("e_rot", "| 5 | Five of Five | Politics", "Politics")),
        _b(2, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Science"), _tx("e_rot", "| 2 | Two of Five | Fight", "Weapons, Engineering"),
           _tx("e_rot", "| 3 | Three of Five | Talk", "Comms"), _tx("e_rot", "| 4 | Four of Five | Race", "Helm"), _tx("e_rot", "| 5 | Five of Five | Politics", "Comms, the captain")),
        _b(3, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Search, with a fight they can refuse"), _tx("e_rot", "| 5 | Five of Five | Politics", "Comms, the captain")),
        _b(4, "e_rot", _tx("e_rot", "| Evening | Title | Style", "On offer beside it")),
        _b(5, "e_rot", _tx("e_rot", "| 1 | One of Five | Search", "Escort, the levy"), _tx("e_rot", "| 3 | Three of Five | Talk", "The Deepwell's work"), _tx("e_rot", "| 5 | Five of Five | Politics", "A ceasefire with the Gleaners")),
        _b(6, "e_rot", _ln("e_rot", "| 1 | One of Five | Search", 6)),
        _b(7, "e_rot", _ln("e_rot", "| 1 | One of Five | Search", 6))),
    "s05_a_talk_evening": _sc(3,
        _b(0, "e_then3", _tx("e_then3", "Then: reveal s03_ask")),
        _b(2, "e_ask", _tx("e_ask", "Done when: signal plover_asked")),
        _b(3, "e_hail", _tx("e_hail", _ANS1, "signal plover_asked")),
        _b(4, "e_ask", _ln("e_ask", "### [The Long Count: The Plover's Price](s03_ask)", 13)),
        _b(5, "e_ask", _tx("e_ask", "[](ship://starbase_industry)", "[](ship://starbase_industry)")),
        _b(6, "e_ask", _tx("e_ask", "How you ask is up to you", "How you ask is up to you, and they will remember it.")),
        _b(7, "e_hail", _tx("e_hail", _ANS1, "Pay the search fee for the Plover's bill of sale"), _tx("e_hail", _ANS2, "Tell the clerk the Compact will hear of a refusal")),
        _b(8, "e_hail", _tx("e_hail", _ANS1, "costs 150 credits")),
        _b(9, "e_hail", _tx("e_hail", _ANS2, "Tell the clerk the Compact will hear of a refusal")),
        _b(10, "e_hail", _tx("e_hail", _ANS1, "signal plover_asked"), _tx("e_hail", _ANS2, "signal plover_asked")),
        _b(12, "e_hail", _tx("e_hail", _ANS1, "earns deepwell by-the-book 20"), _tx("e_hail", _ANS2, "earns deepwell violent 20")),
        _b(14, "e_hail", _ln("e_hail", _ANS1, 3)),
        _b(15, "e_hail", _ln("e_hail", _ANS1, 2)),
        _b(17, "e_greet", _ln("e_greet", "%{standing >= 20} Assay Office", 2))),
    "s06_where_clocks_go": _sc(4,
        _b(0, "card_clock"),
        _b(3, "card_clock", ("part", "r1")),
        _b(5, "card_clock", ("part", "r2")),
        _b(6, "card_clock", ("part", "r3")),
        _b(7, "card_clock", ("part", "r1")),
        _b(8, "card_clock", ("part", "r3"))),
    "s07_a_race_that_s_safe": _sc(4,
        _b(0, "e_lamp", _tx("e_lamp", "Fails when: 10 minutes")),
        _b(1, "e_lamp", _tx("e_lamp", "Penalty: 100 credits")),
        _b(3, "e_lamp", _tx("e_lamp", "Done when: reach 2, 2")),
        _b(5, "e_lamp", _tx("e_lamp", "Tier: 2\nDone when: reach 2, 2", "Tier: 2")),
        _b(6, "e_offers", _tx("e_offers", "Offers: patrol, escort, lamp_run", "lamp_run")),
        _b(7, "e_ledger", _tx("e_ledger", "| 2 | 30 |", "Hollin tier 2 jobs")),
        _b(8, "e_lamp", _ln("e_lamp", "The marker lamp out by the Wren", 1)),
        _b(10, "e_lamp", _tx("e_lamp", "![](icon://hourglass)", "![](icon://hourglass)"))),
    "s08_an_evening_off_the_map": _sc(5,
        _b(0, "card_inter"),
        _b(3, "card_inter", ("part", "r1c1")),
        _b(5, "card_inter", ("part", "r1c2")),
        _b(7, "card_inter", ("part", "r3c1")),
        _b(8, "card_inter", ("part", "r3c2"))),
    "s09_lint_and_play": _sc(7,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(1, "game_c67_nolamp"),
        _b(3, "game_c67_lamp"),
        _b(5, "game_c67_done"),
        _b(7, "game_c67_ask"),
        _b(9, "game_c67_open")),
    "s10_close": _sc(7,
        _b(0, "card_check", ("part", "item1")),
        _b(2, "card_check", ("part", "item5")),
        _b(3, "card_check", ("part", "item3")),
        _b(4, "card_next")),
}
