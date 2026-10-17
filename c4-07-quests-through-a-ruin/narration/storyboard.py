"""Storyboard for c4-07-quests-through-a-ruin: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12 and in _tools/picture/README.md. Caption numbers are those of shots.py.

The lecture starts from Lecture 6's finished files (the class is a chain): `MyRuin` as `sbs create
MyRuin -t amd` made it, `mission.amd` (304 lines) and `story.mast` (116 lines, with the card)
from c4-06's example. Lecture 4's exercise is NOT done. `story.mast` is never opened. The steps
are typed in the video's order: the arc's heading ("arc"), Find the Way In ("door"), The First
Marker and The Second Marker ("first", "second"), `Then: reveal survey/first` on the door
("door_then"), `Then: reveal survey/take` on the second ("second_then"), What Rook Put Back
("take"), Rook at the Niche and What It Is ("calls"), the two scan records ("final", the page's
own example, 409 lines). Three breaks of scene 8: "b_wayin", "b_reveal", "b_req".

GAME STILLS. NOT TAKEN YET: they are planned here and are taken in one scouting sitting.
ONE game, FOUR windows (this one ENDS A GAME, so a take is added to the user's
game_results.yaml; back it up or restore it afterwards):
`python game.py c4-07-quests-through-a-ruin start --state final --consoles server,helm,comms,science`.
No probe patch: Helm flies. Press order:
  1. Helm, at once: the handheld icon (top left), Quests: game_c7_list0 (The Hollow Survey with
     ONE step, Find the Way In). Close it.
  2. Helm: fly to inside 1000 of The Way In (0, 0, -700). The handheld icon, Quests:
     game_c7_list1 (Find the Way In Done, The First Marker running). Close it.
  3. Helm: fly through The Mouth and the ring (the ring call arrives on Comms: leave it), across
     The Nave and up the tunnel to inside 600 of The Altar (3000, 0, 2800): game_c7_vault (Helm's
     view in the Vault). Comms: game_c7_calls (the altar call on top of the list, the ring call
     below it).
  4. Science: select The Altar, the scan tab: game_c7_science (the Altar Reading).
  5. Comms: open the altar call, "Play the rest.", "Mark the Gallery.".
  6. Helm: fly back across The Nave, into The Gallery, inside 400 of The Niche (3000, 0, -2500).
     The handheld icon, Quests: game_c7_list3 (three steps Done, What Rook Put Back running).
     Comms: game_c7_second (the second recording at the TOP of the list). Open it: game_c7_takeit
     ("What is it?" and "Take it aboard.").
  7. Comms: "Take it aboard.": game_c7_end (the end screen, the win).
No marks are set on the game stills yet: set them from the screenshots once they exist.
"""
LECTURE = "c4-07-quests-through-a-ruin"
TITLE = ("Class 4, Lecture 7", "Quests through a ruin", "Four steps, a win and a loss, and a word Comms sends")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-07-quests-through-a-ruin/example"
_ARC = ("### [The Hollow Survey](survey)\n---\nArc\nScope: shared\nStarts when: at once\nFails when: 20 minutes\n"
        "Win: The Hollow is surveyed, and what Rook put back is aboard.\n"
        "Lose: The haze closed in before the survey was done.\n---\n"
        "![](ship://starbase_command) Orders from DS 1, the station you started at.\n\n"
        "Somebody surveyed The Hollow forty years ago and left markers behind. Some of them still play when a ship comes close. "
        "Follow them, room by room.\n\n"
        "The haze round The Hollow is thickening. Once it closes, no ship will find the way in. You have twenty minutes.\n")
_DOOR = ("#### [Find the Way In](door)\n---\nScope: shared\nStarts when: at once\n"
         "Objective: Bring the ship to the mouth of The Hollow\nDone when: reach entrance 1000\nReward: 50 credits\n"
         "Part of: survey\nRequired: true\n---\nThe Hollow has one door. Start there.\n")
