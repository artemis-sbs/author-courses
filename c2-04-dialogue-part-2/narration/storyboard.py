"""Storyboard for c2-04-dialogue-part-2: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 3's finished file ("start", the whole chain). The answers
go in one step at a time, then the quest, then the call that comes back ("final", the
page's own example\\mission.amd).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. Start them with
`python game.py c2-04-dialogue-part-2 start --state g_near --consoles server,helm,comms`.
g_near is PROBE-ONLY (never shown in the editor): the hulk 1500 from the ship in place of
9000, so a short flight puts the ship inside 500 and the beat places Quill's call. Every
word on screen is the page's. A takes is picked by chance, so the line on a still may be
either of the scene's takes.
"""
LECTURE = "c2-04-dialogue-part-2"
TITLE = ("Class 2, Lecture 4", "Dialogue, part 2", "The crew answers")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_QUILL = "ter #e4cb8e 1 0;ter #fff 12 6;ter #e4cb8e 3 1;ter #e4cb8e 5 2;ter #704025 7 3;"
_COLD = "- [She is cold. No power, no lights.]"
_NOTNOW = "- [Not now, DS 1. Artemis out.]()"
_OFFER = ("\n### [The Offer](quill_offer)\n---\nSpeaker: quill\n---\n"
          "% Then she is salvage, and somebody has to hang a beacon on her before the Breakers do. Do you want the job?\n"
          "% Dead, then. That makes her salvage, and salvage wants a beacon. Are you offering?\n\n"
          "- [We will tag her.]()\n- [Find someone else, DS 1.]()\n")
_HISTORY = ("### [What DS 1 Knows](quill_history)\n---\nSpeaker: quill\n---\n"
            "% She came through the gate eleven days ago with her transponder off. Nobody has claimed her.\n"
            "% No flight plan, no transponder, no crew list. She arrived, and she stopped.\n\n"
            "- [She is cold, DS 1. No power, no lights.](quill_offer)\n- [Thank you, DS 1. Artemis out.]()\n\n")
_CALLS_END = "DS 1 saw the ship go in close, and wants to hear about it.\n"
_TAG = ("\n### [Tag the Hulk](tag_hulk)\n---\nScope: shared\nStarts when: revealed\n"
        "Objective: Give the salvage beacon 30 seconds to set\nDone when: 30 seconds\nReward: 150 credits\n---\n"
        "![](face://" + _QUILL + ") Harbormaster Quill, DS 1 traffic control\n\n"
        "DS 1 wants a salvage beacon on the hulk before the Breakers find her.\n\n"
        "A beacon makes her a claim on DS 1's salvage ledger. Until one is set, she belongs to whoever gets a "
        "line on her first, and the Breaker Cutter is already standing off.\n")
_TAG_END = "and the Breaker Cutter is already standing off.\n"
_BEACON = ("\n### [Beacon Set](beacon_set)\n---\nBeat\nStarts when: revealed\nAction:\n"
           "  - quill hails quill_thanks\n---\nThe beacon is live, and DS 1 calls to say so.\n")
_THANKS = ("\n### [Quill Calls Back](quill_thanks)\n---\nSpeaker: quill\nWhen: hail\nTitle: Your beacon\n---\n"
           "% Your beacon is singing, Artemis. The claim is logged in your name.\n"
           "% Beacon is live. That makes her yours, on paper.\n\n- [Glad to help, DS 1. Artemis out.]()\n")
