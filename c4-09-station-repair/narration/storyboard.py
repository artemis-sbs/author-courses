"""Storyboard for c4-09-station-repair: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-17).

The lecture starts from MyRuin as Lecture 8 left it (`c4-08-eva\\example\\mission.amd`, 501
lines) and Lecture 6's story.mast (116 lines). The states, in the order the video types
them: w1 DS 1 Worksite, w2 The Work Area, w3 The Station, w4 The Airlock, j1 Survey Mast,
q1 the quest Raise the Mast, d1 `hollow_door` added to The Way In (the file lints clean and
Find the Way In still says `reach entrance 1000`: the page's "lint cannot see" row), d2
Find the Way In waits for `hollow_door` (= final, the page's own example, byte for byte).

GAME STILLS. NOT YET TAKEN: no Class 4 game still exists. They are taken in ONE scouting
sitting in the real engine, from the finished mission, after Lecture 8's (this lecture has
never been filmed: station repair was built the day the page was written, so scout it first
and fix the page where the screen differs):
`python game.py c4-09-station-repair start --state final --consoles server,helm,comms`
Two people, or one at two consoles. If a console closes when the suit appears, add
`eva_set_suit_hull("tsn_shuttle")` as Lecture 8's page says. No probe patch, but note the
ship starts 2300 to 4400 from the airlock: if the Boarding Party app offers nothing, fly
toward DS 1 (that IS the page's advice). Marks are left off until the stills exist.
  1. Helm, at once: game_c9_ship (the ship near DS 1, before any press).
  2. Helm: fly within 3000 of the airlock. The handheld icon, the Boarding Party app:
     game_c9_party (it names DS 1 Worksite, the button SUIT UP).
  3. Press SUIT UP: game_c9_suit (the crew member in a suit at The Airlock, beside the
     station). No face.
  4. Nav: game_c9_nav (one row, Survey Mast, about 533). Pick it: game_c9_flying (the suit
     part way round the hull).
  5. When it stops: Fire: game_c9_fire (the row 'Repair: Survey Mast   260' and under the
     list 'A Repair takes the tool it names.'). Select the row, press again at once:
     game_c9_banner (the banner 'REPAIR - Survey Mast, 12s').
  6. Wait fourteen seconds. Helm's quest list: game_c9_quests (Raise the Mast done, 40
     credits paid).
"""
LECTURE = "c4-09-station-repair"
TITLE = ("Class 4, Lecture 9", "EVA elsewhere", "A repair outside a station")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_C6 = "c4-06-clues-side-stories-cutscenes/example"      # the story.mast (Lecture 6's card)
_PREV = "c4-08-eva/example"
_EX = "c4-09-station-repair/example"

_W1 = """### [DS 1 Worksite](yard)
---
Loc: 0, 0, 0
Walls: none
Debris: 0
---
The space around DS 1 where a suit can work. Not a ruin: no walls, no rock, no cloud.
"""
_W2 = """### [The Work Area](yard_area)
---
Relic: yard
Chamber: 0, 0, 0, 1500
---
Everywhere a suit may go.
"""
_W3 = """### [The Station](yard_hull)
---
Relic: yard
Solid: sphere, 0, 0, 0, 500
---
DS 1 itself. A suit goes round it, never through it.
"""
_W4 = """### [The Airlock](airlock)
---
Relic: yard
Point: 0, 0, -1200
Roles: entrance
---
Where a suit comes out, and where the worksite's name sits on the map.
"""
_J1 = """### [Survey Mast](mast)
---
Relic: yard
Repair: 0, 0, -560, 80
Clear with: beam
---
The station's survey antenna. It has been dead since the first survey came home.
"""
_HEAD = "down across its doorway.\n\n"
_TAIL = "\n\n// ---- Items"


def _region(blocks):
    """The text between the slab and the Items comment, with these blocks typed."""
    return _HEAD + "\n".join(blocks) + _TAIL if blocks else _HEAD + "\n// ---- Items"