_FIRST = ("#### [The First Marker](first)\n---\nScope: shared\nStarts when: revealed\n"
          "Objective: Take the ship into The Vault, as far as the altar\nDone when: reach altar 600\nReward: 50 credits\n"
          "Then: reveal survey/second\nPart of: survey\nRequired: true\n---\n"
          "An old survey marker is transmitting from the far room.\n")
_SECOND = ("#### [The Second Marker](second)\n---\nScope: shared\nStarts when: revealed\n"
           "Objective: Find the niche at the back of The Gallery\nDone when: reach niche 400\nReward: 100 credits\n"
           "Part of: survey\nRequired: true\n---\n"
           "The first survey team put something back, somewhere at the back of the built room.\n")
_TAKE = ("#### [What Rook Put Back](take)\n---\nScope: shared\nStarts when: revealed\n"
         "Objective: Answer the second marker on Comms\nDone when: signal hollow_taken\nReward: 300 credits\n"
         "Action:\n  - rook hails rook_niche\nPart of: survey\nRequired: true\n---\n"
         "The second marker is playing. Hear it out, and bring aboard what is in the niche.\n\n"
         "Rook's team took it from the altar forty years ago, and then they carried it back. "
         "His recordings are the only account of why.\n")
_SCANS = ("### [Altar Reading](altar_scan)\n---\nScan of: altar\nTab: scan\n---\n"
          "% A stone table, one piece with the floor. The bowl worn into its top is empty.\n\n"
          "### [Niche Reading](niche_scan)\n---\nScan of: niche\nTab: scan\n---\n"
          "% A square recess, cut later than the room. Something small and dense sits at the back of it.\n")
_CALLS = ("### [Rook at the Niche](rook_niche)\n---\nSpeaker: rook\nWhen: hail\nTitle: A second recording\nPriority: 5\n---\n"
          "% Marker two. This is where we put it back. We could not keep it.\n"
          "% Marker two, the Gallery. It is in the niche. We carried it out once, and then we carried it back.\n\n"
          "- [What is it?](rook_what)\n- [Take it aboard.]() ; signal hollow_taken\n\n"
          "### [What It Is](rook_what)\n---\nSpeaker: rook\n---\n"
          "% A bowl. Stone, like the table. It sat on the altar longer than there have been people to count.\n\n"
          "- [Take it aboard.]() ; signal hollow_taken\n")

