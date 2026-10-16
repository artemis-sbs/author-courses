"""Storyboard for c3-02-party-and-place: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 1's hand-over: `MyBoarding` as `sbs create` made it, the
borrowed scene and its card given back ("start", the same as c3-01's "start"). The roster
is typed in two parts ("r1a", "r1"), then the three rooms ("r2", where lint warns), then
Close Inspection among the quests ("r3"), then the card ("final", the page's own
example\\, both files).

GAME STILLS. Not taken yet; no marks until the screenshots exist. ONE game, THREE windows:
`python game.py c3-02-party-and-place start --state final --consoles server,helm,engineering`.
No probe patch: Helm flies to the hulk, 9000 out. Helm is whoever the game names; the
Engineering console is Chief Okoro (the roster). The visit is played on Engineering, on
the HANDHELD: BEAM DOWN turns the console into the xESS (a bar with name, job and room
over the Act app: the room's line, kept as a running page, with the choices as buttons).
Press order:
  1. Engineering, at once: game_l2_eng_start (the name at the top, beside the handheld icon).
  2. Helm: the handheld icon (top left), Quests, Close Inspection: game_l2_log. Close it.
  3. Helm: fly inside 500 of the Unknown Hulk: game_l2_complete (the strip line).
  4. Engineering: the handheld icon: game_l2_tile. Boarding Party: game_l2_app.
  5. Engineering: BEAM DOWN: game_l2_airlock. Go aft, toward the reactor: game_l2_reactor.
  6. Go back to the airlock, Go forward, to the bridge: game_l2_bridge.
  7. Go back to the airlock: game_l2_back. Return to the ship: game_l2_home.
"""
LECTURE = "c3-02-party-and-place"
TITLE = ("Class 3, Lecture 2", "A party and a place", "Who goes, where they go, and the lines that start it")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-02-party-and-place/example"
_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hulk"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hulk")]
_WATCH = ("\n\n## [The Watch](watch)\n---\ncrew\nShip: Artemis\nNames: locked\n---\n"
          "The people aboard for this story.\n")
_PEOPLE = ("\n### [Chief Okoro](okoro)\n---\nConsole: engineering\nFace: terran_male\nRoles: engineering\n---\n"
           "\n### [Dr Hale](hale)\n---\nConsole: science\nFace: terran_female\nRoles: medical\n---\n")
_ROOMS = ("\n\n## [Scenes](boarding)\n\n"
          "### [The Airlock](airlock)\n"
          "% The outer door was never sealed. Frost on the inside of the glass, and a row of suits still on their hooks.\n\n"
          "- [Go aft, toward the reactor](reactor)\n- [Go forward, to the bridge](bridge)\n- [Return to the ship]()\n\n"
          "### [The Reactor Room](reactor)\n"
          "% Cold. The core was shut down by hand, in the right order, by someone who had time.\n\n"
          "- [Go back to the airlock](airlock)\n\n"
          "### [The Bridge](bridge)\n"
          "% Every station is dark but one. The log is open on the captain's chair, and the last entry is a single word.\n\n"
          "- [Go back to the airlock](airlock)\n")
_STUDY = "Science should take a full scan of the hull.\n"
_QUEST = ("\n### [Close Inspection](approach)\n---\nScope: shared\nStarts when: at once\n"
          "Objective: Close to within 500 of the hulk\nDone when: reach derelict 500\n"
          "Then: signal board_hulk\nReward: 100 credits\n---\n"
          "![](ship://tsn_warpster) The Unknown Hulk, as DS 1's sensors see her.\n\n"
          "The hulk is not answering hails. Bring the ship in close and take a look.\n\n"
          "Inside 500, a boarding party can go across. Whoever goes, goes as themselves, so think about who you send.\n")
_CARD = ("\n\n#\n# Start the boarding visit. `Then: signal board_hulk` in mission.amd sends this signal\n"
         "# when the Close Inspection quest completes.\n#\n"
         "//shared/signal/board_hulk\n"
         "    party_ship = next(iter(role(\"__player__\")), None)\n"
         "    ->END if party_ship is None\n"
         "    boarding_visit(party_ship, dialogue_scenes(amd_section(MISSION_DOC, \"boarding\")), "
         "\"airlock\", title=\"The Hulk\")\n"
         "    ->END\n")

STATES = {
    # Lecture 1's hand-over: the mission as `sbs create` made it
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED},
    # Step 1: the roster, the section first and then the two people
    "r1a": {"base": "start", "edits": [("append", FILE, _WATCH)]},
    "r1": {"base": "r1a", "edits": [("append", FILE, _PEOPLE)]},
    # Step 2: the three rooms. Lint warns here (line 86, as the page says)
    "r2": {"base": "r1", "edits": [("append", FILE, _ROOMS)]},
    # Step 4: the quest, below Study the Derelict
    "r3": {"base": "r2", "edits": [("replace", FILE, _STUDY, _STUDY + _QUEST)]},
    # Step 4: and the card. The page's own example, both files.
    "final": {"base": "r3", "edits": [("append", MAST, _CARD)],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    # Exercise, step 6: a room with no way back. Lint says clean
    "b_noback": {"base": "final", "edits": [
        ("replace", FILE, "someone who had time.\n\n- [Go back to the airlock](airlock)\n", "someone who had time.\n")]},
}

