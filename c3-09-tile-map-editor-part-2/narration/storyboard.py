"""Storyboard for c3-09-tile-map-editor-part-2: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 8's files ("start": Lecture 7's starter with Lecture 8's
gully.tiles). Each of the page's steps is a state: the yard's exit (s1), the way back (s2),
`known: no` (s3), water in the tileset (s4), the cistern (s5), the stairs (s6), the exits:
block (s7), the trail sign (s8), the pump and the crate (s9), and the longer patrol
("final", the page's five example files).

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders), and lint prints `ground\\...` as the student's does. The close views of
the text hide the Side Bar, as every close view of this class does.

STEP 10 also opens a path behind the relay house (row 0, cells 17 to 27, painted dust): the
only other way east runs about three cells from the sentry's loop, which notices anyone
within four. Along the path and on to the sign and the exit, nothing comes nearer the loop
than five cells (checked with the library's own walking and noticing rules), so the page's
"walk east along the north side of the yard, well clear of the sentry" is true as written.

THE TILE MAP EDITOR STILLS are taken in the add-on's own editors ("editor": "tiles" /
"tileset", opened with vscode.openWith), set up over DevTools ("view": "art", "zoom"). See
capture.web_steps.

GAME STILLS. Not taken yet; no marks until the screenshots exist. TWO windows, server and
engineering (Chief Okoro), state final as the page has it (no probe-only change):
`python game.py c3-09-tile-map-editor-part-2 start --consoles server,engineering`.
  1. About 15 s after Engineering is seated: handheld icon (top left), Boarding Party, Kesh
     Relay, BEAM DOWN. Open Beam: game_l9_beam0 (nowhere else on it).
  2. Click the path behind the relay house (about 22, 0, the top row) and wait for the walk
     (about 10 s), then click the trail sign (28, 5): game_l9_sign (its line on the
     handheld). Never along row 6: that passes three cells from the sentry's loop.
  3. Click the exit, the cell under the sign and to the right (29, 6): game_l9_gully (Okoro
     in the gully at 1, 4, beside the way back).
  4. Open Beam: game_l9_beam1 (To The Dry Gully on it now).
  5. Walk into the pump house (the gap at 12, 5) and click the pump (15, 4): game_l9_pump.
  6. Click the stairs against the east wall (17, 5): game_l9_cistern (the cistern, Okoro at
     2, 1 beside the foot of the stairs, the tank of water).
"""
LECTURE = "c3-09-tile-map-editor-part-2"
TITLE = ("Class 3, Lecture 9", "The Tile Map Editor, part 2", "Three maps, and things on them")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"
LT, GT, TS, CT = "ground/landing.tiles", "ground/gully.tiles", "ground/starter.tileset", "ground/cistern.tiles"

_L7 = "c3-07-anatomy-of-a-long-away-mission/example"
_L8 = "c3-08-tile-map-editor-part-1/example"
_EX = "c3-09-tile-map-editor-part-2/example"

_CISTERN = ("# Under the pump house: a walkway round a tank of standing water.\n"
            "area: cistern\ntitle: The Cistern\ntileset: starter\nentry: foot\nknown: no\nbeam: no\nsize: 18x7\n"
            "legend:\n  W: wall\n  _: floor\n  ~: water\n  u: floor @to_gully\n  f: floor @foot\n---\n"
            "WWWWWWWWWWWWWWWWWW\n"
            "Wu_f__________W__W\n"
            "W_~~~~~~~~~~_____W\n"
            "W_~~~~~~~~~~__W__W\n"
            "W_~~~~~~~~~~__W__W\n"
            "W_____________W__W\n"
            "WWWWWWWWWWWWWWWWWW\n")
_SIGN = ("### [Trail sign](sign)\n---\nArea: landing\nAt: 28, 5\nSprite: prop:sign\n---\n"
         "A painted board on a post: PUMP HOUSE, and an arrow pointing east.\n")
_PUMP = ("// SCENERY again: no words, so nothing offers to use it. It only stands there, and blocks.\n"
         "### [The pump](pump)\n---\nArea: gully\nMark: pump\nSprite: prop:machinery\nBlocks: yes\n---\n\n"
         "### [Crate](gully_crate)\n---\nArea: gully\nAt: 6, 9\nSprite: prop:crate\nBlocks: yes\n---\n")

