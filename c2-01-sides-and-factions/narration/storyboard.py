"""Storyboard for c2-01-sides-and-factions: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Class 1 Lecture 11's finished mission.amd and story.mast plus the
other five files of Lecture 3's example\\ ("start", seven files; Lecture 12's renamed
Lantern story is NOT the start: the page says "as Lecture 11 left it"). The records are
typed one step at a time and end on this lecture's own example\\, both files ("final").

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. Each
note says which state to start (`python game.py c2-01-sides-and-factions start --state
<state> --consoles server,helm,science,comms`) and what to click. The g_ states are
PROBE-ONLY (never shown in the editor): they bring the cutter and the yard close to the
ship, or start a step at once, so nobody has to fly or play the whole story.
Science is the NEW console: pick a contact from the contact list on the right (far
contacts are off the map), press its Queue Scan button in the tab stack at the lower left,
wait for the scan; the read-out's title (top right) is the name in the relation's color
with the side's key at its right in the side's own color.
"""
LECTURE = "c2-01-sides-and-factions"
TITLE = ("Class 2, Lecture 1", "Sides and factions", "Who is whose enemy")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_LIFEBOAT_END = "The hulk's lifeboat. It left her with the flight log aboard.\n"
_SIDES_HEAD = ("\n\n// ---- Sides. Each record is one faction: its name, its color, and who it fights or\n"
               "// stands with. `Side:` on a landmark names one of these keys.\n"
               "## [Sides](sides)\n\n")
_TSN = "### [TSN](tsn)\n---\nColor: #07F\n---\nThe Terran Stellar Navy. The crew's own side.\n"
_BREAKERS = ("\n### [The Breakers](breaker)\n---\nColor: #F80\nEnemies: tsn\n---\n"
             "Scavengers. They strip dead ships, and they do not wait for the paperwork.\n")
_GUILD = ("\n### [Harbor Guild](guild)\n---\nColor: #0C6\nAllies: tsn\n---\n"
          "The pilots and tug crews who work the lanes around DS 1.\n")
_CUTTER = ("\n### [Breaker Cutter](cutter)\n---\nPrefab: ship\nSide: breaker\nRoles: cutter\n"
           "Art: pirate_strongbow\nLoc: 3000, 0, 11000\n---\n"
           "A Breaker ship, standing off until the hulk goes quiet.\n")
_YARD = ("\n### [Guild Yard](guild_yard)\n---\nPrefab: station\nSide: guild\nRoles: yard\n"
         "Art: starbase_civil\nLoc: -6000, 0, 3000\n---\nThe Harbor Guild's repair yard.\n")
_WORDS_AT = "// ROLE    tug               worn by the Salvage Tug, once it arrives\n"
_WORDS = ("// ROLE    home              worn by DS 1, and by nothing else\n"
          "// ROLE    cutter            worn by the Breaker Cutter, a landmark in this file\n"
          "// ROLE    yard              worn by the Guild Yard, a landmark in this file\n")