_EX = "c2-04-dialogue-part-2/example"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example",
                       "c2-01-sides-and-factions/example", "c2-02-characters-and-faces/example",
                       "c2-03-dialogue-part-1/example")},
    # Step 1: two answers that end the call
    "a1": {"base": "start", "edits": [("append", FILE, "\n" + _COLD + "()\n" + _NOTNOW + "\n")]},
    # Step 2: the first one leads on (lint warns), then the scene it leads to
    "a2": {"base": "a1", "edits": [("replace", FILE, _COLD + "()", _COLD + "(quill_offer)")]},
    "a3": {"base": "a2", "edits": [("append", FILE, _OFFER)]},
    # Step 3: a second way in
    "a4": {"base": "a3", "edits": [
        ("replace", FILE, _COLD + "(quill_offer)\n" + _NOTNOW,
         _COLD + "(quill_offer)\n- [What do you know about her?](quill_history)\n" + _NOTNOW),
        ("replace", FILE, "### [The Offer](quill_offer)", _HISTORY + "### [The Offer](quill_offer)")]},
    # Step 4: the quest (lint warns: nothing reveals it), then the answer that accepts it
    "a5": {"base": "a4", "edits": [("replace", FILE, _CALLS_END, _CALLS_END + _TAG)]},
    "a6": {"base": "a5", "edits": [("replace", FILE, "- [We will tag her.]()", "- [We will tag her.]() ; accepts tag_hulk")]},
    # Step 5: two things at once
    "a7": {"base": "a6", "edits": [
        ("replace", FILE, "; accepts tag_hulk\n", "; accepts tag_hulk, completes ds1_calls\n"),
        ("replace", FILE, "- [Find someone else, DS 1.]()", "- [Find someone else, DS 1.]() ; completes ds1_calls")]},
    # Step 6: the Then line (lint warns), the beat (lint warns), the scene
    "a8": {"base": "a7", "edits": [("replace", FILE, "Reward: 150 credits\n---", "Reward: 150 credits\nThen: reveal beacon_set\n---")]},
    "a9": {"base": "a8", "edits": [("replace", FILE, _TAG_END, _TAG_END + _BEACON)]},
    "final": {"base": "a9", "edits": [("append", FILE, _THANKS)], "same_as": _EX + "/mission.amd"},
    # PROBE-ONLY, for the game stills: the hulk 1500 from the ship. Never shown in the editor.
    "g_near": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Unknown Hulk"', 'npc_spawn(0, 0, 1500, "Unknown Hulk"')]},
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}

