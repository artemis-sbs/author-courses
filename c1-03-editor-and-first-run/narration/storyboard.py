"""Storyboard for c1-03-editor-and-first-run: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6, and the new kinds of still in _tools/picture/README.md. Caption numbers are those
of the narration REWRITTEN FOR THE EAR (2026-10-06).

What is real and what is not:

- The Command Prompt stills are ONE real cmd.exe session in the stand-in (tool 0.13) with
  no MyMission in it: `sbs templates`, the `create` line (Enter at its question), the
  `fetch` line, lint and the dry run, in that order. The folder it made is the page's
  example\\ byte for byte. The window round the text is drawn.
- VS Code is real (1.140, add-on 0.9.4, the throwaway profile). The Extensions panel, the
  Workspace Trust page, the Outline and the Problems panel are opened by VS Code's own
  commands, run by a helper add-on that exists only in the throwaway profile: no key is
  pressed. That helper is why the Extensions panel is filtered to "Artemis": it would
  otherwise be listed beside the add-on. The untrusted window is a real Restricted Mode.
- The two web pages and the `sbs debug` page are drawn by headless Edge.
- The game is real (game.py): the page's own run line on a probe copy of the example.
- The VS Code installer, the menus and the store apps are cards in the page's own words.
"""
LECTURE = "c1-03-editor-and-first-run"
TITLE = ("Class 1, Lecture 3", "Your editor and your first run", "An editor, a mission made with one line, and a first flight")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example"},
    # Step 5: line 47 with its key taken off, as the page has the student do
    "b47": {"base": "start", "edits": [("replace", FILE, "### [Derelict Hull](derelict_scan)", "### [Derelict Hull]")]},
}

_NO = {"without": ("MyMission",)}
_CREATE = 'sbs create MyMission -t amd --title "The Cold Hulk"'
_FETCH = 'sbs fetch "MyMission" --update-libs'
_DRY = "sbs run server,helm,science -m MyMission map=0 --dry-run"
_MAKE = ["sbs templates", (_CREATE, ("",)), _FETCH, "sbs lint MyMission", _DRY]
_SLIPS = ["sbs create MyMission -t amd", "sbs run MyMission --dry-run",
          "sbs run server, helm -m MyMission map=0 --dry-run"]
_S5 = "Step 5 - Open your mission in VS Code"
_S9 = "Step 9 - Check it: what the tools say when you slip"
_BACK = ["workbench.action.focusFirstEditorGroup"]

