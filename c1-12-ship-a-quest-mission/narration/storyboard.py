"""Storyboard for c1-12-ship-a-quest-mission: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6. Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-05).

The lecture starts from Lecture 11's finished mission.amd and story.mast plus the other
five files of Lecture 3's example\\ ("start": seven files). The first changes of words are
made one at a time; then the picture cuts to the finished files, which are this lecture's
own example\\, all seven ("final").

(2026-10-06: where a still can show a step's RESULT, File Explorer is now real: the folder
under its old and new names, with and without the logs, and the zip beside it. The menus
and the right-click are still cards.)

WHAT IS NOT A CAPTURE. File Explorer (the rename, the clean-up, the zip, the friend's
side) cannot be captured by this pipeline: those steps are plain cards that list the page's
own steps. The printed documents are shown by what `sbs docs` really printed (run WITHOUT
--open) and a card that says what each holds. After the folder is renamed the Command
Prompt stills are made by SCRATCH\\v912\\term12.py from TERM12 below (make.py --capture can
only work in a folder called MyMission): the same real commands, really run.
"""
import os as _os
import re as _re

LECTURE = "c1-12-ship-a-quest-mission"
TITLE = ("Class 1, Lecture 12", "Ship a quest mission", "Make it yours, check it, print it, share it")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_EX = "c1-12-ship-a-quest-mission/example"


def _example(name):
    with open(_os.path.join(_HERE, "example", name), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


def _renamed(name):
    return _re.sub(r"\bsalvage\b", "keeper", _example(name))


STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example")},
    # Step 2: the first changes of words, one at a time
    "w1": {"base": "start", "edits": [("replace", FILE, "### [Salvage Run](salvage)", "### [The Keeper](salvage)")]},
    "w2": {"base": "w1", "edits": [
        ("replace", FILE, "Win: The log is home. DS 1 knows what happened out there.",
         "Win: The keeper is home, and Lantern Nine will burn again."),
        ("replace", FILE, "Lose: The reactor let go with the log still aboard.",
         "Lose: The storm closed over the Deep with the keeper still out there."),
        ("replace", FILE, "The hulk's reactor is failing. Get her flight log back to DS 1 before she goes.",
         "A storm front is ten minutes out. One woman keeps Lantern Nine, and she is not answering. "
         "Find her and bring her in.")]},
    "w3": {"base": "w2", "edits": [
        ("replace", FILE, "#### [Close Inspection](approach)", "#### [Come Alongside](approach)"),
        ("replace", FILE, "Objective: Close to within 500 of the hulk", "Objective: Close to within 500 of Lantern Nine"),
        ("replace", FILE, "The hulk is not answering hails.", "The lantern is not answering hails.")]},
    "w4": {"base": "w3", "edits": [
        ("replace", FILE, "% The hull is cold. Whatever happened here happened a long time ago.",
         "% The lamp housing is cold. Nothing has burned here since last night.")]},
    # ... and the finished text: the page's own example, all seven files
    "final": {"folder": _EX, "same_as": tuple(_EX + "/" + f for f in (
        "mission.amd", "story.mast", "description.yaml", "settings.yaml", "story.json", "__lib__.json", "script.py"))},
    # Step 3: the rule that matters. A title with a bare hyphen in it.
    "hyphen": {"base": "final", "edits": [
        ("replace", "description.yaml", "Visible Mission Name: The Quiet Lantern", "Visible Mission Name: Half-Light")]},
    # Step 4: a key renamed the safe way (everywhere, both files), and by hand (the fact sheet only)
    "r_all": {"base": "final", "edits": [("write", FILE, _renamed(FILE)), ("write", MAST, _renamed(MAST))]},
    "r_hand": {"base": "final", "edits": [("write", FILE, _renamed(FILE))]},
    # PROBE-ONLY, for the game stills, so nobody has to fly. Never shown in the editor.
    # Lantern Nine 2500 away, the skiff 1500 off to one side, the tender brought in beside
    # it, and the reach distances widened. The names, the ship and the sentences are the page's.
    "g_tug": {"base": "final", "edits": [
        ("replace", MAST, 'npc_spawn(0, 0, 9000, "Lantern Nine"', 'npc_spawn(0, 0, 2500, "Lantern Nine"'),
        ("replace", MAST, "npc_spawn(5600, 0, 6000,", "npc_spawn(1100, 0, 1500,"),
        ("replace", FILE, "of Lantern Nine\nDone when: reach derelict 500", "of Lantern Nine\nDone when: reach derelict 30000"),
        ("replace", FILE, "two minutes\nDone when: reach derelict 500", "two minutes\nDone when: reach derelict 30000"),
        ("replace", FILE, "Done when: reach lifeboat 500", "Done when: reach lifeboat 30000"),
        ("replace", FILE, "Loc: 6000, 0, 6000", "Loc: 1500, 0, 1500")]},
    "g_win": {"base": "g_tug", "edits": [("replace", FILE, "Done when: reach station 1000", "Done when: reach station 30000")]},
}

