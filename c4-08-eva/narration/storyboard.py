"""Storyboard for c4-08-eva: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-17).

The lecture starts from MyRuin as Lecture 7 left it with Lecture 5's Steps 2 to 6 done as
well (461 lines, the order "Lectures 1 to 4, 6 and 7, then 5": Lecture 5's two quests are
the last records of the Quests section) and Lecture 6's story.mast (116 lines). The page's
own example\\ is the end of the lecture, so "start" is BUILT BACKWARDS from it: every pair
of (before, after) text below is typed forward, one state per step, and the last state must
equal the example byte for byte ("same_as"). The steps, in the order the video types them:
g1 The Gallery Door, g2 The Fallen Slab, c1 Cut Through, c2 The First Marker's Then line,
b1 the two answers, b2 The Niche's two lines, b3 the objective, b4 The Bowl deleted, h1 the
Then line on What Rook Put Back, h2 Carry It Home, k1 the clock in the fence, k2 the clock
in the last paragraph (= final). "typo" and "nogate" are Step 7's two breakages, on final.

GAME STILLS. NOT YET TAKEN: no Class 4 game still exists. They are taken in ONE scouting
sitting in the real engine, from the finished mission (this lecture has never been filmed;
nobody has flown a suit, so scout it first and fix the page where the screen differs):
`python game.py c4-08-eva start --state final --consoles server,helm,comms`
Two people, or one at two consoles: Helm goes outside, Comms answers. SUIT UP closed the
client until 2026-10-17 (assigned a ship in its spawn frame); the library now waits ~2 s,
so take the suit stills a few seconds after the press. One probe patch for scouting puts
the ship at the door (`_scout.pos = Vec3(0, 0, 18700)` after spawn_players). Marks are left off until the stills exist. Press order:
  1. Helm: fly to the door of The Hollow (Find the Way In completes), stop the ship:
     game_c8_door (the ship at the mouth).
  2. Helm: the handheld icon, the Boarding Party app: game_c8_party (it names The Hollow,
     the button SUIT UP).
  3. Press SUIT UP: game_c8_suit (the console of the crew member in the suit, the five apps).
  4. Nav: game_c8_nav (the list: The Ring Plate, The Gallery Door, The Cache, The Altar).
     Pick The Altar: game_c8_flying (the suit part way along the route, through the Nave).
  5. At the altar: Act, the scene At the Altar with its two answers: game_c8_altar_act.
     Scan: game_c8_scan (The Vault, then The Altar with the Scan: line).
  6. Comms: the altar recording, Mark the Gallery.: game_c8_comms_mark (the call with the
     answer). Helm, Nav: game_c8_nav_niche (The Niche now on the list). Pick it:
     game_c8_noway (Nav: No way through to niche from here.).
  7. Nav: The Gallery Door. On arrival, Act: game_c8_door_act (the Scan: line added).
  8. Fire: game_c8_fire (one row, The Fallen Slab 450). Select the row, press again at once:
     game_c8_beam (the banner BEAM - The Fallen Slab, 12s).
  9. Wait fourteen seconds. Helm's quest list: game_c8_quests (Cut Through done, The Second
     Marker running).
 10. Nav: The Niche. On arrival, Comms: game_c8_comms_second (A second recording, the
     answer Open the niche.). Choose it: game_c8_bowl (the bowl in the niche, the suit beside).
 11. The suit takes the bowl: game_c8_pickup (the line 'Pickup: The Stone Bowl').
 12. Crew app: game_c8_crew (Come aboard). Press it, then Helm flies to within 1000 of DS 1:
     game_c8_win (the end screen with the Win: sentence). Never caption a face.
"""
LECTURE = "c4-08-eva"
TITLE = ("Class 4, Lecture 8", "EVA", "A crew member goes outside, and a slab comes down")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-08-eva/example"
_C6 = "c4-06-clues-side-stories-cutscenes/example"      # the story.mast (Lecture 6's card)

