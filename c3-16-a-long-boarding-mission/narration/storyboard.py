"""Storyboard for c3-16-a-long-boarding-mission: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-16).

The capstone is a second mission, MyClaim (`sbs create MyClaim -t away --title "Corvin's
Claim"`). The lecture shows it finished, so there is one state, "final": the page's whole
example\\ folder. Most of the lecture is the page's tables, drawn as cards.

THE GROUND FOLDER. The state holds `ground\\` as the student has it (states.py reads, diffs
and writes subfolders). The three maps in the cold open are pictures from the Tile Map
Editor, Art view ("editor": "tiles"; see capture.web_steps); works.tiles in scene 3 is its
TEXT, at the lines the scene marks.

2026-10-15: scene 6 and the page's Step 8 said a FULL shot removes any prop. The library
released after the page was measured leaves every prop where it was and opens only one
whose `Opens with:` lists `cut`. Both were rewritten from the library's documentation;
not re-played.

GAME STILLS. Taken 2026-10-16 in the real engine (1.3.15, sbs_utils 7ea2c918), all 10
KEPT, marks set from them. State "final":
`python game.py c3-16-a-long-boarding-mission start --consoles server,science,engineering`
(the probe is made from the `away` template with every file of the state laid over it,
ground\\ included; the template's own landing.tiles is taken out, as the page has the
student delete it; GAME_RESULTS_SAVE is false). THREE windows: the server,
Science (Dr Ines Hale) and Engineering (Chief Okoro). The party is offered at once (the
handheld icon, Boarding Party, BEAM DOWN). To read the bridge's quest list, Okoro presses
Crew, Beam up; then Boarding Party, BEAM DOWN puts him back where the party is.
GAME ONE, the dig (Science and Engineering; 25 minutes of game time):
  1. Both beam down at the camp. Okoro beams up: Quests, game_l16_list_before (one line,
     Hold at the Relay, Done). Beam down.
  2. Hale: click Ada Corvin, Ask what happened (the clock starts). Okoro beams up:
     game_l16_list_after (the arc with its time left, Get the Lift Running Active); the
     arc selected, game_l16_log_arc (the table and the hourglass line). Beam down.
  3. Okoro: the stores key (by Ada's door, once she is asked about the stores), the
     stores, the jacks. Then east to the Lift House: game_l16_works (his map at the works
     gate, the hauler in the yard, the house still in fog). From the works gate, Fire,
     FULL, Arm, and click the cell the hauler has just entered on the west side of its
     square (7,3 or 7,4): one shot downs it, and the coupling it drops is picked up
     (Act: `Chief Okoro picked up coupling.`). A human will miss often.
  4. Okoro in the house: Fire, FULL, Arm, click the lift gate: game_l16_gate_shot (the gate
     still shut; Look's last line is still `Picked up coupling.` - a shot leaves no note).
     The ventilator panel: Reset the breakers. The lift console: Fit the coupling.
     Okoro beams up: game_l16_list_lift (the time left under the arc, Reach the Rock Fall
     Active, Get the Lift Running Done). Beam down.
  5. Both down the lift. Hale: the gallery plan, then Jo Reth: game_l16_reth (Set his leg
     offered). Set his leg.
  6. Okoro, with the jacks: the rock fall, once four things are known: game_l16_fall
     (Shore the roof and dig among the answers). Shore, Set the jacks and dig, Bring them
     up. The server's last screen: game_l16_won_dig.
GAME TWO, the blast (Science alone; 10 minutes of game time): Ada (what happened, the lift,
the stores), the stores key, the stores door, the charges, the hauler shot from the works
gate, the coupling, the lift console, down, the rock fall, Set the charges, Fire them as
they are, Bring them up. The server's last screen: game_l16_won_blast.
Every game still shows the AREA TITLE in the xESS bar's third slot, where the restored
library will name the mark; no caption describes that slot, so none needs a re-shoot for it.
No beat shows the squashed xESS home after Back.
"""
LECTURE = "c3-16-a-long-boarding-mission"
TITLE = ("Class 3, Lecture 16", "Capstone: a long boarding mission", "Corvin's Claim, and then yours")
MISSION = "MyClaim"
FILE = "mission.amd"
MAST = "story.mast"

_EX = LECTURE + "/example"

