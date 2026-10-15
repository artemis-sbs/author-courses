"""Storyboard for c1-10-things-quests-point-at: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6. Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-05).

The lecture starts from Lecture 9's finished files (its example\\, with no exercise quest
in it: the line numbers 89, 93, 162 and 169 the voice and the tool say need that file line
for line) and ends on its own example\\, both files, byte for byte.

2026-10-14 (later): the briefings. Lecture 9's file arrives with Close Inspection's three
paragraphs and the arc's table, and Step 5 now ends with one more line: DS 1's picture at
the top of the arc's briefing, `![](ship://starbase_command) ...` (state "final"; the old
final is "chain"). Line numbers were remapped by matching each old line to its new place,
and every still whose picture changed is new (suffix _p2).
"""
LECTURE = "c1-10-things-quests-point-at"
TITLE = ("Class 1, Lecture 10", "Things quests point at", "Give a thing a role, then point at the role")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_BIO = [
    "### [Derelict Life Signs](derelict_bio)",
    "---",
    "Scan of: derelict",
    "Tab: bio",
    "---",
    "% No life signs. Six suits hang in the airlock, and all six are empty.",
    "% No life signs. The air aboard went bad a long time ago.",
    "% One faint reading aft. It is a plant in a pot, and it is doing fine.",
]
_PLANT = _BIO[-1] + "\n"
_NOTE = ("// ---- Places. Each record is one thing on the map. `Roles:` is the label quests and\n"
         "// scans point at, `Art:` is what it looks like, and `Loc:` is where it sits.\n"
         "## [Landmarks](landmarks)\n")
_BOAT = [
    "### [The Lifeboat](lifeboat)",
    "---",
    "Prefab: wreck",
    "Roles: lifeboat",
    "Art: wreck",
    "Loc: 6000, 0, 6000",
    "---",
    "The hulk's lifeboat. It left her with the flight log aboard.",
]
_GHOST = "// ROLE    ghost_ship        worn by the Unknown Hulk\n"
_WORD = "// ROLE    lifeboat          worn by The Lifeboat, a landmark in this file\n"
_LSCAN = ("\n### [Lifeboat Hull](lifeboat_scan)\n---\nScan of: lifeboat\nTab: scan\n---\n"
          "% A lifeboat, cold and tumbling. The hatch was opened from the inside.\n"
          "\n### [Lifeboat Intel](lifeboat_intel)\n---\nScan of: lifeboat\nTab: intel\n---\n"
          "% The flight log is aboard, sealed in the pilot's locker.\n")
# the LAST line of Close Inspection's description (three paragraphs since Lecture 8)
_LOOK = ("A ship with nobody at the helm is a danger to every lane near the border. If she is empty, DS 1 "
         "needs to know why. If she is not, somebody aboard needs help.\n")
_SHIP = "![](ship://starbase_command) Orders from DS 1, the station you started at.\n\n"
_REACTOR = "---\nThe hulk's reactor is failing."
_STEP = ("\n#### [Find the Lifeboat](boat)\n---\nScope: shared\nStarts when: revealed\n"
         "Objective: Get within 500 of the hulk's lifeboat\nDone when: reach lifeboat 500\n"
         "Reward: 100 credits\nThen: reveal salvage/home\nPart of: salvage\nRequired: true\n---\n"
         "Her log is not aboard, and one lifeboat cradle is empty. Find the boat.\n")
_CI_THEN = "Reward: 100 credits\nThen: reveal salvage/home\nPart of: salvage\nRequired: true\n---\nThe hulk"


def _bio(n):
    return ("append", FILE, "\n" + "\n".join(_BIO[:n]) + "\n")


def _boat(n):
    return ("append", FILE, "\n\n" + _NOTE + ("\n" + "\n".join(_BOAT[:n]) + "\n" if n else ""))


