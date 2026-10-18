"""Storyboard for c4-10-a-ruin-episode: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-17).

The lecture starts from MyRuin as Lecture 9 left it (`c4-09-station-repair\\example\\
mission.amd`, 554 lines) and Lecture 6's story.mast (116 lines, never opened here). The
states, in the order the video types them: m1 Lecture 9's quest Raise the Mast deleted from
the end of the Quests section, m2 Raise the Mast typed again inside the arc with four
hashes, m3 Find the Way In `Starts when: revealed`, f1 the quest Forty-One, f2 the altar's
answer `; learn tally, accepts forty_one`, f3 `Scene:` and `Scan:` on The Cairn, f4 the
scenes At the Cairn and The Count (= final, the page's own example, byte for byte, 587
lines). "typo" is Step 4's `accepts fourty_one`; "loss" is "The other ending" (`Fails when:
20 seconds`); "logempty" is the finished file with an empty `mast.runtime.log` beside it.
The page's optional Side Stories section is NOT shown: the capstone file and its walk do
not have it (the script keeps it off camera unless lint is shown clean).

GAME STILLS. NOT YET TAKEN: no Class 4 game still exists. They are taken in ONE scouting
sitting in the real engine, after Lectures 8 and 9 are scouted (this episode has been walked
by a script only; nobody has played it, and nothing in it has been flown by a person, so
scout it first and fix the page where the screen differs; time the whole walk while there,
the forty minutes is a guess). The walk is Step 5 of the page, row by row:
`python game.py c4-10-a-ruin-episode start --state final --consoles server,helm,comms`
Two people, or one at two consoles. If a console closes when the suit appears, add
`eva_set_suit_hull("tsn_shuttle")` as Lecture 8's page says. No probe patch. The run ends a
game (it writes a line to the game's game_results.yaml: that is fine). No marks yet. Press
order, with the row of the walk table:
  1. Row 1, Helm: open the quest list at once: game_c10_quests0 (The Hollow Survey with ONE
     step, Raise the Mast).
  2. Row 2, Helm: fly within 3000 of DS 1's airlock. Handheld, Boarding Party:
     game_c10_party_ds1 (it names DS 1 Worksite, the button SUIT UP).
  3. Row 3: SUIT UP. Nav: Survey Mast. Fire: select the row, press again:
     game_c10_mast (the banner 'REPAIR - Survey Mast, 12s'). Fourteen seconds later the
     quest list: game_c10_quests1 (Raise the Mast done, Find the Way In appearing).
  4. Row 4: Crew, Come aboard. Fly to within 1000 of the door of The Hollow:
     game_c10_door (the ship at the mouth, The First Marker appearing).
  5. Row 5: the Boarding Party app: game_c10_party_hollow (it names The Hollow now). SUIT UP.
  6. Row 6: Nav, The Ring Plate. Comms: game_c10_comms_ring ('A recording at the ring',
     the answer Log the names.). Choose it.
  7. Row 7: Nav, The Altar. On arrival, Act: game_c10_altar_act (the scene At the Altar, its
     two answers). Comms: game_c10_comms_altar ('A recording at the altar').
  8. Row 8: choose Read the marks on the rim: game_c10_marks (the marks scene, Step back).
     Step back. Helm's quest list: game_c10_quests2 (Forty-One in it).
  9. Row 9, Comms: Play the entry keyed to Dace., Mark the side room., Mark the Gallery.:
     game_c10_comms_dace (the call with its answers; The One Who Stayed is in the list).
 10. Row 10: Nav, The Cairn. On arrival: game_c10_stayed (the strip line 'Quest complete:
     The One Who Stayed'), game_c10_cutscene (the cutscene on the main screen, server
     console), game_c10_cairn_act (Act: the scene At the Cairn with Count the stones against
     the tally and Leave her be).
 11. Row 11: Count the stones against the tally: game_c10_count (the scene The Count, Log it).
     Log it: game_c10_done41 (the strip line 'Quest complete: Forty-One').
 12. Row 12: Nav, The Gallery Door. Fire: game_c10_beam (the banner 'BEAM - The Fallen
     Slab, 12s'). Fourteen seconds later the slab is open.
 13. Row 13: Nav, The Niche. Comms: game_c10_comms_second ('A second recording', the answer
     Open the niche.). Choose it. (No "bowl beside the suit" frame: the suit stands at the
     niche, so the bowl is taken the moment it appears - engine-seen 2026-10-18.)
 14. Row 14: the suit takes the bowl: game_c10_pickup ('Pickup: The Stone Bowl').
 15. Row 15: Crew, Come aboard: game_c10_crew. Fly to within 1000 of DS 1: game_c10_win (the
     end screen with the Win: sentence).
 16. The other ending, a second start with the clock at 20 seconds:
     `python game.py c4-10-a-ruin-episode start --state loss --consoles server,helm,comms`,
     sit still: game_c10_lose (the end screen with the Lose: sentence). Never caption a face.
"""
LECTURE = "c4-10-a-ruin-episode"
TITLE = ("Class 4, Lecture 10", "A ruin episode", "Everything you have written, as one story")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_C6 = "c4-06-clues-side-stories-cutscenes/example"      # the story.mast (Lecture 6's card)
_PREV = "c4-09-station-repair/example"
_EX = "c4-10-a-ruin-episode/example"

