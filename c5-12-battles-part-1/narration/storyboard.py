"""Storyboard for c5-12-battles-part-1: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py (2026-10-18).

The lecture starts from Lecture 9's `MyUniverse` (the c5-02 files with c5-03 to c5-09 laid
over them), with a `settings.yaml` that has DIFFICULTY: 5 on line 53 (the template's own) and
the template's `story.mast`, which has no DANGER / ENCOUNTERS card yet. The steps are typed
in the video's order: DIFFICULTY 5 -> 4 ("d4"), the Bone Pile's `Guards: torgoth 7` ("g7"),
the Tern's `Guards: pirate 2` ("tern"), then the card pasted into story.mast ("final", the
page's own example: kestrel_verge.amd, settings.yaml and story.mast all `same_as`).
Lines are looked up in the text (_ln), never typed, so a state that moves a line moves its marks.

NOT SHOWN AS WRITTEN: the page's long "mistakes lint cannot see" tables are never drawn (the
lecture's scenes do not read them). The lint terminal is the stand-in's real `sbs lint`.

GAME STILLS. NOT TAKEN YET: planned here, to be taken in one sitting in the real engine. This is
an Open Universe mission: the probe is built in data/missions/_sandbox so it cannot touch the
player's saves (game.py backs them up and restores them), but DO NOT start it from a hand
launch. ONE game, THREE windows:
`python game.py c5-12-battles-part-1 start --state final --consoles server,helm,comms`
(the page's run line, on a probe copy of the example, seed=7). No probe patch. Marks are left
off every game still until the stills are taken. Press order:
  1. Helm, at once: the handheld icon, Quests: game_c12_log (the three leads, The Third
     Colony among them, an Engage button).
  2. Engage The Third Colony. The ship arrives at The Tern: game_c12_tern (the card `The Tern`
     and the orange `Threat` card, "The Tern is guarded - hostiles on approach.", both up).
  3. Quest Log, Engage The Breaking Yard (the Gleaners' home). On arrival: game_c12_home (the
     map or 3D view with the station and its one fleet close).
  4. Same visit, Weapons or Helm radar a few seconds later, once the four fighters have
     launched (five visits in seven do): game_c12_fighters (four small contacts beside the
     station; do not caption any name). If the fighters do not launch, leave the game and
     start again with the same line: the save is restored between runs.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.join(_HERE, "..", "..")


def _rd(*parts):
    with open(os.path.join(_ROOT, *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


def _ln(text, needle, nth=1):
    """The 1-based line of the nth place `needle` starts in text."""
    at = -1
    for _ in range(nth):
        at = text.index(needle, at + 1)
    return text.count("\n", 0, at) + 1


LECTURE = "c5-12-battles-part-1"
TITLE = ("Class 5, Lecture 12", "Battles, part 1", "How dangerous a system is, and a budget of ships")
MISSION = "MyUniverse"
FILE = "kestrel_verge.amd"
MAST = "story.mast"
TEMPLATE = "ou"

_EX = "c5-12-battles-part-1/example"
_OVER9 = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe"))

_AMD0 = _rd("c5-09-organizing-a-big-universe", "example", "kestrel_verge.amd")
_AMD7 = _AMD0.replace("Guards: torgoth\n", "Guards: torgoth 7\n")
_AMDT = _AMD7.replace("Terrain: nebula blue\n", "Terrain: nebula blue\nGuards: pirate 2\n")
_SET_F = _rd("c5-12-battles-part-1", "example", "settings.yaml")
_SET_5 = _SET_F.replace("DIFFICULTY: 4", "DIFFICULTY: 5")
_MAST0 = _rd("c5-02-your-universe-file", "example", "story.mast")
_MAST_F = _rd("c5-12-battles-part-1", "example", "story.mast")

_DIFF = _ln(_SET_5, "DIFFICULTY: 5")
_G0 = _ln(_AMD0, "Guards: torgoth")
_G7 = _ln(_AMD7, "Guards: torgoth 7")
_GT = _ln(_AMDT, "Guards: pirate 2")
_PILE = _ln(_AMD0, "### [The Bone Pile]")
_GLE_A = _ln(_AMDT, "### [The Gleaners](gleaners)")
_GLE_B = _ln(_AMDT, "They strip dead ships for a living")
_TR_A = _ln(_MAST0, "default shared QUEST_ENGAGE_ENABLED")
_TR_B = _ln(_MAST0, "default shared WAYPOINTS_ENABLED")
_CARD_A = _ln(_MAST_F, "# How dangerous the galaxy is")
_DG = _ln(_MAST_F, "default shared DANGER")
_EN = _ln(_MAST_F, "default shared ENCOUNTERS")

STATES = {
    # Lecture 9's files; settings.yaml as the template ships it (DIFFICULTY: 5)
    "start": {"folder": "c5-02-your-universe-file/example", "over": _OVER9,
              "edits": [("write", "settings.yaml", _SET_5)]},
    # Step 2: line 53 made 4
    "d4": {"base": "start", "edits": [("replace", "settings.yaml", "DIFFICULTY: 5", "DIFFICULTY: 4")]},
    # Step 3: the Bone Pile's guards get a tier, then the Tern gets a guard
    "g7": {"base": "d4", "edits": [("replace", FILE, "Guards: torgoth\n", "Guards: torgoth 7\n")]},
    "tern": {"base": "g7", "edits": [("replace", FILE, "Terrain: nebula blue\n", "Terrain: nebula blue\nGuards: pirate 2\n")]},
    # Step 5: the DANGER / ENCOUNTERS card pasted into story.mast. The page's own example.
    "final": {"base": "tern", "edits": [("write", MAST, _MAST_F)],
              "same_as": (_EX + "/kestrel_verge.amd", _EX + "/settings.yaml", _EX + "/story.mast")},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}
_SET = {"file": "settings.yaml", "side": False}
_MST = {"file": MAST, "side": False}

STILLS = {
    # The editor. Each window shows the 21 lines round the line named.
    "e_set5": ("vscode", "start", _DIFF, "big", _SET),         # settings.yaml, DIFFICULTY: 5
    "e_set4": ("vscode", "d4", _DIFF, "big", _SET),            # DIFFICULTY: 4
    "e_bone0": ("vscode", "start", _G0, "big", _NS),           # the Bone Pile, Guards: torgoth
    "e_bone7": ("vscode", "g7", _G7, "big", _NS),              # Guards: torgoth 7
    "e_tern": ("vscode", "tern", _GT, "big", _NS),             # the Tern, Guards: pirate 2
    "e_gleaners": ("vscode", "final", _GLE_A + 6, "big", _NS),  # the Gleaners' side record
    "e_mast0": ("vscode", "start", _TR_B, "big", _MST),        # story.mast, the two travel lines
    "e_mastc": ("vscode", "final", _DG, "big", _MST),          # story.mast with the card
    # the command prompt
    "t_lint": ("terminal", [("final", _LINT)]),
    "t_run": ("session", ["sbs run server,helm,comms -m MyUniverse map=0 --dry-run"], {"state": "final"}),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c12_log": ("game", "Helm, the Quest Log open: the three leads, The Third Colony among them, with Engage"),
    "game_c12_tern": ("game", "Helm just after arriving at The Tern: the Tern card and the orange Threat card 'The Tern is guarded - hostiles on approach.' both up"),
    "game_c12_home": ("game", "Helm just after arriving at the Gleaners' home: their station and one fleet close by"),
    "game_c12_fighters": ("game", "The same system a few seconds later: four small fighters launched beside the station, on the radar"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_where": ("card", "table", {"heading": "Step 1 - Where the ships come from", "nth": 1, "kicker": "Three places an enemy ship comes from"}),
    "card_tiers": ("card", "table", {"heading": "Step 1 - Where the ships come from", "nth": 2, "kicker": "Ships in one fleet, by tier"}),
    "card_diff": ("card", "table", {"heading": "Step 2 - The Difficulty number", "nth": 1, "kicker": "What Difficulty does to one enemy system"}),
    "card_four": ("card", "list", {"heading": "Step 3 - Guards with a tier of their own", "kicker": "Four things are true of every guard fleet"}),
    "card_home": ("card", "table", {"heading": "Step 4 - A foe's home", "nth": 1, "kicker": "Ships in a foe's home fleet"}),
    "card_danger": ("card", "table", {"heading": "Step 5 - How thick, and how close", "nth": 1, "kicker": "DANGER: how many systems are enemy systems"}),
    "card_enc": ("card", "table", {"heading": "Step 5 - How thick, and how close", "nth": 2, "kicker": "ENCOUNTERS: where the fleets wait"}),
    "card_gentle": ("card", "rows", {"kicker": "A wrong word is not an error. It is the gentle setting.",
                                     "header": ["You wrote", "What the game does"],
                                     "rows": [['default shared DANGER = "dangerous", in small letters', '"Quiet"'],
                                              ['default shared ENCOUNTERS = "dormant"', '"On Arrival"'],
                                              ['ENCOUNTER for ENCOUNTERS', '"On Arrival"']]}),
    "card_budget": ("card", "table", {"heading": "Step 6 - The ship budget", "nth": 1, "kicker": "The budget: ships at The Bone Pile"}),
    "card_known": ("card", "table", {"heading": "Step 6 - The ship budget", "nth": 2, "kicker": "How many is too many for the game itself?"}),
    "card_eye": ("card", "rows", {"kicker": "Lint cannot see these: check them by eye",
                                  "header": ["Where", "What it must say"],
                                  "rows": [["settings.yaml, line 53", "DIFFICULTY:, a space, and a number from 1 to 11"],
                                           ["story.mast", "The two card lines start at the left edge, in quote marks, with capitals as on the page"],
                                           ["Every Guards: line", "One kind of ship, a space, and at most one whole number from 1 to 11"],
                                           ["After you play", "mast.runtime.log is empty"]]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Count your own universe"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 13", "sub": "A battle that waits for the story"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c12_tern"},
        {"from": 3, "still": "card_where"},
        {"from": 5, "still": "card_budget"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_three_places_the_ships_come_": {"step": 1, "beats": [
        {"from": 0, "still": "card_where"},
        {"from": 1, "still": "card_where", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_where", "marks": [("part", "r1c3")]},
        {"from": 3, "still": "card_where", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_where", "marks": [("part", "r3")]},
        {"from": 5, "still": "e_bone0", "marks": [("lines", _G0, _G0)]},
        {"from": 6, "still": "card_where"},
    ]},
    "s03_fleets_and_tiers": {"step": 1, "beats": [
        {"from": 0, "still": "card_tiers"},
        {"from": 1, "still": "card_tiers", "marks": [("part", "head")]},
        {"from": 2, "still": "card_tiers"},
        {"from": 3, "still": "card_tiers", "marks": [("part", f"r{i}c1") for i in range(1, 7)]},
        {"from": 4, "still": "card_tiers", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_tiers", "marks": [("part", "r1c2"), ("part", "r1c7")]},
        {"from": 6, "still": "card_tiers", "marks": [("part", "r1c12")]},
        {"from": 7, "still": "card_tiers", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_tiers", "marks": [("part", "r1c12")]},
        {"from": 9, "still": "card_tiers", "marks": [("part", "r1c12")]},
    ]},
    "s04_the_difficulty_number": {"step": 2, "beats": [
        {"from": 0, "still": "e_set5"},
        {"from": 1, "still": "e_set5", "marks": [("text", _DIFF, "DIFFICULTY")]},
        {"from": 2, "still": "e_set5", "marks": [("lines", _DIFF, _DIFF)]},
        {"from": 3, "still": "card_diff"},
        {"from": 4, "still": "card_diff", "marks": [("part", "r4")]},
        {"from": 5, "still": "card_diff", "marks": [("part", "r5")]},
        {"from": 6, "still": "card_diff", "marks": [("part", "r6")]},
        {"from": 7, "still": "card_diff"},
        {"from": 8, "still": "card_diff", "marks": [("part", f"r{i}c2") for i in range(1, 7)]},
        {"from": 9, "still": "card_diff", "marks": [("part", f"r{i}c1") for i in range(1, 7)]},
        {"from": 10, "still": "e_set5", "marks": [("lines", _DIFF, _DIFF)]},
        {"from": 11, "still": "e_set4", "marks": [("text", _DIFF, "DIFFICULTY: 4")]},
    ]},
    "s05_guards_with_a_number": {"step": 3, "beats": [
        {"from": 0, "still": "e_bone0", "marks": [("lines", _G0, _G0)]},
        {"from": 1, "still": "e_bone0", "marks": [("text", _G0, "torgoth")]},
        {"from": 2, "still": "e_bone0", "marks": [("lines", _G0, _G0)]},
        {"from": 3, "still": "e_bone7", "marks": [("text", _G7, "torgoth 7")]},
        {"from": 4, "still": "card_tiers", "marks": [("part", "r1c8")]},
        {"from": 5, "still": "e_tern", "marks": [("text", _GT, "Guards: pirate 2")]},
        {"from": 6, "still": "e_tern", "marks": [("lines", _GT, _GT)]},
        {"from": 7, "still": "card_four"},
        {"from": 8, "still": "game_c12_tern"},
        {"from": 9, "still": "card_four", "marks": [("part", "item2")]},
        {"from": 10, "still": "card_four", "marks": [("part", "item3")]},
        {"from": 11, "still": "card_four", "marks": [("part", "item4")]},
    ]},
    "s06_a_foe_s_home": {"step": 4, "beats": [
        {"from": 0, "still": "card_home"},
        {"from": 1, "still": "game_c12_home"},
        {"from": 2, "still": "game_c12_home"},
        {"from": 3, "still": "game_c12_fighters"},
        {"from": 6, "still": "e_gleaners", "marks": [("lines", _GLE_A, _GLE_B)]},
        {"from": 7, "still": "card_home"},
    ]},
    "s07_how_thick_and_how_close": {"step": 5, "beats": [
        {"from": 0, "still": "e_mast0"},
        {"from": 1, "still": "e_mast0", "marks": [("lines", _TR_A, _TR_B)]},
        {"from": 2, "still": "e_mastc", "marks": [("lines", _CARD_A, _EN)]},
        {"from": 3, "still": "e_mastc", "marks": [("text", _DG, '"Quiet"'), ("text", _EN, '"Dormant"')]},
        {"from": 4, "still": "e_mastc", "marks": [("text", _DG, "DANGER")]},
        {"from": 5, "still": "card_danger"},
        {"from": 7, "still": "card_danger", "marks": [("part", "r1c1"), ("part", "r3c1")]},
        {"from": 8, "still": "card_danger", "marks": [("part", "r1c2"), ("part", "r3c2")]},
        {"from": 9, "still": "e_mastc", "marks": [("text", _EN, "ENCOUNTERS")]},
        {"from": 10, "still": "card_enc", "marks": [("part", "r2")]},
        {"from": 11, "still": "card_enc", "marks": [("part", "r2c2")]},
        {"from": 12, "still": "e_mastc", "marks": [("text", _DG, '"Quiet"'), ("text", _EN, '"Dormant"')]},
        {"from": 13, "still": "card_gentle"},
        {"from": 14, "still": "card_gentle", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
    ]},
    "s08_the_budget": {"step": 6, "beats": [
        {"from": 0, "still": "card_budget"},
        {"from": 1, "still": "e_bone7", "marks": [("lines", _PILE, _G7)]},
        {"from": 2, "still": "card_budget", "marks": [("part", "r1c2")]},
        {"from": 3, "still": "card_budget", "marks": [("part", "r2c2"), ("part", "r3c2")]},
        {"from": 4, "still": "card_budget", "marks": [("part", "r3c4")]},
        {"from": 5, "still": "card_known"},
        {"from": 7, "still": "card_known", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_known", "marks": [("part", "r2")]},
        {"from": 10, "still": "card_known", "marks": [("part", "r3")]},
        {"from": 13, "still": "card_known", "marks": [("part", "r4")]},
    ]},
    "s09_check_and_fly_it": {"step": 7, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("span", 1, "0 error(s), 0 warning(s)")]},
        {"from": 1, "still": "e_set4", "marks": [("lines", _DIFF, _DIFF)]},
        {"from": 2, "still": "card_eye"},
        {"from": 3, "still": "t_run", "marks": [("cmd", 1, "server,helm,comms")]},
        {"from": 4, "still": "game_c12_log"},
        {"from": 5, "still": "game_c12_tern"},
        {"from": 6, "still": "game_c12_home"},
        {"from": 7, "still": "game_c12_fighters"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_next"},
    ]},
}
