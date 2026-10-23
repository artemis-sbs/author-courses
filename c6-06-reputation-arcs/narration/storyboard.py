"""Storyboard for c6-06-reputation-arcs: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 5 storyboards. Caption numbers are those of shots.py. The helpers below only build
the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 5 left it (kestrel_verge.amd and campaign.md =
c6-05's example). The steps are typed in the video's order, each state one step on the one
before: Step 3, the lead The Tern's Manifest in Narrative ("s_lead"), the Ask answer in Hollin
Hail ("s_answer"), The Manifest record ("s_rec"); Step 4, the Sell answer in Gleaner Hail and
the Sold record ("s_sold", the page's own kestrel_verge.amd); Step 5, the standing ledger in
campaign.md ("final", the page's own example for both files).

NOT SHOWN AS WRITTEN: the page's Step 1 and Step 4 tables and the "Why 40" paragraph and the
bold sentence on prize and price are cards from the page; the paragraph and the sentence are
drawn as a short list in the board's own words. How an answer that is not offered looks in the
engine (absent or greyed) is not known: the game stills are taken, never described here.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine
for them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on
the sandbox probe:
`python game.py c6-06-reputation-arcs start --state final --consoles server,helm,comms`
Marks are left off every game still until the stills exist. Press order (Step 7 of the page):
  1. Comms, select the Hollin Compact's station, Hail: game_c66_hail3 (three answers, no
     Ask to see the Tern's manifest).
  2. Pay the relay levy twice (200 credits, standing 40). Hail again: game_c66_hail4 (the
     fourth answer is there).
  3. Press Ask to see the Tern's manifest. Helm, Quest Log: game_c66_asked (The Tern's
     Manifest done, 200 credits paid).
  4. Quest Log, engage The Breaking Yard. Comms, the Gleaners' station, Hail The Gleaners,
     Sell them a copy of the Count: game_c66_sold (their answer, and nothing about the cost).
  5. Engage Kestrel Relay. Comms, select the Hollin station: game_c66_home (no Patrol on its
     list, Escort at 292). Hail: game_c66_cold (the cold greeting, three answers again).
Never caption a face or a clock time.
"""
import os
import re

LECTURE = "c6-06-reputation-arcs"
TITLE = ("Class 6, Lecture 6", "Reputation arcs", "A door that trust opens, and a way to slam it")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
CAMP = "campaign.md"
_EX = "c6-06-reputation-arcs/example"
_PREV = "c6-05-campaign-architecture/example"
_MORE = ("c6-05-campaign-architecture/example",)


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

_il = _FA.index("### [The Tern's Manifest](door_manifest)")
_LEAD = _FA[_il:_nx(_FA, _il) + 1]
_ANS = "- [Ask to see the Tern's manifest](hollin_manifest) if standing >= 40 ; signal manifest_seen\n"
_GL = "- [Sell them a copy of the Count](gleaner_sold) ; earns gleaners resourceful 35, earns hollin liar 40\n"
_im = _FA.index("### [The Manifest](hollin_manifest)")
_is = _FA.index("### [Sold](gleaner_sold)")
_T_REC = (_FA[:_is].rstrip("\n") + "\n").replace(_GL, "")
_T_ANS = _T_REC[:_T_REC.index("\n### [The Manifest](hollin_manifest)")] + "\n"
_T_ANS = _T_ANS.rstrip("\n") + "\n"
_T_LEAD = _T_ANS.replace(_ANS, "")
assert _T_LEAD.replace(_LEAD, "") == _TEXT["start"][FILE], "the base of the amd"

_ic = _FC.index("\n## Standing ledger - Act One")
assert _FC[:_ic] == _TEXT["start"][CAMP], "the base of campaign.md"

