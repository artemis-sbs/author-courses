"""Storyboard for c1-06-lint-is-your-editor: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in c1-05's storyboard.py; this
lecture also uses what was added to the shared code for it:

  ("vscode", state, line, size, {"side": False})   the Side Bar hidden, sizes "mid" and "big"
  ("vscode", ..., {"file": "mast.runtime.log", "wrap": True})   another file of the folder
  ("card", "page", {...}) and ("card", "points", {...})   a sheet of prose; a list of the script's own words
  on a Command Prompt still:  ("span", run, "words")  those words in that run's output, across a wrap
                              ("out", run, n)         the run's nth line of output that is not blank
  a beat with "move": False keeps its picture from pushing in.

THE FILE THIS LECTURE IS SHOWN ON. The script's "Before recording" table asks for the
untouched template (Lecture 4's finished folder; the file is the same as this lecture's own
example\\mission.amd), and every line number and every count the voice says was measured on
it. So that is what is on screen. The student who followed Lecture 5 has one more record at
the end of the file, and for the one-hash half of break 5 the real tool then prints SIX
findings, not three: the still "t_b5b_chain" is that screen, made and not used. See the
report of 2026-10-05.
"""
LECTURE = "c1-06-lint-is-your-editor"
TITLE = ("Class 1, Lecture 6", "Lint is your editor", "Change, save, lint, read the first line")
MISSION = "MyMission"
FILE = "mission.amd"
LOG = "mast.runtime.log"

_PLAIN = "Fly out and locate the drifting hulk."
_CURLY = "Fly out and locate the “ghost ship”. It isn’t answering."
_RETYPED = "Fly out and locate the \"ghost ship\". It isn't answering."
_HULL = "### [Derelict Hull](derelict_scan)"
_NOTE = "# remember to make this scarier"
# What the game wrote in mast.runtime.log when it was played with four hashes on Derelict Hull.
# Read from the real game on 2026-10-05 (game.py ... log); it is the line on the page.
_LOGGED = ("AMD error: line 47: `#### [Derelict Hull](derelict_scan)` has 4 hashes, and a heading here can have "
           "at most 3. It is read as if it had 3. Take the extra off, or put back the heading above it\n")

STATES = {
    "start": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "same_as": "c1-06-lint-is-your-editor/example/mission.amd"},
    "b1": {"base": "start", "edits": [
        ("replace", FILE, "Done when: signal derelict_found", "Done wen: signal derelict_found")]},
    "b2": {"base": "start", "edits": [("replace", FILE, _PLAIN, _CURLY)]},
    "b2_retyped": {"base": "start", "edits": [("replace", FILE, _PLAIN, _RETYPED)]},
    "b3": {"base": "start", "edits": [("replace", FILE, "](study)", "](examine)")]},
    "b4": {"base": "start", "edits": [("replace", FILE, "Tab: scan\n---\n", "Tab: scan\n")]},
    "b5a": {"base": "start", "edits": [("replace", FILE, "\n" + _HULL, "\n#" + _HULL)]},
    "b5b": {"base": "start", "edits": [("replace", FILE, "\n" + _HULL, "\n" + _HULL[2:])]},
    "note": {"base": "start", "edits": [("replace", FILE, _PLAIN + "\n", _PLAIN + "\n" + _NOTE + "\n")]},
    # scene 10: the folder after a play. The game writes both logs; an untroubled play leaves them empty.
    "played4": {"base": "b5a", "edits": [("write", "mast.compile.log", ""), ("write", LOG, _LOGGED)]},
    "mended": {"base": "start", "edits": [("write", "mast.compile.log", ""), ("write", LOG, _LOGGED)]},
    "played_ok": {"base": "start", "edits": [("write", "mast.compile.log", ""), ("write", LOG, "")]},
    # NOT what the script records on: Lecture 5's finished file, with the one-hash break.
    "chain": {"folder": "c1-04-markdown-in-twenty-minutes/example", "skip": ("step-11-only",),
              "over": ("c1-05-the-shape-of-a-record/example",)},
    "chain_b5b": {"base": "chain", "edits": [("replace", FILE, "\n" + _HULL, "\n" + _HULL[2:])]},
}