STATES = {
    # Lecture 8's files: the starter and the gully
    "start": {"folder": _L7, "over": (_L8,)},
    # Step 1: a way out of the yard
    "s1": {"base": "start", "edits": [
        ("replace", LT, "  h: scrub @scrub\n", "  h: scrub @scrub\n  >: dust @to_gully\n"),
        ("replace", LT, "^#...................T........^^", "^#...................T.......>^^")]},
    # Step 2: a way back
    "s2": {"base": "s1", "edits": [
        ("replace", GT, "  a: dust @arrive\n", "  a: dust @arrive\n  <: dust @to_landing\n"),
        ("replace", GT, "^.a.........D_____W", "^<a.........D_____W")]},
    # Step 3: what the ship knows
    "s3": {"base": "s2", "edits": [("replace", GT, "entry: arrive\n", "entry: arrive\nknown: no\n")]},
    # Step 4: water
    "s4": {"base": "s3", "edits": [("replace", TS, "look=cliff\n", "look=cliff\n  water:        see   look=water\n")]},
    # Step 5: the cistern
    "s5": {"base": "s4", "edits": [("write", CT, _CISTERN)]},
    # Step 6: stairs down
    "s6": {"base": "s5", "edits": [
        ("replace", GT, "@to_landing\n", "@to_landing\n  v: floor @to_cistern\n"),
        ("replace", GT, "^<a.........D_____W", "^<a.........D____vW")]},
    # Step 7: where they arrive
    "s7": {"base": "s6", "edits": [("replace", GT, "@to_cistern\n---", "@to_cistern\nexits:\n  to_cistern: cistern @foot\n---")]},
    # Step 8: a thing at a cell
    "s8": {"base": "s7", "edits": [("replace", FILE, "Sprite: prop:tent\nBlocks: yes\n---\n\n",
                                    "Sprite: prop:tent\nBlocks: yes\n---\n\n" + _SIGN + "\n")]},
    # Step 9: a thing on a mark
    "s9": {"base": "s8", "edits": [
        ("replace", GT, "@to_cistern\nexits:", "@to_cistern\n  p: floor @pump\nexits:"),
        ("replace", GT, "^...........W_____W..#^^\n^<a", "^...........W__p__W..#^^\n^<a"),
        ("replace", FILE, "pointing east.\n", "pointing east.\n\n" + _PUMP)]},
    # Step 10: the sentry's walk, and the path behind the relay house. The page's five files.
    "final": {"base": "s9", "edits": [("replace", FILE, "Patrol: 20 9; 26 9; 26 11; 20 11", "Patrol: 18 9; 27 9; 27 11; 18 11"),
                                      ("replace", LT, "---\n" + "^" * 32 + "\n", "---\n" + "^" * 17 + "." * 11 + "^" * 4 + "\n")],
              "same_as": (_EX + "/mission.amd", _EX + "/ground/landing.tiles", _EX + "/ground/gully.tiles",
                          _EX + "/ground/starter.tileset", _EX + "/ground/cistern.tiles")},
    # Step 8: the sign after one drag with Move (and before Undo move)
    "b_moved": {"base": "s8", "edits": [("replace", FILE, "At: 28, 5", "At: 29, 5")]},
    # Step 11 / scene 8: two slips lint catches
    "b_landng": {"base": "final", "edits": [("replace", GT, "@to_landing", "@to_landng")]},
    "b_at": {"base": "final", "edits": [("replace", FILE, "Mark: pump\n", "At: pump\n")]},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}


def _t(f):
    return {"side": False, "file": f}


def _ed(f, zoom, **more):
    """The file in the Tile Map Editor, Art view (see capture.web_steps)."""
    return dict(_NS, file=f, editor="tiles", view="art", zoom=zoom, **more)


def _lint(state):
    """sbs lint on the state, as the student types it."""
    return ("session", [_LINT], {"state": state})
