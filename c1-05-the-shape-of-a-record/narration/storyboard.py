"""Storyboard for c1-05-the-shape-of-a-record: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. Scene ids and caption numbers are those of shots.py
(captions count from 0 inside a scene). Written by hand; nothing here is generated.

STATES   the student's mission folder at each moment of the lecture: a starting folder, a
         file to lay over it, then edits. ("replace", file, old, new) must match exactly once;
         ("append", file, text) adds to the end.
STILLS   every picture the lecture needs, and how it is got:
           ("vscode", state, line, size)     real VS Code, the file open with the cursor on
                                             that line; size is "wide" or "close"
           ("terminal", [(state, command)])  the real commands, run in order in the stand-in
                                             install, drawn as a Command Prompt
           ("game", note)                    a screenshot of the real game: game.py makes it
           ("card", kind, {...})             drawn: "title", "table" and "list" take their
                                             words from lesson.md
BOARD    per scene: "step" (the page's numbered step that starts here, or None) and "beats".
         A beat: "from" = the caption it starts on (2.5 = halfway through caption 2), "still",
         and "marks". It lasts until the next beat starts.
Marks on a vscode or terminal still (line numbers are the file's, or the terminal's rows):
           ("lines", a, b)        a box round whole lines a to b
           ("text", line, "s")    a box round those characters on that line (first match;
                                  ("text", line, "s", 2) for the second)
           ("hashes", line)       the hashes that start the line
           ("after", line)        the empty space after the end of the line
         on a card: ("part", "name") - the names a card kind offers are listed in cards.py
         on anything: ("rect", u0, v0, u1, v1) in fractions of the frame
         "dim": True darkens everything outside the marks. "crop": (u0, v0, u1, v1) shows
         that part of the still, enlarged to the frame.
"""
LECTURE = "c1-05-the-shape-of-a-record"
TITLE = ("Class 1, Lecture 5", "The shape of a record", "Heading, fence, body")
MISSION = "MyMission"
FILE = "mission.amd"

_OLD = "A derelict has drifted into the sector. Find out what happened to it."
_NEW = "A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is."
_HEAD = "### [Derelict Intel](derelict_intel)"
_BODY = "% No flight plan was ever filed for this ship. Somebody wanted her forgotten."

STATES = {
    # Lecture 4's finished folder is where Lecture 5 starts.
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example"},
    "reworded": {"base": "start", "edits": [("replace", FILE, _OLD, _NEW)]},
    # the new record, as it is typed
    "w1": {"base": "reworded", "edits": [("append", FILE, "\n### [Derelict Intel]\n")]},
    "w2": {"base": "reworded", "edits": [("append", FILE, "\n" + _HEAD + "\n---\n")]},
    "w3": {"base": "w2", "edits": [("append", FILE, "Scan of: derelict\n")]},
    "w4": {"base": "w3", "edits": [("append", FILE, "Tab: intel\n---\n")]},
    "final": {"base": "w4", "edits": [("append", FILE, _BODY + "\n")],
              "same_as": "c1-05-the-shape-of-a-record/example/mission.amd"},
    # scene 9: three ways to break the shape
    "nospace": {"base": "final", "edits": [("replace", FILE, _HEAD, "###[Derelict Intel](derelict_intel)")]},
    "indent": {"base": "final", "edits": [("replace", FILE, "\nTab: intel\n", "\n    Tab: intel\n")]},
    "hyphens": {"base": "final", "edits": [
        ("replace", FILE, _HEAD + "\n---\n", _HEAD + "\n--\n"),
        ("replace", FILE, "Tab: intel\n---\n", "Tab: intel\n--\n")]},
    # scene 10: the one lint calls clean
    "onehash": {"base": "final", "edits": [("replace", FILE, _HEAD, "# [Derelict Intel](derelict_intel)")]},
}

_LINT = "sbs lint MyMission"

