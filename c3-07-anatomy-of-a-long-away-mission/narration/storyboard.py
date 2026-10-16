"""Storyboard for c3-07-anatomy-of-a-long-away-mission: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

A NEW MISSION, MyAway, made by `sbs create MyAway -t away --title "Kesh Relay"`. Nothing is
typed in this lecture: every state is the page's own example (the starter as the command
makes it). The steps are "Stops" on the page, not "Step N", so every scene's step chip is None.

THE GROUND FOLDER. A state holds the example's `ground\\` folder as the student has it
(states.py reads, diffs and writes subfolders), so the files are named `ground/landing.tiles`
and lint prints `ground\\landing.tiles`. v_folder shows the file list with ground\\ open.
The close views of a file hide the Side Bar, as every close view of this class does.
  - t_create / t_fetch / t_lint0 are ONE real cmd.exe session, with any MyAway hidden
    meanwhile and what it made thrown away after (a copy is kept in <out>\\made\\myaway, to
    compare with this lecture's example).

THE TILE MAP EDITOR still (d_editor_landing) is taken in the add-on's own editor: capture
opens the file with vscode.openWith ("editor": "tiles") and sets the view over DevTools
("view": "art"). See capture.web_steps.

GAME STILLS. Not taken yet; no marks until the screenshots exist. THREE windows:
server, science (Dr Ines Hale, medical and science) and weapons (Lt Sam Reyes, security),
the page's own `sbs run server,science,weapons -m MyAway map=0`. State "final" as it is: the
ship starts beside Kesh Relay, so nothing is patched and nobody flies.
`python game.py c3-07-anatomy-of-a-long-away-mission start --consoles server,science,weapons`
makes the probe from the `away` template and lays every file of the state over it, ground\\
included.
GAME A (the win):
  1. Wait about 15 s after both consoles are seated: Hold at the Relay completes on its own.
     On Science press the handheld icon (top left), then Boarding Party: game_l7_offer.
  2. BEAM DOWN on Science: game_l7_landed (the yard, Dr Hale on the pad, before any click).
  3. Science: click open ground east of the pad (about cell 9, 5): game_l7_walk.
  4. Science: click Old Marrow (the figure south of the tent): game_l7_marrow (his scene).
  5. Press 'Ask what he has put by': game_l7_putby. 'Thank him', then look at the map: the
     medical kit on the scrub beside the pad (cell 6, 8): game_l7_kit. ('Look at that cough'
     can be pressed after; it is in game_l7_marrow as a button only.)
  6. Weapons: handheld icon, Boarding Party, BEAM DOWN. Walk east until the sentry is in
     view on its square (cells 20-26, 9-11): game_l7_sentry (the keycard at 24, 10 also in
     view if the fog allows). Keep away: it notices within 4 cells and hits hard.
  7. Weapons: open Fire on the handheld, choose FULL, press Arm: game_l7_fire. Click the
     sentry. When it falls: game_l7_sentry_down (the power cell where it fell).
  8. Weapons: click the cell, then the keycard (both picked up), then the relay door (22, 5):
     game_l7_door (the door open). Walk in, click the beacon: game_l7_beacon.
  9. 'Fit the power cell', then 'Call it in'. The last screen on the server: game_l7_win.
GAME B (the loss): start again. Weapons only: beam down, FULL the sentry as before, then
  with Fire on CUT click the relay door (it is `Opens with: ... cut`; a quicker way in than
  the page's door code - only the last screen is shown). Click the beacon, 'Pull the governor
  and run it wide open', then 'Step back from the smoke'. The last screen: game_l7_lose.
"""
LECTURE = "c3-07-anatomy-of-a-long-away-mission"
TITLE = ("Class 3, Lecture 7", "Anatomy of a long away mission", "A map, a fact sheet and one card")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-07-anatomy-of-a-long-away-mission/example"

STATES = {
    # The starter as `sbs create ... -t away` makes it, ground\ and all.
    "start": {"folder": _EX},
    "final": {"base": "start", "same_as": (_EX + "/mission.amd", _EX + "/story.mast",
                                           _EX + "/ground/landing.tiles", _EX + "/ground/starter.tileset")},
}

