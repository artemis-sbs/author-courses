"""Storyboard for c5-15-admiral-part-2: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py (2026-10-18).

The lecture starts from Lecture 13's `MyUniverse`: Lecture 9's files with c5-12's three files and
c5-13's story.mast laid over them (the page says `kestrel_verge.amd` and `settings.yaml` match
c5-12, `story.mast` matches c5-13). The mission also holds a `story.json` that the Cosmos
template ships with both libraries; the c5-02 to c5-13 example folders do not hold it, so the
state brings c5-10's example copy ("start"). Then the two steps in the video's order: the mode
(`Mode: story` -> `Mode: campaign`, "mode") and the four chapters appended at the end of
kestrel_verge.amd ("chapters", the page's own example, `same_as`). Lines are looked up (_ln).

NOT SHOWN AS WRITTEN: the page's long tables of mistakes, and the `story.json` comma break
(not in the narration). Scene 3 shows `story.json` as it is, unchanged: the page says to leave
it alone if it has both lines.

GAME STILLS. NOT TAKEN YET: planned here, to be taken in one sitting in the real engine. Open
Universe probe: built in data/missions/_sandbox, saves backed up and restored by game.py;
never start the game by hand for it. NOTE: the page says nobody has seen the Admiral console,
so this is the first sitting that does. ONE game, FOUR windows:
`python game.py c5-15-admiral-part-2 start --state chapters --consoles server,admiral,helm,comms`
(seed=7, no probe patch). Marks are left off every game still until the stills are taken.
Press order:
  1. Helm, at once: the handheld icon, Quests: game_c15_helm (the three leads in the Quest Log,
     the credits at 500). Take it before anything else is pressed; it is also the cold-open shot
     and the proof in scene 7 that the bridge did not change.
  2. Admiral window, at once: game_c15_admiral (the home system from above, Kestrel Relay's
     system, Hollin Prime the one world) and game_c15_home (Hollin Prime selected, the pools at
     3,600 ore, 1,200 gas, 480 crew showing).
  3. Select Hollin Prime: game_c15_hq (the button "Build Headquarters (150 ore, 15 crew)").
     Press it, wait half a minute.
  4. Select it again, build an Extractor, an Academy, a Shipyard and a Lab, wait 45 seconds:
     game_c15_platforms (all four standing, ore climbing).
  5. Select the Shipyard: game_c15_shipyard (one button, "Commission Commodore Ilse Maren - the
     Harbormaster"; do not caption any face). Press it: game_c15_fleet (three ships formed at
     the Shipyard).
  6. Select the Lab: game_c15_lab1 ("Research Deeper Silos [engineering]"). Press it, wait 41
     seconds, select the Lab again: game_c15_lab2 ("Research Hot Drills [engineering]" offered).
  7. Close every window. Start again with the same line (do not delete the save), wait 20
     seconds: game_c15_continue (Admiral console, the platforms standing, the ore rising).
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


LECTURE = "c5-15-admiral-part-2"
TITLE = ("Class 5, Lecture 15", "The Admiral, part 2", "An Admiral alongside a bridge crew")
MISSION = "MyUniverse"
FILE = "kestrel_verge.amd"
MAST = "story.mast"
TEMPLATE = "ou"

_EX = "c5-15-admiral-part-2/example"
_OVER = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1", "c5-13-battles-part-2"))

_A0 = _rd("c5-12-battles-part-1", "example", "kestrel_verge.amd")
_F = _rd("c5-15-admiral-part-2", "example", "kestrel_verge.amd")
_CH = _F[_F.index("\n## [Worldlets](worldlets)"):]
_SJ = _rd("c5-10-a-boarding-site-on-the-map", "example", "story.json")
_A1 = _A0.replace("Mode: story\n", "Mode: campaign\n")

# story.json
_J_LIB = _ln(_SJ, '"mastlib": [')
_J_UC = _ln(_SJ, "universe_core")
_J_AD = _ln(_SJ, "admiral.v1.4.0")
# kestrel_verge.amd
_SCN = _ln(_A0, "## [Scenario](scenario)")
_MODE0 = _ln(_A0, "Mode: story")
_MODE1 = _ln(_A1, "Mode: campaign")
_END0 = _A0.rstrip("\n").count("\n") + 1
_WL = _ln(_F, "## [Worldlets](worldlets)")
_HPH = _ln(_F, "### [Hollin Prime](hollin_prime)")
_HPR = _ln(_F, "Reserve: unlimited")
_LAMP = _ln(_F, "### [The Lamp](the_lamp)")
_LAMPR = _ln(_F, "Reserve: 6000")
_LAMPE = _ln(_F, "The banded giant the relay was named for.")
_ADMH = _ln(_F, "## [Admiralty](admiralty)")
_ADMD = _ln(_F, "Command points: 2")
_MAR = _ln(_F, "### [Commodore Ilse Maren](maren)")
_MARE = _ln(_F, "Thirty years of freight schedules")
_RES = _ln(_F, "## [Research](research)")
_S1 = _ln(_F, "### [Deeper Silos](silos)")
_S2 = _ln(_F, "### [Hot Drills](hot_drills)")
_S2E = _ln(_F, "Every extractor works a quarter again as fast.")
_HOME = _ln(_F, "Home: 0, 0")
_WIN = _ln(_F, "Win: The Bone Pile is broken")

STATES = {
    # Lecture 13's files, with story.json (the template ships it with the Admiral's library)
    "start": {"folder": "c5-02-your-universe-file/example", "over": _OVER,
              "edits": [("write", "story.json", _SJ)]},
    # Step 3: one word in the Scenario chapter
    "mode": {"base": "start", "edits": [("replace", FILE, "Mode: story\n", "Mode: campaign\n")]},
    # Step 4: the four chapters at the end of the file. The page's own example.
    "chapters": {"base": "mode", "edits": [("append", FILE, _CH)], "same_as": (_EX + "/kestrel_verge.amd",)},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}
_JS = {"file": "story.json", "side": False}

STILLS = {
    # The editor. Each window shows the 21 lines round the line named.
    "e_json": ("vscode", "start", 20, "big", _JS),                 # story.json, the libraries (lines 10 to 30)
    "e_mode0": ("vscode", "start", _MODE0, "big", _NS),            # the Scenario chapter, Mode: story
    "e_mode1": ("vscode", "mode", _MODE1, "big", _NS),             # Mode: campaign
    "e_end15": ("vscode", "mode", _END0 - 3, "big", _NS),          # the end of the Dialogue chapter, before the paste
    "e_ch1": ("vscode", "chapters", _LAMP - 1, "big", _NS),        # Worldlets: Hollin Prime and The Lamp
    "e_ch2": ("vscode", "chapters", _MAR, "big", _NS),             # Admiralty and Officers
    "e_ch3": ("vscode", "chapters", _S2 - 1, "big", _NS),          # Research
    "e_home": ("vscode", "chapters", _HOME, "big", _NS),           # the Compact's Home: 0, 0
    "e_goal": ("vscode", "chapters", _WIN, "big", _NS),            # the goal's Win: line
    # the command prompt
    "t_lint": ("terminal", [("chapters", _LINT)]),
    "t_run": ("session", ["sbs run server,admiral,helm,comms -m MyUniverse map=0 --dry-run"], {"state": "chapters"}),
    "t_run2": ("session", ["sbs run server,helm,comms,weapons -m MyUniverse map=0 --dry-run"], {"state": "chapters"}),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c15_admiral": ("game", "The Admiral console looking down on Kestrel Relay's system, Hollin Prime in view"),
    "game_c15_helm": ("game", "Helm, the Quest Log open: the three leads, the credits at 500"),
    "game_c15_home": ("game", "Hollin Prime selected, the pools showing 3,600 ore, 1,200 gas and 480 crew"),
    "game_c15_hq": ("game", "Hollin Prime selected: the single button 'Build Headquarters (150 ore, 15 crew)'"),
    "game_c15_platforms": ("game", "Hollin Prime with an Extractor, an Academy, a Shipyard and a Lab standing, the ore climbing"),
    "game_c15_shipyard": ("game", "The Shipyard selected: one button 'Commission Commodore Ilse Maren - the Harbormaster'"),
    "game_c15_fleet": ("game", "The Admiral console: a fleet of three ships formed at the Shipyard, holding"),
    "game_c15_lab1": ("game", "The Lab selected: one button 'Research Deeper Silos [engineering]'"),
    "game_c15_lab2": ("game", "The Lab selected after the first step is done: 'Research Hot Drills [engineering]' is offered"),
    "game_c15_continue": ("game", "The Admiral console after Continue and twenty seconds: the five platforms standing, the ore rising again"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_three": ("card", "table", {"heading": "Step 1 - Three things switch it on", "nth": 1, "kicker": "Three things switch the Admiral on"}),
    "card_left": ("card", "table", {"heading": "Step 1 - Three things switch it on", "nth": 2, "kicker": "Each one left out in turn"}),
    "card_mult": ("card", "table", {"heading": "Step 5 - What the game does with your numbers", "nth": 1, "kicker": "What the game does with your numbers"}),
    "card_empty": ("card", "table", {"heading": "Step 8 - Play it with the Admiral's seat empty", "nth": 1, "kicker": "With the seat empty"}),
    "card_cont": ("card", "table", {"heading": "Step 10 - Stop, and Continue", "nth": 1, "kicker": "After Continue"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Write it, take it out, put it back"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 16", "sub": "A playable universe"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c15_admiral"},
        {"from": 3, "still": "game_c15_helm"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_three_things_switch_it_on": {"step": 1, "beats": [
        {"from": 0, "still": "card_three"},
        {"from": 3, "still": "card_three", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_three", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_three", "marks": [("part", "r3")]},
        {"from": 6, "still": "card_left"},
        {"from": 7, "still": "card_left", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 8, "still": "card_three"},
    ]},
    "s03_the_library_and_the_mode": {"step": 2, "beats": [
        {"from": 0, "still": "e_json"},
        {"from": 1, "still": "e_json", "marks": [("lines", _J_LIB + 5, _J_AD)]},
        {"from": 2, "still": "e_json", "marks": [("lines", _J_UC, _J_UC)]},
        {"from": 3, "still": "e_json", "marks": [("lines", _J_AD, _J_AD)]},
        {"from": 4, "still": "e_json", "marks": [("lines", _J_UC, _J_AD)]},
        {"from": 5, "still": "e_json", "marks": [("lines", _J_AD, _J_AD)]},
        {"from": 6, "still": "e_mode0", "marks": [("lines", _SCN, _MODE0)]},
        {"from": 7, "still": "e_mode0", "marks": [("text", _MODE0, "story")]},
        {"from": 8, "still": "e_mode1", "marks": [("text", _MODE1, "campaign")]},
    ]},
    "s04_the_chapters_come_home": {"step": 4, "beats": [
        {"from": 0, "still": "e_end15"},
        {"from": 1, "still": "e_end15", "marks": [("lines", _END0, _END0)]},
        {"from": 3, "still": "e_ch1", "marks": [("lines", _WL, _LAMPE)]},
        {"from": 4, "still": "e_ch1", "marks": [("text", _HPR, "Reserve: unlimited"), ("text", _LAMPR, "Reserve: 6000")]},
        {"from": 5, "still": "e_ch2", "marks": [("lines", _ADMH, _ADMD + 1)]},
        {"from": 6, "still": "e_ch2", "marks": [("lines", _MAR, _MARE)]},
        {"from": 7, "still": "e_ch3", "marks": [("lines", _S1, _S2E)]},
        {"from": 8, "still": "e_home", "marks": [("text", _HOME, "Home: 0, 0")]},
        {"from": 9, "still": "e_ch1", "marks": [("lines", _HPH, _HPH + 7)]},
        {"from": 10, "still": "e_ch1", "marks": [("text", _HPR, "Reserve: unlimited")]},
    ]},
    "s05_an_honest_number": {"step": 5, "beats": [
        {"from": 0, "still": "card_mult"},
        {"from": 1, "still": "card_mult", "marks": [("part", "r1c1")]},
        {"from": 2, "still": "card_mult", "marks": [("part", "r1c1")]},
        {"from": 3, "still": "card_mult", "marks": [("part", "r1c2")]},
        {"from": 4, "still": "card_mult", "marks": [("part", "r1c3")]},
        {"from": 5, "still": "card_mult", "marks": [("part", "r4c3")]},
        {"from": 7, "still": "card_mult", "marks": [("part", "r6"), ("part", "r7"), ("part", "r8"), ("part", "r9")]},
        {"from": 9, "still": "card_mult"},
        {"from": 10, "still": "card_mult", "marks": [("part", "r9")]},
    ]},
    "s06_lint": {"step": 6, "beats": [
        {"from": 0, "still": "t_lint"},
        {"from": 1, "still": "t_lint", "marks": [("span", 1, "0 error(s), 0 warning(s)")]},
    ]},
    "s07_both_seats_filled": {"step": 7, "beats": [
        {"from": 0, "still": "t_run", "marks": [("cmd", 1, "server,admiral,helm,comms")]},
        {"from": 1, "still": "game_c15_home"},
        {"from": 2, "still": "game_c15_hq"},
        {"from": 4, "still": "game_c15_platforms"},
        {"from": 6, "still": "game_c15_shipyard"},
        {"from": 7, "still": "game_c15_fleet"},
        {"from": 8, "still": "game_c15_lab1"},
        {"from": 9, "still": "game_c15_lab2"},
        {"from": 11, "still": "game_c15_helm"},
    ]},
    "s08_the_empty_seat": {"step": 8, "beats": [
        {"from": 0, "still": "card_empty"},
        {"from": 2, "still": "t_run2", "marks": [("cmd", 1, "server,helm,comms,weapons")]},
        {"from": 3, "still": "card_empty", "marks": [("part", "r4")]},
        {"from": 4, "still": "card_empty", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_empty", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_empty"},
    ]},
    "s09_how_it_ends_and_what_comes_b": {"step": 9, "beats": [
        {"from": 0, "still": "e_goal"},
        {"from": 2, "still": "e_goal", "marks": [("lines", _WIN - 5, _WIN - 5)]},
        {"from": 3, "still": "e_goal", "marks": [("text", _WIN, "Win: The Bone Pile is broken")]},
        {"from": 4, "still": "card_cont"},
        {"from": 5, "still": "card_cont", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_cont", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_cont", "marks": [("part", "r4"), ("part", "r5")]},
        {"from": 8, "still": "game_c15_continue"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 6, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 7, "still": "card_next"},
    ]},
}
