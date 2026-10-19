"""Storyboard for c5-03-sides-diplomacy-goods: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py.

The lecture starts from Lecture 2's file: `MyUniverse` with c5-02's `kestrel_verge.amd`
("start", 84 lines; only that file is ever opened). The steps are typed in the video's order:
the template's two sides deleted ("empty"), Hollin Compact ("hollin"), the other two ("three"),
the Narrative chapter with its two leads ("leads"), then the Goods chapter between Landmarks
and Narrative ("goods", the page's own example, 138 lines). The text of every state is built
from the page's example by cutting it into the pieces the student types (see _H, _D, _G, _NARR,
_GOODS), so "goods" equals the example byte for byte.

Line numbers in the marks are worked out from each state's own text (ln()).

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine by the
person, NEVER by a script: an Open Universe run writes a save. ONE game, TWO windows:
`sbs run server,helm,comms -m MyUniverse map=0` on a probe copy of the example, with a new
game (the Lecture 2 save deleted). Marks are left off every game still until the stills are
taken. Never caption a face. Press order:
  1. Comms at once: select Hollin Compact (the station at home): game_c53_hollin (Patrol
     (200 cr) and Escort (250 cr) among its buttons). Then select Kestrel Relay:
     game_c53_relay (a market and no such jobs).
  2. Comms: Accept Cargo Run from either station: game_c53_cargo.
  3. Helm: the handheld icon, Quests: game_c53_quests (The Second Colony, The Breaking Yard
     and the cargo run in the list, Engage in view).
  4. Engage the cargo run (400 credits, 900 now). Engage The Second Colony. On arrival, Comms,
     the station Deepwell Assembly: game_c53_deepwell (Escort (250 cr) and no patrol).
  5. Engage The Breaking Yard. On arrival: game_c53_gleaners (the station The Gleaners, the
     Torgoth fleet standing by it).
  6. Comms, select the Gleaners' station: game_c53_ceasefire (Negotiate Ceasefire among its
     buttons). Press it: game_c53_peace (the war is off, 600 credits spent).
  7. Comms, the Gleaners' station again: game_c53_nowork (no jobs listed).
"""
import os

LECTURE = "c5-03-sides-diplomacy-goods"
TITLE = ("Class 5, Lecture 3", "Sides, diplomacy and goods", "Three factions, one of them a foe, and the cargo of your world")
MISSION = "MyUniverse"
FILE = "kestrel_verge.amd"

_EX2 = "c5-02-your-universe-file/example"
_EX = "c5-03-sides-diplomacy-goods/example"
_HERE = os.path.dirname(os.path.abspath(__file__))