_RAISE = """### [Raise the Mast](raise_mast)
---
Scope: shared
Starts when: at once
Objective: Go outside at DS 1 and mend the survey mast
Done when: signal mast_repaired
Reward: 40 credits
---
![](ship://starbase_command) Orders from DS 1, the station you started at.

The station's survey antenna is dead. Somebody has to go out and weld it.

- ![](icon://person) Suit up while the ship is near DS 1
- ![](icon://wrench) Fly the suit round the hull to the mast, and mend it with the beam

"""
_LEFT_END = "Nobody at DS 1 knows what is in them.\n\n"
_SCANS = "// ---- Science scans."

STATES = {
    "start": {"folder": _C6, "over": (_PREV,)},
    "w1": {"base": "start", "edits": [("replace", FILE, _region([]), _region([_W1]))]},
    "w2": {"base": "w1", "edits": [("replace", FILE, _region([_W1]), _region([_W1, _W2]))]},
    "w3": {"base": "w2", "edits": [("replace", FILE, _region([_W1, _W2]), _region([_W1, _W2, _W3]))]},
    "w4": {"base": "w3", "edits": [("replace", FILE, _region([_W1, _W2, _W3]), _region([_W1, _W2, _W3, _W4]))]},
    "j1": {"base": "w4", "edits": [("replace", FILE, _region([_W1, _W2, _W3, _W4]),
                                    _region([_W1, _W2, _W3, _W4, _J1]))]},
    "q1": {"base": "j1", "edits": [("replace", FILE, _LEFT_END + _SCANS, _LEFT_END + _RAISE + _SCANS)]},
    # Step 5: the role first. Lint is clean here, and Find the Way In still reads `reach entrance`
    "d1": {"base": "q1", "edits": [("replace", FILE, "Roles: entrance\n---\nWhere a ship arrives",
                                    "Roles: entrance, hollow_door\n---\nWhere a ship arrives")]},
    "d2": {"base": "d1", "edits": [("replace", FILE, "Done when: reach entrance 1000",
                                    "Done when: reach hollow_door 1000")],
           "same_as": (_EX + "/mission.amd",)},
    "final": {"base": "d2"},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}
_M = {"file": MAST, "side": False}

# centers of the 21-line windows, and the lines marked (from the states above)
_C = {"ws": 372, "area": 378, "hull": 384, "lock": 392, "mast": 399, "q": 200, "way": 302,
      "air": 407, "find": 97, "waydr": 302, "finddr": 97}
_L = {"ws_a": 366, "ws_b": 372, "ws_head": 366, "ws_loc": 368, "ws_walls": 369, "ws_debris": 370,
      "area_a": 374, "area_b": 379, "hull_a": 381, "hull_b": 386, "hull_solid": 384,
      "lock_a": 388, "lock_b": 394, "lock_roles": 392,
      "job_a": 396, "job_b": 402, "job_repair": 399, "job_clear": 400,
      "q_a": 193, "q_b": 206, "q_done": 198, "q_lead": 201, "q_list_a": 205, "q_list_b": 206,
      "way_roles": 302, "air_roles": 407, "find_done": 97, "find_reward": 98, "find_then": 99}

