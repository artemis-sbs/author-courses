"""Storyboard for c2-07-the-story-tools: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5 and 6 (c1-05's docstring has every kind of still and mark). Written 2026-10-15.

THE FOLDER. The lecture starts from Lecture 5's finished mission: Lecture 3's seven files,
with Class 2 Lecture 1's story.mast and Lecture 5's mission.amd laid over them ("start").
Each step is a state: the four notes ("notes"), the three pointers ("plan"), then each new
record ("w_claim", "w_vane", "final" = this lecture's example, byte for byte), and the cut
("cut").

THE FOUR VIEWS are real: the add-on's own commands run in the throwaway window by the "do"
list (amd.showStoryOutline, amd.showTimeline, amd.showGraph, amd.showMissing). Each view
opens beside the file; the cursor goes back to the file so the line band is still found. A
wait comes first, so the language server is up before the view asks it for its model. The
hover box is the add-on's own too: the cursor is moved onto `report_in` and
editor.action.showHover is run. Marks on a view are rects, set after the still exists.

NOT MADE BY make.py. `sbs docs MyMission --lens all --title "My Mission"` has quote marks in
it, and make.py would wipe the __docs__ folder it writes before the pages were drawn, so the
docs prompt and the four pages are made by the Class 2 helper (scratchpad c2sbx\\c2pic.py,
from C2PIC below; they are ("derived", ...) in STILLS).

GAME STILLS (all ten taken 2026-10-15; marks are rects measured on them). Every one is the probe mission:
    python game.py c2-07-the-story-tools start --state <state> --consoles server,helm,comms
and, to skip the flight, the probe-only patch Class 1 used, with the hulk inside 500 at once:
    --patch "npc_spawn(0, 0, 9000, \\"Unknown Hulk\\"=>npc_spawn(0, 0, 400, \\"Unknown Hulk\\""
The Quest Log is on Helm's handheld: the handheld icon top left, then Quests. A call is on
Comms: the row in Incoming Hails, then Continue, then the answers.
"""
import os as _os

LECTURE = "c2-07-the-story-tools"
TITLE = ("Class 2, Lecture 7", "The story tools", "Four views, and a to-do list the tool writes")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))


def _final_lines():
    with open(_os.path.join(_HERE, "example", FILE), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n").split("\n")


_L = _final_lines()
_CLAIM = "\n".join(_L[187:206])          # lines 188 to 206 of the finished file: The Claim
_VANE = "\n".join(_L[338:343])           # lines 339 to 343: Assessor Vane
_RIVALS = "\n".join(_L[405:413])         # lines 406 to 413: Who Else Is Asking

_NOTES = [
    ("### [First Contact](first_contact)\n---",
     "### [First Contact](first_contact)\n= The mystery. It stays open until the crew reads the log.\n---"),
    ("#### [Close Inspection](approach)\n---",
     "#### [Close Inspection](approach)\n= The crew sees the hulk up close. DS 1 sees them do it, and that starts the talking.\n---"),
    ("### [DS 1 Calls](ds1_calls)\n---",
     "### [DS 1 Calls](ds1_calls)\n= The offer. Quill needs a beacon on the hulk and has nobody else to send.\n---"),
    ("### [Report to DS 1](report_in)\n---",
     "### [Report to DS 1](report_in)\n= End of act one. The crew has done DS 1 a favor, and now DS 1 owes them the truth.\n---"),
]
_ANSWER = "- [It is ours, DS 1. The beacon is set.]() ; completes report_in"
_SENT = "The beacon is live. DS 1 pays when she hears it from the ship."
_RECORD = "so that it is on the record.\n"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c2-01-sides-and-factions/example", "c2-05-hails/example"),
              "same_as": "c2-05-hails/example/mission.amd"},
    # Step 2: four notes
    "notes": {"base": "start", "edits": [("replace", FILE, a, b) for a, b in _NOTES]},
    # Step 4: three pointers at things that are not written yet
    "plan": {"base": "notes", "edits": [
        ("replace", FILE, "Reward: 150 credits\nAction:", "Reward: 150 credits\nThen: reveal claim\nAction:"),
        ("replace", FILE, _SENT, _SENT + " Chief Ives says [[vane]] has been asking what she is worth."),
        ("replace", FILE, _ANSWER + "\n", _ANSWER + "\n- [Who else is asking about her?](quill_rivals)\n")]},
    # Step 6: the three records, one at a time
    "w_claim": {"base": "plan", "edits": [("replace", FILE, _RECORD + "\n", _RECORD + "\n" + _CLAIM + "\n\n")]},
    "w_vane": {"base": "w_claim", "edits": [
        ("replace", FILE, "Has never paid for a ship in her life.\n\n",
         "Has never paid for a ship in her life.\n\n" + _VANE + "\n\n")]},
    "final": {"base": "w_vane", "edits": [("append", FILE, "\n" + _RIVALS + "\n")],
              "same_as": "c2-07-the-story-tools/example/mission.amd"},
    # Step 7: the scene cut, still in the file
    "cut": {"base": "final", "edits": [
        ("replace", FILE, "### [What DS 1 Knows](quill_history)", "/*\n### [What DS 1 Knows](quill_history)"),
        ("replace", FILE, "- [Thank you, DS 1. Artemis out.]()\n", "- [Thank you, DS 1. Artemis out.]()\n*/\n")]},
}