_chain("start", [
    ("s_lead", {FILE: _T_LEAD}),
    ("s_answer", {FILE: _T_ANS}),
    ("s_rec", {FILE: _T_REC}),
    ("s_sold", {FILE: _FA}),
    ("final", {CAMP: _FC}),
])
_same("s_sold", FILE)
_same("final", FILE, CAMP)

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_lead", "s_lead", "### [The Tern's Manifest](door_manifest)", off=8)
_E("e_answer", "s_answer", _ANS.rstrip("\n"), off=0)
_E("e_rec", "s_rec", "### [The Manifest](hollin_manifest)", off=4)
_E("e_gl", "s_sold", _GL.rstrip("\n"), off=1)
_E("e_sold", "s_sold", "### [Sold](gleaner_sold)", off=3)
_E("e_ledger", "final", "## Standing ledger - Act One", off=8, file=CAMP)
_E("e_ledger_a", "final", "What I expect, if the crew takes", off=3, file=CAMP)
_term("t_lint", "final")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c66_hail3", "Comms with the Hollin Compact selected, Hail Hollin Compact pressed: the cold greeting and three answers, no Ask to see the Tern's manifest")
_game("game_c66_hail4", "Comms after two levies, hailing again: four answers, the fourth Ask to see the Tern's manifest")
_game("game_c66_asked", "Helm, Quest Log: The Tern's Manifest done, 200 credits paid")
_game("game_c66_sold", "Comms at the Gleaners' home after Sell them a copy of the Count: their answer on the screen, nothing about what it cost")
_game("game_c66_home", "Comms at Kestrel Relay with the Hollin station selected: Patrol gone from its list, Escort now at 292")
_game("game_c66_cold", "Comms hailing the Hollin Compact again: the cold greeting and three answers")

# drawn
_card("card_moves", "table", heading="Step 1 - What moves standing, over weeks", nth=1, kicker="What moves standing, measured")
_card("card_prize", "points", kicker="An arc has two tools", items=[
    "A prize is a deed on a step. It is given once, on the evening you choose.",
    "Jobs can be taken again, and answers can be given again.",
    "So on those you put a price, in credits or in time.",
    "You decide how much of each an evening pays."])
_card("card_why40", "points", kicker="Why 40, and not 20 or 60", items=[
    "At 20 the door opens after one levy, on evening 1, and is not a door.",
    "At 60 it needs three levies or twelve jobs, and a crew may never get there.",
    "At 40 it is two levies, or eight tier 1 jobs, or a mix.",
    "A crew that takes one job a week and pays the levy once arrives in the fourth week."])