_LINT = "sbs lint MyMission"
_MISSING = "sbs lint MyMission --missing"
_NS = {"side": False}

STILLS = {
    # the file, Side Bar hidden
    "e_top": ("vscode", "start", 1, "big", _NS),          # lines 1 to 21: the notes that start with //
    "e_find": ("vscode", "start", 28, "big", _NS),        # lines 18 to 38
    "e_b1": ("vscode", "b1", 28, "big", _NS),
    "e_b2": ("vscode", "b2", 31, "big", _NS),
    "e_b2_retyped": ("vscode", "b2_retyped", 31, "big", _NS),
    "e_study": ("vscode", "start", 33, "big", _NS),       # lines 23 to 43
    "e_b3": ("vscode", "b3", 33, "big", _NS),
    "e_hull": ("vscode", "start", 51, "big", _NS),        # lines 41 to 61
    "e_b4": ("vscode", "b4", 50, "big", _NS),
    "e_b5a": ("vscode", "b5a", 47, "big", _NS),           # lines 37 to 57
    "e_b5b": ("vscode", "b5b", 47, "big", _NS),
    "e_hull47": ("vscode", "start", 47, "big", _NS),
    "e_note": ("vscode", "note", 32, "big", _NS),
    # the logs, with the file list: the scene is about which files are in the folder
    "e_log": ("vscode", "played4", 1, "close", {"file": LOG, "wrap": True}),
    "e_log_stale": ("vscode", "mended", 1, "close", {"file": LOG, "wrap": True}),
    "e_log_empty": ("vscode", "played_ok", 1, "close", {"file": LOG}),
    # the Command Prompt: every one is the real tool's answer for that state
    "t_clean": ("terminal", [("start", _LINT)]),
    "t_b1": ("terminal", [("b1", _LINT)]),
    "t_b1_fix": ("terminal", [("b1", _LINT), ("start", _LINT)]),
    "t_b2": ("terminal", [("b2", _LINT)]),
    "t_b2_fix": ("terminal", [("b2", _LINT), ("b2_retyped", _LINT)]),
    "t_b3": ("terminal", [("b3", _LINT)]),
    "t_b3_missing": ("terminal", [("b3", _LINT), ("b3", _MISSING)]),
    "t_b3_fix": ("terminal", [("b3", _MISSING), ("start", _LINT)]),
    "t_b4": ("terminal", [("b4", _LINT)]),
    "t_b4_fix": ("terminal", [("b4", _LINT), ("start", _LINT)]),
    "t_b5a": ("terminal", [("b5a", _LINT)]),
    "t_b5a_fix": ("terminal", [("b5a", _LINT), ("start", _LINT)]),
    "t_b5b": ("terminal", [("b5b", _LINT)]),
    "t_b5b_fix": ("terminal", [("b5b", _LINT), ("start", _LINT)]),
    "t_note": ("terminal", [("note", _LINT)]),
    "t_b5b_chain": ("terminal", [("chain_b5b", _LINT)]),   # made, not used: see the docstring
    # the real game
    "game_epadd": ("game", "Helm with the handheld open; four hashes on Derelict Hull"),
    "game_quests": ("game", "The Quest Log, First Contact selected; four hashes on Derelict Hull"),
    "game_note": ("game", "The Quest Log, Find the Derelict selected; the # note under its description"),
    "game_quests_ok": ("game", "The Quest Log after the fix, First Contact selected"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_manuscript": ("card", "page", {
        "kicker": "An editor reads. She marks. You fix.",
        "text": ["The hulk had been drifting for a very long time when we found her. Nobody "
                 "aboard answered, and and nobody on the station would say whose she was."],
        "strike": ["very ", "and and"], "notes": [("very ", "cut"), ("and and", "twice")]}),
    "card_habit": ("card", "points", {"kicker": "The habit", "items": [
        "Change something.", "Save.", "Run lint.", "Read the first line it prints."]}),
    "card_wp": ("card", "page", {
        "kicker": "A word processor",
        "text": [_CURLY], "find": ["“", "”", "’"],
        "caption": "It turned the quote marks curly as they were typed."}),
    "card_notmean": ("card", "table", {"heading": "What `clean` does not mean", "kicker": "Lint says clean, and"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 7", "sub": "Roles and signals"}),
}

# The finding of break 1, in pieces (they are found in the real output; a wrong word stops the run).
_B1_IS = "`Done wen` is not a field a quest has"
_B1_DOES = "so nothing reads this line"
_B1_WRITE = "Did you mean `Done when`?"
_B1_SENTENCE = _B1_IS + ", " + _B1_DOES + ". " + _B1_WRITE
_DRAWS = "The game cannot draw it and shows `\"` in its place"
_B4_READ = "The lines under its fields are read as fields, so `### [Derelict Hull](derelict_scan)` has no text"
_B5A_COUNT = "has 4 hashes and the heading it sits under has 2: 1 too many"
_B5A_GUESS = "The game reads it as if it had 3"
_B5A_ALL = "`#### [Derelict Hull](derelict_scan)` " + _B5A_COUNT + ". " + _B5A_GUESS + ", which may not be the record you meant it to be"
_ICON = ("rect", 0.203, 0.0, 0.232, 0.046)             # the handheld icon, on a console
_QUESTS_TILE = ("rect", 0.0, 0.395, 0.32, 0.56)
_FC_ROW = ("rect", 0.003, 0.146, 0.38, 0.214)
_TEXT_PANE = ("rect", 0.383, 0.074, 0.98, 0.20)
# on the stills of a log, with the file list (a wrapped line cannot be marked by its words)
_LOGS = ("rect", 0.035, 0.157, 0.222, 0.209)           # the two logs in the file list
_LOG_LINE = ("rect", 0.258, 0.074, 0.972, 0.182)       # the one line the game wrote, as wrapped

# Re-fitted on 2026-10-05 to the narration written for the ear (154 pieces, where there were
# 99 sentences). Same stills and marks; each beat now starts on the piece that says it.
BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "t_b1", "marks": [("out", 1, 2)], "dim": True},
        {"from": 1, "still": "t_b1", "marks": [("out", 1, 1)]},
        {"from": 1.5, "still": "t_b1", "marks": [("span", 1, "line 28:1")]},
        {"from": 2, "still": "t_b1", "marks": [("span", 1, _B1_IS)]},
        {"from": 2.4, "still": "t_b1", "marks": [("span", 1, _B1_DOES)]},
        {"from": 3, "still": "card_title"},
    ]},
    "s02_what_lint_is": {"step": None, "beats": [
        # added: what "lists whatever looks wrong" looks like, before the comparison
        {"from": 0, "still": "t_b1", "marks": [("out", 1, 2)]},
        {"from": 2, "still": "card_manuscript"},
        {"from": 5, "still": "card_habit"},
        {"from": 6, "still": "card_habit", "marks": [("part", "item1")]},
        {"from": 6.55, "still": "card_habit", "marks": [("part", "item2")]},
        {"from": 7, "still": "card_habit", "marks": [("part", "item3")]},
        {"from": 8, "still": "card_habit", "marks": [("part", "item4")]},
    ]},
    "s03_a_file_with_nothing_wrong": {"step": 1, "beats": [
        {"from": 0, "still": "t_clean", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_clean", "marks": [("out", 1, 1)]},
        {"from": 1.5, "still": "t_clean", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "t_clean", "marks": [("part", "run1:last")]},
        {"from": 2.45, "still": "t_clean", "marks": [("span", 1, "1 amd")]},
        {"from": 2.72, "still": "t_clean", "marks": [("span", 1, "1 mast file(s)")]},
        {"from": 3, "still": "t_clean", "marks": [("span", 1, "0 error(s)")]},
        {"from": 3.5, "still": "t_clean", "marks": [("span", 1, "0 warning(s)")]},
        {"from": 4, "still": "t_clean", "marks": [("part", "run1:last")]},
    ]},
    "s04_break_1_a_field_name": {"step": 2, "beats": [
        {"from": 0, "still": "e_b1", "marks": [("text", 28, "Done wen")]},
        {"from": 1, "still": "t_b1", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "t_b1", "marks": [("out", 1, 2)]},
        {"from": 3, "still": "t_b1", "marks": [("span", 1, "[WARNING]"), ("span", 1, "line 28:1"),
                                                ("span", 1, _B1_SENTENCE), ("span", 1, "(unknown-field)")]},
        {"from": 4, "still": "t_b1", "marks": [("span", 1, "[WARNING]")]},
        {"from": 5, "still": "t_b1", "marks": [("span", 1, "line 28:1")]},
        {"from": 7, "still": "t_b1", "marks": [("span", 1, _B1_SENTENCE)]},
        {"from": 8, "still": "t_b1", "marks": [("span", 1, "(unknown-field)")]},
        {"from": 10, "still": "e_b1", "marks": [("lines", 28, 28)]},
        {"from": 11, "still": "t_b1", "marks": [("span", 1, _B1_SENTENCE)]},
        {"from": 12, "still": "t_b1", "marks": [("span", 1, _B1_IS)]},
        {"from": 13, "still": "t_b1", "marks": [("span", 1, _B1_DOES)]},
        {"from": 14, "still": "t_b1", "marks": [("span", 1, _B1_WRITE)]},
        {"from": 15, "still": "e_find", "marks": [("text", 28, "Done when")]},
        {"from": 16, "still": "t_b1_fix", "marks": [("part", "run2:clean")]},
        {"from": 17, "still": "t_b1", "marks": [("span", 1, "[WARNING]")]},
        {"from": 19, "still": "e_b1", "marks": [("lines", 24, 31)], "dim": True},
        {"from": 21, "still": "e_b1", "marks": [("lines", 28, 28), ("lines", 29, 29)]},
    ]},
    "s05_break_2_words_from_a_word_pr": {"step": 3, "beats": [
        {"from": 0, "still": "card_wp"},
        {"from": 2, "still": "card_wp", "marks": [("part", "find1"), ("part", "find2"), ("part", "find3")]},
        {"from": 3, "still": "t_b2", "marks": [("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 5, "still": "t_b2", "marks": [("span", 1, "line 31:24"), ("span", 1, "line 31:35"), ("span", 1, "line 31:44")]},
        {"from": 6, "still": "e_b2", "marks": [("text", 31, "“"), ("text", 31, "”"), ("text", 31, "’")]},
        {"from": 7, "still": "t_b2", "marks": [("span", 1, _DRAWS)]},
        {"from": 10, "still": "e_b2", "marks": [("lines", 31, 31)]},
        {"from": 11, "still": "t_b2", "marks": [("span", 1, "[WARNING]"), ("span", 1, "[WARNING]", 2), ("span", 1, "[WARNING]", 3)]},
        {"from": 12, "still": "t_b2", "marks": [("span", 1, "(non-ascii)"), ("span", 1, "(non-ascii)", 2), ("span", 1, "(non-ascii)", 3)]},
        {"from": 14, "still": "e_b2_retyped", "marks": [("text", 31, "\""), ("text", 31, "\"", 2), ("text", 31, "'")]},
        {"from": 15, "still": "t_b2_fix", "marks": [("part", "run2:clean")]},
    ]},
    "s06_break_3_a_key_that_no_longer": {"step": 4, "beats": [
        {"from": 0, "still": "e_b3", "marks": [("text", 33, "(examine)")]},
        {"from": 1, "still": "t_b3", "marks": [("span", 1, "line 29:14"), ("span", 1, "line 36")]},
        {"from": 2, "still": "e_b3", "marks": [("lines", 33, 33)]},
        {"from": 4, "still": "e_b3", "marks": [("lines", 29, 29)]},
        {"from": 5, "still": "t_b3", "marks": [("span", 1, "no record has that key, so nothing is revealed")]},
        {"from": 7, "still": "e_b3", "marks": [("lines", 36, 36), ("text", 33, "(examine)")]},
        {"from": 8, "still": "t_b3", "marks": [("span", 1, "waits to be revealed, and nothing reveals it")]},
        {"from": 10, "still": "e_b3", "marks": [("text", 29, "first_contact/study"), ("text", 33, "(examine)")]},
        {"from": 11, "still": "e_b3", "marks": [("lines", 29, 29), ("lines", 36, 36)]},
        {"from": 12, "still": "t_b3"},
        {"from": 13, "still": "t_b3_missing", "marks": [("part", "run2:cmd")], "move": False},
        {"from": 14, "still": "t_b3_missing", "marks": [("out", 2, 2), ("out", 2, 3)], "move": False},
        {"from": 15, "still": "t_b3_missing", "marks": [("out", 2, 1)], "move": False},
        {"from": 16, "still": "e_study", "marks": [("text", 33, "(study)")]},
        {"from": 17, "still": "t_b3_fix", "marks": [("part", "run2:clean")]},
    ]},
    "s07_break_4_a_fence_left_open": {"step": 5, "beats": [
        {"from": 0, "still": "e_hull", "marks": [("lines", 51, 51)]},
        {"from": 1.5, "still": "e_b4", "marks": [("after", 50)]},
        {"from": 2, "still": "t_b4", "marks": [("span", 1, "[ERROR]")]},
        {"from": 3, "still": "e_b4", "marks": [("after", 50)]},
        {"from": 4, "still": "t_b4", "marks": [("span", 1, "line 48")]},
        {"from": 5, "still": "e_b4", "marks": [("lines", 48, 48)]},
        {"from": 7, "still": "t_b4", "marks": [("out", 1, 2)]},
        {"from": 8, "still": "t_b4", "marks": [("span", 1, _B4_READ)]},
        {"from": 9, "still": "e_b4", "marks": [("lines", 49, 52)]},
        {"from": 10, "still": "t_b4", "marks": [("span", 1, "Add a `---` line under its last field")]},
        {"from": 12, "still": "e_hull", "marks": [("lines", 51, 51)]},
        {"from": 12.5, "still": "t_b4_fix", "marks": [("part", "run2:clean")]},
        {"from": 13, "still": "e_b4", "marks": [("lines", 48, 48), ("after", 50)]},
        {"from": 15, "still": "t_b4", "marks": [("out", 1, 2)]},
    ]},
    "s08_break_5_the_number_of_hashes": {"step": 6, "beats": [
        {"from": 0, "still": "e_hull47", "marks": [("hashes", 45), ("hashes", 47), ("hashes", 55)]},
        {"from": 1, "still": "e_b5a", "marks": [("hashes", 47)]},
        {"from": 2, "still": "t_b5a", "marks": [("span", 1, "[ERROR]")]},
        {"from": 3, "still": "e_b5a", "marks": [("hashes", 47)]},
        {"from": 4, "still": "e_b5a", "marks": [("hashes", 47), ("hashes", 45)]},
        {"from": 5, "still": "t_b5a", "marks": [("span", 1, _B5A_GUESS)]},
        {"from": 7, "still": "e_b5a", "marks": [("lines", 47, 53)]},
        {"from": 9, "still": "t_b5a", "marks": [("span", 1, "[ERROR]")]},
        {"from": 11, "still": "t_b5a", "marks": [("span", 1, "[ERROR]"), ("span", 1, _B5A_ALL)]},
        {"from": 12, "still": "t_b5a", "marks": [("span", 1, _B5A_ALL)]},
        {"from": 13, "still": "e_hull47", "marks": [("hashes", 47)]},
        {"from": 13.7, "still": "t_b5a_fix", "marks": [("part", "run2:clean")]},
        {"from": 14, "still": "e_b5b", "marks": [("hashes", 47)]},
        {"from": 15, "still": "t_b5b", "marks": [("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 17, "still": "t_b5b", "marks": [("out", 1, 2)], "dim": True},
        {"from": 19, "still": "t_b5b", "marks": [("span", 1, "line 47")]},
        {"from": 20, "still": "t_b5b", "marks": [("span", 1, "One hash starts a new title")]},
        {"from": 20.62, "still": "t_b5b", "marks": [("span", 1, "Give it 3")]},
        {"from": 21, "still": "t_b5b", "marks": [("span", 1, "line 55:6"), ("span", 1, "line 55:6", 2)]},
        {"from": 22, "still": "e_b5b", "marks": [("lines", 55, 55)]},
        {"from": 23, "still": "t_b5b", "marks": [("span", 1, "give its heading 4 hashes"),
                                                  ("span", 1, "Give it the same number of hashes")]},
        {"from": 24, "still": "e_hull47", "marks": [("hashes", 47)]},
        {"from": 25, "still": "t_b5b_fix", "marks": [("part", "run2:clean")]},
        {"from": 26, "still": "t_b5b_fix", "marks": [("out", 1, 2), ("part", "run2:clean")]},
    ]},
    "s09_what_clean_does_not_mean": {"step": 7, "beats": [
        {"from": 0, "still": "e_find", "marks": [("lines", 31, 31)]},
        {"from": 1, "still": "e_note", "marks": [("lines", 32, 32)]},
        {"from": 2, "still": "e_note", "marks": [("hashes", 32)]},
        {"from": 3, "still": "t_note", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "game_note", "marks": [_TEXT_PANE]},
        {"from": 5, "still": "e_top", "marks": [("text", 1, "//"), ("text", 4, "//"), ("text", 7, "//"), ("text", 13, "//")]},
        {"from": 6, "still": "t_note", "marks": [("part", "run1:clean"), ("part", "run1:last")]},
        {"from": 9, "still": "card_notmean"},
        {"from": 10, "still": "card_notmean", "marks": [("part", "r3")]},
    ]},
    "s10_the_second_check": {"step": 8, "beats": [
        {"from": 0, "still": "t_clean", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "e_log_empty", "marks": [_LOGS], "move": False},
        {"from": 4, "still": "e_b5a", "marks": [("hashes", 47)]},
        {"from": 4.55, "still": "game_epadd", "marks": [_ICON, _QUESTS_TILE]},
        {"from": 5, "still": "game_quests", "marks": [_FC_ROW]},
        {"from": 7, "still": "e_log", "marks": [_LOG_LINE]},
        {"from": 8, "still": "e_log", "marks": [("rect", 0.345, 0.074, 0.405, 0.111), ("rect", 0.624, 0.110, 0.972, 0.146), ("rect", 0.258, 0.146, 0.328, 0.182)]},
        {"from": 9, "still": "t_b5a", "marks": [("span", 1, "line 47"), ("span", 1, _B5A_GUESS)]},
        {"from": 11, "still": "e_hull47", "marks": [("hashes", 47)]},
        {"from": 11.5, "still": "t_b5a_fix", "marks": [("part", "run2:clean")]},
        {"from": 12, "still": "e_log_stale", "marks": [_LOG_LINE]},
        {"from": 13, "still": "e_log_stale", "marks": [_LOGS]},
        {"from": 15, "still": "game_epadd", "marks": [_QUESTS_TILE]},
        {"from": 15.5, "still": "game_quests_ok", "marks": [_FC_ROW]},
        {"from": 16, "still": "e_log_empty", "marks": [_LOGS], "move": False},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 4, "still": "card_next"},
    ]},
}