_X_CAIRN = "A pile of stones in the middle of the Crypt.\n\n"
_DOOR = """### [The Gallery Door](gallery_door)
---
Relic: hollow
Point: 3000, 0, -650
Roles: gallery_door
Scan: A slab of the wall has come down across the doorway. It is cracked through the middle.
---
The Nave side of the doorway into the Gallery. Where a crew member stands to cut.

"""
_SLAB = """### [The Fallen Slab](slab)
---
Relic: hollow
Barrier: 3000, 0, -1100, 320
Clear with: beam
---
A slab of the Gallery's own wall, down across its doorway.

"""
_X_MARKER = "An old survey marker is transmitting from the far room.\n\n"
_CUT = """#### [Cut Through](cut)
---
Scope: shared
Starts when: revealed
Objective: Send someone out to cut the slab across the Gallery door
Done when: signal slab_opened
Reward: 100 credits
Then: reveal survey/second
Part of: survey
Required: true
---
A slab has come down across the way into the built room. Somebody has to go out there and cut it.

- ![](icon://person) Suit up at The Way In, while the ship is close
- ![](icon://flame) Fly to The Gallery Door, and cut the slab with the beam

The cut takes twelve seconds. The ship's own beams can break the slab as well.

"""
_FIRST_OLD = "Then: reveal survey/second\nPart of: survey\nRequired: true\n---\nAn old survey marker"
_FIRST_NEW = "Then: reveal survey/cut\nPart of: survey\nRequired: true\n---\nAn old survey marker"
_ANS1_OLD = "- [What is it?](rook_what)\n- [Take it aboard.]() ; signal hollow_taken"
_ANS1_NEW = "- [What is it?](rook_what)\n- [Open the niche.]() ; signal niche_open"
_ANS2_OLD = "people to count.\n\n- [Take it aboard.]() ; signal hollow_taken"
_ANS2_NEW = "people to count.\n\n- [Open the niche.]() ; signal niche_open"
_NICHE_OLD = "Item: stone_bowl\n---\nA recess"
_NICHE_NEW = ("Item: stone_bowl\nStarts when: signal niche_open\n"
              "Scan: A square recess, cut later than the room. A stone bowl sits at the back of it.\n---\nA recess")
_OBJ_OLD = "Objective: Answer the second marker on Comms"
_OBJ_NEW = "Objective: Have Comms open the niche, then bring out what is in it"
_BOWL = """### [The Bowl](bowl)
---
Scope: shared
Starts when: at once
Objective: Take the stone bowl out of the niche
Done when: signal hollow_taken
Reward: 200 credits
---
Something small and heavy sits in the niche at the back of The Gallery.

It is the one thing in The Hollow worth the trip. Whatever else the crew finds in there, this is what DS 1 sent them for.

"""
_SCANS = "// ---- Science scans."
_HOME_OLD = "  - rook hails rook_niche\nPart of: survey"
_HOME_NEW = "  - rook hails rook_niche\nThen: reveal survey/home\nPart of: survey"
_X_TAKE = ("Rook's team took it from the altar forty years ago, and then they carried it back. "
           "His recordings are the only account of why.\n\n")
_CARRY = """#### [Carry It Home](home)
---
Scope: shared
Starts when: revealed
Objective: Bring everyone aboard, and return to within 1000 of DS 1
Done when: reach station 1000
Reward: 100 credits
Part of: survey
Required: true
---
It is aboard. Take it back to DS 1.

Count heads before Helm turns for home. Anybody still in a suit is still out at The Hollow.

"""
_CLOCK_OLD = "Fails when: 20 minutes"
_CLOCK_NEW = "Fails when: 40 minutes"
_HAZE_OLD = "You have twenty minutes."
_HAZE_NEW = "You have forty minutes."

