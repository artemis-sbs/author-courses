"""Storyboard for c5-14-admiral-part-1: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py (2026-10-18).

This lecture works in `AdmiralLab`, a COPY of the Open Universe mission, not in MyUniverse. The
only file the lecture changes is `skirmish_arena.amd`, and the page's example folder holds just
that file in its FINISHED form. The starting file ("start") is rebuilt from it by taking the
lecture's four additions out again: the Hollin Prime world, the three dial lines, Commodore
Maren and the Research chapter. The steps are typed in the video's order: "w_hollin" (the
world, scene 5), "dials" (scene 6), "maren" (scene 7), then "final" (the Research chapter,
scene 8; the page's own example, `same_as`). Lines are looked up in the text (_ln), never typed.

NOT SHOWN AS WRITTEN:
- Lint. The page's `sbs lint AdmiralLab` runs on the whole Open Universe folder (13 .amd files,
  two old warnings that are not the student's). The stand-in has only skirmish_arena.amd, so a
  real terminal would say something else. "card_lint" draws the page's own output in its place
  (rows of the page's output, the two warnings kept). Replace it only if a stand-in copy of
  the Open Universe mission is ever made.
- Nothing is shown of File Explorer for the copy and rename (scene 3): the stand-in does not
  hold the OpenUniverse folder. "card_lab" draws the page's four moves.

GAME STILLS. NOT TAKEN YET: planned here, for one sitting in the real engine. Open Universe
runs write the player's save (the Skirmish save, shared with the real Open Universe): the probe
must be a sandboxed copy and game.py must back the saves up. NOTE FOR THE SITTING: game.py makes
its probe from the `ou` template (TEMPLATE below), which does NOT register "Skirmish - The Broken
Accord"; the probe needs to be a copy of OpenUniverse with the state's skirmish_arena.amd laid
over it. Check that first. Also NOTE: the page says nobody has seen the Admiral console yet, so
this sitting is the first time. ONE game, TWO windows:
`python game.py c5-14-admiral-part-1 start --state final --consoles server,admiral`
Marks are left off every game still until the stills are taken. Press order:
  1. Server start screen: Universe = Skirmish - The Broken Accord, Start = New Game:
     game_c14_start. Start the mission.
  2. Admiral window, at once: game_c14_home (the home system from above, Hollin Prime the one
     world, the pools showing 6,000 ore).
  3. Select Hollin Prime: game_c14_hq (the button "Build Headquarters (150 ore, 15 crew)").
     Press it, wait half a minute.
  4. Select it again, build an Extractor, an Academy, a Shipyard and a Lab, wait 45 seconds:
     game_c14_platforms (all four standing, the ore climbing).
  5. Select the Shipyard: game_c14_shipyard (the first button reads "Commission Commodore Ilse
     Maren - the Harbormaster"; do not caption any face). Press it and let the fleet form:
     game_c14_fleet (three ships at the Shipyard; the same still is used in the cold open with
     game_c14_admiral, which is the same sitting's first wide view of a system from above).
  6. Select the Lab: game_c14_lab1 ("Research Deeper Silos [engineering]" is the only button).
     Press it, wait 41 seconds, select the Lab again: game_c14_lab2 (Hot Drills now offered).
  7. game_c14_helm is a separate, short Helm sitting (any mission with a ship): the bridge seen
     from one ship, for the contrast in the cold open.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.join(_HERE, "..", "..")


def _rd(*parts):
    with open(os.path.join(_ROOT, *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


def _ln(text, needle, nth=1):
    """The 1-based line of the nth place `needle` starts in text."""
    at = -1
    for _ in range(nth):
        at = text.index(needle, at + 1)
    return text.count("\n", 0, at) + 1


LECTURE = "c5-14-admiral-part-1"
TITLE = ("Class 5, Lecture 14", "The Admiral, part 1", "The game from above: worlds, dials, an officer and a ladder")
MISSION = "AdmiralLab"
FILE = "skirmish_arena.amd"
MAST = "story.mast"
TEMPLATE = "ou"

_EX = "c5-14-admiral-part-1/example"

# The finished file, and the four additions taken back out of it
_F = _rd("c5-14-admiral-part-1", "example", "skirmish_arena.amd")
_HP = _F[_F.index("### [Hollin Prime]"):_F.index("### [Cinder World]")]
_MA = _F[_F.index("### [Commodore Ilse Maren]"):_F.index("### [Commodore Ansel Vale]")]
_RES = _F[_F.index("\n## [Research]"):]
_DIALS = "Start ore: 500\nCommand points: 2\nSkirmish pressure: none\n"
_T3 = _F.replace(_RES, "")                                                       # Maren in, no Research
_T2 = _T3.replace(_MA, "")                                                       # dials in, no Maren
_T1 = _T2.replace(_DIALS, "")                                                    # world in, no dials
_T0 = _T1.replace(_HP, "")                                                       # as the page opens it

# lines
_WLD0 = _ln(_T0, "## [Worldlets](worldlets)")
_CIN0 = _ln(_T0, "### [Cinder World](cinder)")
_VEI0 = _ln(_T0, "### [Veiled Giant](veiled_giant)")
_HAV0 = _ln(_T0, "### [Haven World](haven)")
_HP1 = _ln(_T1, "### [Hollin Prime](hollin_prime)")
_HP1E = _ln(_T1, "The world the Compact farms")
_YI = _ln(_T1, "Yields: crew 3, ore 4, gas 1")
_RS = _ln(_T1, "Reserve: unlimited")
_DS = _ln(_T2, "Start ore: 500")
_DC = _ln(_T2, "Command points: 2")
_DP = _ln(_T2, "Skirmish pressure: none")
_ADM = _ln(_T2, "## [Admiralty](admiralty)")
_MH = _ln(_T3, "### [Commodore Ilse Maren](maren)")
_MV = _ln(_T3, "Values: by-the-book 40, honest 30\n")
_MP = _ln(_T3, "Thirty years of freight schedules")
_T3END = _T3.rstrip("\n").count("\n") + 1
_RH = _ln(_F, "## [Research](research)")
_S1 = _ln(_F, "### [Deeper Silos](silos)")
_S1T = _ln(_F, "Time: 40")
_S1C = _ln(_F, "Costs: ore 120, gas 40")
_S1U = _ln(_F, "Unlocks: storage 500")
_S2 = _ln(_F, "### [Hot Drills](hot_drills)")
_S2R = _ln(_F, "Requires: silos")
_S2E = _ln(_F, "Every extractor works a quarter again as fast.")

STATES = {
    # The file as the page opens it: the arena without the four additions
    "start": {"folder": _EX, "edits": [("write", FILE, _T0)]},
    # Step 4: Hollin Prime above Cinder World
    "w_hollin": {"base": "start", "edits": [("write", FILE, _T1)]},
    # Step 5: three lines in the Admiralty fence
    "dials": {"base": "w_hollin", "edits": [("write", FILE, _T2)]},
    # Step 6: Commodore Ilse Maren above Commodore Ansel Vale
    "maren": {"base": "dials", "edits": [("write", FILE, _T3)]},
    # Step 7: the Research chapter at the end. The page's own example.
    "final": {"base": "maren", "edits": [("write", FILE, _F)], "same_as": (_EX + "/skirmish_arena.amd",)},
}

_NS = {"side": False}

STILLS = {
    # The editor. Each window shows the 21 lines round the line named.
    "e_arena0": ("vscode", "start", _VEI0 + 1, "big", _NS),       # the three kinds of world
    "e_arena1": ("vscode", "w_hollin", _HP1 + 3, "big", _NS),     # Hollin Prime added above Cinder World
    "e_dials": ("vscode", "dials", _DC, "big", _NS),              # the Admiralty fence with three lines more
    "e_maren": ("vscode", "maren", _MV, "big", _NS),              # Commodore Ilse Maren
    "e_end14": ("vscode", "maren", _T3END - 3, "big", _NS),       # the end of the file, before the Research chapter
    "e_res": ("vscode", "final", _S1 + 9, "big", _NS),            # the Research chapter, both steps
    # the command prompt
    "t_run": ("session", ["sbs run server,admiral -m AdmiralLab --dry-run"], {"state": "final"}),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c14_helm": ("game", "Helm, a ship's bridge view in a system: one ship, one crew (the contrast with the Admiral)"),
    "game_c14_admiral": ("game", "The Admiral console looking down on a whole system, a worldlet in view, no ship of the Admiral's own"),
    "game_c14_fleet": ("game", "The Admiral console: a fleet of three ships formed at the Shipyard, on the Admiral's side"),
    "game_c14_start": ("game", "The server start screen: Universe set to 'Skirmish - The Broken Accord', Start set to New Game"),
    "game_c14_home": ("game", "The Admiral console in the home system: one world, Hollin Prime, and the pools showing"),
    "game_c14_hq": ("game", "Hollin Prime selected: the single button 'Build Headquarters (150 ore, 15 crew)'"),
    "game_c14_platforms": ("game", "Hollin Prime with an Extractor, an Academy, a Shipyard and a Lab standing, the ore climbing"),
    "game_c14_shipyard": ("game", "The Shipyard selected: the first button reads 'Commission Commodore Ilse Maren - the Harbormaster'"),
    "game_c14_lab1": ("game", "The Lab selected: one button, 'Research Deeper Silos [engineering]'"),
    "game_c14_lab2": ("game", "The Lab selected after the first step is done: 'Research Hot Drills [engineering]' is offered"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_two": ("card", "table", {"heading": "Read this first: two lectures, two folders", "nth": 1, "kicker": "Two lectures, two folders"}),
    "card_chapters": ("card", "table", {"heading": "Step 3 - Read the arena file", "nth": 1, "kicker": "What is in the arena file"}),
    "card_lab": ("card", "points", {"kicker": "Step 1 - Make the lab",
                                    "items": ["Never change the OpenUniverse folder itself. An update replaces it.",
                                              "In File Explorer, go to C:\\Cosmos\\data\\missions. Copy the OpenUniverse folder and paste it beside itself.",
                                              "Rename the copy AdmiralLab.",
                                              "In VS Code, open the AdmiralLab folder."]}),
    "card_save": ("card", "rows", {"kicker": "A save is named after the universe, not the folder",
                                   "header": ["Universe", "Its save file"],
                                   "rows": [["Skirmish - The Broken Accord",
                                             "common_data\\saves\\universe_save_skirmish_the_broken_accord_1.yaml"]]}),
    "card_does": ("card", "table", {"heading": "Step 2 - What an Admiral does", "nth": 1, "kicker": "What an Admiral does"}),
    "card_plat": ("card", "table", {"heading": "Step 2 - What an Admiral does", "nth": 2, "kicker": "The platforms are the game's, not yours"}),
    "card_write": ("card", "rows", {"kicker": "What you write",
                                    "header": ["You write", "In the chapter"],
                                    "rows": [["The worlds", "Worldlets"], ["The dials", "Admiralty"],
                                             ["The people", "Officers"], ["The ladder", "Research"]]}),
    "card_home": ("card", "rows", {"kicker": "Which world is home: the first that never runs dry",
                                   "header": ["World", "Reserve", "Home?"],
                                   "rows": [["Hollin Prime", "unlimited", "Home, because it is first"],
                                            ["Cinder World", "4000", ""],
                                            ["Veiled Giant", "6000", ""],
                                            ["Haven World", "unlimited", "Home, before your change"]]}),
    "card_six": ("card", "rows", {"kicker": "What the lab did to the numbers",
                                  "header": ["You wrote", "The game used"],
                                  "rows": [["Start ore: 500", "6,000 ore at the start"],
                                           ["Storage: 600 (the game's own)", "The pools held 7,200"],
                                           ["Hollin Prime yields 4 ore a minute", "One Extractor there brought in 64"]]}),
    "card_mult": ("card", "table", {"heading": "Step 5 - The dials", "nth": 2, "kicker": "Multiplied today, in this lab"}),
    "card_traits": ("card", "table", {"heading": "Step 6 - An officer", "nth": 2, "kicker": "Three traits do something for a fleet"}),
    "card_lint": ("card", "rows", {"kicker": "sbs lint AdmiralLab: the page's own output (abridged)",
                                   "header": ["File", "Lint says"],
                                   "rows": [["cast\\frontier.amd", "WARNING line 30: `Patience` is not a field a lifeform has (unknown-field)"],
                                            ["dialogue\\ashfang.amd", "WARNING line 24: `ashfang_deal` emits signal `ashfang_paid` but no route was found (signal-no-route)"],
                                            ["skirmish_arena.amd", "clean"],
                                            ["13 amd + 14 mast file(s)", "0 error(s), 2 warning(s)"]]}),
    "card_moves": ("card", "table", {"heading": "Taking it to your own universe", "nth": 1, "kicker": "Three moves to bring it home"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your own world, officers and ladder"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 15", "sub": "An Admiral beside your bridge crew"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c14_helm"},
        {"from": 3, "still": "game_c14_admiral"},
        {"from": 5, "still": "game_c14_admiral"},
        {"from": 6, "still": "game_c14_fleet"},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_two_lectures_two_folders": {"step": None, "beats": [
        {"from": 0, "still": "card_two"},
        {"from": 1, "still": "card_two", "marks": [("part", "r1c3")]},
        {"from": 2, "still": "card_two", "marks": [("part", f"r{i}c3") for i in range(1, 5)]},
        {"from": 3, "still": "card_two", "marks": [("part", f"r{i}c2") for i in range(1, 5)]},
        {"from": 4, "still": "card_two", "marks": [("part", "r1c2")]},
        {"from": 5, "still": "card_two", "marks": [("part", "r2c2")]},
        {"from": 6, "still": "card_chapters", "marks": [("part", "r3"), ("part", "r6")]},
        {"from": 7, "still": "card_chapters"},
        {"from": 8, "still": "card_two", "marks": [("part", "r1c2")]},
        {"from": 9, "still": "card_two", "marks": [("part", "r1c3")]},
    ]},
    "s03_make_the_lab": {"step": 1, "beats": [
        {"from": 0, "still": "card_lab"},
        {"from": 1, "still": "card_lab", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_lab", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 4, "still": "card_save"},
        {"from": 5, "still": "card_save", "marks": [("part", "r1c1")]},
        {"from": 6, "still": "card_save", "marks": [("part", "r1c2")]},
        {"from": 7, "still": "card_save"},
    ]},
    "s04_what_an_admiral_does": {"step": 2, "beats": [
        {"from": 0, "still": "card_does"},
        {"from": 1, "still": "card_does", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 2, "still": "card_does", "marks": [("part", "r4")]},
        {"from": 4, "still": "card_does", "marks": [("part", "r5")]},
        {"from": 6, "still": "card_does", "marks": [("part", "r6")]},
        {"from": 7, "still": "card_does", "marks": [("part", "r8")]},
        {"from": 8, "still": "card_plat"},
        {"from": 10, "still": "card_write"},
    ]},
    "s05_a_world_of_your_own": {"step": 4, "beats": [
        {"from": 0, "still": "e_arena0"},
        {"from": 1, "still": "e_arena0", "marks": [("text", _CIN0, "### [Cinder World](cinder)"),
                                                    ("text", _VEI0, "### [Veiled Giant](veiled_giant)"),
                                                    ("text", _HAV0, "### [Haven World](haven)")]},
        {"from": 2, "still": "e_arena1", "marks": [("lines", _HP1, _HP1E)]},
        {"from": 3, "still": "e_arena1", "marks": [("text", _YI, "Yields: crew 3, ore 4, gas 1")]},
        {"from": 4, "still": "e_arena1", "marks": [("text", _RS, "Reserve: unlimited")]},
        {"from": 5, "still": "card_home"},
        {"from": 7, "still": "card_home", "marks": [("part", "r1")]},
        {"from": 8, "still": "e_arena1", "marks": [("lines", _HP1, _HP1E)]},
    ]},
    "s06_dials_and_an_honest_number": {"step": 5, "beats": [
        {"from": 0, "still": "e_dials", "marks": [("lines", _DS, _DP)]},
        {"from": 1, "still": "e_dials", "marks": [("text", _DS, "Start ore: 500")]},
        {"from": 2, "still": "e_dials", "marks": [("text", _DC, "Command points: 2")]},
        {"from": 3, "still": "e_dials", "marks": [("text", _DP, "Skirmish pressure: none")]},
        {"from": 4, "still": "e_dials", "marks": [("text", _DS, "Start ore: 500")]},
        {"from": 6, "still": "card_six", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_six"},
        {"from": 9, "still": "card_mult"},
        {"from": 12, "still": "e_dials", "marks": [("lines", _DS, _DP)]},
    ]},
    "s07_an_officer": {"step": 6, "beats": [
        {"from": 0, "still": "e_maren", "marks": [("lines", _MH, _MP)]},
        {"from": 1, "still": "e_maren", "marks": [("text", _MV, "Values: by-the-book 40, honest 30")]},
        {"from": 2, "still": "card_traits"},
        {"from": 3, "still": "card_traits", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_traits", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_traits", "marks": [("part", "r3")]},
        {"from": 6, "still": "e_maren", "marks": [("text", _MV, "honest 30")]},
        {"from": 8, "still": "e_maren", "marks": [("lines", _MP, _MP)]},
    ]},
    "s08_research": {"step": 7, "beats": [
        {"from": 0, "still": "e_end14", "marks": [("lines", _T3END, _T3END)]},
        {"from": 1, "still": "e_res", "marks": [("lines", _S1, _S1), ("lines", _S2, _S2)]},
        {"from": 2, "still": "e_res", "marks": [("text", _S1C, "Costs:"), ("text", _S1T, "Time:"), ("text", _S1U, "Unlocks:")]},
        {"from": 3, "still": "e_res", "marks": [("text", _S2R, "Requires: silos")]},
        {"from": 4, "still": "e_res", "marks": [("lines", _S2, _S2E)]},
        {"from": 5, "still": "card_lint"},
        {"from": 6, "still": "card_lint", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 8, "still": "card_lint", "marks": [("part", "r4")]},
        {"from": 9, "still": "card_lint", "marks": [("part", "r3")]},
        {"from": 10, "still": "e_res", "marks": [("text", _S1T, "Time: 40")]},
        {"from": 13, "still": "card_lint", "marks": [("part", "r1"), ("part", "r2"), ("part", "r4")]},
    ]},
    "s09_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "t_run", "marks": [("cmd", 1, "server,admiral")]},
        {"from": 1, "still": "game_c14_start"},
        {"from": 2, "still": "game_c14_home"},
        {"from": 3, "still": "game_c14_hq"},
        {"from": 4, "still": "game_c14_platforms"},
        {"from": 6, "still": "game_c14_shipyard"},
        {"from": 7, "still": "game_c14_lab1"},
        {"from": 8, "still": "game_c14_lab2"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3"), ("part", "item4")]},
        {"from": 3, "still": "card_exercise"},
        {"from": 5, "still": "card_moves"},
        {"from": 7, "still": "card_moves", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 8, "still": "card_next"},
    ]},
}