# Command Prompt stills made by term12.py: {still: [(state, folder, command)]}
_Q = "QuietLantern"
_DOCS = "sbs docs QuietLantern --title \"The Quiet Lantern\" --profile player --pdf"
TERM12 = {
    "t_old_name": [("final", _Q, "sbs lint QuietLantern"), ("final", None, "sbs lint MyMission")],
    "t_lint_q": [("final", _Q, "sbs lint QuietLantern")],
    "t_doctor": [("final", _Q, "sbs doctor QuietLantern")],
    "t_docs": [("final", _Q, _DOCS)],
    "t_bible": [("final", _Q, "sbs docs QuietLantern --lens bible")],
    "t_version": [("final", _Q, "sbs version")],
}

_LINT = "sbs lint MyMission"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

_D = {"file": "description.yaml", "side": False}
_S = {"file": "settings.yaml", "side": False}

STILLS = {
    # Step 2: the fact sheet, the first changes one at a time (lines 46 to 66, then 56 to 76)
    "e_w1": ("vscode", "w1", 56, "big", _NS),
    "e_w2": ("vscode", "w2", 56, "big", _NS),
    "e_w3": ("vscode", "w3", 66, "big", _NS),
    "e_w4": ("vscode", "w4", 133, "big", _NS),
    # ... the finished file, in two long looks
    "e_fin_a": ("vscode", "final", 62, "mid", _NS),
    "e_fin_c": ("vscode", "final", 140, "mid", _NS),
    # ... and the script's five places
    "m_25": ("vscode", "final", 25, "big", _M),
    "m_64": ("vscode", "final", 66, "big", _M),
    "m_113": ("vscode", "final", 105, "big", _M),
    # Step 3: the two small files
    "d_desc0": ("vscode", "start", 9, "big", _D),
    "d_desc": ("vscode", "final", 9, "big", _D),
    "d_hyphen": ("vscode", "hyphen", 9, "big", _D),
    "d_set0": ("vscode", "start", 70, "big", _S),
    "d_set": ("vscode", "final", 70, "big", _S),
    # Step 4: a key renamed by hand, in the fact sheet only
    "e_rhand": ("vscode", "r_hand", 56, "big", _NS),
    "m_rhand": ("vscode", "r_hand", 105, "big", _M),
    # the Command Prompt, while the folder is still MyMission
    "t_final": ("terminal", [("final", _LINT)]),
    "t_hyphen": ("terminal", [("hyphen", _LINT)]),
    "t_rall": ("terminal", [("r_all", _LINT)]),
    "t_rhand": ("terminal", [("r_hand", _LINT)]),
    # ... and after the rename: made by term12.py from TERM12 (the same real commands)
    "t_old_name": ("terminal", [("final", "sbs lint QuietLantern"), ("final", "sbs lint MyMission")]),
    "t_lint_q": ("terminal", [("final", "sbs lint QuietLantern")]),
    "t_doctor": ("terminal", [("final", "sbs doctor QuietLantern")]),
    "t_docs": ("terminal", [("final", _DOCS)]),
    "t_bible": ("terminal", [("final", "sbs docs QuietLantern --lens bible")]),
    # the real game, all seven files of the PROBE states laid over a probe mission (game12.py)
    "game_map": ("game", "Helm: Kittiwake, Marrow Station, Lantern Nine, Tender Osprey beside the skiff"),
    "game_log": ("game", "The Quest Log with the example's names"),
    "game_win": ("game", "Helm, Game results with the example's Win sentence"),
    # drawn
    # File Explorer, REAL (added 2026-10-06): the RESULT of a step, never the act. The stand-in's
    # MyMission holds the finished files; for these stills it is called QuietLantern, as the
    # student's is after Step 5, and the logs, the scratch folder and the zip are really there.
    "x_mine": ("explorer", "data\\missions", {"state": "final"}),
    "x_named": ("explorer", "data\\missions", {"state": "final", "rename": {"MyMission": "QuietLantern"}}),
    "x_dirty": ("explorer", "data\\missions\\QuietLantern", {"state": "final", "rename": {"MyMission": "QuietLantern"},
                "add": {"QuietLantern\\__docs__": "dir", "QuietLantern\\__pycache__": "dir",
                        "QuietLantern\\mast.compile.log": "file", "QuietLantern\\mast.runtime.log": "file"}}),
    "x_seven": ("explorer", "data\\missions\\QuietLantern", {"state": "final", "rename": {"MyMission": "QuietLantern"}}),
    "x_zip": ("explorer", "data\\missions", {"state": "final", "rename": {"MyMission": "QuietLantern"},
              "add": {"QuietLantern.zip": "zip:QuietLantern"}}),
    "card_title": ("card", "title", {}),
    "card_do": ("card", "points", {"kicker": "Today", "items": ["Make it yours.", "Check it.", "Print it.", "Share it."]}),
    "card_plan": ("card", "table", {"heading": "Step 1 - Plan your story on paper", "kicker": "The shape, and its slots"}),
    "card_mine": ("card", "table", {"heading": "Step 1 - Plan your story on paper", "kicker": "Mine: The Quiet Lantern",
                                    "rows": (1, 4, 5, 6, 14)}),
    "card_rule": ("card", "points", {"kicker": "One rule", "items": [
        "Change names and sentences. Leave every key.", "[Square brackets] are yours.", "(Round brackets) are the game's."]}),
    "card_noyaml": ("card", "points", {"kicker": "In these two values", "items": [
        "Use letters, numbers, spaces, commas and full stops.", "No hyphen. No colon. No quote mark."]}),
    "card_rename": ("card", "list", {"heading": "Step 4 - If you want to rename a key (you do not have to)",
                                     "kicker": "The safe way is one way: Replace All, across the whole folder"}),
    "card_search": ("card", "search", {"state": "final", "word": "salvage", "want": (9, 2), "kicker": "Replace in the folder: read the list first"}),
    "card_folder": ("card", "list", {"heading": "Step 5 - Give the folder its name", "kicker": "In File Explorer (not captured: the page's own steps)"}),
    "card_sees": ("card", "table", {"heading": "What each check sees", "kicker": "Three checks", "rows": (1, 2, 4, 8)}),
    "card_play": ("card", "list", {"heading": "Check 3 - Play it: does the story happen?", "kicker": "Play it once to a win, and tick this list"}),
    "card_parts": ("card", "table", {"heading": "Step 7 - Print it", "kicker": "One command"}),
    "card_pdf": ("card", "points", {"kicker": "What the PDF holds (three pages; names and sentences only)", "items": [
        "A contents list.", "Every arc and step, with its description.", "Every reading.", "The landmark.",
        "It is the whole plot, in order: for a friend who reads, not one who plays."]}),
    "card_bible": ("card", "points", {"kicker": "What the bible page holds (QuietLantern-bible.html)", "items": [
        "The story as numbered beats: Beat 1, Beat 2, ...", "Under each step: `reached from`, and `leads to`.",
        "A step in the wrong beat is a `Then:` line pointing at the wrong place.",
        "It prints `Win False` and `Lose False`. Your two sentences are fine: the printing is wrong."]}),
    "card_clean": ("card", "table", {"heading": "Your side: clean it, zip it", "kicker": "In File Explorer (not captured): take out what is not the mission"}),
    "card_seven": ("card", "points", {"kicker": "Seven files, and nothing else", "items": [
        "`__lib__.json`", "`description.yaml`", "`mission.amd`", "`script.py`", "`settings.yaml`", "`story.json`", "`story.mast`"]}),
    "card_zip": ("card", "points", {"kicker": "In File Explorer (not captured): zip the folder", "items": [
        "Go up to data\\missions.", "Right-click the QuietLantern folder itself, not the files inside it.",
        "Windows 11: Compress to, then ZIP File. Windows 10: Send to, then Compressed (zipped) folder.",
        "You get QuietLantern.zip beside the folder. The example's is 7 KB."]}),
    "card_friend": ("card", "points", {"kicker": "Their side, in File Explorer (not captured)", "items": [
        "Put the QuietLantern folder from the zip file in the game's data\\missions folder.",
        "Open data\\missions\\QuietLantern: you must see story.mast at once, not another folder."]}),
    "card_note": ("card", "points", {"kicker": "Then four lines, in a command prompt in data\\missions", "items": [
        "`sbs version`", "`sbs update`", "`sbs fetch \"QuietLantern\" --update-libs`",
        "`sbs run server,helm,science -m QuietLantern map=0`"]}),
    "card_rubric": ("card", "points", {"kicker": "The capstone rubric: what done means", "items": [
        "It is yours.", "It is checked.", "It is printed.", "It is shared."]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Three, in order of nerve"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Class 2", "sub": "People in your story"}),
}