_LINT = "sbs lint MyBoarding"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    "e_end0": ("vscode", "start", 50, "big", _NS),        # lines 40 to 60: the end of the file
    "e_r1a": ("vscode", "r1a", 70, "big", _NS),           # lines 60 to 70: the roster section, the last line of the file (line 73 is not there yet)
    "e_r1": ("vscode", "r1", 73, "big", _NS),             # the same lines: the two people under it
    "e_r2": ("vscode", "r2", 94, "big", _NS),             # lines 84 to 104: the three rooms
    "e_r3": ("vscode", "r3", 47, "big", _NS),             # lines 37 to 57: Close Inspection
    "m_end0": ("vscode", "start", 95, "big", _M),         # lines 85 to 105: the end of story.mast
    "m_card": ("vscode", "final", 106, "big", _M),        # lines 96 to 116: the card
    "t_r1": ("terminal", [("r1", _LINT)]),
    "t_r2": ("terminal", [("r2", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_noback": ("terminal", [("b_noback", _LINT)]),
    # THE REAL GAME (not taken yet). State final, consoles server,helm,engineering (see the docstring)
    "game_l2_eng_start": ("game", "Engineering at the start (state final), before Helm moves: the name Chief Okoro at the top of the console, beside the handheld icon"),
    "game_l2_log": ("game", "Helm, the handheld icon (top left), then Quests, Close Inspection selected: State Active, Reward 100 credits, the order 'Close to within 500 of the hulk', the hulk's picture with 'The Unknown Hulk, as DS 1's sensors see her.', and the two paragraphs"),
    "game_l2_complete": ("game", "Helm, the ship inside 500 of the Unknown Hulk: the strip line 'Quest complete: Close Inspection'"),
    "game_l2_tile": ("game", "Engineering, just after Close Inspection completes: the handheld icon pressed, the page of tiles with the Boarding Party tile and its line 'The Hulk'"),
    "game_l2_app": ("game", "Engineering, the Boarding Party tile pressed: 'Going down to The Hulk', Chief Okoro's face and name, engineering, and the BEAM DOWN button"),
    "game_l2_airlock": ("game", "Engineering, BEAM DOWN pressed: the handheld (xESS) on its Act app. The bar: Chief Okoro, then engineering and The Airlock. The airlock's line, and three buttons: Go aft, toward the reactor; Go forward, to the bridge; Return to the ship"),
    "game_l2_reactor": ("game", "Engineering's handheld after Go aft, toward the reactor: the page keeps the airlock's line, then Chief Okoro and his choice, then the reactor room's line and its one button, Go back to the airlock. The bar reads The Reactor Room"),
    "game_l2_bridge": ("game", "Engineering's handheld after Go back to the airlock, then Go forward, to the bridge: the bridge's line and its one button, Go back to the airlock, under the page so far. The bar reads The Bridge"),
    "game_l2_back": ("game", "Engineering's handheld after Go back to the airlock from the bridge: the bar reads The Airlock, the airlock's line at the foot of the page again, and its three buttons"),
    "game_l2_home": ("game", "Engineering, Return to the ship pressed: the console back at its Engineering screen with no other press, the name Chief Okoro at the top"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_rules": ("card", "list", {"heading": "Step 3 - Two rules for a place", "kicker": "Two rules for a place"}),
    # the page's table under Step 4, as rows: table_of stops at the card's `#` comment lines inside the code block
    "card_three": ("card", "rows", {"kicker": "Three things on the card are yours", "header": ["On the card", "Change it to"],
                                    "rows": [["board_hulk (on the card, and in your quest's Then: line)", "The signal name your quest sends"],
                                             ["\"airlock\"", "The key of the room the party arrives in"],
                                             ["\"The Hulk\"", "What the crew should see as the name of the place"]]}),
    "card_cannot": ("card", "table", {"heading": "Step 5 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (1, 2)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A fourth room, a third person"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 3", "sub": "Everyone gets a menu"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l2_airlock"},
        {"from": 3, "still": "game_l2_eng_start"},
        {"from": 4, "still": "game_l2_airlock"},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_your_crew": {"step": 1, "beats": [
        # the game first: the name on the Engineering console
        {"from": 0, "still": "game_l2_eng_start"},
        {"from": 3, "still": "e_end0", "marks": [("lines", 55, 60)]},
        {"from": 4, "still": "e_r1a", "marks": [("lines", 65, 65)]},
        {"from": 5, "still": "e_r1a", "marks": [("lines", 66, 66)]},
        {"from": 6, "still": "e_r1a", "marks": [("lines", 67, 67)]},
        {"from": 7, "still": "e_r1", "marks": [("lines", 71, 83)]},
        {"from": 8, "still": "e_r1", "marks": [("lines", 73, 73)]},
        {"from": 9, "still": "e_r1", "marks": [("lines", 74, 75)]},
        {"from": 10, "still": "game_l2_eng_start"},
        {"from": 11, "still": "e_r1", "marks": [("lines", 71, 76)]},
        {"from": 12, "still": "t_r1", "marks": [("part", "run1:clean")]},
    ]},
    "s03_the_place": {"step": 2, "beats": [
        # the game first: the room on the handheld
        {"from": 0, "still": "game_l2_airlock"},
        {"from": 3, "still": "e_r2", "marks": [("lines", 88, 93)]},
        {"from": 4, "still": "e_r2", "marks": [("lines", 86, 86)]},
        {"from": 5, "still": "e_r2", "marks": [("lines", 88, 88)]},
        {"from": 7, "still": "e_r2", "marks": [("lines", 89, 89)]},
        {"from": 8, "still": "e_r2", "marks": [("lines", 91, 93)]},
        {"from": 9, "still": "e_r2", "marks": [("text", 91, "[Go aft, toward the reactor]")]},
        {"from": 10, "still": "e_r2", "marks": [("text", 91, "(reactor)")]},
        {"from": 11, "still": "e_r2", "marks": [("text", 93, "()")]},
        {"from": 12, "still": "game_l2_airlock"},
        {"from": 13, "still": "e_r2", "marks": [("lines", 93, 93)]},
    ]},
    "s04_lint_notices": {"step": 2, "beats": [
        {"from": 0, "still": "t_r2"},
        {"from": 2, "still": "t_r2", "marks": [("span", 1, "section-not-loaded")]},
        {"from": 3, "still": "t_r2", "marks": [("span", 1, "boarding")]},
        {"from": 5, "still": "e_r2", "marks": [("text", 86, "(boarding)")]},
    ]},
    "s05_two_rules": {"step": 3, "beats": [
        {"from": 0, "still": "card_rules"},
        {"from": 1, "still": "card_rules", "marks": [("part", "item1")]},
        # the game first: the one button in the reactor room
        {"from": 2, "still": "game_l2_reactor"},
        {"from": 4, "still": "e_r2", "marks": [("lines", 98, 98), ("lines", 103, 103)]},
        {"from": 5, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 7, "still": "e_r2", "marks": [("lines", 93, 93)]},
        {"from": 9, "still": "game_l2_airlock"},
        {"from": 10, "still": "e_r2", "marks": [("lines", 88, 93)]},
    ]},
    "s06_start_it": {"step": 4, "beats": [
        # the game first: the step in Helm's Quest Log
        {"from": 0, "still": "game_l2_log"},
        {"from": 3, "still": "e_r3", "marks": [("lines", 41, 54)]},
        {"from": 4, "still": "e_r3", "marks": [("lines", 46, 46)]},
        {"from": 5, "still": "e_r3", "marks": [("lines", 47, 47)]},
        {"from": 7, "still": "e_r3", "marks": [("text", 47, "board_hulk")]},
        {"from": 8, "still": "e_r3", "marks": [("lines", 50, 54)]},
        {"from": 9, "still": "e_r3", "marks": [("lines", 50, 50)]},
        {"from": 10, "still": "e_r3", "marks": [("lines", 52, 54)]},
        {"from": 11, "still": "e_r3", "marks": [("lines", 54, 54)]},
        # the game first: the tile the card makes
        {"from": 13, "still": "game_l2_tile"},
        {"from": 15, "still": "m_end0", "marks": [("lines", 103, 105)]},
        {"from": 16, "still": "m_card", "marks": [("lines", 108, 116)]},
        {"from": 17, "still": "card_three"},
        {"from": 18, "still": "m_card", "marks": [("text", 112, "board_hulk")]},
        {"from": 19, "still": "m_card", "marks": [("text", 115, "\"airlock\"")]},
        {"from": 20, "still": "card_three", "marks": [("part", "r3")]},       # "The Hulk" is past the window's right edge
        {"from": 21, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s07_play_it": {"step": 6, "beats": [
        {"from": 0, "still": "game_l2_eng_start"},
        {"from": 2, "still": "game_l2_complete"},
        {"from": 4, "still": "game_l2_tile"},
        {"from": 5, "still": "game_l2_app"},
        {"from": 6, "still": "game_l2_airlock"},
        {"from": 9, "still": "game_l2_reactor"},
        {"from": 10, "still": "game_l2_bridge"},
        {"from": 11, "still": "game_l2_back"},
        {"from": 12, "still": "game_l2_home"},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item6")]},
        {"from": 4, "still": "t_noback", "marks": [("part", "run1:clean")]},
        {"from": 5, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_next"},
    ]},
}
