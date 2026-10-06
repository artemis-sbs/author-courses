"""Storyboard for c1-02-files-folders-command-prompt: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6, and the new kinds of still (File Explorer, a cmd session) in _tools/picture/README.md.
Caption numbers are those of the narration REWRITTEN FOR THE EAR (2026-10-06).

This lecture makes no file, so there are no STATES. What is on screen:

- File Explorer is REAL: this machine's own File Explorer on the pipeline's stand-in game
  folder, as it is before the student makes a mission ("without" MyMission). Its address bar
  shows the stand-in's real folders (... > Cosmos > data > missions), not C:\\Cosmos.
- Every Command Prompt still is one real cmd.exe session in the stand-in (tool 0.13); the
  window round it is drawn, and the stand-in's real folder is written C:\\Cosmos, as the
  page writes it.
- This machine SHOWS file name extensions, and that setting is not touched. The hidden
  state, the two menus, the click on the address bar, the store apps and the word
  processor are cards in the page's own words.
"""
LECTURE = "c1-02-files-folders-command-prompt"
TITLE = ("Class 1, Lecture 2", "Files, folders and the command prompt",
         "Find the game's folder, open a window in it, and ask one question")
MISSION = "MyMission"
FILE = "mission.amd"

STATES = {}

_NO = {"without": ("MyMission",)}                     # the student has not made a mission yet
_S9 = "Step 9 - Check it: what the window says when you slip"
_LOST = ["cd LegendaryMissions", "sbs version", "cd ..", "sbs version"]
_VER = ["sbs version", "sbs update", "sbs version"]

