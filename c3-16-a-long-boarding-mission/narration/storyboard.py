"""Storyboard for c3-16-a-long-boarding-mission: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

The capstone is a second mission, MyClaim (`sbs create MyClaim -t away --title "Corvin's
Claim"`). The lecture shows it finished, so there is one state, "final": the page's whole
example\\ folder. Most of the lecture is the page's tables, drawn as cards.

THE GROUND IS LAID FLAT, as in Lectures 12 to 15: the tool reads one folder level, so the
three maps and the tileset are written beside mission.amd (`sbs lint` prints the same).
The three maps in the cold open and works.tiles in scene 3 are their TEXT. A Tile Map
Editor still is DEFERRED: capture opens a file at a line, which is always the text editor,
and the throwaway profile still has add-on 0.9.4, the one with the "Experimental" badge.

2026-10-15: scene 6 and the page's Step 8 said a FULL shot removes any prop. The library
released after the page was measured leaves every prop where it was and opens only one
whose `Opens with:` lists `cut`. Both were rewritten from the library's documentation;
not re-played.

GAME STILLS. Not taken yet; no marks until the screenshots exist. game.py cannot start this
mission (it makes its probe from the `amd` template and copies only mission.amd and
story.mast). Copy the page's example\\ folder, ground\\ included, to data\\missions\\MyClaim,
`sbs fetch MyClaim --update-libs` once, then `sbs run server,science,engineering -m MyClaim
map=0` with COSMOS_SETTINGS '{"GAME_RESULTS_SAVE": false}'. THREE windows: the server,
Science (Dr Ines Hale) and Engineering (Chief Okoro). The party is offered at once (the
handheld icon, Boarding Party, BEAM DOWN). To read the bridge's quest list, Okoro presses
Crew, Beam up; then Boarding Party, BEAM DOWN puts him back where the party is.
GAME ONE, the dig (about ten minutes):
  1. Both beam down at the camp. Okoro beams up: Quests, game_l16_list_before (one line,
     Hold at the Relay). Beam down.
  2. Hale: talk to Ada Corvin, Ask what happened (the clock starts). Okoro beams up:
     game_l16_list_after (Bring the Dig Crew Out, Get the Lift Running); the arc
     selected, game_l16_log_arc (the table and the hourglass line). Beam down.
  3. Okoro: walk east to the Lift House: game_l16_works (his map, at the gate). Fire,
     FULL, Arm, click the lift gate: game_l16_gate_shot (the gate still shut; Look's last
     note). The ventilator panel (Needs engineering).
  4. Hale: the rest of Ada's answers and the gallery plan; between them, the stores key,
     the stores (the jacks), the hauler's coupling, the lift console. When the lift runs,
     Okoro beams up: game_l16_list_lift (a time under the arc, Reach the Rock Fall Active,
     Get the Lift Running Done). Beam down.
  5. Both down the lift. Hale: talk to Jo Reth: game_l16_reth (Set his leg offered). Set
     his leg.
  6. Okoro, with the jacks: the rock fall, once four things are known: game_l16_fall
     (Shore the roof and dig among the answers). Shore, Set the jacks and dig, Bring them
     up. The server's last screen: game_l16_won_dig.
GAME TWO, the blast (about six minutes, Science alone): Ada, the stores key, the charges,
the coupling, the lift, down, the rock fall, Set the charges, Fire them as they are, Bring
them up. The server's last screen: game_l16_won_blast.
"""
import os as _os

LECTURE = "c3-16-a-long-boarding-mission"
TITLE = ("Class 3, Lecture 16", "Capstone: a long boarding mission", "Corvin's Claim, and then yours")
MISSION = "MyClaim"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_COURSES = _os.path.dirname(_HERE)


