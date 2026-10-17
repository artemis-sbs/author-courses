"""Storyboard for c4-06-clues-side-stories-cutscenes: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12 and in _tools/picture/README.md. Caption numbers are those of shots.py.

The lecture starts from Lecture 4's finished files, WITHOUT Lecture 5: `MyRuin` as `sbs create
MyRuin -t amd` made it, `mission.amd` replaced by c4-04's example (199 lines) and the template's
`story.mast` (105 lines, `relics_spawn` on line 62, with the `Prefab:` comment since 2026-10-17).
The steps are typed in the video's order: the ring plate, Marker Zero and Rook at the Ring
("plate", "mz", "ring"), the altar's new answer and the entry for Dace ("answer", "dace"), the
Crypt and the Cairn ("room"), `; reveal cairn` ("reveal"), the side story and `, accepts stayed`
("stayed", "accepts"), the Cutscenes section ("cuts": lint warns, line 275), the map line of the
card ("card_a": clean), `Then: signal cairn_found` ("card_b": lint warns, line 65), and the
block at the end of story.mast ("final", the page's own example, both files). Three breaks of
scene 9: "b_learn", "b_carin", "b_lower".

GAME STILLS. NOT TAKEN YET: they are planned here and are taken in one scouting sitting.
ONE game, THREE windows; the SERVER window must be on the main screen:
`python game.py c4-06-clues-side-stories-cutscenes start --state final --consoles server,helm,comms`.
No probe patch: Helm flies. Press order:
  1. Helm: fly from The Way In through The Mouth and the ring, inside 500 of The Ring Plate
     (1400, 0, 0). Comms: the call row "Surveyor Rook - A recording at the ring":
     game_c6_ring_row. Open it: game_c6_ring_call (the take, "Log the names." and "Shut it
     off."). Press "Log the names.".
  2. Helm: fly on across The Nave and up the tunnel to inside 600 of The Altar (3000, 0, 2800).
     Comms: open Rook at the Altar: game_c6_altar3 (three answers, "Play the entry keyed to
     Dace." in the middle).
  3. Comms: "Play the entry keyed to Dace.": game_c6_entry (the entry and its one answer). Press
     "Mark the side room.".
  4. Helm: the map: game_c6_map_cairn (The Cairn as a new contact on the far side of The Nave).
     Helm: the handheld icon, Quests: game_c6_quests (The One Who Stayed Active, with the
     small table of surveyors in its description).
  5. Comms: "Play the rest.", "Mark the Gallery.". Helm: fly back across The Nave and into
     The Crypt, inside 400 of The Cairn (5200, 0, 0). The SERVER window, the main screen:
       game_c6_shot1 (about 1 second in: black bars, the lower third 'The Altar' and 'The tally on
       the rim stops at forty-one.', the ship panel top left reading The Altar),
       game_c6_shot2 (about 6 seconds in: 'The Cairn' and 'Forty-one stones. One for each day.'),
       game_c6_after (about 12 seconds in: the ship's own view again, the bars gone).
No marks are set on the game stills yet: set them from the screenshots once they exist.
"""
LECTURE = "c4-06-clues-side-stories-cutscenes"
TITLE = ("Class 4, Lecture 6", "Clues, side stories and cutscenes", "A secret in the ruin, a story it starts, and a film")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-06-clues-side-stories-cutscenes/example"
_PLATE = ("### [The Ring Plate](plate)\n---\nRelic: hollow\nPoint: 1400, 0, 0\nRoles: plate\n---\n"
          "A metal plate bolted to the ring. The first survey left it.\n")
_CRYPT = ("### [The Crypt](crypt)\n---\nRelic: hollow\nChamber: 5200, 0, 0, 600\nPassage to: nave 250\n---\n"
          "A small side room off the Nave. The first survey's notes do not mention it.\n")
_CAIRN = ("### [The Cairn](cairn)\n---\nRelic: hollow\nPoint: 5200, 0, 0\nRoles: cairn\nHidden: yes\nDress: generic-cone 2\n---\n"
          "A pile of stones in the middle of the Crypt.\n")
_MZ = ("### [Marker Zero](marker_zero)\n---\nBeat\nStarts when: reach plate 500\nAction:\n  - rook hails rook_plate\n---\n"
       "The ship flies through the ring, and the plate on it starts to play.\n")
