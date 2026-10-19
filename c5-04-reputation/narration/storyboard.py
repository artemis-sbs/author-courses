"""Storyboard for c5-04-reputation: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py.

The lecture starts from Lecture 3's file: `MyUniverse` with c5-03's `kestrel_verge.amd`
("start", 138 lines; only that file is ever opened). The steps are typed in the video's order:
a Values: line on each of the three sides ("values"), the escort's ending and the patrol's
rank ("jobs"), the Dialogue chapter with Hollin's call ("dlg1"), and the Gleaners' call
("final", the page's own example, 198 lines). The text of every state is cut from the
example (see _V, _DLG1, _DLG2), so "final" equals the example byte for byte.

The thresholds (Step 4) and the dials are cards from the page's own tables: the dials are
never written in the finished files, so no state holds them.

Line numbers in the marks are worked out from each state's own text (ln()).

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine by the
person, NEVER by a script: an Open Universe run writes a save. ONE game, TWO windows:
`sbs run server,helm,comms -m MyUniverse map=0` on a probe copy of the example, a new game
(the earlier save deleted). Marks are left off every game still until the stills are taken.
Never caption a face. Press order (the page's Step 6):
  1. Comms, select Hollin Compact: game_c54_hollin (Hail Hollin Compact and Escort (250 cr),
     no Patrol).
  2. Press Hail Hollin Compact: game_c54_cold ("Hollin Compact. State your business,
     captain." and the three answers as buttons).
  3. Press Pay the relay levy: game_c54_levy (the crew has 400 credits).
  4. Select the station again: game_c54_hollin_after (Patrol (240 cr) on offer, Escort now
     (300 cr)).
  5. Hail again: game_c54_friendly ("Kestrel Relay knows your ship, captain.").
  6. Press Escort (300 cr). Helm, the Quest Log, select Hollin Compact: Escort:
     game_c54_engage. Press Engage; on arrival the job is done: game_c54_done.
  7. Quest Log, The Breaking Yard, Engage. Comms, select the Gleaners' station:
     game_c54_gl_station (Negotiate Ceasefire at 600, the game's own Hail and Taunt among
     the buttons, and the Gleaners' own Hail The Gleaners).
  8. Press Hail The Gleaners: game_c54_gl_hail ("You are standing in our yard. Explain
     that." and its two answers). Press Tell them you go where you like.
  9. Select the station again: game_c54_gl_after (Salvage (180 cr) on offer, Negotiate
     Ceasefire now at 200).
"""
import os

LECTURE = "c5-04-reputation"
TITLE = ("Class 5, Lecture 4", "Reputation", "Sides that remember what the crew says and does")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"

_EX3 = "c5-03-sides-diplomacy-goods/example"
_EX = "c5-04-reputation/example"
_HERE = os.path.dirname(os.path.abspath(__file__))