STATES = {
    # The page's whole example\\ folder, ground\\ and all
    "final": {"folder": _EX,
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
}

_LINT = "sbs lint MyClaim"
_NS = {"side": False}
_TEXT = {"side": False}                                 # a map as text, at a line
_MAP = {"side": False, "editor": "tiles", "view": "art"}  # a map in the Tile Map Editor (capture.web_steps)

STILLS = {
    # The three maps, in the Tile Map Editor's Art view
    "e_map_camp": ("vscode", "final", 1, "mid", dict(_MAP, file="ground/camp.tiles", zoom=40)),
    "e_map_works": ("vscode", "final", 1, "mid", dict(_MAP, file="ground/works.tiles", zoom=40)),
    "e_map_gallery": ("vscode", "final", 1, "mid", dict(_MAP, file="ground/gallery.tiles", zoom=48)),
    # Step 3: the middle map as text
    "e_works": ("vscode", "final", 12, "big", dict(_TEXT, file="ground/works.tiles")),    # lines 2 to 22: title (3), known (6), the marks (15, 18, 19)
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
    # THE REAL GAME (taken 2026-10-16). Three windows: server, Science (Dr Hale), Engineering
    # (Chief Okoro). Press order in the docstring.
    "game_l16_list_before": ("game", "Engineering, beamed back up, the ePADD Quest Log before Ada Corvin's first answer: one line, Hold at the Relay, Done"),
    "game_l16_list_after": ("game", "Engineering's Quest Log after Ask what happened: Bring the Dig Crew Out with the time left where its state would be, Get the Lift Running Active under it, Hold at the Relay Done"),
    "game_l16_log_arc": ("game", "Engineering's Quest Log, Bring the Dig Crew Out selected: its sentence, the three-row table Who / Where, and the hourglass line 'Half an hour of air...', above the checklist of its steps"),
    "game_l16_works": ("game", "Engineering's console in the Lift House area: the map with Chief Okoro at the works gate and the ore hauler on its square; the house itself still in fog, not drawn"),
    "game_l16_gate_shot": ("game", "Engineering's console after a FULL shot at the lift gate: the gate still drawn shut, and Look's last line still the note from before the shot ('Picked up coupling.'): a shot leaves no note"),
    "game_l16_list_lift": ("game", "Engineering's Quest Log after the lift runs: Bring the Dig Crew Out with the time left, Reach the Rock Fall Active, Get the Lift Running Done"),
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

# Marks on the game stills (fractions of the 1280x960 window), set from the PNGs.
_WK_MAP = ("rect", 0.0, 0.21, 0.35, 0.74)          # game_l16_works: the drawn part of the map
_WK_OKORO = ("rect", 0.035, 0.345, 0.09, 0.43)     # ... Chief Okoro at the works gate
_WK_HAULER = ("rect", 0.26, 0.345, 0.32, 0.435)    # ... the ore hauler on its square
_WK_FOG = ("rect", 0.35, 0.21, 0.66, 0.74)         # ... the lift house, still in fog
_WK_FIRE = ("rect", 0.668, 0.9, 0.98, 0.99)        # ... the Fire row of the xESS home
_GS_HOUSE = ("rect", 0.19, 0.26, 0.548, 0.635)     # game_l16_gate_shot: the lift house
_GS_GATE = ("rect", 0.5, 0.415, 0.55, 0.48)        # ... the lift gate, still shut
_GS_LOOK = ("rect", 0.668, 0.19, 0.99, 0.585)      # ... Look's list
_GS_LAST = ("rect", 0.672, 0.59, 0.82, 0.628)      # ... its last line, 'Picked up coupling.'
_LB_RELAY = ("rect", 0.004, 0.148, 0.17, 0.21)     # game_l16_list_before: Hold at the Relay, Done
_LA_ARC = ("rect", 0.004, 0.152, 0.215, 0.282)     # game_l16_list_after: the arc, its time, Get the Lift Running
_LL_ALL = ("rect", 0.0, 0.15, 0.22, 0.43)          # game_l16_list_lift: the whole list
_LL_STEPS = ("rect", 0.028, 0.222, 0.215, 0.352)   # ... Reach the Rock Fall Active, Get the Lift Running Done
_LOG_DESC = ("rect", 0.385, 0.075, 0.995, 0.4)     # game_l16_log_arc: the arc's description
_RT_MAP = ("rect", 0.0, 0.315, 0.62, 0.63)         # game_l16_reth: the party in the Lower Gallery
_RT_SCENE = ("rect", 0.67, 0.695, 0.965, 0.98)     # ... Jo Reth's line and answers, Set his leg among them
_FL_SCENE = ("rect", 0.67, 0.595, 0.965, 0.915)    # game_l16_fall: the draft line and the three answers
_FL_SHORE = ("rect", 0.672, 0.805, 0.868, 0.855)   # ... Shore the roof and dig
_WON_LINE = ("rect", 0.015, 0.215, 0.25, 0.315)    # game_l16_won_*: the Win: sentence

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "e_map_camp"},
        {"from": 1, "still": "e_map_works"},
        {"from": 2, "still": "e_map_gallery"},
        {"from": 3, "still": "game_l16_list_lift", "marks": [_LL_ALL]},
        {"from": 5, "still": "game_l16_won_dig", "marks": [_WON_LINE]},
        {"from": 6, "still": "game_l16_won_blast", "marks": [_WON_LINE]},
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
        # the game first: the lift house area on the engineer's console
        {"from": 0, "still": "game_l16_works", "marks": [_WK_MAP]},
        {"from": 1, "still": "game_l16_works", "marks": [_WK_OKORO, _WK_HAULER]},
        {"from": 2, "still": "game_l16_works", "marks": [_WK_FOG]},
        {"from": 3, "still": "card_areas"},
        {"from": 4, "still": "card_areas", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_areas", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_areas", "marks": [("part", "r3")]},
        {"from": 9, "still": "e_works", "marks": [("lines", 6, 6)]},
        {"from": 10, "still": "e_works", "marks": [("lines", 15, 15), ("lines", 18, 18)]},
        {"from": 12, "still": "e_works", "marks": [("lines", 3, 3)]},
    ]},
    "s04_three_people_nobody_can_repl": {"step": 4, "beats": [
        {"from": 0, "still": "card_cols"},
        {"from": 2, "still": "card_only"},
        # the game first: the doctor's answer
        {"from": 4, "still": "game_l16_reth", "marks": [_RT_SCENE]},
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
        {"from": 0, "still": "game_l16_list_lift", "marks": [_LL_ALL]},
        {"from": 3, "still": "e_arc", "marks": [("lines", 78, 84)]},
        {"from": 4, "still": "e_arc", "marks": [("lines", 82, 83)]},
        {"from": 4.5, "still": "game_l16_list_before", "marks": [_LB_RELAY]},
        {"from": 5, "still": "game_l16_list_after", "marks": [_LA_ARC]},
        {"from": 6, "still": "game_l16_list_lift", "marks": [_LL_STEPS]},
        {"from": 7, "still": "e_steps", "marks": [("lines", 117, 122), ("lines", 126, 131)]},
        {"from": 9, "still": "e_steps", "marks": [("lines", 120, 120), ("lines", 129, 129)]},
        {"from": 13, "still": "game_l16_log_arc", "marks": [_LOG_DESC]},
        {"from": 16, "still": "e_arc", "marks": [("lines", 88, 92)]},
        {"from": 17, "still": "e_arc", "marks": [("lines", 94, 94)]},
    ]},
    "s06_two_endings_and_a_full_shot": {"step": 6, "beats": [
        # the game first: the rock fall
        {"from": 0, "still": "game_l16_fall", "marks": [_FL_SCENE]},
        {"from": 2, "still": "game_l16_fall", "marks": [_FL_SHORE]},
        {"from": 3, "still": "e_fall", "marks": [("lines", 434, 435)]},
        {"from": 5, "still": "e_fall", "marks": [("text", 434, "if learned >= 4"), ("text", 446, "if holding jacks")]},
        # the game: a shot at the lift gate, and no word about it
        {"from": 6, "still": "game_l16_gate_shot", "marks": [_GS_HOUSE]},
        {"from": 8, "still": "game_l16_gate_shot", "marks": [_GS_GATE]},
        {"from": 10, "still": "game_l16_gate_shot", "marks": [_GS_LOOK]},
        {"from": 11, "still": "game_l16_gate_shot", "marks": [_GS_LAST]},
        {"from": 12, "still": "card_shot", "marks": [("part", "r3")]},
        {"from": 13, "still": "card_shot", "marks": [("part", "r2")]},
        {"from": 15, "still": "card_shot"},
    ]},
    "s07_twelve_checks_and_the_walk": {"step": 9, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "card_checks"},
        {"from": 4, "still": "card_checks", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 5, "still": "card_checks", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 6, "still": "card_checks", "marks": [("part", "r5")]},
        {"from": 7, "still": "card_checks", "marks": [("part", "r7"), ("part", "r9")]},
        {"from": 8, "still": "card_checks", "marks": [("part", "r10"), ("part", "r11"), ("part", "r12")]},
        {"from": 9, "still": "game_l16_reth", "marks": [_RT_MAP]},
        # the hauler: one FULL shot from the works gate
        {"from": 10, "still": "game_l16_works", "marks": [_WK_HAULER]},
        {"from": 11, "still": "game_l16_works", "marks": [_WK_OKORO]},
        {"from": 12, "still": "game_l16_works", "marks": [_WK_HAULER]},
        {"from": 14, "still": "game_l16_works", "marks": [_WK_FIRE]},
        {"from": 16, "still": "game_l16_won_dig", "marks": [_WON_LINE]},
        {"from": 17, "still": "game_l16_won_blast", "marks": [_WON_LINE]},
        {"from": 18, "still": "card_checks"},
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
