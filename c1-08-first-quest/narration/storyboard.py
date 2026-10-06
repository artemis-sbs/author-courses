"""Storyboard for c1-08-first-quest: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5, 6 and 7. The lecture starts from Lecture 7's finished files and ends on its own
example\\, both files, byte for byte.
"""
LECTURE = "c1-08-first-quest"
TITLE = ("Class 1, Lecture 8", "Your first quest", "A verb, a role, a number")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_RECORD = [
    "### [Close Inspection](approach)",
    "---",
    "Scope: shared",
    "Starts when: at once",
    "Objective: Close to within 500 of the hulk",
    "Done when: reach derelict 500",
    "Reward: 100 credits",
    "---",
    "The hulk is not answering hails. Bring the ship in close and take a look.",
]
_SPOT = "Science should take a full scan of the hull.\n\n\n// ---- Science scans."


def _typed(n):
    """The first n lines of the record, typed on the blank line above the Science scans note."""
    return ("replace", FILE, _SPOT, "Science should take a full scan of the hull.\n\n"
            + "\n".join(_RECORD[:n]) + "\n\n// ---- Science scans.")


STATES = {
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example")},
    **{f"q{n}": {"base": "start", "edits": [_typed(n)]} for n in range(1, 9)},
    "final": {"base": "start", "edits": [_typed(9)],
              "same_as": ("c1-08-first-quest/example/mission.amd", "c1-08-first-quest/example/story.mast")},
    # Step 5: two slips lint catches, and one it does not
    "sl1": {"base": "final", "edits": [("replace", FILE, "Done when: reach derelict 500", "When: reach derelict 500")]},
    "sl2": {"base": "final", "edits": [("replace", FILE, "reach derelict 500", "reach derelect 500")]},
    "sl3": {"base": "final", "edits": [("replace", FILE, "Starts when: at once\nObjective", "Objective")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    "e_quests": ("vscode", "start", 24, "big", _NS),      # lines 14 to 34: the section and its story
    "e_fc": ("vscode", "start", 34, "mid", _NS),          # lines 20 to 48: the whole Quests section
    "e_spot": ("vscode", "start", 46, "big", _NS),        # lines 36 to 56
    # the record as it is typed: every still looks at the same lines (41 to 61), so only the new line changes
    "e_q1": ("vscode", "q1", 51, "big", _NS),
    "e_q2": ("vscode", "q2", 51, "big", _NS),
    "e_q3": ("vscode", "q3", 51, "big", _NS),
    "e_q4": ("vscode", "q4", 51, "big", _NS),
    "e_q5": ("vscode", "q5", 51, "big", _NS),
    "e_q6": ("vscode", "q6", 51, "big", _NS),
    "e_q7": ("vscode", "q7", 51, "big", _NS),
    "e_q8": ("vscode", "q8", 51, "big", _NS),
    "e_q9": ("vscode", "final", 51, "big", _NS),
    "e_done": ("vscode", "final", 52, "big", _NS),        # lines 42 to 62
    "e_sl1": ("vscode", "sl1", 52, "big", _NS),
    "e_sl2": ("vscode", "sl2", 52, "big", _NS),
    "e_sl3": ("vscode", "sl3", 50, "big", _NS),
    "m_hulk": ("vscode", "final", 68, "mid", _M),
    "m_signal": ("vscode", "final", 93, "mid", _M),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_sl1": ("terminal", [("sl1", _LINT)]),
    "t_sl2": ("terminal", [("sl2", _LINT)]),
    "t_sl3": ("terminal", [("sl3", _LINT)]),
    "game_start": ("game", "Helm, the Quest Log at the start, Close Inspection selected"),
    "game_helm": ("game", "Helm, the console itself"),
    "game_2000": ("game", "Helm, the Quest Log: Find and Study done, Close Inspection still Active"),
    "game_done": ("game", "Helm, the Quest Log: Close Inspection selected, Done"),
    "card_title": ("card", "title", {}),
    "card_cannot": ("card", "table", {"heading": "What lint cannot see", "kicker": "Lint says clean, and",
                                      "rows": (5, 7, 9, 1)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_verbs": ("card", "table", {"heading": "Other built-in verbs", "kicker": "Five verbs are built in"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 9", "sub": "Chains and trees"}),
}

_REC = [("lines", 47, 55)]
# on the game's Quest Log (fractions of the 4:3 picture); set from the screenshots
_ROW_FIND = ("rect", 0.02, 0.290, 0.38, 0.358)         # game_2000: Find the Derelict, the second step row
_MINE3 = ("rect", 0.0, 0.292, 0.38, 0.362)             # Close Inspection when one step is listed above it
_MINE4 = ("rect", 0.0, 0.361, 0.38, 0.431)             # ... and when two are
_PANE = ("rect", 0.383, 0.074, 0.99, 0.21)             # State, Reward, the objective, the description

# Re-fitted on 2026-10-05 to the narration written for the ear (68 pieces, where there were
# 49 sentences). Same stills and marks; each beat now starts on the piece that says it.
BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_done", "marks": [_MINE4]},
        {"from": 1, "still": "e_q9", "marks": _REC, "dim": True},
        {"from": 2, "still": "card_title"},
    ]},
    "s02_where_quests_live": {"step": 1, "beats": [
        {"from": 0, "still": "e_quests"},
        {"from": 1, "still": "e_quests", "marks": [("hashes", 20)]},
        {"from": 2, "still": "e_fc", "marks": [("lines", 20, 20)]},
        {"from": 3, "still": "e_fc", "marks": [("lines", 22, 45)]},
        {"from": 4, "still": "e_fc", "marks": [("lines", 22, 22), ("lines", 30, 30), ("lines", 39, 39)]},
        {"from": 5, "still": "e_spot", "marks": [("lines", 46, 46), ("lines", 48, 48)]},
    ]},
    "s03_write_it": {"step": 3, "beats": [
        {"from": 0, "still": "e_q1", "marks": [("hashes", 47)]},
        {"from": 1, "still": "e_q1", "marks": [("text", 47, "[Close Inspection]"), ("text", 47, "(approach)")]},
        {"from": 2, "still": "e_q2", "marks": [("lines", 48, 48)]},
        {"from": 3, "still": "e_q3", "marks": [("lines", 49, 49)]},
        {"from": 4, "still": "e_q4", "marks": [("lines", 50, 50)]},
        {"from": 5, "still": "e_q5", "marks": [("lines", 51, 51)]},
        {"from": 6, "still": "e_q6", "marks": [("lines", 52, 52)]},
        {"from": 7, "still": "e_q7", "marks": [("lines", 53, 53)]},
        {"from": 7.55, "still": "e_q8", "marks": [("lines", 54, 54)]},
        {"from": 8, "still": "e_q9", "marks": [("lines", 55, 55)]},
    ]},
    "s04_the_line_that_matters": {"step": 4, "beats": [
        {"from": 0, "still": "e_done", "marks": [("lines", 52, 52)], "dim": True},
        {"from": 1, "still": "e_done", "marks": [("text", 52, "reach"), ("text", 52, "derelict"), ("text", 52, "500")]},
        {"from": 2, "still": "e_done", "marks": [("text", 52, "reach")]},
        {"from": 3, "still": "e_done", "marks": [("text", 52, "500")]},
        {"from": 4, "still": "e_done", "marks": [("text", 52, "derelict")]},
        {"from": 6, "still": "m_hulk", "marks": [("text", 68, "\"tsn, derelict, ghost_ship\"")]},
        {"from": 7, "still": "m_hulk", "marks": [("text", 68, "tsn")]},
        {"from": 7.4, "still": "m_hulk", "marks": [("text", 68, "derelict"), ("text", 68, "ghost_ship")]},
        {"from": 8, "still": "m_hulk", "marks": [("text", 68, "derelict")]},
        {"from": 10, "still": "e_done", "marks": [("text", 52, "reach")]},
        {"from": 11, "still": "m_signal", "marks": [("text", 93, "\"ghost_ship_found\"")]},
        {"from": 13, "still": "e_done", "marks": [("text", 52, "reach")]},
        {"from": 14, "still": "e_done", "marks": [("lines", 52, 52)]},
        {"from": 15, "still": "m_hulk"},
    ]},
    "s05_getting_it_wrong": {"step": 5, "beats": [
        {"from": 0, "still": "e_done", "marks": [("lines", 52, 52)]},
        {"from": 1, "still": "e_sl1", "marks": [("text", 52, "When:")]},
        {"from": 2, "still": "t_sl1", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "e_sl2", "marks": [("text", 52, "derelect")]},
        {"from": 5, "still": "t_sl2", "marks": [("out", 1, 2)]},
        {"from": 6, "still": "e_done", "marks": [("lines", 50, 50)]},
        {"from": 7, "still": "e_sl3", "marks": [("lines", 49, 50)]},
        {"from": 8, "still": "t_sl3", "marks": [("part", "run1:clean")]},
        {"from": 10, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 12, "still": "card_cannot", "marks": [("part", "r2c1")]},
        {"from": 12.5, "still": "card_cannot", "marks": [("part", "r3c1")]},
        {"from": 13, "still": "card_cannot", "marks": [("part", "r4c1")]},
    ]},
    "s06_check_it": {"step": None, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_final", "marks": [("part", "run1:clean"), ("part", "run1:last")]},
    ]},
    "s07_play_it": {"step": 6, "beats": [
        {"from": 0, "still": "game_start", "marks": [_MINE3]},
        {"from": 1, "still": "game_start", "marks": [_PANE]},
        {"from": 2, "still": "game_helm"},
        {"from": 3, "still": "game_2000", "marks": [_ROW_FIND]},
        {"from": 5, "still": "game_2000", "marks": [_MINE4]},
        {"from": 6, "still": "game_helm"},
        {"from": 7, "still": "game_done", "marks": [_MINE4, _PANE]},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_verbs", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_verbs"},
        {"from": 5, "still": "card_next"},
    ]},
}
