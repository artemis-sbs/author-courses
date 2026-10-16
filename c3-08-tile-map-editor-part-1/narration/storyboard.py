"""Storyboard for c3-08-tile-map-editor-part-1: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 7's untouched starter ("start") and makes ONE new file,
ground\\gully.tiles: empty ("g0"), the header ("g_head"), Step 2's whole file ("g1"), the door
("g2"), the arrive mark ("g3") and the entry line ("final", the page's own example file).
The steps are the page's "## Step N" headings.

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders): the new file is `ground/gully.tiles`, v_new shows it in the file list
with ground\\ open, and lint prints `ground\\gully.tiles` as the student's does. The close
views of the text hide the Side Bar, as every close view of this class does.

THE TILE MAP EDITOR stills are taken in the add-on's own editor: capture opens the file with
vscode.openWith ("editor": "tiles") and sets up what the caption says over DevTools - the
view ("view": "art"), a legend row picked ("pick"), + Entry's form filled in ("form"), the
cell under the pointer ("hover"), a title-bar button's tooltip ("tip"). Nothing moves the
real mouse. See capture.web_steps.

GAME STILLS. Not taken yet; no marks until the screenshots exist. TWO windows, server and
engineering (Chief Okoro), the page's `sbs run server,engineering -m MyAway map=0`, state
"final": `python game.py c3-08-tile-map-editor-part-1 start --consoles server,engineering`
(the probe is made from the `away` template, with every file of the state laid over it).
  1. About 15 s after Engineering is seated: handheld icon (top left), Boarding Party, Kesh
     Relay, BEAM DOWN. Chief Okoro is on the pad of the yard.
  2. Open Beam on the handheld: game_l8_beam (the list with one place, To The Dry Gully).
  3. Press it: game_l8_arrived (the gully, Okoro on the arrive mark at cell 2, 5, the pump
     house to the east; the handheld's words `Energizing - The Dry Gully.` if they show).
  4. Click inside the pump house (cell 15, 5) and wait for the walk (a few seconds):
     game_l8_inside (Okoro on the floor, in through the gap at 12, 5).
"""
LECTURE = "c3-08-tile-map-editor-part-1"
TITLE = ("Class 3, Lecture 8", "The Tile Map Editor, part 1", "A map of your own")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"
G = "ground/gully.tiles"

_L7 = "c3-07-anatomy-of-a-long-away-mission/example"
_EX = "c3-08-tile-map-editor-part-1/example"

_HEAD = ("# The dry gully east of the relay yard, and the pump house that stands in it.\n"
         "area: gully\ntitle: The Dry Gully\ntileset: starter\nsize: 24x12\n")
_LEGEND = "legend:\n  .: dust\n  ,: scrub\n  #: rock\n  ^: cliff\n  _: floor\n  W: wall\n"
_ROWS = ("---\n"
         "^^^^^^^^^^^^^^^^^^^^^^^^\n"
         "^###......,,....####^^^^\n"
         "^#.........,........##^^\n"
         "^#..........WWWWWWW..#^^\n"
         "^...........W_____W..#^^\n"
         "^...........W_____W..#^^\n"
         "^...........W_____W..#^^\n"
         "^#..,,......WWWWWWW..#^^\n"
         "^#...,,..............#^^\n"
         "^##.................##^^\n"
         "^^###...........#####^^^\n"
         "^^^^^^^^^^^^^^^^^^^^^^^^\n")
_ROW5 = "^...........W_____W..#^^\n^...........W_____W..#^^\n^...........W_____W..#^^\n"

STATES = {
    # Lecture 7's starter, ground\ and all
    "start": {"folder": _L7},
    # Step 1: the new file, empty
    "g0": {"base": "start", "edits": [("write", G, "")]},
    # Step 2: the header, then the legend and the ground
    "g_head": {"base": "start", "edits": [("write", G, _HEAD)]},
    "g1": {"base": "start", "edits": [("write", G, _HEAD + _LEGEND + _ROWS)]},
    # Step 4: the door
    "g2": {"base": "g1", "edits": [
        ("replace", G, "  W: wall\n---", "  W: wall\n  D: floor @pump_door\n---"),
        ("replace", G, _ROW5, "^...........W_____W..#^^\n^...........D_____W..#^^\n^...........W_____W..#^^\n")]},
    # Step 5: the arrive mark
    "g3": {"base": "g2", "edits": [
        ("replace", G, "@pump_door\n---", "@pump_door\n  a: dust @arrive\n---"),
        ("replace", G, "^...........D_____W", "^.a.........D_____W")]},
    # Step 6: the entry. The page's own file.
    "final": {"base": "g3", "edits": [("replace", G, "tileset: starter\nsize:", "tileset: starter\nentry: arrive\nsize:")],
              "same_as": _EX + "/ground/gully.tiles"},
    # Step 8 / scene 7: two slips lint catches
    "b_arival": {"base": "final", "edits": [("replace", G, "entry: arrive", "entry: arival")]},
    "b_w": {"base": "final", "edits": [("replace", G, "^#..........WWWWWWW..#^^\n^...", "^#..........WWWwWWW..#^^\n^...")]},
}

