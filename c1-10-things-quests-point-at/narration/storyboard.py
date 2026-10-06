"""Storyboard for c1-10-things-quests-point-at: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6. Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-05).

The lecture starts from Lecture 9's finished files (its example\\, with no exercise quest
in it: the line numbers 75, 77, 146 and 153 the voice and the tool say need that file line
for line) and ends on its own example\\, both files, byte for byte.
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
    "Kind: wreck",
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
_LOOK = "The hulk is not answering hails. Bring the ship in close and take a look.\n"
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
    "final": {"base": "step", "edits": [("replace", FILE, _CI_THEN, _CI_THEN.replace("salvage/home", "salvage/boat"))],
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
    "e_ci": ("vscode", "start", 63, "big", _NS),            # lines 53 to 73: reach derelict 500
    "e_scans": ("vscode", "start", 107, "big", _NS),        # lines 97 to 117
    "e_scans_mid": ("vscode", "start", 109, "mid", _NS),    # lines 96 to the end: the three records
    # Step 2, typed: every still looks at lines 111 to 131
    "e_b4": ("vscode", "bio4", 121, "big", _NS),
    "e_bio": ("vscode", "bio", 121, "big", _NS),
    # Step 3, typed: lines 123 to 143
    "e_sec": ("vscode", "sec", 133, "big", _NS),
    "e_l1": ("vscode", "boat1", 133, "big", _NS),
    "e_l3": ("vscode", "boat3", 133, "big", _NS),
    "e_l4": ("vscode", "boat4", 133, "big", _NS),
    "e_l5": ("vscode", "boat5", 133, "big", _NS),
    "e_l6": ("vscode", "boat6", 133, "big", _NS),
    "e_words": ("vscode", "words", 12, "big", _NS),         # lines 2 to 22: the word list
    # Step 4: lines 127 to 147, and a longer look that holds the place as well
    "e_ls": ("vscode", "lscan", 137, "big", _NS),
    "e_ls_mid": ("vscode", "lscan", 144, "mid", _NS),
    # Step 5: lines 67 to 87
    "e_st0": ("vscode", "lscan", 77, "big", _NS),
    "e_st": ("vscode", "step", 77, "big", _NS),
    "e_fin_ci": ("vscode", "final", 66, "big", _NS),        # lines 56 to 76
    "e_chain": ("vscode", "final", 72, "mid", _NS),         # lines 58 to 86: the three required steps
    "e_fin": ("vscode", "final", 77, "big", _NS),
    "e_bio_final": ("vscode", "final", 138, "big", _NS),    # lines 128 to 148
    "e_boat": ("vscode", "final", 163, "big", _NS),         # lines 153 to the end
    # Step 6: one mistake at a time
    "e_noroles": ("vscode", "no_roles", 163, "big", _NS),
    "e_tab": ("vscode", "tab_life", 138, "big", _NS),
    "e_plural": ("vscode", "plural", 138, "big", _NS),
    "e_noloc": ("vscode", "no_loc", 163, "big", _NS),
    "e_places": ("vscode", "places", 161, "big", _NS),
    # the Command Prompt: the real tool's answer for that state
    "t_step": ("terminal", [("step", _LINT)]),
    "t_fix": ("terminal", [("step", _LINT), ("final", _LINT)]),
    "t_noroles": ("terminal", [("no_roles", _LINT)]),
    "t_tab": ("terminal", [("tab_life", _LINT)]),
    "t_plural": ("terminal", [("plural", _LINT)]),
    "t_noloc": ("terminal", [("no_loc", _LINT)]),
    "t_places": ("terminal", [("places", _LINT)]),
    # the real game (game.py). All but game_log are from PROBE states: see STATES.
    "game_log": ("game", "Helm, the Quest Log at the start (the page's own files)"),
    "game_helm": ("game", "Helm, the console, 'Quest complete: Quick Work'"),
    "game_hulk": ("game", "The Quest Log: two steps Done, Find the Lifeboat Active"),
    "game_sci_hulk": ("game", "Science, the hulk selected: four tabs, the scan reading"),
    "game_bio": ("game", "Science, the hulk's bio tab: one of the three readings"),
    "game_map": ("game", "Science, the map: the lifeboat is the white icon with no name"),
    "game_boat": ("game", "Science, the lifeboat selected: its scan tab"),
    "game_boat_intel": ("game", "Science, the lifeboat's intel tab before Science scans: Start Intel Scan"),
    "game_boat_scanned": ("game", "Science, the lifeboat's intel tab after the scan"),
    "game_boat_done": ("game", "The Quest Log: Find the Lifeboat Done, Bring the Log Home Active"),
    "game_win": ("game", "Helm, Game results with the Win sentence"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_tabs": ("card", "points", {"kicker": "The five tabs", "items": ["scan", "status", "intel", "mat", "bio"]}),
    "card_rules": ("card", "list", {"heading": "Step 2 - Add a tab of your own", "kicker": "Five rules for scan text"}),
    "card_kind": ("card", "table", {"heading": "Kind", "kicker": "Kind: what sort of thing"}),
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
_READING = ("rect", 0.697, 0.385, 1.0, 0.452)          # Science: the reading
_TABS = ("rect", 0.697, 0.048, 0.94, 0.132)            # Science: the tabs of the selected thing
_BIO_TAB = ("rect", 0.697, 0.088, 0.772, 0.132)
_ICON = ("rect", 0.458, 0.538, 0.505, 0.60)            # Science: the lifeboat on the map
_NAME = ("rect", 0.697, 0.198, 0.80, 0.232)            # Science: "The Lifeboat"
_START = ("rect", 0.697, 0.412, 1.0, 0.458)            # Science: Start Intel Scan
_SENTENCE = ("rect", 0.012, 0.215, 0.25, 0.287)

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_bio", "marks": [_READING]},
        {"from": 1, "still": "e_bio_final", "marks": [("lines", 140, 140)]},
        {"from": 3, "still": "card_title"},
        {"from": 4, "still": "game_boat", "marks": [_READING]},
        {"from": 5, "still": "game_map", "marks": [_ICON]},
    ]},
    "s02_the_idea_point_at_a_role": {"step": None, "beats": [
        {"from": 0, "still": "m_hulk", "marks": [("text", 68, _LIST)]},
        {"from": 1, "still": "m_hulk", "marks": [("text", 68, "ghost_ship")]},
        {"from": 2, "still": "m_hulk", "marks": [("text", 68, _LIST)]},
        {"from": 3, "still": "e_ci", "marks": [("text", 63, "reach derelict 500")]},
        {"from": 4, "still": "e_ci", "marks": [("text", 63, "derelict")]},
        {"from": 6, "still": "e_scans", "marks": [("text", 101, "Scan of: derelict")]},
        {"from": 7, "still": "m_hulk", "marks": [("text", 68, "derelict"), ("text", 68, "ghost_ship")]},
        {"from": 8, "still": "e_boat", "marks": [("lines", 163, 170)]},
        {"from": 9, "still": "e_boat", "marks": [("lines", 166, 166)]},
        {"from": 11, "still": "e_fin", "marks": [("text", 77, "lifeboat")]},
    ]},
    "s03_the_scans_you_have": {"step": 1, "beats": [
        {"from": 0, "still": "e_scans_mid", "marks": [("lines", 99, 99), ("lines", 107, 107), ("lines", 114, 114)]},
        {"from": 1, "still": "e_scans_mid", "marks": [("lines", 99, 105), ("lines", 107, 112)]},
        {"from": 2, "still": "e_scans_mid", "marks": [("lines", 114, 119)]},
        {"from": 3, "still": "e_scans_mid", "marks": [("text", 102, "Tab: scan"), ("text", 110, "Tab: mat")]},
        {"from": 4, "still": "e_scans_mid", "marks": [("text", 116, "Scan of: ghost_ship"), ("text", 117, "Tab: intel")]},
        {"from": 5, "still": "card_tabs"},
        {"from": 7, "still": "e_scans", "marks": [("text", 104, "%"), ("text", 105, "%")]},
        {"from": 8, "still": "e_scans", "marks": [("lines", 104, 105)]},
    ]},
    "s04_a_tab_of_your_own": {"step": 2, "beats": [
        {"from": 0, "still": "e_scans_mid", "marks": [("text", 102, "Tab: scan"), ("text", 110, "Tab: mat"), ("text", 117, "Tab: intel")]},
        {"from": 1, "still": "e_b4", "marks": [("lines", 124, 124)]},
        {"from": 2, "still": "e_b4", "marks": [("lines", 123, 123), ("lines", 124, 124)]},
        {"from": 3, "still": "e_bio", "marks": [("lines", 126, 128)]},
        {"from": 4, "still": "card_rules"},
        {"from": 5, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 8, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 9, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 10, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item5")]},
        {"from": 12, "still": "card_rules", "marks": [("part", "item1"), ("part", "item2"), ("part", "item3"), ("part", "item4")]},
        {"from": 13, "still": "card_rules", "marks": [("part", "item5")]},
    ]},
    "s05_a_place_of_your_own": {"step": 3, "beats": [
        {"from": 0, "still": "m_hulk", "marks": [("lines", 64, 64), ("lines", 68, 68)]},
        {"from": 1, "still": "e_sec", "marks": [("lines", 133, 133)]},
        {"from": 2, "still": "e_sec", "marks": [("hashes", 133)]},
        {"from": 3, "still": "e_sec", "marks": [("text", 133, "(landmarks)")]},
        {"from": 4, "still": "e_l1", "marks": [("lines", 135, 135)]},
        {"from": 5, "still": "e_l1", "marks": [("text", 135, "[The Lifeboat]")]},
        {"from": 6, "still": "e_l3", "marks": [("lines", 137, 137)]},
        {"from": 7, "still": "card_kind"},
        {"from": 8, "still": "e_l4", "marks": [("lines", 138, 138)]},
        {"from": 10, "still": "e_l4", "marks": [("lines", 138, 138)], "dim": True},
        {"from": 12, "still": "e_l5", "marks": [("lines", 139, 139)]},
        {"from": 13, "still": "card_art"},
        {"from": 14, "still": "e_l6", "marks": [("lines", 140, 140)]},
        {"from": 15, "still": "e_l6", "marks": [("text", 140, "6000, 0, 6000")]},
        {"from": 17, "still": "card_loc", "marks": [("part", "r1")]},
        {"from": 18, "still": "card_loc", "marks": [("part", "r2")]},
        {"from": 19, "still": "card_loc"},
        {"from": 20, "still": "card_loc", "marks": [("part", "r3")]},
        {"from": 21, "still": "e_words", "marks": [("lines", 15, 15)]},
    ]},
    "s06_words_for_the_lifeboat": {"step": 4, "beats": [
        {"from": 0, "still": "e_ls", "marks": [("lines", 131, 136), ("lines", 138, 143)]},
        {"from": 1, "still": "e_ls", "marks": [("lines", 133, 133), ("lines", 140, 140)]},
        {"from": 2, "still": "e_ls", "marks": [("lines", 134, 134), ("lines", 141, 141)]},
        {"from": 3, "still": "e_ls_mid", "marks": [("lines", 131, 143), ("lines", 150, 157)]},
        {"from": 5, "still": "e_ls_mid", "marks": [("text", 133, "lifeboat"), ("text", 140, "lifeboat"), ("text", 153, "lifeboat")]},
    ]},
    "s07_point_the_story_at_it": {"step": 5, "beats": [
        {"from": 0, "still": "e_st0", "marks": [("after", 70)]},
        {"from": 1, "still": "e_st", "marks": [("lines", 72, 83)]},
        {"from": 2, "still": "e_st", "marks": [("lines", 75, 75)]},
        {"from": 3, "still": "t_step", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "t_step", "marks": [("span", 1, "waits to be revealed, and nothing reveals it")]},
        {"from": 6, "still": "e_fin_ci", "marks": [("lines", 66, 66)]},
        {"from": 7, "still": "e_fin_ci", "marks": [("text", 66, "salvage/boat")]},
        {"from": 8, "still": "t_fix", "marks": [("part", "run2:clean")]},
        {"from": 8.45, "still": "e_chain", "marks": [("lines", 59, 59), ("lines", 72, 72), ("lines", 85, 85)]},
        {"from": 9, "still": "e_fin", "marks": [("lines", 77, 77)]},
        {"from": 11, "still": "e_fin", "marks": [("text", 77, "reach"), ("text", 77, "lifeboat"), ("text", 77, "500")]},
        {"from": 12, "still": "e_boat", "marks": [("lines", 166, 166)]},
        {"from": 13, "still": "e_boat", "marks": [("text", 163, "(lifeboat)"), ("text", 166, "lifeboat")]},
    ]},
    "s08_lint": {"step": 6, "beats": [
        {"from": 0, "still": "e_boat", "marks": [("lines", 166, 166)]},
        {"from": 1, "still": "e_noroles", "marks": [("after", 165)]},
        {"from": 2, "still": "t_noroles", "marks": [("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 3, "still": "t_noroles", "marks": [("span", 1, "line 77"), ("span", 1, "line 146"), ("span", 1, "line 153")]},
        {"from": 4, "still": "t_noroles", "marks": [("out", 1, 2)], "dim": True},
        {"from": 5, "still": "t_noroles", "marks": [("span", 1, _KEY)]},
        {"from": 6, "still": "t_noroles", "marks": [("span", 1, "`reach` looks for a ROLE")]},
        {"from": 7, "still": "e_noroles", "marks": [("text", 163, "(lifeboat)")]},
        {"from": 8, "still": "e_boat", "marks": [("lines", 166, 166)]},
        {"from": 9, "still": "e_tab", "marks": [("text", 138, "life")]},
        {"from": 9.5, "still": "t_tab", "marks": [("out", 1, 2)]},
        {"from": 10, "still": "e_plural", "marks": [("text", 137, "derelicts")]},
        {"from": 10.5, "still": "t_plural", "marks": [("out", 1, 2)]},
        {"from": 12, "still": "e_noloc", "marks": [("after", 167)]},
        {"from": 12.45, "still": "t_noloc", "marks": [("out", 1, 2)]},
        {"from": 13, "still": "e_places", "marks": [("text", 161, "(places)")]},
        {"from": 14, "still": "t_places", "marks": [("out", 1, 2)]},
        {"from": 16, "still": "card_cannot"},
        {"from": 17, "still": "card_cannot", "marks": [("part", "r1c1")]},
        {"from": 18, "still": "card_cannot", "marks": [("part", "r2c1")]},
        {"from": 19, "still": "card_cannot", "marks": [("part", "r1c1"), ("part", "r2c1")]},
    ]},
    "s09_play_it": {"step": 7, "beats": [
        {"from": 0, "still": "game_log", "marks": [_TWO]},
        {"from": 1, "still": "game_helm"},
        {"from": 2, "still": "game_hulk", "marks": [_ROW1]},
        {"from": 3, "still": "game_sci_hulk", "marks": [_TABS]},
        {"from": 4, "still": "game_bio", "marks": [_BIO_TAB, _READING]},
        {"from": 5, "still": "game_map", "marks": [_ICON]},
        {"from": 7, "still": "game_boat", "marks": [_ICON, _NAME]},
        {"from": 8, "still": "game_boat", "marks": [_READING]},
        {"from": 9, "still": "game_boat_intel", "marks": [_START]},
        {"from": 10, "still": "game_boat_scanned", "marks": [_READING]},
        {"from": 11, "still": "game_boat_done", "marks": [_ROW3]},
        {"from": 12, "still": "game_win", "marks": [_SENTENCE]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 3, "still": "card_next"},
    ]},
}
