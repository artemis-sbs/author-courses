"""Storyboard for c5-02-your-universe-file: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py.

The lecture starts from NOTHING: `sbs create MyUniverse -t ou --title "The Kestrel Verge"` makes
a folder from the `ou` template (mast_starter/templates/ou): `my_universe.amd` (a universe
called My Universe, two sides, three jobs), `story.mast` that still says My Universe four
times and my_universe.amd twice, and a `description.yaml` that already has the title. The
"start" state is the page's example with those words put back (see _TEMPLATE_* below).

The steps are typed in the video's order: the file renamed ("renamed"), the title record
("titled"), the Scenario chapter ("scen"), the Landmarks chapter ("land", the page's own
kestrel_verge.amd), then story.mast: the title in four places ("mast_t"), the file name in two
("mast_f"), the two start-screen lines ("final", both files the page's own). "typo" is the
Step 8 break: one letter of the title on the `display:` line only.

Line numbers in the marks are worked out from the state's own text (ln()), so they stay true
if a state changes. The stand-in folder is MyUniverse.

NOT SHOWN AS WRITTEN: the save file (universe_save_the_kestrel_verge_1.yaml) is drawn as a
card from the page's words, because no state holds a real save; and mast.runtime.log is a
card of the two things the page says it can name. Replace them with real stills if wanted.

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine by the
person, NEVER by a script: an Open Universe run writes a save. ONE game, TWO windows:
`sbs run server,helm,comms -m MyUniverse map=0` on a probe copy of the example (state final).
Marks are left off every game still until the stills are taken. Never caption a face.
Press order:
  0. Before the game: the server's mission list with The Kestrel Verge in it: game_c52_list.
  1. Start. Helm at once: game_c52_card (the card naming Kestrel Relay with the line under it).
  2. Comms, select a station, Accept Cargo Run: game_c52_comms.
  3. Helm: the handheld icon, Quests, the run selected with Engage: game_c52_quests.
  4. Press Engage. On arrival: game_c52_arrived (the new system, the run paid).
  5. Quest Log, Charted Locations open with Kestrel Relay in it: game_c52_charted.
  6. Close the game. Start again with the same command: game_c52_resumed (the system the
     ship stopped in, 900 credits). Engage Kestrel Relay from Charted Locations; the card
     reads Kestrel Relay again (game_c52_card is reused).
  7. A second run with the typo state (one letter wrong on the display: line):
     game_c52_home_port (the card says Home Port, no Kestrel Relay).
"""
import os

LECTURE = "c5-02-your-universe-file"
TITLE = ("Class 5, Lecture 2", "Your universe file", "A title, a home port, and a game that can be continued")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
FILE = "kestrel_verge.amd"
MAST = "story.mast"

_EX = "c5-02-your-universe-file/example"
_HERE = os.path.dirname(os.path.abspath(__file__))


