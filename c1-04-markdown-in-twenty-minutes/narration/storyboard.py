"""Storyboard for c1-04-markdown-in-twenty-minutes: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6, and the new kinds of still in _tools/picture/README.md. Caption numbers are those
of the narration REWRITTEN FOR THE EAR (2026-10-06).

The story bible is built up line by line (states b0 to b7); the last state must equal the
page's example\\story-bible.md byte for byte. Every still of it is ONE real VS Code window:
the file as text on the left, VS Code's own markdown preview on the right, opened by VS
Code's command "Open Preview to the Side" (run by the helper add-on of the throwaway
profile; no key is pressed). Word wrap is on, as it is for a .md file.

The twelve lines of Step 11 are the page's example\\step-11-only\\mission.amd (state m12),
and the game stills are that file in the real game (game.py, no probe change). Reworked
2026-10-14 (later): a description is a page, and the Quest Log joins a paragraph's lines
as the preview does; the Quest Log still is new (game_log_p2), taken 2026-10-14. The one
Science still (2026-10-14 rework, NEW console, _sci2) is the page's example, not state m9.

Cards: the word processor (prose on a sheet), the menu and the keys, and tables in the
page's own words.
"""
LECTURE = "c1-04-markdown-in-twenty-minutes"
TITLE = ("Class 1, Lecture 4", "Markdown in twenty minutes", "Six marks, one page, and what the game does with them")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"
BIBLE = "story-bible.md"

_P1 = "A dead ship has drifted across the border. Nobody sent her, and nobody will say whose she is."
_P2 = "The crew has one watch to find out what happened aboard, before somebody else comes to claim her."
_LINK = (" The idea comes from [the Mary Celeste](https://en.wikipedia.org/wiki/Mary_Celeste), a ship found "
         "sailing with nobody aboard.")
_HEADS = "# Nobody Aboard\n\n## Premise\n\n## People\n\n## What happens\n"
_PEOPLE = ("- Captain Mara Vell, who gives the order and hates it\n- Chief Osei, who has seen a hull like this one "
           "before\n- The Voice, still talking on the hulk's radio\n")
_STEPS = "1. The crew finds the hulk.\n2. Science takes a full scan of the hull.\n3. Not written yet: somebody answers.\n"
_CURLY = "“She’s still out there,” he said — and then… nothing."
_TWELVE = ("## Orders\nFly out and locate the **drifting** hulk.\nShe went dark three days ago, past the border.\n\n"
           "- Find her.\n- Scan her.\n\n| Last heard | Her words |\n|---|---|\n| Three days ago | Stay. |\n\n"
           "Read [the old report](https://example.com/report) first.\n")

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example"},
    "b0": {"base": "start", "edits": [("write", BIBLE, "# Nobody Aboard\n")]},
    "b1": {"base": "start", "edits": [("write", BIBLE, _HEADS)]},
    "b1x": {"base": "b1", "edits": [("replace", BIBLE, "## Premise", "##Premise")]},
    "b2": {"base": "b1", "edits": [("replace", BIBLE, "# Nobody Aboard\n", "# Nobody Aboard\n\n" + _P1 + "\n"),
                                   ("replace", BIBLE, "## Premise\n", "## Premise\n\n" + _P2 + "\n")]},
    "b2e": {"base": "b2", "edits": [("replace", BIBLE, "border. Nobody sent her", "border.\nNobody sent her")]},
    "b2t": {"base": "b2", "edits": [("replace", BIBLE, "\nA dead ship", "\n\tA dead ship")]},
    "b3": {"base": "b2", "edits": [("replace", BIBLE, "## People\n", "## People\n\n" + _PEOPLE)]},
    "b4": {"base": "b3", "edits": [("replace", BIBLE, "## What happens\n", "## What happens\n\n" + _STEPS)]},
    "b5": {"base": "b4", "edits": [("replace", BIBLE, "claim her.\n", "claim her." + _LINK + "\n")]},
    "b6": {"base": "b5", "edits": [("replace", BIBLE, "with nobody aboard", "with **nobody** aboard")]},
    "b7": {"base": "b6", "edits": [("replace", BIBLE, "3. Not written yet:", "3. *Not written yet:*")],
           "same_as": ("c1-04-markdown-in-twenty-minutes/example/story-bible.md",
                       "c1-04-markdown-in-twenty-minutes/example/mission.amd")},
    # Step 8: a sentence brought over from a word processor, pasted under the first paragraph
    "bw": {"base": "b7", "edits": [("replace", BIBLE, _P1 + "\n", _P1 + "\n\n" + _CURLY + "\n")]},
    # Step 11: the twelve lines, in place of line 31
    "m12": {"base": "b7", "edits": [("replace", FILE, "Fly out and locate the drifting hulk.\n", _TWELVE)],
           "same_as": "c1-04-markdown-in-twenty-minutes/example/step-11-only/mission.amd"},
}