_DS1 = '"DS 1", "tsn, station"'
_EX = "c2-01-sides-and-factions/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example")},
    # Step 2: the section and the crew's own side
    "s_tsn": {"base": "start", "edits": [("append", FILE, _SIDES_HEAD + _TSN)]},
    # Step 3: two more sides
    "s_three": {"base": "s_tsn", "edits": [("append", FILE, _BREAKERS + _GUILD)]},
    # Step 4: one thing on each side, in the Landmarks section, above the Sides note
    "s_land": {"base": "s_three", "edits": [("replace", FILE, _LIFEBOAT_END, _LIFEBOAT_END + _CUTTER + _YARD)]},
    # Step 5: the step first (lint warns), then DS 1's word
    "s_half": {"base": "s_land", "edits": [("replace", FILE, "Done when: reach station 1000", "Done when: reach home 1000")]},
    "s_home": {"base": "s_half", "edits": [("replace", MAST, _DS1, '"DS 1", "tsn, station, home"')]},
    # Step 6: the Breakers and the Guild
    "s_guild": {"base": "s_home", "edits": [("replace", FILE, "Enemies: tsn\n", "Enemies: tsn, guild\n")]},
    # Step 7: the word list, and the page's own files
    "final": {"base": "s_guild", "edits": [("replace", FILE, _WORDS_AT, _WORDS_AT + _WORDS)],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    # Scene 8: three breaks, each on the finished files
    "b_tsm": {"base": "final", "edits": [("replace", FILE, "Enemies: tsn, guild", "Enemies: tsm")]},
    "b_noside": {"base": "final", "edits": [("replace", FILE, "Prefab: ship\nSide: breaker\n", "Prefab: ship\n")]},
    "b_hash4": {"base": "final", "edits": [("replace", FILE, "### [Harbor Guild](guild)", "#### [Harbor Guild](guild)")]},
    # PROBE-ONLY, for the game stills. Never shown in the editor.
    # The cutter 2500 ahead of the ship and the yard 1500 off to one side, so both are
    # in sensor range and on the map at once. Names, sides and sentences are the page's.
    "g_near": {"base": "final", "edits": [
        ("replace", FILE, "Loc: 3000, 0, 11000", "Loc: 1500, 0, 2500"),
        ("replace", FILE, "Loc: -6000, 0, 3000", "Loc: -1500, 0, 1500")]},
    # ... the same, with no Side: line on the cutter (scene 8)
    "g_noside": {"base": "g_near", "edits": [("replace", FILE, "Prefab: ship\nSide: breaker\n", "Prefab: ship\n")]},
    # Bring the Log Home Active from the start, and out of reach, so the Quest Log can show it
    "g_home": {"base": "final", "edits": [
        ("replace", FILE, "Starts when: revealed\nObjective: Return to within 1000 of DS 1\nDone when: reach home 1000",
         "Starts when: at once\nObjective: Return to within 1000 of DS 1\nDone when: reach home 5")]},
    # every step done at once, so the game ends on the Win sentence (the hulk scan still
    # needs Science: pick the hulk, Queue Scan)
    "g_win": {"base": "final", "edits": [
        ("replace", FILE, "Done when: reach derelict 500\nReward: 100", "Done when: reach derelict 30000\nReward: 100"),
        ("replace", FILE, "Done when: reach lifeboat 500", "Done when: reach lifeboat 30000"),
        ("replace", FILE, "Done when: reach home 1000", "Done when: reach home 30000")]},
}

