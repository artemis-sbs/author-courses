"""Storyboard for c4-01-what-a-ruin-is: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and Class 3's. Caption numbers are those of shots.py (2026-10-17).

The lecture starts from nothing: `sbs create MyRuin -t amd --title "The Hollow"` makes the
same files as Class 1's hand-over, 60 lines in `mission.amd` ("start", Class 1, Lecture 3's
example with the title given). The borrowed block is pasted at the very end ("pasted", the
page's own example\\mission.amd, 118 lines, `## [Relics](relics)` on line 63). Giving it back
is "start" again.

Where the page's Stop 5 quotes the shipped file (the near side with Scene and Scan, the
scene, the haul and its item, the picket boat, the side story, the cutscene shot) those are
drawn as cards in the page's own words: nothing of Storm's Beacon is run or captured.

GAME STILLS. NOT TAKEN YET: they are named here and will be taken in one sitting in the real
engine. ONE game, TWO windows:
`python game.py c4-01-what-a-ruin-is start --state pasted --consoles server,helm`
(the page's own run line, `sbs run server,helm -m MyRuin map=0`, on a probe copy of the
example). No probe patch. Marks are left off every game still until the stills are taken.
Press order:
  1. Helm, at once, the map zoomed out until the hulk and The Sink are both on it:
     game_c1_map (The Sink past the hulk and off to one side).
  2. Helm: fly to The Sink's name, at the mouth of the way in. The server window, just
     inside the inlet, the ship nose-in: game_c1_haze (purple haze and rock).
  3. Server window, further down the inlet, the walls close on both sides: game_c1_inlet.
  4. Server window, the moment the inlet opens into the big room: game_c1_basin.
  5. Server window, the drift hanging in the middle of the big room, ahead: game_c1_drift.
  6. Fly round the drift to the far side. Helm's map, the ship near the far side, the three
     names (the inlet mouth, the near side, the far side) on it: game_c1_far.
"""
LECTURE = "c4-01-what-a-ruin-is"
TITLE = ("Class 4, Lecture 1", "What a ruin is", "Fly one that somebody else wrote, then read how it was made")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-01-what-a-ruin-is/example"
_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hollow"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hollow")]

STATES = {
    # what `sbs create MyRuin -t amd --title "The Hollow"` makes: 60 lines in mission.amd, relics_spawn on line 62 of story.mast
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED},
    # Stop 2: the borrowed block pasted at the end (the page's example, 118 lines)
    "pasted": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED, "over": (_EX,),
               "same_as": (_EX + "/mission.amd",)},
}

_CREATE = 'sbs create MyRuin -t amd --title "The Hollow"'
_FETCH = 'sbs fetch "MyRuin" --update-libs'
_NO = {"without": ("MyRuin",)}
_MAKE = [(_CREATE, ("",)), _FETCH, "sbs lint MyRuin"]
_NS = {"side": False}