_STAYED = ("### [The One Who Stayed](stayed)\n---\nScope: shared\nStarts when: revealed\n"
           "Objective: Find the cairn in the side room off The Nave\nDone when: reach cairn 400\n---\n"
           "Five surveyors went into The Hollow. Four came out.\n\n"
           "| Surveyor | Came out |\n|---|---|\n| Rook, who led the survey | Yes |\n| Imre, Sato and Vell | Yes |\n| Dace | No |\n\n"
           "Rook says they built Dace a cairn in a side room off The Nave. Nobody has stood in that room since.\n")
_RING = ("### [Rook at the Ring](rook_plate)\n---\nSpeaker: rook\nWhen: hail\nTitle: A recording at the ring\n---\n"
         "% Marker zero. Five of us went in: Rook, Dace, Imre, Sato and Vell. The markers inside answer to our names.\n\n"
         "- [Log the names.]() ; learn names\n- [Shut it off.]()\n")
_DACE = ("### [The Entry for Dace](rook_dace)\n---\nSpeaker: rook\n---\n"
         "% Dace did not come out with us. We built her a cairn in the side room, off the Nave. Forty-one stones.\n\n"
         "- [Mark the side room.](rook_more)\n")
_CUTS = ("\n\n// ---- Cutscenes. What the main screen shows at a moment in the story.\n## [Cutscenes](cutscenes)\n\n"
         "### [At the Cairn](cairn_scene)\n---\nLetterbox: yes\n---\nPlayed when the crew finds the cairn.\n\n"
         "### [The count](cairn_shot_1)\n---\nCutscene: cairn_scene\nSubject: altar\nFraming: close\nSeconds: 4\n"
         "Overlay: lower_third\nName: The Altar\n---\nThe tally on the rim stops at forty-one.\n\n"
         "### [The stones](cairn_shot_2)\n---\nCutscene: cairn_scene\nSubject: cairn\nFraming: wide, close\nSeconds: 6\n"
         "Overlay: lower_third\nName: The Cairn\n---\nForty-one stones. One for each day.\n")
_MAPLINE = ("    # The cutscenes, if mission.amd has a Cutscenes section.\n"
            "    amd_cutscenes(amd_section(MISSION_DOC, \"cutscenes\"))\n\n")
_CARD = ("\n\n#\n# At the Cairn: the cutscene that plays when The One Who Stayed is finished.\n#\n"
         "//shared/signal/cairn_found\n    cutscene_amd(\"cairn_scene\", to=role(\"mainscreen\"))\n    ->END\n")
_OLD_P = ("    # The places, if mission.amd has a Landmarks section: each one with an `Art:` line is\n"
          "    # put in the game where its `Loc:` says. Before the quests, so a step that says")
_NEW_P = ("    # The places, if mission.amd has a Landmarks section: each one is made by its\n"
          "    # `Prefab:` where its `Loc:` says. Before the quests, so a step that says")