def _read(*parts):
    with open(os.path.join(_HERE, "..", *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


_START = _read("..", "c5-03-sides-diplomacy-goods", "example", "kestrel_verge.amd")
_FINAL = _read("example", "kestrel_verge.amd")

_V1, _V2, _V3 = ("Values: honest 40, generous 30\n", "Values: by-the-book 40, peaceful 20\n",
                 "Values: fearsome 40, resourceful 30\n")
_I_DLG, _I_GL = _FINAL.index("## [Dialogue](dialogue)"), _FINAL.index("### [Gleaner Hail](gleaner_hail)")
_DLG1 = _FINAL[_I_DLG:_I_GL].rstrip("\n") + "\n"
_DLG2 = _FINAL[_I_GL:]

_T = {}
_T["start"] = _START
_T["values"] = (_START.replace("Home: 0, 0\nOffers: patrol, escort", "Home: 0, 0\n" + _V1 + "Offers: patrol, escort")
                .replace("Home: 3, 1\nOffers: escort", "Home: 3, 1\n" + _V2 + "Offers: escort")
                .replace("Home: -3, -2\nOffers: salvage", "Home: -3, -2\n" + _V3 + "Offers: salvage"))
_T["jobs"] = (_T["values"]
              .replace("### [Escort](escort)\n---\nReward: 250 credits", "### [Escort](escort)\n---\nDone when: reach 3, 1\nReward: 250 credits")
              .replace("### [Patrol](patrol)\n---\nReward: 200 credits", "### [Patrol](patrol)\n---\nTier: 2\nReward: 200 credits"))
_T["dlg1"] = _T["jobs"] + "\n" + _DLG1
_T["final"] = _T["dlg1"] + "\n" + _DLG2


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
    # C5-02 holds the folder (story.mast, description.yaml); C5-03 holds only the .amd.
    "start": {"folder": "c5-02-your-universe-file/example", "over": [_EX3]},
    # Step 1: a Values: line on each side
    "values": {"base": "start", "edits": [("write", FILE, _T["values"])]},
    # Step 2: the escort's ending and the patrol's rank
    "jobs": {"base": "values", "edits": [("write", FILE, _T["jobs"])]},
    # Step 3: the Dialogue chapter with Hollin's call, then the Gleaners' call. The page's own example.
    "dlg1": {"base": "jobs", "edits": [("write", FILE, _T["dlg1"])]},
    "final": {"base": "dlg1", "edits": [("write", FILE, _T["final"])], "same_as": (_EX + "/kestrel_verge.amd",)},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}

# where the marks are
_HOL = ln("values", "### [Hollin Compact]")
_DW = ln("values", "### [Deepwell Assembly]")
_GL = ln("values", "### [The Gleaners]")
_HV, _DV, _GV = ln("values", "Values: honest"), ln("values", "Values: by-the-book"), ln("values", "Values: fearsome")
_PAT, _ESC = ln("jobs", "### [Patrol]"), ln("jobs", "### [Escort]")
_TIER, _DONE = ln("jobs", "Tier: 2"), ln("jobs", "Done when: reach 3, 1", 1)
_DH = ln("final", "## [Dialogue]")
_HH = ln("final", "### [Hollin Hail]")                       # the call: Speaker, When, two guarded lines, three answers
_LEVY = ln("final", "- [Pay the relay levy]")
_G1, _G2 = ln("final", "%{standing >= 20} Kestrel"), ln("final", "%{standing < 20} Hollin")
_GH = ln("final", "### [Gleaner Hail]")
_GA1, _GA2 = ln("final", "- [Tell them you go where you like]"), ln("final", "- [Back away]")

STILLS = {
    # The editor. A still shows 21 lines: the one named, ten above and ten below
    "e_val_hd": ("vscode", "values", (_HV + _DV) // 2, "big", _NS),     # the Values: lines of Hollin and Deepwell
    "e_val_g": ("vscode", "values", _GV, "big", _NS),                   # the Gleaners' Values: line
    "e_jobs": ("vscode", "jobs", (_PAT + _ESC) // 2 + 3, "big", _NS),   # Patrol with Tier: 2, Escort with Done when
    "e_dlg_a": ("vscode", "dlg1", _HH + 7, "big", _NS),                 # Hollin's call: Speaker, When, the guarded lines, the answers
    "e_dlg_b": ("vscode", "dlg1", _LEVY + 6, "big", _NS),               # the answers and the three short records they lead to
    "e_dlg_c": ("vscode", "final", _GH + 6, "big", _NS),                # the Gleaners' call, no cost on the bold answer
    "e_final": ("vscode", "final", _GH - 4, "big", _NS),                # the end of Hollin's records and the Gleaners' call
    # the command prompt
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm,comms
    "game_c54_hollin": ("game", "Comms with Hollin Compact selected: Hail Hollin Compact and Escort (250 cr) among its buttons, no Patrol"),
    "game_c54_cold": ("game", "Comms after Hail Hollin Compact: 'Hollin Compact. State your business, captain.' and the three answers as buttons"),
    "game_c54_levy": ("game", "Comms just after Pay the relay levy: the answer 'Paid and entered', the crew down to 400 credits"),
    "game_c54_hollin_after": ("game", "Comms with Hollin Compact selected again: Patrol (240 cr) on offer and Escort now reading (300 cr)"),
    "game_c54_friendly": ("game", "Comms after a second Hail: 'Kestrel Relay knows your ship, captain.'"),
    "game_c54_engage": ("game", "Helm's Quest Log with Hollin Compact: Escort selected, the Engage button in view"),
    "game_c54_done": ("game", "Helm on arrival at 3, 1: the escort done, the pay in"),
    "game_c54_gl_station": ("game", "Comms with the Gleaners' station selected: Negotiate Ceasefire at 600 and Hail The Gleaners among the buttons"),
    "game_c54_gl_hail": ("game", "Comms after Hail The Gleaners: 'You are standing in our yard. Explain that.' and its two answers"),
    "game_c54_gl_after": ("game", "Comms with the Gleaners' station selected again: Salvage (180 cr) on offer and Negotiate Ceasefire at 200"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_traits": ("card", "table", {"heading": "Step 1 - What each side values", "nth": 1, "kicker": "Seven pairs of traits"}),
    "card_avg": ("card", "table", {"heading": "Step 1 - What each side values", "nth": 2, "kicker": "Standing with Hollin, who value honest 40, generous 30"}),
    "card_deeds": ("card", "points", {"kicker": "Two ways to earn a name", "items": [
        "Finish a side's job: its standing goes up by 5, and you write nothing for it.",
        "Give an answer when a station calls: the answer says what it costs and what it earns."]}),
    "card_thresh": ("card", "table", {"heading": "Step 4 - The thresholds", "nth": 1, "kicker": "Where standing crosses a line"}),
    "card_dials": ("card", "table", {"heading": "Step 4 - The thresholds", "nth": 2, "kicker": "Each line is a dial in the title record"}),
    "card_farm": ("card", "rows", {"kicker": "The Gleaners' bold answer, given again for nothing", "header": ["Times given", "Standing with the Gleaners"],
                                   "rows": [["Once", "20"], ["Three times", "57, and it stops there: they value resourceful too"]]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Give each side a memory"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 5", "sub": "The map"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_val_hd"},
        {"from": 3, "still": "e_dlg_a"},
        {"from": 4, "still": "game_c54_hollin"},
        {"from": 5, "still": "card_deeds"},
        {"from": 7, "still": "game_c54_hollin_after"},
    ]},
    "s02_what_a_side_values": {"step": 1, "beats": [
        {"from": 0, "still": "card_traits"},
        {"from": 1, "still": "card_traits", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 2, "still": "card_traits", "marks": [("part", "r4")]},
        {"from": 3, "still": "card_traits"},
        {"from": 4, "still": "card_traits", "marks": [("part", "r6")]},
        {"from": 5, "still": "card_traits", "marks": [("part", "r2")]},
        {"from": 6, "still": "e_val_hd", "marks": [("lines", _HV, _HV)]},
        {"from": 7, "still": "e_val_hd", "marks": [("text", _HV, "honest 40, generous 30")]},
        {"from": 8, "still": "e_val_hd", "marks": [("lines", _HV, _HV)]},
        {"from": 9, "still": "e_val_hd", "marks": [("lines", _DV, _DV)]},
        {"from": 10, "still": "e_val_g", "marks": [("lines", _GV, _GV)]},
    ]},
    "s03_standing_is_an_average": {"step": 1, "beats": [
        {"from": 0, "still": "card_avg"},
        {"from": 4, "still": "card_avg", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_avg", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_avg", "marks": [("part", "r4")]},
        {"from": 7, "still": "card_avg"},
    ]},
    "s04_a_deed_in_work": {"step": 2, "beats": [
        {"from": 0, "still": "card_deeds"},
        {"from": 2, "still": "card_deeds", "marks": [("part", "item1")]},
        {"from": 6, "still": "e_jobs"},
        {"from": 7, "still": "e_jobs", "marks": [("lines", _DONE, _DONE)]},
        {"from": 8, "still": "e_jobs", "marks": [("text", _DONE, "reach 3, 1")]},
        {"from": 9, "still": "e_jobs", "marks": [("lines", _TIER, _TIER)]},
        {"from": 10, "still": "card_thresh", "marks": [("part", "r1")]},
    ]},
    "s05_a_deed_in_talk": {"step": 3, "beats": [
        {"from": 0, "still": "e_dlg_a", "marks": [("hashes", _DH)]},
        {"from": 1, "still": "e_dlg_a", "marks": [("lines", _HH, _LEVY + 2)]},
        {"from": 4, "still": "e_dlg_a", "marks": [("lines", _HH + 2, _HH + 2)]},
        {"from": 5, "still": "e_dlg_a", "marks": [("lines", _HH + 3, _HH + 3)]},
        {"from": 6, "still": "e_dlg_a", "marks": [("lines", _G1, _G2)]},
        {"from": 7, "still": "e_dlg_a", "marks": [("lines", _LEVY, _LEVY + 2)]},
        {"from": 9, "still": "e_dlg_a", "marks": [("text", _LEVY, "; costs 100 credits, earns hollin honest 20, earns hollin generous 20")]},
        {"from": 10, "still": "e_dlg_a", "marks": [("text", _LEVY, "costs 100 credits")]},
        {"from": 11, "still": "e_dlg_a", "marks": [("text", _LEVY, "earns hollin honest 20"), ("text", _LEVY, "earns hollin generous 20")]},
        {"from": 13, "still": "e_dlg_a", "marks": [("text", _G1, "%{standing >= 20}")]},
        {"from": 14, "still": "e_dlg_a", "marks": [("text", _G1, "standing >= 20")]},
        {"from": 15, "still": "e_dlg_a", "marks": [("lines", _G1, _G2)]},
    ]},
    "s06_two_traps_in_a_call": {"step": 3, "beats": [
        {"from": 0, "still": "e_dlg_a", "marks": [("lines", _G1, _G2)]},
        {"from": 2, "still": "e_dlg_a", "marks": [("lines", _G2, _G2)]},
        {"from": 4, "still": "e_dlg_b", "marks": [("lines", _LEVY, _LEVY + 2)]},
        {"from": 7, "still": "e_dlg_b", "marks": [("text", _LEVY, "costs 100 credits")]},
        {"from": 8, "still": "e_dlg_c", "marks": [("lines", _GA1, _GA1)]},
        {"from": 9, "still": "e_dlg_c", "marks": [("text", _GA1, "earns gleaners fearsome 35")]},
    ]},
    "s07_the_thresholds": {"step": 4, "beats": [
        {"from": 0, "still": "card_thresh"},
        {"from": 1, "still": "card_thresh", "marks": [("part", "r1"), ("part", "r3")]},
        {"from": 3, "still": "card_thresh", "marks": [("part", "r4")]},
        {"from": 4, "still": "card_thresh", "marks": [("part", "r5")]},
        {"from": 5, "still": "card_thresh", "marks": [("part", "r5"), ("part", "r6")]},
        {"from": 6, "still": "card_dials"},
        {"from": 8, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s08_play_it_the_farmers": {"step": 6, "beats": [
        {"from": 0, "still": "game_c54_hollin"},
        {"from": 1, "still": "game_c54_cold"},
        {"from": 2, "still": "game_c54_levy"},
        {"from": 3, "still": "game_c54_hollin_after"},
        {"from": 5, "still": "game_c54_friendly"},
        {"from": 7, "still": "game_c54_engage"},
        {"from": 8, "still": "game_c54_done"},
    ]},
    "s09_play_it_the_wreckers": {"step": 6, "beats": [
        {"from": 0, "still": "game_c54_gl_station"},
        {"from": 4, "still": "game_c54_gl_hail"},
        {"from": 7, "still": "game_c54_gl_after"},
        {"from": 11, "still": "e_dlg_c", "marks": [("text", _GA1, "earns gleaners fearsome 35")]},
        {"from": 12, "still": "card_farm", "marks": [("part", "r2")]},
        {"from": 15, "still": "card_farm"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_next"},
    ]},
}
