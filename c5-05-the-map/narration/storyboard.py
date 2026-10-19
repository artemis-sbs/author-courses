"""Storyboard for c5-05-the-map: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py.

The lecture starts from Lecture 4's file: `MyUniverse` with c5-04's `kestrel_verge.amd`
("start", 198 lines; only that file is ever opened). The steps are typed in the video's order:
the four dial lines under Display: in the title record ("dials"), the Regions chapter in front
of Landmarks, The Hollin Fields first ("reg1") and then The Breakers ("reg2"), the three
landmarks under Kestrel Relay, one at a time ("l1" Assay Office, "l2" The Tern, "l3" The Bone
Pile), and the two leads at the end of the Narrative chapter ("final", the page's own example, 272 lines). The text of
every state is cut from the example (see _REG_H, _REG_B, _LM_A, _LM_T, _LM_B, _LEADS), so
"final" equals the example byte for byte.

Line numbers in the marks are worked out from each state's own text (ln()).

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine by the
person, NEVER by a script: an Open Universe run writes a save. ONE game, TWO windows:
`sbs run server,helm,comms -m MyUniverse map=0` on a probe copy of the example, a new game
(the earlier save deleted). The seed is not controlled for these stills: which system is
which is different in every new game (the page says so), but the landmarks, the homes and the
regions are fixed. Marks are left off every game still until the stills are taken. Never
caption a face. Press order (the page's Step 7):
  1. Helm at once, the handheld icon, Quests: game_c55_quests (four leads: The Second
     Colony, The Breaking Yard, The Third Colony, What the Gleaners Keep).
  2. Engage The Third Colony: game_c55_tern (the card reading The Tern with its line, the dead
     ship in a nebula).
  3. Engage The Second Colony: game_c55_assay (the card reading Assay Office). Comms, select
     the Assay Office: game_c55_assay_comms (the Deepwell's escort among its buttons).
  4. Engage What the Gleaners Keep: game_c55_bone (the card reading The Bone Pile, the red
     sky of the Breakers, a fleet waiting).
  5. Engage The Breaking Yard: game_c55_breakers (the card reading The Breakers, with the
     system's two numbers under it).
  6. Quest Log, Charted Locations open: game_c55_charted (Kestrel Relay, The Tern, Assay
     Office, The Bone Pile).
  7. For game_c55_uncharted, ONE extra run with a probe copy of state l1 minus the Assay
     Office record (the file as Lecture 4 left it): engage The Second Colony; the card reads
     Uncharted and (3, 1).
"""
import os

LECTURE = "c5-05-the-map"
TITLE = ("Class 5, Lecture 5", "The map", "Regions, landmarks and the dials that shape the galaxy")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"

_EX4 = "c5-04-reputation/example"
_EX = "c5-05-the-map/example"
_HERE = os.path.dirname(os.path.abspath(__file__))