STATES = {
    # Lecture 4's files: the template's story.mast (as of 2026-10-17), c4-04's mission.amd
    "start": {"folder": "c1-03-editor-and-first-run/example", "over": ("c4-04-places-that-speak/example",),
              "edits": [("replace", MAST, _OLD_P, _NEW_P)]},
    # Step 2: the place on the ring, the beat, the scene
    "plate": {"base": "start", "edits": [
        ("replace", FILE, "A recess at the back of the Gallery. Easy to miss.\n\n",
         "A recess at the back of the Gallery. Easy to miss.\n\n" + _PLATE + "\n")]},
    "mz": {"base": "plate", "edits": [
        ("replace", FILE, "the old survey marker starts to play.\n\n", "the old survey marker starts to play.\n\n" + _MZ + "\n")]},
    "ring": {"base": "mz", "edits": [
        ("replace", FILE, "### [At the Altar](altar_look)\n", _RING + "\n### [At the Altar](altar_look)\n")]},
    # Step 3: the altar's new answer, and the entry it leads to
    "answer": {"base": "ring", "edits": [
        ("replace", FILE, "- [Play the rest.](rook_more)\n",
         "- [Play the rest.](rook_more)\n- [Play the entry keyed to Dace.](rook_dace) if learned >= 1\n")]},
    "dace": {"base": "answer", "edits": [
        ("replace", FILE, "### [At the Altar](altar_look)\n", _DACE + "\n### [At the Altar](altar_look)\n")]},
    # Step 4: the side room and the place in it, then the answer shows it
    "room": {"base": "dace", "edits": [
        ("replace", FILE, "The first survey left it.\n\n", "The first survey left it.\n\n" + _CRYPT + "\n"),
        ("replace", FILE, "do not mention it.\n\n", "do not mention it.\n\n" + _CAIRN + "\n")]},
    "reveal": {"base": "room", "edits": [
        ("replace", FILE, "- [Mark the side room.](rook_more)\n", "- [Mark the side room.](rook_more) ; reveal cairn\n")]},
    # Step 5: the side story, and the answer starts it
    "stayed": {"base": "reveal", "edits": [
        ("replace", FILE, "the plate on it starts to play.\n\n", "the plate on it starts to play.\n\n" + _STAYED + "\n")]},
    "accepts": {"base": "stayed", "edits": [
        ("replace", FILE, "; reveal cairn\n", "; reveal cairn, accepts stayed\n")]},
    # Step 6: the Cutscenes section. Lint warns: nothing reads it (line 275)
    "cuts": {"base": "accepts", "edits": [("append", FILE, _CUTS)]},
    # Step 7: part one of the card, in the map block (lint clean)
    "card_a": {"base": "cuts", "edits": [
        ("replace", MAST, "    relics_spawn(get_mission_dir_filename(\"mission.amd\"))\n\n",
         "    relics_spawn(get_mission_dir_filename(\"mission.amd\"))\n\n" + _MAPLINE)]},
    # Step 7: the quest sends the word (lint warns: nothing hears it, line 65)
    "card_b": {"base": "card_a", "edits": [
        ("replace", FILE, "Done when: reach cairn 400\n", "Done when: reach cairn 400\nThen: signal cairn_found\n")]},
    # Step 7: part two, the block at the end of story.mast. The page's own example, both files.
    "final": {"base": "card_b", "edits": [("append", MAST, _CARD)],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    # Step 8: three breaks, each undone
    "b_learn": {"base": "final", "edits": [("replace", FILE, "if learned >= 1", "if learned => 1")]},
    "b_carin": {"base": "final", "edits": [("replace", FILE, "Subject: cairn\n", "Subject: carin\n")]},
    "b_lower": {"base": "final", "edits": [
        ("replace", FILE, "Overlay: lower_third\nName: The Altar", "Overlay: lowerthird\nName: The Altar")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

STILLS = {
    # The editor. Each window shows the 20 lines round the line named.
    "e_plate": ("vscode", "plate", 158, "big", _NS),         # lines 148 to 168: the Ring Plate below the Niche
    "e_mz": ("vscode", "mz", 54, "big", _NS),                # lines 44 to 64: Marker Zero below Marker One
    "e_ring": ("vscode", "ring", 211, "big", _NS),           # lines 201 to 221: Rook at the Ring
    "e_answer": ("vscode", "answer", 195, "big", _NS),       # lines 185 to 205: the altar's middle answer
    "e_dace": ("vscode", "dace", 222, "big", _NS),           # lines 212 to 232: The Entry for Dace
    "e_room": ("vscode", "room", 178, "big", _NS),           # lines 168 to 188: The Crypt and The Cairn
    "e_room_k": ("vscode", "reveal", 180, "big", _NS),       # lines 170 to 190: the same, once the answer shows it
    "e_reveal": ("vscode", "reveal", 242, "big", _NS),       # lines 232 to 252: `; reveal cairn`
    "e_stayed": ("vscode", "stayed", 66, "big", _NS),        # lines 56 to 76: The One Who Stayed
    "e_accepts": ("vscode", "accepts", 259, "big", _NS),     # lines 249 to 269: `, accepts stayed`
    "e_cuts_a": ("vscode", "cuts", 283, "big", _NS),         # lines 273 to 293: the section, the cutscene, shot 1
    "e_cuts_b": ("vscode", "cuts", 293, "big", _NS),         # lines 283 to 303: shot 1 and shot 2
    "m_map": ("vscode", "card_a", 65, "big", _M),            # lines 55 to 75 of story.mast: the map line under relics_spawn
    "e_then": ("vscode", "card_b", 65, "big", _NS),          # lines 55 to 75: `Then: signal cairn_found`
    "m_end": ("vscode", "final", 113, "big", _M),            # lines 103 to 116 of story.mast: the block at the end
    "e_learn": ("vscode", "b_learn", 231, "big", _NS),       # lines 221 to 241: `if learned => 1`
    "e_carin": ("vscode", "b_carin", 298, "big", _NS),       # lines 288 to 304: `Subject: carin`
    "e_lower": ("vscode", "b_lower", 290, "big", _NS),       # lines 280 to 300: `Overlay: lowerthird`
    "t_cuts": ("terminal", [("cuts", _LINT)]),
    "t_card_a": ("terminal", [("card_a", _LINT)]),
    "t_noroute": ("terminal", [("card_b", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_learn": ("terminal", [("b_learn", _LINT)]),
    "t_carin": ("terminal", [("b_carin", _LINT)]),
    "t_lower": ("terminal", [("b_lower", _LINT)]),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c6_ring_row": ("game", "Comms, the call row 'Surveyor Rook - A recording at the ring' waiting in the list"),
    "game_c6_ring_call": ("game", "Comms, Rook at the Ring open: the take, and the answers 'Log the names.' and 'Shut it off.'"),
    "game_c6_altar3": ("game", "Comms, Rook at the Altar open after the names were logged: three answers, 'Play the entry keyed to Dace.' in the middle"),
    "game_c6_entry": ("game", "Comms, The Entry for Dace open: the take about the cairn, and its one answer 'Mark the side room.'"),
    "game_c6_map_cairn": ("game", "Helm's map: The Cairn as a new contact on the far side of The Nave"),
    "game_c6_quests": ("game", "Helm, the handheld icon then Quests: The One Who Stayed Active, with the small table of surveyors in its description"),
    "game_c6_shot1": ("game", "The server's main screen, about 1 second into the cutscene: black bars, the lower third 'The Altar' over 'The tally on the rim stops at forty-one.', the ship panel top left reading The Altar"),
    "game_c6_shot2": ("game", "The server's main screen, about 6 seconds in: 'The Cairn' over 'Forty-one stones. One for each day.'"),
    "game_c6_after": ("game", "The server's main screen, about 12 seconds in: the ship's own view again, the bars gone"),
    # drawn
    "card_clue": ("card", "table", {"heading": "Step 1 - What a clue is", "nth": 1, "kicker": "A clue can open four things"}),
    "card_rules": ("card", "points", {"kicker": "Four rules for learn and learned", "items": [
        "learn writes one word down: ; learn names adds the word names to what this crew knows",
        "learned counts, and can ask for one word: if learned >= 1, or if learned names",
        "Every word learned in a call goes on one list, kept for the whole game",
        "The count is read when the crew opens the scene, and only then"]}),
    "card_other": ("card", "rows", {"kicker": "The other kind of side story", "header": ["", "A side story for the ship", "A side story for one person"],
                                    "rows": [["Where you write it", "The Quests section", "A section of its own, Side Stories"],
                                             ["What says whose it is", "Nothing. It is everybody's", "For: and a job, such as For: comms"],
                                             ["Who is handed it", "The ship, when an answer says accepts", "A crew member, when they leave the ship"],
                                             ["Where it is read", "The quest list on any console", "That person's handheld"],
                                             ["You can play it", "Today", "Once a crew member can suit up: Lecture 8"]]}),
    "card_beacon": ("card", "points", {"kicker": "Storm's Beacon: a side story for one person", "items": [
        "For: comms", "State: active", "Done when: signal recorder_taken", "Leads to: at_near, sink_wreck", "Pays: 80 credits"]}),
    # the page's table under Step 7: the code block above it has a `#` line, which ends the heading's section for the tool
    "card_parts": ("card", "rows", {"kicker": "The card has two parts", "header": ["Part of the card", "What it means", "Yours to change"],
                                    "rows": [["amd_cutscenes(amd_section(MISSION_DOC, \"cutscenes\"))", "Read the section whose key is cutscenes", "No"],
                                             ["The three # lines", "A note to yourself", "Yes"],
                                             ["//shared/signal/cairn_found", "This block runs when the word cairn_found is sent", "The word. It is the word after Then: signal"],
                                             ["cutscene_amd(\"cairn_scene\", ...)", "Play the cutscene with this key", "The key. It is the key of your cutscene's first record"],
                                             ["to=role(\"mainscreen\")", "Play it on every main screen", "No"],
                                             ["->END", "The block is finished", "No"]]}),
    "card_log": ("card", "points", {"kicker": "mast.runtime.log, after you play", "items": [
        "Cutscene shot 'cairn_shot_2': Subject 'carin' is neither cast nor a role - shot dropped"]}),
    "card_blind": ("card", "table", {"heading": "Step 8 - Check it", "nth": 4, "kicker": "Lint says clean, and nothing tells you"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A line for those who know, a payment, a third shot, two breaks"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 7", "sub": "The main story, step by step"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c6_altar3"},
        {"from": 3, "still": "game_c6_map_cairn"},
        {"from": 4, "still": "game_c6_quests"},
        {"from": 5, "still": "game_c6_shot1"},
        {"from": 7, "still": "game_c6_shot2"},
    ]},
    "s02_what_a_clue_is": {"step": 1, "beats": [
        {"from": 0, "still": "card_clue"},
        {"from": 2, "still": "card_clue", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_clue", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 6, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 9, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 10, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 14, "still": "card_clue", "marks": [("part", "r2")]},
    ]},
    "s03_the_first_clue": {"step": 2, "beats": [
        {"from": 0, "still": "game_c6_ring_row"},
        {"from": 2, "still": "e_plate", "marks": [("lines", 157, 157)]},
        {"from": 3, "still": "e_plate", "marks": [("lines", 158, 158)]},
        {"from": 4, "still": "e_mz", "marks": [("lines", 50, 57)]},
        {"from": 5, "still": "e_mz", "marks": [("lines", 53, 53)]},
        {"from": 6, "still": "e_ring", "marks": [("lines", 206, 215)]},
        {"from": 7, "still": "e_ring", "marks": [("lines", 214, 215)]},
        {"from": 8, "still": "e_ring", "marks": [("text", 214, "; learn names")]},
        {"from": 11, "still": "game_c6_ring_call"},
    ]},
    "s04_the_clue_opens_an_answer": {"step": 3, "beats": [
        {"from": 0, "still": "e_answer", "marks": [("lines", 195, 195)]},
        {"from": 2, "still": "e_answer", "marks": [("text", 195, "(rook_dace)")]},
        {"from": 3, "still": "e_answer", "marks": [("text", 195, "if learned >= 1")]},
        {"from": 5, "still": "game_c6_altar3"},
        {"from": 7, "still": "e_dace", "marks": [("lines", 218, 225)]},
        {"from": 8, "still": "e_dace", "marks": [("lines", 222, 222)]},
        {"from": 10, "still": "e_dace", "marks": [("lines", 224, 224)]},
    ]},
    "s05_a_side_room_and_the_place_in": {"step": 4, "beats": [
        {"from": 0, "still": "e_reveal", "marks": [("lines", 242, 242)]},
        {"from": 1, "still": "e_room", "marks": [("lines", 174, 175)]},
        {"from": 3, "still": "e_room", "marks": [("lines", 182, 185)]},
        {"from": 5, "still": "e_reveal", "marks": [("text", 242, "reveal cairn")]},
        {"from": 6, "still": "e_room_k", "marks": [("text", 179, "(cairn)")]},
        {"from": 7, "still": "e_room_k", "marks": [("text", 171, "(crypt)")]},
    ]},
    "s06_the_side_story": {"step": 5, "beats": [
        {"from": 0, "still": "e_stayed", "marks": [("lines", 59, 75)]},
        {"from": 1, "still": "e_stayed", "marks": [("lines", 59, 59)]},
        {"from": 2, "still": "e_stayed", "marks": [("lines", 62, 62)]},
        {"from": 3, "still": "e_stayed", "marks": [("lines", 64, 64)]},
        {"from": 4, "still": "e_stayed", "marks": [("lines", 66, 74)]},
        {"from": 5, "still": "e_stayed", "marks": [("lines", 68, 72)]},
        {"from": 7, "still": "game_c6_quests"},
        {"from": 9, "still": "e_accepts", "marks": [("text", 259, "accepts stayed")]},
        {"from": 11, "still": "card_beacon"},
        {"from": 12, "still": "card_other"},
    ]},
    "s07_the_cutscene_what_you_write": {"step": 6, "beats": [
        {"from": 0, "still": "e_cuts_a", "marks": [("lines", 277, 281)]},
        {"from": 1, "still": "e_cuts_a", "marks": [("text", 275, "(cutscenes)")]},
        {"from": 2, "still": "e_cuts_a", "marks": [("lines", 277, 281)]},
        {"from": 3, "still": "e_cuts_a", "marks": [("text", 277, "(cairn_scene)"), ("lines", 279, 279)]},
        {"from": 4, "still": "e_cuts_b", "marks": [("lines", 283, 283), ("lines", 294, 294)]},
        {"from": 5, "still": "e_cuts_a", "marks": [("lines", 285, 285)]},
        {"from": 6, "still": "e_cuts_a", "marks": [("lines", 286, 286)]},
        {"from": 7, "still": "e_stayed", "marks": [("text", 64, "cairn")]},
        {"from": 8, "still": "e_cuts_a", "marks": [("lines", 287, 287)]},
        {"from": 9, "still": "e_cuts_b", "marks": [("lines", 298, 298)]},
        {"from": 10, "still": "e_cuts_a", "marks": [("lines", 288, 288)]},
        {"from": 11, "still": "e_cuts_a", "marks": [("lines", 289, 289)]},
        {"from": 12, "still": "e_cuts_a", "marks": [("lines", 290, 290)]},
        {"from": 13, "still": "e_cuts_a", "marks": [("lines", 292, 292)]},
        {"from": 15, "still": "game_c6_shot1"},
        {"from": 16, "still": "e_cuts_b", "marks": [("lines", 303, 303)]},
    ]},
    "s08_the_card": {"step": 7, "beats": [
        {"from": 0, "still": "t_cuts"},
        {"from": 1, "still": "t_cuts", "marks": [("span", 1, "section-not-loaded")]},
        {"from": 4, "still": "card_parts"},
        {"from": 5, "still": "m_map", "marks": [("lines", 64, 65)]},
        {"from": 6, "still": "m_map", "marks": [("lines", 62, 62)]},
        {"from": 7, "still": "m_map", "marks": [("lines", 64, 65)]},
        {"from": 8, "still": "t_card_a", "marks": [("part", "run1:clean")]},
        {"from": 10, "still": "e_then", "marks": [("lines", 65, 65)]},
        {"from": 11, "still": "e_then", "marks": [("text", 65, "cairn_found")]},
        {"from": 12, "still": "t_noroute", "marks": [("span", 1, "signal-no-route")]},
        {"from": 14, "still": "m_end", "marks": [("lines", 111, 116)]},
        {"from": 15, "still": "m_end", "marks": [("lines", 115, 115)]},
        {"from": 16, "still": "m_end", "marks": [("text", 114, "cairn_found"), ("text", 115, "cairn_scene")]},
        {"from": 17, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s09_lint": {"step": 8, "beats": [
        {"from": 0, "still": "e_learn"},
        {"from": 1, "still": "e_learn", "marks": [("text", 231, "learned => 1")]},
        {"from": 2, "still": "t_learn", "marks": [("span", 1, "unreadable-guard")]},
        {"from": 4, "still": "e_carin", "marks": [("text", 298, "carin")]},
        {"from": 5, "still": "t_carin", "marks": [("part", "run1:clean")]},
        {"from": 6, "still": "e_carin", "marks": [("lines", 295, 303)]},
        {"from": 7, "still": "card_log"},
        {"from": 9, "still": "e_lower", "marks": [("text", 290, "lowerthird")]},
        {"from": 10, "still": "t_lower", "marks": [("part", "run1:clean")]},
        {"from": 11, "still": "e_lower", "marks": [("lines", 290, 291)]},
        {"from": 12, "still": "card_blind"},
    ]},
    "s10_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "game_c6_ring_row"},
        {"from": 1, "still": "game_c6_ring_call"},
        {"from": 3, "still": "game_c6_altar3"},
        {"from": 4, "still": "game_c6_entry"},
        {"from": 6, "still": "game_c6_map_cairn"},
        {"from": 7, "still": "game_c6_quests"},
        {"from": 9, "still": "game_c6_shot1"},
        {"from": 12, "still": "game_c6_shot2"},
        {"from": 13, "still": "game_c6_after"},
        {"from": 14, "still": "game_c6_shot1"},
    ]},
    "s11_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 5, "still": "card_next"},
    ]},
}