_B = {"file": BIBLE, "side": False, "wrap": True, "beside": "preview"}
_NS = {"side": False}

STILLS = {
    "v_files": ("vscode", "start", 10, "wide"),
    "b0n": ("vscode", "b0", 1, "mid", {"file": BIBLE, "side": False, "wrap": True}),
    "b0": ("vscode", "b0", 1, "mid", _B),
    "b1": ("vscode", "b1", 3, "mid", _B),
    "b1x": ("vscode", "b1x", 3, "mid", _B),
    "b2": ("vscode", "b2", 3, "mid", _B),
    "b2e": ("vscode", "b2e", 4, "mid", _B),
    "b2t": ("vscode", "b2t", 3, "mid", _B),
    "b3": ("vscode", "b3", 11, "mid", _B),
    "b4": ("vscode", "b4", 17, "mid", _B),
    "b5": ("vscode", "b5", 7, "mid", _B),
    "b6": ("vscode", "b6", 7, "mid", _B),
    "b7": ("vscode", "b7", 19, "mid", _B),
    "b_final": ("vscode", "b7", 1, "mid", _B),
    "bw": ("vscode", "bw", 5, "mid", _B),
    "m47": ("vscode", "b7", 47, "big", _NS),               # lines 37 to 57: a note, a heading, a fence, readings
    "m31": ("vscode", "b7", 31, "big", _NS),
    "m12": ("vscode", "m12", 36, "big", _NS),             # lines 26 to 46
    # the real game (game.py --state m12), nothing changed for the probe
    "game_helm": ("game", "Helm as it comes up"),
    "game_padd": ("game", "Helm: the handheld"),
    # NEW 2026-10-14 (later), taken 2026-10-14: the twelve lines, on the library whose text areas join paragraphs
    "game_log_p2": ("game", "helm, the Quest Log, state m12, Find the Derelict selected: the pane shows State/Active, then the heading Orders, ONE paragraph (the two typed lines joined, stars shown round drifting), a gap, the two-item list, a gap, the small table Last heard / Her words, a gap, the link line as typed"),
    # REWORK 2026-10-14, taken 2026-10-14: the NEW Science console, on the page's example (state b7)
    "game_sci_hull_sci2": ("game", "the science window, NEW console, the page's example (no probe change): the hulk selected and scanned, its tab stack over the map with Scan chosen, the read-out showing one of the two Derelict Hull readings"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_wp": ("card", "page", {"kicker": "In a word processor, a heading is a style you choose",
                                 "text": ["Nobody Aboard", _P1], "find": ["Nobody Aboard"],
                                 "notes": [("Nobody Aboard", "Heading 1")],
                                 "caption": "The file remembers the style in a way only the word processor can read."}),
    "card_marks": ("card", "points", {"kicker": "Six marks", "items": [
        "`#` and `##`: a title and a heading", "A blank line: the end of a paragraph", "`-`: a list",
        "`1.`: a numbered list", "`[words](address)`: a link", "`**bold**` and `*slanted*`"]}),
    "card_new": ("card", "points", {"kicker": "A new file in your mission's folder", "items": [
        "Right-click an empty place under the last file. Choose **New File...**",
        "Type the name and press Enter: `story-bible.md`"]}),
    "card_keys": ("card", "points", {"kicker": "The preview, and save", "items": [
        "Press `Ctrl+K`, let go, then press `V`. The preview opens beside your file.",
        "Press `Ctrl+S` to save."]}),
    "card_curly": ("card", "page", {"kicker": "Typed in a word processor", "text": [_CURLY],
                                    "find": ["“", "’", "”", "—", "…"],
                                    "caption": "It changed the quote marks, the apostrophe, the hyphens and the three dots. It did not ask."}),
    "card_plain": ("card", "table", {"heading": "Step 8 - The plain keyboard", "kicker": "The plain keyboard"}),
    "card_five": ("card", "table", {"heading": "Step 9 - Read `mission.amd` with new eyes",
                                    "kicker": "Five marks that are not markdown's"}),
    "card_reads": ("card", "rows", {"kicker": "In the Quest Log", "header": ("You typed", "The crew reads"), "rows": [
        ("`## Orders`", "`Orders`, as a heading: larger gray letters, and no hashes"),
        ("The two lines under it", "One paragraph, the lines joined. The stars are shown as typed"),
        ("The three blank lines", "A gap, where the paragraph, the list and the table end"),
        ("`- Find her.` and `- Scan her.`", "A list: indented, light blue"),
        ("The three lines that start with a bar", "A small table"),
        ("`Read [the old report](https://example.com/report) first.`", "The same, brackets and address. There is nothing to click")]}),
    "card_rules": ("card", "points", {"kicker": "Three rules for mission.amd", "items": [
        "Write a description as a page: paragraphs, and a heading, a list or a small table where it helps.",
        "Leave stars, backticks and links out. The crew would read the marks.",
        "A Science reading is one line. Every line is a reading of its own."]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn: my-story.md"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 5", "sub": "The shape of a record"}),
}