STILLS = {
    # VS Code, real. A still shows 21 lines: the one named, ten above and ten below
    "e_end0": ("vscode", "start", 55, "big", _NS),          # lines 45 to 60: the end of the file as sbs create made it
    "e_w1": ("vscode", "pasted", 73, "big", _NS),           # lines 63 to 83: the heading, The Sink, the start of the inlet
    "e_w88": ("vscode", "pasted", 86, "big", _NS),          # lines 76 to 96: the two Box lines, the Solid
    "e_w108": ("vscode", "pasted", 108, "big", _NS),        # lines 98 to 118: the three places
    "e_back": ("vscode", "start", 55, "big", _NS),          # lines 45 to 60 again, the block gone
    # the command prompt, one real session
    "t_prompt": ("session", [], _NO),
    "t_create": ("session", _MAKE, dict(_NO, show=(1, 1))),
    "t_fetch": ("session", _MAKE, dict(_NO, show=(2, 2), tail=14)),
    "t_lint_new": ("session", _MAKE, dict(_NO, show=(3, 3))),
    "t_pasted": ("terminal", [("pasted", "sbs lint MyRuin")]),
    "t_back": ("terminal", [("start", "sbs lint MyRuin")]),
    "t_run": ("session", ["sbs run server,helm -m MyRuin map=0 --dry-run"], {"state": "pasted"}),
    # THE REAL GAME. Not taken yet (see the docstring). State pasted, consoles server,helm
    "game_c1_map": ("game", "Helm, the map at the start: the hulk, and past it and off to one side the name The Sink"),
    "game_c1_haze": ("game", "The server window, the ship just inside the inlet: purple haze and rock all round, seen from the bridge"),
    "game_c1_inlet": ("game", "The server window, further down the inlet: a long narrow room, rock close on both sides, the haze"),
    "game_c1_basin": ("game", "The server window as the inlet opens into the big room: rock a long way off on every side"),
    "game_c1_drift": ("game", "The server window in the big room: the mass of the drift hanging ahead, in the middle of the room"),
    "game_c1_far": ("game", "Helm's map with the ship on the far side of the drift: the three names, the inlet mouth, the near side and the far side, on it"),
    # drawn: the shipped file's pieces, as Stop 5 quotes them
    "card_title": ("card", "title", {}),
    "card_near": ("card", "page", {"kicker": "Shipped: a place with a scene and a scan", "text": [
        "### [the near side](at_near)", "---", "Relic: sink", "Point: -1600, 0, 0", "Roles: sink_near",
        "Scene: sink_near_look",
        "Scan: A drift of debris hangs in the middle of the room, hiding the far wall.", "---"]}),
    "card_scene": ("card", "page", {"kicker": "Shipped: the scene it names, in Dialogue", "text": [
        "### [The Far Side](sink_far_look)", "---", "Backdrop: pic:cv_rubble", "---",
        "% Behind the drift: the far side, and the heaviest of everything that ever settled here.",
        "- [Tell Eddy what you have found](sink_far_eddy) if comms", "- [Move on]()"]}),
    "card_haul": ("card", "page", {"kicker": "Shipped: a place that holds a thing", "text": [
        "### [the haul](haul_place)", "---", "Relic: sink", "Point: 2000, 0, 2000", "Roles: sink_treasure",
        "Item: sink_salvage", "Qty: 5", "---"]}),
    "card_wreck": ("card", "page", {"kicker": "Shipped: a place that is hidden", "text": [
        "### [the picket boat](sink_wreck)", "---", "Relic: sink", "Point: 1300, -300, 0", "Roles: sink_wreck",
        "Hidden: yes", "Item: clue_recorder", "Starts when: signal sink_wreck_found", "Scene: sink_wreck_look", "---"]}),
    "card_story": ("card", "page", {"kicker": "Shipped: a small story for one member of the crew", "text": [
        "### [Still Pinging](sink_pinging)", "---", "For: comms", "State: active",
        "Done when: signal recorder_taken", "Leads to: at_near, sink_wreck", "Pays: 80 credits", "---"]}),
    "card_cutscene": ("card", "page", {"kicker": "Shipped: what the main screen shows on arrival", "text": [
        "### [One room](arrive_sink_1)", "---", "Cutscene: arrive_sink", "Subject: relic_contact",
        "Lens: 0, 2200, -6500", "Seconds: 5", "Overlay: lower_third", "Name: The Sink", "---"]}),
    "card_cut": ("card", "table", {"heading": "What was cut, and why", "kicker": "What was cut, and why"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Before you delete it"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 2", "sub": "A ruin is a place"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c1_map"},
        {"from": 2, "still": "game_c1_haze"},
        {"from": 4, "still": "e_w1", "marks": [("lines", 63, 73)]},
        {"from": 6, "still": "game_c1_map"},
        {"from": 7, "still": "e_w1"},
    ]},
    "s02_a_mission_for_this_class": {"step": 1, "beats": [
        {"from": 0, "still": "t_prompt"},
        {"from": 4, "still": "t_create", "marks": [("cmd", 1, "MyRuin")]},
        {"from": 5, "still": "t_fetch"},
        {"from": 6, "still": "e_end0"},
        {"from": 7, "still": "t_lint_new", "marks": [("part", "run1:clean")]},
    ]},
    "s03_borrow_a_ruin": {"step": 2, "beats": [
        {"from": 0, "still": "e_end0"},
        {"from": 3, "still": "e_end0", "marks": [("lines", 59, 60)]},
        {"from": 4, "still": "e_w1", "marks": [("lines", 63, 83)]},
        {"from": 5, "still": "e_w1"},
        {"from": 6, "still": "t_pasted", "marks": [("part", "run1:clean")]},
        {"from": 7, "still": "e_w1", "marks": [("text", 67, "Loc: 6000, 0, 12000")]},
    ]},
    "s04_fly_it": {"step": 3, "beats": [
        {"from": 0, "still": "t_run", "marks": [("cmd", 1, "server,helm")]},
        {"from": 1, "still": "game_c1_map"},
        {"from": 2, "still": "game_c1_haze"},
        {"from": 3, "still": "game_c1_inlet"},
        {"from": 5, "still": "game_c1_basin"},
        {"from": 6, "still": "game_c1_drift"},
        {"from": 8, "still": "game_c1_far"},
    ]},
    "s05_read_what_you_pasted": {"step": 4, "beats": [
        {"from": 0, "still": "e_w1"},
        {"from": 2, "still": "e_w1", "marks": [("lines", 65, 73)]},
        {"from": 3, "still": "e_w88", "marks": [("text", 78, "Box:"), ("text", 85, "Box:")]},
        {"from": 4, "still": "e_w88", "marks": [("text", 93, "Solid:")]},
        {"from": 6, "still": "e_w108", "marks": [("text", 101, "Point:"), ("text", 108, "Point:"), ("text", 115, "Point:")]},
        {"from": 7, "still": "e_w88", "marks": [("text", 77, "Relic: sink"), ("text", 84, "Relic: sink"), ("text", 92, "Relic: sink")]},
        {"from": 9, "still": "e_w88", "marks": [("text", 77, "sink"), ("text", 84, "sink"), ("text", 92, "sink")]},
        {"from": 10, "still": "e_w108", "marks": [("text", 100, "Relic: sink"), ("text", 107, "Relic: sink"), ("text", 114, "Relic: sink")]},
        {"from": 11, "still": "e_w88"},
        {"from": 13, "still": "e_w88", "marks": [("lines", 78, 78), ("lines", 85, 85)]},
    ]},
    "s06_read_the_rest_of_the_file": {"step": 5, "beats": [
        {"from": 0, "still": "card_near", "move": False},
        {"from": 3, "still": "card_near"},
        {"from": 4, "still": "card_scene"},
        {"from": 5, "still": "card_haul"},
        {"from": 6, "still": "card_wreck"},
        {"from": 7, "still": "card_story"},
        {"from": 8, "still": "card_cutscene"},
        {"from": 12, "still": "card_cut"},
    ]},
    "s07_give_it_back": {"step": 6, "beats": [
        {"from": 0, "still": "e_w1", "marks": [("lines", 63, 63)]},
        {"from": 1, "still": "e_w1", "marks": [("lines", 63, 83)]},
        {"from": 2, "still": "e_back"},
        {"from": 3, "still": "t_back", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "e_back", "marks": [("lines", 45, 60)]},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_exercise", "marks": []},   # the paper questions: not list items
        {"from": 7, "still": "card_next"},
    ]},
}
