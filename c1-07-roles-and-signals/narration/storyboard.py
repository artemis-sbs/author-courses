"""Storyboard for c1-07-roles-and-signals: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in c1-05's and c1-06's
storyboard.py. New here: ("card", "search", {"state", "word", "want": (hits, files)}) counts
the word in the state's own files (match case, whole word) and draws the result plainly;
"want" is what the script says, and a different count stops the run.

The lecture starts from Lecture 5's finished file (Lecture 6 leaves the file as it found
it) and ends on this lecture's own example\\, both files, byte for byte.
"""
LECTURE = "c1-07-roles-and-signals"
TITLE = ("Class 1, Lecture 7", "Roles and signals", "The words your two files share")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"
LOG = "mast.runtime.log"

_LIST = [
    "// ---- Words this file shares with story.mast. Keep this list true.",
    "// ROLE    derelict          worn by the Unknown Hulk",
    "// ROLE    ghost_ship        worn by the Unknown Hulk",
    "// SIGNAL  ghost_ship_found  said when a ship comes within 2000 of the hulk",
    "// SIGNAL  derelict_scanned  said when Science scans anything that wears derelict",
]
_TITLE_LINE = "# [Sample Mission](sample_mission)\n"


def _listed(n):
    return ("replace", FILE, _TITLE_LINE, _TITLE_LINE + "\n" + "\n".join(_LIST[:n]) + "\n")


