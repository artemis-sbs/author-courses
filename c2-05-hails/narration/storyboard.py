"""Storyboard for c2-05-hails: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 4's finished file ("start", the whole chain). Tag the Hulk
loses its pay, the beat becomes a quest, the call learns to ask, Chief Ives gets a block,
and the call gets a priority ("final", the page's own example\\mission.amd).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. Start them with
`python game.py c2-05-hails start --state g_near --consoles server,helm,comms`. g_near is
PROBE-ONLY (never shown in the editor): the hulk 1500 from the ship in place of 9000. Then
on Helm fly inside 500 of the hulk; on Comms open Quill's first call, Continue, She is
cold..., We will tag her.; wait 30 seconds for the report step and its call.
"""
LECTURE = "c2-05-hails"
TITLE = ("Class 2, Lecture 5", "Hails", "A step only the crew can finish")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_IVES = "ter #d2b2a1 0 0;ter #fff 13 6;ter #d2b2a1 11 1;ter #d2b2a1 12 2;ter #934e2c 11 3;ter #fff 9 5;"
_BEAT_OLD = ("### [Beacon Set](beacon_set)\n---\nBeat\nStarts when: revealed\nAction:\n"
             "  - quill hails quill_thanks\n---\nThe beacon is live, and DS 1 calls to say so.\n")
_REPORT = ("### [Report to DS 1](report_in)\n---\nScope: shared\nStarts when: revealed\n"
           "Objective: Answer DS 1 and tell her the beacon is set\nReward: 150 credits\nAction:\n"
           "  - quill hails quill_thanks\n---\n"
           "![](face://" + _IVES + ") Chief Ives, salvage desk, DS 1\n\n"
           "The beacon is live. DS 1 pays when she hears it from the ship.\n\n"
           "Chief Ives will not write a claim into the ledger on a beacon's signal alone. Somebody aboard "
           "the ship that set it has to say so on Comms, so that it is on the record.\n")
_TAKES_OLD = ("% Your beacon is singing, Artemis. The claim is logged in your name.\n"
              "% Beacon is live. That makes her yours, on paper.\n\n- [Glad to help, DS 1. Artemis out.]()\n")
_TAKES_NEW = ("% Something just started singing out by that hulk. Tell me it is yours.\n"
              "% I have a new beacon on my board, out by the hulk. Is that your work?\n\n"
              "- [It is ours, DS 1. The beacon is set.]() ; completes report_in\n")
_IVES_BLOCK = ("\n@ives\n% Salvage desk. If it is theirs, I need to hear them say it.\n"
               "% Chief Ives, salvage desk. Say it for the ledger, please.\n")
_EX = "c2-05-hails/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example",
                       "c2-01-sides-and-factions/example", "c2-02-characters-and-faces/example",
                       "c2-03-dialogue-part-1/example", "c2-04-dialogue-part-2/example")},
    # Step 1: Tag the Hulk, then the beat replaced by a quest
    "r1": {"base": "start", "edits": [
        ("replace", FILE, "Reward: 150 credits\nThen: reveal beacon_set\n---", "Then: reveal report_in\n---"),
        ("replace", FILE, "before the Breakers find her.\n", "before the Breakers find her. It pays when\nthe ship reports back.\n")]},
    "r2": {"base": "r1", "edits": [("replace", FILE, _BEAT_OLD, _REPORT)]},
    # Step 2: the call asks, and its answer completes the step
    "r3": {"base": "r2", "edits": [("replace", FILE, _TAKES_OLD, _TAKES_NEW)]},
    # Step 3: a second voice
    "r4": {"base": "r3", "edits": [
        ("replace", FILE, "---\n% Something just started", "---\n@quill\n% Something just started"),
        ("replace", FILE, "Is that your work?\n", "Is that your work?\n" + _IVES_BLOCK)]},
    # Step 4: a priority. The page's own file.
    "final": {"base": "r4", "edits": [("replace", FILE, "Title: Your beacon\n---", "Title: Your beacon\nPriority: 5\n---")],
              "same_as": _EX + "/mission.amd"},
    # Scene 8: the two mistakes lint cannot see
    "b_nocomplete": {"base": "final", "edits": [("replace", FILE, "set.]() ; completes report_in", "set.]()")]},
    "b_beat": {"base": "final", "edits": [("replace", FILE, "---\nScope: shared\nStarts when: revealed\nObjective: Answer DS 1",
                                           "---\nBeat\nScope: shared\nStarts when: revealed\nObjective: Answer DS 1")]},
    # PROBE-ONLY, for the game stills: the hulk 1500 from the ship. Never shown in the editor.
    "g_near": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 1500, "Unknown Hulk"')]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}