_card("card_before", "table", heading="Step 4 - A door that closes", nth=1, kicker="One conversation, three things at home")
_card("card_arc", "table", heading="Step 7 - Play it", nth=1, kicker="What you need to know about an arc")
_card("card_next", "title", kicker="Next", title="Lecture 7", sub="Mixing the play styles")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c66_hail4"),
        _b(4, "game_c66_hail4"),
        _b(5, "game_c66_cold")),
    "s02_what_moves_it": _sc(1,
        _b(0, "card_moves"),
        _b(2, "card_moves", ("part", "r1"), ("part", "r2")),
        _b(3, "card_moves", ("part", "r1"), ("part", "r2")),
        _b(4, "card_moves", ("part", "r3")),
        _b(5, "card_moves", ("part", "r3")),
        _b(6, "card_moves", ("part", "r5")),
        _b(7, "card_moves", ("part", "r5")),
        _b(8, "card_moves", ("part", "r5")),
        _b(10, "card_moves", ("part", "r5"))),
    "s03_a_prize_and_a_price": _sc(1,
        _b(0, "card_prize"),
        _b(1, "card_prize", ("part", "item1")),
        _b(3, "card_prize", ("part", "item2")),
        _b(6, "card_prize", ("part", "item3")),
        _b(8, "card_prize", ("part", "item4"))),
    "s04_a_door_that_opens": _sc(3,
        _b(0, "e_lead", _ln("e_lead", "Scope: shared\nStarts when: at once\nDone when: signal manifest_seen", 13)),
        _b(1, "e_lead", _tx("e_lead", "Starts when: at once\nDone when: signal manifest_seen", "Starts when: at once")),
        _b(2, "e_lead", _tx("e_lead", "The Compact keeps the Tern's manifest under seal", "Earn their trust at Kestrel Relay, then ask.")),
        _b(5, "e_lead", _tx("e_lead", "## What the Compact trusts")),
        _b(6, "e_lead", _ln("e_lead", "- ![](icon://handshake)", 3)),
        _b(7, "e_lead", _tx("e_lead", "- ![](icon://handshake)", "- "), _tx("e_lead", "- ![](icon://flag)", "- "), _tx("e_lead", "- ![](icon://ban)", "- ")),
        _b(8, "e_lead", _tx("e_lead", "- ![](icon://handshake)", "![](icon://handshake)")),
        _b(9, "e_lead", _tx("e_lead", "- ![](icon://handshake)", "A ship that pays the relay levy")),
        _b(10, "e_lead", _tx("e_lead", "- ![](icon://flag)", "A ship that flies their patrols and escorts")),
        _b(11, "e_lead", _tx("e_lead", "- ![](icon://ban)", "Not a ship that trades with the Gleaners")),
        _b(12, "e_answer", _tx("e_answer", "- [Ask to see the Tern's manifest]", "- [Ask to see the Tern's manifest](hollin_manifest)")),
        _b(13, "e_answer", _tx("e_answer", "- [Ask to see the Tern's manifest]", "if standing >= 40")),
        _b(14, "e_answer", _tx("e_answer", "- [Ask to see the Tern's manifest]", "if standing >= 40")),
        _b(15, "e_rec", _ln("e_rec", "### [The Manifest](hollin_manifest)", 5)),
        _b(16, "e_rec", _tx("e_rec", "% Seal broken, and witnessed.", "Seal broken, and witnessed."))),
    "s05_why_forty": _sc(3,
        _b(0, "card_why40"),
        _b(1, "card_why40", ("part", "item1")),
        _b(3, "card_why40", ("part", "item2")),
        _b(4, "card_why40", ("part", "item3")),
        _b(6, "card_why40", ("part", "item4")),
        _b(9, "card_why40")),
    "s06_a_door_that_closes": _sc(4,
        _b(0, "e_gl"),
        _b(2, "e_gl", _tx("e_gl", "- [Sell them a copy of the Count]", "- [Sell them a copy of the Count](gleaner_sold)")),
        _b(4, "e_gl", _tx("e_gl", "- [Sell them a copy of the Count]", "earns gleaners resourceful 35")),
        _b(5, "e_gl", _tx("e_gl", "- [Sell them a copy of the Count]", "earns hollin liar 40")),
        _b(6, "e_sold", _ln("e_sold", "### [Sold](gleaner_sold)", 5)),
        _b(7, "card_before"),
        _b(8, "card_before", ("part", "r1")),
        _b(9, "card_before", ("part", "r3"), ("part", "r4"), ("part", "r5")),
        _b(10, "card_before", ("part", "r3"), ("part", "r4"), ("part", "r5"))),
    "s07_the_ledger": _sc(5,
        _b(0, "e_ledger"),
        _b(1, "e_ledger", _ln("e_ledger", "| 1 | 5 | 0 | 0 |", 5)),
        _b(2, "e_ledger", _tx("e_ledger", "| End of evening |", "Hollin | Deepwell | Gleaners")),
        _b(3, "e_ledger", _tx("e_ledger", "| End of evening |", "A door I expect to open or close")),
        _b(4, "e_ledger_a", _tx("e_ledger_a", "What I expect, if the crew takes", "What I expect, if the crew takes one Hollin job a week and pays the levy when they can.")),
        _b(5, "e_ledger", _tx("e_ledger", "| 2 | 30 |", "Hollin tier 2 jobs"), _tx("e_ledger", "| 3 | 35 |", "Deepwell tier 2 jobs"), _tx("e_ledger", "| 4 | 45 |", "The Tern's manifest")),
        _b(6, "e_ledger", _tx("e_ledger", "| 4 | 45 |", "The Tern's manifest")),
        _b(7, "e_ledger", _tx("e_ledger", "Prices I have set:", "Prices I have set: the levy, 100 credits for +20.")),
        _b(8, "e_ledger", _tx("e_ledger", "Prices I have set:", "Wages: 300, 350, then 300 an evening.")),
        _b(10, "e_ledger")),
    "s08_lint_and_play": _sc(7,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(1, "game_c66_hail3"),
        _b(3, "game_c66_hail4"),
        _b(4, "game_c66_asked"),
        _b(6, "game_c66_sold"),
        _b(8, "game_c66_home"),
        _b(9, "game_c66_cold")),
    "s09_close": _sc(7,
        _b(0, "card_arc", ("part", "r1")),
        _b(2, "card_arc", ("part", "r2")),
        _b(3, "card_arc", ("part", "r6")),
        _b(5, "card_next")),
}