# (state, [(before, after), ...]) in the order the video types them
_STEPS = [
    ("g1", [(_X_CAIRN, _X_CAIRN + _DOOR)]),
    ("g2", [(_DOOR, _DOOR + _SLAB)]),
    ("c1", [(_X_MARKER, _X_MARKER + _CUT)]),
    ("c2", [(_FIRST_OLD, _FIRST_NEW)]),
    ("b1", [(_ANS1_OLD, _ANS1_NEW), (_ANS2_OLD, _ANS2_NEW)]),
    ("b2", [(_NICHE_OLD, _NICHE_NEW)]),
    ("b3", [(_OBJ_OLD, _OBJ_NEW)]),
    ("b4", [(_BOWL + _SCANS, _SCANS)]),
    ("h1", [(_HOME_OLD, _HOME_NEW)]),
    ("h2", [(_X_TAKE, _X_TAKE + _CARRY)]),
    ("k1", [(_CLOCK_OLD, _CLOCK_NEW)]),
    ("k2", [(_HAZE_OLD, _HAZE_NEW)]),
]

STATES = {
    "start": {"folder": _C6, "over": (_EX,),
              "edits": [("replace", FILE, after, before)
                        for _s, pairs in reversed(_STEPS) for before, after in reversed(pairs)]},
}
_prev = "start"
for _s, _pairs in _STEPS:
    STATES[_s] = {"base": _prev, "edits": [("replace", FILE, b, a) for b, a in _pairs]}
    _prev = _s
STATES["k2"]["same_as"] = (_EX + "/mission.amd",)
STATES["final"] = {"base": "k2"}
# Step 7: the two breakages, on the finished file
STATES["typo"] = {"base": "final", "edits": [
    ("replace", FILE, "Done when: signal slab_opened", "Done when: signal slab_open")]}
STATES["nogate"] = {"base": "final", "edits": [("replace", FILE, _DOOR, "")]}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

# line numbers, from the states above (centers of the 21-line windows, and the lines marked)
_C = {"way_in": 266, "r0": 324, "g1": 332, "g2": 338, "c1": 122, "c2": 122, "d0": 448, "d1": 448,
      "niche": 304, "obj": 156, "bowl": 184, "del": 184, "h1": 155, "h2": 172, "k1": 86, "k2": 86,
      "typo": 123, "nogate": 348, "fin": 358}
_L = {"way_in_a": 262, "way_in_b": 268, "way_in_roles": 266,
      "door_a": 326, "door_b": 334, "door_point": 329,
      "slab_a": 335, "slab_b": 341, "slab_barrier": 338, "slab_clear": 339,
      "cut_a": 118, "cut_b": 132, "cut_done": 123, "cut_list_a": 131, "cut_list_b": 132,
      "first_a": 112, "first_b": 116, "first_then": 112,
      "ans_old_a": 444, "ans_old_b": 452, "ans_new_a": 444, "ans_new_b": 452,
      "niche_item": 304, "niche_starts": 305, "obj_new": 153, "bowl_a": 178, "bowl_b": 188,
      "home_then": 158, "carry_done": 171, "carry_para2": 178, "fails": 82, "haze": 90,
      "typo_done": 123, "fin_slab_a": 358, "fin_slab_b": 364}