STILLS = {
    "ed_top": ("vscode", "start", 1, "wide"),
    "ed_a": ("vscode", "start", 28, "wide"),            # lines 10 to 46: six of the headings
    "ed_b": ("vscode", "start", 44, "wide"),            # lines 26 to 60: the other end
    "ed_head": ("vscode", "start", 16, "close"),
    "ed_find": ("vscode", "start", 27, "close"),
    "ed_fc": ("vscode", "start", 19, "close"),
    "ed_hull": ("vscode", "start", 50, "close"),
    "ed_fc_new": ("vscode", "reworded", 19, "close"),
    "ed_end": ("vscode", "reworded", 61, "close"),
    "ed_w1": ("vscode", "w1", 62, "close"),
    "ed_w2": ("vscode", "w2", 63, "close"),
    "ed_w3": ("vscode", "w3", 64, "close"),
    "ed_w4": ("vscode", "w4", 66, "close"),
    "ed_final": ("vscode", "final", 67, "close"),
    "ed_final_wide": ("vscode", "final", 50, "wide"),
    "ed_final_a": ("vscode", "final", 28, "wide"),
    "ed_nospace": ("vscode", "nospace", 62, "close"),
    "ed_indent": ("vscode", "indent", 65, "close"),
    "ed_hyphens": ("vscode", "hyphens", 63, "close"),
    "ed_onehash": ("vscode", "onehash", 62, "close"),
    "term1": ("terminal", [("final", _LINT)]),
    "term2": ("terminal", [("final", _LINT), ("onehash", _LINT)]),
    "term3": ("terminal", [("final", _LINT), ("onehash", _LINT), ("final", _LINT)]),
    "game_epadd": ("game", "Helm with the handheld open"),
    "game_quests": ("game", "The Quest Log, First Contact selected"),
    "game_science": ("game", "Science, the hulk selected"),
    "game_intel": ("game", "Science, the hulk's intel tab"),
    "card_title": ("card", "title", {}),
    "card_shows": ("card", "table", {"heading": "Step 4 - What shows, and where"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 6", "sub": "Lint is your editor"}),
}

_REC = [("lines", 62, 67)]
_SENTENCE = ("rect", 0.695, 0.388, 0.998, 0.448)       # the reading, on the Science console
_PARTS = [("lines", 62, 62), ("lines", 63, 66), ("lines", 67, 67)]

# Re-fitted on 2026-10-05 to the narration written for the ear (114 pieces, where there were
# 80 sentences). The pieces are clauses now, so nearly every beat starts on a whole piece
# and none is placed by a guessed fraction of a sentence.
_THREE = [("lines", 16, 22), ("lines", 24, 32), ("lines", 33, 39)]
_HASHES_A = [("hashes", n) for n in (10, 14, 16, 24, 33, 45)]

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_intel", "marks": [_SENTENCE], "dim": True},
        {"from": 1, "still": "ed_final", "marks": _REC, "dim": True},
        {"from": 3, "still": "ed_final_a", "marks": _THREE},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_the_file": {"step": 1, "beats": [
        {"from": 0, "still": "ed_top"},
        {"from": 1, "still": "ed_top", "marks": [("lines", 1, 8)]},
        {"from": 3, "still": "ed_a", "marks": _THREE},
        {"from": 5, "still": "ed_b", "marks": [("lines", 47, 53), ("lines", 55, 60)]},
        {"from": 6, "still": "ed_final_wide", "marks": [("lines", 62, 67)]},
    ]},
    "s03_eight_headings": {"step": None, "beats": [
        {"from": 0, "still": "ed_a", "marks": _HASHES_A},
        {"from": 1, "still": "ed_b", "marks": [("hashes", n) for n in (33, 45, 47, 55)]},
        {"from": 2, "still": "ed_head", "marks": [("lines", 16, 16)]},
        {"from": 4, "still": "ed_head", "marks": [("hashes", 16)]},
        {"from": 5, "still": "ed_head", "marks": [("text", 16, "[First Contact]")]},
        {"from": 6, "still": "ed_head", "marks": [("text", 16, "(first_contact)")]},
        {"from": 7, "still": "ed_head", "marks": [("text", 16, "[First Contact](first_contact)")]},
        {"from": 8, "still": "ed_a", "marks": _HASHES_A},
        {"from": 9, "still": "ed_a", "marks": [("lines", 10, 10)]},
        {"from": 10, "still": "ed_a", "marks": [("lines", 14, 14), ("lines", 45, 45)]},
        {"from": 12, "still": "ed_a", "marks": [("lines", 16, 16)]},
        {"from": 13, "still": "ed_a", "marks": [("lines", 24, 24), ("lines", 33, 33)]},
        {"from": 14, "still": "ed_a", "marks": [("lines", 16, 16), ("lines", 24, 32), ("lines", 33, 39)]},
    ]},
    "s04_one_record_three_parts": {"step": 2, "beats": [
        {"from": 0, "still": "ed_find", "marks": [("lines", 24, 32)], "dim": True},
        {"from": 1, "still": "ed_find", "marks": [("lines", 24, 24)]},
        {"from": 2, "still": "ed_find", "marks": [("lines", 25, 31)]},
        {"from": 4, "still": "ed_find", "marks": [("lines", 26, 29)]},
        {"from": 5, "still": "ed_find",
         "marks": [("text", 26, "Scope"), ("text", 26, ":"), ("text", 26, "shared")]},
        {"from": 6, "still": "ed_find", "marks": [("lines", 26, 29)]},
        {"from": 7, "still": "ed_find", "marks": [("lines", 32, 32)]},
        # "So that's heading, | fence, | body." is three very short pieces: one picture.
        {"from": 9, "still": "ed_find", "marks": [("lines", 24, 24), ("lines", 25, 31), ("lines", 32, 32)]},
        {"from": 12, "still": "ed_find", "marks": [("lines", 26, 29)]},
        {"from": 13, "still": "ed_find", "marks": [("lines", 29, 29)]},
        {"from": 14, "still": "ed_find",
         "marks": [("text", 29, "first_contact/study"), ("text", 16, "(first_contact)"),
                   ("text", 33, "(study)")]},
    ]},
    "s05_two_more": {"step": 3, "beats": [
        {"from": 0, "still": "ed_fc", "marks": [("lines", 16, 16), ("lines", 17, 21), ("lines", 22, 22)]},
        {"from": 1, "still": "ed_fc", "marks": [("lines", 18, 18)]},
        {"from": 2, "still": "ed_fc", "marks": [("lines", 17, 17), ("text", 18, "Arc")]},
        {"from": 3, "still": "ed_hull", "marks": [("lines", 47, 47), ("lines", 48, 51), ("lines", 52, 53)]},
        {"from": 4, "still": "ed_hull", "marks": [("text", 52, "%"), ("text", 53, "%")]},
        {"from": 5, "still": "ed_hull", "marks": [("lines", 52, 52), ("lines", 53, 53)]},
        # added: the one reading Science was shown, on the real console
        {"from": 6, "still": "game_science", "marks": [_SENTENCE]},
    ]},
    "s06_what_shows_where": {"step": 4, "beats": [
        {"from": 0, "still": "card_shows", "marks": [("part", "r1c2")]},
        {"from": 1, "still": "card_shows", "marks": [("part", "r3c2")]},
        {"from": 2, "still": "card_shows", "marks": [("part", "r1c3")]},
        {"from": 4, "still": "card_shows", "marks": [("part", "r3c3")]},
        {"from": 5, "still": "card_shows", "marks": [("part", "r2")]},
    ]},
    "s07_change_the_words": {"step": 5, "beats": [
        {"from": 0, "still": "ed_fc", "marks": [("lines", 22, 22)]},
        {"from": 1, "still": "ed_fc_new", "marks": [("lines", 22, 22)]},
        {"from": 3, "still": "ed_fc_new", "marks": [("lines", 16, 16), ("lines", 17, 21)]},
    ]},
    "s08_write_a_record": {"step": 6, "beats": [
        {"from": 0, "still": "ed_end"},
        {"from": 1, "still": "ed_w1", "marks": [("hashes", 62)]},
        {"from": 2, "still": "ed_w1", "marks": [("text", 62, "[Derelict Intel]")]},
        {"from": 3, "still": "ed_w2", "marks": [("text", 62, "(derelict_intel)")]},
        {"from": 4, "still": "ed_w2", "marks": [("lines", 63, 63)]},
        {"from": 5, "still": "ed_w3", "marks": [("lines", 64, 64)]},
        {"from": 6, "still": "ed_w4", "marks": [("lines", 65, 65)]},
        {"from": 7, "still": "ed_w4", "marks": [("lines", 66, 66)]},
        {"from": 8, "still": "ed_final", "marks": [("text", 67, "%"), ("lines", 67, 67)]},
        {"from": 9, "still": "ed_final", "marks": _REC},
        {"from": 10, "still": "ed_final"},
        {"from": 11, "still": "ed_final", "marks": [("hashes", 62)]},
        {"from": 12, "still": "ed_final", "marks": [("after", 62)]},
        {"from": 13, "still": "ed_final", "marks": [("text", 64, "Scan of:"), ("text", 65, "Tab:")]},
    ]},
    "s09_three_ways_to_break_the_shap": {"step": None, "beats": [
        {"from": 0, "still": "ed_final", "marks": _REC},
        {"from": 1, "still": "ed_nospace", "marks": [("text", 62, "###[")]},
        {"from": 3, "still": "ed_nospace", "marks": [("lines", 62, 67)]},
        {"from": 4, "still": "ed_indent", "marks": [("text", 65, "    Tab:")]},
        {"from": 7, "still": "ed_hyphens", "marks": [("lines", 63, 63), ("lines", 66, 66)]},
        {"from": 9, "still": "ed_final", "marks": _REC, "dim": True},
        {"from": 11, "still": "ed_final", "marks": _PARTS},
    ]},
    "s10_check_it": {"step": 7, "beats": [
        {"from": 0, "still": "ed_final_wide"},
        {"from": 1, "still": "term1"},
        {"from": 2, "still": "term1", "marks": [("part", "run1:clean")]},
        {"from": 3, "still": "term1", "marks": [("part", "run1:last")]},
        {"from": 5, "still": "ed_final", "marks": [("hashes", 62)]},
        {"from": 6, "still": "ed_onehash", "marks": [("hashes", 62)]},
        {"from": 7, "still": "term2", "marks": [("part", "run2:clean")]},
        {"from": 8, "still": "ed_onehash", "marks": [("lines", 62, 62)]},
        {"from": 10, "still": "term3", "marks": [("part", "run1:clean"), ("part", "run2:clean"), ("part", "run3:clean")]},
        {"from": 11, "still": "ed_final", "marks": [("hashes", 62)]},
    ]},
    "s11_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_epadd", "marks": [("rect", 0.203, 0.0, 0.232, 0.046), ("rect", 0.0, 0.395, 0.32, 0.56)]},
        {"from": 1, "still": "game_quests", "marks": [("rect", 0.003, 0.146, 0.38, 0.214)]},
        {"from": 2, "still": "game_quests", "marks": [("rect", 0.383, 0.074, 0.98, 0.14)]},
        {"from": 3, "still": "game_science", "marks": [("rect", 0.697, 0.648, 0.93, 0.692)]},
        {"from": 5, "still": "game_science", "marks": [("rect", 0.697, 0.05, 0.937, 0.093)]},
        {"from": 6, "still": "game_intel", "marks": [("rect", 0.778, 0.05, 0.86, 0.093), _SENTENCE]},
    ]},
    "s12_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 3, "still": "card_next"},
    ]},
}
