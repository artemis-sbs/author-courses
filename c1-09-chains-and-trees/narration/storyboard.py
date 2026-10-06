"""Storyboard for c1-09-chains-and-trees: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6. Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-05).

THE FILE ON SCREEN. The lecture starts from Lecture 8's finished files, plus what the
script's "Before recording" table asks for: the student's own quest from Lecture 8's
exercise, typed under Close Inspection (here "Long Watch", keyed `watch`). It is on screen
from the first still to the last, because scene 4 points at it. The state "page" takes it
out again and must equal this lecture's example\\ byte for byte, so every line the picture
shows above it (lines 47 to 92) is the page's own line.
"""
LECTURE = "c1-09-chains-and-trees"
TITLE = ("Class 1, Lecture 9", "Chains and trees", "An arc, its steps, and two endings")
MISSION = "MyMission"
FILE = "mission.amd"

_CI = "### [Close Inspection](approach)"
_LOOK = "The hulk is not answering hails. Bring the ship in close and take a look.\n"
_WATCH = ("\n### [Long Watch](watch)\n---\nScope: shared\nStarts when: at once\n"
          "Objective: Keep station for two minutes\nDone when: 2 minutes\nReward: 25 credits\n---\n"
          "Hold your position and watch her for any sign of life.\n")
_ARC = [
    "### [Salvage Run](salvage)",
    "---",
    "Arc",
    "Scope: shared",
    "Starts when: at once",
    "---",
    "The hulk's reactor is failing. Get her flight log back to DS 1 before she goes.",
]
_HOME = [
    "#### [Bring the Log Home](home)",
    "---",
    "Scope: shared",
    "Starts when: revealed",
    "Objective: Return to within 1000 of DS 1",
    "Done when: reach station 1000",
    "Reward: 200 credits",
    "---",
    "You have her flight log. Carry it back to DS 1.",
]
_CARRY = "You have her flight log. Carry it back to DS 1.\n"
_QUICK = ("\n#### [Quick Work](quick)\n---\nScope: shared\nStarts when: at once\n"
          "Objective: Reach the hulk inside two minutes\nDone when: reach derelict 500\n"
          "Fails when: 2 minutes\nReward: 50 credits\n---\nOptional. DS 1 pays a bonus for a fast approach.\n")
_NEEDS = "Part of: salvage\nRequired: true\n"
_ENDS = ("Fails when: 10 minutes\nWin: The log is home. DS 1 knows what happened out there.\n"
         "Lose: The reactor let go with the log still aboard.\n")
_ARC_END = "Starts when: at once\n---\nThe hulk's reactor"


def _arc(n):
    """The first n lines of the arc's record, typed in front of Close Inspection."""
    return ("replace", FILE, "\n" + _CI, "\n" + "\n".join(_ARC[:n]) + "\n\n" + _CI)


def _home(n):
    """The first n lines of Bring the Log Home, typed under Close Inspection's description."""
    return ("replace", FILE, _LOOK, _LOOK + "\n" + "\n".join(_HOME[:n]) + "\n")