STILLS = {
    # File Explorer, real
    "x_root": ("explorer", "", {}),
    "x_data": ("explorer", "data", {}),
    "x_missions": ("explorer", "data\\missions", _NO),
    # one real cmd.exe session each (drawn window, real text)
    "t_fresh": ("session", [], dict(_NO, banner=True)),
    "t_ps": ("session", [], dict(_NO, shell="powershell")),
    "t_ps_fail": ("session", ["sbs version"], dict(_NO, shell="powershell")),
    "t_dir": ("session", ["dir"], _NO),
    "t_ver1": ("session", _VER, dict(_NO, show=(1, 1))),
    "t_ver2": ("session", _VER, dict(_NO, show=(1, 2))),
    "t_ver3": ("session", _VER, _NO),
    "t_env": ("session", ["sbs doctor --env"], _NO),
    "t_lost1": ("session", _LOST, dict(_NO, show=(1, 1))),
    "t_lost2": ("session", _LOST, dict(_NO, show=(1, 2))),
    "t_lost3": ("session", _LOST, dict(_NO, show=(1, 3))),
    "t_lost4": ("session", _LOST, _NO),
    "t_slip1": ("session", ["sbs doctr"], _NO),
    "t_slip2": ("session", ["sbs doctor \u2013env"], _NO),
    "t_doc": ("session", ["sbs doctor"], dict(_NO, tail=24)),
    "t_doc_lm": ("session", ["sbs doctor LegendaryMissions"], _NO),
    # drawn
    "card_title": ("card", "title", {}),
    "card_store": ("card", "table", {"heading": "Step 1 - Find the game's folder", "kicker": "Ask the store where the game is"}),
    "card_path": ("card", "points", {"kicker": "Click the empty part of the address bar: the path", "items": [
        "`C:\\Cosmos\\data\\missions`",
        "The drive `C:`, the folder `Cosmos` on it, `data` inside that, `missions` inside that.",
        "The backslash `\\` means inside."]}),
    "card_hidden": ("card", "points", {"kicker": "Windows hides the extension of every kind of file it knows", "items": [
        "A file named `sbs.bat` is shown as `sbs`.",
        "A file named `mission.amd.txt` is shown as `mission.amd`. It looks right, and the game cannot find it."]}),
    "card_ext": ("card", "table", {"heading": "Step 3 - Show file name extensions", "kicker": "Turn the hiding off, once"}),
    "card_cmd": ("card", "list", {"heading": "Step 4 - Open a command prompt in `data\\missions`",
                                  "kicker": "Open a command prompt here"}),
    "card_word": ("card", "page", {"kicker": "Copied from a word processor", "text": ["sbs doctor \u2013env"],
                                   "find": ["\u2013"], "caption": "It turned two hyphens into one long dash."}),
    "card_keys": ("card", "points", {"kicker": "Four keys", "items": [
        "**Enter** runs the line you typed.", "**Up arrow** brings back the last command you ran.",
        "**Backspace** rubs out the character before the cursor.", "**Esc** clears the line you are typing."]}),
    "card_slips": ("card", "table", {"heading": _S9, "nth": 2, "rows": (1, 2, 3, 5, 6, 7),
                                     "kicker": "Typing slips, in the right place"}),
    "card_rules": ("card", "points", {"kicker": "A problem row under a mission", "items": [
        "Is it your mission? A mission that came with the game is not yours. Leave it.",
        "Do not type a command because a report says so.",
        "Never type `sbs fetch` with nothing after it: it replaces a whole mission folder."]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 3", "sub": "Your editor and your first run"}),
}

_COUNT = "0 problems"
_NOTREC = "'sbs' is not recognized as an internal or external command,"

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "t_env", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_env", "marks": [("part", "run1:last")]},
        {"from": 2, "still": "t_env"},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_files_folders_and_the_two_wi": {"step": None, "beats": [
        {"from": 0, "still": "x_root"},
        {"from": 1, "still": "x_root", "marks": [("part", "row:Artemis3-x64-release.exe")]},
        {"from": 3, "still": "x_root", "marks": [("part", "row:data")]},
        {"from": 4, "still": "x_data", "marks": [("part", "row:missions")]},
        {"from": 5, "still": "x_missions"},
        {"from": 6, "still": "t_fresh"},
        {"from": 7, "still": "x_missions", "marks": [("part", "rows")]},
    ]},
    "s03_find_the_game_s_folder": {"step": 1, "beats": [
        {"from": 0, "still": "card_store"},
        {"from": 3, "still": "card_store", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_store", "marks": [("part", "r2")]},
        {"from": 7, "still": "x_root"},
        {"from": 8, "still": "x_root", "marks": [("part", "row:data"), ("part", "row:PyAddons"), ("part", "row:PyRuntime"),
                                                ("part", "row:Artemis3-x64-release.exe")]},
        {"from": 9, "still": "x_root", "marks": [("part", "row:Artemis3-x64-release.exe")]},
        {"from": 10, "still": "x_root", "marks": [("part", "row:data")]},
        {"from": 11, "still": "x_root", "marks": [("part", "row:PyAddons"), ("part", "row:PyRuntime")]},
        {"from": 12, "still": "x_root"},
    ]},
    "s04_down_to_missions_and_what_a_": {"step": 2, "beats": [
        {"from": 0, "still": "x_root", "marks": [("part", "row:data")]},
        {"from": 0.5, "still": "x_data", "marks": [("part", "row:missions")]},
        {"from": 1, "still": "x_missions"},
        {"from": 2, "still": "x_missions", "marks": [("part", "row:LegendaryMissions"), ("part", "row:SecretMeeting"),
                                                    ("part", "row:WalkTheLine")]},
        {"from": 4, "still": "x_missions", "marks": [("part", "address")]},
        {"from": 6, "still": "card_path", "marks": [("part", "item1")]},
        {"from": 9, "still": "card_path", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_path", "marks": [("part", "item3")]},
        {"from": 12, "still": "card_path", "marks": [("part", "item1")]},
    ]},
    "s05_show_the_extensions": {"step": 3, "beats": [
        {"from": 0, "still": "x_missions"},
        {"from": 1, "still": "x_missions", "marks": [("part", "row:sbs.bat"), ("part", "row:sbs.pyz")]},
        {"from": 3, "still": "card_hidden"},
        {"from": 4, "still": "card_hidden", "marks": [("part", "item1")]},
        {"from": 6, "still": "card_hidden"},
        {"from": 7, "still": "card_hidden", "marks": [("part", "item2")]},
        {"from": 10, "still": "card_ext", "marks": [("part", "r1")]},
        {"from": 11, "still": "x_missions", "marks": [("part", "row:sbs.bat")]},
    ]},
    "s06_open_the_command_prompt_here": {"step": 4, "beats": [
        {"from": 0, "still": "x_missions", "marks": [("part", "address")]},
        {"from": 1, "still": "card_cmd", "marks": [("part", "item2")]},
        {"from": 2, "still": "card_cmd", "marks": [("part", "item3"), ("part", "item4")]},
        {"from": 3, "still": "t_fresh"},
        {"from": 4, "still": "t_fresh", "marks": [("part", "end:prompt")]},
        {"from": 8, "still": "t_ps"},
        {"from": 10, "still": "t_ps", "marks": [("part", "end:prompt")]},
        {"from": 11, "still": "t_ps_fail", "marks": [("out", 1, 1), ("out", 1, 2)]},
        {"from": 12, "still": "t_fresh", "marks": [("part", "end:prompt")]},
    ]},
    "s07_look_around_dir_and_four_key": {"step": 5, "beats": [
        {"from": 0, "still": "t_dir", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_dir"},
        {"from": 2, "still": "t_dir", "marks": [("span", 1, "<DIR>          LegendaryMissions")]},
        {"from": 3, "still": "t_dir", "marks": [("span", 1, "121 sbs.bat")]},
        {"from": 4, "still": "x_missions", "marks": [("part", "rows")]},
        {"from": 6, "still": "card_keys"},
        {"from": 7, "still": "card_keys", "marks": [("part", "item1")]},
        {"from": 8, "still": "card_keys", "marks": [("part", "item2")]},
        {"from": 9, "still": "card_keys", "marks": [("part", "item3")]},
        {"from": 10, "still": "card_keys", "marks": [("part", "item4")]},
    ]},
    "s08_the_first_command_to_the_too": {"step": 6, "beats": [
        {"from": 0, "still": "x_missions"},
        {"from": 1, "still": "x_missions", "marks": [("part", "row:sbs.bat"), ("part", "row:sbs.pyz")]},
        {"from": 3, "still": "t_ver1", "marks": [("part", "run1:cmd")]},
        {"from": 5, "still": "t_ver1", "marks": [("out", 1, 1), ("out", 1, 2)]},
        {"from": 7, "still": "t_ver1", "marks": [("out", 1, 2)]},
        {"from": 8, "still": "t_ver1", "marks": [("out", 1, 1)]},
        {"from": 11, "still": "t_ver1"},
        {"from": 12, "still": "t_ver2", "marks": [("part", "run2:cmd")]},
        {"from": 13, "still": "t_ver2", "marks": [("span", 2, "Updated sbs in")]},
        {"from": 14, "still": "t_ver3", "marks": [("part", "run3:cmd")]},
        {"from": 15, "still": "t_ver3", "marks": [("out", 3, 1)]},
    ]},
    "s09_is_this_computer_set_up": {"step": 7, "beats": [
        {"from": 0, "still": "t_env"},
        {"from": 1, "still": "t_env", "marks": [("part", "run1:cmd")]},
        {"from": 4, "still": "t_env"},
        {"from": 6, "still": "t_env", "marks": [("part", "run1:last")]},
        {"from": 8, "still": "t_env", "marks": [("span", 1, "ok", 1), ("span", 1, "--", 1)]},
        {"from": 9, "still": "t_env", "marks": [("out", 1, 2), ("out", 1, 3), ("out", 1, 4)]},
        {"from": 10, "still": "t_env", "marks": [("span", 1, "--  faces"), ("span", 1, "--  weasyprint"),
                                                 ("span", 1, "--  sbs"), ("span", 1, "--  engine")]},
        {"from": 11, "still": "t_env"},
        {"from": 12, "still": "t_env", "marks": [("span", 1, "faces will print as placeholders in `sbs docs`")]},
        {"from": 13, "still": "t_env", "marks": [("span", 1, "--  faces"),
                                                 ("span", 1, "faces will print as placeholders in `sbs docs`")]},
        {"from": 15, "still": "t_env", "marks": [("span", 1, "--  faces"), ("span", 1, "--  weasyprint"),
                                                 ("span", 1, "--  sbs"), ("span", 1, "--  engine")]},
    ]},
    "s10_get_lost_on_purpose": {"step": 8, "beats": [
        {"from": 0, "still": "x_missions", "marks": [("part", "row:sbs.bat"), ("part", "row:sbs.pyz")]},
        {"from": 2, "still": "t_lost1", "marks": [("part", "run1:cmd")]},
        {"from": 3, "still": "t_lost1", "marks": [("part", "end:prompt")]},
        {"from": 4, "still": "t_lost2", "marks": [("part", "run2:cmd")]},
        {"from": 5, "still": "t_lost2", "marks": [("out", 2, 1), ("out", 2, 2)]},
        {"from": 7, "still": "t_lost2", "marks": [("part", "run2:prompt")]},
        {"from": 8, "still": "t_lost3", "marks": [("part", "run3:cmd")]},
        {"from": 9, "still": "t_lost4", "marks": [("part", "run4:cmd")]},
        {"from": 10, "still": "t_lost4", "marks": [("out", 4, 1), ("out", 4, 2)]},
        {"from": 11, "still": "t_lost4", "marks": [("out", 2, 1), ("out", 2, 2)]},
        {"from": 12, "still": "t_lost4", "marks": [("part", "run2:prompt")]},
        {"from": 13, "still": "card_cmd"},
    ]},
    "s11_three_slips": {"step": 9, "beats": [
        {"from": 0, "still": "t_slip1"},
        {"from": 1, "still": "t_slip1", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "t_slip1", "marks": [("span", 1, "No such command 'doctr'"),
                                                  ("span", 1, "(Did you mean one of: 'docs', 'doctor'?)")]},
        {"from": 3, "still": "card_word"},
        {"from": 4, "still": "card_word", "marks": [("part", "find1")]},
        {"from": 5, "still": "t_slip2", "marks": [("out", 1, 1)]},
        {"from": 6, "still": "t_slip2", "marks": [("part", "run1:cmd")]},
        {"from": 7, "still": "t_lost2", "marks": [("out", 2, 1), ("out", 2, 2)]},
        {"from": 8, "still": "card_slips"},
    ]},
    "s12_the_long_report": {"step": 10, "beats": [
        {"from": 0, "still": "t_doc"},
        {"from": 2, "still": "t_doc", "marks": [("span", 1, _COUNT)]},
        {"from": 3, "still": "t_doc", "marks": [("span", 1, "LegendaryMissions"), ("span", 1, "ok  story.json", 1),
                                                ("span", 1, "ok  libraries", 1), ("span", 1, "ok  art", 2)]},
        {"from": 5, "still": "t_doc"},
        {"from": 6, "still": "card_rules"},
        {"from": 7, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 9, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 13, "still": "t_doc_lm", "marks": [("part", "run1:cmd")], "crop": (0.05, 0.05, 0.6, 0.6)},
    ]},
    "s13_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item4"), ("part", "item5")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item9"), ("part", "item10")]},
        {"from": 4, "still": "card_exercise"},
        {"from": 5, "still": "card_next"},
    ]},
}