STILLS = {
    "e_a0": ("vscode", "start", 292, "big", _NS),          # lines 282 to 302: Quill Checks In
    "e_a1": ("vscode", "a1", 295, "big", _NS),             # lines 285 to 305
    "e_a2": ("vscode", "a2", 295, "big", _NS),
    "e_a3": ("vscode", "a3", 305, "big", _NS),             # lines 295 to 315: the answers and The Offer
    "e_a4": ("vscode", "a4", 314, "mid", _NS),             # lines 300 to 328
    "e_tag": ("vscode", "a5", 160, "big", _NS),            # lines 150 to 170: Tag the Hulk
    "e_a6": ("vscode", "a6", 336, "big", _NS),             # lines 326 to 346: The Offer
    "e_a7": ("vscode", "a7", 336, "big", _NS),
    "e_a8": ("vscode", "a8", 160, "big", _NS),
    "e_a9": ("vscode", "a9", 168, "big", _NS),             # lines 158 to 178: the beat below the quest
    "e_thanks": ("vscode", "final", 355, "big", _NS),      # lines 345 to 365: the scene at the end
    "t_a1": ("terminal", [("a1", _LINT)]),
    "t_a2": ("terminal", [("a2", _LINT)]),
    "t_a3": ("terminal", [("a3", _LINT)]),
    "t_a5": ("terminal", [("a5", _LINT)]),
    "t_a6": ("terminal", [("a6", _LINT)]),
    "t_a8": ("terminal", [("a8", _LINT)]),
    "t_a9": ("terminal", [("a8", _LINT), ("a9", _LINT)]),
    "t_final": ("terminal", [("a9", _LINT), ("final", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). State g_near, consoles server,helm,comms. Fly inside
    # 500 of the hulk on Helm; on Comms open Quill's row, press Continue.
    "game_comms_answers": ("game", "Comms, Quill's call after Continue (state g_near): her closing question, and under it the three answers 'She is cold. No power, no lights.', 'What do you know about her?', 'Not now, DS 1. Artemis out.'"),
    "game_comms_history": ("game", "Comms, as game_comms_answers, after picking 'What do you know about her?': What DS 1 Knows, her line about the gate (or the other take), and the answers 'She is cold, DS 1. No power, no lights.' and 'Thank you, DS 1. Artemis out.'"),
    "game_comms_offer": ("game", "Comms, after 'She is cold...': The Offer, her offer ('...Do you want the job?' or '...Are you offering?') and the answers 'We will tag her.' and 'Find someone else, DS 1.'"),
    "game_log_tag": ("game", "Helm, the ePADD Quest Log right after 'We will tag her.' (state g_near): Tag the Hulk selected, Active: Quill's portrait and 'Harbormaster Quill, DS 1 traffic control' at the top, the order 'Give the salvage beacon 30 seconds to set', and the two paragraphs"),
    "game_log_tag_done": ("game", "Helm, the Quest Log 30 seconds after 'We will tag her.': Tag the Hulk Done, Reward 150 credits; DS 1 Calls listed as done"),
    "game_comms_thanks_row": ("game", "Comms, 30 seconds after 'We will tag her.': the Incoming Hails row 'Harbormaster Quill - Your beacon'"),
    "game_comms_thanks": ("game", "Comms, the Your beacon call open: Quill's face, one of its two takes, and the one answer 'Glad to help, DS 1. Artemis out.'"),
    "game_log_notag": ("game", "Helm, the Quest Log in a second start (state g_near), after answering 'Find someone else, DS 1.': no Tag the Hulk anywhere; DS 1 Calls listed as done"),
    "game_comms_back": ("game", "Comms, a third start: Quill's call opened, then Back pressed: the row 'Harbormaster Quill - About that hulk' is in the Incoming Hails list again"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_answer": ("card", "table", {"heading": "Step 1 - Give the crew something to say", "kicker": "An answer"}),
    "card_accepts": ("card", "table", {"heading": "Step 4 - An answer that does something", "kicker": "After the semicolon"}),
    "card_four": ("card", "table", {"heading": "Step 5 - Two things at once, and the four words", "kicker": "Four words"}),
    "card_depend": ("card", "table", {"heading": "Step 7 - Answers that depend on the story", "kicker": "Two ways"}),
    "card_if": ("card", "points", {"kicker": "A third way: not in this mission yet", "items": [
        "`- [words](scene_key) if some_name >= 10 ; accepts tag_hulk`",
        "It cannot read your quests or your credits.",
        "A name it cannot read counts as zero: never offered, and lint cannot tell.",
        "Lecture 6: a ship's standing with a side."]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Answers for your second call"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 5", "sub": "Hails"}),
}

# Marks on the game stills (fractions of the 1280x960 frame), set from the screenshots 2026-10-15.
# Comms shows an answer list two rows at a time, with a scroll bar at its right.
_TAKE = ("rect", 0.27, 0.82, 0.57, 0.86)              # game_comms_answers: her question
_LIST = ("rect", 0.0, 0.845, 0.275, 0.995)            # ... the answer list: Back, She is cold
_SCROLL = ("rect", 0.252, 0.875, 0.278, 0.995)        # ... its scroll bar: the other answers are below
_ANS2 = ("rect", 0.0, 0.925, 0.255, 0.985)            # ... the second row: She is cold (history: She is cold, DS 1)
_TAKE_HIST = ("rect", 0.27, 0.82, 0.965, 0.86)        # game_comms_history: the gate line
_TAKE_OFFER = ("rect", 0.27, 0.82, 0.88, 0.86)        # game_comms_offer: Dead, then ... Are you offering?
_OFFER_TAG = ("rect", 0.0, 0.875, 0.255, 0.915)       # ... We will tag her.
_OFFER_ANS = ("rect", 0.0, 0.875, 0.255, 0.97)        # ... both answers
_LOG_TAG_ROW = ("rect", 0.0, 0.503, 0.38, 0.573)      # game_log_tag: Tag the Hulk, Active
_LOG_ORDER = ("rect", 0.385, 0.075, 0.72, 0.19)       # ... State, Reward, the order
_LOG_FACE = ("rect", 0.385, 0.152, 0.74, 0.27)        # ... the order and Quill's portrait under it
_DONE_ROW = ("rect", 0.0, 0.575, 0.38, 0.645)         # game_log_tag_done: Tag the Hulk, Done
_DONE_STATE = ("rect", 0.385, 0.075, 0.62, 0.14)      # ... State Done, Reward 150 credits
_CALLS_DONE = ("rect", 0.0, 0.503, 0.2, 0.573)        # game_log_tag_done / game_log_notag: DS 1 Calls, Done
_NOTAG_LIST = ("rect", 0.0, 0.15, 0.38, 0.575)        # game_log_notag: the whole list, no Tag the Hulk
_ROW = ("rect", 0.0, 0.845, 0.275, 0.91)              # an Incoming Hails row
_COMPLETE = ("rect", 0.018, 0.493, 0.272, 0.527)      # game_comms_thanks_row: Quest complete: Tag the Hulk
_THANKS_TITLE = ("rect", 0.58, 0.735, 0.69, 0.772)    # game_comms_thanks: Your beacon
_THANKS_TAKE = ("rect", 0.27, 0.82, 0.76, 0.86)       # ... her take
_THANKS_ANS = ("rect", 0.0, 0.925, 0.275, 0.965)      # ... Glad to help, DS 1. Artemis out.

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_comms_answers"},
        {"from": 2, "still": "card_title"},
        {"from": 3, "still": "game_comms_history", "marks": [_TAKE_HIST]},
        {"from": 4, "still": "game_comms_offer", "marks": [_OFFER_TAG]},
        {"from": 5, "still": "e_a4", "marks": [("lines", 305, 305)]},
        {"from": 6, "still": "game_log_tag", "marks": [_LOG_TAG_ROW]},
    ]},
    "s02_an_answer": {"step": 1, "beats": [
        # the game first: the answers on Comms
        {"from": 0, "still": "game_comms_answers", "marks": [_TAKE]},
        {"from": 1, "still": "game_comms_answers", "marks": [_LIST]},
        {"from": 2, "still": "game_comms_answers", "marks": [_SCROLL]},
        {"from": 3, "still": "game_comms_answers", "marks": [_ANS2]},
        {"from": 4, "still": "e_a0", "marks": [("lines", 300, 301)]},
        {"from": 5, "still": "e_a1", "marks": [("lines", 303, 304)]},
        {"from": 6, "still": "e_a1", "marks": [("text", 303, "- ")]},
        {"from": 7, "still": "e_a1", "marks": [("text", 303, "[She is cold. No power, no lights.]")]},
        {"from": 8, "still": "e_a1", "marks": [("text", 303, "()")]},
        {"from": 9, "still": "card_answer"},
        {"from": 11, "still": "e_a1", "marks": [("text", 303, "[She is cold. No power, no lights.]"), ("text", 304, "[Not now, DS 1. Artemis out.]")]},
        {"from": 12, "still": "e_a1", "marks": [("text", 303, "()"), ("text", 304, "()")]},
        {"from": 13, "still": "t_a1", "marks": [("part", "run1:clean")]},
    ]},
    "s03_an_answer_that_leads_somewhe": {"step": 2, "beats": [
        {"from": 0, "still": "e_a2", "marks": [("text", 303, "(quill_offer)")]},
        {"from": 2, "still": "t_a2", "marks": [("span", 1, "dangling-choice")]},
        {"from": 4, "still": "game_comms_offer", "marks": [_TAKE_OFFER]},
        {"from": 5, "still": "game_comms_offer", "marks": [_TAKE_OFFER, _OFFER_ANS]},
        {"from": 6, "still": "e_a3", "marks": [("lines", 306, 314)]},
        {"from": 7, "still": "e_a3", "marks": [("hashes", 306)]},
        {"from": 8, "still": "e_a3", "marks": [("lines", 307, 309)]},
        {"from": 10, "still": "e_a3", "marks": [("text", 303, "(quill_offer)"), ("text", 306, "(quill_offer)")]},
    ]},
    "s04_a_second_way_in": {"step": 3, "beats": [
        {"from": 0, "still": "game_comms_answers", "marks": [_LIST]},
        {"from": 1, "still": "game_comms_history", "marks": [_TAKE_HIST]},
        {"from": 3, "still": "e_a4", "marks": [("lines", 304, 304)]},
        {"from": 4, "still": "e_a4", "marks": [("lines", 307, 315)]},
        {"from": 5, "still": "e_a4", "marks": [("text", 314, "(quill_offer)")]},
        {"from": 6, "still": "e_a4", "marks": [("text", 303, "(quill_offer)"), ("text", 314, "(quill_offer)"), ("text", 317, "(quill_offer)")]},
        {"from": 8, "still": "e_a4", "marks": [("lines", 303, 305)]},
    ]},
    "s05_the_quest": {"step": 4, "beats": [
        {"from": 0, "still": "e_a4", "marks": [("lines", 324, 325)]},
        # the game first: the quest in the Quest Log
        {"from": 3, "still": "game_log_tag"},
        {"from": 4, "still": "game_log_tag", "marks": [_LOG_TAG_ROW]},
        {"from": 5, "still": "game_log_tag", "marks": [_LOG_FACE]},
        {"from": 6, "still": "e_tag", "marks": [("lines", 153, 165)]},
        {"from": 7, "still": "e_tag", "marks": [("lines", 156, 156)]},
        {"from": 9, "still": "e_tag", "marks": [("lines", 161, 165)]},
        {"from": 10, "still": "e_tag", "marks": [("lines", 161, 161)]},
        {"from": 12, "still": "e_tag", "marks": [("lines", 163, 163)]},
        {"from": 13, "still": "e_tag", "marks": [("lines", 165, 165)]},
        {"from": 14, "still": "t_a5", "marks": [("span", 1, "never-revealed")]},
        {"from": 15, "still": "t_a5", "marks": [("span", 1, "no answer")]},
        {"from": 18, "still": "e_a6", "marks": [("lines", 338, 338)]},
        {"from": 19, "still": "e_a6", "marks": [("text", 338, ";")]},
        {"from": 20, "still": "e_a6", "marks": [("text", 338, "accepts tag_hulk")]},
        {"from": 21, "still": "card_accepts"},
    ]},
    "s06_two_things_at_once": {"step": 5, "beats": [
        {"from": 0, "still": "e_a7", "marks": [("text", 338, "; accepts tag_hulk, completes ds1_calls")]},
        {"from": 2, "still": "e_a7", "marks": [("text", 338, "completes ds1_calls"), ("text", 339, "completes ds1_calls")]},
        {"from": 4, "still": "card_four"},
        {"from": 5, "still": "card_four", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_four", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_four", "marks": [("part", "r3")]},
        {"from": 8, "still": "card_four", "marks": [("part", "r4")]},
    ]},
    "s07_the_call_that_comes_back": {"step": 6, "beats": [
        # the game first: the second call
        {"from": 0, "still": "game_comms_thanks_row"},
        {"from": 1, "still": "game_comms_thanks_row", "marks": [_COMPLETE]},
        {"from": 2, "still": "game_comms_thanks_row", "marks": [_ROW]},
        {"from": 3, "still": "game_comms_thanks", "marks": [_THANKS_TITLE]},
        {"from": 4, "still": "e_a8", "marks": [("lines", 160, 160)]},
        {"from": 6, "still": "t_a8", "marks": [("span", 1, "dangling-reveal")]},
        {"from": 7, "still": "e_a9", "marks": [("lines", 168, 175)]},
        {"from": 8, "still": "t_a9", "marks": [("span", 2, "dangling-action-ref")]},
        {"from": 9, "still": "e_thanks", "marks": [("lines", 351, 360)]},
        {"from": 9.6, "still": "t_final", "marks": [("part", "run2:clean")]},
        {"from": 10, "still": "game_comms_thanks", "marks": [_THANKS_TITLE, _THANKS_TAKE]},
    ]},
    "s08_if_and_why_not_yet": {"step": 7, "beats": [
        {"from": 0, "still": "card_depend"},
        {"from": 1, "still": "card_depend", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_depend", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_if", "marks": [("part", "item1")]},
        {"from": 6, "still": "card_if", "marks": [("part", "item2")]},
        {"from": 7, "still": "card_if", "marks": [("part", "item3")]},
        {"from": 9, "still": "card_if", "marks": [("part", "item4")]},
    ]},
    "s09_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_comms_answers"},
        {"from": 1, "still": "game_comms_answers", "marks": [_TAKE]},
        {"from": 2, "still": "game_comms_answers", "marks": [_LIST]},
        {"from": 3, "still": "game_comms_answers", "marks": [_SCROLL]},
        {"from": 5, "still": "game_comms_history", "marks": [_TAKE_HIST]},
        {"from": 6, "still": "game_comms_history", "marks": [_ANS2]},
        {"from": 7, "still": "game_comms_offer", "marks": [_TAKE_OFFER]},
        {"from": 8, "still": "game_comms_offer", "marks": [_OFFER_TAG]},
        {"from": 9, "still": "game_log_tag"},
        {"from": 10, "still": "game_log_tag", "marks": [_LOG_TAG_ROW]},
        {"from": 11, "still": "game_log_tag", "marks": [_LOG_FACE]},
        {"from": 12, "still": "game_log_tag_done", "marks": [_DONE_ROW, _DONE_STATE]},
        {"from": 13, "still": "game_comms_thanks_row", "marks": [_ROW]},
    ]},
    "s10_the_other_roads": {"step": None, "beats": [
        {"from": 0, "still": "game_comms_offer", "marks": [_OFFER_ANS]},
        {"from": 1, "still": "game_log_notag", "marks": [_NOTAG_LIST]},
        {"from": 2, "still": "game_log_notag", "marks": [_CALLS_DONE]},
        {"from": 3, "still": "game_comms_answers", "marks": [_SCROLL]},
        {"from": 5, "still": "game_comms_back"},
        {"from": 6, "still": "game_comms_back", "marks": [_ROW]},
        {"from": 9, "still": "e_a7", "marks": [("lines", 339, 339)]},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_next"},
    ]},
}