STILLS = {
    "e_mast_file": ("vscode", "w4", 67, "big", _M),
    "e_ws": ("vscode", "w4", _C["ws"], "big", _NS),
    "e_area": ("vscode", "w4", _C["area"], "big", _NS),
    "e_hull": ("vscode", "w4", _C["hull"], "big", _NS),
    "e_lock": ("vscode", "w4", _C["lock"], "big", _NS),
    "e_job": ("vscode", "j1", _C["mast"], "big", _NS),
    "e_quest": ("vscode", "q1", _C["q"], "big", _NS),
    "e_way_q": ("vscode", "q1", _C["way"], "big", _NS),
    "e_air_q": ("vscode", "q1", _C["air"], "big", _NS),
    "e_find_q": ("vscode", "q1", _C["find"], "big", _NS),
    "e_way_d": ("vscode", "d1", _C["waydr"], "big", _NS),
    "e_find_d": ("vscode", "d2", _C["finddr"], "big", _NS),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_both": ("terminal", [("d1", _LINT)]),
    # THE REAL GAME (NOT YET TAKEN; see the docstring). State final, consoles server,helm,comms. No marks yet.
    "game_c9_ship": ("game", "Helm at once: the ship near DS 1, before any press"),
    "game_c9_party": ("game", "Helm, the handheld open on the Boarding Party app: it names DS 1 Worksite, and the button SUIT UP"),
    "game_c9_suit": ("game", "The same console just after SUIT UP: the crew member in a suit beside the station, at The Airlock, the handheld with its five apps. No face"),
    "game_c9_nav": ("game", "The suit's Nav app: one row, Survey Mast, with its distance"),
    "game_c9_flying": ("game", "The suit part way round the hull of DS 1 on its way to the mast"),
    "game_c9_fire": ("game", "The suit's Fire app by the mast: 'Repair: Survey Mast   260' and under the list 'A Repair takes the tool it names.'"),
    "game_c9_banner": ("game", "The Fire app after the row is selected and pressed again: the banner 'REPAIR - Survey Mast, 12s'"),
    "game_c9_quests": ("game", "Helm's quest list after the repair: Raise the Mast done"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_ruin1": ("card", "table", {"heading": "Step 1 - A ruin with the ruin turned off", "kicker": "A ruin, and a worksite"}),
    "card_ruin2": ("card", "table", {"heading": "Step 1 - A ruin with the ruin turned off", "nth": 2, "kicker": "A barrier, and a repair job"}),
    "card_offer": ("card", "points", {"kicker": "When SUIT UP is offered here", "items": [
        "The rule is Lecture 8's: the ship within 3000 of the entrance. Here the entrance is The Airlock.",
        "A ship does not always start that close. In the stand-in it started 2322 from the airlock in one game and 4342 in another. If the Boarding Party app offers nothing, fly toward the station.",
        "With two ruins in one mission, the offer follows the ship. Near the station it is the worksite. At the door of The Hollow it is The Hollow."]}),
    "card_tools": ("card", "table", {"heading": "Step 3 - The job", "nth": 2, "kicker": "What opens it"}),
    "card_words": ("card", "table", {"heading": "Step 4 - A quest that waits for it", "kicker": "The words the game sends"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 10", "sub": "The whole class, in one episode"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c9_ship"},
        {"from": 1, "still": "game_c9_party"},
        {"from": 2, "still": "game_c9_suit"},
        {"from": 3, "still": "game_c9_fire"},
        {"from": 4, "still": "game_c9_suit"},
        {"from": 5, "still": "game_c9_banner"},
        {"from": 6, "still": "game_c9_quests"},
    ]},
    "s02_a_ruin_with_the_ruin_turned_": {"step": 1, "beats": [
        {"from": 0, "still": "card_ruin1"},
        {"from": 4, "still": "card_ruin1", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 5, "still": "card_ruin1", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 6, "still": "card_ruin1", "marks": [("part", "r4")]},
        {"from": 7, "still": "card_ruin1", "marks": [("part", "r5")]},
        {"from": 8, "still": "card_ruin2"},
        {"from": 9, "still": "card_ruin2", "marks": [("part", "r1")]},
        {"from": 10, "still": "card_ruin2", "marks": [("part", "r3")]},
    ]},
    "s03_the_worksite": {"step": 2, "beats": [
        {"from": 0, "still": "e_ws", "marks": [("lines", _L.get("ws_a", 1), _L.get("ws_b", 1))]},
        {"from": 1, "still": "e_ws", "marks": [("lines", _L.get("ws_head", 1), _L.get("ws_head", 1))]},
        {"from": 2, "still": "e_ws", "marks": [("lines", _L.get("ws_loc", 1), _L.get("ws_loc", 1))]},
        {"from": 3, "still": "e_ws", "marks": [("text", _L.get("ws_loc", 1), "0, 0, 0")]},
        {"from": 4, "still": "e_mast_file", "marks": [("lines", 67, 67)]},
        {"from": 5, "still": "e_ws", "marks": [("lines", _L.get("ws_walls", 1), _L.get("ws_debris", 1))]},
        {"from": 7, "still": "e_area", "marks": [("lines", _L.get("area_a", 1), _L.get("area_b", 1))]},
        {"from": 8, "still": "e_hull", "marks": [("lines", _L.get("hull_a", 1), _L.get("hull_b", 1))]},
        {"from": 9, "still": "e_hull", "marks": [("lines", _L.get("hull_solid", 1), _L.get("hull_solid", 1))]},
        {"from": 11, "still": "e_lock", "marks": [("lines", _L.get("lock_a", 1), _L.get("lock_b", 1))]},
        {"from": 12, "still": "e_lock", "marks": [("lines", _L.get("lock_roles", 1), _L.get("lock_roles", 1))]},
    ]},
    "s04_when_the_offer_is_made": {"step": 2, "beats": [
        {"from": 0, "still": "card_offer", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_offer", "marks": [("part", "item2")]},
        {"from": 6, "still": "card_offer", "marks": [("part", "item3")]},
    ]},
    "s05_the_job": {"step": 3, "beats": [
        {"from": 0, "still": "e_job", "marks": [("lines", _L.get("job_a", 1), _L.get("job_b", 1))]},
        {"from": 1, "still": "e_job", "marks": [("lines", _L.get("job_repair", 1), _L.get("job_repair", 1))]},
        {"from": 3, "still": "e_job", "marks": [("lines", _L.get("job_clear", 1), _L.get("job_clear", 1))]},
        {"from": 5, "still": "card_tools", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_tools", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_tools", "marks": [("part", "r3")]},
    ]},
    "s06_a_quest_that_waits": {"step": 4, "beats": [
        {"from": 0, "still": "e_quest", "marks": [("lines", _L.get("q_a", 1), _L.get("q_b", 1))]},
        {"from": 1, "still": "e_job", "marks": [("text", _L.get("job_a", 1), "(mast)")]},
        {"from": 2, "still": "e_quest", "marks": [("text", _L.get("q_done", 1), "signal mast_repaired")]},
        {"from": 3, "still": "card_words"},
        {"from": 4, "still": "card_words", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_words", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_words", "marks": [("part", "r3")]},
        {"from": 8, "still": "e_quest", "marks": [("lines", _L.get("q_lead", 1), _L.get("q_list_b", 1))]},
        {"from": 9, "still": "e_quest", "marks": [("lines", _L.get("q_lead", 1), _L.get("q_lead", 1))]},
        {"from": 10, "still": "e_quest", "marks": [("lines", _L.get("q_list_a", 1), _L.get("q_list_b", 1))]},
    ]},
    "s07_two_doors_one_word": {"step": 5, "beats": [
        {"from": 0, "still": "e_air_q"},
        {"from": 1, "still": "e_way_q", "marks": [("lines", _L.get("way_roles", 1), _L.get("way_roles", 1))]},
        {"from": 2, "still": "e_air_q", "marks": [("lines", _L.get("air_roles", 1), _L.get("air_roles", 1))]},
        {"from": 3, "still": "e_find_q", "marks": [("lines", _L.get("find_done", 1), _L.get("find_done", 1))]},
        {"from": 5, "still": "e_find_q", "marks": [("text", _L.get("find_done", 1), "reach entrance 1000")]},
        {"from": 6, "still": "e_air_q", "marks": [("lines", _L.get("air_roles", 1), _L.get("air_roles", 1))]},
        {"from": 8, "still": "e_find_q", "marks": [("lines", _L.get("find_done", 1), _L.get("find_done", 1))]},
        {"from": 9, "still": "e_find_q", "marks": [("lines", _L.get("find_reward", 1), _L.get("find_then", 1))]},
        {"from": 11, "still": "t_both", "marks": [("part", "run1:clean")]},
        {"from": 13, "still": "e_way_d", "marks": [("text", _L.get("way_roles", 1), "hollow_door")]},
        {"from": 14, "still": "e_find_d", "marks": [("text", _L.get("find_done", 1), "hollow_door")]},
    ]},
    "s08_lint_and_play": {"step": 7, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "game_c9_party"},
        {"from": 2, "still": "game_c9_suit"},
        {"from": 3, "still": "game_c9_nav"},
        {"from": 4, "still": "game_c9_flying"},
        {"from": 5, "still": "game_c9_fire"},
        {"from": 7, "still": "game_c9_banner"},
        {"from": 8, "still": "game_c9_quests"},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 6, "still": "card_next"},
    ]},
}