def _read(name):
    with open(os.path.join(_HERE, "..", "example", name), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


_AMD, _MAST = _read("kestrel_verge.amd"), _read("story.mast")

# The `ou` template's own words, put back into the page's finished files
_TITLE_NEW = ("# [The Kestrel Verge](kestrel_verge)\n---\nUniverse\nDisplay: The Kestrel Verge\n---\n"
              "Past the last relay the charts are forty years old, and nobody has come to correct them.\n"
              "Three colonies were planted out here. Two still answer.\n")
_TITLE_OLD = ("# [My Universe](my_universe)\n---\nUniverse\nDisplay: My Universe\n---\n"
              "A small frontier to build on. Two sides, a handful of jobs, and space to fill in.\n")
_SCEN = "\n## [Scenario](scenario)\n---\nMode: story\n---\n"
_LAND_AT = _AMD.index("\n## [Landmarks](landmarks)")
_LAND = _AMD[_LAND_AT:]
_DESC_NEW = ('" Past the last relay the charts are forty years old. Two colonies still answer.\n'
             '" Take work at Kestrel Relay and find out what happened to the third.\n')
_DESC_OLD = ('" Explore a procedurally generated frontier. Engage the jump drive on the Navigation\n'
             '" console to travel between systems - the same seed always regenerates the same galaxy.\n')
_T_AMD = _AMD[:_LAND_AT].replace(_TITLE_NEW + _SCEN, _TITLE_OLD)
_T_MAST = _MAST.replace("The Kestrel Verge", "My Universe").replace("kestrel_verge.amd", "my_universe.amd").replace(_DESC_NEW, _DESC_OLD)
_M_TITLE = _MAST.replace("kestrel_verge.amd", "my_universe.amd").replace(_DESC_NEW, _DESC_OLD)     # the title in four places done
_M_FILE = _MAST.replace(_DESC_NEW, _DESC_OLD)                                                      # and the file name

# the text of each state, for the line numbers of the marks
_TXT = {
    "start": (_T_AMD, _T_MAST),
    "renamed": (_T_AMD, _T_MAST),
    "titled": (_T_AMD.replace(_TITLE_OLD, _TITLE_NEW), _T_MAST),
    "scen": (_T_AMD.replace(_TITLE_OLD, _TITLE_NEW + _SCEN), _T_MAST),
    "land": (_AMD, _T_MAST),
    "mast_t": (_AMD, _M_TITLE),
    "mast_f": (_AMD, _M_FILE),
    "final": (_AMD, _MAST),
    "typo": (_AMD, _MAST.replace("display: The Kestrel Verge", "display: The Kestral Verge")),
}


def ln(state, needle, nth=1, mast=False):
    """The 1-based line of the nth line of a state's file (story.mast when mast) holding needle."""
    text = _TXT[state][1 if mast else 0]
    seen = 0
    for i, line in enumerate(text.split("\n"), 1):
        if needle in line:
            seen += 1
            if seen == nth:
                return i
    raise ValueError(f"{state}: {needle!r} is not in the file {nth} time(s)")


STATES = {
    # what `sbs create MyUniverse -t ou --title "The Kestrel Verge"` makes
    "start": {"folder": _EX, "edits": [("write", "my_universe.amd", _T_AMD), ("delete", "kestrel_verge.amd"),
                                       ("write", MAST, _T_MAST)]},
    # Step 3: the file renamed
    "renamed": {"base": "start", "edits": [("delete", "my_universe.amd"), ("write", FILE, _T_AMD)]},
    # Step 4: the title record; Step 5: the Scenario chapter; Step 6: the Landmarks chapter
    "titled": {"base": "renamed", "edits": [("replace", FILE, _TITLE_OLD, _TITLE_NEW)]},
    "scen": {"base": "titled", "edits": [("replace", FILE, _TITLE_NEW, _TITLE_NEW + _SCEN)]},
    "land": {"base": "scen", "edits": [("append", FILE, _LAND)], "same_as": (_EX + "/kestrel_verge.amd",)},
    # Step 7: story.mast, the title in four places, the file name in two, the two lines
    "mast_t": {"base": "land", "edits": [("write", MAST, _M_TITLE)]},
    "mast_f": {"base": "mast_t", "edits": [("write", MAST, _M_FILE)]},
    "final": {"base": "mast_f", "edits": [("write", MAST, _MAST)],
              "same_as": (_EX + "/kestrel_verge.amd", _EX + "/story.mast", _EX + "/description.yaml")},
    # Step 8: one letter of the title on the display: line only
    "typo": {"base": "final", "edits": [("replace", MAST, "display: The Kestrel Verge", "display: The Kestral Verge")]},
}

_CREATE = 'sbs create MyUniverse -t ou --title "The Kestrel Verge"'
_FETCH = 'sbs fetch "MyUniverse" --update-libs'
_LINT = "sbs lint MyUniverse"
_NO = {"without": ("MyUniverse",)}
_MAKE = [(_CREATE, ("",)), _FETCH, _LINT]
_NS = {"side": False}
_MS = {"file": MAST, "side": False}
_DY = {"file": "description.yaml", "side": False}
_OLD = {"file": "my_universe.amd", "side": False}

# where the marks are (worked out from the states)
_HEAD = ln("scen", "# [The Kestrel Verge]")                  # 13: the title record's heading
_DISP = ln("scen", "Display:")
_SC = ln("scen", "## [Scenario]")
_MODE = ln("scen", "Mode:")
_LH = ln("land", "## [Landmarks]")
_LK = ln("land", "### [Kestrel Relay]")
_LAT = ln("land", "At: 0, 0")
_LPR = ln("land", "Prefab: station")
_LTX = ln("land", "The last relay anyone")
_M_DEF = ln("start", 'default shared UNIVERSE_SELECT = "My', mast=True)
_M_MAP = ln("start", "@map/my_universe", mast=True)
_M_D1 = _M_MAP + 1                                                 # the first of the two start-screen lines
_M_DISP = ln("start", "display: My Universe", mast=True)
_M_UNI = ln("start", "universe: my_universe.amd", mast=True)
_M_LAST = ln("start", '    UNIVERSE_SELECT = "My Universe"', mast=True)
_M_ENG = ln("start", "default shared QUEST_ENGAGE_ENABLED", mast=True)
_M_WAY = ln("start", "default shared WAYPOINTS_ENABLED", mast=True)

STILLS = {
    # The editor. A still shows 21 lines: the one named, ten above and ten below
    "e_folder": ("vscode", "start", 15, "mid", {"file": "my_universe.amd"}),            # the Side Bar: the files of the new folder
    "e_tpl": ("vscode", "start", 15, "big", dict(_OLD, **_NS)),                         # my_universe.amd as the template made it
    "e_mast_top": ("vscode", "start", _M_DEF, "big", _MS),                              # the template's names in story.mast
    "e_desc": ("vscode", "start", 11, "big", _DY),                                      # description.yaml, the title already in it
    "e_rename": ("vscode", "renamed", 15, "mid", {"file": FILE}),                        # the file under its new name, in the Side Bar
    "e_title_old": ("vscode", "renamed", 16, "big", _NS),                               # the title record as the template made it
    "e_title": ("vscode", "titled", 16, "big", _NS),                                    # the title record written
    "e_scen": ("vscode", "scen", _MODE, "big", _NS),                                    # the Scenario chapter
    "e_land": ("vscode", "land", _LK + 3, "big", _NS),                                  # the Landmarks chapter, at the end of the file
    "e_m_old": ("vscode", "mast_f", _M_MAP, "big", _MS),                                # the map line, display:, the last UNIVERSE_SELECT
    "e_m_new": ("vscode", "mast_t", (_M_DISP + _M_MAP) // 2, "big", _MS),                                # the title in four places
    "e_m_file": ("vscode", "mast_f", _M_UNI, "big", _MS),                               # universe: kestrel_verge.amd
    "e_m_desc_old": ("vscode", "mast_f", _M_D1 + 1, "big", _MS),                        # the template's two description lines
    "e_m_desc": ("vscode", "final", _M_D1 + 1, "big", _MS),                             # the two lines written
    "e_m_travel": ("vscode", "final", _M_ENG, "big", _MS),                              # the two lines that let the crew travel
    "e_m_final": ("vscode", "final", (_M_DISP + _M_MAP) // 2, "big", _MS),                               # the finished map line, display:, last UNIVERSE_SELECT
    "e_typo": ("vscode", "typo", _M_DISP, "big", _MS),                                  # one letter wrong on the display: line
    "e_title_f": ("vscode", "final", 16, "big", _NS),                                   # the finished title record (cold open)
    "e_land_f": ("vscode", "final", _LK + 3, "big", _NS),                               # the finished Landmarks chapter (cold open)
    # the command prompt, one real session for the first three
    "t_prompt": ("session", [], _NO),
    "t_create": ("session", _MAKE, dict(_NO, show=(1, 1))),
    "t_fetch": ("session", _MAKE, dict(_NO, show=(2, 2), tail=14)),
    "t_lint_new": ("session", _MAKE, dict(_NO, show=(3, 3))),
    "t_clean": ("terminal", [("final", _LINT)]),
    "t_typo": ("terminal", [("typo", _LINT)]),
    "t_run": ("session", ["sbs run server,helm,comms -m MyUniverse map=0 --dry-run"], {"state": "final"}),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm,comms
    "game_c52_list": ("game", "The server's mission list with The Kestrel Verge in it"),
    "game_c52_card": ("game", "Helm at the start: the card naming Kestrel Relay with 'The last relay anyone keeps lit. Past it is rumor.' under the name"),
    "game_c52_comms": ("game", "Comms with a station selected: Accept Cargo Run among its buttons"),
    "game_c52_quests": ("game", "Helm's Quest Log with the cargo run selected: the Engage button in view"),
    "game_c52_arrived": ("game", "Helm after the jump: the new system, the cargo run paid"),
    "game_c52_charted": ("game", "Helm's Quest Log, Charted Locations open with Kestrel Relay in it"),
    "game_c52_resumed": ("game", "The second start of the game: the ship in the system it stopped in, with the pay from the run"),
    "game_c52_home_port": ("game", "State typo: Helm at the start with the card reading Home Port, and no Kestrel Relay anywhere"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_modes": ("card", "table", {"heading": "Step 5 - The scenario", "nth": 1, "kicker": "What Mode says"}),
    "card_find_title": ("card", "search", {"state": "land", "word": "My Universe", "want": (4, 1), "kicker": "Search the folder"}),
    "card_find_file": ("card", "search", {"state": "mast_t", "word": "my_universe.amd", "want": (2, 1), "kicker": "Search the folder"}),
    "card_log": ("card", "rows", {"kicker": "mast.runtime.log, when the universe could not be loaded", "header": ["It names", "Then"],
                                  "rows": [["A file called sides.amd", "The title is spelled two ways"],
                                           ["Your own file", "The name after universe: is wrong, or the file was never renamed"]]}),
    "card_save": ("card", "rows", {"kicker": "universe_save_the_kestrel_verge_1.yaml", "header": ["Find", "What it holds"],
                                   "rows": [["The file's name", "Your title in small letters with underscores, then _1"],
                                            ["current_system", "The two numbers of the system you stopped in"],
                                            ["side_credits", "900: the 500 you start with and the 400 the run paid"]]}),
    "card_facts": ("card", "table", {"heading": "Step 9 - Play it", "nth": 1, "kicker": "What you need to know about the save"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Make the universe yours"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 3", "sub": "Sides, diplomacy and goods"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_title_f"},
        {"from": 3, "still": "game_c52_card"},
        {"from": 5, "still": "card_save", "marks": [("part", "r1")]},
        {"from": 6, "still": "e_land_f", "marks": [("lines", _LK, _LK + 6)]},
        {"from": 7, "still": "e_m_desc", "marks": [("lines", _M_D1, _M_D1 + 1)]},
    ]},
    "s02_make_the_mission": {"step": 1, "beats": [
        {"from": 0, "still": "t_prompt"},
        {"from": 1, "still": "t_create", "marks": [("cmd", 1, "-t ou")]},
        {"from": 4, "still": "t_create", "marks": [("cmd", 1, "MyUniverse")]},
        {"from": 6, "still": "t_fetch"},
        {"from": 7, "still": "t_lint_new", "marks": [("part", "run1:cmd")]},
        {"from": 8, "still": "t_lint_new", "marks": [("part", "run1:clean")]},
        {"from": 10, "still": "e_tpl", "marks": [("lines", 13, 18)]},
    ]},
    "s03_what_s_in_the_folder": {"step": 2, "beats": [
        {"from": 0, "still": "e_folder"},
        {"from": 1, "still": "e_tpl", "marks": [("lines", 13, 18)]},
        {"from": 2, "still": "e_mast_top", "marks": [("lines", _M_DEF, _M_DEF)]},
        {"from": 3, "still": "e_desc", "marks": [("text", 11, "Visible Mission Name: The Kestrel Verge")]},
        {"from": 5, "still": "e_folder"},
    ]},
    "s04_name_the_file_and_the_title_": {"step": 3, "beats": [
        {"from": 0, "still": "e_rename"},
        {"from": 1, "still": "e_title_old", "marks": [("lines", 13, 18)]},
        {"from": 2, "still": "e_title", "marks": [("hashes", _HEAD)]},
        {"from": 3, "still": "e_title", "marks": [("text", _HEAD, "# [The Kestrel Verge](kestrel_verge)")]},
        {"from": 4, "still": "e_title", "marks": [("lines", _DISP - 1, _DISP - 1)]},
        {"from": 6, "still": "e_title", "marks": [("lines", _DISP + 2, _DISP + 3)]},
        {"from": 8, "still": "e_title", "marks": [("lines", _HEAD, _DISP + 3)], "dim": True},
    ]},
    "s05_the_scenario": {"step": 5, "beats": [
        {"from": 0, "still": "e_scen", "marks": [("hashes", _SC)]},
        {"from": 1, "still": "e_scen", "marks": [("lines", _MODE, _MODE)]},
        {"from": 3, "still": "card_modes", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_modes", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_modes", "marks": [("part", "r3")]},
        {"from": 6, "still": "card_modes"},
        {"from": 8, "still": "e_scen", "marks": [("text", _SC, "(scenario)")]},
    ]},
    "s06_a_front_door": {"step": 6, "beats": [
        {"from": 0, "still": "e_land"},
        {"from": 1, "still": "e_land", "marks": [("hashes", _LH)]},
        {"from": 2, "still": "e_land", "marks": [("hashes", _LK)]},
        {"from": 3, "still": "e_land", "marks": [("text", _LAT, "At:")]},
        {"from": 4, "still": "e_land", "marks": [("text", _LAT, "0, 0")]},
        {"from": 5, "still": "e_land", "marks": [("lines", _LK, _LTX)]},
        {"from": 6, "still": "game_c52_card"},
        {"from": 8, "still": "game_c52_comms"},
        {"from": 9, "still": "game_c52_charted"},
        {"from": 11, "still": "e_land", "marks": [("lines", _LTX, _LTX)]},
        {"from": 13, "still": "e_land", "marks": [("text", _LTX, "The last relay anyone keeps lit. Past it is rumor.")]},
    ]},
    "s07_the_story_file": {"step": 7, "beats": [
        {"from": 0, "still": "e_mast_top", "marks": [("text", _M_DEF, "My Universe")]},
        {"from": 2, "still": "card_find_title", "marks": [("part", "word")]},
        {"from": 3, "still": "e_m_new", "marks": [("text", _M_MAP, "The Kestrel Verge"), ("text", _M_DISP, "The Kestrel Verge")]},
        {"from": 4, "still": "card_find_file", "marks": [("part", "word")]},
        {"from": 5, "still": "e_m_file", "marks": [("text", _M_UNI, "kestrel_verge.amd")]},
        {"from": 6, "still": "card_find_file", "marks": [("part", "summary")]},
        {"from": 8, "still": "e_m_desc_old", "marks": [("lines", _M_D1, _M_D1 + 1)]},
        {"from": 10, "still": "e_m_desc", "marks": [("lines", _M_D1, _M_D1 + 1)]},
        {"from": 11, "still": "e_m_travel", "marks": [("lines", _M_ENG, _M_WAY)]},
        {"from": 12, "still": "e_m_travel", "marks": [("lines", _M_ENG, _M_ENG)]},
        {"from": 13, "still": "e_m_travel", "marks": [("lines", _M_WAY, _M_WAY)]},
    ]},
    "s08_check_it": {"step": 8, "beats": [
        {"from": 0, "still": "t_clean", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_typo"},
        {"from": 2, "still": "e_typo", "marks": [("text", _M_DISP, "Kestral")]},
        {"from": 3, "still": "t_typo", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "game_c52_home_port"},
        {"from": 7, "still": "e_m_final", "marks": [("text", _M_MAP, "The Kestrel Verge"), ("text", _M_DISP, "The Kestrel Verge")]},
        {"from": 8, "still": "card_log"},
        {"from": 10, "still": "e_m_final", "marks": [("text", _M_DISP, "The Kestrel Verge")]},
    ]},
    "s09_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_c52_card"},
        {"from": 1, "still": "game_c52_comms"},
        {"from": 3, "still": "game_c52_quests"},
        {"from": 5, "still": "game_c52_arrived"},
        {"from": 7, "still": "game_c52_charted"},
    ]},
    "s10_the_save_and_coming_back": {"step": 9, "beats": [
        {"from": 0, "still": "card_save"},
        {"from": 1, "still": "card_save", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_save", "marks": [("part", "r2")]},
        {"from": 3, "still": "t_run", "marks": [("cmd", 1, "map=0")]},
        {"from": 4, "still": "game_c52_resumed"},
        {"from": 5, "still": "game_c52_card"},
        {"from": 6, "still": "card_facts"},
        {"from": 7, "still": "card_facts", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_facts", "marks": [("part", "r2")]},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 4, "still": "card_next"},
    ]},
}