STILLS = {
    # lint, each on the real layout
    "t_s2": _lint("s2"),
    "t_s7": _lint("s7"),
    "t_final": _lint("final"),
    "t_landng": _lint("b_landng"),
    "t_at": _lint("b_at"),
    # the files as text
    "e_exit": ("vscode", "s1", 35, "big", _t(LT)),         # lines 25 to 45: the legend's end, the map
    "e_back": ("vscode", "s2", 13, "mid", _t(GT)),          # lines 1 to 29
    "e_known": ("vscode", "s3", 13, "mid", _t(GT)),
    "e_water": ("vscode", "s4", 10, "big", _t(TS)),         # the whole tileset, 18 lines
    "e_cistern": ("vscode", "s5", 11, "mid", _t(CT)),       # the whole file, 22 lines
    "e_stairs": ("vscode", "s6", 13, "mid", _t(GT)),
    "e_exits": ("vscode", "s7", 13, "mid", _t(GT)),
    "e_sign": ("vscode", "s8", 201, "big", _NS),            # lines 191 to 211
    "e_moved": ("vscode", "b_moved", 201, "big", _NS),
    "e_pumpmark": ("vscode", "final", 15, "mid", _t(GT)),   # lines 1 to 29
    "e_pump": ("vscode", "final", 213, "big", _NS),         # lines 203 to 223: the pump, the crate
    "e_at": ("vscode", "b_at", 213, "big", _NS),
    "e_patrol": ("vscode", "final", 257, "big", _NS),       # lines 247 to 267: the sentry
    "e_landng": ("vscode", "b_landng", 15, "mid", _t(GT)),
    # The Tile Map Editor (see the docstring)
    # the yard, Art, Marks on: its exit outlined in blue, labelled gully (and the path behind the relay house)
    "d_three": ("vscode", "final", 1, "mid", _ed(LT, 32)),
    # landing.tiles (s1), Marks on: the new exit at 29, 6 outlined in blue with the name of the area it leads to
    "d_exit": ("vscode", "s1", 1, "mid", _ed(LT, 32)),
    # starter.tileset (s4) in the Tileset Editor: the new water row, See ticked, Walk not, Look water
    "d_tileset": ("vscode", "s4", 1, "mid", dict(_NS, file=TS, editor="tileset")),
    # cistern.tiles (s5), Art: the walkway round the tank, the east room
    "d_cistern": ("vscode", "s5", 1, "mid", _ed(CT, 48)),
    # gully.tiles (s7), Marks on: the stairs at 17, 5 outlined in blue, labelled cistern
    "d_stairs": ("vscode", "s7", 1, "mid", _ed(GT, 40)),
    # landing.tiles (s8), Things on, Art: the trail sign drawn at 28, 5
    "d_sign": ("vscode", "s8", 1, "mid", _ed(LT, 32)),
    # landing.tiles (final), Things on: the sentry's patrol as a dashed loop, 18-27 by 9-11
    "d_patrol": ("vscode", "final", 1, "mid", _ed(LT, 32)),
    # THE REAL GAME (not taken yet). State final, consoles server,engineering; see the docstring
    "game_l9_beam0": ("game", "Engineering (Chief Okoro), just beamed down to the yard: the Beam app open, with nowhere else on it"),
    "game_l9_sign": ("game", "Engineering, the trail sign (28, 5) clicked: its line 'A painted board on a post: PUMP HOUSE, and an arrow pointing east.' on the handheld"),
    "game_l9_gully": ("game", "Engineering, the yard's exit (29, 6) clicked: Okoro standing in the gully at 1, 4, beside its way back"),
    "game_l9_beam1": ("game", "Engineering, in the gully: the Beam app open, To The Dry Gully on it now"),
    "game_l9_pump": ("game", "Engineering, inside the pump house, the pump (15, 4) clicked: Okoro beside it, and nothing more"),
    "game_l9_cistern": ("game", "Engineering, the stairs (17, 5) clicked: the cistern, Okoro at 2, 1 beside the foot of the stairs, the tank of water beside the walkway"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_rules": ("card", "points", {"kicker": "Three rules about exits", "items": [
        "An exit takes whoever stops on it. Click the exit itself",
        "Each person goes through alone",
        "They arrive beside the way back, never on it"]}),
    "card_known": ("card", "table", {"heading": "Step 3 - What the ship knows", "kicker": "Two header lines"}),
    "card_place": ("card", "table", {"heading": "Step 8 - A thing at a cell", "kicker": "Where a record stands"}),
    "card_lint": ("card", "table", {"heading": "Step 11 - Check it", "kicker": "What lint says", "rows": (1, 6, 11)}),
    "card_run": ("card", "points", {"kicker": "A server and one console", "items": ["sbs run server,engineering -m MyAway map=0"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "More on the maps"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 10", "sub": "Props"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "d_three"},
        {"from": 2, "still": "game_l9_gully"},
        {"from": 4, "still": "game_l9_cistern"},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_a_way_out_and_a_way_back": {"step": 1, "beats": [
        # the game first: through the exit
        {"from": 0, "still": "game_l9_gully"},
        {"from": 3, "still": "e_exit", "marks": [("text", 30, "@to_gully")]},
        {"from": 6, "still": "e_exit", "marks": [("lines", 30, 30)]},
        {"from": 8, "still": "e_exit", "marks": [("text", 38, ">")]},
        {"from": 9, "still": "e_back", "marks": [("lines", 16, 16), ("text", 23, "<")]},
        {"from": 11, "still": "card_rules"},
        {"from": 12, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 14, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 15, "still": "card_rules", "marks": [("part", "item3")]},
    ]},
    "s03_what_the_ship_knows": {"step": 3, "beats": [
        # the game first: the Beam app at the start
        {"from": 0, "still": "game_l9_beam0"},
        {"from": 2, "still": "card_known"},
        {"from": 6, "still": "card_known", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_known", "marks": [("part", "r2")]},
        {"from": 11, "still": "e_known", "marks": [("lines", 6, 6)]},
    ]},
    "s04_water_and_a_third_map": {"step": 4, "beats": [
        # the game first: the cistern
        {"from": 0, "still": "game_l9_cistern"},
        {"from": 2, "still": "d_tileset"},
        {"from": 4, "still": "e_water", "marks": [("lines", 17, 17)]},
        {"from": 5, "still": "e_water", "marks": [("text", 17, "see")]},
        {"from": 7, "still": "e_water", "marks": [("lines", 16, 17)]},
        {"from": 10, "still": "e_cistern", "marks": [("lines", 16, 22)]},
        {"from": 12, "still": "d_cistern"},
        {"from": 14, "still": "e_cistern", "marks": [("lines", 6, 7)]},
    ]},
    "s05_stairs_and_where_they_arrive": {"step": 6, "beats": [
        {"from": 0, "still": "e_stairs", "marks": [("lines", 18, 18), ("text", 25, "v")]},
        {"from": 2, "still": "game_l9_cistern"},
        {"from": 3, "still": "e_exits", "marks": [("lines", 19, 20)]},
        {"from": 6, "still": "e_exits", "marks": [("lines", 20, 20)]},
        {"from": 8, "still": "e_cistern", "marks": [("text", 14, "@foot")]},
        {"from": 9, "still": "d_stairs"},
        {"from": 10, "still": "e_exits", "marks": [("lines", 19, 20)]},
    ]},
    "s06_a_thing_at_a_cell": {"step": 8, "beats": [
        {"from": 0, "still": "card_place"},
        {"from": 2, "still": "card_place", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 4, "still": "card_place", "marks": [("part", "r1")]},
        {"from": 6, "still": "e_sign", "marks": [("lines", 198, 204)]},
        {"from": 7, "still": "e_sign", "marks": [("lines", 200, 201)]},
        # the game: the sign, clicked
        {"from": 8, "still": "game_l9_sign"},
        {"from": 10, "still": "d_sign"},
        {"from": 12, "still": "e_moved", "marks": [("lines", 201, 201)]},
    ]},
    "s07_a_thing_on_a_mark_and_a_patr": {"step": 9, "beats": [
        {"from": 0, "still": "e_pumpmark", "marks": [("lines", 19, 19), ("text", 27, "p")]},
        {"from": 2, "still": "e_pump", "marks": [("lines", 209, 210)]},
        {"from": 4, "still": "e_pump", "marks": [("lines", 210, 210), ("lines", 218, 218)]},
        {"from": 7, "still": "e_at", "marks": [("lines", 210, 210)]},
        {"from": 10, "still": "e_pump", "marks": [("lines", 206, 221)]},
        {"from": 12, "still": "e_pump", "marks": [("lines", 212, 212), ("lines", 220, 220)]},
        # the game: the pump, clicked
        {"from": 13, "still": "game_l9_pump"},
        {"from": 15, "still": "e_patrol", "marks": [("lines", 247, 260)]},
        {"from": 16, "still": "e_patrol", "marks": [("lines", 257, 257)]},
        {"from": 18, "still": "d_patrol"},
    ]},
    "s08_lint_play_it_and_your_turn": {"step": 11, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_landng", "marks": [("text", 17, "@to_landng")]},
        {"from": 2, "still": "t_landng", "marks": [("span", 1, "there is no area 'landng'")]},
        {"from": 3, "still": "t_at", "marks": [("span", 1, "a mark name goes in Mark:")]},
        {"from": 5, "still": "card_lint", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_run"},
        {"from": 8, "still": "game_l9_beam0"},
        {"from": 10, "still": "game_l9_gully"},
        {"from": 11, "still": "game_l9_beam1"},
        {"from": 12, "still": "game_l9_cistern"},
        {"from": 14, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 15, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 16, "still": "card_next"},
    ]},
}
