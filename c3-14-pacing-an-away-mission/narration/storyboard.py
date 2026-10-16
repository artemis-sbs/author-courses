"""Storyboard for c3-14-pacing-an-away-mission: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-16).

The lecture starts from Lecture 13's finished files in MyAway ("start"). Only mission.amd
changes, in three records: the clock on Relight Kesh Relay ("r5"), the terminal's update
hands over the sentry's cell ("r6"), and Marrow pays the doctor with a fuse ("final", the
page's own example\\mission.amd). Most of the lecture is the page's tables, drawn as cards.

2026-10-15: example\\mission.amd here (and in Lecture 15) carried four of the starter's OLD
mark lines (Mark: keycard, At: 6, 8, At: 16, 2, Mark: sentry) that Lecture 13's re-measure
had changed to Mark: yard / scrub / crate / post; lint reported two of them as never placed.
They now match Lecture 13, and the finished file lints clean.

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders). The three maps in scene 3 are pictures from the Tile Map Editor, Art
view ("editor": "tiles"; see capture.web_steps).

GAME STILLS. Taken 2026-10-16 in the engine, two games of state final, consoles
server,science,weapons (Dr Ines Hale, Lt Sam Reyes). What they showed: the clock runs from
MAP START, so by beam-down it already reads a few minutes under thirty - captions never quote
a time. Tasks opens on Hale's own story; Relight Kesh Relay is picked from the list, and its
page has a `Time left` row (so does the Quest Log page aboard). THE YARD TERMINAL IS INSIDE
THE SENTRY'S NOTICE: every cell beside it (20,6 / 22,6 / 21,7) is within Notice 4 (Manhattan)
of the loop 18 9; 25 9; 25 11; 18 11 (walkcheck), and game 1's Hale was shot down at it. The
lesson's route is now: Reyes STUNs the sentry (Stun: 10), Hale works the terminal while it
stands, a second stun if it wakes; never FULL (that drops the cell and removes Step 6's
problem). Once calm the sentry stays standing where it was stunned; the line says it walks to
the terminal, the map does not show that, and the cell simply appears in her pack. Pack lists
items by item key: fuse x1 FIRST, then power cell x1. The kept Act/Pack stills of the
terminal and Marrow are from game 2 (game 1's Hale chose while DOWN - a library defect).
`python game.py c3-14-pacing-an-away-mission start --consoles server,science,weapons`
(GAME_RESULTS_SAVE is false). Take the clock stills first.
  1. Weapons (Reyes), still aboard: the handheld icon, Quests, select Relight Kesh Relay:
     game_l14_log_clock (time left on its row, a Time left row, the hourglass line under the
     first paragraph).
  2. Science (Hale): the handheld icon, Boarding Party, BEAM DOWN. Tasks, pick Relight Kesh
     Relay in the list: game_l14_tasks_clock. Walk her to 16,6 (mid-yard, five cells west of
     the terminal, outside the sentry's notice): game_l14_yard.
  3. Reyes: beam down. Fire, choose FULL, Arm (do not click the map): game_l14_fire_full.
     Make safe. Then STUN, Arm, and click the sentry the moment it enters a cell (18,10 on its
     west leg).
  4. Hale, at once while it stands: the terminal. Pull the door code out of its memory, Copy
     it down, Send the sentry its recognition update (about 6 s): game_l14_update (the
     room's line; the sentry standing at 18,10). If it wakes first, Reyes stuns it again.
     Step back. Pack: game_l14_pack_cell (power cell x1).
  5. Hale: talk to Old Marrow, Look at that cough: game_l14_dust_lung (the line ending
     'pays for it with the fuse out of his kettle'). Leave him. Pack: game_l14_pack_fuse
     (fuse x1, then power cell x1).
No still needs a re-shoot: none shows the xESS bar's mark slot, a downed member's press, or
another library defect being fixed.
"""
import os as _os

LECTURE = "c3-14-pacing-an-away-mission"
TITLE = ("Class 3, Lecture 14", "Pacing an away mission", "A clock, three lists and three columns")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_COURSES = _os.path.dirname(_HERE)