def _read(*parts):
    with open(os.path.join(_HERE, "..", *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


_START = _read("..", "c5-02-your-universe-file", "example", "kestrel_verge.amd")
_FINAL = _read("example", "kestrel_verge.amd")

_I_IRON = _START.index("### [Iron Concord](iron)")
_I_JOBS = _START.index("// ---- Job types")
_OLD_SIDES = _START[_I_IRON:_I_JOBS]                                  # both template sides, and the blank lines after
_I_H, _I_D = _FINAL.index("### [Hollin Compact]"), _FINAL.index("### [Deepwell Assembly]")
_I_G, _I_J = _FINAL.index("### [The Gleaners]"), _FINAL.index("// ---- Job types")
_H = _FINAL[_I_H:_I_D].rstrip("\n")
_D = _FINAL[_I_D:_I_G].rstrip("\n")
_G = _FINAL[_I_G:_I_J].rstrip("\n")
_I_GOODS, _I_NARR = _FINAL.index("## [Goods](goods)"), _FINAL.index("## [Narrative](narrative)")
_GOODS = _FINAL[_I_GOODS:_I_NARR]
_NARR = _FINAL[_I_NARR:]

_T = {}
_T["start"] = _START
_T["empty"] = _START.replace(_OLD_SIDES, "")
_T["hollin"] = _T["empty"].replace("## [Sides](sides)\n\n// ----", "## [Sides](sides)\n\n" + _H + "\n\n\n// ----")
_T["three"] = _T["hollin"].replace(_H + "\n\n\n// ----", _H + "\n\n" + _D + "\n\n" + _G + "\n\n\n// ----")
_T["leads"] = _T["three"] + "\n" + _NARR
_T["goods"] = _T["leads"].replace("## [Narrative](narrative)", _GOODS + "## [Narrative](narrative)")


def ln(state, needle, nth=1):
    """The 1-based line of the nth line of a state's file holding needle."""
    seen = 0
    for i, line in enumerate(_T[state].split("\n"), 1):
        if needle in line:
            seen += 1
            if seen == nth:
                return i
    raise ValueError(f"{state}: {needle!r} is not in the file {nth} time(s)")


STATES = {
    "start": {"folder": _EX2},
    # Step 1: both template sides taken out
    "empty": {"base": "start", "edits": [("write", FILE, _T["empty"])]},
    # Step 2: Hollin Compact; Step 3: Deepwell Assembly and The Gleaners
    "hollin": {"base": "empty", "edits": [("write", FILE, _T["hollin"])]},
    "three": {"base": "hollin", "edits": [("write", FILE, _T["three"])]},
    # Step 4: the Narrative chapter with its two leads, at the end
    "leads": {"base": "three", "edits": [("write", FILE, _T["leads"])]},
    # Step 5: the Goods chapter, between Landmarks and Narrative. The page's own example.
    "goods": {"base": "leads", "edits": [("write", FILE, _T["goods"])], "same_as": (_EX + "/kestrel_verge.amd",)},
}
STATES["final"] = {"base": "goods"}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}

# where the marks are
_SIDES = ln("three", "## [Sides]")
_IRON, _ASH = ln("start", "### [Iron Concord]"), ln("start", "### [Ashfall Run]")
_HOST = ln("start", "Disposition: hostile")
_ASH_END = ln("start", "Salvagers who stopped waiting")
_HOL = ln("hollin", "### [Hollin Compact]")
_DW = ln("three", "### [Deepwell Assembly]")
_GL = ln("three", "### [The Gleaners]")
_NA = ln("leads", "## [Narrative]")
_L1, _L2 = ln("leads", "### [The Second Colony]"), ln("leads", "### [The Breaking Yard]")
_GO = ln("goods", "## [Goods]")
_ORE, _PRO, _TEC, _CON = (ln("goods", "### [Ore]"), ln("goods", "### [Provisions]"),
                          ln("goods", "### [Tech]"), ln("goods", "### [Contraband]"))
_N_END = ln("start", "rumor.")


def _w(state, head, key):
    """The line of a fact (key) inside the record that starts at head (a line number)."""
    for i, line in enumerate(_T[state].split("\n")[head - 1:], head):
        if line.startswith(key):
            return i
    raise ValueError(key)


STILLS = {
    # The editor. A still shows 21 lines: the one named, ten above and ten below
    "e_end0": ("vscode", "start", _N_END - 3, "big", _NS),          # the end of Lecture 2's file: the landmark
    "e_old": ("vscode", "start", _IRON + 10, "big", _NS),            # the template's two sides, Iron Concord and Ashfall Run
    "e_empty": ("vscode", "empty", _SIDES + 3, "big", _NS),         # the Sides heading with nothing under it
    "e_hollin": ("vscode", "hollin", _HOL + 5, "big", _NS),         # Hollin Compact, the first side
    "e_three": ("vscode", "three", (_DW + _GL) // 2 + 3, "big", _NS),   # Deepwell Assembly and The Gleaners
    "e_leads": ("vscode", "leads", _NA + 8, "big", _NS),            # the Narrative chapter: two leads
    "e_goods": ("vscode", "goods", _PRO + 2, "big", _NS),           # Goods: Ore, Provisions, Tech
    "e_goods_con": ("vscode", "goods", _CON + 2, "big", _NS),       # Goods: Contraband, then Narrative
    "e_final": ("vscode", "final", _GL + 4, "big", _NS),            # the finished sides
    # the command prompt
    "t_start": ("terminal", [("start", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME. Not taken yet (see the docstring). State goods, consoles server,helm,comms
    "game_c53_hollin": ("game", "Comms with the station Hollin Compact selected: Patrol (200 cr) and Escort (250 cr) among its buttons"),
    "game_c53_relay": ("game", "Comms with Kestrel Relay selected: a market, and no Patrol or Escort"),
    "game_c53_cargo": ("game", "Comms with a station selected: Accept Cargo Run among its buttons"),
    "game_c53_quests": ("game", "Helm's Quest Log: The Second Colony and The Breaking Yard beside the cargo run, Engage in view"),
    "game_c53_deepwell": ("game", "Comms at 3, 1 with the station Deepwell Assembly selected: Escort (250 cr) and no patrol"),
    "game_c53_gleaners": ("game", "Helm at -3, -2: the station The Gleaners and a fleet of Torgoth ships standing by it"),
    "game_c53_ceasefire": ("game", "Comms with the Gleaners' station selected: Negotiate Ceasefire among its buttons"),
    "game_c53_peace": ("game", "Comms just after Negotiate Ceasefire: the war is off, the 600 credits gone"),
    "game_c53_nowork": ("game", "Comms with the Gleaners' station selected after the ceasefire: no jobs among its buttons"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_disp": ("card", "table", {"heading": "Step 3 - Two more sides, and who shoots first", "nth": 1, "kicker": "Disposition has two words"}),
    "card_foe": ("card", "list", {"heading": "Step 3 - Two more sides, and who shoots first", "kicker": "A foe gets three things for free"}),
    "card_keys": ("card", "table", {"heading": "Step 5 - Goods", "nth": 1, "kicker": "The five goods the game knows"}),
    "card_eye": ("card", "points", {"kicker": "After lint, check these by eye", "items": [
        "Disposition: is neutral or foe, in small letters.",
        "Every Home: is two numbers, and no two sides share one.",
        "Every word after Offers: is the key of a record in the Jobs chapter.",
        "Every word after Flies: is one of the six.",
        "Every key in the Goods chapter is one of the five, and every Weight: is a number.",
        "The two numbers after reach are the two numbers of that side's Home:."]}),
    "card_cease": ("card", "table", {"heading": "Step 7 - Play it", "nth": 1, "kicker": "What you need to know about a ceasefire"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Make these three your own"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 4", "sub": "Reputation"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_end0"},
        {"from": 2, "still": "e_final"},
        {"from": 4, "still": "game_c53_hollin"},
        {"from": 5, "still": "game_c53_deepwell"},
        {"from": 6, "still": "game_c53_gleaners"},
        {"from": 7, "still": "e_three"},
        {"from": 8, "still": "card_title"},
    ]},
    "s02_out_with_the_old": {"step": 1, "beats": [
        {"from": 0, "still": "e_old", "marks": [("lines", _IRON, _ASH_END - 1)]},
        {"from": 1, "still": "e_old", "marks": [("text", _HOST, "Disposition: hostile")]},
        {"from": 4, "still": "card_disp", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 5, "still": "e_old", "marks": [("text", _HOST, "hostile")]},
        {"from": 6, "still": "t_start", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "t_start", "marks": [("part", "run1:clean")]},
    ]},
    "s03_the_first_side": {"step": 2, "beats": [
        {"from": 0, "still": "e_hollin", "marks": [("hashes", _HOL)]},
        {"from": 1, "still": "e_hollin", "marks": [("text", _HOL, "[Hollin Compact]")]},
        {"from": 2, "still": "e_hollin", "marks": [("text", _HOL, "(hollin)")]},
        {"from": 3, "still": "e_hollin", "marks": [("lines", _HOL + 2, _HOL + 2)]},
        {"from": 4, "still": "e_hollin", "marks": [("lines", _HOL + 3, _HOL + 3)]},
        {"from": 5, "still": "e_hollin", "marks": [("lines", _HOL + 4, _HOL + 4)]},
        {"from": 6, "still": "e_hollin", "marks": [("lines", _HOL + 5, _HOL + 5)]},
        {"from": 7, "still": "e_hollin", "marks": [("lines", _HOL + 6, _HOL + 6)]},
        {"from": 8, "still": "e_hollin", "marks": [("lines", _HOL + 7, _HOL + 7)]},
        {"from": 9, "still": "e_hollin", "marks": [("text", _HOL + 5, "0, 0")]},
        {"from": 11, "still": "game_c53_hollin"},
    ]},
    "s04_two_more_and_who_shoots_firs": {"step": 3, "beats": [
        {"from": 0, "still": "e_three", "marks": [("lines", _DW, _DW + 9)]},
        {"from": 1, "still": "e_three", "marks": [("text", _DW + 4, "neutral")]},
        {"from": 2, "still": "e_three", "marks": [("text", _DW + 5, "3, 1")]},
        {"from": 3, "still": "e_three", "marks": [("text", _GL + 4, "foe")]},
        {"from": 4, "still": "card_disp", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_disp", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_disp", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_foe"},
        {"from": 8, "still": "card_foe", "marks": [("part", "item1")]},
        {"from": 9, "still": "card_foe", "marks": [("part", "item2")]},
        {"from": 12, "still": "e_three", "marks": [("text", _GL + 4, "foe")]},
    ]},
    "s05_two_leads": {"step": 4, "beats": [
        {"from": 0, "still": "e_leads", "marks": [("lines", _L1, _L2 + 6)]},
        {"from": 2, "still": "e_leads", "marks": [("lines", _L1 + 1, _L1 + 5), ("lines", _L2 + 1, _L2 + 5)]},
        {"from": 3, "still": "e_leads", "marks": [("lines", _L1 + 2, _L1 + 3)]},
        {"from": 4, "still": "e_leads", "marks": [("hashes", _NA), ("text", _NA, "(narrative)")]},
        {"from": 5, "still": "e_leads", "marks": [("text", _L1 + 4, "reach 3, 1")]},
        {"from": 6, "still": "e_leads", "marks": [("text", _L1 + 4, "reach 3, 1"), ("text", _L2 + 4, "reach -3, -2")]},
        {"from": 7, "still": "game_c53_quests"},
    ]},
    "s06_goods": {"step": 5, "beats": [
        {"from": 0, "still": "e_goods", "marks": [("hashes", _GO)]},
        {"from": 2, "still": "card_keys"},
        {"from": 3, "still": "e_goods", "marks": [("lines", _ORE, _CON - 1)]},
        {"from": 5, "still": "e_goods", "marks": [("text", _ORE + 2, "Weight: 40"), ("text", _PRO + 2, "Weight: 30"), ("text", _TEC + 2, "Weight: 10")]},
        {"from": 6, "still": "e_goods", "marks": [("text", _ORE + 2, "Weight: 40")]},
        {"from": 7, "still": "e_goods", "marks": [("text", _PRO + 2, "Weight: 30")]},
        {"from": 8, "still": "e_goods_con", "marks": [("text", _CON + 2, "Weight: 5")]},
        {"from": 9, "still": "card_keys", "marks": [("part", "r2")]},
        {"from": 11, "still": "e_goods", "marks": [("hashes", _GO)]},
    ]},
    "s07_check_it": {"step": 6, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "card_eye"},
        {"from": 2, "still": "card_eye", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_eye", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_eye", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_eye", "marks": [("part", "item4")]},
        {"from": 6, "still": "card_eye", "marks": [("part", "item5")]},
        {"from": 7, "still": "card_eye", "marks": [("part", "item6")]},
    ]},
    "s08_meet_the_neighbors": {"step": 7, "beats": [
        {"from": 0, "still": "game_c53_hollin"},
        {"from": 3, "still": "game_c53_relay"},
        {"from": 5, "still": "game_c53_cargo"},
        {"from": 6, "still": "game_c53_quests"},
        {"from": 9, "still": "game_c53_deepwell"},
    ]},
    "s09_the_ones_who_shoot_first": {"step": 7, "beats": [
        {"from": 0, "still": "game_c53_gleaners"},
        {"from": 3, "still": "game_c53_ceasefire"},
        {"from": 8, "still": "game_c53_peace"},
        {"from": 9, "still": "card_cease", "marks": [("part", "r3")]},
        {"from": 11, "still": "card_cease", "marks": [("part", "r4")]},
        {"from": 12, "still": "game_c53_nowork"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_next"},
    ]},
}