_LINT = "sbs lint MyAway"
_GT = {"side": False, "file": G}
_ED = {"side": False, "file": G, "editor": "tiles", "zoom": 40}          # the Tile Map Editor
_ART = dict(_ED, view="art")


def _lint(state):
    """sbs lint on the state, as the student types it."""
    return ("session", [_LINT], {"state": state})


STILLS = {
    "t_g1": _lint("g1"),
    "t_final": _lint("final"),
    "t_arival": _lint("b_arival"),
    "t_w": _lint("b_w"),
    # the file list, ground\ open, the new empty gully.tiles
    "v_new": ("vscode", "g0", 1, "wide", {"file": G}),
    "e_empty": ("vscode", "g0", 1, "mid", _GT),
    "e_head": ("vscode", "g_head", 5, "mid", _GT),
    "e_g1": ("vscode", "g1", 13, "mid", _GT),             # the whole file, lines 1 to 25
    "e_g2": ("vscode", "g2", 13, "mid", _GT),             # 26 lines
    "e_g3": ("vscode", "g3", 13, "mid", _GT),             # 27 lines
    "e_final": ("vscode", "final", 13, "mid", _GT),       # 28 lines
    "e_arival": ("vscode", "b_arival", 13, "mid", _GT),
    # The Tile Map Editor (see the docstring)
    # the finished gully, Art view
    "d_art": ("vscode", "final", 1, "mid", _ART),
    # the gully (g1), Kinds view: the cells nobody can walk hatched
    "d_kinds": ("vscode", "g1", 1, "mid", dict(_ED, view="kinds")),
    # the empty gully.tiles: 'No map yet.' and the toolbar with Text at its end
    "d_nomap": ("vscode", "g0", 1, "mid", _ED),
    # gully.tiles as text, the title-bar button 'Open in Tile Map / Tileset Editor', its tip showing
    "d_button": ("vscode", "g1", 13, "mid", dict(_GT, tip="Open in Tile Map")),
    # g1, Art, the pointer over cell 12, 5: the bottom line reading the cell, wall, and the area's name and size
    "d_hover": ("vscode", "g1", 1, "mid", dict(_ART, hover=(12, 5))),
    # + Entry's form filled in: Kind floor, Mark pump_door, Character D
    "d_form": ("vscode", "g1", 1, "mid", dict(_ART, form={"kind": "floor", "mark": "pump_door", "char": "D"})),
    # g2, Art, after painting cell 12, 5: the gap in the west wall, the legend row D floor @pump_door selected
    "d_door": ("vscode", "g2", 1, "mid", dict(_ART, pick="D")),
    # final, Art: the arrive mark outlined at 2, 5 and the green star of the entry on it
    "d_star": ("vscode", "final", 1, "mid", _ART),
    # THE REAL GAME (not taken yet). Consoles server,engineering; see the docstring
    "game_l8_beam": ("game", "Engineering (Chief Okoro) beamed down to the yard: the handheld's Beam app open, listing one place, To The Dry Gully"),
    "game_l8_arrived": ("game", "Engineering, To The Dry Gully pressed: the gully map, Okoro on the arrive mark at the west end (2, 5), the pump house with its gap in the west wall to the east"),
    "game_l8_inside": ("game", "Engineering, after a click inside the pump house (15, 5) and the walk: Okoro on the pump house floor, in through the gap at 12, 5"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_header": ("card", "rows", {"kicker": "The header", "header": ("Line", "Means"), "rows": (
        ("area: gully", "This area's key. Every area in a mission needs its own"),
        ("title: The Dry Gully", "What the crew is shown"),
        ("tileset: starter", "Its kinds of ground come from starter.tileset"),
        ("size: 24x12", "24 cells across and 12 down. A small x, and no spaces"))}),
    "card_editor": ("card", "table", {"heading": "Step 3 - Look at it in the editor", "kicker": "The editor, read from its own files"}),
    "card_tools": ("card", "table", {"heading": "Step 7 - More of the editor", "kicker": "The other tools"}),
    "card_lint": ("card", "table", {"heading": "Step 8 - Check it", "kicker": "What lint says", "rows": (1, 3, 15, 16)}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 2, "kicker": "Lint says clean, and"}),
    "card_run": ("card", "points", {"kicker": "A server and one console", "items": ["sbs run server,engineering -m MyAway map=0"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Try the other tools"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 9", "sub": "The Tile Map Editor, part 2"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "d_art"},
        {"from": 2, "still": "e_final", "marks": [("lines", 2, 28)]},
        {"from": 4, "still": "game_l8_inside"},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_a_new_file_and_the_header": {"step": 1, "beats": [
        {"from": 0, "still": "v_new"},
        {"from": 2, "still": "d_nomap"},
        {"from": 4, "still": "e_empty"},
        {"from": 5, "still": "e_head", "marks": [("lines", 2, 5)]},
        {"from": 6, "still": "e_head", "marks": [("lines", 2, 2)]},
        {"from": 8, "still": "e_head", "marks": [("lines", 3, 3)]},
        # the game: where the title is read
        {"from": 9, "still": "game_l8_beam"},
        {"from": 10, "still": "e_head", "marks": [("lines", 4, 4)]},
        {"from": 11, "still": "e_head", "marks": [("lines", 5, 5)]},
        {"from": 12, "still": "card_header", "marks": [("part", "r4")]},
    ]},
    "s03_the_legend_and_the_ground": {"step": 2, "beats": [
        {"from": 0, "still": "e_g1", "marks": [("lines", 6, 12)]},
        {"from": 1, "still": "e_g1", "marks": [("lines", 7, 7)]},
        {"from": 3, "still": "e_g1", "marks": [("lines", 7, 7)]},
        {"from": 4, "still": "e_g1", "marks": [("lines", 12, 12)]},
        {"from": 5, "still": "e_g1", "marks": [("lines", 13, 13)]},
        {"from": 6, "still": "e_g1", "marks": [("lines", 14, 25)]},
        {"from": 8, "still": "e_g1", "marks": [("lines", 14, 25)]},
        {"from": 9, "still": "e_g1", "marks": [("lines", 19, 19)]},
        {"from": 10, "still": "t_g1", "marks": [("part", "run1:cmd")]},
        {"from": 11, "still": "t_g1", "marks": [("part", "run1:clean")]},
        {"from": 12, "still": "t_g1"},
    ]},
    "s04_look_at_it": {"step": 3, "beats": [
        {"from": 0, "still": "d_button"},
        {"from": 2, "still": "card_editor"},
        {"from": 3, "still": "d_kinds"},
        {"from": 5, "still": "d_art"},
        {"from": 6, "still": "d_hover"},
        {"from": 9, "still": "e_g1", "marks": [("lines", 17, 21)]},
    ]},
    "s05_a_door": {"step": 4, "beats": [
        # the game first: the gap the crew walks through
        {"from": 0, "still": "game_l8_inside"},
        {"from": 3, "still": "e_g1", "marks": [("lines", 18, 20)]},
        {"from": 6, "still": "e_g1", "marks": [("lines", 18, 20)]},
        {"from": 8, "still": "d_form"},
        {"from": 12, "still": "d_door"},
        {"from": 14, "still": "e_g2", "marks": [("lines", 13, 13), ("lines", 20, 20)]},
        {"from": 15, "still": "e_g2", "marks": [("lines", 13, 13)]},
        {"from": 16, "still": "e_g2", "marks": [("text", 20, "D")]},
        {"from": 17, "still": "e_g2"},
    ]},
    "s06_a_mark_to_arrive_on_and_the_": {"step": 5, "beats": [
        # the game first: where the Beam app puts you
        {"from": 0, "still": "game_l8_arrived"},
        {"from": 2, "still": "e_g3", "marks": [("lines", 14, 14)]},
        {"from": 4, "still": "e_g3", "marks": [("text", 21, "a")]},
        {"from": 5, "still": "e_g3", "marks": [("text", 14, "@arrive")]},
        {"from": 6, "still": "e_g3", "marks": [("text", 14, "dust")]},
        {"from": 7, "still": "e_final", "marks": [("lines", 5, 5)]},
        {"from": 9, "still": "d_star"},
        {"from": 10, "still": "card_tools", "marks": [("part", "r5")]},
        {"from": 12, "still": "e_final", "marks": [("text", 5, "arrive")]},
    ]},
    "s07_lint_and_what_it_can_t_see": {"step": 8, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_arival", "marks": [("text", 5, "arival")]},
        {"from": 2, "still": "t_arival", "marks": [("span", 1, "is neither a mark on this map nor x, y")]},
        {"from": 3, "still": "t_w", "marks": [("span", 1, "is not in the legend")]},
        {"from": 4, "still": "t_w", "marks": [("span", 1, "the whole area will not load")]},
        {"from": 5, "still": "card_lint", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_lint", "marks": [("part", "r4")]},
        {"from": 8, "still": "card_cannot"},
        {"from": 9, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 11, "still": "e_final", "marks": [("lines", 17, 28)]},
    ]},
    "s08_play_it_and_your_turn": {"step": 9, "beats": [
        {"from": 0, "still": "card_run"},
        {"from": 2, "still": "game_l8_beam"},
        {"from": 5, "still": "game_l8_arrived"},
        {"from": 6, "still": "game_l8_inside"},
        {"from": 8, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 10, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 11, "still": "card_next"},
    ]},
}