STATES = {
    # Lecture 6's finished files
    "start": {"folder": "c1-03-editor-and-first-run/example", "over": ("c4-06-clues-side-stories-cutscenes/example",)},
    # Step 2: the arc, below the last quest
    "arc": {"base": "start", "edits": [
        ("replace", FILE, "Nobody has stood in that room since.\n\n", "Nobody has stood in that room since.\n\n" + _ARC + "\n")]},
    # Step 3: the first step
    "door": {"base": "arc", "edits": [
        ("replace", FILE, "You have twenty minutes.\n", "You have twenty minutes.\n\n" + _DOOR)]},
    # Step 4: two more steps, then the door reveals the first
    "first": {"base": "door", "edits": [
        ("replace", FILE, "The Hollow has one door. Start there.\n", "The Hollow has one door. Start there.\n\n" + _FIRST)]},
    "second": {"base": "first", "edits": [
        ("replace", FILE, "An old survey marker is transmitting from the far room.\n",
         "An old survey marker is transmitting from the far room.\n\n" + _SECOND)]},
    "door_then": {"base": "second", "edits": [
        ("replace", FILE, "Reward: 50 credits\nPart of: survey", "Reward: 50 credits\nThen: reveal survey/first\nPart of: survey")]},
    # Step 5: the second step reveals the last, and the last waits for a word
    "second_then": {"base": "door_then", "edits": [
        ("replace", FILE, "Reward: 100 credits\nPart of: survey", "Reward: 100 credits\nThen: reveal survey/take\nPart of: survey")]},
    "take": {"base": "second_then", "edits": [
        ("replace", FILE, "back of the built room.\n", "back of the built room.\n\n" + _TAKE)]},
    "calls": {"base": "take", "edits": [
        ("replace", FILE, "reveal cairn, accepts stayed\n", "reveal cairn, accepts stayed\n\n" + _CALLS)]},
    # Step 6: what Science reads. The page's own example.
    "final": {"base": "calls", "edits": [
        ("replace", FILE, "matches no weapon in use in this sector.\n\n", "matches no weapon in use in this sector.\n\n" + _SCANS + "\n")],
              "same_as": (_EX + "/mission.amd",)},
    # Step 7: three breaks, each undone
    "b_wayin": {"base": "final", "edits": [("replace", FILE, "reach entrance 1000", "reach way_in 1000")]},
    "b_reveal": {"base": "final", "edits": [("replace", FILE, "Then: reveal survey/first", "Then: reveal first")]},
    "b_req": {"base": "final", "edits": [
        ("replace", FILE, "Action:\n  - rook hails rook_niche\nPart of: survey\nRequired: true\n", "Action:\n  - rook hails rook_niche\n")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

STILLS = {
    # The editor. Each window shows the 20 lines round the line named.
    "e_arc": ("vscode", "arc", 84, "big", _NS),                # lines 74 to 94: the arc's heading
    "e_door": ("vscode", "door", 97, "big", _NS),              # lines 87 to 107: Find the Way In
    "e_way_in": ("vscode", "final", 242, "big", _NS),          # lines 232 to 252: The Way In, Roles: entrance
    "e_marker_one": ("vscode", "final", 44, "big", _NS),       # lines 34 to 54: Marker One, `reach altar 600`
    "e_first": ("vscode", "second", 112, "big", _NS),          # lines 102 to 122: the first and second steps
    "e_chain": ("vscode", "second_then", 106, "big", _NS),     # lines 96 to 116: the door's and the first step's Then lines
    "e_second": ("vscode", "second_then", 124, "big", _NS),    # lines 114 to 134: The Second Marker
    "e_niche_place": ("vscode", "final", 260, "big", _NS),     # lines 250 to 270: The Niche, Hidden: yes
    "e_take": ("vscode", "take", 138, "big", _NS),             # lines 128 to 148: What Rook Put Back
    "e_calls": ("vscode", "final", 355, "big", _NS),           # lines 345 to 365: Rook at the Niche and What It Is
    "e_altar": ("vscode", "final", 252, "big", _NS),           # lines 242 to 262: The Altar's Scan: line
    "e_scans": ("vscode", "final", 175, "big", _NS),           # lines 165 to 185: Altar Reading and Niche Reading
    "e_wayin_b": ("vscode", "b_wayin", 97, "big", _NS),        # lines 87 to 107: `reach way_in 1000`
    "e_reveal_b": ("vscode", "b_reveal", 99, "big", _NS),      # lines 89 to 109: `Then: reveal first`
    "e_req": ("vscode", "final", 138, "big", _NS),             # lines 128 to 148: Part of / Required on the last step
    "t_final": ("terminal", [("final", _LINT)]),
    "t_wayin": ("terminal", [("b_wayin", _LINT)]),
    "t_reveal": ("terminal", [("b_reveal", _LINT)]),
    "t_req": ("terminal", [("b_req", _LINT)]),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c7_list0": ("game", "Helm, the handheld icon then Quests, at once: The Hollow Survey with ONE step, Find the Way In"),
    "game_c7_list1": ("game", "Helm, the handheld icon then Quests, inside 1000 of The Way In: Find the Way In Done, The First Marker running"),
    "game_c7_vault": ("game", "Helm in The Vault, inside 600 of The Altar"),
    "game_c7_calls": ("game", "Comms, the call list: the altar call on top, the ring call below it"),
    "game_c7_science": ("game", "Science, The Altar selected, the scan tab: the Altar Reading"),
    "game_c7_list3": ("game", "Helm, the handheld icon then Quests, inside 400 of The Niche: three steps Done, What Rook Put Back running"),
    "game_c7_second": ("game", "Comms, the call list: the second recording ('A second recording') at the TOP"),
    "game_c7_takeit": ("game", "Comms, Rook at the Niche open: the answers 'What is it?' and 'Take it aboard.'"),
    "game_c7_end": ("game", "The end screen after 'Take it aboard.': the win"),
    # drawn
    "card_chain": ("card", "table", {"heading": "Step 1 - What an episode is", "nth": 1, "kicker": "Every episode is the same chain"}),
    "card_today": ("card", "table", {"heading": "Step 1 - What an episode is", "nth": 2, "kicker": "What your mission can do today"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A second tab, a fifth step, a way to lose, two breaks"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 8", "sub": "The crew goes outside, in suits"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c7_list0"},
        {"from": 2, "still": "game_c7_vault"},
        {"from": 3, "still": "game_c7_list3"},
        {"from": 4, "still": "game_c7_takeit"},
        {"from": 5, "still": "game_c7_end"},
    ]},
    "s02_what_an_episode_is": {"step": 1, "beats": [
        {"from": 0, "still": "card_chain"},
        {"from": 3, "still": "card_chain", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_chain", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_chain", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 6, "still": "card_chain", "marks": [("part", "r5")]},
        {"from": 8, "still": "card_today"},
        {"from": 9, "still": "card_today", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_today", "marks": [("part", "r5")]},
        {"from": 11, "still": "card_today", "marks": [("part", "r4")]},
    ]},
    "s03_the_heading": {"step": 2, "beats": [
        {"from": 0, "still": "e_arc", "marks": [("lines", 77, 77)]},
        {"from": 1, "still": "e_arc", "marks": [("lines", 74, 75)]},
        {"from": 2, "still": "e_arc", "marks": [("lines", 77, 77)]},
        {"from": 3, "still": "e_arc", "marks": [("lines", 79, 79)]},
        {"from": 4, "still": "e_arc", "marks": [("lines", 81, 82)]},
        {"from": 5, "still": "e_arc", "marks": [("lines", 83, 83)]},
        {"from": 6, "still": "e_arc", "marks": [("lines", 84, 84)]},
        {"from": 7, "still": "e_arc", "marks": [("lines", 79, 84)]},
        {"from": 8, "still": "e_arc", "marks": [("lines", 86, 90)]},
        {"from": 10, "still": "e_arc", "marks": [("lines", 86, 86)]},
        {"from": 12, "still": "e_arc", "marks": [("lines", 88, 88)]},
        {"from": 13, "still": "e_arc", "marks": [("lines", 90, 90)]},
    ]},
    "s04_the_way_in": {"step": 3, "beats": [
        {"from": 0, "still": "e_door", "marks": [("lines", 92, 102)]},
        {"from": 1, "still": "e_door", "marks": [("lines", 92, 92)]},
        {"from": 2, "still": "e_door", "marks": [("lines", 97, 97)]},
        {"from": 4, "still": "e_marker_one", "marks": [("text", 44, "reach altar 600")]},
        {"from": 5, "still": "e_door", "marks": [("lines", 97, 97)]},
        {"from": 7, "still": "e_way_in", "marks": [("lines", 242, 242)]},
        {"from": 8, "still": "e_way_in", "marks": [("text", 238, "(way_in)")]},
        {"from": 10, "still": "e_door", "marks": [("text", 97, "1000")]},
    ]},
    "s05_room_by_room": {"step": 4, "beats": [
        {"from": 0, "still": "e_first", "marks": [("lines", 104, 104), ("lines", 117, 117)]},
        {"from": 1, "still": "e_first", "marks": [("lines", 107, 107), ("lines", 120, 120)]},
        {"from": 2, "still": "e_chain", "marks": [("text", 99, "survey/first")]},
        {"from": 3, "still": "e_chain", "marks": [("text", 112, "survey/second")]},
        {"from": 4, "still": "e_chain", "marks": [("text", 99, "survey/first"), ("text", 112, "survey/second")]},
        {"from": 6, "still": "e_marker_one", "marks": [("text", 44, "reach altar 600")]},
        {"from": 9, "still": "e_chain", "marks": [("text", 110, "reach altar 600")]},
        {"from": 10, "still": "game_c7_vault"},
        {"from": 11, "still": "game_c7_calls"},
        {"from": 12, "still": "e_second", "marks": [("lines", 123, 123)]},
        {"from": 13, "still": "e_niche_place", "marks": [("lines", 261, 261)]},
        {"from": 15, "still": "game_c7_calls"},
        {"from": 16, "still": "e_second", "marks": [("lines", 118, 129)]},
    ]},
    "s06_the_step_that_waits_for_a_wo": {"step": 5, "beats": [
        {"from": 0, "still": "e_take", "marks": [("lines", 131, 146)]},
        {"from": 2, "still": "game_c7_takeit"},
        {"from": 3, "still": "e_take", "marks": [("lines", 136, 136)]},
        {"from": 4, "still": "e_take", "marks": [("text", 136, "hollow_taken")]},
        {"from": 5, "still": "e_take", "marks": [("lines", 138, 139)]},
        {"from": 7, "still": "e_calls", "marks": [("lines", 346, 357)]},
        {"from": 8, "still": "e_calls", "marks": [("lines", 356, 356)]},
        {"from": 9, "still": "e_calls", "marks": [("text", 357, "signal hollow_taken")]},
        {"from": 11, "still": "e_take", "marks": [("lines", 136, 137)]},
        {"from": 12, "still": "game_c7_end"},
        {"from": 13, "still": "e_calls", "marks": [("lines", 357, 357), ("lines", 365, 365)]},
        {"from": 19, "still": "game_c7_takeit"},
        {"from": 20, "still": "e_take", "marks": [("text", 136, "hollow_taken")]},
        {"from": 23, "still": "e_take", "marks": [("lines", 136, 136)]},
    ]},
    "s07_what_science_reads": {"step": 6, "beats": [
        {"from": 0, "still": "e_altar", "marks": [("lines", 252, 252)]},
        {"from": 2, "still": "game_c7_science"},
        {"from": 3, "still": "e_scans", "marks": [("lines", 168, 181)]},
        {"from": 4, "still": "e_altar", "marks": [("lines", 250, 250)]},
        {"from": 5, "still": "e_scans", "marks": [("lines", 170, 170)]},
        {"from": 6, "still": "e_scans", "marks": [("lines", 170, 173)]},
        {"from": 7, "still": "e_altar", "marks": [("lines", 252, 252)]},
        {"from": 8, "still": "e_scans", "marks": [("lines", 168, 173)]},
    ]},
    "s08_lint": {"step": 7, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_wayin_b", "marks": [("text", 97, "way_in")]},
        {"from": 2, "still": "t_wayin", "marks": [("span", 1, "role-nothing-wears")]},
        {"from": 4, "still": "e_reveal_b", "marks": [("text", 99, "reveal first")]},
        {"from": 5, "still": "t_reveal", "marks": [("span", 1, "reveal-path")]},
        {"from": 7, "still": "e_req", "marks": [("lines", 140, 141)]},
        {"from": 8, "still": "t_req", "marks": [("part", "run1:clean")]},
        {"from": 9, "still": "e_chain", "marks": [("lines", 100, 101), ("lines", 113, 114)]},
        {"from": 12, "still": "t_req", "marks": [("part", "run1:clean")]},
        {"from": 13, "still": "e_chain", "marks": [("lines", 100, 101), ("lines", 113, 114)]},
    ]},
    "s09_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_c7_list0"},
        {"from": 1, "still": "game_c7_list1"},
        {"from": 3, "still": "game_c7_calls"},
        {"from": 4, "still": "game_c7_vault"},
        {"from": 5, "still": "game_c7_calls"},
        {"from": 6, "still": "game_c7_science"},
        {"from": 7, "still": "game_c7_calls"},
        {"from": 8, "still": "game_c7_list3"},
        {"from": 9, "still": "game_c7_second"},
        {"from": 10, "still": "game_c7_takeit"},
        {"from": 11, "still": "game_c7_end"},
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
