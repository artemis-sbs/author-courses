"""Storyboard for c2-02-characters-and-faces: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 1's finished files (the chain from Class 1 Lecture 3's
seven files, with every later example laid over them: "start"). The three people are
typed one at a time and the face line goes on Close Inspection last ("final", the page's
own example\\mission.amd).

WHAT IS NOT A CAPTURE. The Story Graph opens by a command (amd.showGraph), and Preview Node
too (amd.showPreview, with the cursor inside the record); those are real windows, read once
they stop changing. The Inspector (right-click a box, Edit...), its Face... list and the
Face Builder are reached only by clicks inside the graph, which this pipeline never makes:
those are cards in the page's own words. Two rolls of `Face: female` are a card too.

GAME STILL. One, taken 2026-10-15, marked: the Quest Log with Quill's portrait (state final).
"""
LECTURE = "c2-02-characters-and-faces"
TITLE = ("Class 2, Lecture 2", "Characters and faces", "Three people, and a face that stays")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_QUILL = "ter #e4cb8e 1 0;ter #fff 12 6;ter #e4cb8e 3 1;ter #e4cb8e 5 2;ter #704025 7 3;"
_IVES = "ter #d2b2a1 0 0;ter #fff 13 6;ter #d2b2a1 11 1;ter #d2b2a1 12 2;ter #934e2c 11 3;ter #fff 9 5;"
_SABLE = "ska #813e20 1 0;ska #fff 1 4;ska #813e20 2 1;ska #813e20 1 2;ska #fff 4 3;"
_HEAD = ("\n\n// ---- Characters. The people in the story. `Face:` is how each one looks.\n"
         "## [Characters](characters)\n\n")
_Q = ("### [Harbormaster Quill](quill)\n---\nFace: female\n---\n"
      "Runs traffic control on DS 1. Has watched this lane for eleven years.\n")
_I = "\n### [Chief Ives](ives)\n---\nFace: male\n---\nKeeps the salvage ledger on DS 1. Counts everything twice.\n"
_S = ("\n### [Captain Sable](sable)\n---\nFace: female\n---\n"
      "Flies the Breaker Cutter. Has never paid for a ship in her life.\n")
