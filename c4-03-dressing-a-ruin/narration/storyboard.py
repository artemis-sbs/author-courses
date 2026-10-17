"""Storyboard for c4-03-dressing-a-ruin: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and Class 3's. Caption numbers are those of shots.py (2026-10-17).

The lecture starts from Lecture 2's hand-over: The Hollow with The Mouth, The Nave and The
Vault, 92 lines. The page's own example\\mission.amd (141 lines) is the finished section;
each step's state is that file with the lines of the LATER steps left out ("gallery" has
The Gallery and nothing else new; "walls", "blocks", "vart", "dials", "haze", "ring" each
add one step; "final" is the example whole). Lint's breaks are one change each on "final".
The Relic Plan is not used in this lecture.

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine. ONE
game, TWO windows:
`python game.py c4-03-dressing-a-ruin start --state final --consoles server,helm`
(the page's run line, `sbs run server,helm -m MyRuin map=0`, on a probe copy of the example).
No probe patch. Marks are left off every game still until the stills are taken.
Press order:
  1. Helm, at once, the map zoomed out: game_c3_map (the name The Hollow now at the way in,
     700 nearer than before, 19300 out).
  2. Fly to the name and in. The server window, just inside the way in, the haze and the
     rock: game_c3_haze.
  3. Fly on until the ring is across the passage ahead: server window, game_c3_ring.
  4. Through the ring and into The Nave, the ring behind, the block walls of The Gallery
     off to one side: game_c3_nave (also the cold open).
  5. Up the tunnel to The Vault until The Altar turns gold on the map: Helm, game_c3_altar
     (the name The Altar on the map).
  6. Back to The Nave and into The Gallery. The server window, built walls with pieces
     missing: game_c3_gallery.
"""
import os

LECTURE = "c4-03-dressing-a-ruin"
TITLE = ("Class 4, Lecture 3", "Dressing a ruin", "What the walls are made of, a haze, a gate, and places with names")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-03-dressing-a-ruin/example"
_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "..", "example", "mission.amd"), encoding="utf-8", newline="") as _fh:
    _F = _fh.read().replace("\r\n", "\n").split("\n")
if _F[-1] == "":
    _F.pop()

# the lines of the finished file (1-based) that each step adds
_STEP = {"walls": {68}, "dials": {69, 70, 71}, "haze": {72}, "vart": {96}, "gwalls": {105},
         "ring": set(range(108, 117)), "places": set(range(117, 142))}
_ORDER = ["walls", "dials", "haze", "vart", "gwalls", "ring", "places"]


def _have(*steps):
    """The finished file with every step NOT named left out."""
    gone = set()
    for s in _ORDER:
        if s not in steps:
            gone |= _STEP[s]
    return "".join(line + "\n" for i, line in enumerate(_F, 1) if i not in gone)


_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hollow"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hollow")]

