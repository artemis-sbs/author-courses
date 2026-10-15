"""Storyboard for c2-03-dialogue-part-1: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 2's finished file (the chain from Class 1 Lecture 3's
seven files, with every later example laid over them: "start"). The scene is typed, then
given its two blocks, then the beat goes in among the quests ("final", the page's own
example\\mission.amd).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. Start them with
`python game.py c2-03-dialogue-part-1 start --state g_near --consoles server,helm,comms`.
g_near is PROBE-ONLY (never shown in the editor): the hulk 1500 from the ship in place of
9000, so a short flight puts the ship inside 500 and the beat places the call. The words,
the scene and the beat are the page's.
"""
LECTURE = "c2-03-dialogue-part-1"
TITLE = ("Class 2, Lecture 3", "Dialogue, part 1", "A call from the station")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_SCENE = ("\n\n// ---- Dialogue. A scene is who speaks and what they say.\n"
          "## [Dialogue](dialogue)\n\n"
          "### [Quill Checks In](quill_hello)\n---\nSpeaker: quill\nWhen: hail\nTitle: About that hulk\n---\n"
          "% Artemis, DS 1. We watched you go in close.\n"
          "% Artemis, this is Quill on DS 1. You got nearer to that hulk than I would have.\n"
          "% DS 1 to Artemis. Nice flying out there.\n")
_SECOND = "\n@quill\n% Now tell me she is as dead as she looks.\n% So. Is anybody home?\n"
_QUICK_END = "Optional. DS 1 pays a bonus for a fast approach.\n"
_BEAT = ("\n### [DS 1 Calls](ds1_calls)\n---\nBeat\nStarts when: reach derelict 500\nAction:\n"
         "  - quill hails quill_hello\n---\nDS 1 saw the ship go in close, and wants to hear about it.\n")
