"""Storyboard for c4-02-a-ruin-is-a-place: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and Class 3's. Caption numbers are those of shots.py (2026-10-17).

The lecture starts from Lecture 1's hand-over: `MyRuin` as `sbs create` made it, the
borrowed ruin given back ("start": 60 lines, `relics_spawn` on line 62 of story.mast).
The Relics section is typed in steps, each state the first lines of the page's own
example\\mission.amd (92 lines): the heading and the ruin ("t_sec", "t_hollow", to line 69),
The Mouth (to 76), The Nave (to 84), The Vault ("final", to 92). Lint's breaks are one
change each on "final" ("b_crypt", "b_four", "b_noloc"); the exercise's Gallery is three
states ("g_box" overlapping The Nave, "g_far" moved away, "g_pass" joined by a passage).

NOT SHOWN AS WRITTEN: the Relic Plan (the VS Code panel, Artemis AMD: Show Relic Plan) is
a webview and the picture tools have no still for it, and the command palette is a key press.
"card_plan" stands in for it: a table of the three rooms with the numbers the plan would
draw (in the page's own words). Replace it with a real capture of the panel once a still
kind exists for it (Top view; hover; click The Vault, r 800, Undo).

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine. ONE
game, TWO windows:
`python game.py c4-02-a-ruin-is-a-place start --state final --consoles server,helm`
(the page's run line, `sbs run server,helm -m MyRuin map=0`, on a probe copy of the example).
No probe patch. Marks are left off every game still until the stills are taken.
Press order:
  1. Helm, at once, the map zoomed out until the hulk and The Hollow are both on it:
     game_c2_map (the name The Hollow past the hulk, on the same line from the station).
  2. Fly to the name. The server window, the ship at the marker, in the middle of The Mouth:
     game_c2_mouth (rock all round, spaced well apart).
  3. Fly on through the passage into The Nave. The server window: game_c2_nave.
"""
import os

LECTURE = "c4-02-a-ruin-is-a-place"
TITLE = ("Class 4, Lecture 2", "A ruin is a place", "Three rooms and two passages, written down, drawn, and flown")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-02-a-ruin-is-a-place/example"
_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "..", "example", "mission.amd"), encoding="utf-8", newline="") as _fh:
    _LINES = _fh.read().replace("\r\n", "\n").splitlines(True)


def _upto(n):
    """The first n lines of the page's example (the file as the student has it at that step)."""
    return "".join(_LINES[:n])


_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hollow"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hollow")]
_GALLERY = ("\n### [The Gallery](gallery)\n---\nRelic: hollow\nBox: 3000, 0, -1600, 600, 400, 800\n---\n"
            "A built room, with flat walls and real corners. Somebody added this later.\n")