_GAME_STOPS = "stops the GAME from starting at all, for every mission"
# on the game's windows (fractions of the 4:3 picture); set from the screenshots
_SHIP = ("rect", 0.18, 0.078, 0.262, 0.112)             # game_map: Kittiwake
_STATION = ("rect", 0.34, 0.532, 0.456, 0.566)
_BEACON = ("rect", 0.35, 0.432, 0.447, 0.466)
_TENDER = ("rect", 0.375, 0.472, 0.487, 0.538)
_MSG = ("rect", 0.015, 0.488, 0.275, 0.56)
_SENTENCE = ("rect", 0.012, 0.215, 0.265, 0.287)

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_map"},
        {"from": 1, "still": "game_map", "marks": [_SHIP, _BEACON]},
        {"from": 2, "still": "card_title"},
        {"from": 4, "still": "card_do"},
        {"from": 5, "still": "card_do", "marks": [("part", "item1")]},
        {"from": 6, "still": "card_do", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 7, "still": "card_do", "marks": [("part", "item4")]},
    ]},
    "s02_the_plan_on_paper": {"step": 1, "beats": [
        {"from": 0, "still": "card_plan"},
        {"from": 4, "still": "card_plan", "marks": [("part", "r3c3"), ("part", "r4c3"), ("part", "r5c3"), ("part", "r6c3")]},
        {"from": 5, "still": "card_plan", "marks": [("part", "r3c2"), ("part", "r4c2"), ("part", "r5c2"), ("part", "r6c2")]},
        {"from": 6, "still": "card_plan", "marks": [("part", "r1c5"), ("part", "r2c5"), ("part", "r3c5")]},
        {"from": 7, "still": "card_mine", "marks": [("part", "r2c4")]},
        {"from": 8, "still": "card_mine", "marks": [("part", "r5c4")]},
    ]},
    "s03_the_words": {"step": 2, "beats": [
        {"from": 0, "still": "card_rule"},
        {"from": 1, "still": "e_w1", "marks": [("text", 50, "[The Keeper]")]},
        {"from": 2, "still": "e_w1", "marks": [("text", 50, "(salvage)")]},
        {"from": 3, "still": "e_w3", "marks": [("text", 66, "derelict")]},
        {"from": 5, "still": "e_w2", "marks": [("lines", 56, 57)]},
        {"from": 6, "still": "e_w3", "marks": [("text", 65, "500"), ("text", 66, "500")]},
        {"from": 8, "still": "e_w4", "marks": [("lines", 133, 133)]},
        {"from": 9, "still": "e_fin_a"},
        {"from": 9.5, "still": "e_fin_c"},
        {"from": 10, "still": "m_25", "marks": [("text", 25, "\"The Quiet Lantern\""), ("lines", 26, 26)]},
        {"from": 10.5, "still": "m_64", "marks": [("text", 64, "\"Marrow Station\""), ("text", 68, "\"Lantern Nine\"")]},
        {"from": 11, "still": "m_113", "marks": [("text", 113, "\"Tender Osprey\"")]},
        {"from": 12, "still": "m_113", "marks": [("text", 113, "\"tsn, tug\"")]},
    ]},
    "s04_lint": {"step": None, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s05_two_small_files": {"step": 3, "beats": [
        {"from": 0, "still": "d_desc0"},
        {"from": 1, "still": "d_desc0", "marks": [("lines", 11, 11), ("lines", 14, 14)]},
        {"from": 2, "still": "d_desc", "marks": [("lines", 11, 11), ("lines", 14, 14)]},
        {"from": 3, "still": "card_noyaml"},
        {"from": 4, "still": "card_noyaml", "marks": [("part", "item2")]},
        {"from": 5, "still": "d_hyphen", "marks": [("text", 11, "Half-Light")]},
        {"from": 8, "still": "t_hyphen", "marks": [("out", 1, 4)]},
        {"from": 9, "still": "t_hyphen", "marks": [("span", 1, _GAME_STOPS)]},
        {"from": 10, "still": "d_desc", "marks": [("lines", 11, 11), ("lines", 14, 14)]},
        {"from": 12, "still": "d_set0", "marks": [("lines", 70, 70)]},
        {"from": 13, "still": "d_set", "marks": [("text", 70, "Kittiwake")]},
        {"from": 14, "still": "game_map", "marks": [_SHIP]},
    ]},
    "s06_renaming_a_key_the_safe_way": {"step": 4, "beats": [
        {"from": 0, "still": "card_rename"},
        {"from": 3, "still": "card_rename", "marks": [("part", "item1"), ("part", "item3")]},
        {"from": 4, "still": "card_search", "marks": [("part", "summary")]},
        {"from": 5, "still": "card_search", "marks": [("part", "file2")]},
        {"from": 6, "still": "t_rall", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "e_rhand", "marks": [("text", 50, "(keeper)")]},
        {"from": 10, "still": "t_rhand", "marks": [("part", "run1:clean")]},
        {"from": 11, "still": "m_rhand", "marks": [("text", 111, "\"salvage/tug\"")]},
        {"from": 12, "still": "m_rhand", "marks": [("text", 111, "\"salvage/tug\"")], "dim": True},
    ]},
    "s07_the_folder_gets_its_name": {"step": 5, "beats": [
        {"from": 0, "still": "x_mine", "marks": [("part", "row:MyMission")]},
        {"from": 3, "still": "card_folder", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 3.6, "still": "x_named", "marks": [("part", "row:QuietLantern")]},
        {"from": 4, "still": "t_old_name", "marks": [("out", 2, 1)]},
        {"from": 5, "still": "t_old_name", "marks": [("part", "run1:cmd")]},
    ]},
    "s08_check_it_three_checks": {"step": 6, "beats": [
        {"from": 0, "still": "card_sees"},
        {"from": 2, "still": "t_lint_q", "marks": [("part", "run1:clean")]},
        {"from": 3, "still": "t_doctor", "move": False},
        {"from": 4, "still": "t_doctor", "marks": [("out", 1, 26), ("out", 1, 27), ("out", 1, 28), ("out", 1, 29)], "move": False},
        {"from": 5, "still": "t_doctor", "marks": [("span", 1, "0 problems")], "move": False},
        {"from": 6, "still": "t_doctor", "marks": [("out", 1, 27), ("out", 1, 28), ("out", 1, 29)], "move": False},
        {"from": 7, "still": "game_map"},
        {"from": 8, "still": "game_map", "marks": [_SHIP, _STATION, _BEACON]},
        {"from": 9, "still": "game_map", "marks": [_TENDER, _MSG]},
        {"from": 10, "still": "game_win", "marks": [_SENTENCE]},
        {"from": 11, "still": "card_play", "marks": [("part", "item9")]},
        {"from": 12, "still": "card_play"},
    ]},
    "s09_print_it": {"step": 7, "beats": [
        {"from": 0, "still": "t_docs", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "card_parts", "marks": [("part", "r2"), ("part", "r3")]},
        {"from": 3, "still": "card_parts", "marks": [("part", "r4")]},
        {"from": 4, "still": "t_docs", "marks": [("out", 1, 2), ("out", 1, 3)]},
        {"from": 5, "still": "card_pdf"},
        {"from": 6, "still": "card_pdf", "marks": [("part", "item5")]},
        {"from": 8, "still": "t_bible", "marks": [("part", "run1:cmd")]},
        {"from": 9, "still": "card_bible", "marks": [("part", "item1")]},
        {"from": 10, "still": "card_bible", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_bible", "marks": [("part", "item3")]},
        {"from": 13, "still": "card_bible", "marks": [("part", "item4")]},
    ]},
    "s10_share_it_my_side": {"step": 8, "beats": [
        {"from": 0, "still": "x_named", "marks": [("part", "row:QuietLantern")]},
        {"from": 2, "still": "card_clean"},
        {"from": 3, "still": "x_dirty", "marks": [("part", "row:__docs__")]},
        {"from": 4, "still": "x_dirty", "marks": [("part", "row:__pycache__"), ("part", "row:mast.compile.log"),
                                                 ("part", "row:mast.runtime.log")]},
        {"from": 6, "still": "x_seven", "marks": [("part", "rows")]},
        {"from": 8, "still": "card_zip", "marks": [("part", "item2")]},
        {"from": 9, "still": "x_zip", "marks": [("part", "row:QuietLantern.zip")]},
    ]},
    "s11_share_it_their_side": {"step": None, "beats": [
        {"from": 0, "still": "card_friend", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_friend", "marks": [("part", "item2")]},
        {"from": 2, "still": "x_seven", "marks": [("part", "row:story.mast")]},
        {"from": 3, "still": "card_note", "marks": [("part", "item1")]},
        {"from": 4, "still": "card_note", "marks": [("part", "item2")]},
        {"from": 5, "still": "card_note", "marks": [("part", "item3")]},
        {"from": 7, "still": "card_note", "marks": [("part", "item4")]},
    ]},
    "s12_done": {"step": None, "beats": [
        {"from": 0, "still": "card_rubric"},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 5, "still": "card_next"},
    ]},
}