_EX = "c2-03-dialogue-part-1/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example",
                       "c2-01-sides-and-factions/example", "c2-02-characters-and-faces/example")},
    # Step 1: the section and the scene, three takes
    "d1": {"base": "start", "edits": [("append", FILE, _SCENE)]},
    # Step 3: two blocks
    "d2": {"base": "d1", "edits": [
        ("replace", FILE, "---\n% Artemis, DS 1. We", "---\n@quill\n% Artemis, DS 1. We"),
        ("append", FILE, _SECOND)]},
    # Step 4: the beat, below Quick Work. The page's own file.
    "final": {"base": "d2", "edits": [("replace", FILE, _QUICK_END, _QUICK_END + _BEAT)],
              "same_as": _EX + "/mission.amd"},
    # Scene 7: the two mistakes lint cannot see
    "b_nostart": {"base": "final", "edits": [("replace", FILE, "Starts when: reach derelict 500\nAction:", "Action:")]},
    "b_name": {"base": "final", "edits": [("replace", FILE, "@quill\n% Now tell", "@Harbormaster Quill\n% Now tell")]},
    # PROBE-ONLY, for the game stills: the hulk 1500 from the ship. Never shown in the editor.
    "g_near": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 1500, "Unknown Hulk"')]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    "m_49": ("vscode", "start", 49, "big", _M),
    "e_end0": ("vscode", "start", 264, "big", _NS),        # lines 254 to 274: the cast at the end
    "e_d1": ("vscode", "d1", 282, "big", _NS),             # lines 272 to 292
    "e_d2": ("vscode", "d2", 283, "big", _NS),             # lines 273 to 293
    "e_quick": ("vscode", "d2", 138, "big", _NS),          # lines 128 to 148: Quick Work, the last quest
    "e_beat": ("vscode", "final", 143, "big", _NS),        # lines 133 to 153
    "e_nostart": ("vscode", "b_nostart", 143, "big", _NS),
    "e_name": ("vscode", "b_name", 290, "big", _NS),       # lines 280 to 300
    "e_scene": ("vscode", "final", 292, "big", _NS),       # lines 282 to 302: the finished scene
    "t_d1": ("terminal", [("d1", _LINT)]),
    "t_d2": ("terminal", [("d2", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_nostart": ("terminal", [("b_nostart", _LINT)]),
    "t_name": ("terminal", [("b_name", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). State g_near, consoles server,helm,comms.
    "game_comms_empty": ("game", "Comms at the start, before the ship moves (state g_near): no call waiting, no Incoming Hails row"),
    "game_comms_row": ("game", "Comms just after the ship goes inside 500 of the hulk on Helm (state g_near): the Incoming Hails list with one row, 'Harbormaster Quill - About that hulk'"),
    "game_comms_call": ("game", "Comms, the row selected (state g_near, as game_comms_row): the call open with Quill's face, her name, the title About that hulk, and one of her three opening takes; the list offers Back and Continue"),
    "game_comms_call2": ("game", "Comms, the same call after Continue: one of her two closing takes ('Now tell me she is as dead as she looks.' or 'So. Is anybody home?'); the list offers Back and Close"),
    "game_comms_call_alt": ("game", "Comms, the call open in a SECOND start of the mission (stop, start --state g_near again, fly in): a different opening take from game_comms_call"),
    "game_log_done": ("game", "Helm, the ePADD Quest Log (handheld icon, then Quests), right after the ship goes inside 500 of the hulk (state g_near): Close Inspection selected, Done"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_lines": ("card", "table", {"heading": "Step 1 - Write the scene", "kicker": "One scene"}),
    "card_takes": ("card", "list", {"heading": "Step 2 - Takes", "kicker": "Three rules for a take"}),
    "card_beat": ("card", "table", {"heading": "Step 4 - Have the story place the call", "kicker": "A beat"}),
    "card_cannot": ("card", "table", {"heading": "Step 5 - Check it", "nth": 3, "kicker": "Lint says clean, and", "rows": (1, 12)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A second call"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 4", "sub": "Dialogue, part 2"}),
}

_SCENE_REC = ("lines", 279, 287)        # d1: the scene, three takes

# Marks on the game stills (fractions of the 1280x960 frame), set from the screenshots 2026-10-15.
_HAILS_EMPTY = ("rect", 0.0, 0.84, 0.275, 0.97)       # game_comms_empty: where the Incoming Hails list would be
_HAILS_ROW = ("rect", 0.0, 0.845, 0.275, 0.91)        # game_comms_row: Incoming Hails, Harbormaster Quill - About that hulk
_CALL_FACE = ("rect", 0.27, 0.45, 0.5, 0.735)         # the call: Quill's face
_CALL_NAME = ("rect", 0.27, 0.775, 0.53, 0.815)       # ... Harbormaster Quill, in bold
_CALL_TITLE = ("rect", 0.57, 0.735, 0.7, 0.772)       # ... the title About that hulk
_CALL_TAKE = ("rect", 0.27, 0.82, 0.57, 0.86)         # ... the take
_CALL_TAKE_ALT = ("rect", 0.27, 0.82, 0.83, 0.86)     # game_comms_call_alt: the longer take
_CALL_LIST = ("rect", 0.0, 0.845, 0.275, 0.97)        # ... the answer list: Back, Continue (or Close)
_CALL_BACK = ("rect", 0.0, 0.878, 0.275, 0.928)       # ... Back
_CALL_NEXT = ("rect", 0.0, 0.925, 0.275, 0.975)       # ... Continue, or Close
_LOG_ROW = ("rect", 0.025, 0.503, 0.38, 0.573)        # game_log_done: Close Inspection, Done
_LOG_STATE = ("rect", 0.385, 0.075, 0.62, 0.19)       # ... State Done, Reward, the order

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_comms_empty"},
        {"from": 2, "still": "card_title"},
        {"from": 3, "still": "game_comms_row", "marks": [_HAILS_ROW]},
        {"from": 4, "still": "game_comms_call", "marks": [_CALL_TAKE]},
        {"from": 5, "still": "e_scene", "marks": [("lines", 288, 301)]},
        {"from": 6, "still": "e_beat", "marks": [("lines", 144, 152)]},
    ]},
    "s02_the_scene": {"step": 1, "beats": [
        # the game first: the call open on Comms
        {"from": 0, "still": "game_comms_call"},
        {"from": 1, "still": "game_comms_call", "marks": [_CALL_FACE, _CALL_NAME]},
        {"from": 2, "still": "game_comms_call", "marks": [_CALL_TITLE]},
        {"from": 3, "still": "m_49", "marks": [("lines", 49, 49)]},
        {"from": 4, "still": "m_49", "marks": [("text", 49, "\"dialogue\"")]},
        {"from": 5, "still": "e_d1", "marks": [("lines", 277, 277)]},
        {"from": 6, "still": "e_d1", "marks": [_SCENE_REC]},
        {"from": 7, "still": "e_d1", "marks": [("lines", 281, 281)]},
        {"from": 8, "still": "e_d1", "marks": [("lines", 282, 282)]},
        {"from": 9, "still": "e_d1", "marks": [("lines", 283, 283)]},
        {"from": 11, "still": "e_d1", "marks": [("lines", 285, 287)]},
        {"from": 12, "still": "e_d1", "marks": [("text", 285, "%"), ("text", 286, "%"), ("text", 287, "%")]},
    ]},
    "s03_takes": {"step": 2, "beats": [
        {"from": 0, "still": "e_d1", "marks": [("lines", 285, 287)]},
        {"from": 2, "still": "e_d1", "marks": [("lines", 286, 286)]},
        {"from": 4, "still": "game_comms_call", "marks": [_CALL_TAKE]},
        {"from": 5, "still": "card_takes", "marks": [("part", "item2")]},
        {"from": 7, "still": "card_takes", "marks": [("part", "item1")]},
        {"from": 8, "still": "t_d1", "marks": [("part", "run1:clean")]},
    ]},
    "s04_a_second_thing_to_say": {"step": 3, "beats": [
        # the game first: Continue, and her question
        {"from": 0, "still": "game_comms_call", "marks": [_CALL_TAKE]},
        {"from": 1, "still": "game_comms_call", "marks": [_CALL_TAKE, _CALL_NEXT]},
        {"from": 2, "still": "game_comms_call2", "marks": [_CALL_TAKE]},
        {"from": 3, "still": "e_d2"},
        {"from": 4, "still": "e_d2", "marks": [("lines", 285, 285), ("lines", 290, 290)]},
        {"from": 6, "still": "e_d2", "marks": [("lines", 285, 288)]},
        {"from": 7, "still": "e_d2", "marks": [("lines", 290, 292)]},
        {"from": 8, "still": "e_d2", "marks": [("lines", 286, 286), ("lines", 291, 291)]},
        {"from": 9, "still": "game_comms_call", "marks": [_CALL_TAKE, _CALL_NEXT]},
        {"from": 10, "still": "game_comms_call2", "marks": [_CALL_TAKE]},
    ]},
    "s05_nobody_calls_yet": {"step": None, "beats": [
        {"from": 0, "still": "t_d2", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "game_comms_empty", "marks": [_HAILS_EMPTY]},
        {"from": 3, "still": "e_quick", "marks": [("lines", 133, 142)]},
    ]},
    "s06_the_beat": {"step": 4, "beats": [
        # the game first: the row arrives as the ship gets in close
        {"from": 0, "still": "game_comms_row"},
        {"from": 1, "still": "game_comms_row", "marks": [_HAILS_ROW]},
        {"from": 3, "still": "e_beat", "marks": [("lines", 144, 152)]},
        {"from": 4, "still": "e_beat", "marks": [("hashes", 144)]},
        {"from": 5, "still": "e_beat", "marks": [("lines", 146, 146)]},
        {"from": 7, "still": "card_beat", "marks": [("part", "r2")]},
        {"from": 9, "still": "e_beat", "marks": [("lines", 147, 147)]},
        {"from": 12, "still": "e_beat", "marks": [("text", 147, "reach derelict 500")]},
        {"from": 14, "still": "game_log_done", "marks": [_LOG_ROW, _LOG_STATE]},
        {"from": 15, "still": "e_beat", "marks": [("lines", 148, 148)]},
        {"from": 16, "still": "e_beat", "marks": [("text", 149, "  - ")]},
        {"from": 17, "still": "e_beat", "marks": [("text", 149, "quill"), ("text", 149, "hails"), ("text", 149, "quill_hello")]},
    ]},
    "s07_what_lint_cannot_see": {"step": 5, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "card_cannot"},
        {"from": 3, "still": "e_nostart", "marks": [("lines", 146, 147)]},
        {"from": 3.6, "still": "t_nostart", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 5, "still": "e_name", "marks": [("text", 299, "@Harbormaster Quill")]},
        {"from": 6, "still": "t_name", "marks": [("part", "run1:clean")]},
        {"from": 7, "still": "card_cannot", "marks": [("part", "r2")]},
    ]},
    "s08_play_it": {"step": 6, "beats": [
        {"from": 0, "still": "game_comms_empty"},
        {"from": 1, "still": "game_comms_empty", "marks": [_HAILS_EMPTY]},
        {"from": 3, "still": "game_log_done", "marks": [_LOG_ROW]},
        {"from": 4, "still": "game_comms_row", "marks": [_HAILS_ROW]},
        {"from": 5, "still": "game_comms_call", "marks": [_CALL_FACE]},
        {"from": 6, "still": "game_comms_call", "marks": [_CALL_TAKE]},
        {"from": 7, "still": "game_comms_call2", "marks": [_CALL_TAKE]},
        {"from": 8, "still": "game_comms_call2", "marks": [_CALL_NEXT]},
    ]},
    "s09_back_and_again": {"step": None, "beats": [
        {"from": 0, "still": "game_comms_call"},
        {"from": 1, "still": "game_comms_call", "marks": [_CALL_BACK]},
        {"from": 2, "still": "game_comms_row", "marks": [_HAILS_ROW]},
        {"from": 5, "still": "game_comms_call_alt"},
        {"from": 6, "still": "game_comms_call_alt", "marks": [_CALL_TAKE_ALT]},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_next"},
    ]},
}