_MISS = "sbs lint MyMission --missing"
_DOCS = 'sbs docs MyMission --lens all --title "My Mission"'
_NS = {"side": False}
_WAIT = 7000                                              # ms: the language server first


def _view(command):
    return {"side": False, "do": [_WAIT, [command], 4000, ["workbench.action.focusFirstEditorGroup"]]}


# Made by c2pic.py (see the docstring): the docs prompt, and the pages it wrote, drawn at once
C2PIC = {
    "t_docs": ("term", [("final", None, _DOCS)], {"web": {
        # "top": pixels down the page (drawn at twice the size), as if the reader had scrolled there
        "w_prose": ("__docs__/My Mission-prose.html", {"scale": 2.0, "top": 2400}),         # Quests: First Contact, its note
        "w_screenplay": ("__docs__/My Mission-screenplay.html", {"scale": 2.0, "top": 2130}),  # QUILL CHECKS IN
        "w_catalog": ("__docs__/My Mission-catalog.html", {"scale": 2.0, "top": 1950}),     # Side, Lifeform
        "w_bible": ("__docs__/My Mission-bible.html", {"scale": 2.0, "top": 1950})}}),      # The shape of it, Beat 1
}

STILLS = {
    # Step 1: the file, top to bottom (Side Bar hidden)
    "e_top": ("vscode", "start", 14, "mid", _NS),            # lines 1 to 28 or so: notes, the root, Quests
    "e_quests": ("vscode", "start", 150, "mid", _NS),        # the middle of the Quests section
    "e_people": ("vscode", "start", 330, "mid", _NS),        # Characters and Dialogue
    "t_none0": ("terminal", [("start", _MISS)]),
    # Step 2: notes
    "e_fc": ("vscode", "start", 31, "big", _NS),             # lines 21 to 41: First Contact, no note
    "e_fc_note": ("vscode", "notes", 31, "big", _NS),        # the note on line 29
    "e_notes_mid": ("vscode", "notes", 160, "mid", _NS),     # DS 1 Calls (note 147) and Report to DS 1 (note 172)
    "e_hover": ("vscode", "notes", 162, "big", {"side": False, "do": [
        _WAIT, ["cursorEnd"], ["cursorWordLeft"], ["editor.action.showHover"], 2500]}),
    # Step 3: the views. The editor's icons, then each view beside the file
    "e_icons": ("vscode", "notes", 31, "big", _NS),
    "v_outline": ("vscode", "notes", 31, "mid", _view("amd.showStoryOutline")),
    "v_timeline": ("vscode", "notes", 31, "mid", _view("amd.showTimeline")),
    "v_graph": ("vscode", "notes", 31, "mid", _view("amd.showGraph")),
    "v_timeline_final": ("vscode", "final", 192, "mid", _view("amd.showTimeline")),
    # Step 4: the three pointers
    "e_rep": ("vscode", "notes", 178, "big", _NS),           # lines 168 to 188: Report to DS 1 before
    "e_plan_rep": ("vscode", "plan", 178, "big", _NS),       # Then: reveal claim (178), the link (184)
    "e_plan_ans": ("vscode", "plan", 372, "big", _NS),       # lines 362 to 382: the new answer on 378
    # Step 5: the list
    "t_miss3": ("terminal", [("plan", _MISS)]),
    "v_missing": ("vscode", "plan", 178, "mid", _view("amd.showMissing")),
    # Step 6: each record, and the list after it
    "e_claim": ("vscode", "w_claim", 197, "big", _NS),       # lines 187 to 207: The Claim
    "t_miss2": ("terminal", [("w_claim", _MISS)]),
    "e_vane": ("vscode", "w_vane", 341, "big", _NS),         # lines 331 to 351: Assessor Vane
    "t_miss1": ("terminal", [("w_vane", _MISS)]),
    "e_rivals": ("vscode", "final", 403, "big", _NS),        # lines 393 to 413: the answer and the scene
    "t_none_end": ("terminal", [("final", _MISS)]),
    # Step 7: the cut
    "e_hist": ("vscode", "final", 366, "big", _NS),          # lines 356 to 376: Quill Checks In's answers, What DS 1 Knows
    "e_cut": ("vscode", "cut", 373, "big", _NS),             # lines 363 to 383: /* on 368, */ on 378
    "t_cut": ("terminal", [("cut", _MISS)]),
    # Step 8: made by c2pic.py
    "t_docs": ("derived", "made by c2pic.py: sbs docs, run as typed"),
    "w_prose": ("derived", "made by c2pic.py: the prose page, as Edge draws it"),
    "w_screenplay": ("derived", "made by c2pic.py: the screenplay page"),
    "w_catalog": ("derived", "made by c2pic.py: the catalog page"),
    "w_bible": ("derived", "made by c2pic.py: the bible page"),
    # The game. None taken yet. States and clicks: see the docstring.
    "game_fc_log": ("game", "Helm's handheld, Quests: the Quest Log with First Contact selected and its description in the pane ('A dead ship has drifted across the border...'). State final (notes never show). No flying needed: open the handheld (icon top left), Quests, First Contact"),
    "game_offer_comms": ("game", "Comms: the call Harbormaster Quill - About that hulk open, after She is cold: Quill's offer and the two answers 'We will tag her.' and 'Find someone else, DS 1.'. State final, hulk patched to 400 so the call comes at once; Incoming Hails row, Continue, 'She is cold. No power, no lights.'"),
    "game_rep_log": ("game", "Helm's handheld, Quests: Report to DS 1 selected, its page in the pane ending 'DS 1 pays when she hears it from the ship.' (NO Vane sentence). State START: call 1, Continue, She is cold, We will tag her; wait 30 s for Tag the Hulk; then the handheld, Quests, Report to DS 1"),
    "game_thanks_ives": ("game", "Comms: Harbormaster Quill - Your beacon open, after Continue: Chief Ives's face and line, ONE answer 'It is ours, DS 1. The beacon is set.'. State START, as game_rep_log, then the second row in Incoming Hails, Continue"),
    "game_thanks_two": ("game", "Comms: the same as game_thanks_ives, state FINAL: Chief Ives's line and TWO answers, the second 'Who else is asking about her?'"),
    "game_rivals_comms": ("game", "Comms: after 'Who else is asking about her?', Quill's scene Who Else Is Asking: her line about Sable and the Guild's assessor, and the one answer 'Then log the claim, DS 1. The beacon is set.'. State final"),
    "game_hello_comms": ("game", "Comms: Harbormaster Quill - About that hulk open, after Continue: Quill's second line and the THREE answers, the middle one 'What do you know about her?'. State final, hulk patched to 400"),
    "game_vane_log": ("game", "Helm's handheld, Quests: Report to DS 1 selected; its page ends 'Chief Ives says Assessor Vane has been asking what she is worth.' (the link printed as the name). State final, as game_rep_log"),
    "game_claim_log": ("game", "Helm's handheld, Quests: The Claim selected, Active: its order 'Stand by the hulk for 60 seconds', the sentence, the heading 'Who else wants her', the two-row table (Sable, Vane), the closing paragraph. State final, after 'Then log the claim, DS 1.' on Comms"),
    "game_claim_done": ("game", "Helm's handheld, Quests: The Claim selected, Done, Reward 200 credits. State final, about 60 s after game_claim_log; keep the ship by the hulk"),
    # Cards
    "card_title": ("card", "title", {}),
    "card_gaps": ("card", "table", {"heading": "Step 3 - Four views of the same file", "nth": 3,
                                    "kicker": "The timeline does not know everything"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 8", "sub": "A Siege boss"}),
}

# Marks on the game stills (fractions of the 1280x960 frame, measured on the taken stills)
_QL_FC = ("rect", 0.0, 0.146, 0.38, 0.214)          # Quest Log: the First Contact row
_QL_SEL5 = ("rect", 0.0, 0.505, 0.38, 0.573)        # Quest Log: the selected fifth row
_QL_DESC = ("rect", 0.385, 0.075, 0.985, 0.235)     # First Contact's description and its link
_QL_STATE = ("rect", 0.385, 0.075, 0.6, 0.14)       # State and Reward
_QL_VANE = ("rect", 0.385, 0.28, 0.98, 0.348)       # the sentence with the Vane link in it
_QL_VNAME = ("rect", 0.385, 0.31, 0.505, 0.348)     # 'Assessor Vane', printed as a plain name
_CLAIM_PAGE = ("rect", 0.385, 0.155, 0.99, 0.51)    # The Claim: order, sentence, heading, table, closing
_CLAIM_TABLE = ("rect", 0.385, 0.285, 0.99, 0.44)   # The Claim: the heading and the two-row table
_C_SPEAKER = ("rect", 0.27, 0.445, 0.9, 0.86)       # Comms: the face, the name and the line
_C_LINE = ("rect", 0.27, 0.775, 0.9, 0.86)          # Comms: the name and the line
_C_ANS1 = ("rect", 0.0, 0.878, 0.27, 0.92)          # Comms: the first answer row on view
_C_ANS2 = ("rect", 0.0, 0.922, 0.27, 0.966)         # Comms: the second answer row on view
_C_ANS_HL = ("rect", 0.0, 0.927, 0.275, 0.98)       # Comms: the one answer, under Back

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "v_timeline_final"},
        {"from": 2, "still": "card_title"},
        {"from": 4, "still": "t_miss3", "marks": [("out", 1, 1)]},
    ]},
    "s02_why_a_file_isn_t_enough": {"step": 1, "beats": [
        {"from": 0, "still": "e_top"},
        {"from": 1, "still": "e_quests"},
        {"from": 2, "still": "e_people"},
        {"from": 3, "still": "t_none0", "marks": [("part", "run1:cmd")]},
        {"from": 4, "still": "t_none0", "marks": [("part", "run1:cmd")]},
        {"from": 5, "still": "t_none0", "marks": [("out", 1, 1)]},
    ]},
    "s03_a_note_on_a_record": {"step": 2, "beats": [
        {"from": 0, "still": "game_fc_log", "marks": [_QL_FC]},
        {"from": 1, "still": "game_fc_log", "marks": [_QL_DESC]},
        {"from": 3, "still": "e_fc", "marks": [("lines", 28, 28), ("lines", 35, 35)]},
        {"from": 5, "still": "e_fc_note", "marks": [("lines", 29, 29)]},
        {"from": 6, "still": "e_fc_note", "marks": [("text", 29, "= ")]},
        {"from": 7, "still": "e_fc_note", "marks": [("lines", 29, 29)]},
        {"from": 8, "still": "e_notes_mid", "marks": [("lines", 147, 147), ("lines", 172, 172)]},
        {"from": 9, "still": "game_fc_log", "marks": [_QL_DESC]},
        {"from": 11, "still": "e_hover", "marks": [("text", 162, "report_in")]},
        {"from": 13, "still": "e_fc_note", "marks": [("text", 29, "= ")]},
    ]},
    "s04_three_views": {"step": 3, "beats": [
        {"from": 0, "still": "e_icons"},
        {"from": 2, "still": "v_outline"},
        {"from": 4, "still": "v_timeline"},
        {"from": 8, "still": "v_graph"},
        {"from": 10, "still": "v_timeline"},
    ]},
    "s05_what_the_timeline_can_t_see": {"step": None, "beats": [
        {"from": 0, "still": "v_timeline"},
        {"from": 3, "still": "card_gaps"},
        {"from": 5, "still": "v_timeline"},
        {"from": 6, "still": "game_offer_comms", "marks": [_C_ANS1]},
        {"from": 7, "still": "v_timeline"},
        {"from": 8, "still": "w_screenplay"},
    ]},
    "s06_plan_act_two_by_pointing_at_": {"step": 4, "beats": [
        {"from": 0, "still": "e_rep", "marks": [("lines", 171, 186)]},
        {"from": 6, "still": "game_rep_log", "marks": [_QL_SEL5]},
        {"from": 7, "still": "game_thanks_ives", "marks": [_C_SPEAKER]},
        {"from": 9, "still": "game_thanks_ives", "marks": [_C_ANS_HL]},
        {"from": 10, "still": "e_plan_rep", "marks": [("lines", 178, 178)]},
        {"from": 11, "still": "e_plan_rep", "marks": [("lines", 184, 184)]},
        {"from": 12, "still": "e_plan_rep", "marks": [("text", 184, "[[vane]]")]},
        {"from": 14, "still": "e_plan_ans", "marks": [("lines", 378, 378)]},
    ]},
    "s07_the_to_do_list": {"step": 5, "beats": [
        {"from": 0, "still": "t_miss3", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_miss3", "marks": [("out", 1, 1)]},
        {"from": 2, "still": "t_miss3", "marks": [("out", 1, 2), ("out", 1, 4), ("out", 1, 6)]},
        {"from": 3, "still": "t_miss3", "marks": [("out", 1, 3), ("out", 1, 5), ("out", 1, 7)]},
        {"from": 4, "still": "t_miss3"},
        {"from": 6, "still": "v_missing"},
    ]},
    "s08_write_them_and_cut_one": {"step": 6, "beats": [
        {"from": 0, "still": "t_miss3", "marks": [("out", 1, 2), ("out", 1, 4), ("out", 1, 6)]},
        {"from": 2, "still": "game_claim_log", "marks": [_QL_SEL5]},
        {"from": 3, "still": "game_claim_log", "marks": [_CLAIM_PAGE]},
        {"from": 4, "still": "e_claim", "marks": [("lines", 188, 206)]},
        {"from": 5, "still": "t_miss2", "marks": [("out", 1, 1)]},
        {"from": 6, "still": "e_vane", "marks": [("lines", 339, 343)]},
        {"from": 7, "still": "game_vane_log", "marks": [_QL_SEL5]},
        {"from": 8, "still": "game_vane_log", "marks": [_QL_VANE]},
        {"from": 9, "still": "t_miss1", "marks": [("out", 1, 1)]},
        {"from": 10, "still": "game_rivals_comms", "marks": [_C_SPEAKER]},
        {"from": 11, "still": "e_rivals", "marks": [("lines", 406, 413)]},
        {"from": 12, "still": "t_none_end", "marks": [("out", 1, 1)]},
        {"from": 13, "still": "e_hist", "marks": [("lines", 368, 376)]},
        {"from": 15, "still": "e_cut", "marks": [("lines", 368, 368)]},
        {"from": 16, "still": "e_cut", "marks": [("lines", 378, 378)]},
        {"from": 17, "still": "e_cut", "marks": [("lines", 368, 378)]},
        {"from": 18, "still": "t_cut", "marks": [("part", "run1:cmd")]},
        {"from": 19, "still": "t_cut", "marks": [("out", 1, 2), ("out", 1, 3)]},
        {"from": 20, "still": "game_hello_comms", "marks": [_C_ANS2]},
        {"from": 24, "still": "t_cut", "marks": [("out", 1, 3)]},
    ]},
    "s09_print_it_four_ways": {"step": 8, "beats": [
        {"from": 0, "still": "t_docs", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_docs", "marks": [("out", 1, 1), ("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 2, "still": "w_prose"},
        {"from": 3, "still": "w_screenplay"},
        {"from": 9, "still": "w_catalog"},
        {"from": 10, "still": "w_bible"},
    ]},
    "s10_play_act_two": {"step": 10, "beats": [
        {"from": 0, "still": "game_vane_log", "marks": [_QL_SEL5]},
        {"from": 2, "still": "game_vane_log", "marks": [_QL_VNAME]},
        {"from": 3, "still": "game_thanks_two", "marks": [_C_ANS2]},
        {"from": 4, "still": "game_rivals_comms", "marks": [_C_SPEAKER]},
        {"from": 5, "still": "game_rivals_comms", "marks": [_C_ANS_HL]},
        {"from": 6, "still": "game_claim_log", "marks": [_QL_SEL5]},
        {"from": 7, "still": "game_claim_log", "marks": [_CLAIM_TABLE]},
        {"from": 8, "still": "game_claim_done", "marks": [_QL_STATE]},
        {"from": 9, "still": "game_fc_log", "marks": [_QL_DESC]},
        {"from": 11, "still": "card_next"},
    ]},
}