_SRC, _PRE, _TAB = ("part", "source"), ("part", "preview"), ("part", "preview_tab")
_URL = "(https://en.wikipedia.org/wiki/Mary_Celeste)"
# on the game's windows (fractions of the 4:3 picture); set from the screenshots
_QUESTS = ("rect", 0.07, 0.52, 0.23, 0.64)
_G_ROW = ("rect", 0.025, 0.218, 0.38, 0.285)
# game_log_p2: the pane, State to the link line, and its parts
_G_TEXT = ("rect", 0.385, 0.075, 0.975, 0.443)
_G_HEAD = ("rect", 0.385, 0.128, 0.5, 0.163)
_G_PARA = ("rect", 0.385, 0.163, 0.975, 0.23)
_G_STARS = ("rect", 0.549, 0.163, 0.628, 0.2)          # **drifting**
_G_LIST = ("rect", 0.4, 0.243, 0.49, 0.308)
_G_TABLE = ("rect", 0.385, 0.322, 0.705, 0.392)
_G_LINK = ("rect", 0.385, 0.405, 0.81, 0.44)
# game_sci_hull_sci2: the read-out on the right, the Scan button in the lower left
_G_READ = ("rect", 0.697, 0.245, 0.99, 0.307)
_G_SCAN = ("rect", 0.007, 0.761, 0.286, 0.8)

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "b_final", "marks": [_SRC]},
        {"from": 1, "still": "b_final", "marks": [_PRE]},
        {"from": 2, "still": "b_final", "marks": [("hashes", 1), ("hashes", 5), ("hashes", 9), ("hashes", 15),
                                                  ("text", 7, "**nobody**"), ("text", 19, "*Not written yet:*")]},
        {"from": 4, "still": "m47", "marks": [("lines", 47, 47)]},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_what_markdown_is": {"step": None, "beats": [
        {"from": 0, "still": "card_wp", "marks": [("part", "find1")]},
        {"from": 2, "still": "b0n", "marks": [("hashes", 1)]},
        {"from": 3, "still": "b0", "marks": [_PRE]},
        {"from": 4, "still": "b_final"},
        {"from": 5, "still": "card_marks"},
    ]},
    "s03_make_the_file_open_the_previ": {"step": 1, "beats": [
        {"from": 0, "still": "v_files"},
        {"from": 1, "still": "card_new", "marks": [("part", "item2")]},
        {"from": 2, "still": "b0n", "marks": [("lines", 1, 1)]},
        {"from": 3, "still": "card_keys", "marks": [("part", "item1")]},
        {"from": 4, "still": "b0", "marks": [_PRE]},
        {"from": 5, "still": "b0", "marks": [("hashes", 1), _PRE]},
        {"from": 6, "still": "b0", "marks": [_TAB]},
        {"from": 7, "still": "card_keys", "marks": [("part", "item2")]},
        {"from": 8, "still": "b0"},
    ]},
    "s04_a_title_and_three_headings": {"step": 2, "beats": [
        {"from": 0, "still": "b1", "marks": [("lines", 3, 3), ("lines", 5, 5), ("lines", 7, 7)]},
        {"from": 1, "still": "b1", "marks": [_PRE]},
        {"from": 2, "still": "b1", "marks": [("hashes", 1), ("hashes", 3), ("hashes", 5), ("hashes", 7)]},
        {"from": 4, "still": "b1"},
        {"from": 5, "still": "b1", "marks": [("hashes", 3), ("hashes", 5), ("hashes", 7)]},
        {"from": 6, "still": "b1", "marks": [("text", 3, "## "), ("text", 5, "## "), ("text", 7, "## ")]},
        {"from": 7, "still": "b1x", "marks": [("lines", 3, 3)]},
        {"from": 8, "still": "b1x", "marks": [_PRE]},
        {"from": 9, "still": "b1", "marks": [("lines", 3, 3)]},
    ]},
    "s05_paragraphs": {"step": 3, "beats": [
        {"from": 0, "still": "b2", "marks": [("lines", 3, 3)]},
        {"from": 2, "still": "b2", "marks": [("lines", 4, 4)]},
        {"from": 3, "still": "b2"},
        {"from": 4, "still": "b2e", "marks": [("lines", 3, 4)]},
        {"from": 5, "still": "b2e", "marks": [_PRE]},
        {"from": 6, "still": "game_log_p2", "marks": [_G_PARA]},     # the game first: two typed lines, one paragraph
        {"from": 8, "still": "game_sci_hull_sci2", "marks": [_G_READ]},  # a reading, where a line IS a reading
        {"from": 10, "still": "b2t", "marks": [("lines", 3, 3)]},
        {"from": 11, "still": "b2t", "marks": [_PRE]},
        {"from": 13, "still": "b2"},
    ]},
    "s06_two_lists": {"step": 4, "beats": [
        {"from": 0, "still": "b3", "marks": [("lines", 11, 13)]},
        {"from": 1, "still": "b3", "marks": [_PRE]},
        {"from": 2, "still": "b4", "marks": [("lines", 17, 19)]},
        {"from": 3, "still": "b4", "marks": [_PRE]},
        {"from": 4, "still": "b4", "marks": [("lines", 17, 19)]},
        {"from": 6, "still": "b4", "marks": [("lines", 10, 10), ("lines", 14, 14), ("lines", 16, 16)]},
    ]},
    "s07_one_link": {"step": 6, "beats": [
        {"from": 0, "still": "b5", "marks": [("text", 7, "[the Mary Celeste]"), ("text", 7, _URL)]},
        {"from": 1, "still": "b5", "marks": [("text", 7, "[the Mary Celeste]")]},
        {"from": 2, "still": "b5", "marks": [("text", 7, _URL)]},
        {"from": 3, "still": "b5", "marks": [("text", 7, "[the Mary Celeste]"), ("text", 7, _URL)]},
        {"from": 4, "still": "b5"},
        {"from": 5, "still": "b5", "marks": [_PRE]},
        {"from": 6, "still": "game_sci_hull_sci2"},
        {"from": 8, "still": "game_sci_hull_sci2", "marks": [_G_READ, _G_SCAN]},
        {"from": 9, "still": "m47", "marks": [("lines", 47, 47)]},
        {"from": 10, "still": "m47", "marks": [("hashes", 47), ("text", 47, "[Derelict Hull]"), ("text", 47, "(derelict_scan)")]},
        {"from": 12, "still": "m47", "marks": [("lines", 47, 47)]},
        {"from": 13, "still": "m47", "marks": [("text", 47, "(derelict_scan)")]},
    ]},
    "s08_bold_and_italic": {"step": 7, "beats": [
        {"from": 0, "still": "b6", "marks": [("text", 7, "**nobody**")]},
        {"from": 1, "still": "b7", "marks": [("text", 19, "*Not written yet:*")]},
        {"from": 2, "still": "b7", "marks": [_PRE]},
        {"from": 3, "still": "m47"},
    ]},
    "s09_the_plain_keyboard": {"step": 8, "beats": [
        {"from": 0, "still": "b_final"},
        {"from": 1, "still": "card_curly"},
        {"from": 2, "still": "card_curly", "marks": [("part", "find1"), ("part", "find2"), ("part", "find3")]},
        {"from": 3, "still": "card_curly", "marks": [("part", "find4"), ("part", "find5")]},
        {"from": 4, "still": "card_curly"},
        {"from": 5, "still": "bw", "marks": [("lines", 5, 5)]},
        {"from": 6, "still": "card_plain"},
        {"from": 8, "still": "b_final"},
        {"from": 9, "still": "card_curly"},
        {"from": 10, "still": "card_plain", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3"), ("part", "r4")]},
    ]},
    "s10_the_mission_file_with_new_ey": {"step": 9, "beats": [
        {"from": 0, "still": "m47"},
        {"from": 2, "still": "m47", "marks": [("hashes", 45), ("hashes", 47), ("hashes", 55),
                                              ("text", 47, "[Derelict Hull](derelict_scan)")]},
        {"from": 3, "still": "m47"},
        {"from": 4, "still": "m47", "marks": [("lines", 47, 47)]},
        {"from": 5, "still": "m47", "marks": [("text", 47, "[Derelict Hull]"), ("text", 47, "(derelict_scan)")]},
        {"from": 6, "still": "m47", "marks": [("lines", 48, 48), ("lines", 51, 51)]},
        {"from": 7, "still": "m47", "marks": [("lines", 48, 51)]},
        {"from": 8, "still": "game_sci_hull_sci2", "marks": [_G_READ]},
        {"from": 10, "still": "m47", "marks": [("lines", 52, 53)]},
        {"from": 12, "still": "game_sci_hull_sci2", "marks": [_G_READ]},
        {"from": 13, "still": "m47", "marks": [("lines", 42, 44)]},
        {"from": 14, "still": "card_five", "marks": [("part", "r5")]},
        {"from": 16, "still": "card_five"},
        {"from": 17, "still": "b_final", "marks": [_PRE]},
        {"from": 18, "still": "game_log_p2"},
    ]},
    "s11_the_game_is_not_a_preview": {"step": 11, "beats": [
        {"from": 0, "still": "m31", "marks": [("lines", 31, 31)]},
        {"from": 1, "still": "m12", "marks": [("lines", 31, 42)]},
        {"from": 2, "still": "m12", "marks": [("hashes", 31), ("lines", 32, 33), ("lines", 35, 36)]},
        {"from": 3, "still": "m12", "marks": [("lines", 38, 40), ("text", 42, "[the old report](https://example.com/report)")]},
        {"from": 5, "still": "game_helm"},
        {"from": 6, "still": "game_padd", "marks": [_QUESTS]},
        {"from": 7, "still": "game_log_p2", "marks": [_G_ROW]},
        {"from": 8, "still": "game_log_p2", "marks": [_G_TEXT]},
        {"from": 9, "still": "game_log_p2", "marks": [_G_HEAD]},
        {"from": 10, "still": "game_log_p2", "marks": [_G_PARA]},
        {"from": 12, "still": "game_log_p2", "marks": [_G_STARS]},
        {"from": 13, "still": "game_log_p2", "marks": [_G_LIST]},
        {"from": 14, "still": "game_log_p2", "marks": [_G_TABLE]},
        {"from": 15, "still": "game_log_p2", "marks": [_G_LINK]},
        {"from": 16, "still": "game_log_p2", "marks": [_G_TEXT]},
        {"from": 18, "still": "card_reads"},
        {"from": 20, "still": "card_rules"},
        {"from": 21, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 23, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 24, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 26, "still": "m12", "marks": [("lines", 31, 42)]},
        {"from": 27, "still": "m31", "marks": [("lines", 31, 31)]},
    ]},
    "s12_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4"), ("part", "item5"), ("part", "item6")]},
        {"from": 4, "still": "card_exercise"},
        {"from": 6, "still": "card_next"},
    ]},
}