STILLS = {
    "e_tag0": ("vscode", "start", 163, "mid", _NS),        # lines 149 to 177: Tag the Hulk and the beat
    "e_r1": ("vscode", "r1", 163, "mid", _NS),
    "e_r2": ("vscode", "r2", 172, "big", _NS),             # lines 162 to 182: Report to DS 1
    "e_call0": ("vscode", "r2", 366, "big", _NS),          # lines 356 to 376: Quill Calls Back
    "e_r3": ("vscode", "r3", 366, "big", _NS),
    "e_r4": ("vscode", "r4", 368, "big", _NS),             # lines 358 to 378
    "e_cast": ("vscode", "r4", 302, "big", _NS),           # lines 292 to 312: Chief Ives in the cast
    "e_final": ("vscode", "final", 368, "big", _NS),
    "e_nocomplete": ("vscode", "b_nocomplete", 368, "big", _NS),
    "e_beat": ("vscode", "b_beat", 172, "big", _NS),
    "t_r2": ("terminal", [("r2", _LINT)]),
    "t_r4": ("terminal", [("r4", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_nocomplete": ("terminal", [("b_nocomplete", _LINT)]),
    "t_beat": ("terminal", [("b_nocomplete", _LINT), ("b_beat", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). State g_near, consoles server,helm,comms (see the docstring)
    "game_log_report": ("game", "Helm, the ePADD Quest Log 30 s after 'We will tag her.' (state g_near): Report to DS 1 selected, running: Chief Ives's portrait with 'Chief Ives, salvage desk, DS 1', the order 'Answer DS 1 and tell her the beacon is set', and the two paragraphs"),
    "game_comms_report_row": ("game", "Comms, at the same moment: the Incoming Hails row 'Harbormaster Quill - Your beacon' at the top of the list"),
    "game_comms_report_quill": ("game", "Comms, the Your beacon call opened: Quill's face and name, one of her two takes ('...Tell me it is yours.' or '...Is that your work?'); the list offers Back and Continue"),
    "game_comms_report_ives": ("game", "Comms, the same call after Continue: Chief Ives's face and name, one of his two takes, and the one answer 'It is ours, DS 1. The beacon is set.'"),
    "game_log_report_done": ("game", "Helm, the Quest Log after the crew answers 'It is ours, DS 1. The beacon is set.': Report to DS 1 Done, Reward 150 credits"),
    "game_comms_dial": ("game", "Comms with a call waiting in the list: the drop-down above the list, OPEN (Both, Main Screen, This Console, Off, top to bottom; it starts on Both)"),
    "game_comms_hails_tab": ("game", "Comms, the info panel's Hails tab after the report call: the last icon of the left column (two figures); the finished calls as bare rows 'Harbormaster Quill', one per call. A row cannot be read again: clicking only highlights it"),
    "game_comms_shiplog": ("game", "The ship's log line the finished report call left: who called, what about, and what the crew answered (the strip under the left panel, in green; the same screenshot as game_comms_hails_tab)"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_diff": ("card", "table", {"heading": "Step 1 - A step only an answer can finish", "kicker": "A quest, not a beat"}),
    "card_top": ("card", "table", {"heading": "Step 4 - Which call is on top", "kicker": "Four facts"}),
    "card_who": ("card", "table", {"heading": "Step 5 - Who gets called", "kicker": "With two ships"}),
    "card_comms": ("card", "table", {"heading": "Step 6 - What Comms can do with a call", "kicker": "On the Comms console"}),
    "card_cannot": ("card", "table", {"heading": "Step 7 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (2, 1)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "More voices"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 6", "sub": "Reputation, a first look"}),
}

# Marks on the game stills (fractions of the 1280x960 frame), set from the screenshots 2026-10-15.
_REP_ROW = ("rect", 0.0, 0.503, 0.38, 0.573)          # game_log_report: Report to DS 1, Active
_REP_ORDER = ("rect", 0.385, 0.075, 0.72, 0.19)       # ... State, Reward, the order
_REP_FACE = ("rect", 0.385, 0.195, 0.67, 0.27)        # ... Chief Ives's portrait under the order
_TAG_DONE = ("rect", 0.0, 0.655, 0.2, 0.715)          # ... Tag the Hulk, Done
_ROW = ("rect", 0.0, 0.845, 0.275, 0.91)              # an Incoming Hails row: Harbormaster Quill - Your beacon
_FACE = ("rect", 0.27, 0.45, 0.5, 0.735)              # the call: the face
_NAME = ("rect", 0.27, 0.775, 0.53, 0.815)            # ... the speaker's name, in bold
_FACE_NAME = ("rect", 0.27, 0.45, 0.53, 0.815)        # ... both
_TAKE = ("rect", 0.27, 0.82, 0.76, 0.86)              # ... the take
_NEXT = ("rect", 0.0, 0.925, 0.275, 0.965)            # game_comms_report_quill: Continue
_ANSWER = ("rect", 0.0, 0.925, 0.275, 0.975)          # game_comms_report_ives: It is ours, DS 1. The beacon is set.
_DONE_ROW = ("rect", 0.0, 0.648, 0.38, 0.718)         # game_log_report_done: Report to DS 1, Done
_DONE_STATE = ("rect", 0.385, 0.075, 0.62, 0.14)      # ... State Done, Reward 150 credits
_DROP = ("rect", 0.0, 0.62, 0.16, 0.795)              # game_comms_dial: the drop-down, open
_HAILS_ROWS = ("rect", 0.0, 0.055, 0.18, 0.145)       # game_comms_hails_tab: two rows, Harbormaster Quill
_HAILS_ICON = ("rect", 0.0, 0.355, 0.035, 0.405)      # ... the Hails tab icon (two figures)
_LOG_LINE = ("rect", 0.0, 0.495, 0.275, 0.58)         # game_comms_shiplog: the ship's log line

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_log_report"},
        {"from": 2, "still": "game_comms_report_row", "marks": [_ROW]},
        {"from": 3, "still": "game_comms_report_quill", "marks": [_TAKE]},
        {"from": 4, "still": "game_comms_report_ives", "marks": [_FACE_NAME]},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_a_step_only_an_answer_can_fi": {"step": 1, "beats": [
        # the game first: the step in the Quest Log
        {"from": 0, "still": "game_log_report", "marks": [_REP_ROW]},
        {"from": 1, "still": "game_log_report", "marks": [_REP_FACE]},
        {"from": 2, "still": "game_log_report", "marks": [_REP_ORDER]},
        {"from": 3, "still": "e_tag0", "marks": [("lines", 153, 160)]},
        {"from": 4, "still": "e_r1", "marks": [("lines", 158, 159)]},
        {"from": 6, "still": "e_tag0", "marks": [("lines", 168, 175)]},
        {"from": 7, "still": "e_r2", "marks": [("lines", 168, 182)]},
        {"from": 8, "still": "e_r2", "marks": [("lines", 170, 170)]},
        {"from": 9, "still": "e_r2", "marks": [("lines", 172, 172)]},
        {"from": 10, "still": "e_r2", "marks": [("lines", 173, 173)]},
        {"from": 11, "still": "e_r2", "marks": [("lines", 174, 175)]},
        {"from": 13, "still": "card_diff", "marks": [("part", "r5")]},
        {"from": 15, "still": "e_r2", "marks": [("lines", 177, 177)]},
        {"from": 18, "still": "e_r2", "marks": [("lines", 179, 181)]},
        {"from": 19, "still": "e_r2", "marks": [("lines", 172, 172), ("lines", 179, 181)]},
        {"from": 20, "still": "t_r2", "marks": [("part", "run1:clean")]},
    ]},
    "s03_the_answer_that_finishes_it": {"step": 2, "beats": [
        {"from": 0, "still": "e_call0", "marks": [("lines", 363, 366)]},
        # the game first: the call as it asks
        {"from": 2, "still": "game_comms_report_quill", "marks": [_TAKE]},
        {"from": 4, "still": "game_comms_report_ives", "marks": [_ANSWER]},
        {"from": 5, "still": "e_r3", "marks": [("lines", 363, 364)]},
        {"from": 6, "still": "e_r3", "marks": [("text", 366, "; completes report_in")]},
        {"from": 8, "still": "e_r3", "marks": [("lines", 366, 366)]},
        {"from": 10, "still": "card_cannot", "marks": [("part", "r1")]},
    ]},
    "s04_a_second_voice": {"step": 3, "beats": [
        # the game first: Continue, and Chief Ives
        {"from": 0, "still": "game_comms_report_quill", "marks": [_FACE_NAME]},
        {"from": 1, "still": "game_comms_report_quill", "marks": [_NEXT]},
        {"from": 2, "still": "game_comms_report_ives", "marks": [_FACE_NAME]},
        {"from": 3, "still": "e_cast", "marks": [("lines", 302, 306)]},
        {"from": 5, "still": "e_r4", "marks": [("lines", 367, 369)]},
        {"from": 7, "still": "game_comms_report_row", "marks": [_ROW]},
        {"from": 9, "still": "e_r4", "marks": [("lines", 363, 363), ("lines", 367, 367)]},
        {"from": 11, "still": "e_r4", "marks": [("text", 367, "@ives")]},
        {"from": 13, "still": "t_r4", "marks": [("part", "run1:clean")]},
    ]},
    "s05_which_call_is_on_top": {"step": 4, "beats": [
        {"from": 0, "still": "card_top", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_top", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 4, "still": "e_final", "marks": [("lines", 362, 362)]},
        {"from": 5, "still": "e_final", "marks": [("text", 362, "5")]},
        {"from": 7, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s06_who_gets_called": {"step": 5, "beats": [
        {"from": 0, "still": "card_who"},
        {"from": 4, "still": "card_who", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_who", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_who", "marks": [("part", "r5")]},
        {"from": 8, "still": "card_who"},
    ]},
    "s07_what_comms_can_do": {"step": 6, "beats": [
        {"from": 0, "still": "card_comms"},
        {"from": 3, "still": "game_comms_report_row", "marks": [_ROW]},
        {"from": 4, "still": "game_comms_report_quill", "marks": [_FACE_NAME]},
        {"from": 5, "still": "card_comms", "marks": [("part", "r3")]},
        {"from": 6, "still": "game_comms_dial", "marks": [_DROP]},
        {"from": 8, "still": "game_comms_hails_tab", "marks": [_HAILS_ICON, _HAILS_ROWS]},
        {"from": 9, "still": "game_comms_hails_tab", "marks": [_HAILS_ROWS]},
        {"from": 10, "still": "game_comms_shiplog", "marks": [_LOG_LINE]},
        {"from": 11, "still": "game_comms_shiplog", "marks": [_LOG_LINE]},
        {"from": 12, "still": "card_comms"},
    ]},
    "s08_what_lint_cannot_see": {"step": 7, "beats": [
        {"from": 0, "still": "card_cannot"},
        {"from": 3, "still": "e_nocomplete", "marks": [("lines", 372, 372)]},
        {"from": 3.6, "still": "t_nocomplete", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "card_cannot", "marks": [("part", "r2")]},
        {"from": 5, "still": "e_beat", "marks": [("lines", 170, 170)]},
        {"from": 6, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_cannot"},
    ]},
    "s09_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_comms_report_row"},
        {"from": 2, "still": "game_log_report", "marks": [_TAG_DONE]},
        {"from": 3, "still": "game_log_report", "marks": [_REP_ROW, _REP_ORDER]},
        {"from": 4, "still": "game_comms_report_row", "marks": [_ROW]},
        {"from": 5, "still": "game_comms_report_quill", "marks": [_FACE_NAME]},
        {"from": 6, "still": "game_comms_report_ives", "marks": [_FACE_NAME]},
        {"from": 7, "still": "game_comms_report_row", "marks": [_ROW]},
        {"from": 8, "still": "game_comms_report_ives", "marks": [_ANSWER]},
        {"from": 9, "still": "game_log_report_done", "marks": [_DONE_ROW, _DONE_STATE]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_next"},
    ]},
}