def _read(*parts):
    with open(_os.path.join(_COURSES, *parts), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_G = (LECTURE, "example", "ground")
_EX = LECTURE + "/example"

STATES = {
    # The page's whole example\\ folder, its maps laid flat
    "final": {"folder": _EX,
              "edits": [("write", name, _read(*_G, name))
                        for name in ("starter.tileset", "camp.tiles", "works.tiles", "gallery.tiles")],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
}

_LINT = "sbs lint MyClaim"
_NS = {"side": False}
_TEXT = {"side": False, "settings": {"workbench.editorAssociations": {"*.tiles": "default", "*.tileset": "default"}}}

STILLS = {
    # Not on screen: the first window on a new folder must show the Side Bar, so the tool can
    # hide it for every still after (the folder is laid flat, so it is never used).
    "v_open": ("vscode", "final", 1, "wide"),
    # The three maps, as text: the rows of each map
    "e_map_camp": ("vscode", "final", 24, "big", dict(_TEXT, file="camp.tiles")),         # lines 14 to 34: the map, rows 19 to 29
    "e_map_works": ("vscode", "final", 26, "big", dict(_TEXT, file="works.tiles")),       # lines 16 to 36: the map, rows 21 to 31
    "e_map_gallery": ("vscode", "final", 18, "big", dict(_TEXT, file="gallery.tiles")),   # lines 8 to 28: the map, rows 16 to 21
    # Step 3: the middle map as text
    "e_works": ("vscode", "final", 12, "big", dict(_TEXT, file="works.tiles")),    # lines 2 to 22: title (3), known (6), the marks (15, 18, 19)
    # Step 4: the three lines only one person can use
    "e_vent": ("vscode", "final", 254, "big", _NS),        # lines 244 to 264: Ventilator panel, Needs: engineering (256)
    "e_leg": ("vscode", "final", 415, "big", _NS),         # lines 405 to 425: Jo Reth's scene, Set his leg (415)
    "e_charges": ("vscode", "final", 458, "big", _NS),     # lines 448 to 468: Four Charges, Shape them (458)
    # Step 5: the arc
    "e_arc": ("vscode", "final", 88, "big", _NS),          # lines 78 to 98: the arc (78 to 94)
    "e_steps": ("vscode", "final", 117, "mid", _NS),       # about lines 103 to 131: Reach the Rock Fall, Dig Them Out (117), Blast Them Out (126)
    # Step 6: the room that decides
    "e_fall": ("vscode", "final", 440, "mid", _NS),        # about lines 426 to 454: The Rock Fall (429 to 436), Where to Dig (443 to 447)
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME (not taken yet). Three windows: server, Science (Dr Hale), Engineering
    # (Chief Okoro). Press order in the docstring.
    "game_l16_list_before": ("game", "Engineering, beamed back up, the ePADD Quest Log before Ada Corvin's first answer: one line, Hold at the Relay"),
    "game_l16_list_after": ("game", "Engineering's Quest Log after Ask what happened: Bring the Dig Crew Out and Get the Lift Running, both Active (the arc with its time)"),
    "game_l16_log_arc": ("game", "Engineering's Quest Log, Bring the Dig Crew Out selected: its sentence, the three-row table Who / Where, and the hourglass line 'Half an hour of air...', above the checklist of its steps"),
    "game_l16_works": ("game", "Engineering's console in the Lift House: the map with Chief Okoro at the works gate, the lift house walls and the gate at the far end"),
    "game_l16_gate_shot": ("game", "Engineering's console after a FULL shot at the lift gate: the gate still drawn shut, and the Look app's last note on the shot"),
    "game_l16_list_lift": ("game", "Engineering's Quest Log after the lift runs: Bring the Dig Crew Out with about '24:40 left', Reach the Rock Fall Active, Get the Lift Running Done"),
    "game_l16_reth": ("game", "Science's xESS in the Lower Gallery, Act, Jo Reth's scene: his line, and Set his leg among the answers"),
    "game_l16_fall": ("game", "Engineering's xESS at the rock fall once four things are known: the line with the draft on your face, then Listen at the rock, Shore the roof and dig, Step back"),
    "game_l16_won_dig": ("game", "The server's last screen after Bring them up (the dig): 'All four walk out, and Corvin's Claim opens again in the morning.'"),
    "game_l16_won_blast": ("game", "The server's last screen after the blast (game two): 'All four walk out. Behind them the lower gallery comes down for good.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_sentences": ("card", "table", {"heading": "Step 1 - Three sentences", "kicker": "Three sentences, on paper"}),
    "card_beats": ("card", "table", {"heading": "Step 2 - The beat sheet, with times", "kicker": "My beat sheet"}),
    "card_areas": ("card", "table", {"heading": "Step 3 - Three areas", "kicker": "Three areas, one decision each"}),
    "card_cols": ("card", "table", {"heading": "Step 4 - Three tracks, a join, and three people nobody can replace", "kicker": "Three columns"}),
    "card_only": ("card", "table", {"heading": "Step 4 - Three tracks, a join, and three people nobody can replace", "nth": 2, "kicker": "Three things only one person can do"}),
    "card_roads": ("card", "table", {"heading": "Step 4 - Three tracks, a join, and three people nobody can replace", "nth": 3, "kicker": "Never the only road"}),
    "card_shot": ("card", "table", {"heading": "Step 8 - What a FULL shot does", "kicker": "A FULL shot on Corvin's Claim"}),
    "card_checks": ("card", "table", {"heading": "Step 9 - One sheet of checks", "kicker": "Twelve checks, in order"}),
    "card_rubric": ("card", "table", {"heading": "The rubric", "kicker": "The rubric"}),
    "card_end": ("card", "title", {"kicker": "Class 3", "title": "Boarding Parties", "sub": "Now go and write yours"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_map_camp"},
        {"from": 1, "still": "e_map_works"},
        {"from": 2, "still": "e_map_gallery"},
        {"from": 3, "still": "game_l16_list_lift"},
        {"from": 5, "still": "game_l16_won_dig"},
        {"from": 6, "still": "game_l16_won_blast"},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_three_sentences_and_a_beat_s": {"step": 1, "beats": [
        {"from": 0, "still": "card_sentences"},
        {"from": 1, "still": "card_sentences", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 2, "still": "card_sentences", "marks": [("part", "r3")]},
        {"from": 3, "still": "card_sentences", "marks": [("part", "r2c2")]},
        {"from": 5, "still": "card_sentences", "marks": [("part", "r3c2")]},
        {"from": 7, "still": "card_beats"},
        {"from": 8, "still": "card_beats", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 9, "still": "card_beats", "marks": [("part", "r4"), ("part", "r5")]},
        {"from": 10, "still": "card_beats"},
    ]},
    "s03_three_areas": {"step": 3, "beats": [
        # the game first: the lift house on the engineer's console
        {"from": 0, "still": "game_l16_works"},
        {"from": 2, "still": "card_areas"},
        {"from": 3, "still": "card_areas", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_areas", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_areas", "marks": [("part", "r3")]},
        {"from": 8, "still": "e_works", "marks": [("lines", 6, 6)]},
        {"from": 9, "still": "e_works", "marks": [("lines", 15, 15), ("lines", 18, 18)]},
        {"from": 11, "still": "e_works", "marks": [("lines", 3, 3)]},
    ]},
    "s04_three_people_nobody_can_repl": {"step": 4, "beats": [
        {"from": 0, "still": "card_cols"},
        {"from": 2, "still": "card_only"},
        # the game first: the doctor's answer
        {"from": 4, "still": "game_l16_reth"},
        {"from": 5, "still": "e_leg", "marks": [("text", 415, "if skill medical >= 3")]},
        {"from": 7, "still": "e_vent", "marks": [("lines", 256, 256)]},
        {"from": 7.5, "still": "e_charges", "marks": [("text", 458, "if skill security >= 3")]},
        {"from": 8, "still": "card_only"},
        {"from": 10, "still": "card_roads"},
        {"from": 13, "still": "card_roads", "marks": [("part", "r1")]},
        {"from": 14, "still": "card_roads", "marks": [("part", "r2"), ("part", "r3")]},
    ]},
    "s05_the_quest_tree": {"step": 5, "beats": [
        # the game first: the bridge's list
        {"from": 0, "still": "game_l16_list_lift"},
        {"from": 3, "still": "e_arc", "marks": [("lines", 78, 84)]},
        {"from": 4, "still": "e_arc", "marks": [("lines", 82, 83)]},
        {"from": 4.5, "still": "game_l16_list_before"},
        {"from": 5, "still": "game_l16_list_after"},
        {"from": 6, "still": "game_l16_list_lift"},
        {"from": 7, "still": "e_steps", "marks": [("lines", 117, 122), ("lines", 126, 131)]},
        {"from": 9, "still": "e_steps", "marks": [("lines", 120, 120), ("lines", 129, 129)]},
        {"from": 13, "still": "game_l16_log_arc"},
        {"from": 16, "still": "e_arc", "marks": [("lines", 88, 92)]},
        {"from": 17, "still": "e_arc", "marks": [("lines", 94, 94)]},
    ]},
    "s06_two_endings_and_a_full_shot": {"step": 6, "beats": [
        # the game first: the rock fall
        {"from": 0, "still": "game_l16_fall"},
        {"from": 3, "still": "e_fall", "marks": [("lines", 434, 435)]},
        {"from": 5, "still": "e_fall", "marks": [("text", 434, "if learned >= 4"), ("text", 446, "if holding jacks")]},
        # the game: a shot at the lift gate
        {"from": 6, "still": "game_l16_gate_shot"},
        {"from": 10, "still": "card_shot", "marks": [("part", "r3")]},
        {"from": 11, "still": "card_shot", "marks": [("part", "r2")]},
        {"from": 13, "still": "card_shot"},
    ]},
    "s07_twelve_checks_and_the_walk": {"step": 9, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "card_checks"},
        {"from": 4, "still": "card_checks", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 5, "still": "card_checks", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 6, "still": "card_checks", "marks": [("part", "r5")]},
        {"from": 7, "still": "card_checks", "marks": [("part", "r7"), ("part", "r9")]},
        {"from": 8, "still": "card_checks", "marks": [("part", "r10"), ("part", "r11"), ("part", "r12")]},
        {"from": 9, "still": "game_l16_reth"},
        {"from": 10, "still": "game_l16_won_dig"},
        {"from": 11, "still": "game_l16_won_blast"},
        {"from": 12, "still": "card_checks"},
    ]},
    "s08_the_rubric_and_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_rubric"},
        {"from": 2, "still": "card_rubric", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 3, "still": "card_rubric", "marks": [("part", "r4")]},
        {"from": 4, "still": "card_rubric", "marks": [("part", "r5")]},
        {"from": 5, "still": "card_rubric", "marks": [("part", "r6")]},
        {"from": 6, "still": "card_rubric", "marks": [("part", "r7")]},
        {"from": 7, "still": "card_rubric"},
        {"from": 10, "still": "card_end"},
    ]},
}