STILLS = {
    # VS Code, real
    "v_color": ("vscode", "start", 10, "wide"),
    "v_ext": ("vscode", "start", 10, "wide", {"do": [["workbench.extensions.search", "@installed Artemis"]]}),
    "v_search": ("vscode", "start", 10, "wide", {"do": [["workbench.extensions.search", "Artemis"], 5000]}),
    "v_untrusted": ("vscode", "start", 10, "wide", {"trust": False}),
    "v_trustpage": ("vscode", "start", 10, "wide", {"trust": False, "plain": True, "do": [["workbench.trust.manage"]]}),
    "v_outline": ("vscode", "start", 10, "wide", {"do": [["outline.focus"], _BACK]}),
    "v_47": ("vscode", "start", 47, "close"),
    "v_47b": ("vscode", "b47", 47, "close"),
    "v_problems": ("vscode", "b47", 47, "close", {"do": [["workbench.actions.view.problems"], _BACK]}),
    "v_dot": ("vscode", "start", 46, "close", {"do": [["type", {"text": " "}]]}),
    # one real cmd.exe session
    "t_prompt": ("session", [], _NO),
    "t_templates": ("session", _MAKE, dict(_NO, show=(1, 1), head=17, keep={"MyMission_as_created": "MyMission"})),
    "t_create": ("session", _MAKE, dict(_NO, show=(2, 2))),
    "t_fetch_head": ("session", _MAKE, dict(_NO, show=(3, 3), head=8)),
    "t_fetch": ("session", _MAKE, dict(_NO, show=(3, 3), tail=14)),
    "t_lint": ("session", _MAKE, dict(_NO, show=(4, 4))),
    "t_dry": ("session", _MAKE, dict(_NO, show=(5, 5))),
    "t_s1": ("session", _SLIPS, {"state": "start", "show": (1, 1)}),
    "t_s2": ("session", _SLIPS, {"state": "start", "show": (2, 2)}),
    "t_s3": ("session", _SLIPS, {"state": "start", "show": (3, 3)}),
    # File Explorer, real
    "x_before": ("explorer", "data\\missions", _NO),
    "x_after": ("explorer", "data\\missions", {"state": "start"}),
    "x_lib": ("explorer", "data\\missions\\__lib__", {}),
    # web pages, by headless Edge
    "w_code": ("web", "https://code.visualstudio.com/", {"wait": 8}),
    "w_release": ("web", "https://github.com/artemis-sbs/sbs_cli/releases/tag/amd-vscode-v0.9.4", {"wait": 8}),
    "w_debug": ("web", "debug", {"state": "start", "map": "0", "budget": 12000}),
    "w_debug_term": ("derived", "what `sbs debug MyMission --map 0` printed while w_debug was taken"),
    # the real game (game.py), the page's run line on a probe copy of the example
    "game_server": ("game", "the window titled server: the main screen"),
    "game_helm": ("game", "the window titled helm"),
    "game_science": ("game", "the window titled science"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_word": ("card", "page", {"kicker": "What a word processor does to what you type",
                                   "text": ["sbs create MyMission –title “The Cold Hulk”"],
                                   "find": ["–", "“", "”"],
                                   "caption": "Curled quote marks, and two hyphens joined into one long dash. The game reads neither."}),
    "card_installer": ("card", "table", {"heading": "Step 1 - Get VS Code", "kicker": "The installer: Select Additional Tasks"}),
    "card_vsix": ("card", "list", {"heading": "Step 2 - Add the Artemis AMD add-on", "kicker": "Hand the add-on to VS Code"}),
    "card_open": ("card", "points", {"kicker": "Open the mission's folder, not one file in it", "items": [
        "In VS Code, open the **File** menu and choose **Open Folder...**",
        "Go to `data\\missions`. Click `MyMission` once. Click **Select Folder**."]}),
    "card_trust": ("card", "table", {"heading": _S5, "kicker": "VS Code decides whether it trusts the folder"}),
    "card_keys": ("card", "table", {"heading": _S5, "nth": 4, "kicker": "Two habits for the editor"}),
    "card_stop": ("card", "points", {"kicker": "To stop the rehearsal", "items": [
        "Click the command prompt window and press `Ctrl+C`. It prints `[runner] stopped`.",
        "If it then asks `Terminate batch job (Y/N)?`, type `Y` and press Enter."]}),
    "card_slips": ("card", "table", {"heading": _S9, "nth": 5, "rows": (1, 4, 5, 8), "kicker": "What nothing warns you about"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 4", "sub": "Markdown in twenty minutes"}),
}

# on the real windows (fractions of the picture); set from the stills
_ACT = ("rect", 0.0, 0.036, 0.032, 0.962)                # v_color: the Activity Bar
_SIDE = ("rect", 0.034, 0.036, 0.226, 0.962)             # the Side Bar
_EDIT = ("rect", 0.230, 0.036, 0.998, 0.962)             # the Editor
_STAT = ("rect", 0.0, 0.964, 1.0, 1.0)                   # the Status Bar
_FILES = ("rect", 0.036, 0.106, 0.223, 0.285)            # the seven files
_F_AMD = ("rect", 0.036, 0.157, 0.223, 0.183)            # mission.amd in the list
_F_MAST = ("rect", 0.036, 0.259, 0.223, 0.285)           # story.mast
_F_REST = [("rect", 0.036, 0.106, 0.223, 0.156), ("rect", 0.036, 0.184, 0.223, 0.258)]   # the other five
_AMD = ("rect", 0.951, 0.968, 0.975, 0.996)              # "AMD" in the Status Bar
_EXT_ICON = ("rect", 0.004, 0.243, 0.030, 0.287)         # v_ext: the Extensions icon
_EXT_DOTS = ("rect", 0.208, 0.043, 0.226, 0.068)         # the three dots
_EXT_AMD = ("rect", 0.037, 0.122, 0.223, 0.200)          # Artemis AMD, installed
_EXT_REST = ("rect", 0.037, 0.205, 0.223, 0.955)         # v_search: what a search offers
_ASSET = ("rect", 0.190, 0.655, 0.300, 0.692)            # w_release: the .vsix under Assets
_BAND = ("rect", 0.0, 0.037, 0.43, 0.064)                # v_untrusted: the Restricted Mode band
_RESTRICTED = ("rect", 0.024, 0.966, 0.105, 0.998)       # Restricted Mode in the Status Bar
_TRUSTME = ("rect", 0.883, 0.966, 0.975, 0.998)          # AMD: trust this folder
_TRUST = ("rect", 0.308, 0.658, 0.374, 0.697)            # v_trustpage: the Trust button
_OUTLINE = ("rect", 0.037, 0.755, 0.223, 0.925)          # v_outline
_PROBLEMS = ("rect", 0.232, 0.628, 0.998, 0.722)         # v_problems: the panel
_TAB = ("rect", 0.234, 0.040, 0.318, 0.072)              # v_dot: the tab and its dot
_STATION = ("rect", 0.455, 0.455, 0.545, 0.585)          # game_helm: DS 1 and the ship
_HULK = ("rect", 0.455, 0.370, 0.540, 0.448)             # game_helm: the hulk and its bearing
_SCI_ROW = ("rect", 0.698, 0.688, 0.930, 0.733)          # game_science: the hulk in the list (still "unknown")
_TITLE = ("rect", 0.885, 0.0, 1.0, 0.045)                # a game window's name

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "v_color"},
        {"from": 1, "still": "game_helm"},
        {"from": 2, "still": "x_before"},
        {"from": 3, "still": "card_title"},
    ]},
    "s02_get_vs_code": {"step": 1, "beats": [
        {"from": 0, "still": "v_color"},
        {"from": 1, "still": "card_word"},
        {"from": 2, "still": "card_word", "marks": [("part", "find1"), ("part", "find2"), ("part", "find3")]},
        {"from": 4, "still": "w_code"},
        {"from": 6, "still": "card_installer"},
        {"from": 7, "still": "card_installer", "marks": [("part", "r2"), ("part", "r3")]},
        {"from": 8, "still": "v_color"},
        {"from": 9, "still": "v_color", "marks": [_ACT, _SIDE]},
        {"from": 10, "still": "v_color", "marks": [_EDIT]},
        {"from": 11, "still": "v_color", "marks": [_STAT]},
    ]},
    "s03_the_add_on": {"step": 2, "beats": [
        {"from": 0, "still": "v_color"},
        {"from": 2, "still": "v_ext", "marks": [_EXT_ICON]},
        {"from": 4, "still": "w_release"},
        {"from": 5, "still": "w_release", "marks": [_ASSET]},
        {"from": 6, "still": "card_vsix", "marks": [("part", "item3"), ("part", "item4")]},
        {"from": 6.6, "still": "v_ext", "marks": [_EXT_DOTS, _EXT_AMD]},
        {"from": 7, "still": "v_search"},
        {"from": 9, "still": "v_search", "marks": [_EXT_REST]},
    ]},
    "s04_make_the_mission": {"step": 3, "beats": [
        {"from": 0, "still": "t_prompt"},
        {"from": 1, "still": "t_prompt", "marks": [("part", "end:prompt")]},
        {"from": 2, "still": "t_templates", "marks": [("part", "run1:cmd")]},
        {"from": 3, "still": "t_templates", "marks": [("span", 1, "minimal"), ("span", 1, "sandbox"), ("span", 1, "addon"),
                                                      ("span", 1, "amd  "), ("span", 1, "ou  ")]},
        {"from": 4, "still": "t_templates", "marks": [("span", 1, "amd            AMD driven mission")]},
        {"from": 5, "still": "t_create", "marks": [("part", "run1:cmd")]},
        {"from": 6, "still": "t_create", "marks": [("cmd", 1, "create MyMission")]},
        {"from": 7, "still": "t_create", "marks": [("cmd", 1, "-t amd")]},
        {"from": 8, "still": "t_create", "marks": [("cmd", 1, "--title")]},
        {"from": 9, "still": "t_create", "marks": [("cmd", 1, "\"The Cold Hulk\"")]},
        {"from": 10, "still": "t_create", "marks": [("span", 1, "Fetch these dependencies now? [Y/n]:")]},
        {"from": 12, "still": "x_after", "marks": [("part", "row:MyMission")]},
    ]},
    "s05_bring_the_libraries_up_to_da": {"step": 4, "beats": [
        {"from": 0, "still": "t_create", "marks": [("span", 1, _FETCH)]},
        {"from": 1, "still": "x_lib"},
        {"from": 2, "still": "t_create", "marks": [("span", 1, "14 of its 14 libraries were already here and were kept as they are.")]},
        {"from": 4, "still": "t_fetch_head", "marks": [("part", "run1:cmd")]},
        {"from": 5, "still": "t_fetch"},
        {"from": 6, "still": "t_fetch", "marks": [("span", 1, "Libraries are up to date. MyMission itself was not changed.")]},
        {"from": 7, "still": "t_fetch_head", "marks": [("cmd", 1, "--update-libs")]},
    ]},
    "s06_open_the_folder_and_trust_it": {"step": 5, "beats": [
        {"from": 0, "still": "card_open"},
        {"from": 2, "still": "card_open", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_open", "marks": [("part", "item2")]},
        {"from": 4, "still": "v_untrusted", "marks": [_BAND]},
        {"from": 5, "still": "v_trustpage", "marks": [_TRUST]},
        {"from": 6, "still": "v_untrusted", "marks": [_RESTRICTED]},
        {"from": 7, "still": "v_untrusted", "marks": [_TRUSTME]},
        {"from": 9, "still": "v_color", "marks": [_FILES]},
        {"from": 10, "still": "v_color", "marks": [_F_AMD]},
        {"from": 11, "still": "v_color", "marks": [_F_MAST]},
        {"from": 12, "still": "v_color", "marks": _F_REST},
    ]},
    "s07_the_add_on_at_work": {"step": None, "beats": [
        {"from": 0, "still": "v_color"},
        {"from": 1, "still": "v_color", "marks": [("lines", 10, 10), _AMD]},
        {"from": 2, "still": "v_outline", "marks": [_OUTLINE]},
        {"from": 3, "still": "v_47"},
        {"from": 4, "still": "v_47", "marks": [("text", 47, "(derelict_scan)")]},
        {"from": 5, "still": "v_47b", "marks": [("lines", 47, 47)]},
        {"from": 6, "still": "v_problems", "marks": [_PROBLEMS]},
        {"from": 7, "still": "v_47", "marks": [("text", 47, "(derelict_scan)")]},
        {"from": 8, "still": "v_47"},
        {"from": 9, "still": "card_keys"},
        {"from": 10, "still": "card_keys", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 11, "still": "v_dot", "marks": [_TAB]},
    ]},
    "s08_check_it": {"step": 6, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_lint", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "t_lint"},
    ]},
    "s09_play_it": {"step": 7, "beats": [
        {"from": 0, "still": "t_dry", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "t_dry", "marks": [("span", 1, "server  "), ("span", 1, "helm  "), ("span", 1, "science  ")]},
        {"from": 3, "still": "t_dry", "marks": [("cmd", 1, "--dry-run")]},
        {"from": 5, "still": "t_dry", "marks": [("cmd", 1, "server,helm,science")]},
        {"from": 6, "still": "t_dry", "marks": [("cmd", 1, "-m MyMission")]},
        {"from": 7, "still": "t_dry", "marks": [("cmd", 1, "map=0")]},
        {"from": 8, "still": "t_dry"},
        {"from": 9, "still": "game_server"},
        {"from": 9.5, "still": "game_science", "marks": [_TITLE]},
        {"from": 10, "still": "game_helm", "marks": [_TITLE]},
        {"from": 11, "still": "game_helm", "marks": [_STATION]},
        {"from": 11.45, "still": "game_helm", "marks": [_HULK]},
        {"from": 12, "still": "game_science", "marks": [_SCI_ROW]},
        {"from": 13, "still": "game_server"},
    ]},
    "s10_the_rehearsal": {"step": 8, "beats": [
        {"from": 0, "still": "w_debug_term", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "w_debug"},
        {"from": 2, "still": "w_debug_term"},
        {"from": 3, "still": "w_debug_term", "marks": [("span", 1, "EXTRA_SHIP_DATA is off"),
                                                       ("span", 1, "no @media/skybox labels are loaded"),
                                                       ("span", 1, "Elapsed time:")]},
        {"from": 4, "still": "w_debug_term"},
        {"from": 6, "still": "w_debug_term", "marks": [("span", 1, "open http://localhost:8765/")]},
        {"from": 7, "still": "w_debug"},
        {"from": 9, "still": "card_stop", "marks": [("part", "item1")]},
        {"from": 10, "still": "game_helm"},
    ]},
    "s11_four_slips": {"step": 9, "beats": [
        {"from": 0, "still": "t_s1"},
        {"from": 1, "still": "t_s1", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "t_s1", "marks": [("span", 1, "already exists and is not empty")]},
        {"from": 3, "still": "t_s2", "marks": [("cmd", 1, "MyMission")]},
        {"from": 4, "still": "t_s2", "marks": [("span", 1, "note: no 'Server' in the list")]},
        {"from": 5, "still": "t_s3", "marks": [("cmd", 1, "server, helm")]},
        {"from": 6, "still": "t_s3", "marks": [("out", 1, 2)]},
        {"from": 7, "still": "v_untrusted"},
        {"from": 8, "still": "v_untrusted", "marks": [_RESTRICTED, _TRUSTME]},
        {"from": 9, "still": "card_slips"},
    ]},
    "s12_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item6")]},
        {"from": 5, "still": "card_next"},
    ]},
}