_HAILS = "---\nThe hulk is not answering hails."
_EX = "c2-02-characters-and-faces/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example",
                       "c2-01-sides-and-factions/example")},
    # Step 1: the section and Quill, with a keyword
    "q1": {"base": "start", "edits": [("append", FILE, _HEAD + _Q)]},
    # Step 3: her face, written down
    "q2": {"base": "q1", "edits": [("replace", FILE, "Face: female", "Face: " + _QUILL)]},
    # Step 5: Ives, then his face
    "i1": {"base": "q2", "edits": [("append", FILE, _I)]},
    "i2": {"base": "i1", "edits": [("replace", FILE, "Face: male", "Face: " + _IVES)]},
    # Step 6: Sable, then a Skaraan face
    "s1": {"base": "i2", "edits": [("append", FILE, _S)]},
    "s2": {"base": "s1", "edits": [("replace", FILE, "Face: female", "Face: " + _SABLE)]},
    # Step 10: her face on Close Inspection, and the page's own file
    "final": {"base": "s2", "edits": [("replace", FILE, _HAILS, "---\n![](face://" + _QUILL
                                       + ") Harbormaster Quill, DS 1 traffic control\n\nThe hulk is not answering hails.")],
              "same_as": _EX + "/mission.amd"},
    # Scene 8: Enter pressed in the middle of Sable's string. Scene 9: Face: woman
    "b_enter": {"base": "s2", "edits": [("replace", FILE, "ska #fff 1 4;ska #813e20 2 1;", "ska #fff 1 4;\nska #813e20 2 1;")]},
    "b_woman": {"base": "s2", "edits": [("replace", FILE, "Face: " + _QUILL, "Face: woman")]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    "m_48": ("vscode", "start", 48, "big", _M),
    "e_end0": ("vscode", "start", 240, "big", _NS),        # lines 230 to 250: the Harbor Guild at the end
    "e_q1": ("vscode", "q1", 255, "big", _NS),             # lines 245 to 265
    "e_q2": ("vscode", "q2", 257, "big", _NS),
    # the Story Graph, by its command (no clicks); read once the window stops changing
    "v_graph": ("vscode", "q1", 257, "wide", {"side": False, "plain": True, "do": [["amd.showGraph"], 8000]}),
    "e_i1": ("vscode", "i1", 263, "big", _NS),
    "e_i2": ("vscode", "i2", 263, "big", _NS),
    "e_s1": ("vscode", "s1", 262, "big", _NS),             # lines 252 to 272: all three
    "e_s2": ("vscode", "s2", 262, "big", _NS),
    "e_enter": ("vscode", "b_enter", 262, "big", _NS),
    "e_woman": ("vscode", "b_woman", 257, "big", _NS),
    # Preview Node, by its command, the cursor inside each record
    "v_prev_quill": ("vscode", "s2", 257, "big", {"side": False, "plain": True, "do": [["amd.showPreview"], 5000]}),
    "v_prev_ives": ("vscode", "s2", 263, "big", {"side": False, "plain": True, "do": [["amd.showPreview"], 5000]}),
    "v_prev_sable": ("vscode", "s2", 269, "big", {"side": False, "plain": True, "do": [["amd.showPreview"], 5000]}),
    # Close Inspection, before and after the face line (lines 75 to 95)
    "e_close0": ("vscode", "s2", 85, "big", _NS),
    "e_close": ("vscode", "final", 85, "big", _NS),
    "t_q1": ("terminal", [("q1", _LINT)]),
    "t_enter": ("terminal", [("b_enter", _LINT)]),
    "t_woman": ("terminal", [("b_woman", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME (taken 2026-10-15): game.py c2-02-characters-and-faces start --state final
    "game_log_quill": ("game", "Helm, the ePADD Quest Log (the handheld icon top left, then Quests). State final, at the start. Close Inspection selected (Active from the start): Quill's portrait at the top of its description, two lines tall, with 'Harbormaster Quill, DS 1 traffic control' beside it, then the paragraphs and the heading Why it matters"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_keywords": ("card", "table", {"heading": "Step 2 - What one word gets you", "kicker": "Seven keywords, all human"}),
    "card_roll": ("card", "points", {"kicker": "Face: female, in two games", "items": [
        "Each game rolls her again: eyes, mouth, hair, clothes and skin.",
        "Tonight one woman. Tomorrow another.",
        "About half the rolls come up with skin that is green, blue or pink."]}),
    "card_inspector": ("card", "points", {"kicker": "In the Story Graph (clicks: not captured)", "items": [
        "Right-click the box Harbormaster Quill, and choose Edit...",
        "The AMD Inspector tab opens: her record as a form.",
        "Beside the Face box, click Face...",
        "From the list, choose Random Terran (female)."]}),
    "card_builder": ("card", "table", {"heading": "Step 4 - Change one thing about her", "kicker": "The AMD Face Builder (click her portrait)"}),
    "card_ives": ("card", "points", {"kicker": "Chief Ives (clicks: not captured)", "items": [
        "The graph has drawn a box for him already.",
        "Right-click it, Edit..., Face...",
        "Random Terran (male). Not him? Roll again."]}),
    "card_races": ("card", "table", {"heading": "Step 6 - Someone who is not human", "kicker": "Six peoples"}),
    "card_rules": ("card", "list", {"heading": "Step 7 - Four rules for a face string", "kicker": "Four rules"}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (1, 2, 3)}),
    "card_parts": ("card", "table", {"heading": "Step 10 - Her face on a job", "kicker": "One line, at the top of the description"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A fourth person"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 3", "sub": "Dialogue, part 1"}),
}

_QUILL_REC = ("lines", 255, 259)

# Marks on game_log_quill (fractions of the 1280x960 frame), set from the screenshot 2026-10-15.
_QL_ROW = ("rect", 0.025, 0.36, 0.38, 0.43)           # Close Inspection, Active, selected
_QL_ORDER = ("rect", 0.385, 0.152, 0.62, 0.19)        # the order: Close to within 500 of the hulk
_QL_QUILL = ("rect", 0.385, 0.195, 0.74, 0.27)        # the portrait and Harbormaster Quill, DS 1 traffic control

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        # the game first: her face in the Quest Log
        {"from": 0, "still": "game_log_quill", "marks": [_QL_ROW]},
        {"from": 1, "still": "game_log_quill", "marks": [_QL_QUILL]},
        {"from": 2, "still": "card_title"},
        {"from": 3, "still": "e_end0"},
        {"from": 6, "still": "e_s2", "marks": [("lines", 255, 271)]},
        {"from": 8, "still": "e_s2", "marks": [("lines", 253, 253)]},
    ]},
    "s02_one_person": {"step": 1, "beats": [
        {"from": 0, "still": "m_48", "marks": [("lines", 48, 48)]},
        {"from": 2, "still": "m_48", "marks": [("text", 48, "\"characters\"")]},
        {"from": 4, "still": "e_q1", "marks": [("lines", 253, 253)]},
        {"from": 5, "still": "e_q1", "marks": [("hashes", 255)]},
        {"from": 6, "still": "e_q1", "marks": [("text", 255, "[Harbormaster Quill]"), ("text", 255, "(quill)")]},
        {"from": 7, "still": "e_q1", "marks": [("lines", 257, 257)]},
        {"from": 9, "still": "e_q1", "marks": [("lines", 259, 259)]},
        {"from": 11, "still": "t_q1", "marks": [("part", "run1:clean")]},
    ]},
    "s03_what_one_word_gets_you": {"step": 2, "beats": [
        {"from": 0, "still": "card_keywords"},
        {"from": 2, "still": "card_roll", "marks": [("part", "item1")]},
        {"from": 5, "still": "card_roll", "marks": [("part", "item2")]},
        {"from": 6, "still": "card_roll", "marks": [("part", "item3")]},
        {"from": 7, "still": "e_q1", "marks": [_QUILL_REC]},
    ]},
    "s04_a_face_that_stays": {"step": 3, "beats": [
        {"from": 0, "still": "e_q1", "marks": [("text", 257, "Face: female")]},
        {"from": 2, "still": "v_graph"},
        {"from": 7, "still": "card_inspector", "marks": [("part", "item1")]},
        {"from": 8, "still": "card_inspector", "marks": [("part", "item2")]},
        {"from": 10, "still": "card_inspector", "marks": [("part", "item3"), ("part", "item4")]},
        {"from": 12, "still": "e_q2"},
        {"from": 13, "still": "e_q2", "marks": [("lines", 257, 257)]},
    ]},
    "s05_change_one_thing": {"step": 4, "beats": [
        {"from": 0, "still": "card_builder"},
        {"from": 4, "still": "card_builder", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_builder", "marks": [("part", "r3")]},
        {"from": 8, "still": "card_builder", "marks": [("part", "r5")]},
        {"from": 11, "still": "e_q2", "marks": [("lines", 257, 257)]},
    ]},
    "s06_the_second_person": {"step": 5, "beats": [
        {"from": 0, "still": "e_i1", "marks": [("lines", 261, 265)]},
        {"from": 2, "still": "e_i1", "marks": [("text", 263, "Face: male")]},
        {"from": 3, "still": "card_ives", "marks": [("part", "item1")]},
        {"from": 4, "still": "card_ives", "marks": [("part", "item2")]},
        {"from": 5, "still": "e_i2", "marks": [("lines", 263, 263)]},
        {"from": 6, "still": "card_ives", "marks": [("part", "item3")]},
    ]},
    "s07_someone_who_is_not_human": {"step": 6, "beats": [
        {"from": 0, "still": "e_s1", "marks": [("lines", 267, 271)]},
        {"from": 2, "still": "card_races"},
        {"from": 3, "still": "card_races", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_races", "marks": [("part", "r2"), ("part", "r3"), ("part", "r4"), ("part", "r5"), ("part", "r6")]},
        {"from": 6, "still": "e_s1", "marks": [("text", 269, "Face: female")]},
        {"from": 7, "still": "e_s2", "marks": [("lines", 269, 269)]},
        {"from": 8, "still": "card_races", "marks": [("part", "r2")]},
    ]},
    "s08_four_rules": {"step": 7, "beats": [
        {"from": 0, "still": "e_s2", "marks": [("lines", 257, 257), ("lines", 263, 263), ("lines", 269, 269)]},
        {"from": 2, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 6, "still": "e_s2", "marks": [("lines", 269, 269)]},
        {"from": 7, "still": "e_enter", "marks": [("lines", 269, 270)]},
        {"from": 8, "still": "t_enter", "marks": [("span", 1, "fence-syntax")]},
        {"from": 9, "still": "card_rules"},
    ]},
    "s09_what_lint_cannot_see": {"step": 8, "beats": [
        {"from": 0, "still": "e_q2", "marks": [("lines", 257, 257)]},
        {"from": 1, "still": "e_woman", "marks": [("text", 257, "Face: woman")]},
        {"from": 3, "still": "t_woman", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_cannot"},
    ]},
    "s10_look_at_them": {"step": 9, "beats": [
        {"from": 0, "still": "e_s2", "marks": [("lines", 255, 271)]},
        {"from": 2, "still": "e_s2", "marks": [_QUILL_REC]},
        {"from": 4, "still": "v_prev_quill"},
        {"from": 5, "still": "v_prev_ives"},
        {"from": 5.5, "still": "v_prev_sable"},
    ]},
    "s11_her_face_on_a_job": {"step": 10, "beats": [
        # the game first: her portrait on Close Inspection
        {"from": 0, "still": "game_log_quill"},
        {"from": 2, "still": "game_log_quill", "marks": [_QL_ROW]},
        {"from": 3, "still": "game_log_quill", "marks": [_QL_ORDER, _QL_QUILL]},
        {"from": 4, "still": "game_log_quill", "marks": [_QL_QUILL]},
        {"from": 5, "still": "e_close0", "marks": [("lines", 85, 85)]},
        {"from": 7, "still": "e_q2", "marks": [("text", 257, _QUILL)]},
        {"from": 10, "still": "card_parts", "marks": [("part", "r1")]},
        {"from": 12, "still": "e_close", "marks": [("lines", 85, 85)]},
        {"from": 13, "still": "e_close", "marks": [("text", 85, "Harbormaster Quill, DS 1 traffic control")]},
        {"from": 14, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 15, "still": "e_close", "marks": [("lines", 85, 85)]},
    ]},
    "s12_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_next"},
    ]},
}
