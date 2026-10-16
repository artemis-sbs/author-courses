"""Storyboard for c3-01-what-a-boarding-party-is: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

Class 3 does not build on MyMission. This lecture makes `MyBoarding` with
`sbs create MyBoarding -t amd --title "The Hulk"` ("start": Class 1 Lecture 3's example,
which is what `sbs create` makes, with the title the page gives). Then two blocks are
pasted: the Scenes section of Open Universe's quiet_shore.amd ("p1"), and a card at the
end of story.mast ("final", the page's own example\\, both files). Stop 6 deletes both
again, so the lecture ends on "start".

The shipped file is never opened: the student does not need Open Universe, and the stand-in
does not have it. Scene 6 shows the page's own excerpts as cards (the order of the parts is
the shipped file's, checked against quiet_shore.amd, 211 lines, 2026-10-15).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. ONE game,
TWO windows:
`python game.py c3-01-what-a-boarding-party-is start --state final --consoles server,helm`.
No probe patch: the hulk stays 9000 out and Helm flies to it (about a minute at full
impulse), so somebody is seated at a console when the visit opens. (If the visit opened
with nobody seated, nobody would be offered the covering choices: a known library defect.)
A boarding visit is played on the HANDHELD: BEAM DOWN turns the console into the xESS, an
identity bar (name; job and the room) over the Act app, which shows the room's line as a
running page with the choices as buttons in the text. Press order, all on Helm:
  1. Zoom the map out once (the magnifier above it): game_l1_helm_start. The hulk is an
     unnamed mark at 22, 8K; it is named only within about 4K. Fly to it; stop inside 2000.
  2. game_l1_near once 'Quest complete: Find the Derelict' shows on the strip.
  3. the handheld icon (top left): game_l1_tile. Press Boarding Party: game_l1_app.
  4. BEAM DOWN: game_l1_field.
  5. 'Look at the people meeting you (covering for medical)': game_l1_medic. Say it out loud.
  6. Walk in with her: game_l1_hall. Ask to see the east cable: game_l1_cable_shut.
  7. Walk back to the hall; take 'Look at what is heating this room (covering for
     engineering)', Say it out loud, then 'Look at the far end (covering for security)', Say
     it out loud (three things found: thin, idle, tended). Ask to see the east cable:
     game_l1_cable_open.
"""
LECTURE = "c3-01-what-a-boarding-party-is"
TITLE = ("Class 3, Lecture 1", "What a boarding party is", "Ten minutes in a colony that says it is fine")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-01-what-a-boarding-party-is/example"
# `sbs create ... --title "The Hulk"` names the mission in description.yaml (Class 1 used "The Cold Hulk")
_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hulk"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hulk")]
_CARD = ("\n\n#\n# LECTURE 1 ONLY. When the ship finds the derelict, open a boarding visit.\n#\n"
         "//shared/signal/quest_signal if SIGNAL_NAME == \"derelict_found\"\n"
         "    party_ship = next(iter(role(\"__player__\")), None)\n"
         "    ->END if party_ship is None\n"
         "    boarding_visit(party_ship, dialogue_scenes(amd_section(MISSION_DOC, \"boarding\")), "
         "\"arrival\", title=\"Ferrow Landing\")\n"
         "    ->END\n")

STATES = {
    # Stop 1: the mission as `sbs create` makes it. It is also where Stop 6 ends.
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED},
    # Stop 2: the borrowed scene pasted, and no card yet
    "p1": {"folder": "c1-03-editor-and-first-run/example", "over": (_EX,),
           "edits": _TITLED + [("replace", MAST, _CARD, "")]},
    # Stop 2: and the card. The page's own example, both files.
    "final": {"folder": "c1-03-editor-and-first-run/example", "over": (_EX,), "edits": _TITLED,
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    # Stop 6, the slip: the scene given back and the card left behind
    "b_card": {"base": "start", "edits": [("append", MAST, _CARD)]},
}