STATES = {
    "l8": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
           "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                    "c1-08-first-quest/example")},
    "start": {"base": "l8", "edits": [("replace", FILE, _LOOK, _LOOK + _WATCH)]},
    # Step 1: the arc's record
    "arc1": {"base": "start", "edits": [_arc(1)]},
    "arc3": {"base": "start", "edits": [_arc(3)]},
    "arc6": {"base": "start", "edits": [_arc(6)]},
    "arc": {"base": "start", "edits": [_arc(7)]},
    # Step 2: one more hash
    "h4": {"base": "arc", "edits": [("replace", FILE, "\n" + _CI, "\n#" + _CI)]},
    # Step 3: the second step, then the line that starts it
    "home1": {"base": "h4", "edits": [_home(1)]},
    "home4": {"base": "h4", "edits": [_home(4)]},
    "home": {"base": "h4", "edits": [_home(9)]},
    "then": {"base": "home", "edits": [
        ("replace", FILE, "Reward: 100 credits\n", "Reward: 100 credits\nThen: reveal salvage/home\n")]},
    # Step 4: the bonus
    "quick": {"base": "then", "edits": [("replace", FILE, _CARRY, _CARRY + _QUICK)]},
    # Step 5: which steps count
    "req1": {"base": "quick", "edits": [
        ("replace", FILE, "Then: reveal salvage/home\n", "Then: reveal salvage/home\n" + _NEEDS)]},
    "req": {"base": "req1", "edits": [
        ("replace", FILE, "Reward: 200 credits\n", "Reward: 200 credits\n" + _NEEDS)]},
    # Step 6: two endings
    "end1": {"base": "req", "edits": [("replace", FILE, _ARC_END, "Starts when: at once\n" + _ENDS.split("\n")[0] + "\n---\nThe hulk's reactor")]},
    "end2": {"base": "req", "edits": [("replace", FILE, _ARC_END, "Starts when: at once\n" + "\n".join(_ENDS.split("\n")[:2]) + "\n---\nThe hulk's reactor")]},
    "final":{"base": "req", "edits": [("replace", FILE, _ARC_END, "Starts when: at once\n" + _ENDS + "---\nThe hulk's reactor")]},
    "page": {"base": "final", "edits": [("replace", FILE, _WATCH, "")],
             "same_as": ("c1-09-chains-and-trees/example/mission.amd", "c1-09-chains-and-trees/example/story.mast")},
    # scene 9: one hash too few
    "trap": {"base": "final", "edits": [("replace", FILE, "\n" + _HOME[0], "\n" + _HOME[0][1:])]},
    # scene 11: thirty seconds
    "lose30": {"base": "final", "edits": [("replace", FILE, "Fails when: 10 minutes", "Fails when: 30 seconds")]},
    # PROBE-ONLY, for the game stills, so nobody has to fly: "the ship is at the hulk" is
    # made true by widening the two distances, and "the ship is home" by widening the third.
    # Never shown in the editor.
    "g_hulk": {"base": "final", "edits": [
        ("replace", FILE, "of the hulk\nDone when: reach derelict 500", "of the hulk\nDone when: reach derelict 30000"),
        ("replace", FILE, "two minutes\nDone when: reach derelict 500", "two minutes\nDone when: reach derelict 30000")]},
    "g_win": {"base": "g_hulk", "edits": [
        ("replace", FILE, "Done when: reach station 1000", "Done when: reach station 30000")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}

STILLS = {
    # Lecture 8's quest, and the arc typed in front of it: every still looks at lines 41 to 61
    "e_ci": ("vscode", "start", 51, "big", _NS),
    "e_a1": ("vscode", "arc1", 51, "big", _NS),
    "e_a3": ("vscode", "arc3", 51, "big", _NS),
    "e_a6": ("vscode", "arc6", 51, "big", _NS),
    "e_a7": ("vscode", "arc", 51, "big", _NS),
    # one more hash: lines 45 to 65
    "e_h3": ("vscode", "arc", 55, "big", _NS),
    "e_h4": ("vscode", "h4", 55, "big", _NS),
    # the second step: lines 55 to 75, and a longer look (46 to 74) for whose step it is
    "e_gap": ("vscode", "h4", 65, "big", _NS),
    "e_h4_mid": ("vscode", "h4", 60, "mid", _NS),
    "e_home1": ("vscode", "home1", 65, "big", _NS),
    "e_home4": ("vscode", "home4", 65, "big", _NS),
    "e_home": ("vscode", "home", 65, "big", _NS),
    "e_then": ("vscode", "then", 62, "big", _NS),          # lines 52 to 72
    "e_quick": ("vscode", "quick", 80, "big", _NS),        # lines 70 to 90
    "e_steps": ("vscode", "quick", 68, "mid", _NS),        # lines 55 to 82: the three steps' headings
    "e_req1": ("vscode", "req1", 62, "big", _NS),
    "e_req": ("vscode", "req", 73, "mid", _NS),            # lines 59 to 87
    "e_arcs": ("vscode", "req", 36, "mid", _NS),           # lines 22 to 50: both arcs
    "e_end0": ("vscode", "req", 55, "big", _NS),           # lines 45 to 65
    "e_end1": ("vscode", "end1", 55, "big", _NS),
    "e_end2": ("vscode", "end2", 55, "big", _NS),
    "e_end": ("vscode", "final", 55, "big", _NS),
    "e_final": ("vscode", "final", 60, "mid", _NS),        # lines 47 to 74: the arc and two steps
    "e_final_home": ("vscode", "final", 71, "big", _NS),   # lines 61 to 81
    "e_trap": ("vscode", "trap", 71, "big", _NS),
    "e_trap_mid": ("vscode", "trap", 61, "mid", _NS),
    "e_lose": ("vscode", "lose30", 55, "big", _NS),
    # the Command Prompt: the real tool's answer for that state
    "t_home": ("terminal", [("home", _LINT)]),
    "t_then": ("terminal", [("home", _LINT), ("then", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_trap": ("terminal", [("trap", _LINT)]),
    # the real game (game.py; the sessions are listed in the report of 2026-10-05)
    "game_log": ("game", "Helm, the Quest Log at the start: Salvage Run with two steps, clocks running"),
    "game_arc": ("game", "The Quest Log, Salvage Run selected: its description, two steps, more to follow"),
    "game_helm": ("game", "Helm with 'Quest complete: Quick Work' (probe: the reach distances widened)"),
    "game_hulk": ("game", "The Quest Log at the hulk: two steps Done, Bring the Log Home Active (same probe)"),
    "game_home": ("game", "The Quest Log, Bring the Log Home selected (same probe)"),
    "game_win": ("game", "Helm, Game results with the Win sentence (probe: all three distances widened)"),
    "game_lose": ("game", "Helm, Game results with the Lose sentence (the page's own 30 seconds, nothing else changed)"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_first": ("card", "table", {"heading": "Step 4 - A step the crew can skip", "kicker": "Quick Work: whichever comes first"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn: a fourth step"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 10", "sub": "Things quests point at"}),
}

_WARN = "waits to be revealed, and nothing reveals it"
_WRITE = "`Then: reveal salvage/home`"
_OFFER = "write `Then: reveal home`"
# on the game's windows (fractions of the 4:3 picture); set from the screenshots
_TWO = ("rect", 0.02, 0.365, 0.38, 0.50)               # game_log: Close Inspection and Quick Work
_CLOCK = ("rect", 0.0, 0.322, 0.085, 0.358)            # game_log: "9:15 left" under Salvage Run
_QCLOCK = ("rect", 0.024, 0.466, 0.10, 0.502)          # game_log: "1:15 left" under Quick Work
_MORE = ("rect", 0.385, 0.17, 0.53, 0.208)             # game_arc: "... more to follow"
_ARC_PANE = ("rect", 0.385, 0.074, 0.95, 0.208)
_MSG = ("rect", 0.015, 0.488, 0.275, 0.528)            # game_helm: Quest complete: Quick Work
_DONE2 = ("rect", 0.02, 0.435, 0.38, 0.572)            # game_hulk: the two Done rows
_HOME_ROW = ("rect", 0.02, 0.362, 0.38, 0.432)         # game_hulk, game_home: Bring the Log Home
_HOME_PANE = ("rect", 0.385, 0.074, 0.75, 0.208)
_SENTENCE = ("rect", 0.012, 0.215, 0.25, 0.287)        # game_win, game_lose: the writer's sentence

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_ci", "marks": [("lines", 47, 55)]},
        {"from": 2, "still": "game_arc", "marks": [_ARC_PANE]},
        {"from": 3, "still": "game_win", "marks": [_SENTENCE]},
        {"from": 4, "still": "e_final"},
        {"from": 5, "still": "e_final", "marks": [("lines", 58, 69)]},
        {"from": 6.55, "still": "card_title"},
    ]},
    "s02_a_heading_for_the_story": {"step": 1, "beats": [
        {"from": 0, "still": "e_ci", "marks": [("hashes", 47)]},
        {"from": 1, "still": "e_a1", "marks": [("lines", 47, 47)]},
        {"from": 2, "still": "e_a1", "marks": [("hashes", 47), ("text", 47, "[Salvage Run]"), ("text", 47, "(salvage)")]},
        {"from": 3, "still": "e_a3", "marks": [("lines", 49, 49)]},
        {"from": 4, "still": "e_a3", "marks": [("text", 49, "Arc")]},
        {"from": 5, "still": "e_a3", "marks": [("text", 49, "Arc")], "dim": True},
        {"from": 7, "still": "e_a6", "marks": [("lines", 50, 51)]},
        {"from": 8, "still": "e_a6", "marks": [("lines", 50, 50), ("lines", 51, 51)]},
        {"from": 9, "still": "e_a7", "marks": [("lines", 53, 53)]},
    ]},
    "s03_one_hash": {"step": 2, "beats": [
        {"from": 0, "still": "e_h3", "marks": [("hashes", 55)]},
        {"from": 0.5, "still": "e_h4", "marks": [("hashes", 55)]},
        {"from": 1, "still": "e_h4", "marks": [("hashes", 55), ("hashes", 47)]},
        {"from": 2, "still": "e_h4", "marks": [("lines", 47, 47), ("lines", 55, 55)]},
        {"from": 3, "still": "e_h4", "marks": [("text", 55, "[Close Inspection]")]},
        {"from": 4, "still": "e_h4", "marks": [("text", 47, "[Salvage Run]"), ("text", 55, "[Close Inspection]")]},
        {"from": 5, "still": "e_h4", "marks": [("text", 47, "(salvage)"), ("text", 55, "(approach)")]},
    ]},
    "s04_the_second_step_and_where_no": {"step": 3, "beats": [
        {"from": 0, "still": "e_gap", "marks": [("after", 63)]},
        {"from": 1, "still": "e_h4_mid", "marks": [("hashes", 55), ("hashes", 47)]},
        {"from": 2, "still": "e_h4_mid", "marks": [("hashes", 65), ("text", 65, "[Long Watch]")]},
        {"from": 3, "still": "e_h4_mid", "marks": [("after", 73)]},
        {"from": 4, "still": "e_h4_mid", "marks": [("lines", 65, 73)]},
        {"from": 5, "still": "e_h4_mid", "marks": [("lines", 55, 63)]},
        {"from": 6, "still": "e_gap", "marks": [("after", 63)]},
        {"from": 9, "still": "e_home1", "marks": [("lines", 65, 65)]},
        {"from": 9.45, "still": "e_home4", "marks": [("lines", 68, 68)]},
        {"from": 10, "still": "e_home", "marks": [("text", 68, "revealed")]},
    ]},
    "s05_the_chain": {"step": None, "beats": [
        {"from": 0, "still": "t_home", "marks": [("out", 1, 2)]},
        {"from": 1, "still": "e_home", "marks": [("lines", 68, 68)]},
        {"from": 2, "still": "t_home", "marks": [("span", 1, _WARN)]},
        {"from": 3, "still": "t_home", "marks": [("out", 1, 2)], "dim": True},
        {"from": 4, "still": "t_home", "marks": [("span", 1, _WRITE)]},
        {"from": 6, "still": "e_then", "marks": [("lines", 62, 62)]},
        {"from": 7, "still": "e_then", "marks": [("text", 62, "salvage/home")]},
        {"from": 9, "still": "e_then", "marks": [("lines", 56, 63)]},
        {"from": 10, "still": "t_then", "marks": [("part", "run2:clean")]},
        {"from": 11, "still": "e_then", "marks": [("lines", 62, 62), ("lines", 66, 66)]},
    ]},
    "s06_a_step_you_can_skip": {"step": 4, "beats": [
        {"from": 0, "still": "e_quick", "marks": [("lines", 76, 85)]},
        {"from": 1, "still": "e_quick", "marks": [("lines", 81, 81)]},
        {"from": 2, "still": "e_quick", "marks": [("lines", 82, 82)]},
        {"from": 3, "still": "e_quick", "marks": [("lines", 81, 82)]},
        {"from": 4, "still": "card_first", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_first", "marks": [("part", "r2")]},
    ]},
    "s07_what_the_story_needs": {"step": 5, "beats": [
        {"from": 0, "still": "e_steps", "marks": [("lines", 55, 55), ("lines", 66, 66), ("lines", 76, 76)]},
        {"from": 1, "still": "e_steps", "marks": [("lines", 76, 82)]},
        {"from": 2, "still": "e_steps", "marks": [("lines", 55, 55), ("lines", 66, 66)]},
        {"from": 3, "still": "e_req1", "marks": [("lines", 63, 64)]},
        {"from": 4, "still": "e_req", "marks": [("lines", 63, 64), ("lines", 75, 76)]},
        {"from": 5, "still": "e_req", "marks": [("lines", 63, 64), ("lines", 75, 76)], "dim": True},
    ]},
    "s08_two_endings": {"step": 6, "beats": [
        {"from": 0, "still": "e_arcs", "marks": [("lines", 22, 22), ("lines", 47, 47)]},
        {"from": 1, "still": "e_arcs", "marks": [("lines", 24, 26), ("lines", 49, 50)]},
        {"from": 2, "still": "e_end0", "marks": [("text", 47, "[Salvage Run]")]},
        {"from": 3, "still": "e_end1", "marks": [("lines", 52, 52)]},
        {"from": 4, "still": "e_end2", "marks": [("lines", 53, 53)]},
        {"from": 5, "still": "e_end", "marks": [("lines", 54, 54)]},
        {"from": 6, "still": "e_end", "marks": [("text", 53, "Win:")]},
        {"from": 7, "still": "e_end", "marks": [("text", 54, "Lose:")]},
        {"from": 8, "still": "e_end", "marks": [("lines", 52, 52), ("lines", 54, 54)]},
        {"from": 9, "still": "e_end", "marks": [("text", 52, "Fails when:")]},
        {"from": 10, "still": "e_end", "marks": [("text", 54, "Lose:")]},
        {"from": 11, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s09_the_warning_with_a_trap": {"step": 7, "beats": [
        {"from": 0, "still": "e_final_home", "marks": [("hashes", 71)]},
        {"from": 2, "still": "e_trap", "marks": [("hashes", 71)]},
        {"from": 3, "still": "t_trap", "marks": [("span", 1, "line 65:14")]},
        {"from": 4, "still": "e_trap", "marks": [("lines", 65, 65)]},
        {"from": 5, "still": "t_trap", "marks": [("out", 1, 2)]},
        {"from": 6, "still": "t_trap", "marks": [("span", 1, _OFFER)]},
        {"from": 7, "still": "t_trap", "marks": [("span", 1, "There is a `home` at `home`")]},
        {"from": 8, "still": "t_trap", "marks": [("span", 1, _OFFER)]},
        {"from": 9, "still": "t_trap", "marks": [("span", 1, _OFFER)], "dim": True},
        {"from": 10, "still": "e_trap_mid", "marks": [("lines", 58, 69)]},
        {"from": 12, "still": "e_trap", "marks": [("lines", 65, 65)]},
        {"from": 13, "still": "e_trap", "marks": [("hashes", 71)]},
        {"from": 14, "still": "t_trap", "marks": [("span", 1, _OFFER)]},
        {"from": 15, "still": "e_final_home", "marks": [("hashes", 71)]},
    ]},
    "s10_play_it_win": {"step": 8, "beats": [
        {"from": 0, "still": "game_log", "marks": [_TWO]},
        {"from": 1, "still": "game_arc", "marks": [_MORE]},
        {"from": 2, "still": "game_helm"},
        {"from": 3, "still": "game_helm", "marks": [_MSG]},
        {"from": 3.5, "still": "game_hulk", "marks": [_DONE2]},
        {"from": 4, "still": "game_hulk", "marks": [_HOME_ROW]},
        {"from": 5, "still": "game_home", "marks": [_HOME_PANE]},
        {"from": 6, "still": "game_win", "marks": [_SENTENCE]},
    ]},
    "s11_play_it_lose": {"step": None, "beats": [
        {"from": 0, "still": "e_lose", "marks": [("text", 52, "30 seconds")]},
        {"from": 2, "still": "game_lose", "marks": [_SENTENCE]},
        {"from": 3, "still": "game_lose"},
        {"from": 4, "still": "game_log", "marks": [_CLOCK, _QCLOCK]},
        {"from": 5, "still": "e_final", "marks": [("lines", 56, 56)]},
        {"from": 6, "still": "e_final", "marks": [("lines", 69, 69)]},
        {"from": 7, "still": "e_end", "marks": [("text", 52, "10 minutes")]},
    ]},
    "s12_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item5")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3"), ("part", "item4")]},
        {"from": 3, "still": "card_exercise"},
        {"from": 4, "still": "card_next"},
    ]},
}
