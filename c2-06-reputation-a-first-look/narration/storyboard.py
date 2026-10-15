"""Storyboard for c2-06-reputation-a-first-look: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

THIS LECTURE WORKS IN A COPY. The student copies MyMission to MyStanding (Lecture 7 starts
from Lecture 5's file, so these lines must not go into it). MISSION is therefore
"MyStanding": capture materializes each state into the stand-in's data\\missions\\MyStanding,
so lint is run as `sbs lint MyStanding` and VS Code's title reads MyStanding.
** After capturing, delete the stand-in's MyStanding folder (the capture leaves it there),
or every later File Explorer still of data\\missions shows it. **
"start" is Lecture 5's finished file (the whole chain); "final" is the page's own
example\\mission.amd. The copy itself (Ctrl+C, Ctrl+V, F2) is a card in the page's words;
x_copy is the real File Explorer showing the result, both folders.

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. Start them with
`python game.py c2-06-reputation-a-first-look start --state g_yard --consoles server,helm,comms`.
g_yard is PROBE-ONLY (never shown in the editor): the hulk 1500 from the ship and the
Guild Yard at -3000, 0, 3000, so both are a short flight away. The words are the page's.
Game one (the cold line): fly straight to the yard. Game two (the warm line): the hulk,
Quill's call, We will tag her., 30 s, the report call's SECOND answer (the fee to the tug
crews), then the yard.
"""
LECTURE = "c2-06-reputation-a-first-look"
TITLE = ("Class 2, Lecture 6", "Reputation, a first look", "A side that keeps score")
MISSION = "MyStanding"
FILE = "mission.amd"
MAST = "story.mast"

_QUILL = "ter #e4cb8e 1 0;ter #fff 12 6;ter #e4cb8e 3 1;ter #e4cb8e 5 2;ter #704025 7 3;"
_PLAIN = "- [It is ours, DS 1. The beacon is set.]() ; completes report_in\n"
_FEE = "- [It is ours. Give our fee to the tug crews.]() ; completes report_in, earns guild generous 30\n"
_REPORT_END = "so that it is on the record.\n"
_YARD_BEAT = ("\n### [The Yard Calls](yard_calls)\n---\nBeat\nStarts when: reach yard 1500\nAction:\n"
              "  - quill hails quill_yard\n---\nThe Guild yard has seen the ship coming, and Quill speaks for it.\n")
_YARD_SCENE = ("\n### [The Guild Yard](quill_yard)\n---\nSpeaker: quill\nWhen: hail\nTitle: The Guild yard\n---\n"
               "%{standing < 30} Artemis, the Guild yard is for members. Hold outside the markers.\n"
               "%{standing >= 30} Artemis, the tug crews told me what you did. The yard is open to you.\n\n"
               "- [Understood, DS 1.]() ; completes yard_calls\n")
_BERTH = "- [Request a berth at the yard.]() if standing >= 30 ; completes yard_calls\n"
_EX = "c2-06-reputation-a-first-look/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example",
                       "c2-01-sides-and-factions/example", "c2-02-characters-and-faces/example",
                       "c2-03-dialogue-part-1/example", "c2-04-dialogue-part-2/example",
                       "c2-05-hails/example")},
    # Step 1: what the Guild values
    "v1": {"base": "start", "edits": [("replace", FILE, "Allies: tsn\n---\nThe pilots",
                                       "Allies: tsn\nValues: honest 40, generous 30\n---\nThe pilots")]},
    # Step 2: Quill speaks for the Guild
    "v2": {"base": "v1", "edits": [("replace", FILE, "Face: " + _QUILL + "\n---", "Face: " + _QUILL + "\nSide: guild\n---")]},
    # Step 3: a deed in work
    "v3": {"base": "v2", "edits": [("replace", FILE, "Reward: 150 credits\n", "Reward: 150 credits, earns guild honest 30\n")]},
    # Step 4: a deed in talk
    "v4": {"base": "v3", "edits": [("replace", FILE, _PLAIN, _PLAIN + _FEE)]},
    # Step 5: the beat, then the scene with two guarded lines
    "v5": {"base": "v4", "edits": [("replace", FILE, _REPORT_END, _REPORT_END + _YARD_BEAT)]},
    "v6": {"base": "v5", "edits": [("append", FILE, _YARD_SCENE)]},
    # Step 6: an answer that needs standing. The page's own file.
    "final": {"base": "v6", "edits": [("append", FILE, _BERTH)], "same_as": _EX + "/mission.amd"},
    # Scene 10: a misspelled side after earns (lint sees it); no Side: on Quill (lint does not)
    "b_gild": {"base": "final", "edits": [("replace", FILE, "earns guild honest 30", "earns gild honest 30")]},
    "b_noside": {"base": "final", "edits": [("replace", FILE, "Side: guild\n---\nRuns traffic", "---\nRuns traffic")]},
    # PROBE-ONLY, for the game stills. Never shown in the editor.
    "g_yard": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 1500, "Unknown Hulk"'),
        ("replace", FILE, "Loc: -6000, 0, 3000", "Loc: -3000, 0, 3000")]},
}