STATES = {
    # Lecture 2's hand-over, The Gallery added (Step 1): lines 65 to 101 are the ruin so far
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED, "over": ("c4-02-a-ruin-is-a-place/example",)},
    "gallery": {"base": "start", "edits": [("write", FILE, _have())]},
    "walls": {"base": "start", "edits": [("write", FILE, _have("walls"))]},
    "blocks": {"base": "start", "edits": [("write", FILE, _have("walls", "gwalls"))]},
    "vart": {"base": "start", "edits": [("write", FILE, _have("walls", "gwalls", "vart"))]},
    "dials": {"base": "start", "edits": [("write", FILE, _have("walls", "gwalls", "vart", "dials"))]},
    "haze": {"base": "start", "edits": [("write", FILE, _have("walls", "gwalls", "vart", "dials", "haze"))]},
    "ring": {"base": "start", "edits": [("write", FILE, _have("walls", "gwalls", "vart", "dials", "haze", "ring"))]},
    "final": {"base": "start", "edits": [("write", FILE, _have(*_ORDER))], "same_as": (_EX + "/mission.amd",)},
    # Step 8: the breaks lint names, and the one it does not
    "b_bloks": {"base": "final", "edits": [("replace", FILE, "Walls: blocks", "Walls: bloks")]},
    "b_apoint": {"base": "final", "edits": [("replace", FILE, "Point: 3000, 0, 2800", "Point: 3000, 0")]},
    "b_tortus": {"base": "final", "edits": [("replace", FILE, "Dress: generic-torus 4", "Dress: generic-tortus 4")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

STILLS = {
    # VS Code, real. A still shows 21 lines: the one named, ten above and ten below
    "e_gal": ("vscode", "gallery", 98, "big", _NS),          # lines 88 to 100: The Gallery (Box on 97, Passage on 98)
    "e_walls": ("vscode", "walls", 68, "big", _NS),          # lines 58 to 78: the ruin, Walls: rock on 68
    "e_blocks": ("vscode", "blocks", 100, "big", _NS),       # lines 90 to 102: The Gallery with Walls: blocks on 100
    "e_vart": ("vscode", "vart", 92, "big", _NS),            # lines 82 to 102: Art on 92 (The Vault), Walls: blocks on 101
    "e_dials": ("vscode", "dials", 70, "big", _NS),          # lines 60 to 80: Seed 69, Debris 70, Gaps 71
    "e_haze": ("vscode", "haze", 70, "big", _NS),            # lines 60 to 80: Atmosphere on 72
    "e_ring": ("vscode", "ring", 113, "big", _NS),           # lines 103 to 123: The Ring, Prop 112, Dress 113, Facing 114
    "e_top": ("vscode", "final", 72, "big", _NS),            # lines 62 to 82: the finished fence of the ruin
    "e_places": ("vscode", "final", 130, "big", _NS),        # lines 120 to 140: The Way In's Point 121, The Altar, The Niche
    "e_bloks": ("vscode", "b_bloks", 105, "big", _NS),       # lines 95 to 115: Walls: bloks on 105
    "e_apoint": ("vscode", "b_apoint", 129, "big", _NS),     # lines 119 to 139: the Altar's Point with two numbers
    "e_tortus": ("vscode", "b_tortus", 113, "big", _NS),     # lines 103 to 123: generic-tortus on 113
    # the command prompt
    "t_lint": ("terminal", [("final", _LINT)]),
    "t_bloks": ("terminal", [("b_bloks", _LINT)]),
    "t_apoint": ("terminal", [("b_apoint", _LINT)]),
    "t_tortus": ("terminal", [("b_tortus", _LINT)]),
    "t_run": ("session", ["sbs run server,helm -m MyRuin map=0 --dry-run"], {"state": "final"}),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm
    "game_c3_map": ("game", "Helm, the map at the start: the hulk, and past it the name The Hollow, now at the way in"),
    "game_c3_haze": ("game", "The server window, just inside the way in: the purple haze and rock all round"),
    "game_c3_ring": ("game", "The server window in the first passage: the ring across the tunnel ahead, framing it"),
    "game_c3_nave": ("game", "The server window inside The Nave: haze, rock, the ring behind, the block walls of The Gallery off to one side"),
    "game_c3_altar": ("game", "Helm's map with the ship in the tunnel to The Vault: The Altar a gold contact with its name"),
    "game_c3_gallery": ("game", "The server window in The Gallery: walls of blocks with pieces missing"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_five": ("card", "table", {"heading": "Step 2 - Say what the walls are made of", "kicker": "Five words for a look"}),
    "card_pieces": ("card", "table", {"heading": "Step 2 - Say what the walls are made of", "nth": 2, "kicker": "How many pieces a wall is"}),
    "card_gaps": ("card", "table", {"heading": "Step 4 - Three dials", "nth": 2, "kicker": "Gaps: and the blocks of The Gallery"}),
    "card_colors": ("card", "table", {"heading": "Step 5 - Fill it with haze", "kicker": "Seven colors, or none"}),
    "card_shapes": ("card", "table", {"heading": "Step 6 - Stand something in it", "nth": 2, "kicker": "Shapes that come with the game"}),
    "card_list": ("card", "page", {"kicker": "An art pack adds kits. Write a list", "text": [
        "Walls: torgoth, plates", "Dress: ruins_tg_gate 1.6, generic-torus 4"],
        "caption": "The game uses the first word it knows."}),
    "card_points": ("card", "table", {"heading": "Step 7 - Name the places", "kicker": "What the game does with a point"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 4", "sub": "Places that speak"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c3_nave"},
        {"from": 4, "still": "e_top", "marks": [("lines", 65, 72)]},
    ]},
    "s02_a_built_room": {"step": 1, "beats": [
        {"from": 0, "still": "e_gal"},
        {"from": 4, "still": "e_gal", "marks": [("text", 97, "Box:")]},
        {"from": 6, "still": "e_gal", "marks": [("text", 98, "Passage to: nave 300")]},
    ]},
    "s03_what_the_walls_are_made_of": {"step": 2, "beats": [
        {"from": 0, "still": "e_walls", "marks": [("text", 68, "Walls: rock")]},
        {"from": 1, "still": "card_five"},
        {"from": 2, "still": "card_five", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_five", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_five", "marks": [("part", "r3")]},
        {"from": 5, "still": "card_five", "marks": [("part", "r4")]},
        {"from": 6, "still": "card_five", "marks": [("part", "r5")]},
        {"from": 7, "still": "card_pieces"},
        {"from": 8, "still": "card_pieces", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_pieces", "marks": [("part", "r2")]},
        {"from": 10, "still": "e_walls", "marks": [("text", 68, "rock")]},
    ]},
    "s04_one_room_that_differs": {"step": 3, "beats": [
        {"from": 0, "still": "e_blocks", "marks": [("lines", 95, 101)]},
        {"from": 1, "still": "e_blocks", "marks": [("text", 100, "Walls: blocks")]},
        {"from": 2, "still": "e_blocks", "marks": [("text", 100, "Walls: blocks")]},
        {"from": 3, "still": "e_blocks", "marks": [("text", 99, "Passage to: nave 300")]},
        {"from": 4, "still": "e_vart", "marks": [("lines", 87, 93)]},
        {"from": 5, "still": "e_vart", "marks": [("text", 92, "Art: plain_asteroid_9")]},
        {"from": 8, "still": "e_vart", "marks": [("text", 92, "plain_asteroid_9")]},
        {"from": 9, "still": "e_vart", "marks": [("text", 92, "Art:"), ("text", 101, "Walls:")]},
    ]},
    "s05_three_dials": {"step": 4, "beats": [
        {"from": 0, "still": "e_dials", "marks": [("lines", 69, 71)]},
        {"from": 1, "still": "e_dials", "marks": [("text", 69, "Seed: 12")]},
        {"from": 4, "still": "e_dials", "marks": [("text", 70, "Debris: 30")]},
        {"from": 6, "still": "e_dials", "marks": [("text", 71, "Gaps: 0.2")]},
        {"from": 7, "still": "card_gaps"},
        {"from": 8, "still": "card_gaps", "marks": [("part", "r3")]},
    ]},
    "s06_haze": {"step": 5, "beats": [
        {"from": 0, "still": "e_haze", "marks": [("text", 72, "Atmosphere: purple")]},
        {"from": 2, "still": "card_colors"},
        {"from": 3, "still": "e_haze", "marks": [("text", 72, "Atmosphere")]},
    ]},
    "s07_a_set_piece": {"step": 6, "beats": [
        {"from": 0, "still": "e_ring", "marks": [("lines", 109, 116)]},
        {"from": 1, "still": "e_ring", "marks": [("text", 109, "###"), ("text", 111, "Relic: hollow")]},
        {"from": 3, "still": "e_ring", "marks": [("text", 112, "Prop: 1400, 0, 0")]},
        {"from": 4, "still": "e_ring", "marks": [("text", 112, "1400")]},
        {"from": 5, "still": "e_ring", "marks": [("text", 113, "Dress: generic-torus 4")]},
        {"from": 6, "still": "e_ring", "marks": [("text", 113, "generic-torus 4")]},
        {"from": 8, "still": "e_ring", "marks": [("text", 114, "Facing: nave")]},
        {"from": 9, "still": "e_ring", "marks": [("lines", 112, 112)]},
        {"from": 10, "still": "card_shapes"},
        {"from": 11, "still": "card_list"},
    ]},
    "s08_named_places": {"step": 7, "beats": [
        {"from": 0, "still": "e_places", "marks": [("lines", 121, 122)]},
        {"from": 1, "still": "e_places", "marks": [("text", 121, "Point: 0, 0, -700")]},
        {"from": 2, "still": "e_places", "marks": [("text", 122, "Roles:")]},
        {"from": 3, "still": "e_places", "marks": [("text", 122, "Roles: entrance")]},
        {"from": 4, "still": "card_points", "marks": [("part", "r1")]},
        {"from": 5, "still": "e_places", "marks": [("text", 130, "Roles: altar")]},
        {"from": 6, "still": "e_places", "marks": [("text", 129, "Point: 3000, 0, 2800")]},
        {"from": 7, "still": "card_points", "marks": [("part", "r2")]},
        {"from": 10, "still": "e_places", "marks": [("text", 139, "Hidden: yes")]},
        {"from": 11, "still": "card_points", "marks": [("part", "r3")]},
    ]},
    "s09_lint": {"step": 8, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_bloks", "marks": [("text", 105, "bloks")]},
        {"from": 2, "still": "t_bloks", "marks": [("span", 1, "relic-walls-word")]},
        {"from": 3, "still": "e_apoint", "marks": [("text", 129, "Point: 3000, 0")]},
        {"from": 4, "still": "t_apoint", "marks": [("span", 1, "relic-short-point")]},
        {"from": 5, "still": "e_tortus", "marks": [("text", 113, "generic-tortus")]},
        {"from": 6, "still": "t_tortus", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "e_tortus"},
        {"from": 9, "still": "e_tortus", "marks": [("lines", 112, 114)]},
    ]},
    "s10_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_c3_map"},
        {"from": 1, "still": "game_c3_haze"},
        {"from": 2, "still": "game_c3_ring"},
        {"from": 3, "still": "game_c3_nave"},
        {"from": 5, "still": "game_c3_altar"},
        {"from": 7, "still": "game_c3_gallery"},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 6, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 7, "still": "card_next"},
    ]},
}