# PROBE-ONLY state for game_log_yard: g_near with Bring the Log Home Active from the start
STATES["g_yard"] = {"base": "g_near", "edits": [
    ("replace", FILE, "Starts when: revealed\nObjective: Return to within 1000 of DS 1",
     "Starts when: at once\nObjective: Return to within 1000 of DS 1")]}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # story.mast as Class 1 left it: the side, the three spawn lines, the Sides line
    "m_side": ("vscode", "start", 20, "big", _M),          # lines 10 to 30
    "m_spawn": ("vscode", "start", 66, "mid", _M),         # lines 52 to 80: DS 1 and the hulk
    "m_tug": ("vscode", "start", 110, "big", _M),          # lines 100 to 120: the tug
    "m_44": ("vscode", "start", 44, "big", _M),
    # Step 2: the end of the file, then the section and the TSN record
    "e_end0": ("vscode", "start", 192, "big", _NS),
    "e_tsn": ("vscode", "s_tsn", 206, "big", _NS),         # lines 196 to 216
    # Step 3: the Breakers and the Guild (lines 202 to 230)
    "e_three": ("vscode", "s_three", 216, "mid", _NS),
    # Step 4: the cutter and the yard, above the Sides note
    "e_land": ("vscode", "s_land", 212, "mid", _NS),       # lines 198 to 226
    "e_land_w": ("vscode", "s_land", 210, "wide", _NS),    # lines 192 to 228: both section headings
    # Step 5: the step, then DS 1's line
    "e_half0": ("vscode", "s_land", 121, "big", _NS),
    "e_half": ("vscode", "s_half", 121, "big", _NS),
    "m_half": ("vscode", "s_half", 64, "big", _M),
    "m_home": ("vscode", "s_home", 64, "big", _M),
    # Step 6: the Breakers' relation line
    "e_guild0": ("vscode", "s_home", 237, "big", _NS),
    "e_guild": ("vscode", "s_guild", 237, "big", _NS),
    # the finished Sides section, and the three breaks
    "e_sides": ("vscode", "final", 240, "big", _NS),       # lines 230 to 250
    "e_sides_w": ("vscode", "final", 238, "wide", _NS),    # lines 220 to 256
    "e_cutter": ("vscode", "final", 212, "big", _NS),      # lines 202 to 222
    "e_tsm": ("vscode", "b_tsm", 240, "big", _NS),
    "e_noside": ("vscode", "b_noside", 211, "big", _NS),
    "e_hash4": ("vscode", "b_hash4", 240, "big", _NS),
    # the Command Prompt
    "t_tsn": ("terminal", [("s_tsn", _LINT)]),
    "t_land": ("terminal", [("s_land", _LINT)]),
    "t_half": ("terminal", [("s_half", _LINT)]),
    "t_home": ("terminal", [("s_half", _LINT), ("s_home", _LINT)]),
    "t_tsm": ("terminal", [("b_tsm", _LINT)]),
    "t_noside": ("terminal", [("b_noside", _LINT)]),
    "t_hash4": ("terminal", [("b_noside", _LINT), ("b_hash4", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). `game.py c2-01-sides-and-factions start --state <s>
    # --consoles server,helm,science,comms`. Science is the NEW console (see the docstring).
    "game_sci_ds1_sci2": ("game", "Science, NEW console. State final. Pick DS 1 from the contact list, press Queue Scan in the tab stack at the lower left, wait until Scan is a plain tab. On screen: the read-out's title, DS 1 in green with the word tsn at its right in blue (#07F), and the stock station reading under it"),
    "game_sci_cutter_sci2": ("game", "Science, NEW console. State g_near (the cutter 2500 from the ship). Pick Breaker Cutter from the contact list, press Queue Scan, wait. On screen: the title Breaker Cutter in red, the word breaker at its right in orange (#F80), and 'Enemy vessel. Exercise caution.' in the read-out"),
    "game_sci_yard_sci2": ("game", "Science, NEW console. State g_near. Pick Guild Yard from the contact list, press Queue Scan, wait. On screen: the title Guild Yard in green, the word guild at its right in green (#0C6), and 'This is a friendly station.' in the read-out"),
    "game_sci_noside_sci2": ("game", "Science, NEW console. State g_noside (the cutter has no Side: line). Pick Breaker Cutter from the contact list (press Queue Scan if the stack offers it, and wait). On screen: the title still reads unknown, no side word"),
    "game_helm_map": ("game", "Helm, the 2D map zoomed out far enough to hold all of it. State final, at the start. On screen: DS 1 and the hulk, the Breaker Cutter in RED beyond the hulk (3000, 0, 11000), the Guild Yard in BLUE to the west of DS 1 (-6000, 0, 3000), the crew's ship in green"),
    "game_helm_dock": ("game", "Helm, docked at the Guild Yard. State g_near. Science scans the yard first; on Helm fly inside 600 of the Guild Yard and dock. On screen: Helm showing the ship docked at the yard"),
    "game_helm_cutter": ("game", "Helm, the ship held about 400 from the Breaker Cutter for ten seconds. State g_near. On screen: the cutter red and still on the map, no shots, the ship's shields untouched"),
    "game_log_home": ("game", "Helm, the ePADD Quest Log (the handheld icon top left, then Quests). State g_home (Bring the Log Home starts at once). Bring the Log Home selected: Active, and its order 'Return to within 1000 of DS 1' in the pane"),
    "game_log_yard": ("game", "Helm beside the Guild Yard with the Quest Log open. State g_yard (Bring the Log Home Active from the start, the yard close). Fly inside 1000 of the Guild Yard, open the ePADD Quest Log: Bring the Log Home is still Active"),
    "game_comms_cutter": ("game", "Comms. State g_near. Science scans the Breaker Cutter first (Comms will not open on a contact Science has no data for); then on Comms select the cutter. On screen: its buttons Hail, Taunt and Surrender now"),
    "game_comms_cutter_hail": ("game", "Comms, as game_comms_cutter, after pressing Hail: 'Go away, Artemis! You talk too much!'"),
    "game_comms_yard": ("game", "Comms. State g_near. Science scans the Guild Yard first; then on Comms select the yard. On screen: its buttons Hail, Build Weapons and Request Priority Docking"),
    "game_comms_yard_hail": ("game", "Comms, as game_comms_yard, after pressing Hail: 'Hello, Artemis. We stand ready to assist', the shield and hull figures, and 'You have full docking privileges.'"),
    "game_win": ("game", "Helm, the Game results screen with the Win sentence 'The log is home. DS 1 knows what happened out there.' State g_win (every reach widened): Science scans the hulk (pick it, Queue Scan), the tug arrives 20 s later, and the story ends"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_color": ("card", "table", {"heading": "The color", "kicker": "A hash sign and three characters: red, green, blue"}),
    "card_pairs": ("card", "table", {"heading": "Step 6 - Who is what to whom", "kicker": "Three sides, three pairs"}),
    "card_rel": ("card", "table", {"heading": "What a relation does in the game", "kicker": "What the crew meets"}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (2, 5, 1)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A faction of your own"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 2", "sub": "Characters and faces"}),
}

# Line numbers below are the states': before Step 7 (s_tsn to s_guild) the Sides section
# sits three lines higher than in the finished file.
_TSN_REC = ("lines", 208, 212)
_SIDES_FINAL = [("lines", 231, 235), ("lines", 237, 242), ("lines", 244, 249)]

# Marks on the game stills (fractions of the 1280x960 frame), set from the screenshots 2026-10-15.
_SCI_NAME = ("rect", 0.695, 0.055, 0.9, 0.1)          # Science read-out title: the name
_SCI_SIDE = ("rect", 0.9, 0.055, 1.0, 0.1)            # ... the side's key at its right
_SCI_TITLE = ("rect", 0.695, 0.055, 1.0, 0.1)         # ... both
_SCI_ENEMY = ("rect", 0.695, 0.245, 0.92, 0.282)      # 'Enemy vessel. Exercise caution.'
_SCI_FRIEND = ("rect", 0.695, 0.208, 0.88, 0.243)     # 'This is a friendly station.'
_SCI_TABS = ("rect", 0.005, 0.68, 0.29, 0.84)         # tab stack: Scan, Status, Intel, Bio (no Queue)
_SCI_DS1_MAP = ("rect", 0.405, 0.42, 0.49, 0.53)      # game_sci_ds1_sci2: DS 1 on the map
_SCI_UNKNOWN = ("rect", 0.695, 0.055, 0.83, 0.1)      # game_sci_noside_sci2: unknown
_SCI_QUEUE = ("rect", 0.005, 0.8, 0.29, 0.84)         # ... Queue Scan still offered
_SCI_THREATS0 = ("rect", 0.14, 0.935, 0.285, 0.995)   # ... Threats 0
_HM_ALL = ("rect", 0.36, 0.38, 0.6, 0.63)             # game_helm_map: the contacts around the ship
_HM_CUTTER = ("rect", 0.455, 0.39, 0.53, 0.48)        # ... the cutter, grey, 11K
_HM_YARD = ("rect", 0.37, 0.485, 0.44, 0.585)         # ... the Guild Yard, blue
_HD_DOCKED = ("rect", 0.0, 0.49, 0.15, 0.525)         # game_helm_dock: 'Docked at Guild Yard.'
_HD_STATE = ("rect", 0.13, 0.148, 0.27, 0.175)        # ... State docked
_HD_RELEASE = ("rect", 0.77, 0.455, 1.0, 0.522)       # ... RELEASE DOCK
_HC_CUTTER = ("rect", 0.44, 0.54, 0.54, 0.65)         # game_helm_cutter: the cutter, red, 191 off
_HC_SHIELDS = ("rect", 0.12, 0.175, 0.27, 0.226)      # ... shields 120 / 120
_QL_ROW = ("rect", 0.025, 0.43, 0.38, 0.503)          # Quest Log: Bring the Log Home, Active
_QL_ORDER = ("rect", 0.385, 0.075, 0.72, 0.19)        # ... State, Reward and the order
_CC_BUTTONS = ("rect", 0.625, 0.555, 1.0, 0.795)      # Comms, cutter: Hail, Taunt, Surrender now
_CY_BUTTONS = ("rect", 0.272, 0.517, 0.66, 0.832)     # Comms, yard: Hail ... Market
_CY_HAIL = ("rect", 0.312, 0.517, 0.66, 0.597)        # ... the Hail button
_C_HEADER = ("rect", 0.27, 0.048, 0.512, 0.1)         # the message header in the list (top middle)
_CC_TEXT = ("rect", 0.508, 0.23, 1.0, 0.35)           # the cutter's answer, once the header is clicked
_CY_TEXT = ("rect", 0.508, 0.05, 1.0, 0.35)           # the yard's answer
_WIN = ("rect", 0.015, 0.215, 0.235, 0.285)           # game_win: the Win sentence

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_helm_map", "marks": [_HM_ALL]},
        {"from": 1, "still": "card_title"},
        {"from": 2, "still": "game_sci_cutter_sci2", "marks": [_SCI_TITLE]},
        {"from": 3, "still": "game_sci_yard_sci2", "marks": [_SCI_TITLE]},
        {"from": 4, "still": "e_sides_w", "marks": _SIDES_FINAL},
        {"from": 5, "still": "e_sides_w", "marks": [("lines", 240, 240)]},
    ]},
    "s02_the_side_you_already_have": {"step": 1, "beats": [
        # the game first: DS 1 on Science, its side word
        {"from": 0, "still": "game_sci_ds1_sci2", "marks": [_SCI_DS1_MAP]},
        {"from": 1, "still": "game_sci_ds1_sci2", "marks": [_SCI_NAME]},
        {"from": 2, "still": "game_sci_ds1_sci2", "marks": [_SCI_SIDE]},
        {"from": 3, "still": "m_side", "marks": [("lines", 18, 20)]},
        {"from": 4, "still": "m_side", "marks": [("text", 18, "\"key\":\"tsn\"")]},
        {"from": 5, "still": "m_side", "marks": [("lines", 19, 20)]},
        {"from": 6, "still": "m_spawn"},
        {"from": 7, "still": "m_spawn", "marks": [("text", 64, "tsn")]},
        {"from": 8, "still": "m_spawn", "marks": [("text", 68, "tsn")]},
        {"from": 9, "still": "m_tug", "marks": [("text", 113, "tsn")]},
        {"from": 10, "still": "m_spawn", "marks": [("text", 64, "tsn"), ("text", 68, "tsn")]},
        {"from": 11, "still": "m_spawn", "marks": [("text", 64, "station"), ("text", 68, "derelict, ghost_ship")]},
        {"from": 12, "still": "game_sci_ds1_sci2", "marks": [_SCI_SIDE]},
        {"from": 14, "still": "m_44"},
        {"from": 15, "still": "m_44", "marks": [("lines", 44, 44)]},
        {"from": 16, "still": "m_44", "marks": [("text", 44, "\"sides\"")]},
        {"from": 17, "still": "e_end0"},
    ]},
    "s03_a_sides_section": {"step": 2, "beats": [
        {"from": 0, "still": "e_end0"},
        {"from": 1, "still": "e_tsn", "marks": [("lines", 204, 212)]},
        {"from": 2, "still": "e_tsn", "marks": [("text", 206, "## [Sides]")]},
        {"from": 3, "still": "e_tsn", "marks": [("text", 206, "(sides)")]},
        {"from": 4, "still": "e_tsn", "marks": [_TSN_REC]},
        {"from": 5, "still": "e_tsn", "marks": [("hashes", 208), ("text", 208, "[TSN]"), ("text", 208, "(tsn)")]},
        {"from": 7, "still": "e_tsn", "marks": [("text", 208, "(tsn)")]},
        {"from": 9, "still": "e_tsn", "marks": [("text", 210, "Color: #07F")]},
        {"from": 11, "still": "card_color"},
        {"from": 12, "still": "game_sci_ds1_sci2", "marks": [_SCI_SIDE]},
        {"from": 13, "still": "t_tsn", "marks": [("part", "run1:clean")]},
    ]},
    "s04_two_more_sides": {"step": 3, "beats": [
        # the game first: the two new sides on Science
        {"from": 0, "still": "game_sci_cutter_sci2", "marks": [_SCI_TITLE]},
        {"from": 3, "still": "game_sci_yard_sci2", "marks": [_SCI_TITLE]},
        {"from": 4, "still": "e_three", "marks": [("text", 214, "(breaker)"), ("text", 216, "#F80")]},
        {"from": 5, "still": "e_three", "marks": [("lines", 217, 217)]},
        {"from": 6, "still": "e_three", "marks": [("text", 217, "tsn")]},
        {"from": 7, "still": "e_three", "marks": [("text", 221, "(guild)"), ("text", 223, "#0C6")]},
        {"from": 8, "still": "e_three", "marks": [("lines", 224, 224)]},
        {"from": 9, "still": "e_three", "marks": [("text", 217, "tsn"), ("text", 224, "tsn")]},
        {"from": 10, "still": "e_three", "marks": [("lines", 217, 217)]},
        {"from": 12, "still": "e_three", "marks": [_TSN_REC]},
    ]},
    "s05_something_on_each_side": {"step": 4, "beats": [
        # the game first: the two landmarks on Helm's map
        {"from": 0, "still": "game_helm_map"},
        {"from": 2, "still": "game_helm_map", "marks": [_HM_ALL]},
        {"from": 3, "still": "game_helm_map", "marks": [_HM_CUTTER]},
        {"from": 5, "still": "game_helm_map", "marks": [_HM_YARD]},
        {"from": 6, "still": "e_land", "marks": [("lines", 203, 211), ("lines", 213, 221)]},
        {"from": 7, "still": "e_land", "marks": [("text", 205, "Prefab: ship"), ("text", 215, "Prefab: station")]},
        {"from": 8, "still": "e_land", "marks": [("lines", 206, 206), ("lines", 216, 216)]},
        {"from": 9, "still": "e_land_w"},
        {"from": 10, "still": "e_land_w", "marks": [("lines", 192, 192), ("lines", 203, 221)]},
        {"from": 11, "still": "e_land_w", "marks": [("lines", 226, 226)]},
        {"from": 12, "still": "e_land_w", "marks": [("lines", 226, 226)], "dim": True},
        {"from": 14, "still": "t_land", "marks": [("part", "run1:clean")]},
    ]},
    "s06_a_second_station": {"step": 5, "beats": [
        # the game first: the step in the Quest Log
        {"from": 0, "still": "game_log_home"},
        {"from": 1, "still": "game_log_home", "marks": [_QL_ROW]},
        {"from": 2, "still": "game_log_home", "marks": [_QL_ROW, _QL_ORDER]},
        {"from": 3, "still": "e_half0", "marks": [("text", 121, "reach station 1000")]},
        {"from": 4, "still": "e_half0", "marks": [("text", 121, "station")]},
        {"from": 5, "still": "game_helm_map", "marks": [_HM_YARD]},
        {"from": 7, "still": "e_half", "marks": [("text", 121, "home")]},
        {"from": 8, "still": "e_half", "marks": [("text", 121, "reach home 1000")]},
        {"from": 9, "still": "t_half", "marks": [("span", 1, "role-nothing-wears")]},
        {"from": 10, "still": "t_half", "marks": [("span", 1, "line 121")]},
        {"from": 11, "still": "m_half", "marks": [("lines", 64, 64)]},
        {"from": 12, "still": "m_half", "marks": [("text", 64, "\"tsn, station\"")]},
        {"from": 13, "still": "m_home", "marks": [("text", 64, ", home")]},
        {"from": 14, "still": "m_home", "marks": [("text", 64, "tsn"), ("text", 64, "station, home")]},
        {"from": 15, "still": "t_home", "marks": [("part", "run2:clean")]},
    ]},
    "s07_who_is_what_to_whom": {"step": 6, "beats": [
        {"from": 0, "still": "card_pairs"},
        {"from": 1, "still": "card_pairs", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_pairs", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_pairs", "marks": [("part", "r3")]},
        {"from": 6, "still": "e_guild0", "marks": [("lines", 237, 237)]},
        {"from": 7, "still": "e_guild", "marks": [("text", 237, "tsn, guild")]},
        {"from": 8, "still": "card_rel"},
        {"from": 9, "still": "game_sci_cutter_sci2", "marks": [_SCI_TITLE, _SCI_ENEMY]},
        {"from": 10, "still": "game_comms_cutter", "marks": [_CC_BUTTONS]},
        {"from": 11, "still": "game_comms_yard", "marks": [_CY_BUTTONS]},
        {"from": 12, "still": "game_helm_dock", "marks": [_HD_DOCKED, _HD_STATE]},
        {"from": 13, "still": "game_helm_cutter", "marks": [_HC_CUTTER]},
        {"from": 14, "still": "game_helm_cutter", "marks": [_HC_CUTTER, _HC_SHIELDS]},
    ]},
    "s08_lint_and_what_lint_cannot_se": {"step": 8, "beats": [
        {"from": 0, "still": "e_sides", "marks": [("lines", 240, 240)]},
        {"from": 1, "still": "e_tsm", "marks": [("text", 240, "tsm")]},
        {"from": 2, "still": "t_tsm", "marks": [("span", 1, "dangling-side")]},
        {"from": 3, "still": "t_tsm", "marks": [("span", 1, "is not a side in this mission")]},
        {"from": 4, "still": "t_tsm", "marks": [("span", 1, "Declared here: breaker, guild, tsn")]},
        {"from": 5, "still": "e_cutter", "marks": [("lines", 209, 209)]},
        {"from": 6, "still": "e_noside", "marks": [("lines", 206, 213)]},
        {"from": 7, "still": "t_noside", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "e_hash4", "marks": [("hashes", 244)]},
        {"from": 8.6, "still": "t_hash4", "marks": [("part", "run2:clean")]},
        {"from": 9, "still": "game_sci_noside_sci2", "marks": [_SCI_UNKNOWN]},
        {"from": 12, "still": "game_sci_noside_sci2", "marks": [_SCI_QUEUE]},
        {"from": 13, "still": "game_sci_noside_sci2", "marks": [_SCI_THREATS0]},
        {"from": 14, "still": "game_sci_noside_sci2", "marks": [_SCI_UNKNOWN]},
        {"from": 15, "still": "card_cannot"},
        {"from": 16, "still": "e_cutter", "marks": [("lines", 209, 209)]},
        {"from": 17, "still": "e_sides", "marks": [("hashes", 231), ("hashes", 237), ("hashes", 244)]},
    ]},
    "s09_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_sci_yard_sci2", "marks": [_SCI_NAME]},
        {"from": 1, "still": "game_sci_yard_sci2", "marks": [_SCI_TABS]},
        {"from": 3, "still": "game_sci_yard_sci2", "marks": [_SCI_TITLE, _SCI_FRIEND]},
        {"from": 4, "still": "game_comms_yard_hail", "marks": [_CY_HAIL]},
        {"from": 5, "still": "game_comms_yard_hail", "marks": [_C_HEADER]},
        {"from": 6, "still": "game_comms_yard_hail", "marks": [_CY_TEXT]},
        {"from": 7, "still": "game_helm_dock", "marks": [_HD_DOCKED, _HD_RELEASE]},
        {"from": 8, "still": "game_sci_cutter_sci2"},
        {"from": 9, "still": "game_sci_cutter_sci2", "marks": [_SCI_TITLE]},
        {"from": 10, "still": "game_sci_cutter_sci2", "marks": [_SCI_ENEMY]},
        {"from": 11, "still": "game_comms_cutter_hail", "marks": [_C_HEADER, _CC_TEXT]},
        {"from": 12, "still": "game_helm_cutter", "marks": [_HC_CUTTER]},
        {"from": 13, "still": "game_helm_cutter", "marks": [_HC_CUTTER, _HC_SHIELDS]},
        {"from": 14, "still": "game_log_yard", "marks": [_QL_ROW]},
        {"from": 15, "still": "game_log_yard", "marks": [_QL_ROW, _QL_ORDER]},
        {"from": 17, "still": "game_win", "marks": [_WIN]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item5"), ("part", "item6")]},
        {"from": 5, "still": "card_next"},
    ]},
}