def _read(*parts):
    with open(_os.path.join(_COURSES, *parts), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_LOSE_OLD = "Lose: The beacon is slag. The Kesh run stays dark, and the convoys must find another road.\n"
_LOSE_NEW = "Lose: Kesh Relay stays dark. The convoy comes through blind, and must find another road.\n"
_HOURGLASS = "![](icon://hourglass) Thirty minutes. Then the next convoy comes through, lamp or no lamp.\n\n"
_UPDATE = "(terminal_update) if learned codes ; calm sentry\n"
_ROOM_OLD = ("% The terminal sends nine days of crew lists in one burst. Out in the yard the sentry stops, turns its "
             "head toward you, and goes back to its square with its weapon down.\n")
_ROOM_NEW = ("% The terminal sends nine days of crew lists in one burst. The sentry stops, walks to the terminal, opens "
             "its chest and sets a power cell in your hands. Then it goes back to its square with its weapon down.\n")
_COUGH = "(marrow_treated) if medical ; signal marrow_treated\n"
_DUST = "He takes the inhaler like it is made of glass.\n"

STATES = {
    # Lecture 13's finished files
    "start": {"folder": "c3-07-anatomy-of-a-long-away-mission/example",
              "over": ("c3-09-tile-map-editor-part-2/example", "c3-10-props/example",
                       "c3-11-people-and-hostiles/example", "c3-12-scenes-on-the-ground/example",
                       "c3-13-what-the-crew-sees/example")},
    # Step 5: a clock, a Lose line true every way, and the hourglass for the bridge
    "r5": {"base": "start", "edits": [
        ("replace", FILE, "Leads to: beacon\nWin:", "Leads to: beacon\nFails when: 30 minutes\nWin:"),
        ("replace", FILE, _LOSE_OLD, _LOSE_NEW),
        ("replace", FILE, "Go down and light it.\n\n", "Go down and light it.\n\n" + _HOURGLASS)]},
    # Step 6: the update hands the cell over
    "r6": {"base": "r5", "edits": [
        ("replace", FILE, _UPDATE, "(terminal_update) if learned codes ; calm sentry, give power_cell\n"),
        ("replace", FILE, _ROOM_OLD, _ROOM_NEW)]},
    # Step 7: Marrow pays with a fuse. The page's own file.
    "final": {"base": "r6", "edits": [
        ("replace", FILE, _COUGH, "(marrow_treated) if medical ; signal marrow_treated, give fuse\n"),
        ("replace", FILE, _DUST, "He takes the inhaler like it is made of glass, and pays for it with the fuse out of his kettle.\n")],
        "same_as": LECTURE + "/example/mission.amd"},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}
_MAP = {"side": False, "editor": "tiles", "view": "art"}            # a map in the Tile Map Editor (capture.web_steps)

STILLS = {
    # Step 2: the three maps, in the Tile Map Editor's Art view
    "e_map_landing": ("vscode", "start", 1, "mid", dict(_MAP, file="ground/landing.tiles", zoom=32)),
    "e_map_gully": ("vscode", "start", 1, "mid", dict(_MAP, file="ground/gully.tiles", zoom=40)),
    "e_map_cistern": ("vscode", "start", 1, "mid", dict(_MAP, file="ground/cistern.tiles", zoom=48)),
    # Step 5: the clock
    "e_clock0": ("vscode", "start", 76, "big", _NS),       # lines 66 to 86: Relight Kesh Relay as Lecture 13 left it
    "e_clock": ("vscode", "final", 78, "big", _NS),        # lines 68 to 88: Fails when (75), Lose (77), the hourglass (83)
    "t_r5": ("terminal", [("r5", _LINT)]),
    # Step 6: the terminal
    "e_term0": ("vscode", "start", 491, "big", _NS),       # lines 481 to 501: the update answer (489), its room (494)
    "e_term6": ("vscode", "r6", 494, "big", _NS),          # lines 484 to 504: the answer (492), the room's line (497)
    # Step 7: the cough
    "e_cough0": ("vscode", "r6", 534, "big", _NS),         # lines 524 to 544: Old Marrow, the cough answer (534)
    "e_cough7": ("vscode", "final", 534, "big", _NS),
    "e_dust7": ("vscode", "final", 568, "big", _NS),       # lines 558 to 578: Dust Lung's line (568)
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME (taken 2026-10-16). State final, three windows: server, Science (Dr Hale),
    # Weapons (Lt Reyes). Press order in the docstring.
    "game_l14_log_clock": ("game", "Weapons, aboard, its ePADD Quest Log, Relight Kesh Relay selected: a time left on its row, and in its page the hourglass line 'Thirty minutes. Then the next convoy comes through, lamp or no lamp.' under the first paragraph, then the table"),
    "game_l14_tasks_clock": ("game", "Science's xESS just beamed down, the Tasks app: Relight Kesh Relay picked in the list, its time left under it (already a few minutes under thirty), the page's State and Time left rows"),
    "game_l14_yard": ("game", "Science's console: the map of the yard with Dr Hale's figure part way across it, five cells west of the terminal, outside the sentry's notice"),
    "game_l14_fire_full": ("game", "Weapons' xESS, the Fire app with FULL chosen and ARMED (nothing clicked on the map)"),
    "game_l14_update": ("game", "Science's xESS, Act, after Send the sentry its recognition update: the line 'The sentry stops, walks to the terminal, opens its chest and sets a power cell in your hands...'; on the map the sentry stands where the stun caught it"),
    "game_l14_pack_cell": ("game", "Science's xESS, Pack after the update: power cell x1"),
    "game_l14_dust_lung": ("game", "Science's xESS, Act, Dust Lung after Look at that cough: the line ending 'and pays for it with the fuse out of his kettle.'"),
    "game_l14_pack_fuse": ("game", "Science's xESS, Pack after Marrow's cough: fuse x1, then power cell x1"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_45": ("card", "points", {"kicker": "A sheet of paper", "items": ["My mission: 45 minutes", "Says who?"]}),
    "card_floor": ("card", "points", {"kicker": "Every number today is a floor", "items": [
        "Walked by a script, at the game's own speed",
        "A script never reads, never argues and never gets lost"]}),
    "card_numbers": ("card", "table", {"heading": "Step 1 - The game's own numbers", "kicker": "The game's own numbers"}),
    "card_walks": ("card", "table", {"heading": "Step 2 - Walk your own map", "kicker": "Walk your own map: cells, and seconds"}),
    "card_scenes": ("card", "table", {"heading": "Step 3 - Count the presses", "kicker": "The scenes"}),
    "card_plays": ("card", "table", {"heading": "Step 3 - Count the presses", "nth": 2, "kicker": "Three plays, by script"}),
    "card_guess": ("card", "table", {"heading": "Step 3 - Count the presses", "nth": 3, "kicker": "Presses into minutes: a guess"}),
    "card_tools": ("card", "table", {"heading": "Step 4 - Four ways to press on a crew", "kicker": "Four ways to press on a crew"}),
    "card_areas": ("card", "table", {"heading": "Step 6 - Can every party get there?", "kicker": "Every area"}),
    "card_items": ("card", "table", {"heading": "Step 6 - Can every party get there?", "nth": 2, "kicker": "Every item"}),
    "card_endings": ("card", "table", {"heading": "Step 6 - Can every party get there?", "nth": 3, "kicker": "Every ending"}),
    "card_cols1": ("card", "table", {"heading": "Step 7 - What three crew do at once", "kicker": "As Lecture 13 left it: a chain"}),
    "card_cols2": ("card", "table", {"heading": "Step 7 - What three crew do at once", "nth": 2, "kicker": "With Marrow's fuse: a join"}),
    "card_beats": ("card", "table", {"heading": "Step 8 - The beat sheet, with times", "kicker": "The beat sheet"}),
    "card_sheet45": ("card", "table", {"heading": "Step 8 - The beat sheet, with times", "nth": 2, "kicker": "Forty-five minutes, on paper first"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 15", "sub": "Boarding an enemy ship"}),
}

# Marks on the game stills (fractions of the 1280x960 frame), read off the stills 2026-10-16.
_YD_HALE = ("rect", 0.38, 0.4, 0.435, 0.48)          # game_l14_yard: Dr Hale mid-yard
_TC_ROW = ("rect", 0.675, 0.365, 0.965, 0.45)        # game_l14_tasks_clock: Relight Kesh Relay, its time left
_TC_LEFT = ("rect", 0.675, 0.52, 0.88, 0.59)         # ... the page: State Active, Time left
_FF_FULL = ("rect", 0.665, 0.42, 0.99, 0.6)          # game_l14_fire_full: > FULL and what it does
_FF_HINT = ("rect", 0.665, 0.865, 0.985, 0.93)       # ... 'The next click on the map is a shot. One shot, then safe.'
_LC_HOUR = ("rect", 0.39, 0.385, 0.94, 0.43)         # game_l14_log_clock: the hourglass line
_ML_TERM = ("rect", 0.6, 0.31, 0.765, 0.55)          # e_map_landing (1920x1080): @terminal and the sentry's dashed square
_UP_HALE = ("rect", 0.315, 0.4, 0.39, 0.48)          # game_l14_update: Dr Hale at the terminal
_UP_SENTRY = ("rect", 0.225, 0.6, 0.285, 0.685)      # ... the sentry, standing where the stun caught it
_UP_ROOM = ("rect", 0.67, 0.6, 0.975, 0.915)         # ... the pick and the terminal's line
_UP_WALKS = ("rect", 0.745, 0.72, 0.975, 0.82)       # ... 'The sentry stops, walks to the terminal...'
_PC_CELL = ("rect", 0.665, 0.195, 0.78, 0.235)       # game_l14_pack_cell: power cell x1
_DL_LINE = ("rect", 0.67, 0.695, 0.975, 0.915)       # game_l14_dust_lung: '...pays for it with the fuse out of his kettle.'
_PF_FUSE = ("rect", 0.665, 0.195, 0.74, 0.235)       # game_l14_pack_fuse: fuse x1 (listed first)

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l14_yard", "marks": [_YD_HALE]},
        {"from": 1, "still": "card_45"},
        {"from": 4, "still": "game_l14_tasks_clock", "marks": [_TC_ROW]},
        {"from": 5, "still": "card_areas"},
        {"from": 6, "still": "card_cols1"},
        {"from": 7, "still": "card_floor"},
        {"from": 9, "still": "card_title"},
    ]},
    "s02_the_game_s_numbers": {"step": 1, "beats": [
        {"from": 0, "still": "game_l14_yard", "marks": [_YD_HALE]},
        {"from": 0.5, "still": "card_numbers", "marks": [("part", "r1")]},
        {"from": 1, "still": "card_numbers", "marks": [("part", "r2")]},
        {"from": 2, "still": "card_numbers", "marks": [("part", "r3")]},
        {"from": 4, "still": "card_numbers", "marks": [("part", "r4")]},
        {"from": 6, "still": "card_numbers", "marks": [("part", "r6")]},
        {"from": 7, "still": "card_numbers", "marks": [("part", "r7")]},
        {"from": 8, "still": "game_l14_fire_full", "marks": [_FF_FULL]},
        {"from": 9, "still": "card_numbers", "marks": [("part", "r9")]},
    ]},
    "s03_distance_is_not_pressure": {"step": 2, "beats": [
        {"from": 0, "still": "e_map_landing"},
        {"from": 2, "still": "card_walks", "marks": [("part", "r1")]},
        {"from": 3, "still": "e_map_gully"},
        {"from": 3.5, "still": "e_map_cistern"},
        {"from": 5, "still": "card_walks"},
        {"from": 6, "still": "card_walks", "marks": [("part", "r1")]},
        {"from": 7, "still": "card_scenes"},
    ]},
    "s04_count_the_presses": {"step": 3, "beats": [
        {"from": 0, "still": "card_scenes", "marks": [("part", "r8")]},
        {"from": 1, "still": "card_plays"},
        {"from": 2, "still": "card_plays", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_plays", "marks": [("part", "r3")]},
        {"from": 4, "still": "card_plays", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_guess"},
        {"from": 10, "still": "card_guess", "marks": [("part", "r2")]},
        {"from": 12, "still": "card_guess"},
    ]},
    "s05_a_clock": {"step": 5, "beats": [
        {"from": 0, "still": "card_tools", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 2, "still": "card_tools", "marks": [("part", "r3"), ("part", "r4")]},
        # the game first: the clock on the ground
        {"from": 3, "still": "game_l14_tasks_clock", "marks": [_TC_ROW]},
        {"from": 5, "still": "e_clock0", "marks": [("lines", 74, 75)]},
        {"from": 6, "still": "e_clock", "marks": [("lines", 75, 75)]},
        {"from": 7, "still": "e_clock0", "marks": [("lines", 76, 76)]},
        {"from": 9, "still": "e_clock", "marks": [("lines", 77, 77)]},
        {"from": 11, "still": "e_clock", "marks": [("lines", 83, 83)]},
        # the game: the line in the Quest Log aboard
        {"from": 14, "still": "game_l14_log_clock", "marks": [_LC_HOUR]},
        {"from": 16, "still": "e_clock", "marks": [("lines", 72, 72)]},
        {"from": 17, "still": "t_r5", "marks": [("part", "run1:clean")]},
        # the game: by beam-down the clock is already under thirty (never quote the time)
        {"from": 18, "still": "game_l14_tasks_clock", "marks": [_TC_ROW, _TC_LEFT]},
    ]},
    "s06_can_every_party_get_there": {"step": 6, "beats": [
        {"from": 0, "still": "card_areas"},
        {"from": 2, "still": "card_items"},
        {"from": 2.5, "still": "card_endings"},
        {"from": 4, "still": "card_areas", "marks": [("part", "r4")]},
        # the terminal is inside the sentry's notice: Reyes stuns it first
        {"from": 6, "still": "e_map_landing", "marks": [_ML_TERM]},
        {"from": 8, "still": "card_numbers", "marks": [("part", "r11")]},
        {"from": 9, "still": "game_l14_update", "marks": [_UP_HALE, _UP_SENTRY]},
        {"from": 10, "still": "card_numbers", "marks": [("part", "r11")]},
        {"from": 11, "still": "card_numbers", "marks": [("part", "r12")]},
        {"from": 12, "still": "game_l14_fire_full", "marks": [_FF_HINT]},
        {"from": 14, "still": "e_term0", "marks": [("lines", 489, 489)]},
        {"from": 16, "still": "card_items", "marks": [("part", "r6"), ("part", "r7")]},
        {"from": 18, "still": "card_items", "marks": [("part", "r7")]},
        {"from": 19, "still": "e_term6", "marks": [("lines", 497, 497)]},
        # the game first: the cell in her pack
        {"from": 21, "still": "game_l14_update", "marks": [_UP_ROOM]},
        {"from": 22, "still": "game_l14_update", "marks": [_UP_WALKS]},
        {"from": 23, "still": "game_l14_update", "marks": [_UP_SENTRY]},
        {"from": 24, "still": "game_l14_pack_cell", "marks": [_PC_CELL]},
        {"from": 25, "still": "e_term6", "marks": [("text", 492, ", give power_cell")]},
    ]},
    "s07_three_columns": {"step": 7, "beats": [
        {"from": 0, "still": "card_cols1"},
        {"from": 3, "still": "card_cols1", "marks": [("part", "r2"), ("part", "r4")]},
        {"from": 5, "still": "card_cols1"},
        {"from": 8, "still": "card_cols1", "marks": [("part", "r4")]},
        {"from": 10, "still": "e_cough0", "marks": [("lines", 534, 534)]},
        # the game first: Marrow pays with a fuse
        {"from": 12, "still": "game_l14_dust_lung", "marks": [_DL_LINE]},
        {"from": 13, "still": "game_l14_pack_fuse", "marks": [_PF_FUSE]},
        {"from": 14, "still": "e_cough7", "marks": [("text", 534, ", give fuse")]},
        {"from": 14.5, "still": "e_dust7", "marks": [("lines", 568, 568)]},
        {"from": 15, "still": "card_cols2"},
        {"from": 16, "still": "card_cols2", "marks": [("part", "r3")]},
    ]},
    "s08_the_beat_sheet_and_your_turn": {"step": 8, "beats": [
        {"from": 0, "still": "card_beats"},
        {"from": 1, "still": "card_beats", "marks": [("part", "r9")]},
        {"from": 4, "still": "game_l14_tasks_clock", "marks": [_TC_ROW]},
        {"from": 6, "still": "card_sheet45"},
        {"from": 7, "still": "card_sheet45", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_sheet45", "marks": [("part", "r2")]},
        {"from": 9, "still": "card_sheet45", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_sheet45", "marks": [("part", "r4")]},
        {"from": 11, "still": "card_sheet45", "marks": [("part", "r5")]},
        {"from": 12, "still": "card_next"},
    ]},
}