_LEFT_END = "Nobody at DS 1 knows what is in them.\n\n"
_SCANS = "// ---- Science scans."
_RAISE_OLD = """### [Raise the Mast](raise_mast)
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
_HAZE = "You have forty minutes.\n\n"
_MAST_UP = """#### [Raise the Mast](mast_up)
---
Scope: shared
Starts when: at once
Objective: Go outside at DS 1 and mend the survey mast
Done when: signal mast_repaired
Reward: 40 credits
Then: reveal survey/door
Part of: survey
Required: true
---
![](ship://starbase_command) Orders from DS 1, the station you started at.

The station's survey antenna is dead. Until it is mended, nobody can hear the markers in The Hollow.

- ![](icon://person) Suit up while the ship is near DS 1
- ![](icon://wrench) Fly the suit round the hull to the mast, and mend it with the beam

"""
_DOOR_HEAD = "#### [Find the Way In](door)"
_WAY_OLD = "Starts when: at once\nObjective: Bring the ship to the mouth of The Hollow"
_WAY_NEW = "Starts when: revealed\nObjective: Bring the ship to the mouth of The Hollow"
_STAYED_END = "Nobody has stood in that room since.\n\n"
_FORTY = """### [Forty-One](forty_one)
---
Scope: shared
Starts when: revealed
Objective: Find out what the tally on the altar was counting
Done when: signal count_matched
Reward: 80 credits
---
Somebody cut marks into the rim of the altar, in sets of five. Find out what they were counting.

| The marks | What the crew knows |
|---|---|
| How many | Forty-one. Eight sets of five, and one on its own |
| Who cut them | Nobody has said |

Whoever kept the count kept it for a long time, and then stopped.

"""
_SURVEY_HEAD = "### [The Hollow Survey](survey)"
_ALTAR_OLD = "- [Read the marks on the rim](altar_marks)\n"
_ALTAR_NEW = "- [Read the marks on the rim](altar_marks) ; learn tally, accepts forty_one\n"
_CAIRN_OLD = "Dress: plain_asteroid_9 0.4\n---"
_CAIRN_NEW = ("Dress: plain_asteroid_9 0.4\nScene: cairn_look\n"
              "Scan: A cairn of flat stones, laid by hand. Somebody is under it.\n---")
_BACK = "- [Step back]()\n"
_SCENES = """
### [At the Cairn](cairn_look)
% A pile of flat stones, taller than a person, in the middle of the room. Each one was carried here.

- [Count the stones against the tally](cairn_count) if learned >= 1
- [Leave her be]()

### [The Count](cairn_count)
% Forty-one stones. Forty-one marks on the rim of the altar. They stayed with her as long as they could.

- [Log it]() ; signal count_matched
"""

STATES = {
    "start": {"folder": _C6, "over": (_PREV,)},
    "m1": {"base": "start", "edits": [("replace", FILE, _LEFT_END + _RAISE_OLD + _SCANS, _LEFT_END + _SCANS)]},
    "m2": {"base": "m1", "edits": [("replace", FILE, _HAZE + _DOOR_HEAD, _HAZE + _MAST_UP + _DOOR_HEAD)]},
    "m3": {"base": "m2", "edits": [("replace", FILE, _WAY_OLD, _WAY_NEW)]},
    "f1": {"base": "m3", "edits": [("replace", FILE, _STAYED_END + _SURVEY_HEAD, _STAYED_END + _FORTY + _SURVEY_HEAD)]},
    "f2": {"base": "f1", "edits": [("replace", FILE, _ALTAR_OLD, _ALTAR_NEW)]},
    "f3": {"base": "f2", "edits": [("replace", FILE, _CAIRN_OLD, _CAIRN_NEW)]},
    "f4": {"base": "f3", "edits": [("replace", FILE, _BACK, _BACK + _SCENES)],
           "same_as": (_EX + "/mission.amd",)},
    "final": {"base": "f4"},
    # Step 4: the quest misspelled on the answer
    "typo": {"base": "final", "edits": [
        ("replace", FILE, "; learn tally, accepts forty_one", "; learn tally, accepts fourty_one")]},
    # Step 5: the other ending
    "loss": {"base": "final", "edits": [("replace", FILE, "Fails when: 40 minutes", "Fails when: 20 seconds")]},
    # and the log after both: empty
    "logempty": {"base": "final", "edits": [("write", "mast.runtime.log", "")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

# centers of the 21-line windows, and the lines marked (from the states above)
_C = {"old": 200, "m1": 193, "m2": 100, "m3": 108, "altar_old": 520, "f1": 85, "f2": 536, "f3": 380, "f4": 551,
      "typo": 538, "loss": 99, "log": 1}
_L = {"old_a": 193, "old_b": 206, "m2_head": 92, "m2_then": 99, "m2_part": 100, "m2_req": 101, "m2_lead": 103,
      "m2_para": 105, "m2_list_a": 107, "m2_list_b": 108, "m3_starts": 113, "f2_ans": 536,
      "f1_tab_a": 87, "f1_tab_b": 90, "f1_how": 89, "f3_scene": 381, "f3_scan": 382,
      "f4_count": 549, "f4_leave": 550, "f4_log": 555, "typo_ans": 538, "fails": 99}

STILLS = {
    "e_old": ("vscode", "start", _C["old"], "big", _NS),
    "e_m1": ("vscode", "m1", _C["m1"], "big", _NS),
    "e_m2": ("vscode", "m2", _C["m2"], "big", _NS),
    "e_m3": ("vscode", "m3", _C["m3"], "big", _NS),
    "e_altar_old": ("vscode", "m3", _C["altar_old"], "big", _NS),
    "e_f1": ("vscode", "f1", _C["f1"], "big", _NS),
    "e_f2": ("vscode", "f2", _C["f2"], "big", _NS),
    "e_f3": ("vscode", "f3", _C["f3"], "big", _NS),
    "e_f4": ("vscode", "f4", _C["f4"], "big", _NS),
    "e_typo": ("vscode", "typo", _C["typo"], "big", _NS),
    "e_loss": ("vscode", "loss", _C["loss"], "big", _NS),
    "e_log": ("vscode", "logempty", _C["log"], "mid", {"file": "mast.runtime.log", "wrap": True, "side": False}),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_typo": ("terminal", [("typo", _LINT)]),
    # THE REAL GAME (NOT YET TAKEN; see the docstring). State final (loss: game_c10_lose), consoles server,helm,comms. No marks yet.
    "game_c10_quests0": ("game", "Helm's quest list at the start: The Hollow Survey with ONE step, Raise the Mast"),
    "game_c10_party_ds1": ("game", "Helm, the Boarding Party app near DS 1: it names DS 1 Worksite, and the button SUIT UP"),
    "game_c10_mast": ("game", "The suit's Fire app at the mast after the row is selected and pressed again: the banner 'REPAIR - Survey Mast, 12s'"),
    "game_c10_quests1": ("game", "Helm's quest list after the repair: Raise the Mast done, Find the Way In now in the list"),
    "game_c10_door": ("game", "Helm, the ship at the mouth of The Hollow: Find the Way In done, The First Marker appearing"),
    "game_c10_party_hollow": ("game", "Helm, the Boarding Party app at the door: it names The Hollow, and the button SUIT UP"),
    "game_c10_comms_ring": ("game", "Comms, the call 'A recording at the ring' with the answer Log the names."),
    "game_c10_altar_act": ("game", "The suit at The Altar, the Act app: the scene 'At the Altar', its words and its two answers"),
    "game_c10_comms_altar": ("game", "Comms, the call 'A recording at the altar'"),
    "game_c10_marks": ("game", "The suit's Act app after Read the marks on the rim: the scene The Marks and the answer Step back"),
    "game_c10_quests2": ("game", "Helm's quest list after the marks are read: Forty-One in it, beside the arc"),
    "game_c10_comms_dace": ("game", "Comms, the call with the answers Play the entry keyed to Dace. / Mark the side room. / Mark the Gallery."),
    "game_c10_stayed": ("game", "The strip line 'Quest complete: The One Who Stayed' as the suit reaches The Cairn"),
    "game_c10_cutscene": ("game", "The server console's main screen playing the cairn's cutscene"),
    "game_c10_cairn_act": ("game", "The suit at The Cairn, the Act app: the scene 'At the Cairn' with Count the stones against the tally and Leave her be"),
    "game_c10_count": ("game", "The suit's Act app on the scene The Count, the answer Log it"),
    "game_c10_done41": ("game", "The strip line 'Quest complete: Forty-One' after Log it"),
    "game_c10_beam": ("game", "The suit's Fire app at The Gallery Door: the banner 'BEAM - The Fallen Slab, 12s'"),
    "game_c10_comms_second": ("game", "Comms, the call 'A second recording' with the answer Open the niche."),
    "game_c10_pickup": ("game", "The suit has taken the bowl: the line 'Pickup: The Stone Bowl' and Carry It Home appearing"),
    "game_c10_crew": ("game", "The suit's Crew app: the button Come aboard"),
    "game_c10_win": ("game", "The end screen at DS 1: the Win: sentence 'The Hollow is surveyed, and what Rook put back is aboard.'"),
    "game_c10_lose": ("game", "(state loss) The end screen after sitting still: the Lose: sentence 'The haze closed in before the survey was done.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_episode": ("card", "table", {"heading": "Step 1 - The episode on one page", "kicker": "The episode on one page"}),
    "card_walk": ("card", "table", {"heading": "Step 5 - Check it end to end", "kicker": "The walk"}),
    "card_one": ("card", "table", {"heading": "One more thing - a story for one person", "kicker": "A story for one person"}),
    "card_notgiven": ("card", "table", {"heading": "What this class has not given you", "kicker": "What this class has not given you"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "The class project"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c10_mast"},
        {"from": 1, "still": "game_c10_door"},
        {"from": 2, "still": "game_c10_altar_act"},
        {"from": 3, "still": "game_c10_mast"},
        {"from": 4, "still": "game_c10_cairn_act"},
        {"from": 5, "still": "game_c10_win"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_the_episode_on_one_page": {"step": 1, "beats": [
        {"from": 0, "still": "card_episode"},
        {"from": 5, "still": "card_episode", "marks": [("part", "r1"), ("part", "r2"), ("part", "r4"), ("part", "r9"),
                                                         ("part", "r10"), ("part", "r11"), ("part", "r12")]},
        {"from": 7, "still": "card_episode", "marks": [("part", "r3"), ("part", "r5"), ("part", "r6"),
                                                        ("part", "r7"), ("part", "r8")]},
        {"from": 8, "still": "card_episode"},
    ]},
    "s03_the_mast_is_the_first_step": {"step": 2, "beats": [
        {"from": 0, "still": "e_old", "marks": [("lines", _L.get("old_a", 1), _L.get("old_b", 1))]},
        {"from": 1, "still": "e_m2", "marks": [("lines", _L.get("m2_head", 1), _L.get("m2_head", 1))]},
        {"from": 2, "still": "e_m1"},
        {"from": 3, "still": "e_m2", "marks": [("text", _L.get("m2_head", 1), "####")]},
        {"from": 4, "still": "e_m2", "marks": [("lines", _L.get("m2_then", 1), _L.get("m2_req", 1))]},
        {"from": 5, "still": "e_m2", "marks": [("lines", _L.get("m2_then", 1), _L.get("m2_then", 1))]},
        {"from": 6, "still": "e_m2", "marks": [("lines", _L.get("m2_part", 1), _L.get("m2_req", 1))]},
        {"from": 7, "still": "e_m2", "marks": [("lines", _L.get("m2_lead", 1), _L.get("m2_lead", 1)),
                                                 ("lines", _L.get("m2_list_a", 1), _L.get("m2_list_b", 1))]},
        {"from": 8, "still": "e_m2", "marks": [("lines", _L.get("m2_para", 1), _L.get("m2_para", 1))]},
        {"from": 10, "still": "e_m3", "marks": [("lines", _L.get("m3_starts", 1), _L.get("m3_starts", 1))]},
    ]},
    "s04_a_clue_for_the_crew_who_go_i": {"step": 3, "beats": [
        {"from": 0, "still": "e_altar_old"},
        {"from": 4, "still": "e_f2", "marks": [("lines", _L.get("f2_ans", 1), _L.get("f2_ans", 1))]},
        {"from": 5, "still": "e_f2", "marks": [("text", _L.get("f2_ans", 1), "learn tally, accepts forty_one")]},
        {"from": 6, "still": "e_f1", "marks": [("lines", _L.get("f1_tab_a", 1), _L.get("f1_tab_b", 1))]},
        {"from": 7, "still": "e_f1", "marks": [("lines", _L.get("f1_tab_a", 1), _L.get("f1_tab_a", 1))]},
        {"from": 8, "still": "e_f1", "marks": [("lines", _L.get("f1_how", 1), _L.get("f1_how", 1))]},
        {"from": 9, "still": "e_f3", "marks": [("lines", _L.get("f3_scene", 1), _L.get("f3_scan", 1))]},
        {"from": 10, "still": "e_f4", "marks": [("text", _L.get("f4_count", 1), "if learned >= 1")]},
        {"from": 11, "still": "e_f4", "marks": [("lines", _L.get("f4_count", 1), _L.get("f4_count", 1))]},
        {"from": 12, "still": "e_f4", "marks": [("lines", _L.get("f4_leave", 1), _L.get("f4_leave", 1))]},
        {"from": 13, "still": "e_f4", "marks": [("text", _L.get("f4_log", 1), "signal count_matched")]},
    ]},
    "s05_lint": {"step": 4, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_typo", "marks": [("text", _L.get("typo_ans", 1), "fourty_one")]},
        {"from": 2, "still": "t_typo", "marks": [("span", 1, "outcome-quest-missing")]},
        {"from": 3, "still": "t_typo"},
        {"from": 5, "still": "card_walk"},
    ]},
    "s06_the_walk": {"step": 5, "beats": [
        {"from": 0, "still": "card_walk"},
        {"from": 3, "still": "game_c10_quests0"},
        {"from": 4, "still": "game_c10_party_ds1"},
        {"from": 5, "still": "game_c10_mast"},
        {"from": 6, "still": "game_c10_quests1"},
        {"from": 7, "still": "card_walk", "marks": [("part", "r3")]},
        {"from": 8, "still": "game_c10_door"},
        {"from": 9, "still": "card_walk", "marks": [("part", "r4")]},
    ]},
    "s07_inside": {"step": 5, "beats": [
        {"from": 0, "still": "game_c10_party_hollow"},
        {"from": 1, "still": "game_c10_comms_ring"},
        {"from": 2, "still": "game_c10_altar_act"},
        {"from": 3, "still": "game_c10_marks"},
        {"from": 4, "still": "game_c10_quests2"},
        {"from": 5, "still": "game_c10_comms_dace"},
        {"from": 7, "still": "game_c10_stayed"},
        {"from": 8, "still": "game_c10_cutscene"},
        {"from": 9, "still": "game_c10_cairn_act"},
        {"from": 10, "still": "game_c10_count"},
        {"from": 11, "still": "game_c10_done41"},
    ]},
    "s08_the_bowl_and_home": {"step": 5, "beats": [
        {"from": 0, "still": "game_c10_beam"},
        {"from": 1, "still": "game_c10_comms_second"},
        {"from": 2, "still": "game_c10_pickup"},
        {"from": 3, "still": "game_c10_crew"},
        {"from": 4, "still": "game_c10_win"},
        {"from": 5, "still": "card_walk", "marks": [("part", "r15")]},
        {"from": 6, "still": "card_walk"},
        {"from": 7, "still": "e_loss", "marks": [("lines", _L.get("fails", 1), _L.get("fails", 1))]},
        {"from": 9, "still": "game_c10_lose"},
        {"from": 10, "still": "e_log"},
    ]},
    "s09_one_more_thing_and_what_you_": {"step": None, "beats": [
        {"from": 0, "still": "card_one"},
        {"from": 2, "still": "card_one", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_one", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_one"},
        {"from": 5, "still": "card_notgiven"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3"), ("part", "item4"), ("part", "item5")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item6")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item8")]},
        {"from": 6, "still": "card_exercise"},
    ]},
}