STATES = {
    # Lecture 1's hand-over: the mission as `sbs create` made it
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED},
    # Step 2: the section and the ruin
    "t_sec": {"base": "start", "edits": [("write", FILE, _upto(63))]},
    "t_hollow": {"base": "start", "edits": [("write", FILE, _upto(69))]},
    # Step 3, 4: The Mouth, The Nave, The Vault
    "t_mouth": {"base": "start", "edits": [("write", FILE, _upto(76))]},
    "t_nave": {"base": "start", "edits": [("write", FILE, _upto(84))]},
    "final": {"base": "start", "edits": [("write", FILE, _upto(92))], "same_as": (_EX + "/mission.amd",)},
    # Step 5: The Vault made 800 across from the panel (one line changes)
    "b_r800": {"base": "final", "edits": [("replace", FILE, "Chamber: 3000, 0, 2800, 700", "Chamber: 3000, 0, 2800, 800")]},
    # Step 7: the breaks lint names, one at a time
    "b_crypt": {"base": "final", "edits": [("replace", FILE, "Passage to: nave 300", "Passage to: crypt 300")]},
    "b_four": {"base": "final", "edits": [("replace", FILE, "### [The Vault](vault)", "#### [The Vault](vault)")]},
    "b_noloc": {"base": "final", "edits": [("replace", FILE, "Loc: 0, 0, 20000\n", "")]},
    # Exercise: a box that overlaps The Nave, moved away, then joined by a passage
    "g_box": {"base": "final", "edits": [("append", FILE, _GALLERY)]},
    "g_far": {"base": "g_box", "edits": [("replace", FILE, "Box: 3000, 0, -1600, 600, 400, 800", "Box: 3000, 0, -1900, 600, 400, 800")]},
    "g_pass": {"base": "g_far", "edits": [("replace", FILE, "Box: 3000, 0, -1900, 600, 400, 800\n", "Box: 3000, 0, -1900, 600, 400, 800\nPassage to: nave 300\n")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # VS Code, real. A still shows 21 lines: the one named, ten above and ten below
    "e_end0": ("vscode", "start", 55, "big", _NS),           # lines 45 to 60: the end of the file
    "e_sec": ("vscode", "t_sec", 63, "big", _NS),            # lines 53 to 73: the end of the file and the section heading
    "e_hollow": ("vscode", "t_hollow", 69, "big", _NS),      # lines 59 to 79: the ruin
    "e_mouth": ("vscode", "t_mouth", 76, "big", _NS),        # lines 66 to 86: The Mouth under the ruin
    "e_nave": ("vscode", "t_nave", 84, "big", _NS),          # lines 74 to 94: The Nave
    "e_final": ("vscode", "final", 82, "big", _NS),          # lines 72 to 92: The Mouth's fence, The Nave, The Vault
    "e_rooms": ("vscode", "final", 80, "big", _NS),          # lines 70 to 90: the three headings
    "e_loc": ("vscode", "final", 67, "big", _NS),             # lines 57 to 77: the ruin and its Loc line
    "e_r800": ("vscode", "b_r800", 89, "big", _NS),          # lines 79 to 92: the Vault at 800
    "e_crypt": ("vscode", "b_crypt", 90, "big", _NS),        # lines 80 to 92: the passage to crypt
    "e_four": ("vscode", "b_four", 86, "big", _NS),          # lines 76 to 92: four hashes on The Vault
    "e_noloc": ("vscode", "b_noloc", 67, "big", _NS),        # lines 57 to 77: the ruin with no Loc line
    "e_gbox": ("vscode", "g_box", 100, "big", _NS),          # lines 90 to 100: The Gallery, overlapping
    "e_gfar": ("vscode", "g_far", 100, "big", _NS),          # the Box line moved away
    "e_gpass": ("vscode", "g_pass", 100, "big", _NS),        # the passage line added
    "m_62": ("vscode", "final", 62, "big", _M),              # lines 52 to 72 of story.mast: relics_spawn on line 62
    # the command prompt
    "t_lint": ("terminal", [("final", _LINT)]),
    "t_crypt": ("terminal", [("b_crypt", _LINT)]),
    "t_four": ("terminal", [("b_four", _LINT)]),
    "t_noloc": ("terminal", [("b_noloc", _LINT)]),
    "t_split": ("terminal", [("g_far", _LINT)]),
    "t_pass": ("terminal", [("g_pass", _LINT)]),
    "t_run": ("session", ["sbs run server,helm -m MyRuin map=0 --dry-run"], {"state": "final"}),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm
    "game_c2_map": ("game", "Helm, the map at the start: the hulk, and past it on the same line from the station the name The Hollow"),
    "game_c2_mouth": ("game", "The server window, the ship at the marker in the middle of The Mouth: rock all round it, well apart, no wall"),
    "game_c2_nave": ("game", "The server window, the ship through the first passage and inside The Nave: a bigger field of rock"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_space": ("card", "table", {"heading": "Step 1 - You describe the space, not the walls", "kicker": "You write the hollow"}),
    # stand-in for the Relic Plan panel (see the docstring): the numbers it would draw
    "card_plan": ("card", "rows", {"kicker": "The Relic Plan: three rooms, two passages", "header": ["Room", "Where, from the ruin", "Radius"],
                                   "rows": [["The Mouth", "0, 0, 0", "900"],
                                            ["The Nave", "3000, 0, 0", "1100"],
                                            ["The Vault", "3000, 0, 2800", "700"]]}),
    "card_plan800": ("card", "rows", {"kicker": "The Relic Plan: The Vault made 800", "header": ["Room", "Where, from the ruin", "Radius"],
                                      "rows": [["The Mouth", "0, 0, 0", "900"],
                                               ["The Nave", "3000, 0, 0", "1100"],
                                               ["The Vault", "3000, 0, 2800", "800"]]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A fourth room, a built one"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 3", "sub": "Dressing a ruin"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "card_plan"},
        {"from": 3, "still": "game_c2_map"},
        {"from": 4, "still": "game_c2_mouth"},
        {"from": 5, "still": "e_final"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_space_not_walls": {"step": 1, "beats": [
        {"from": 0, "still": "card_space"},
        {"from": 1, "still": "card_space", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_space", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_space", "marks": [("part", "r3")]},
        {"from": 6, "still": "card_space"},
    ]},
    "s03_the_ruin_itself": {"step": 2, "beats": [
        {"from": 0, "still": "e_end0", "marks": [("lines", 59, 60)]},
        {"from": 1, "still": "e_sec", "marks": [("lines", 63, 63)]},
        {"from": 2, "still": "e_sec", "marks": [("text", 63, "(relics)")]},
        {"from": 4, "still": "e_hollow", "marks": [("lines", 65, 69)]},
        {"from": 5, "still": "e_hollow", "marks": [("text", 65, "[The Hollow](hollow)")]},
        {"from": 6, "still": "e_hollow", "marks": [("text", 67, "Loc: 0, 0, 20000")]},
        {"from": 7, "still": "e_hollow", "marks": [("lines", 67, 67)]},
        {"from": 10, "still": "e_hollow", "marks": [("lines", 69, 69)]},
    ]},
    "s04_the_first_room": {"step": 3, "beats": [
        {"from": 0, "still": "e_mouth", "marks": [("text", 71, "###")]},
        {"from": 1, "still": "e_mouth", "marks": [("lines", 71, 76)]},
        {"from": 3, "still": "e_mouth", "marks": [("text", 73, "Relic: hollow")]},
        {"from": 4, "still": "e_mouth", "marks": [("text", 73, "hollow")]},
        {"from": 5, "still": "e_mouth", "marks": [("text", 74, "Chamber:")]},
        {"from": 6, "still": "e_mouth", "marks": [("text", 74, "0, 0, 0")]},
        {"from": 8, "still": "e_mouth", "marks": [("text", 74, "900")]},
        {"from": 10, "still": "e_mouth", "marks": [("lines", 74, 74)]},
    ]},
    "s05_two_more_rooms_and_the_tunne": {"step": 4, "beats": [
        {"from": 0, "still": "e_nave", "marks": [("text", 81, "3000, 0, 0, 1100")]},
        {"from": 1, "still": "e_nave", "marks": [("text", 82, "Passage to: mouth 350")]},
        {"from": 3, "still": "e_nave", "marks": [("text", 82, "mouth")]},
        {"from": 4, "still": "e_nave", "marks": [("text", 82, "350")]},
        {"from": 5, "still": "e_nave", "marks": [("text", 82, "mouth 350")]},
        {"from": 6, "still": "e_final", "marks": [("text", 82, "Passage to:"), ("text", 90, "Passage to:")]},
        {"from": 7, "still": "e_final", "marks": [("text", 89, "3000, 0, 2800, 700")]},
        {"from": 8, "still": "e_final", "marks": [("text", 90, "Passage to: nave 300")]},
        {"from": 9, "still": "e_final", "marks": [("lines", 78, 92)]},
    ]},
    "s06_look_at_it": {"step": 5, "beats": [
        {"from": 0, "still": "e_final"},
        {"from": 2, "still": "card_plan"},
        {"from": 4, "still": "card_plan"},
        {"from": 7, "still": "card_plan800"},
        {"from": 8, "still": "e_r800", "marks": [("text", 89, "3000, 0, 2800, 800")]},
        {"from": 9, "still": "card_plan"},
        {"from": 10, "still": "e_final", "marks": [("text", 89, "3000, 0, 2800, 700")]},
    ]},
    "s07_nothing_to_paste": {"step": 6, "beats": [
        {"from": 0, "still": "m_62"},
        {"from": 1, "still": "m_62", "marks": [("lines", 62, 62)]},
        {"from": 3, "still": "m_62", "marks": [("text", 62, "relics_spawn")]},
        {"from": 5, "still": "m_62"},
    ]},
    "s08_lint": {"step": 7, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_crypt", "marks": [("text", 90, "crypt")]},
        {"from": 2, "still": "t_crypt", "marks": [("span", 1, "relic-dangling-passage")]},
        {"from": 3, "still": "t_crypt", "marks": [("span", 1, "the game does not build 'hollow' at all")]},
        {"from": 5, "still": "e_four", "marks": [("text", 86, "####")]},
        {"from": 6, "still": "card_plan"},
        {"from": 7, "still": "t_four", "marks": [("span", 1, "relic-part-level")]},
        {"from": 8, "still": "e_rooms", "marks": [("text", 71, "###"), ("text", 78, "###"), ("text", 86, "###")]},
        {"from": 9, "still": "e_noloc", "marks": [("lines", 65, 67)]},
        {"from": 10, "still": "t_noloc", "marks": [("part", "run1:clean")]},
        {"from": 12, "still": "e_noloc"},
        {"from": 13, "still": "e_loc", "marks": [("text", 67, "Loc: 0, 0, 20000")]},
    ]},
    "s09_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "t_run", "marks": [("cmd", 1, "server,helm")]},
        {"from": 1, "still": "game_c2_map"},
        {"from": 2, "still": "game_c2_map"},
        {"from": 3, "still": "game_c2_mouth"},
        {"from": 6, "still": "game_c2_nave"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "e_gbox", "marks": [("lines", 94, 100)]},
        {"from": 3, "still": "e_gbox", "marks": [("text", 97, "Box:")]},
        {"from": 4, "still": "e_gfar", "marks": [("text", 97, "-1900")]},
        {"from": 5, "still": "t_split", "marks": [("span", 1, "relic-disconnected")]},
        {"from": 6, "still": "e_gpass", "marks": [("text", 98, "Passage to: nave 300")]},
        {"from": 7, "still": "card_next"},
    ]},
}