STILLS = {
    "e_way_in": ("vscode", "start", _C["way_in"], "big", _NS),
    "e_r0": ("vscode", "start", _C["r0"], "big", _NS),
    "e_g1": ("vscode", "g1", _C["g1"], "big", _NS),
    "e_g2": ("vscode", "g2", _C["g2"], "big", _NS),
    "e_c1": ("vscode", "c1", _C["c1"], "big", _NS),
    "e_c2": ("vscode", "c2", _C["c2"], "big", _NS),
    "e_d0": ("vscode", "c2", _C["d0"], "big", _NS),
    "e_d1": ("vscode", "b1", _C["d1"], "big", _NS),
    "e_niche": ("vscode", "b2", _C["niche"], "big", _NS),
    "e_obj": ("vscode", "b3", _C["obj"], "big", _NS),
    "e_bowl": ("vscode", "b3", _C["bowl"], "big", _NS),
    "e_del": ("vscode", "b4", _C["del"], "big", _NS),
    "e_h1": ("vscode", "h1", _C["h1"], "big", _NS),
    "e_h2": ("vscode", "h2", _C["h2"], "big", _NS),
    "e_k1": ("vscode", "k1", _C["k1"], "big", _NS),
    "e_k2": ("vscode", "k2", _C["k2"], "big", _NS),
    "e_typo": ("vscode", "typo", _C["typo"], "big", _NS),
    "e_nogate": ("vscode", "nogate", _C["nogate"], "big", _NS),
    "e_fin": ("vscode", "final", _C["fin"], "big", _NS),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_typo": ("terminal", [("typo", _LINT)]),
    "t_nogate": ("terminal", [("nogate", _LINT)]),
    # THE REAL GAME (NOT YET TAKEN; see the docstring). State final, consoles server,helm,comms. No marks yet.
    "game_c8_door": ("game", "Helm, the ship stopped at the mouth of The Hollow (Find the Way In done): the ruin ahead"),
    "game_c8_party": ("game", "Helm, the handheld open on the Boarding Party app: it names The Hollow, and the button SUIT UP"),
    "game_c8_suit": ("game", "The same console just after SUIT UP: the crew member in a suit at The Way In, the view from the suit and the handheld with its five apps (Nav, Act, Scan, Fire, Crew). No face"),
    "game_c8_nav": ("game", "The suit's Nav app: the list of places (The Ring Plate, The Gallery Door, The Cache, The Altar) and Careful / Cruise / Fast"),
    "game_c8_flying": ("game", "The suit part way to The Altar, flying through The Nave on its own"),
    "game_c8_altar_act": ("game", "The suit at The Altar, the Act app: the scene 'At the Altar', its words and its two answers"),
    "game_c8_scan": ("game", "The suit's Scan app at the altar: The Vault, then The Altar with its Scan: line"),
    "game_c8_comms_mark": ("game", "Comms, the altar recording ('A recording at the altar') with the answer Mark the Gallery."),
    "game_c8_nav_niche": ("game", "The suit's Nav app after Mark the Gallery.: The Niche now on the list"),
    "game_c8_noway": ("game", "Nav after The Niche is picked: 'No way through to niche from here.'"),
    "game_c8_door_act": ("game", "The suit at The Gallery Door, the Act app: the place's Scan: line about the fallen slab added to the transcript"),
    "game_c8_fire": ("game", "The suit's Fire app at The Gallery Door: one row, 'The Fallen Slab   450', BEAM the tool in hand"),
    "game_c8_beam": ("game", "The Fire app after the row is selected and pressed again: the banner 'BEAM - The Fallen Slab, 12s'"),
    "game_c8_quests": ("game", "Helm's quest list fourteen seconds later: Cut Through done, The Second Marker running"),
    "game_c8_comms_second": ("game", "Comms, the call 'A second recording' with the answer Open the niche."),
    "game_c8_bowl": ("game", "The suit at The Niche after Open the niche.: the stone bowl in the recess, the suit beside it"),
    "game_c8_pickup": ("game", "The suit has taken the bowl: the line 'Pickup: The Stone Bowl' and Carry It Home appearing"),
    "game_c8_crew": ("game", "The suit's Crew app: the button Come aboard"),
    "game_c8_win": ("game", "The end screen at DS 1: the Win: sentence 'The Hollow is surveyed, and what Rook put back is aboard.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_s1": ("card", "table", {"heading": "Step 1 - What the game does by itself", "kicker": "What the game does by itself"}),
    "card_offer": ("card", "table", {"heading": "The offer", "kicker": "The offer"}),
    "card_apps": ("card", "table", {"heading": "The suit", "kicker": "The suit's five apps"}),
    "card_rules": ("card", "points", {"kicker": "Three things to remember", "items": [
        "A suit flies to places, and to nothing else. It cannot be steered by hand.",
        "A Hidden: yes place is not on the list until somebody has been within 1200 of it, or an answer has revealed it.",
        "The tools reach 600. A thing further off than that is not offered."]}),
    "card_icons": ("card", "table", {"heading": "Step 3 - The slab is a step of the story", "nth": 1, "kicker": "A picture for a bullet"}),
    "card_endrun": ("card", "table", {"heading": "Step 4 - The bowl, by hand", "kicker": "How the end of the story runs now"}),
    "card_cannot": ("card", "table", {"heading": "Step 7 - Check it", "nth": 3, "kicker": "Lint says clean, and", "rows": (1, 2)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 9", "sub": "The same suit, outside a station"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c8_door"},
        {"from": 1, "still": "game_c8_party"},
        {"from": 2, "still": "game_c8_door"},
        {"from": 3, "still": "game_c8_flying"},
        {"from": 4, "still": "game_c8_altar_act"},
        {"from": 5, "still": "game_c8_beam"},
        {"from": 6, "still": "game_c8_pickup"},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_what_the_game_does_by_itself": {"step": 1, "beats": [
        {"from": 0, "still": "card_s1"},
        {"from": 2, "still": "card_s1", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_s1", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_s1", "marks": [("part", "r3")]},
        {"from": 5, "still": "card_s1", "marks": [("part", "r4")]},
        {"from": 6, "still": "e_way_in", "marks": [("lines", _L.get("way_in_a", 1), _L.get("way_in_b", 1))]},
        {"from": 7, "still": "e_way_in", "marks": [("lines", _L.get("way_in_roles", 1), _L.get("way_in_roles", 1))]},
        {"from": 8, "still": "card_offer", "marks": [("part", "r2")]},
        {"from": 9, "still": "card_offer", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_offer", "marks": [("part", "r4")]},
    ]},
    "s03_the_suit": {"step": 1, "beats": [
        {"from": 0, "still": "card_apps"},
        {"from": 2, "still": "card_apps", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_apps", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_apps", "marks": [("part", "r3")]},
        {"from": 5, "still": "card_apps", "marks": [("part", "r4")]},
        {"from": 6, "still": "card_apps", "marks": [("part", "r5")]},
        {"from": 7, "still": "card_rules"},
        {"from": 8, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 10, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item3")]},
    ]},
    "s04_a_place_to_stand_and_a_way_t": {"step": 2, "beats": [
        {"from": 0, "still": "e_r0"},
        {"from": 3, "still": "e_g1", "marks": [("lines", _L.get("door_a", 1), _L.get("door_b", 1))]},
        {"from": 4, "still": "e_g1", "marks": [("lines", _L.get("door_point", 1), _L.get("door_point", 1))]},
        {"from": 7, "still": "e_g1", "marks": [("lines", _L.get("door_a", 1), _L.get("door_b", 1))]},
        {"from": 9, "still": "e_g2", "marks": [("lines", _L.get("slab_a", 1), _L.get("slab_b", 1))]},
        {"from": 10, "still": "e_g2", "marks": [("lines", _L.get("slab_barrier", 1), _L.get("slab_barrier", 1))]},
        {"from": 11, "still": "e_g2", "marks": [("lines", _L.get("slab_clear", 1), _L.get("slab_clear", 1))]},
    ]},
    "s05_the_slab_is_a_step": {"step": 3, "beats": [
        {"from": 0, "still": "e_g2", "marks": [("text", _L.get("slab_a", 1), "(slab)")]},
        {"from": 3, "still": "e_c1", "marks": [("lines", _L.get("cut_a", 1), _L.get("cut_b", 1))]},
        {"from": 4, "still": "e_c1", "marks": [("lines", _L.get("first_a", 1), _L.get("first_b", 1))]},
        {"from": 5, "still": "e_c2", "marks": [("lines", _L.get("first_then", 1), _L.get("first_then", 1))]},
        {"from": 6, "still": "e_c2", "marks": [("text", _L.get("cut_done", 1), "signal slab_opened")]},
        {"from": 9, "still": "e_c2", "marks": [("lines", _L.get("cut_list_a", 1), _L.get("cut_list_b", 1))]},
        {"from": 12, "still": "e_c2", "marks": [("text", _L.get("cut_list_a", 1), "icon://person")]},
        {"from": 13, "still": "e_c2", "marks": [("text", _L.get("cut_list_b", 1), "icon://flame")]},
        {"from": 14, "still": "card_icons", "marks": [("part", "r3")]},
    ]},
    "s06_the_bowl_by_hand": {"step": 4, "beats": [
        {"from": 0, "still": "e_d0", "marks": [("lines", _L.get("ans_old_a", 1), _L.get("ans_old_a", 1)),
                                                 ("lines", _L.get("ans_old_b", 1), _L.get("ans_old_b", 1))]},
        {"from": 2, "still": "e_d1", "marks": [("lines", _L.get("ans_new_a", 1), _L.get("ans_new_a", 1)),
                                                 ("lines", _L.get("ans_new_b", 1), _L.get("ans_new_b", 1))]},
        {"from": 9, "still": "e_niche", "marks": [("text", _L.get("niche_item", 1), "stone_bowl")]},
        {"from": 10, "still": "e_d1", "marks": [("text", _L.get("ans_new_a", 1), "Open the niche.")]},
        {"from": 11, "still": "e_d1", "marks": [("text", _L.get("ans_new_a", 1), "signal niche_open")]},
        {"from": 12, "still": "e_niche", "marks": [("text", _L.get("niche_starts", 1), "signal niche_open")]},
        {"from": 13, "still": "card_endrun"},
        {"from": 14, "still": "e_obj", "marks": [("lines", _L.get("obj_new", 1), _L.get("obj_new", 1))]},
        {"from": 15, "still": "e_bowl", "marks": [("lines", _L.get("bowl_a", 1), _L.get("bowl_b", 1))]},
        {"from": 16, "still": "e_del"},
    ]},
    "s07_coming_home_and_the_clock": {"step": 5, "beats": [
        {"from": 0, "still": "e_h1"},
        {"from": 1, "still": "e_h1", "marks": [("lines", _L.get("home_then", 1), _L.get("home_then", 1))]},
        {"from": 2, "still": "e_h2", "marks": [("lines", _L.get("carry_done", 1), _L.get("carry_done", 1))]},
        {"from": 3, "still": "e_h2", "marks": [("lines", _L.get("carry_para2", 1), _L.get("carry_para2", 1))]},
        {"from": 4, "still": "e_k2", "marks": [("lines", _L.get("fails", 1), _L.get("fails", 1))]},
        {"from": 7, "still": "e_k2", "marks": [("text", _L.get("fails", 1), "40 minutes")]},
        {"from": 8, "still": "e_k2", "marks": [("lines", _L.get("haze", 1), _L.get("haze", 1))]},
    ]},
    "s08_lint": {"step": 7, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_typo", "marks": [("text", _L.get("typo_done", 1), "slab_open")]},
        {"from": 2, "still": "t_typo", "marks": [("span", 1, "unfired-signal")]},
        {"from": 4, "still": "e_nogate"},
        {"from": 5, "still": "t_nogate", "marks": [("part", "run1:clean")]},
        {"from": 9, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 10, "still": "e_fin", "marks": [("lines", _L.get("fin_slab_a", 1), _L.get("fin_slab_b", 1))]},
    ]},
    "s09_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_c8_door"},
        {"from": 1, "still": "game_c8_party"},
        {"from": 3, "still": "game_c8_suit"},
        {"from": 4, "still": "game_c8_nav"},
        {"from": 5, "still": "game_c8_altar_act"},
        {"from": 7, "still": "game_c8_comms_mark"},
        {"from": 8, "still": "game_c8_nav_niche"},
        {"from": 9, "still": "game_c8_noway"},
        {"from": 10, "still": "game_c8_door_act"},
        {"from": 11, "still": "game_c8_fire"},
        {"from": 12, "still": "game_c8_beam"},
        {"from": 13, "still": "game_c8_quests"},
        {"from": 14, "still": "game_c8_comms_second"},
        {"from": 15, "still": "game_c8_bowl"},
        {"from": 16, "still": "game_c8_pickup"},
        {"from": 16.55, "still": "game_c8_crew"},
        {"from": 17, "still": "game_c8_win"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 6, "still": "card_next"},
    ]},
}