def _read(*parts):
    with open(os.path.join(_HERE, "..", *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


_START = _read("..", "c5-04-reputation", "example", "kestrel_verge.amd")
_FINAL = _read("example", "kestrel_verge.amd")

_DIALS = "Station mix: 8%\nEnemy mix: 12%\nNebula mix: 20%\nDerelict chance: 60%\n"
_I_R, _I_BR, _I_L = (_FINAL.index("## [Regions](regions)"), _FINAL.index("### [The Breakers]"),
                     _FINAL.index("## [Landmarks](landmarks)"))
_REG_H, _REG_B = _FINAL[_I_R:_I_BR], _FINAL[_I_BR:_I_L]
_I_A, _I_T, _I_B, _I_G = (_FINAL.index("### [Assay Office]"), _FINAL.index("### [The Tern]"),
                          _FINAL.index("### [The Bone Pile]"), _FINAL.index("## [Goods](goods)"))
_LM_A, _LM_T, _LM_B = _FINAL[_I_A:_I_T], _FINAL[_I_T:_I_B], _FINAL[_I_B:_I_G]
_LEADS = _FINAL[_FINAL.index("### [The Third Colony]"):_FINAL.index("## [Dialogue](dialogue)")]

_T = {}
_T["start"] = _START
_T["dials"] = _START.replace("Display: The Kestrel Verge\n", "Display: The Kestrel Verge\n" + _DIALS)
_T["reg1"] = _T["dials"].replace("## [Landmarks](landmarks)", _REG_H + "## [Landmarks](landmarks)")
_T["reg2"] = _T["reg1"].replace(_REG_H + "## [Landmarks](landmarks)", _REG_H + _REG_B + "## [Landmarks](landmarks)")
_T["l1"] = _T["reg2"].replace("rumor.\n\n## [Goods](goods)", "rumor.\n\n" + _LM_A + "## [Goods](goods)")
_T["l2"] = _T["l1"].replace(_LM_A + "## [Goods](goods)", _LM_A + _LM_T + "## [Goods](goods)")
_T["l3"] = _T["l2"].replace(_LM_A + _LM_T + "## [Goods](goods)", _LM_A + _LM_T + _LM_B + "## [Goods](goods)")
_T["final"] = _T["l3"].replace("## [Dialogue](dialogue)", _LEADS + "## [Dialogue](dialogue)")


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
    "start": {"folder": _EX4},
    # Step 2: four dial lines under Display:
    "dials": {"base": "start", "edits": [("write", FILE, _T["dials"])]},
    # Step 3: the Regions chapter, in front of Landmarks: The Hollin Fields, then The Breakers
    "reg1": {"base": "dials", "edits": [("write", FILE, _T["reg1"])]},
    "reg2": {"base": "reg1", "edits": [("write", FILE, _T["reg2"])]},
    # Step 4: three landmarks under Kestrel Relay
    "l1": {"base": "reg2", "edits": [("write", FILE, _T["l1"])]},
    "l2": {"base": "l1", "edits": [("write", FILE, _T["l2"])]},
    "l3": {"base": "l2", "edits": [("write", FILE, _T["l3"])]},
    # Step 5: the two leads, at the end of the Narrative chapter. The page's own example.
    "final": {"base": "l3", "edits": [("write", FILE, _T["final"])], "same_as": (_EX + "/kestrel_verge.amd",)},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}

# where the marks are
_TH = ln("dials", "# [The Kestrel Verge]")
_DISP = ln("dials", "Display: The Kestrel Verge")
_SM, _EM, _NM, _DC = (ln("dials", "Station mix: 8%"), ln("dials", "Enemy mix: 12%"),
                      ln("dials", "Nebula mix: 20%"), ln("dials", "Derelict chance: 60%"))
_RH = ln("reg1", "## [Regions]")
_HF = ln("reg1", "### [The Hollin Fields]")
_BR = ln("reg2", "### [The Breakers]")
_AO, _TE, _BP = ln("l3", "### [Assay Office]"), ln("l3", "### [The Tern]"), ln("l3", "### [The Bone Pile]")
_KR_TX = ln("l1", "The last relay anyone")
_TC, _GK = ln("final", "### [The Third Colony]"), ln("final", "### [What the Gleaners Keep]")
_SC = ln("final", "### [The Second Colony]")


def _in(state, head, key, nth=1):
    """The line of a fact (key) inside the record that starts on line head."""
    seen = 0
    for i, line in enumerate(_T[state].split("\n")[head - 1:], head):
        if line.startswith(key):
            seen += 1
            if seen == nth:
                return i
    raise ValueError(key)


STILLS = {
    # The editor. A still shows 21 lines: the one named, ten above and ten below
    "e_dials": ("vscode", "dials", _DISP + 2, "big", _NS),                # the title record with the four dials
    "e_dials_old": ("vscode", "start", _DISP + 2, "big", _NS),            # the title record before the dials
    "e_reg1": ("vscode", "reg1", _HF + 6, "big", _NS),                    # the Regions chapter: The Hollin Fields
    "e_reg2": ("vscode", "reg2", _BR + 6, "big", _NS),                    # The Breakers
    "e_l1": ("vscode", "l1", _AO + 4, "big", _NS),                        # Kestrel Relay, then Assay Office
    "e_l2": ("vscode", "l2", _TE + 4, "big", _NS),                        # The Tern
    "e_l3": ("vscode", "l3", _BP + 4, "big", _NS),                        # The Bone Pile
    "e_leads": ("vscode", "final", _TC + 6, "big", _NS),                  # the two new leads, The Third Colony with its two paragraphs
    "e_lead_old": ("vscode", "final", _SC + 5, "big", _NS),               # the old lead that already goes to the Assay Office
    # the command prompt
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm,comms
    "game_c55_quests": ("game", "Helm's Quest Log: four leads (The Second Colony, The Breaking Yard, The Third Colony, What the Gleaners Keep)"),
    "game_c55_tern": ("game", "Helm on arrival at 1, -2: the card reading The Tern with its line, the dead ship in a nebula"),
    "game_c55_uncharted": ("game", "Helm on arrival at 3, 1 in the file as Lecture 4 left it: the card reading Uncharted and (3, 1)"),
    "game_c55_assay": ("game", "Helm on arrival at 3, 1: the card reading Assay Office with its line"),
    "game_c55_assay_comms": ("game", "Comms with the Assay Office selected: the Deepwell's escort among its buttons"),
    "game_c55_bone": ("game", "Helm on arrival at -4, -3: the card reading The Bone Pile, the red sky of the Breakers, a fleet waiting"),
    "game_c55_breakers": ("game", "Helm on arrival at -3, -2: the card reading The Breakers with the system's two numbers under it"),
    "game_c55_charted": ("game", "Helm's Quest Log, Charted Locations open: Kestrel Relay, The Tern, Assay Office and The Bone Pile"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_kinds": ("card", "table", {"heading": "Step 1 - How the game fills a system", "nth": 1, "kicker": "What a system is, unless you say otherwise"}),
    "card_extras": ("card", "table", {"heading": "Step 1 - How the game fills a system", "nth": 2, "kicker": "On top of its kind, a system can have extras"}),
    "card_dials": ("card", "table", {"heading": "Step 2 - The dials", "nth": 1, "kicker": "All eight dials"}),
    "card_counts": ("card", "table", {"heading": "Step 2 - The dials", "nth": 2, "kicker": "Counted over the 169 systems nearest home"}),
    "card_pct": ("card", "rows", {"kicker": "Write the percent sign", "header": ["You write", "The game reads it as"],
                                  "rows": [["Enemy mix: 12%", "12 in 100"],
                                           ["Enemy mix: 12", "1200 in 100, and lint says nothing"]]}),
    "card_lines": ("card", "table", {"heading": "Step 3 - Regions", "nth": 1, "kicker": "A region, line by line"}),
    "card_skies": ("card", "table", {"heading": "Step 3 - Regions", "nth": 2, "kicker": "The seven skies"}),
    "card_paper": ("card", "points", {"kicker": "Draw it on paper first", "items": [
        "Mark each side's home on a grid with 0, 0 in the middle.",
        "Draw each region as a square.",
        "Do two regions overlap? A system belongs to the one written first.",
        "Is each side's home inside the region you meant for it? Nothing moves a home for you."]}),
    "card_lm": ("card", "table", {"heading": "Step 4 - Three more landmarks", "nth": 1, "kicker": "A landmark, line by line"}),
    "card_eye": ("card", "points", {"kicker": "After lint, check these by eye", "items": [
        "Every mix and every chance ends in a percent sign, and the four mixes come to well under 100.",
        "Every region has a Center: of two numbers and a Radius: that is a number.",
        "Every Skybox: is one of the seven, letter for letter.",
        "A small region is written before a large one that overlaps it.",
        "Every landmark's line is one line, of 60 characters or fewer."]}),
    "card_facts": ("card", "table", {"heading": "Step 7 - Play it", "nth": 1, "kicker": "What you need to know about the map"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Draw your own galaxy"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 6", "sub": "Jobs"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "card_kinds"},
        {"from": 2, "still": "e_dials"},
        {"from": 4, "still": "e_reg2"},
        {"from": 5, "still": "e_l3"},
    ]},
    "s02_how_a_system_is_filled": {"step": 1, "beats": [
        {"from": 0, "still": "card_kinds"},
        {"from": 4, "still": "card_kinds", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_kinds", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_kinds", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 7, "still": "card_kinds", "marks": [("part", "r5")]},
        {"from": 8, "still": "card_extras", "marks": [("part", "r1"), ("part", "r2"), ("part", "r4")]},
        {"from": 10, "still": "card_dials"},
    ]},
    "s03_the_dials": {"step": 2, "beats": [
        {"from": 0, "still": "card_dials"},
        {"from": 1, "still": "e_dials", "marks": [("lines", _TH, _DC + 1)]},
        {"from": 3, "still": "e_dials", "marks": [("text", _SM, "Station mix: 8%"), ("text", _NM, "Nebula mix: 20%")]},
        {"from": 4, "still": "e_dials", "marks": [("text", _DC, "Derelict chance: 60%")]},
        {"from": 5, "still": "e_dials", "marks": [("lines", _SM, _DC)]},
        {"from": 6, "still": "card_counts"},
        {"from": 7, "still": "card_counts", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_counts", "marks": [("part", "r3")]},
        {"from": 9, "still": "e_dials", "marks": [("lines", _SM, _DC)]},
        {"from": 10, "still": "e_dials", "marks": [("text", _SM, "%"), ("text", _EM, "%"), ("text", _NM, "%"), ("text", _DC, "%")]},
        {"from": 11, "still": "card_pct", "marks": [("part", "r2")]},
    ]},
    "s04_a_region": {"step": 3, "beats": [
        {"from": 0, "still": "e_reg1", "marks": [("hashes", _RH)]},
        {"from": 1, "still": "e_reg1", "marks": [("lines", _HF, _HF + 9)]},
        {"from": 2, "still": "e_reg1", "marks": [("text", _HF + 2, "Center: 0, 0")]},
        {"from": 3, "still": "e_reg1", "marks": [("text", _HF + 3, "Radius: 2")]},
        {"from": 5, "still": "card_skies"},
        {"from": 6, "still": "e_reg1", "marks": [("lines", _HF + 6, _HF + 7)]},
        {"from": 7, "still": "e_reg1", "marks": [("text", _HF + 6, "Enemy mix: 0%"), ("text", _HF + 7, "Station mix: 25%")]},
        {"from": 8, "still": "e_reg1", "marks": [("lines", _HF, _HF + 9)]},
    ]},
    "s05_a_second_region_and_the_grid": {"step": 3, "beats": [
        {"from": 0, "still": "e_reg2", "marks": [("lines", _BR, _BR + 11)]},
        {"from": 1, "still": "e_reg2", "marks": [("text", _BR + 4, "sky-neb2-rvb"), ("text", _BR + 5, "Artemis2")]},
        {"from": 2, "still": "e_reg2", "marks": [("lines", _BR + 7, _BR + 9)]},
        {"from": 3, "still": "card_paper"},
        {"from": 5, "still": "card_paper", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 7, "still": "card_paper", "marks": [("part", "item3")]},
        {"from": 9, "still": "card_paper", "marks": [("part", "item4")]},
    ]},
    "s06_a_landmark_that_names_a_home": {"step": 4, "beats": [
        {"from": 0, "still": "e_l1", "marks": [("lines", _KR_TX, _KR_TX)]},
        {"from": 2, "still": "card_lm"},
        {"from": 3, "still": "e_l1", "marks": [("lines", _AO, _AO + 7)]},
        {"from": 4, "still": "game_c55_uncharted"},
        {"from": 6, "still": "e_l1", "marks": [("text", _AO + 2, "At: 3, 1")]},
        {"from": 8, "still": "game_c55_assay"},
        {"from": 9, "still": "game_c55_charted"},
        {"from": 10, "still": "e_l1", "marks": [("text", _AO + 4, "Side: deepwell")]},
    ]},
    "s07_a_dead_ship_and_a_guarded_on": {"step": 4, "beats": [
        {"from": 0, "still": "e_l2", "marks": [("text", _TE + 3, "Prefab: derelict")]},
        {"from": 3, "still": "e_l2", "marks": [("lines", _TE, _TE + 6)]},
        {"from": 4, "still": "e_l2", "marks": [("text", _TE + 4, "Terrain: nebula blue")]},
        {"from": 5, "still": "e_l3", "marks": [("lines", _BP, _BP + 7)]},
        {"from": 6, "still": "e_l3", "marks": [("text", _BP + 5, "Guards: torgoth")]},
        {"from": 9, "still": "game_c55_bone"},
    ]},
    "s08_leads_and_check": {"step": 5, "beats": [
        {"from": 0, "still": "e_leads", "marks": [("lines", _TC, _GK + 6)]},
        {"from": 2, "still": "e_lead_old", "marks": [("text", _SC + 4, "reach 3, 1")]},
        {"from": 4, "still": "e_leads", "marks": [("lines", _TC + 6, _TC + 8)]},
        {"from": 7, "still": "e_leads", "marks": [("lines", _TC + 6, _TC + 6)]},
        {"from": 8, "still": "e_leads", "marks": [("lines", _TC + 8, _TC + 8)]},
        {"from": 9, "still": "e_l2", "marks": [("lines", _TE + 6, _TE + 6)]},
        {"from": 13, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 14, "still": "card_eye"},
        {"from": 15, "still": "card_eye", "marks": [("part", "item3")]},
        {"from": 16, "still": "card_eye", "marks": [("part", "item1")]},
    ]},
    "s09_fly_the_map": {"step": 7, "beats": [
        {"from": 0, "still": "game_c55_quests"},
        {"from": 1, "still": "game_c55_tern"},
        {"from": 3, "still": "game_c55_assay"},
        {"from": 5, "still": "game_c55_assay_comms"},
        {"from": 6, "still": "game_c55_bone"},
        {"from": 8, "still": "game_c55_breakers"},
        {"from": 11, "still": "game_c55_charted"},
        {"from": 13, "still": "card_facts", "marks": [("part", "r2")]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item3"), ("part", "item4"), ("part", "item5")]},
        {"from": 5, "still": "card_next"},
    ]},
}