_CREATE = 'sbs create MyAway -t away --title "Kesh Relay"'
_FETCH = 'sbs fetch "MyAway" --update-libs'
_LINT = "sbs lint MyAway"
_MAKE = [(_CREATE, ("",)), _FETCH, _LINT]
_NO = {"without": ("MyAway",), "keep": {"myaway": "MyAway"}}
_NS = {"side": False}
_TILES = {"side": False, "file": "ground/landing.tiles"}
_TSET = {"side": False, "file": "ground/starter.tileset"}
_M = {"side": False, "file": MAST}

STILLS = {
    # Stop 1: one real cmd.exe session, with no MyAway before it
    "t_create": ("session", _MAKE, dict(_NO, show=(1, 1))),
    "t_fetch": ("session", _MAKE, dict(_NO, show=(2, 2), tail=14)),
    "t_lint0": ("session", _MAKE, dict(_NO, show=(3, 3))),
    # MyAway as the student has it: the file list showing ground\ open
    "v_folder": ("vscode", "start", 9, "wide", {"file": "ground/landing.tiles"}),
    "e_json": ("vscode", "final", 14, "big", {"side": False, "file": "story.json"}),    # lines 4 to 24
    "e_head": ("vscode", "final", 19, "big", _TILES),        # lines 9 to 29: header and legend
    "e_map": ("vscode", "final", 34, "big", _TILES),         # lines 24 to 44: the end of the legend, the map
    "e_tileset": ("vscode", "final", 10, "big", _TSET),      # the whole file (17 lines)
    "e_keycard": ("vscode", "final", 159, "big", _NS),       # lines 149 to 169: the door, the keycard
    "e_marrow": ("vscode", "final", 208, "big", _NS),        # lines 198 to 218: Old Marrow
    "e_marrow_scene": ("vscode", "final", 285, "big", _NS),  # lines 275 to 295: his room
    "e_load": ("vscode", "final", 54, "big", _M),            # lines 44 to 64: the load line
    "e_card": ("vscode", "final", 80, "big", _M),            # lines 70 to 88: the card
    "e_relight": ("vscode", "final", 72, "big", _NS),        # lines 62 to 82: Relight Kesh Relay
    "e_endings": ("vscode", "final", 328, "big", _NS),       # lines 318 to 338: the beacon's answers
    # landing.tiles in the Tile Map Editor, Art view: the yard as a picture
    "d_editor_landing": ("vscode", "final", 1, "mid", {"side": False, "file": "ground/landing.tiles", "editor": "tiles",
                                                       "view": "art", "zoom": 32}),
    # THE REAL GAME (not taken yet). Consoles server,science,weapons; see the docstring
    "game_l7_offer": ("game", "GAME A, Science (Dr Ines Hale), ~15 s after the consoles are seated: the handheld (icon top left), the Boarding Party app offering Kesh Relay, with BEAM DOWN"),
    "game_l7_landed": ("game", "GAME A, Science, BEAM DOWN just pressed: the yard map with Dr Hale's figure on the landing pad at the west end, the handheld beside it (her name, medical, the place word), the tent and the relay house in view"),
    "game_l7_walk": ("game", "GAME A, Science, after a click on open ground east of the pad (about 9, 5): Dr Hale has walked there, nearer the tent"),
    "game_l7_marrow": ("game", "GAME A, Science, Old Marrow clicked: the Act app with his line ('Nine days dark. I kept the kettle on...') and five buttons, 'Look at that cough' among them; his face beside what he says"),
    "game_l7_putby": ("game", "GAME A, Science, 'Ask what he has put by' pressed: the Put By line ('...Medical kit, under the netting...') and two buttons, Ask him something else / Thank him"),
    "game_l7_kit": ("game", "GAME A, Science, after Thank him: the yard map with the medical kit now drawn on the scrub beside the pad (cell 6, 8), where it was not before"),
    "game_l7_sentry": ("game", "GAME A, Weapons (Lt Sam Reyes), beamed down and walked east: the sentry on its square south-east of the relay house (cells 20-26, 9-11); the keycard at 24, 10 in view if the fog allows"),
    "game_l7_fire": ("game", "GAME A, Weapons, the Fire app open: the three settings (STUN, CUT, FULL) with FULL chosen, and Arm"),
    "game_l7_sentry_down": ("game", "GAME A, Weapons, after the FULL shot: the sentry down for good, the power cell lying where it fell"),
    "game_l7_door": ("game", "GAME A, Weapons, carrying the cell and the keycard, the relay door clicked: the door at 22, 5 drawn open"),
    "game_l7_beacon": ("game", "GAME A, Weapons, inside the relay house, the beacon clicked: The Beacon's line ('The beacon fills the room, dark...') and its buttons, 'Fit the power cell' first"),
    "game_l7_win": ("game", "GAME A, the server's last screen after 'Fit the power cell' and 'Call it in': Game results, the sentence 'The beacon is lit. Every convoy on the Kesh run has its way home again.' at the left"),
    "game_l7_lose": ("game", "GAME B, the server's last screen after 'Pull the governor...' and 'Step back from the smoke': 'The beacon is slag. The Kesh run stays dark, and the convoys must find another road.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_run": ("card", "points", {"kicker": "A server and two consoles", "items": ["sbs run server,science,weapons -m MyAway map=0"]}),
    "card_files": ("card", "table", {"heading": "Stop 3 - Four files", "kicker": "Four files are the mission"}),
    "card_sections": ("card", "table", {"heading": "Stop 5 - What a record is", "kicker": "Seven sections"}),
    "card_fields": ("card", "table", {"heading": "Stop 5 - What a record is", "nth": 2, "kicker": "A prop"}),
    "card_opens": ("card", "table", {"heading": "Stop 5 - What a record is", "nth": 3, "kicker": "Nobody walks into a scene"}),
    "card_card": ("card", "table", {"heading": "Stop 6 - One line and one card", "kicker": "Beside the Lecture 2 card"}),
    "card_words": ("card", "table", {"heading": "Stop 6 - One line and one card", "nth": 2, "kicker": "Three words are yours"}),
    # the page's own table (its first header cell is empty)
    "card_dawn": ("card", "table", {"heading": "Stop 8 - The long one: Dawnline", "kicker": "Your starter and Dawnline"}),
    "card_exits": ("card", "rows", {"kicker": "Dawnline's first area, ridge", "header": ("In its legend", "Means"),
                                    "rows": (("C: exit @to_colony", "A mark named to_colony: the way out to the area colony"),
                                             ("F: exit @to_flats", "The way out to the area flats"),
                                             ("exits:  to_colony: colony @to_ridge", "And you arrive beside the colony's way back"))}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "One change at a time"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 8", "sub": "The Tile Map Editor, part 1"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l7_landed"},
        {"from": 2, "still": "game_l7_marrow"},
        {"from": 3, "still": "e_map", "marks": [("lines", 31, 44)]},
        {"from": 4, "still": "t_create"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_a_second_mission": {"step": None, "beats": [
        {"from": 0, "still": "t_create"},
        {"from": 2, "still": "t_create", "marks": [("cmd", 1, "-t away")]},
        {"from": 3, "still": "t_create", "marks": [("span", 1, "[Y/n]")]},
        {"from": 4, "still": "t_create", "marks": [("span", 1, "MyAway is ready.")]},
        {"from": 5, "still": "t_fetch"},
        {"from": 7, "still": "t_fetch"},
        {"from": 8, "still": "e_json", "marks": [("lines", 19, 23)]},
        {"from": 9, "still": "e_json", "marks": [("lines", 21, 22)]},
        {"from": 10, "still": "t_create", "marks": [("span", 1, "media unpacked: artemis-sbs.Cosmos-Tiles.frontier.v0.4.2")]},
        {"from": 11, "still": "v_folder"},
        {"from": 12, "still": "t_lint0", "marks": [("part", "run1:clean")]},
    ]},
    "s03_play_it_to_the_win": {"step": None, "beats": [
        {"from": 0, "still": "card_run"},
        {"from": 2, "still": "game_l7_offer"},
        {"from": 3, "still": "game_l7_landed"},
        {"from": 5, "still": "game_l7_walk"},
        {"from": 7, "still": "game_l7_marrow"},
        {"from": 9, "still": "game_l7_putby"},
        {"from": 10, "still": "game_l7_kit"},
        {"from": 11, "still": "game_l7_sentry"},
        {"from": 12, "still": "game_l7_fire"},
        {"from": 14, "still": "game_l7_sentry_down"},
        {"from": 15, "still": "game_l7_door"},
        {"from": 16, "still": "game_l7_beacon"},
        {"from": 17, "still": "game_l7_win"},
    ]},
    "s04_four_files": {"step": None, "beats": [
        {"from": 0, "still": "v_folder"},
        {"from": 1, "still": "card_files"},
        {"from": 3, "still": "card_files", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_files", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_files", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_files", "marks": [("part", "r4")]},
        {"from": 10, "still": "v_folder"},
    ]},
    "s05_what_a_map_is": {"step": None, "beats": [
        # the game first: the yard on the Science console
        {"from": 0, "still": "game_l7_landed"},
        {"from": 5, "still": "d_editor_landing"},
        {"from": 7, "still": "e_head"},
        {"from": 9, "still": "e_head", "marks": [("lines", 9, 12)]},
        {"from": 10, "still": "e_head", "marks": [("lines", 12, 12)]},
        {"from": 11, "still": "e_head", "marks": [("lines", 13, 20)]},
        {"from": 12, "still": "e_head", "marks": [("lines", 14, 14)]},
        {"from": 13, "still": "e_head", "marks": [("lines", 20, 20)]},
        {"from": 14, "still": "e_head", "marks": [("lines", 21, 29)]},
        {"from": 15, "still": "e_head", "marks": [("text", 22, "@door")]},
        {"from": 18, "still": "e_map", "marks": [("lines", 31, 44)]},
        {"from": 19, "still": "e_map", "marks": [("text", 35, "=P=")]},
        {"from": 20, "still": "e_map", "marks": [("text", 34, "t")]},
        {"from": 21, "still": "e_map", "marks": [("text", 32, "WWWWWWWWW"), ("text", 36, "WWWWDWWWW")]},
        {"from": 22, "still": "e_map", "marks": [("lines", 31, 44)]},
        {"from": 23, "still": "e_head", "marks": [("lines", 21, 29)]},
        {"from": 24, "still": "e_tileset", "marks": [("lines", 11, 17)]},
    ]},
    "s06_what_a_record_is": {"step": None, "beats": [
        # the game first: the keycard and Old Marrow on the map
        {"from": 0, "still": "game_l7_sentry"},
        {"from": 2, "still": "game_l7_walk"},
        {"from": 3, "still": "card_sections"},
        {"from": 6, "still": "card_sections", "marks": [("part", "r4"), ("part", "r5"), ("part", "r6")]},
        {"from": 8, "still": "e_keycard", "marks": [("lines", 156, 163)]},
        {"from": 9, "still": "e_keycard", "marks": [("lines", 156, 163)]},
        {"from": 10, "still": "e_keycard", "marks": [("lines", 158, 159)]},
        {"from": 11, "still": "card_fields", "marks": [("part", "r1")]},
        {"from": 12, "still": "card_fields", "marks": [("part", "r2")]},
        {"from": 13, "still": "e_keycard", "marks": [("lines", 161, 161)]},
        {"from": 14, "still": "card_fields", "marks": [("part", "r4")]},
        {"from": 15, "still": "e_marrow", "marks": [("lines", 204, 214)]},
        {"from": 16, "still": "e_marrow", "marks": [("lines", 211, 211)]},
        {"from": 17, "still": "e_marrow_scene", "marks": [("lines", 282, 289)]},
        {"from": 18, "still": "card_opens"},
        {"from": 20, "still": "card_opens", "marks": [("part", "r1"), ("part", "r2")]},
    ]},
    "s07_one_line_one_card_and_the_en": {"step": None, "beats": [
        {"from": 0, "still": "e_load", "marks": [("lines", 54, 54)]},
        # the game first: the tile the card puts on the handheld
        {"from": 3, "still": "game_l7_offer"},
        {"from": 5, "still": "e_card", "marks": [("lines", 84, 88)]},
        {"from": 6, "still": "card_card"},
        {"from": 7, "still": "card_card", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_card", "marks": [("part", "r2")]},
        {"from": 11, "still": "card_words"},
        {"from": 12, "still": "e_card", "marks": [("text", 84, "relay_reached"), ("text", 87, '"Kesh Relay"'),
                                                  ("text", 87, '"landing"')]},
        # the game first: the last screen
        {"from": 13, "still": "game_l7_win"},
        {"from": 16, "still": "e_relight", "marks": [("lines", 75, 75)]},
        {"from": 17, "still": "e_relight", "marks": [("lines", 76, 76)]},
        {"from": 18, "still": "e_endings", "marks": [("lines", 328, 328), ("lines", 338, 338)]},
        {"from": 19, "still": "game_l7_lose"},
    ]},
    "s08_dawnline_and_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_dawn"},
        {"from": 4, "still": "card_dawn", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_dawn", "marks": [("part", "r3")]},
        {"from": 6, "still": "card_dawn"},
        {"from": 7, "still": "card_exits", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 9, "still": "card_exits", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 11, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 12, "still": "card_next"},
    ]},
}
