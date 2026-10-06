"""Storyboard for c1-11-just-enough-mast: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6. Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-05).

This is the lecture where the student edits story.mast. Every still of it is the real file
at its real line numbers: Lecture 10's finished file (105 lines) until scene 9, then the
card as it is pasted, line by line, down to this lecture's example\\ (115 lines), which the
state "final" must equal byte for byte, both files. Every Command Prompt still is the real
`sbs lint` (0.13) on a copy with exactly that one mistake.
"""
LECTURE = "c1-11-just-enough-mast"
TITLE = ("Class 1, Lecture 11", "Just enough MAST", "Read the script once, then paste three cards")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_DESC_OLD = "\" A short investigation, with its content authored in a .amd fact sheet."
_DESC_NEW = "\" A dying hulk, a missing lifeboat, and ten minutes to bring her log home."
_BOAT_THEN = "Then: reveal salvage/home\nPart of: salvage\nRequired: true\n---\nHer log"
_FIND = "Her log is not aboard, and one lifeboat cradle is empty. Find the boat.\n"
_TUG_STEP = ("\n#### [Wait for the Tug](tug)\n---\nScope: shared\nStarts when: revealed\n"
             "Objective: Hold near the lifeboat until the tug arrives\nDone when: signal tug_arrived\n"
             "Reward: 50 credits\nThen: reveal salvage/home\nPart of: salvage\nRequired: true\n---\n"
             "DS 1 is sending a tug for the lifeboat. Stay with her until it gets here.\n")
_NOTE = "#\n# Wait for the Tug: what happens when that step starts.\n#\n"
_ROUTE = "//shared/signal/quest_started if QUEST_ID == \"salvage/tug\"\n"
_WAIT = "    await delay_sim(20)\n"
_SPAWN = "    npc_spawn(5600, 0, 6000, \"Salvage Tug\", \"tsn, tug\", \"cargo_ship\", \"behav_npcship\")\n"
_EMIT = "    signal_emit(\"quest_signal\", {\"SIGNAL_NAME\": \"tug_arrived\"})\n"
_END = "    ->END\n"
_CARD = _NOTE + _ROUTE + _WAIT + _SPAWN + _EMIT + _END
_RELICS = "    relics_spawn(get_mission_dir_filename(\"mission.amd\"))\n"
_W_ROLE = "// ROLE    lifeboat          worn by The Lifeboat, a landmark in this file\n"
_W_TUG = "// ROLE    tug               worn by the Salvage Tug, once it arrives\n"
_W_SIG = "// SIGNAL  derelict_scanned  said when Science scans anything that wears derelict\n"
_W_ARR = "// SIGNAL  tug_arrived       said twenty seconds after Wait for the Tug starts\n"