STATES = {
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "over": ("c1-05-the-shape-of-a-record/example",)},
    # Step 4: the reading points at a role nobody wears, then the hulk is given it
    "r1": {"base": "start", "edits": [("replace", FILE, "Scan of: derelict\nTab: intel", "Scan of: ghost_ship\nTab: intel")]},
    "r2": {"base": "r1", "edits": [("replace", MAST, '"tsn, derelict"', '"tsn, derelict, ghost_ship"')]},
    # Step 5: the step waits for a new word, then the story says it, then the note is made true
    "s1": {"base": "r2", "edits": [("replace", FILE, "Done when: signal derelict_found", "Done when: signal ghost_ship_found")]},
    "s2": {"base": "s1", "edits": [("replace", MAST, '{"SIGNAL_NAME": "derelict_found"}', '{"SIGNAL_NAME": "ghost_ship_found"}')]},
    "s3": {"base": "s2", "edits": [
        ("replace", MAST, 'signal_emit("derelict_found")', 'signal_emit("ghost_ship_found")'),
        ("replace", MAST, "`//signal/derelict_found`", "`//signal/ghost_ship_found`")]},
    # Step 6: the word list, a line at a time
    "wl1": {"base": "s3", "edits": [_listed(1)]},
    "wl2": {"base": "s3", "edits": [_listed(2)]},
    "wl3": {"base": "s3", "edits": [_listed(3)]},
    "wl4": {"base": "s3", "edits": [_listed(4)]},
    "final": {"base": "s3", "edits": [_listed(5)],
              "same_as": ("c1-07-roles-and-signals/example/mission.amd", "c1-07-roles-and-signals/example/story.mast")},
    # scene 9: one slip lint catches, one it cannot
    "x1": {"base": "final", "edits": [("replace", MAST, '{"SIGNAL_NAME": "ghost_ship_found"}', '{"SIGNAL_NAME": "ghost_ship_fond"}')]},
    "x2": {"base": "final", "edits": [("replace", MAST, '"tsn, derelict, ghost_ship"', '"tsn, derelect, ghost_ship"')]},
    "played": {"base": "final", "edits": [("write", "mast.compile.log", ""), ("write", LOG, "")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # mission.amd
    "e_top": ("vscode", "start", 1, "big", _NS),
    "e_five": ("vscode", "start", 46, "wide", _NS),       # lines 27 to 65: the five lines that lean on the other file
    "e_scans": ("vscode", "start", 56, "big", _NS),       # lines 46 to 66
    "e_find": ("vscode", "start", 28, "big", _NS),
    "e_intel": ("vscode", "start", 60, "big", _NS),       # lines 50 to 67
    "e_r1": ("vscode", "r1", 60, "big", _NS),
    "e_find_r2": ("vscode", "r2", 28, "big", _NS),
    "e_s1": ("vscode", "s1", 28, "big", _NS),
    "e_title": ("vscode", "s3", 12, "big", _NS),          # the list as it is typed: every still looks at lines 2 to 22
    "e_wl1": ("vscode", "wl1", 12, "big", _NS),
    "e_wl2": ("vscode", "wl2", 12, "big", _NS),
    "e_wl3": ("vscode", "wl3", 12, "big", _NS),
    "e_wl4": ("vscode", "wl4", 12, "big", _NS),
    "e_wl5": ("vscode", "final", 12, "big", _NS),
    # story.mast: its lines are long, so the text is a size smaller
    "m_side": ("vscode", "start", 1, "wide", {"file": MAST}),      # with the file list: the scene is the click on it
    "m_mid": ("vscode", "start", 52, "wide", _M),
    "m_end": ("vscode", "start", 90, "wide", _M),
    "m_note": ("vscode", "start", 88, "mid", _M),         # lines 74 to 105: notes that start with #
    "m_hulk": ("vscode", "start", 68, "mid", _M),         # lines 54 to 83
    "m_sci": ("vscode", "start", 96, "mid", _M),
    "m_signal": ("vscode", "start", 93, "mid", _M),       # lines 79 to 105
    "m_r2": ("vscode", "r2", 68, "mid", _M),
    "m_s2": ("vscode", "s2", 93, "mid", _M),
    "m_s3": ("vscode", "s3", 93, "mid", _M),
    "m_x1": ("vscode", "x1", 93, "mid", _M),
    "m_final68": ("vscode", "final", 68, "mid", _M),
    "m_x2": ("vscode", "x2", 68, "mid", _M),
    "m_x2_sci": ("vscode", "x2", 96, "mid", _M),
    "e_log_empty": ("vscode", "played", 1, "close", {"file": LOG}),
    # the Command Prompt
    "t_r1": ("terminal", [("r1", _LINT)]),
    "t_r2": ("terminal", [("r1", _LINT), ("r2", _LINT)]),
    "t_s1": ("terminal", [("s1", _LINT)]),
    "t_s2": ("terminal", [("s1", _LINT), ("s2", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_x1": ("terminal", [("x1", _LINT)]),
    "t_x2": ("terminal", [("x2", _LINT)]),
    # a search of the folder, counted and drawn
    "c_derelict": ("card", "search", {"state": "start", "word": "derelict", "want": (8, 2)}),
    "c_found": ("card", "search", {"state": "start", "word": "derelict_found", "want": (4, 2)}),
    "c_scanned": ("card", "search", {"state": "start", "word": "derelict_scanned", "want": (2, 2)}),
    "c_found_s1": ("card", "search", {"state": "s1", "word": "derelict_found", "want": (3, 1)}),
    "c_found_gone": ("card", "search", {"state": "s3", "word": "derelict_found", "want": (0, 0)}),
    "c_ghost_found": ("card", "search", {"state": "s3", "word": "ghost_ship_found", "want": (4, 2)}),
    "c_derelict_x2": ("card", "search", {"state": "x2", "word": "derelict", "want": (8, 2)}),
    # the real game
    "game_quests": ("game", "Helm, the Quest Log after the ship reached the hulk"),
    "game_science": ("game", "Science, the hulk selected: three tabs"),
    "game_intel": ("game", "Science, the hulk's intel tab"),
    "game_x2": ("game", "Helm, the Quest Log with derelect on line 68: Study the Derelict stays Active"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_files": ("card", "table", {"heading": "Step 1 - Two files, three promises", "kicker": "Two files that have to agree"}),
    "card_rules": ("card", "list", {"heading": "Step 1 - Two files, three promises", "kicker": "Three rules for story.mast"}),
    "card_word_rules": ("card", "list", {"heading": "Step 4 - Name a role", "kicker": "Four rules for a role or a signal"}),
    "card_cannot": ("card", "table", {"heading": "What lint cannot see", "kicker": "Lint says clean, and", "rows": (1, 2, 3, 4)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 8", "sub": "Your first quest"}),
}

_FILE_ROW = ("rect", 0.03, 0.279, 0.222, 0.306)        # story.mast in the file list
# on the game's windows (fractions of the 4:3 picture)
_ROW2 = ("rect", 0.02, 0.215, 0.38, 0.285)             # the first step under First Contact in the Quest Log
_ROW3 = ("rect", 0.02, 0.288, 0.38, 0.358)             # the second
_TABS = ("rect", 0.697, 0.05, 0.937, 0.093)            # scan, intel, mat on Science
_INTEL_TAB = ("rect", 0.778, 0.05, 0.86, 0.093)
_READING = ("rect", 0.695, 0.388, 0.998, 0.448)
_LOGS = ("rect", 0.035, 0.157, 0.222, 0.209)           # the two logs in the file list (as in Lecture 6)

# Re-fitted on 2026-10-05 to the narration written for the ear (136 pieces, where there were
# 98 sentences). Same stills and marks; each beat now starts on the piece that says it.
# Re-fitted on 2026-10-05 to the narration written for the ear (136 pieces, where there were
# 98 sentences). Same stills and marks; each beat now starts on the piece that says it.
BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "c_derelict", "marks": [("part", "word")]},
        {"from": 0.4, "still": "c_derelict", "marks": [("part", "file1"), ("part", "file2")]},
        {"from": 0.75, "still": "c_derelict", "marks": [("part", "summary")]},
        {"from": 1, "still": "c_derelict", "marks": [("part", "file1")]},
        {"from": 2, "still": "c_derelict", "marks": [("part", "file2")]},
        {"from": 3, "still": "card_title"},
    ]},
    "s02_two_files_three_promises": {"step": 1, "beats": [
        {"from": 0, "still": "e_scans"},
        {"from": 1, "still": "m_hulk"},
        {"from": 2, "still": "e_five", "marks": [("lines", 28, 28), ("lines", 37, 37), ("lines", 49, 49),
                                                 ("lines", 57, 57), ("lines", 64, 64)]},
        {"from": 3, "still": "e_scans", "marks": [("text", 49, "derelict"), ("text", 57, "derelict"), ("text", 64, "derelict")]},
        {"from": 4, "still": "m_hulk", "marks": [("text", 68, "derelict")]},
        {"from": 6, "still": "e_find", "marks": [("text", 28, "derelict_found")]},
        {"from": 7, "still": "m_signal", "marks": [("text", 93, "\"derelict_found\"")]},
        {"from": 8, "still": "e_find", "marks": [("text", 28, "signal derelict_found"), ("text", 37, "signal derelict_scanned")]},
        {"from": 9, "still": "card_files", "marks": [("part", "r2")]},
    ]},
    "s03_open_the_other_file": {"step": None, "beats": [
        {"from": 0, "still": "m_side", "marks": [_FILE_ROW]},
        {"from": 1, "still": "m_mid"},
        {"from": 1.5, "still": "m_end"},
        {"from": 2, "still": "card_rules"},
        {"from": 3, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 4, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 5, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 6, "still": "m_note", "marks": [("hashes", n) for n in (82, 83, 84, 85, 86, 87, 88)]},
        {"from": 7, "still": "e_top", "marks": [("text", n, "//") for n in (1, 2, 3, 4, 5, 6, 7, 8)]},
    ]},
    "s04_find_the_role": {"step": 2, "beats": [
        {"from": 0, "still": "c_derelict", "marks": [("part", "word")]},
        # added: the hits themselves, while the voice says what the two switches are for
        {"from": 2, "still": "c_derelict", "marks": [("part", f"hit{n}") for n in range(1, 9)]},
        {"from": 3, "still": "c_derelict", "marks": [("part", "summary")]},
        {"from": 4, "still": "c_derelict", "marks": [("part", "file1")]},
        {"from": 5, "still": "c_derelict", "marks": [("part", "file2")]},
        {"from": 6, "still": "c_derelict", "marks": [("part", "f2h1"), ("part", "f2h2"), ("part", "f2h4")]},
        {"from": 7, "still": "c_derelict", "marks": [("part", "f2h3"), ("part", "f2h5")]},
        {"from": 8, "still": "m_hulk", "marks": [("lines", 68, 68)]},
        {"from": 9, "still": "m_hulk", "marks": [("text", 68, "\"Unknown Hulk\""), ("text", 68, "\"tsn, derelict\""),
                                                 ("text", 68, "\"tsn_warpster\""), ("text", 68, "\"behav_npcship\"")]},
        {"from": 10, "still": "m_hulk", "marks": [("text", 68, "\"Unknown Hulk\"")]},
        {"from": 10.6, "still": "m_hulk", "marks": [("text", 68, "\"tsn, derelict\"")]},
        {"from": 11, "still": "m_hulk", "marks": [("text", 68, "\"tsn_warpster\"")]},
        {"from": 11.4, "still": "m_hulk", "marks": [("text", 68, "\"behav_npcship\"")]},
        {"from": 12, "still": "m_hulk", "marks": [("text", 68, "\"tsn, derelict\"")]},
        {"from": 13, "still": "m_hulk", "marks": [("text", 68, "tsn")]},
        {"from": 14, "still": "m_hulk", "marks": [("text", 68, "derelict")]},
        {"from": 15, "still": "m_hulk", "marks": [("text", 68, "tsn"), ("text", 68, "derelict")]},
        {"from": 17, "still": "m_sci", "marks": [("text", 103, "\"derelict\"")]},
    ]},
    "s05_find_the_signals": {"step": 3, "beats": [
        {"from": 0, "still": "c_found", "marks": [("part", "summary")]},
        {"from": 1, "still": "c_found", "marks": [("part", "f1h1")]},
        {"from": 2, "still": "c_found", "marks": [("part", "f2h1"), ("part", "f2h2")]},
        {"from": 3, "still": "c_found", "marks": [("part", "f2h3")]},
        {"from": 4, "still": "m_signal", "marks": [("text", 93, "\"quest_signal\""), ("text", 93, "\"SIGNAL_NAME\""),
                                                   ("text", 93, "\"derelict_found\"")]},
        {"from": 5, "still": "m_signal", "marks": [("text", 93, "\"derelict_found\"")]},
        {"from": 6, "still": "m_signal", "marks": [("text", 93, "\"quest_signal\""), ("text", 93, "\"SIGNAL_NAME\"")]},
        {"from": 8, "still": "m_signal", "marks": [("lines", 89, 92)]},
        {"from": 10, "still": "m_signal", "marks": [("lines", 82, 88)]},
        {"from": 11, "still": "c_scanned", "marks": [("part", "summary")]},
        {"from": 12, "still": "m_sci", "marks": [("lines", 103, 103), ("lines", 104, 104)]},
        {"from": 13, "still": "m_sci", "marks": [("text", 104, "\"derelict_scanned\"")]},
    ]},
    "s06_name_a_role": {"step": 4, "beats": [
        {"from": 0, "still": "e_intel", "marks": [("lines", 62, 67)]},
        {"from": 2, "still": "e_r1", "marks": [("text", 64, "ghost_ship")]},
        {"from": 3, "still": "t_r1", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "t_r1", "marks": [("span", 1, "nothing in this mission wears a role called `ghost_ship`")]},
        {"from": 5, "still": "t_r1", "marks": [("span", 1, "so this scan text matches nothing")]},
        {"from": 6, "still": "m_hulk", "marks": [("text", 68, "\"tsn, derelict\"")]},
        {"from": 7, "still": "m_hulk", "marks": [("text", 68, "\"", 4)]},
        {"from": 8, "still": "m_r2", "marks": [("text", 68, ", ghost_ship")]},
        {"from": 9, "still": "t_r2", "marks": [("part", "run2:clean")]},
        {"from": 9.45, "still": "m_r2", "marks": [("text", 68, "derelict"), ("text", 68, "ghost_ship")]},
        {"from": 10, "still": "card_word_rules"},
        {"from": 11, "still": "card_word_rules", "marks": [("part", "item1")]},
        {"from": 12, "still": "card_word_rules", "marks": [("part", "item2")]},
        {"from": 13, "still": "card_word_rules", "marks": [("part", "item3")]},
        {"from": 14, "still": "card_word_rules", "marks": [("part", "item4")]},
    ]},
    "s07_rename_a_signal": {"step": 5, "beats": [
        {"from": 0, "still": "e_find_r2", "marks": [("lines", 28, 28)]},
        {"from": 1, "still": "e_s1", "marks": [("text", 28, "ghost_ship_found")]},
        {"from": 2, "still": "t_s1", "marks": [("span", 1, "`find` waits for the signal `ghost_ship_found`, and nothing in the mission sends it")]},
        {"from": 4, "still": "t_s1", "marks": [("span", 1, "so that wait never ends")]},
        {"from": 5, "still": "c_found_s1", "marks": [("part", "word")]},
        {"from": 6, "still": "c_found_s1", "marks": [("part", "summary"), ("part", "file1")]},
        {"from": 7, "still": "m_s2", "marks": [("text", 93, "\"ghost_ship_found\"")]},
        {"from": 9, "still": "t_s2", "marks": [("part", "run2:clean")]},
        {"from": 10, "still": "m_s3", "marks": [("text", 86, "ghost_ship_found"), ("text", 87, "ghost_ship_found")]},
        {"from": 11, "still": "m_s3", "marks": [("hashes", n) for n in (82, 83, 84, 85, 86, 87, 88)]},
        {"from": 12, "still": "c_found_gone", "marks": [("part", "word")]},
        {"from": 13, "still": "c_found_gone", "marks": [("part", "summary")]},
        {"from": 14, "still": "c_ghost_found", "marks": [("part", "summary")]},
        {"from": 15, "still": "c_ghost_found", "marks": [("part", "file1"), ("part", "file2")]},
    ]},
    "s08_the_word_list": {"step": 6, "beats": [
        {"from": 0, "still": "e_title", "marks": [("after", 10)]},
        {"from": 0.4, "still": "e_wl1"},
        {"from": 0.7, "still": "e_wl2"},
        {"from": 1, "still": "e_wl3"},
        {"from": 1.36, "still": "e_wl4"},
        {"from": 1.72, "still": "e_wl5"},
        {"from": 2, "still": "e_wl5", "marks": [("lines", 13, 14)]},
        {"from": 2.5, "still": "e_wl5", "marks": [("lines", 15, 16)]},
        {"from": 3, "still": "e_wl5", "marks": [("lines", 12, 16)]},
        {"from": 4, "still": "e_wl5", "marks": [("text", n, "//") for n in (12, 13, 14, 15, 16)]},
        {"from": 6, "still": "e_wl5", "marks": [("lines", 12, 16)]},
        {"from": 7.4, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s09_what_lint_cannot_see": {"step": 7, "beats": [
        {"from": 0, "still": "m_s3", "marks": [("text", 93, "\"ghost_ship_found\"")]},
        {"from": 1, "still": "m_x1", "marks": [("text", 93, "ghost_ship_fond")]},
        {"from": 2, "still": "t_x1", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "t_x1", "marks": [("span", 1, "nothing in the mission sends it")]},
        {"from": 5, "still": "m_final68", "marks": [("text", 68, "\"tsn, derelict, ghost_ship\"")]},
        {"from": 5.5, "still": "m_x2", "marks": [("text", 68, "derelect")]},
        {"from": 6, "still": "t_x2", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "m_x2_sci", "marks": [("text", 103, "\"derelict\"")]},
        {"from": 10, "still": "m_x2", "marks": [("text", 68, "\"tsn, derelect, ghost_ship\"")]},
        {"from": 11, "still": "game_x2", "marks": [_ROW2]},
        {"from": 14, "still": "c_derelict_x2", "marks": [("part", "summary")]},
        {"from": 16, "still": "card_cannot"},
        {"from": 17, "still": "card_cannot", "marks": [("part", "r1c1"), ("part", "r2c1")]},
    ]},
    "s10_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_quests"},
        {"from": 2, "still": "game_quests", "marks": [_ROW2]},
        {"from": 5, "still": "game_quests", "marks": [_ROW3]},
        {"from": 7, "still": "game_science", "marks": [_TABS]},
        {"from": 8, "still": "game_intel", "marks": [_INTEL_TAB, _READING]},
        {"from": 9, "still": "e_log_empty", "marks": [_LOGS]},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_next"},
    ]},
}