_LINT = "sbs lint MyBoarding"
_CREATE = 'sbs create MyBoarding -t amd --title "The Hulk"'
_FETCH = 'sbs fetch "MyBoarding" --update-libs'
_MAKE = [(_CREATE, ("",)), _FETCH, _LINT]
_NO = {"without": ("MyBoarding",)}
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # Stop 1: one real cmd.exe session, with no MyBoarding before it (what it makes is thrown away)
    "t_create": ("session", _MAKE, dict(_NO, show=(1, 1))),
    "t_fetch": ("session", _MAKE, dict(_NO, show=(2, 2), tail=14)),
    "t_lint0": ("session", _MAKE, dict(_NO, show=(3, 3))),
    "v_folder": ("vscode", "start", 1, "wide"),             # the folder open and trusted, its seven files
    "e_end0": ("vscode", "start", 50, "big", _NS),          # lines 40 to 60: the end of the file, Derelict Materials
    "m_end0": ("vscode", "start", 95, "big", _M),           # lines 85 to 105: the end of story.mast
    # Stop 2: the block, and the card
    "e_field": ("vscode", "final", 73, "big", _NS),         # lines 63 to 83: the Scenes heading, The Landing Field
    "e_mid1": ("vscode", "final", 110, "mid", _NS),         # about lines 96 to 124: the block, scrolled
    "e_cable": ("vscode", "final", 140, "big", _NS),        # lines 130 to 150: The East Cable
    "m_card": ("vscode", "final", 105, "big", _M),          # lines 95 to 115: the card
    "t_p1": ("terminal", [("p1", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    # Stop 6: given back
    "e_back": ("vscode", "start", 50, "big", _NS),          # the same lines as e_end0: the file ends at 60 again
    "m_back": ("vscode", "start", 95, "big", _M),
    "t_back": ("terminal", [("start", _LINT)]),
    "t_card": ("terminal", [("b_card", _LINT)]),
    # THE REAL GAME (taken 2026-10-15). State final, consoles server,helm, all on Helm (see the docstring)
    "game_l1_helm_start": ("game", "Helm at the start (state final, no patch), the map zoomed out once: the ship by DS 1, the hulk an unnamed mark at 22, 8K"),
    "game_l1_near": ("game", "Helm, the ship stopped inside 2000 of the Unknown Hulk: the hulk close on the map, and the strip line 'Quest complete: Find the Derelict'"),
    "game_l1_tile": ("game", "Helm, the handheld icon (top left) pressed, just after Find the Derelict completes: the page of tiles, with the Boarding Party tile and its line 'Ferrow Landing' ('Boarding Party' on the tile is cut to 'Boardin': awaiting a re-shoot after the library fix)"),
    "game_l1_app": ("game", "Helm, the Boarding Party tile pressed: 'Going down to Ferrow Landing', the Helm officer's own face and name, the job helm, and the BEAM DOWN button."),
    "game_l1_field": ("game", "Helm, BEAM DOWN pressed: the handheld (xESS) on its Act app. The bar: the officer's name and helm at the left, The Landing Field at the right. One of the room's two lines, and six buttons: Walk in with her and Beam back up FIRST, then four ending '(covering for medical)', '(covering for engineering)', '(covering for security)', '(covering for science)'"),
    "game_l1_medic": ("game", "Helm's handheld after 'Look at the people meeting you (covering for medical)': the page keeps the landing field's line, then who chose and the choice (with no covering words), then one of The People Meeting You's two lines and its one button, Say it out loud"),
    "game_l1_hall": ("game", "Helm's handheld after Say it out loud, then Walk in with her: the bar reads The Long Hall; one of its two lines; six buttons (Ask to see the east cable, Beam back up, then the four covering)"),
    "game_l1_cable_shut": ("game", "Helm's handheld, Ask to see the east cable pressed with ONE thing found (only the medic's reading taken): the bar reads The East Cable; its line; the buttons Ask her plainly what is in the shed, Let her show you the orchard, Walk back to the hall, Beam back up, and NO Open it"),
    "game_l1_cable_open": ("game", "Helm's handheld at The East Cable again, after the engineering and security covering readings in the long hall (three things found): Open it is now the second button"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_why": ("card", "points", {"kicker": "A mission of its own", "items": [
        "Class 1's story ends the game ten minutes after it starts",
        "A boarding party should be allowed to take its time"]}),
    "card_file": ("card", "points", {"kicker": "quiet_shore.amd, as it ships: 211 lines", "items": [
        "A page of the author's notes",
        "Voices: Administrator Bel",
        "Hails: the call that starts the visit",
        "Scenes: the fourteen rooms you pasted, each with Speaker: bel"]}),
    "card_note": ("card", "page", {"kicker": "One of the author's notes", "text": [
        "Every room is REVERSIBLE, not just exitable. The east cable used to offer only two flavour "
        "loops and a gated shed, so a party that walked there under-informed could go back to nothing - "
        "the only way out was off the planet. A room whose options all loop is a dead end however many "
        "of them there are. Every room now leads BACK as well as on."],
        "find": ("Every room now leads BACK as well as on.", "used to offer only two flavour loops")}),
    "card_voice": ("card", "rows", {"kicker": "A voice, and the fence every room had",
                                    "header": ["In the shipped file", "It is"],
                                    "rows": [["### [Administrator Bel](bel)", "A record in the Voices section"],
                                             ["Face: terran_female", "Her face"],
                                             ["Roles: narrator", "What she is for"],
                                             ["Color: \"#fd8\"", "The color of her lines"],
                                             ["Speaker: bel", "In a fence on every room: the lines are hers"]]}),
    "card_call": ("card", "rows", {"kicker": "The call that starts it", "header": ["In the shipped file", "It is"],
                                   "rows": [["### [Ferrow Landing Answers](shore_call)", "A call, in the Hails section"],
                                            ["Speaker: bel", "Who calls"],
                                            ["Title: Ferrow Landing", "What the call is about"],
                                            ["% Ferrow Landing here, and you are very welcome. We are all fine. Nothing needed, nothing to report.", "One of the two things she says"],
                                            ["- [Assemble a boarding party]() ; signal boarding_down", "The answer that opens the scene"],
                                            ["- [Thank her and stay aboard]()", "The answer that does not"]]}),
    "card_cut": ("card", "table", {"heading": "What was cut, and why", "kicker": "What was cut, and why"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Before you give it back"}),
    "card_questions": ("card", "points", {"kicker": "From the file alone, with the game closed", "items": [
        "Which rooms can the party reach from the landing field without finding anything out?",
        "Which two choices teach tended? Whose jobs are they?",
        "A party of one engineer: which choices in the long hall are marked as covering?"]}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 2", "sub": "A party and a place"}),
}

_FIELD = ("lines", 65, 74)       # e_field: The Landing Field

# Game stills, 1280x960, marks as fractions of the frame (taken 2026-10-15)
_HS_ZOOM = ("rect", 0.385, 0.045, 0.44, 0.115)       # game_l1_helm_start: the magnifier pressed once
_HS_HULK = ("rect", 0.57, 0.24, 0.625, 0.33)         # ... the hulk, an unnamed mark at 22, 8K
_HN_HULK = ("rect", 0.465, 0.455, 0.575, 0.525)      # game_l1_near: 'Unknown Hulk', 1824 off
_HN_STRIP = ("rect", 0.015, 0.49, 0.275, 0.53)       # ... 'Quest complete: Find the Derelict'
_HN_SPD = ("rect", 0.02, 0.565, 0.1, 0.6)            # ... SPD 0.01
_TI_TILES = ("rect", 0.0, 0.12, 0.99, 0.79)          # game_l1_tile: the page of tiles
_TI_BOARD = ("rect", 0.0, 0.155, 0.325, 0.335)       # ... the Boarding Party tile, Ferrow Landing
_AP_HEAD = ("rect", 0.03, 0.06, 0.35, 0.1)           # game_l1_app: 'Boarding Party' 'Ferrow Landing'
_AP_BEAM = ("rect", 0.02, 0.235, 0.98, 0.29)         # ... BEAM DOWN
_FI_BAR = ("rect", 0.005, 0.06, 0.99, 0.13)          # game_l1_field: the bar
_FI_ROOM = ("rect", 0.655, 0.095, 0.79, 0.128)       # ... the room, The Landing Field
_FI_LINE = ("rect", 0.01, 0.21, 0.59, 0.245)         # ... the room's line
_FI_ALL = ("rect", 0.01, 0.2, 0.74, 0.42)            # ... the line and the six buttons
_FI_PLAIN = ("rect", 0.01, 0.26, 0.302, 0.31)        # ... Walk in with her, Beam back up (first)
_FI_COVER = [("rect", 0.305, 0.26, 0.735, 0.31),     # ... the four covering choices, after them
             ("rect", 0.01, 0.315, 0.73, 0.418)]
_FI_MED = ("rect", 0.305, 0.26, 0.735, 0.31)         # ... '(covering for medical)'
_ME_FOUND = ("rect", 0.01, 0.39, 0.915, 0.49)        # game_l1_medic: what a medic notices, Say it out loud
_ME_PICK = ("rect", 0.01, 0.255, 0.28, 0.37)         # ... the pick, with no covering words
_HA_ROOM = ("rect", 0.655, 0.095, 0.76, 0.128)       # game_l1_hall: The Long Hall
_HA_COVER = ("rect", 0.01, 0.8, 0.825, 0.955)        # ... the hall's buttons, covering ones last
_CS_ROOM = ("rect", 0.655, 0.095, 0.765, 0.128)      # game_l1_cable_shut: The East Cable
_CS_CHIPS = ("rect", 0.01, 0.93, 0.87, 0.98)         # ... four buttons, no Open it
_CO_OPEN = ("rect", 0.297, 0.932, 0.383, 0.98)       # game_l1_cable_open: Open it
_CO_BEAM = ("rect", 0.825, 0.932, 0.96, 0.98)        # ... Beam back up

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        # the game first: the Helm console, now the handheld
        {"from": 0, "still": "game_l1_field"},
        {"from": 1, "still": "game_l1_helm_start"},
        {"from": 2, "still": "game_l1_field", "marks": [_FI_BAR]},
        {"from": 3, "still": "game_l1_field", "marks": [_FI_ROOM]},
        {"from": 4, "still": "game_l1_field", "marks": [_FI_LINE]},
        {"from": 5, "still": "e_mid1"},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_a_mission_for_this_class": {"step": None, "beats": [
        {"from": 0, "still": "card_why"},
        {"from": 2, "still": "card_why", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_why", "marks": [("part", "item2")]},
        {"from": 4, "still": "t_create"},
        {"from": 6, "still": "t_fetch"},
        {"from": 7, "still": "v_folder"},
        {"from": 8, "still": "t_lint0", "marks": [("part", "run1:clean")]},
    ]},
    "s03_borrow_a_scene": {"step": None, "beats": [
        # the game first: the room on the handheld
        {"from": 0, "still": "game_l1_field"},
        {"from": 3, "still": "game_l1_field", "marks": [_FI_ROOM]},
        {"from": 4, "still": "game_l1_field", "marks": [_FI_ALL]},
        {"from": 6, "still": "e_end0", "marks": [("lines", 55, 60)]},
        {"from": 7, "still": "e_field", "marks": [("lines", 63, 74)]},
        {"from": 8, "still": "e_mid1"},
        {"from": 9, "still": "t_p1", "marks": [("span", 1, "section-not-loaded")]},
        {"from": 10, "still": "t_p1", "marks": [("span", 1, "boarding")]},
        # the game first: the tile that names the visit
        {"from": 12, "still": "game_l1_tile", "marks": [_TI_TILES]},
        {"from": 13, "still": "game_l1_tile", "marks": [_TI_BOARD]},
        {"from": 15, "still": "m_end0", "marks": [("lines", 103, 105)]},
        {"from": 16, "still": "m_card", "marks": [("lines", 108, 115)]},
        {"from": 17, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s04_play_it": {"step": None, "beats": [
        {"from": 0, "still": "game_l1_helm_start"},
        {"from": 2, "still": "game_l1_helm_start", "marks": [_HS_ZOOM]},
        {"from": 3, "still": "game_l1_helm_start", "marks": [_HS_HULK]},
        {"from": 5, "still": "game_l1_near", "marks": [_HN_HULK]},
        {"from": 6, "still": "game_l1_near", "marks": [_HN_STRIP]},
        {"from": 7, "still": "game_l1_near", "marks": [_HN_SPD]},
        {"from": 8, "still": "game_l1_tile"},
        {"from": 9, "still": "game_l1_tile", "marks": [_TI_BOARD]},
        {"from": 9.6, "still": "game_l1_app", "marks": [_AP_BEAM]},
        {"from": 10, "still": "game_l1_field", "marks": [_FI_BAR]},
        {"from": 11, "still": "game_l1_field", "marks": [_FI_PLAIN]},
        {"from": 12, "still": "game_l1_field", "marks": _FI_COVER},
        {"from": 15, "still": "game_l1_field", "marks": [_FI_MED]},
        {"from": 16, "still": "game_l1_medic", "marks": [_ME_FOUND]},
        {"from": 17, "still": "game_l1_medic", "marks": [_ME_PICK]},
        {"from": 19, "still": "game_l1_hall", "marks": [_HA_ROOM]},
        {"from": 20, "still": "game_l1_cable_shut", "marks": [_CS_ROOM]},
        {"from": 21, "still": "game_l1_cable_shut", "marks": [_CS_CHIPS]},
        {"from": 23, "still": "game_l1_hall", "marks": [_HA_COVER]},
        {"from": 24, "still": "game_l1_cable_open", "marks": [_CO_OPEN]},
    ]},
    "s05_read_what_you_pasted": {"step": None, "beats": [
        # the game first: the room as the crew sees it
        {"from": 0, "still": "game_l1_field"},
        {"from": 2, "still": "game_l1_field", "marks": [_FI_ROOM, _FI_ALL]},
        {"from": 3, "still": "e_field", "marks": [("hashes", 63)]},
        {"from": 4, "still": "e_field", "marks": [_FIELD]},
        {"from": 5, "still": "e_field", "marks": [("lines", 65, 65)]},
        {"from": 6, "still": "e_field", "marks": [("text", 66, "%"), ("text", 67, "%")]},
        {"from": 8, "still": "e_field", "marks": [("lines", 66, 67)]},
        {"from": 9, "still": "game_l1_field", "marks": [_FI_LINE]},
        {"from": 10, "still": "e_field", "marks": [("lines", 69, 74)]},
        {"from": 11, "still": "e_field", "marks": [("text", 73, "[Walk in with her]")]},
        {"from": 12, "still": "e_field", "marks": [("text", 73, "(hall)")]},
        {"from": 13, "still": "e_field", "marks": [("text", 69, "if medical >= 1")]},
        {"from": 15, "still": "game_l1_field", "marks": [_FI_MED]},
        {"from": 16, "still": "e_field", "marks": [("text", 69, "; learn thin")]},
        # the game first: the door, shut and then open
        {"from": 18, "still": "game_l1_cable_shut", "marks": [_CS_CHIPS]},
        {"from": 19, "still": "game_l1_cable_open", "marks": [_CO_OPEN]},
        {"from": 20, "still": "e_cable", "marks": [("lines", 141, 141)]},
        {"from": 21, "still": "e_cable", "marks": [("text", 141, "if learned >= 3")]},
        {"from": 22, "still": "e_cable", "marks": [("text", 144, "()")]},
        {"from": 24, "still": "game_l1_cable_open", "marks": [_CO_BEAM]},
    ]},
    "s06_read_the_rest_of_the_file": {"step": None, "beats": [
        {"from": 0, "still": "card_file"},
        {"from": 1, "still": "card_file", "marks": [("part", "item4")]},
        {"from": 2, "still": "card_file", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_note", "marks": [("part", "find1")]},
        {"from": 4, "still": "card_note", "marks": [("part", "find2")]},
        {"from": 5, "still": "card_voice"},
        {"from": 7, "still": "card_call"},
        {"from": 9, "still": "card_cut"},
    ]},
    "s07_give_it_back": {"step": None, "beats": [
        {"from": 0, "still": "e_field"},
        {"from": 1, "still": "e_field", "marks": [("lines", 63, 74)]},
        {"from": 2, "still": "e_back", "marks": [("lines", 60, 60)]},
        {"from": 3, "still": "m_card", "marks": [("lines", 108, 115)]},
        {"from": 4, "still": "m_back", "marks": [("lines", 105, 105)]},
        {"from": 5, "still": "t_back", "marks": [("part", "run1:clean")]},
        {"from": 6, "still": "t_card", "marks": [("part", "run1:clean")]},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 5, "still": "card_questions"},
        {"from": 7, "still": "card_next"},
    ]},
}