_LINT = "sbs lint MyStanding"
_NS = {"side": False}

STILLS = {
    "x_copy": ("explorer", "data\\missions", {"state": "start"}),
    "e_guild0": ("vscode", "start", 288, "big", _NS),      # lines 278 to 298: the Harbor Guild
    "e_v1": ("vscode", "v1", 288, "big", _NS),
    "e_v2": ("vscode", "v2", 299, "big", _NS),             # lines 289 to 309: Harbormaster Quill
    "e_v3": ("vscode", "v3", 172, "big", _NS),             # lines 162 to 182: Report to DS 1
    "e_v4": ("vscode", "v4", 374, "big", _NS),             # lines 364 to 384: Quill Calls Back
    "e_v5": ("vscode", "v5", 184, "big", _NS),             # lines 174 to 194: the beat
    "e_v6": ("vscode", "v6", 388, "big", _NS),             # lines 378 to 398: The Guild Yard
    "e_final": ("vscode", "final", 388, "big", _NS),
    "e_gild": ("vscode", "b_gild", 172, "big", _NS),
    "e_noside": ("vscode", "b_noside", 307, "big", _NS),
    "t_copy": ("terminal", [("start", _LINT)]),
    "t_v1": ("terminal", [("v1", _LINT)]),
    "t_v2": ("terminal", [("v2", _LINT)]),
    "t_v4": ("terminal", [("v4", _LINT)]),
    "t_v6": ("terminal", [("v6", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_gild": ("terminal", [("b_gild", _LINT)]),
    "t_noside": ("terminal", [("b_noside", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). State g_yard, consoles server,helm,comms (see the docstring)
    "game_yard_row": ("game", "Comms, game one (state g_yard): the ship flown straight toward the Guild Yard, inside 1500 of it: the Incoming Hails row 'Harbormaster Quill - The Guild yard'"),
    "game_yard_cold": ("game", "Comms, game one, the row opened: Quill's face, 'Artemis, the Guild yard is for members. Hold outside the markers.', and the ONE answer 'Understood, DS 1.'"),
    "game_report_two": ("game", "Comms, game two (state g_yard): after the hulk, Quill's call and 'We will tag her.', 30 s later the Your beacon call, Continue: Chief Ives, and TWO answers, 'It is ours, DS 1. The beacon is set.' and 'It is ours. Give our fee to the tug crews.'"),
    "game_yard_warm": ("game", "Comms, game two after the fee answer, the ship flown to the Guild Yard and the row opened: 'Artemis, the tug crews told me what you did. The yard is open to you.', and TWO answers, 'Understood, DS 1.' and 'Request a berth at the yard.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_copy": ("card", "points", {"kicker": "In File Explorer (not captured: the page's own steps)", "items": [
        "Go to C:\\Cosmos\\data\\missions.", "Click MyMission once. Ctrl+C, then Ctrl+V: MyMission - Copy.",
        "Click the copy once, press F2, type MyStanding, press Enter.",
        "In VS Code: File, Open Folder, MyStanding."]}),
    "card_traits": ("card", "table", {"heading": "Step 1 - The Guild says what it values", "kicker": "Seven pairs of traits"}),
    "card_deed": ("card", "table", {"heading": "Step 3 - A deed in work", "kicker": "A deed"}),
    "card_guard": ("card", "table", {"heading": "Step 5 - A call that reads standing", "kicker": "A guard on a line"}),
    "card_guardrules": ("card", "list", {"heading": "Step 5 - A call that reads standing", "kicker": "Three rules for guards on lines"}),
    "card_number": ("card", "table", {"heading": "Step 7 - How the number is worked out", "kicker": "honest 40, generous 30"}),
    # the page's two-ship table (Step 8); its first header cell is empty, which the table card cannot draw
    "card_two": ("card", "rows", {"kicker": "Two ships: the Artemis gave the fee away",
                                  "header": ("What happens", "Artemis", "Intrepid"), "rows": (
        ("The quest completes: `earns guild honest 30`", "honest 30", "honest 30"),
        ("The answer: `earns guild generous 30`", "generous 30", "Nothing"),
        ("Standing with the Guild", "30", "17"),
        ("At the yard, Quill says", "The tug crews told me what you did", "The Guild yard is for members"),
        ("Answers offered", "Two", "One"))}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 7", "sub": "The story tools"}),
}

# Marks on the game stills (fractions of the 1280x960 frame), set from the screenshots 2026-10-15.
_ROW = ("rect", 0.0, 0.845, 0.275, 0.91)              # game_yard_row: Harbormaster Quill - The Guild yard
_COLD_TAKE = ("rect", 0.27, 0.82, 0.76, 0.86)         # game_yard_cold: ... Hold outside the markers.
_COLD_NAME = ("rect", 0.27, 0.775, 0.53, 0.815)       # ... Harbormaster Quill
_COLD_ANS = ("rect", 0.0, 0.925, 0.275, 0.965)        # ... the one answer: Understood, DS 1.
_COLD_LIST = ("rect", 0.0, 0.845, 0.275, 0.97)        # ... the list: Back, Understood
_WARM_TAKE = ("rect", 0.27, 0.82, 0.78, 0.86)         # game_yard_warm: ... The yard is open to you.
_WARM_BERTH = ("rect", 0.0, 0.925, 0.255, 0.97)       # ... Request a berth at the yard.
_REP_NAME = ("rect", 0.27, 0.775, 0.41, 0.815)        # game_report_two: Chief Ives
_REP_ANS = ("rect", 0.0, 0.875, 0.255, 0.99)          # ... both answers (Back scrolled off)
_REP_FEE = ("rect", 0.0, 0.925, 0.255, 0.99)          # ... It is ours. Give our fee to the tug crews.

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_yard_cold"},
        {"from": 1, "still": "game_yard_cold", "marks": [_COLD_TAKE]},
        {"from": 2, "still": "game_yard_warm", "marks": [_WARM_TAKE]},
        {"from": 3, "still": "game_yard_warm", "marks": [_WARM_BERTH]},
        {"from": 4, "still": "card_title"},
        {"from": 6, "still": "e_v1", "marks": [("lines", 289, 289)]},
    ]},
    "s02_a_copy_to_work_in": {"step": None, "beats": [
        {"from": 0, "still": "card_copy", "marks": [("part", "item2")]},
        {"from": 3, "still": "x_copy", "marks": [("part", "row:MyStanding")]},
        {"from": 4, "still": "card_copy", "marks": [("part", "item4")]},
        {"from": 5, "still": "t_copy", "marks": [("part", "run1:cmd")]},
        {"from": 6, "still": "t_copy", "marks": [("part", "run1:clean")]},
    ]},
    "s03_what_the_guild_values": {"step": 1, "beats": [
        {"from": 0, "still": "card_traits"},
        {"from": 1, "still": "card_traits", "marks": [("part", "r1"), ("part", "r4"), ("part", "r2")]},
        {"from": 3, "still": "card_traits"},
        {"from": 5, "still": "e_guild0", "marks": [("lines", 285, 290)]},
        {"from": 6, "still": "e_v1", "marks": [("lines", 289, 289)]},
        {"from": 7, "still": "e_v1", "marks": [("text", 289, "honest 40"), ("text", 289, "generous 30")]},
        {"from": 8, "still": "e_v1", "marks": [("text", 289, "40"), ("text", 289, "30")]},
        {"from": 10, "still": "t_v1", "marks": [("part", "run1:clean")]},
    ]},
    "s04_who_speaks_for_the_guild": {"step": 2, "beats": [
        {"from": 0, "still": "e_v1", "marks": [("lines", 289, 289)]},
        {"from": 1, "still": "game_yard_cold", "marks": [_COLD_NAME]},
        {"from": 3, "still": "e_v2", "marks": [("lines", 300, 300)]},
        {"from": 4, "still": "e_v2", "marks": [("text", 300, "guild")]},
        {"from": 5, "still": "e_v2", "marks": [("lines", 297, 302)]},
        {"from": 7, "still": "t_v2", "marks": [("part", "run1:clean")]},
    ]},
    "s05_two_deeds": {"step": 3, "beats": [
        {"from": 0, "still": "e_v1", "marks": [("lines", 289, 289)]},
        # the game first: the report call with its second answer
        {"from": 1, "still": "game_report_two", "marks": [_REP_NAME]},
        {"from": 2, "still": "game_report_two", "marks": [_REP_FEE]},
        {"from": 3, "still": "card_deed"},
        {"from": 5, "still": "e_v3", "marks": [("lines", 173, 173)]},
        {"from": 6, "still": "e_v3", "marks": [("text", 173, ",")]},
        {"from": 7, "still": "e_v3", "marks": [("text", 173, "earns guild honest 30")]},
        {"from": 10, "still": "e_v4", "marks": [("lines", 375, 375)]},
        {"from": 12, "still": "e_v4", "marks": [("text", 375, "earns guild generous 30")]},
        {"from": 13, "still": "e_v4", "marks": [("text", 374, "completes report_in"), ("text", 375, "completes report_in")]},
        {"from": 14, "still": "t_v4", "marks": [("part", "run1:clean")]},
    ]},
    "s06_a_call_that_reads_standing": {"step": 5, "beats": [
        {"from": 0, "still": "e_v4", "marks": [("lines", 374, 375)]},
        # the game first: the yard's call, the cold line
        {"from": 1, "still": "game_yard_row", "marks": [_ROW]},
        {"from": 3, "still": "game_yard_cold", "marks": [_COLD_TAKE]},
        {"from": 5, "still": "e_v5", "marks": [("lines", 183, 190)]},
        {"from": 6, "still": "e_v6", "marks": [("lines", 386, 395)]},
        {"from": 7, "still": "e_v6", "marks": [("lines", 392, 393)]},
        {"from": 10, "still": "e_v6", "marks": [("text", 392, "{standing < 30}"), ("text", 393, "{standing >= 30}")]},
        {"from": 11, "still": "e_v6", "marks": [("text", 392, "{standing < 30}")]},
        {"from": 12, "still": "e_v6", "marks": [("text", 393, "{standing >= 30}")]},
        {"from": 13, "still": "card_guardrules", "marks": [("part", "item3")]},
        {"from": 14, "still": "t_v6", "marks": [("part", "run1:clean")]},
    ]},
    "s07_an_answer_that_needs_standin": {"step": 6, "beats": [
        {"from": 0, "still": "game_yard_cold", "marks": [_COLD_LIST]},
        {"from": 1, "still": "game_yard_warm", "marks": [_WARM_TAKE]},
        {"from": 2, "still": "game_yard_warm", "marks": [_WARM_TAKE, _WARM_BERTH]},
        {"from": 3, "still": "e_final", "marks": [("text", 396, "if standing >= 30")]},
        {"from": 4, "still": "e_final", "marks": [("text", 396, "; completes yard_calls")]},
        {"from": 5, "still": "game_yard_cold", "marks": [_COLD_LIST]},
        {"from": 7, "still": "e_final", "marks": [("lines", 396, 396)]},
        {"from": 9, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s08_how_the_number_works": {"step": 7, "beats": [
        {"from": 0, "still": "card_number"},
        {"from": 1, "still": "card_number", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_number", "marks": [("part", "r2c4"), ("part", "r2c5")]},
        {"from": 7, "still": "card_number", "marks": [("part", "r3")]},
        {"from": 9, "still": "card_two"},
        {"from": 10, "still": "card_two", "marks": [("part", "r1")]},
        {"from": 11, "still": "card_two", "marks": [("part", "r2")]},
        {"from": 12, "still": "card_two", "marks": [("part", "r4")]},
    ]},
    "s09_play_it": {"step": 10, "beats": [
        {"from": 0, "still": "game_yard_row", "marks": [_ROW]},
        {"from": 2, "still": "game_yard_cold", "marks": [_COLD_TAKE]},
        {"from": 3, "still": "game_yard_cold", "marks": [_COLD_ANS]},
        {"from": 4, "still": "game_report_two"},
        {"from": 6, "still": "game_report_two", "marks": [_REP_ANS]},
        {"from": 7, "still": "game_report_two", "marks": [_REP_FEE]},
        {"from": 8, "still": "game_yard_row", "marks": [_ROW]},
        {"from": 9, "still": "game_yard_warm", "marks": [_WARM_TAKE]},
        {"from": 10, "still": "game_yard_warm", "marks": [_WARM_BERTH]},
    ]},
    "s10_what_lint_can_and_cannot_see": {"step": 9, "beats": [
        {"from": 0, "still": "e_gild", "marks": [("text", 173, "gild")]},
        {"from": 2, "still": "t_gild", "marks": [("span", 1, "is not a side in this mission"), ("span", 1, "Declared here: breaker, guild, tsn.")]},
        {"from": 3, "still": "e_noside", "marks": [("lines", 306, 310)]},
        {"from": 5, "still": "t_noside", "marks": [("part", "run1:clean")]},
        {"from": 6, "still": "game_yard_cold", "marks": [_COLD_TAKE]},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 5, "still": "card_next"},
    ]},
}