STATES = {
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example")},
    # Step 2: the map's name, then its description
    "name": {"base": "start", "edits": [("replace", MAST, "\"AMD Sample\"", "\"Salvage Run\"")]},
    "title": {"base": "name", "edits": [("replace", MAST, _DESC_OLD, _DESC_NEW)]},
    # Step 3: one quote mark taken out of line 25
    "q25": {"base": "title", "edits": [("replace", MAST, "\"Salvage Run\"", "\"Salvage Run")]},
    # Step 4: a step that waits for the script
    "then": {"base": "title", "edits": [("replace", FILE, _BOAT_THEN, _BOAT_THEN.replace("salvage/home", "salvage/tug"))]},
    "wait": {"base": "then", "edits": [("replace", FILE, _FIND, _FIND + _TUG_STEP)]},
    # Steps 5 to 7: the card, a line at a time
    "c_note": {"base": "wait", "edits": [("append", MAST, "\n\n" + _NOTE)]},
    "c_route": {"base": "wait", "edits": [("append", MAST, "\n\n" + _NOTE + _ROUTE)]},
    "card1": {"base": "wait", "edits": [("append", MAST, "\n\n" + _NOTE + _ROUTE + _SPAWN + _END)]},
    "card2": {"base": "card1", "edits": [("replace", MAST, _SPAWN + _END, _SPAWN + _EMIT + _END)]},
    "card3": {"base": "card2", "edits": [("replace", MAST, _ROUTE, _ROUTE + _WAIT)]},
    "final": {"base": "card3", "edits": [("replace", FILE, _W_ROLE, _W_ROLE + _W_TUG),
                                         ("replace", FILE, _W_SIG, _W_SIG + _W_ARR)],
              "same_as": ("c1-11-just-enough-mast/example/mission.amd", "c1-11-just-enough-mast/example/story.mast")},
    # Step 8: four mistakes, one at a time
    "m_indent": {"base": "final", "edits": [("replace", MAST, _SPAWN, _SPAWN[1:])]},
    "m_low": {"base": "final", "edits": [("replace", MAST, _EMIT + _END, _END + _EMIT)]},
    "m_mid": {"base": "final", "edits": [("replace", MAST, "\n\n" + _CARD, ""),
                                         ("replace", MAST, _RELICS, _RELICS + "\n" + _CARD)]},
    "m_addr": {"base": "final", "edits": [("replace", MAST, "\"salvage/tug\"", "\"salvage/tgu\"")]},
    # after a play: the game writes both logs, and an untroubled play leaves them empty (0 bytes, seen)
    "played": {"base": "final", "edits": [("write", "mast.compile.log", ""), ("write", "mast.runtime.log", "")]},
    # PROBE-ONLY, for the game stills, so nobody has to fly. Never shown in the editor.
    # The hulk 2500 away, the lifeboat 1500 off to one side, the reach distances widened,
    # and the tug brought in beside the probe's lifeboat (400 short of it, as on the page).
    "g_tug": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 2500, "Unknown Hulk"'),
        ("replace", MAST, "npc_spawn(5600, 0, 6000,", "npc_spawn(1100, 0, 1500,"),
        ("replace", FILE, "of the hulk\nDone when: reach derelict 500", "of the hulk\nDone when: reach derelict 30000"),
        ("replace", FILE, "two minutes\nDone when: reach derelict 500", "two minutes\nDone when: reach derelict 30000"),
        ("replace", FILE, "Done when: reach lifeboat 500", "Done when: reach lifeboat 30000"),
        ("replace", FILE, "Loc: 6000, 0, 6000", "Loc: 1500, 0, 1500")]},
    "g_wait": {"base": "g_tug", "edits": [("replace", MAST, "await delay_sim(20)", "await delay_sim(900)")]},
    "g_win": {"base": "g_tug", "edits": [("replace", FILE, "Done when: reach station 1000", "Done when: reach station 30000")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # story.mast as Lecture 10 left it (105 lines), read from top to bottom
    "m_top": ("vscode", "start", 14, "mid", _M),            # lines 1 to 28
    "m_under": ("vscode", "start", 39, "mid", _M),          # lines 25 to 53: what is indented under the map
    "m_35": ("vscode", "start", 35, "big", _M),             # lines 25 to 45
    "m_load": ("vscode", "start", 54, "big", _M),           # lines 44 to 64
    "m_hulk": ("vscode", "start", 69, "big", _M),           # lines 59 to 79
    "m_tail": ("vscode", "start", 95, "big", _M),           # lines 85 to 105
    # the fact sheet, for the lines the script points at
    "e_top": ("vscode", "start", 10, "big", _NS),           # lines 1 to 20
    "e_find": ("vscode", "start", 35, "big", _NS),          # lines 25 to 45: Find the Derelict
    "e_land": ("vscode", "start", 161, "big", _NS),         # the Landmarks section line
    # Step 2: lines 15 to 35 of the script
    "m_25": ("vscode", "start", 25, "big", _M),
    "m_name": ("vscode", "name", 25, "big", _M),
    "m_title": ("vscode", "title", 25, "big", _M),
    "m_q25": ("vscode", "q25", 25, "big", _M),
    # Step 4: the fact sheet
    "e_w0": ("vscode", "title", 72, "mid", _NS),            # lines 58 to 86: hulk, lifeboat, home
    "e_then": ("vscode", "then", 79, "big", _NS),           # lines 69 to 89
    "e_wait": ("vscode", "wait", 85, "big", _NS),           # lines 75 to 95
    "e_boat": ("vscode", "wait", 176, "big", _NS),          # The Lifeboat record
    # Steps 5 to 7: the card, at the end of the script. Every still looks at lines 95 to 115
    "m_end0": ("vscode", "wait", 105, "big", _M),
    "m_c_note": ("vscode", "c_note", 105, "big", _M),
    "m_c_route": ("vscode", "c_route", 105, "big", _M),
    "m_card1": ("vscode", "card1", 105, "big", _M),
    "m_card2": ("vscode", "card2", 105, "big", _M),
    "m_card3": ("vscode", "card3", 105, "big", _M),
    "e_words": ("vscode", "final", 12, "big", _NS),         # lines 2 to 22: the word list
    # Step 8: four mistakes
    "m_indent": ("vscode", "m_indent", 105, "big", _M),
    "m_low": ("vscode", "m_low", 105, "big", _M),
    "m_mid": ("vscode", "m_mid", 68, "big", _M),            # lines 58 to 78
    "m_addr": ("vscode", "m_addr", 105, "big", _M),
    "e_logs": ("vscode", "played", 1, "close", {"file": "mast.runtime.log"}),   # with the file list: both logs, empty
    # the Command Prompt: the real tool's answer for that state
    "t_title": ("terminal", [("title", _LINT)]),
    "t_q25": ("terminal", [("q25", _LINT)]),
    "t_q25_fix": ("terminal", [("q25", _LINT), ("title", _LINT)]),
    "t_wait": ("terminal", [("wait", _LINT)]),
    "t_card2": ("terminal", [("card1", _LINT), ("card2", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_indent": ("terminal", [("m_indent", _LINT)]),
    "t_low": ("terminal", [("m_low", _LINT)]),
    "t_mid": ("terminal", [("m_mid", _LINT)]),
    "t_addr": ("terminal", [("m_addr", _LINT)]),
    # the real game (game.py). All but game_broken are from PROBE states: see STATES.
    "game_wait_map": ("game", "Helm: 'Quest complete: Find the Lifeboat', the lifeboat's icon, no tug (probe: the wait made long)"),
    "game_wait_log": ("game", "The Quest Log: Wait for the Tug, Active"),
    "game_tug_map": ("game", "Helm: the Salvage Tug beside the lifeboat, 'Quest complete: Wait for the Tug' (the page's own 20 seconds)"),
    "game_tug_log": ("game", "The Quest Log: Wait for the Tug Done, Bring the Log Home Active"),
    "game_win": ("game", "Helm, Game results with the Win sentence"),
    "game_broken": ("game", "Helm with the quote mark missing on line 25: Mast Compiler Errors (no probe change)"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_rules": ("card", "points", {"kicker": "Three rules for story.mast, from Lecture 7", "items": [
        "Change only what is between the quote marks.", "Never touch a quote mark.", "Leave the commas."]}),
    "card_cards": ("card", "points", {"kicker": "Your recipe cards", "items": [
        "Card 1: when a step starts", "Card 2: finish a step", "Card 3: wait"]}),
    "card_cannot": ("card", "table", {"heading": "What lint cannot see", "kicker": "Lint says clean, and", "rows": (1, 2)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 12", "sub": "Ship a quest mission"}),
}

_NEVER = "this line never runs"
# on the game's windows (fractions of the 4:3 picture); set from the screenshots
_ROW1 = ("rect", 0.02, 0.362, 0.38, 0.432)
_ROW4 = ("rect", 0.02, 0.575, 0.38, 0.642)
_MSG = ("rect", 0.015, 0.488, 0.275, 0.56)
_BOAT_ICON = ("rect", 0.425, 0.473, 0.465, 0.52)        # game_wait_map: the lifeboat
_TUG = ("rect", 0.385, 0.475, 0.48, 0.55)               # game_tug_map: the tug, its name and the lifeboat
_SENTENCE = ("rect", 0.012, 0.215, 0.25, 0.287)
_LOGS = ("rect", 0.035, 0.157, 0.222, 0.209)           # e_logs: the two logs in the file list
_HEAD = ("rect", 0.0, 0.066, 0.96, 0.128)               # game_broken: the heading sentence
_LINE25 = ("rect", 0.0, 0.19, 0.46, 0.288)              # game_broken: the error and its line

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_tug_map", "marks": [_TUG]},
        {"from": 2, "still": "m_top"},
        {"from": 4, "still": "m_card3", "marks": [("lines", 108, 115)]},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_two_files_two_sets_of_marks": {"step": None, "beats": [
        {"from": 0, "still": "e_top"},
        {"from": 1, "still": "e_top", "marks": [("hashes", 10)]},
        {"from": 2, "still": "e_top", "marks": [("text", 12, "//"), ("text", 13, "//"), ("text", 14, "//")]},
        {"from": 3, "still": "m_tail"},
        {"from": 4, "still": "m_tail", "marks": [("lines", 99, 102)]},
        {"from": 5, "still": "m_tail", "marks": [("text", 103, "//science")]},
        {"from": 6, "still": "m_tail", "marks": [("lines", 103, 105)]},
        {"from": 7, "still": "m_tail", "marks": [("lines", 99, 102)]},
        {"from": 8, "still": "card_rules"},
        {"from": 9, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 10, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 12, "still": "card_rules"},
    ]},
    "s03_read_the_file_the_top": {"step": 1, "beats": [
        {"from": 0, "still": "m_top", "marks": [("lines", 1, 10)]},
        {"from": 1, "still": "m_top", "marks": [("lines", 12, 12)]},
        {"from": 2, "still": "m_top", "marks": [("text", 12, "shared")]},
        {"from": 3, "still": "m_top", "marks": [("lines", 16, 16)]},
        {"from": 4, "still": "m_top", "marks": [("lines", 18, 20)]},
        {"from": 5, "still": "m_top", "marks": [("lines", 22, 22)]},
        {"from": 6, "still": "m_top", "marks": [("lines", 25, 25)]},
        {"from": 7, "still": "m_top", "marks": [("text", 25, "@map/amd_sample")]},
        {"from": 8, "still": "m_under", "marks": [("lines", 31, 53)]},
    ]},
    "s04_read_the_file_the_lines_that": {"step": None, "beats": [
        {"from": 0, "still": "m_35", "marks": [("lines", 35, 35)]},
        {"from": 1, "still": "m_load", "marks": [("lines", 54, 54), ("lines", 56, 57)]},
        {"from": 2, "still": "m_load", "marks": [("text", 54, "\"landmarks\""), ("text", 56, "\"quests\""), ("text", 57, "\"scans\"")]},
        {"from": 3, "still": "m_load", "marks": [("text", 54, "\"landmarks\"")]},
        {"from": 4, "still": "e_land", "marks": [("text", 161, "(landmarks)")]},
        {"from": 5, "still": "m_load", "marks": [("text", 54, "\"landmarks\"")]},
        {"from": 7, "still": "m_load", "marks": [("lines", 44, 44), ("lines", 48, 49), ("lines", 62, 62)]},
        {"from": 9, "still": "m_hulk", "marks": [("lines", 64, 64), ("lines", 68, 68)]},
        {"from": 10, "still": "m_hulk", "marks": [("text", 68, "ghost_ship")]},
        {"from": 11, "still": "m_hulk", "marks": [("text", 79, "->END")]},
    ]},
    "s05_read_the_file_the_indent_and": {"step": None, "beats": [
        {"from": 0, "still": "m_hulk"},
        {"from": 1, "still": "m_hulk", "marks": [("lines", 64, 79)]},
        {"from": 3, "still": "m_hulk", "marks": [("text", 79, "->END")]},
        {"from": 5, "still": "m_tail", "marks": [("lines", 89, 96), ("lines", 103, 105)]},
        {"from": 6, "still": "m_tail", "marks": [("lines", 93, 93), ("lines", 104, 104)]},
        {"from": 7, "still": "m_tail", "marks": [("text", 93, "\"ghost_ship_found\"")]},
        {"from": 9, "still": "e_find", "marks": [("text", 35, "signal ghost_ship_found")]},
        {"from": 11, "still": "m_tail", "marks": [("lines", 93, 93)]},
    ]},
    "s06_your_first_edit": {"step": 2, "beats": [
        {"from": 0, "still": "m_25"},
        {"from": 1, "still": "m_25", "marks": [("text", 25, "\"AMD Sample\"")]},
        {"from": 2, "still": "m_name", "marks": [("text", 25, "\"Salvage Run\"")]},
        {"from": 3, "still": "m_title", "marks": [("lines", 26, 26)]},
        {"from": 4, "still": "m_title", "marks": [("text", 26, "\""), ("after", 26)]},
        {"from": 6, "still": "m_title", "marks": [("lines", 26, 26)]},
    ]},
    "s07_one_check_two_files": {"step": 3, "beats": [
        {"from": 0, "still": "t_title", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_title", "marks": [("span", 1, "1 amd + 1 mast file(s)")]},
        {"from": 2, "still": "t_title", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "m_q25", "marks": [("after", 25)]},
        {"from": 5, "still": "t_q25", "marks": [("out", 1, 3), ("span", 1, "line 25")]},
        {"from": 6, "still": "t_q25", "marks": [("span", 1, "Unrecognized syntax; no MAST node matched this line")]},
        {"from": 7, "still": "t_q25", "marks": [("span", 1, "NOTHING in this mission runs until this is fixed")]},
        {"from": 9, "still": "game_broken"},
        {"from": 10, "still": "game_broken", "marks": [_HEAD]},
        {"from": 11, "still": "game_broken", "marks": [_LINE25]},
        {"from": 13, "still": "t_q25_fix", "marks": [("part", "run2:clean")]},
    ]},
    "s08_a_step_that_waits_for_the_sc": {"step": 4, "beats": [
        {"from": 0, "still": "e_w0", "marks": [("lines", 59, 59), ("lines", 72, 72), ("lines", 85, 85)]},
        {"from": 2, "still": "e_then", "marks": [("text", 79, "salvage/tug")]},
        {"from": 4, "still": "e_wait", "marks": [("lines", 90, 90)]},
        {"from": 5, "still": "e_wait", "marks": [("text", 90, "tug_arrived")]},
        {"from": 6, "still": "t_wait", "marks": [("out", 1, 2)]},
        {"from": 7, "still": "t_wait", "marks": [("span", 1, "nothing in the mission sends it")]},
        {"from": 8, "still": "t_wait", "marks": [("out", 1, 2)]},
    ]},
    "s09_card_one_when_a_step_starts": {"step": 5, "beats": [
        {"from": 0, "still": "m_end0", "marks": [("after", 105)]},
        {"from": 2, "still": "m_c_note", "marks": [("lines", 108, 110)]},
        {"from": 2.6, "still": "m_c_route", "marks": [("lines", 111, 111)]},
        {"from": 3, "still": "m_c_route", "marks": [("text", 111, "//shared/signal/quest_started")]},
        {"from": 6, "still": "m_c_route", "marks": [("text", 111, "\"salvage/tug\"")]},
        {"from": 7, "still": "e_then", "marks": [("text", 79, "salvage/tug")]},
        {"from": 8, "still": "m_card1", "marks": [("lines", 112, 112)]},
        {"from": 10, "still": "m_hulk", "marks": [("lines", 68, 68)]},
        {"from": 11, "still": "m_card1", "marks": [("text", 112, "5600, 0, 6000"), ("text", 112, "\"Salvage Tug\"")]},
        {"from": 12, "still": "m_card1", "marks": [("text", 112, "\"tsn, tug\"")]},
        {"from": 13, "still": "m_card1", "marks": [("text", 112, "\"cargo_ship\"")]},
        {"from": 14, "still": "e_boat", "marks": [("lines", 176, 183)]},
        {"from": 16, "still": "m_card1", "marks": [("text", 113, "->END")]},
    ]},
    "s10_cards_two_and_three": {"step": 6, "beats": [
        {"from": 0, "still": "m_tail", "marks": [("lines", 93, 93)]},
        {"from": 1, "still": "m_card2", "marks": [("text", 113, "\"tug_arrived\"")]},
        {"from": 2, "still": "m_card2", "marks": [("lines", 112, 113)]},
        {"from": 3, "still": "t_card2", "marks": [("part", "run2:clean")]},
        {"from": 4, "still": "m_card3", "marks": [("lines", 112, 112)]},
        {"from": 5, "still": "m_card3", "marks": [("lines", 112, 112), ("lines", 113, 113), ("lines", 114, 114)]},
        {"from": 7, "still": "e_words", "marks": [("lines", 16, 16), ("lines", 19, 19)]},
        {"from": 8, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s11_four_mistakes": {"step": 8, "beats": [
        {"from": 0, "still": "m_card3", "marks": [("lines", 108, 115)]},
        {"from": 1, "still": "m_indent", "marks": [("lines", 113, 113)]},
        {"from": 2, "still": "t_indent", "marks": [("span", 1, "line 113"), ("span", 1, "Bad indentation")]},
        {"from": 3, "still": "m_low", "marks": [("lines", 115, 115)]},
        {"from": 4, "still": "t_low", "marks": [("span", 1, "[WARNING]")]},
        {"from": 5, "still": "t_low", "marks": [("span", 1, _NEVER)]},
        {"from": 6, "still": "t_low", "marks": [("span", 1, "[WARNING]")]},
        {"from": 8, "still": "m_mid", "marks": [("lines", 64, 71)]},
        {"from": 9, "still": "t_mid", "marks": [("span", 1, _NEVER)]},
        {"from": 10, "still": "t_mid", "marks": [("span", 1, "line 73")]},
        {"from": 11, "still": "t_mid", "marks": [("span", 1, "move it above line 71")]},
        {"from": 12, "still": "m_mid", "marks": [("lines", 73, 73)]},
        {"from": 13, "still": "m_mid", "marks": [("lines", 64, 71)], "dim": True},
        {"from": 15, "still": "t_mid", "marks": [("span", 1, "move what you pasted to the end of the file")]},
        {"from": 16, "still": "m_addr", "marks": [("text", 111, "\"salvage/tgu\"")]},
        {"from": 17, "still": "t_addr", "marks": [("part", "run1:clean")]},
        {"from": 18, "still": "m_addr", "marks": [("text", 111, "\"salvage/tgu\"")]},
        {"from": 19, "still": "card_cannot"},
    ]},
    "s12_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_wait_map", "marks": [_BOAT_ICON, _MSG]},
        {"from": 1, "still": "game_wait_log", "marks": [_ROW1]},
        {"from": 2, "still": "game_tug_map", "marks": [_TUG]},
        {"from": 3, "still": "game_tug_log", "marks": [_ROW4, _ROW1]},
        {"from": 4, "still": "game_win", "marks": [_SENTENCE]},
        {"from": 5, "still": "e_logs", "marks": [_LOGS], "move": False},
    ]},
    "s13_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_cards"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_next"},
    ]},
}