STATES = {
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example")},
    # Step 2: a fourth tab for the hulk
    "bio1": {"base": "start", "edits": [_bio(1)]},
    "bio4": {"base": "start", "edits": [_bio(4)]},
    "bio": {"base": "start", "edits": [_bio(8)]},
    # Step 3: a place
    "sec": {"base": "bio", "edits": [_boat(0)]},
    "boat1": {"base": "bio", "edits": [_boat(1)]},
    "boat3": {"base": "bio", "edits": [_boat(3)]},
    "boat4": {"base": "bio", "edits": [_boat(4)]},
    "boat5": {"base": "bio", "edits": [_boat(5)]},
    "boat6": {"base": "bio", "edits": [_boat(6)]},
    "land": {"base": "bio", "edits": [_boat(8)]},
    "words": {"base": "land", "edits": [("replace", FILE, _GHOST, _GHOST + _WORD)]},
    # Step 4: words for the lifeboat
    "lscan": {"base": "words", "edits": [("replace", FILE, _PLANT, _PLANT + _LSCAN)]},
    # Step 5: the story
    "step": {"base": "lscan", "edits": [("replace", FILE, _LOOK, _LOOK + _STEP)]},
    "chain": {"base": "step", "edits": [("replace", FILE, _CI_THEN, _CI_THEN.replace("salvage/home", "salvage/boat"))]},
    # the end of Step 5: who gives the order, at the top of the arc's briefing
    "final": {"base": "chain", "edits": [("replace", FILE, _REACTOR, "---\n" + _SHIP + "The hulk's reactor is failing.")],
              "same_as": ("c1-10-things-quests-point-at/example/mission.amd",
                          "c1-10-things-quests-point-at/example/story.mast")},
    # Step 6: five mistakes, one at a time
    "no_roles": {"base": "final", "edits": [("replace", FILE, "Roles: lifeboat\n", "")]},
    "tab_life": {"base": "final", "edits": [("replace", FILE, "Tab: bio", "Tab: life")]},
    "plural": {"base": "final", "edits": [("replace", FILE, "Scan of: derelict\nTab: bio", "Scan of: derelicts\nTab: bio")]},
    "no_loc": {"base": "final", "edits": [("replace", FILE, "Loc: 6000, 0, 6000\n", "")]},
    "places": {"base": "final", "edits": [("replace", FILE, "## [Landmarks](landmarks)", "## [Landmarks](places)")]},
    # PROBE-ONLY, for the game stills, so nobody has to fly. Never shown in the editor.
    # "at the hulk": the hulk is spawned 2500 away and the two reach distances widened;
    # the lifeboat is put 1500 off to one side so Science has it in range.
    "g_hulk": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 2500, "Unknown Hulk"'),
        ("replace", FILE, "of the hulk\nDone when: reach derelict 500", "of the hulk\nDone when: reach derelict 30000"),
        ("replace", FILE, "two minutes\nDone when: reach derelict 500", "two minutes\nDone when: reach derelict 30000"),
        ("replace", FILE, "Loc: 6000, 0, 6000", "Loc: 1500, 0, 1500")]},
    "g_boat": {"base": "g_hulk", "edits": [
        ("replace", FILE, "Done when: reach lifeboat 500", "Done when: reach lifeboat 30000")]},
    "g_win": {"base": "g_boat", "edits": [
        ("replace", FILE, "Done when: reach station 1000", "Done when: reach station 30000")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # the script file: line 68, the hulk and its list of roles
    "m_hulk": ("vscode", "start", 68, "mid", _M),
    # the file as Lecture 9 left it
    "e_ci_p2": ("vscode", "start", 71, "big", _NS),            # lines 53 to 73: reach derelict 500
    "e_scans": ("vscode", "start", 121, "big", _NS),        # lines 97 to 117
    "e_scans_mid": ("vscode", "start", 123, "mid", _NS),    # lines 96 to the end: the three records
    # Step 2, typed: every still looks at lines 111 to 131
    "e_b4": ("vscode", "bio4", 135, "big", _NS),
    "e_bio": ("vscode", "bio", 135, "big", _NS),
    # Step 3, typed: lines 123 to 143
    "e_sec": ("vscode", "sec", 147, "big", _NS),
    "e_l1": ("vscode", "boat1", 147, "big", _NS),
    "e_l3": ("vscode", "boat3", 147, "big", _NS),
    "e_l4": ("vscode", "boat4", 147, "big", _NS),
    "e_l5": ("vscode", "boat5", 147, "big", _NS),
    "e_l6": ("vscode", "boat6", 147, "big", _NS),
    "e_words": ("vscode", "words", 12, "big", _NS),         # lines 2 to 22: the word list
    # Step 4: lines 127 to 147, and a longer look that holds the place as well
    "e_ls": ("vscode", "lscan", 151, "big", _NS),
    "e_ls_mid": ("vscode", "lscan", 158, "mid", _NS),
    # Step 5: lines 67 to 87
    "e_st0_p2": ("vscode", "lscan", 91, "big", _NS),
    "e_st_p2": ("vscode", "step", 91, "big", _NS),
    "e_fin_ci_p2": ("vscode", "chain", 74, "big", _NS),        # lines 56 to 76
    "e_chain_p2": ("vscode", "chain", 83, "wide", _NS),        # lines 65 to 101: the three required steps
    "e_fin_p2": ("vscode", "chain", 91, "big", _NS),
    # the end of Step 5: DS 1's picture at the top of the arc's briefing (lines 50 to 70)
    "e_ship0": ("vscode", "chain", 60, "big", _NS),
    "e_ship": ("vscode", "final", 60, "big", _NS),
    "e_bio_final": ("vscode", "final", 154, "big", _NS),    # lines 128 to 148
    "e_boat": ("vscode", "final", 179, "big", _NS),         # lines 153 to the end
    # Step 6: one mistake at a time
    "e_noroles": ("vscode", "no_roles", 179, "big", _NS),
    "e_tab": ("vscode", "tab_life", 154, "big", _NS),
    "e_plural": ("vscode", "plural", 154, "big", _NS),
    "e_noloc": ("vscode", "no_loc", 179, "big", _NS),
    "e_places": ("vscode", "places", 177, "big", _NS),
    # the Command Prompt: the real tool's answer for that state
    "t_step_p2": ("terminal", [("step", _LINT)]),
    "t_fix_p2": ("terminal", [("step", _LINT), ("chain", _LINT)]),
    "t_noroles_p2": ("terminal", [("no_roles", _LINT)]),
    "t_tab_p2": ("terminal", [("tab_life", _LINT)]),
    "t_plural_p2": ("terminal", [("plural", _LINT)]),
    "t_noloc_p2": ("terminal", [("no_loc", _LINT)]),
    "t_places_p2": ("terminal", [("places", _LINT)]),
    # the real game (game.py). All but game_log are from PROBE states: see STATES.
    "game_log": ("game", "Helm, the Quest Log at the start (the page's own files)"),
    # NEW 2026-10-14 (later), taken 2026-10-14: who gives the order
    "game_arc_ship_p2": ("game", "Helm, the Quest Log at the start, the page's own files, Salvage Run selected: at the top of its briefing a small picture of DS 1 (ship://starbase_command) with 'Orders from DS 1, the station you started at.' beside it, then the reactor line and the table"),
    "game_helm": ("game", "Helm, the console, 'Quest complete: Quick Work'"),
    "game_hulk": ("game", "The Quest Log: two steps Done, Find the Lifeboat Active"),
    # Science is the NEW console (2026-10-13): every Science still retaken under a new id
    "game_sci_three_sci2": ("game", "Science (new console), Lecture 9's files: the hulk clicked on the map, its three tab buttons in the lower left under its name - Scan, Intel, Mat"),
    "game_sci_hulk_sci2": ("game", "Science (new console), the hulk clicked on the map: four tab buttons in the lower left under its name - Scan, Intel, Mat, Bio"),
    "game_bio_sci2": ("game", "Science (new console), the hulk's Bio button pressed: the plant-in-a-pot reading in the read-out on the right"),
    "game_map_sci2": ("game", "Science (new console), the map: the lifeboat is the white icon with no name"),
    "game_boat_sci2": ("game", "Science (new console), the lifeboat clicked on the map: buttons Scan and Queue Intel, Scan pressed, its hull line in the read-out"),
    "game_boat_queue_sci2": ("game", "Science (new console), the lifeboat's Queue Intel pressed: the button reads Intel SCANNING with a percentage"),
    "game_boat_scanned_sci2": ("game", "Science (new console), the lifeboat's Intel button after the scan: the flight log line in the read-out"),
    "game_helm_boat": ("game", "Helm, the map: the lifeboat off to one side of the hulk (same probe as the Science shots)"),
    "game_boat_done": ("game", "The Quest Log: Find the Lifeboat Done, Bring the Log Home Active"),
    "game_win": ("game", "Helm, Game results with the Win sentence"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_tabs": ("card", "points", {"kicker": "The five tabs", "items": ["scan", "status", "intel", "mat", "bio"]}),
    "card_rules": ("card", "list", {"heading": "Step 2 - Add a tab of your own", "kicker": "Five rules for scan text"}),
    "card_kind": ("card", "table", {"heading": "Prefab", "kicker": "Prefab: what sort of thing"}),
    "card_art": ("card", "table", {"heading": "Art", "kicker": "Art: what it looks like"}),
    "card_loc": ("card", "table", {"heading": "Loc", "kicker": "Loc: where it sits"}),
    "card_cannot": ("card", "table", {"heading": "What lint cannot see", "kicker": "Lint says clean, and", "rows": (1, 2)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 11", "sub": "Just enough MAST"}),
}

_LIST = "\"tsn, derelict, ghost_ship\""
_KEY = "`lifeboat` is the KEY of the landmark `The Lifeboat`"
# on the game's windows (fractions of the 4:3 picture); set from the screenshots
_TWO = ("rect", 0.02, 0.365, 0.38, 0.50)               # game_log: the two steps showing
_ROW1 = ("rect", 0.02, 0.362, 0.38, 0.432)             # the first step row under Salvage Run
_ROW3 = ("rect", 0.02, 0.505, 0.38, 0.572)             # the third
_MSG = ("rect", 0.015, 0.488, 0.275, 0.528)
# the NEW Science console (the _sci2 stills) and Helm's map
_THREE_BTNS = ("rect", 0.007, 0.722, 0.286, 0.84)      # game_sci_three_sci2: Scan, Intel, Mat
_HULK_STACK = ("rect", 0.005, 0.655, 0.288, 0.882)      # game_sci_hulk_sci2 / game_bio_sci2: the name and five buttons
_BIO = ("rect", 0.007, 0.8, 0.286, 0.84)               # the Bio button
_BIO_READ = ("rect", 0.697, 0.15, 0.96, 0.222)         # game_bio_sci2: the Bio reading in the read-out
_MAP_BOAT = ("rect", 0.462, 0.375, 0.505, 0.435)       # game_map_sci2: the lifeboat's white icon, no name
_BOAT_TITLE = [("rect", 0.697, 0.06, 0.862, 0.096), ("rect", 0.005, 0.728, 0.1, 0.757)]  # The Lifeboat: read-out title, stack name
_BOAT_BTNS = ("rect", 0.007, 0.761, 0.286, 0.84)       # the lifeboat's Scan and (Queue) Intel
_BOAT_SCAN = ("rect", 0.007, 0.761, 0.286, 0.8)        # Scan
_BOAT_INTEL = ("rect", 0.007, 0.8, 0.286, 0.84)        # Queue Intel, then Intel
_BOAT_READ = ("rect", 0.697, 0.155, 0.998, 0.218)      # the lifeboat's line in the read-out
_HELM_BOAT = ("rect", 0.598, 0.405, 0.67, 0.515)       # game_helm_boat: the lifeboat on Helm's map
_SENTENCE = ("rect", 0.012, 0.215, 0.25, 0.287)
_SHIP_ROW = ("rect", 0.385, 0.075, 0.82, 0.175)         # game_arc_ship_p2: DS 1's picture and its words
_ARC_ROW = ("rect", 0.0, 0.36, 0.38, 0.43)              # game_arc_ship_p2: Salvage Run, selected

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_bio_sci2"},
        {"from": 1, "still": "game_bio_sci2", "marks": [_BIO]},
        {"from": 2, "still": "game_bio_sci2", "marks": [_BIO_READ]},
        {"from": 3, "still": "e_bio_final", "marks": [("lines", 156, 156)]},
        {"from": 5, "still": "card_title"},
        {"from": 6, "still": "game_boat_sci2", "marks": [_BOAT_READ]},
        {"from": 7, "still": "game_map_sci2", "marks": [_MAP_BOAT]},
    ]},
    "s02_the_idea_point_at_a_role": {"step": None, "beats": [
        {"from": 0, "still": "m_hulk", "marks": [("text", 68, _LIST)]},
        {"from": 1, "still": "m_hulk", "marks": [("text", 68, "ghost_ship")]},
        {"from": 2, "still": "m_hulk", "marks": [("text", 68, _LIST)]},
        {"from": 3, "still": "e_ci_p2", "marks": [("text", 71, "reach derelict 500")]},
        {"from": 4, "still": "e_ci_p2", "marks": [("text", 71, "derelict")]},
        {"from": 6, "still": "e_scans", "marks": [("text", 115, "Scan of: derelict")]},
        {"from": 7, "still": "m_hulk", "marks": [("text", 68, "derelict"), ("text", 68, "ghost_ship")]},
        {"from": 8, "still": "e_boat", "marks": [("lines", 179, 186)]},
        {"from": 9, "still": "e_boat", "marks": [("lines", 182, 182)]},
        {"from": 11, "still": "e_fin_p2", "marks": [("text", 91, "lifeboat")]},
    ]},
    "s03_the_scans_you_have": {"step": 1, "beats": [
        {"from": 0, "still": "game_sci_three_sci2"},
        {"from": 1, "still": "game_sci_three_sci2", "marks": [_THREE_BTNS]},
        {"from": 2, "still": "e_scans_mid", "marks": [("lines", 113, 113), ("lines", 121, 121), ("lines", 128, 128)]},
        {"from": 3, "still": "e_scans_mid", "marks": [("lines", 113, 119), ("lines", 121, 126)]},
        {"from": 4, "still": "e_scans_mid", "marks": [("lines", 128, 133)]},
        {"from": 5, "still": "e_scans_mid", "marks": [("text", 116, "Tab: scan"), ("text", 124, "Tab: mat")]},
        {"from": 6, "still": "e_scans_mid", "marks": [("text", 130, "Scan of: ghost_ship"), ("text", 131, "Tab: intel")]},
        {"from": 7, "still": "card_tabs"},
        {"from": 9, "still": "e_scans", "marks": [("text", 118, "%"), ("text", 119, "%")]},
        {"from": 10, "still": "e_scans", "marks": [("lines", 118, 119)]},
    ]},
    "s04_a_tab_of_your_own": {"step": 2, "beats": [
        {"from": 0, "still": "e_scans_mid", "marks": [("text", 116, "Tab: scan"), ("text", 124, "Tab: mat"), ("text", 131, "Tab: intel")]},
        {"from": 1, "still": "e_b4", "marks": [("lines", 138, 138)]},
        {"from": 2, "still": "e_b4", "marks": [("lines", 137, 137), ("lines", 138, 138)]},
        {"from": 3, "still": "e_bio", "marks": [("lines", 140, 142)]},
        {"from": 4, "still": "game_bio_sci2", "marks": [_BIO]},
        {"from": 5, "still": "game_bio_sci2", "marks": [_BIO_READ]},
        {"from": 6, "still": "card_rules"},
        {"from": 7, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 10, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 12, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 13, "still": "card_rules", "marks": [("part", "item5")]},
        {"from": 14, "still": "card_rules", "marks": [("part", "item1"), ("part", "item2"), ("part", "item3"), ("part", "item4")]},
        {"from": 15, "still": "card_rules", "marks": [("part", "item5")]},
    ]},
    "s05_a_place_of_your_own": {"step": 3, "beats": [
        {"from": 0, "still": "m_hulk", "marks": [("lines", 64, 64), ("lines", 68, 68)]},
        {"from": 1, "still": "e_sec", "marks": [("lines", 147, 147)]},
        {"from": 2, "still": "game_helm_boat", "marks": [_HELM_BOAT]},
        {"from": 4, "still": "e_sec", "marks": [("hashes", 147)]},
        {"from": 5, "still": "e_sec", "marks": [("text", 147, "(landmarks)")]},
        {"from": 6, "still": "e_l1", "marks": [("lines", 149, 149)]},
        {"from": 7, "still": "e_l1", "marks": [("text", 149, "[The Lifeboat]")]},
        {"from": 8, "still": "game_boat_sci2", "marks": [_BOAT_READ]},
        {"from": 9, "still": "e_l3", "marks": [("lines", 151, 151)]},
        {"from": 10, "still": "card_kind"},
        {"from": 11, "still": "e_l4", "marks": [("lines", 152, 152)]},
        {"from": 13, "still": "e_l4", "marks": [("lines", 152, 152)], "dim": True},
        {"from": 15, "still": "e_l5", "marks": [("lines", 153, 153)]},
        {"from": 16, "still": "card_art"},
        {"from": 17, "still": "e_l6", "marks": [("lines", 154, 154)]},
        {"from": 18, "still": "e_l6", "marks": [("text", 154, "6000, 0, 6000")]},
        {"from": 20, "still": "card_loc", "marks": [("part", "r1")]},
        {"from": 21, "still": "card_loc", "marks": [("part", "r2")]},
        {"from": 22, "still": "card_loc"},
        {"from": 23, "still": "card_loc", "marks": [("part", "r3")]},
        {"from": 24, "still": "game_helm_boat", "marks": [_HELM_BOAT]},
        {"from": 25, "still": "e_words", "marks": [("lines", 15, 15)]},
    ]},
    "s06_words_for_the_lifeboat": {"step": 4, "beats": [
        {"from": 0, "still": "game_boat_sci2", "marks": _BOAT_TITLE},
        {"from": 1, "still": "game_boat_sci2", "marks": [_BOAT_BTNS]},
        {"from": 2, "still": "e_ls", "marks": [("lines", 145, 150), ("lines", 152, 157)]},
        {"from": 4, "still": "e_ls", "marks": [("lines", 147, 147), ("lines", 154, 154)]},
        {"from": 5, "still": "e_ls", "marks": [("lines", 148, 148), ("lines", 155, 155)]},
        {"from": 6, "still": "e_ls_mid", "marks": [("lines", 145, 157), ("lines", 164, 171)]},
        {"from": 8, "still": "e_ls_mid", "marks": [("text", 147, "lifeboat"), ("text", 154, "lifeboat"), ("text", 167, "lifeboat")]},
    ]},
    "s07_point_the_story_at_it": {"step": 5, "beats": [
        {"from": 0, "still": "e_st0_p2", "marks": [("lines", 85, 85)]},
        {"from": 1, "still": "e_st_p2", "marks": [("lines", 86, 97)]},
        {"from": 2, "still": "e_st_p2", "marks": [("lines", 89, 89)]},
        {"from": 3, "still": "t_step_p2", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "t_step_p2", "marks": [("span", 1, "waits to be revealed, and nothing reveals it")]},
        {"from": 6, "still": "e_fin_ci_p2", "marks": [("lines", 74, 74)]},
        {"from": 7, "still": "e_fin_ci_p2", "marks": [("text", 74, "salvage/boat")]},
        {"from": 8, "still": "t_fix_p2", "marks": [("part", "run2:clean")]},
        {"from": 8.45, "still": "e_chain_p2", "marks": [("lines", 67, 67), ("lines", 86, 86), ("lines", 99, 99)]},
        {"from": 9, "still": "e_fin_p2", "marks": [("lines", 91, 91)]},
        {"from": 11, "still": "e_fin_p2", "marks": [("text", 91, "reach"), ("text", 91, "lifeboat"), ("text", 91, "500")]},
        {"from": 12, "still": "e_boat", "marks": [("lines", 182, 182)]},
        {"from": 13, "still": "game_boat_sci2", "marks": _BOAT_TITLE},
        {"from": 14, "still": "e_boat", "marks": [("text", 179, "(lifeboat)"), ("text", 182, "lifeboat")]},
        # who gives the order: the game first, then the line
        {"from": 16, "still": "game_arc_ship_p2"},
        {"from": 17, "still": "game_arc_ship_p2", "marks": [_ARC_ROW]},
        {"from": 18, "still": "game_arc_ship_p2", "marks": [_SHIP_ROW]},
        {"from": 20, "still": "e_ship0", "marks": [("lines", 57, 57)]},
        {"from": 21, "still": "e_ship", "marks": [("text", 57, "![]")]},
        {"from": 22, "still": "e_ship", "marks": [("text", 57, "(ship://starbase_command)")]},
        {"from": 23, "still": "e_ship", "marks": [("text", 57, "starbase_command")]},
    ]},
    "s08_lint": {"step": 6, "beats": [
        {"from": 0, "still": "e_boat", "marks": [("lines", 182, 182)]},
        {"from": 1, "still": "e_noroles", "marks": [("after", 181)]},
        {"from": 2, "still": "t_noroles_p2", "marks": [("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 3, "still": "t_noroles_p2", "marks": [("span", 1, "line 93"), ("span", 1, "line 162"), ("span", 1, "line 169")]},
        {"from": 4, "still": "t_noroles_p2", "marks": [("out", 1, 2)], "dim": True},
        {"from": 5, "still": "t_noroles_p2", "marks": [("span", 1, _KEY)]},
        {"from": 6, "still": "t_noroles_p2", "marks": [("span", 1, "`reach` looks for a ROLE")]},
        {"from": 7, "still": "e_noroles", "marks": [("text", 179, "(lifeboat)")]},
        {"from": 8, "still": "e_boat", "marks": [("lines", 182, 182)]},
        {"from": 9, "still": "e_tab", "marks": [("text", 154, "life")]},
        {"from": 9.5, "still": "t_tab_p2", "marks": [("out", 1, 2)]},
        {"from": 10, "still": "e_plural", "marks": [("text", 153, "derelicts")]},
        {"from": 10.5, "still": "t_plural_p2", "marks": [("out", 1, 2)]},
        {"from": 12, "still": "e_noloc", "marks": [("after", 183)]},
        {"from": 12.45, "still": "t_noloc_p2", "marks": [("out", 1, 2)]},
        {"from": 13, "still": "e_places", "marks": [("text", 177, "(places)")]},
        {"from": 14, "still": "t_places_p2", "marks": [("out", 1, 2)]},
        {"from": 16, "still": "card_cannot"},
        {"from": 17, "still": "card_cannot", "marks": [("part", "r1c1")]},
        {"from": 18, "still": "card_cannot", "marks": [("part", "r2c1")]},
        {"from": 19, "still": "card_cannot", "marks": [("part", "r1c1"), ("part", "r2c1")]},
    ]},
    "s09_play_it": {"step": 7, "beats": [
        {"from": 0, "still": "game_log", "marks": [_TWO]},
        {"from": 1, "still": "game_arc_ship_p2", "marks": [_SHIP_ROW]},
        {"from": 2, "still": "game_helm"},
        {"from": 3, "still": "game_hulk", "marks": [_ROW1]},
        {"from": 4, "still": "game_sci_hulk_sci2", "marks": [_HULK_STACK]},
        {"from": 5, "still": "game_bio_sci2", "marks": [_BIO, _BIO_READ]},
        {"from": 7, "still": "game_helm_boat", "marks": [_HELM_BOAT]},
        {"from": 9, "still": "game_map_sci2", "marks": [_MAP_BOAT]},
        {"from": 10, "still": "game_boat_sci2", "marks": [_BOAT_SCAN, _BOAT_READ]},
        {"from": 11, "still": "game_boat_sci2", "marks": [_BOAT_INTEL]},
        {"from": 13, "still": "game_boat_queue_sci2", "marks": [_BOAT_INTEL]},
        {"from": 14, "still": "game_boat_scanned_sci2", "marks": [_BOAT_INTEL, _BOAT_READ]},
        {"from": 15, "still": "game_boat_done", "marks": [_ROW3]},
        {"from": 16, "still": "game_win"},
        {"from": 17, "still": "game_win", "marks": [_SENTENCE]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 3, "still": "card_next"},
    ]},
}
