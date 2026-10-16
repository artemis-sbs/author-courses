"""Storyboard for c3-05-personal-quests: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 4's finished files ("start": the `sbs create` folder of
Class 1 Lecture 3 for the files nobody edits, with Class 3 Lectures 2 to 4 laid over it).
A Side Stories section with Six Names, the surgeon's reading sends its signal, the card
hands the stories to the visit, A Cold Core and its signal, then Six Names leads on to the
ship's Account for the Crew ("final", the page's own example\\mission.amd and story.mast).

NO COMMAND STARTS THE GAME HERE. `sbs run server,helm,engineering,science -m MyBoarding
map=0` is a drawn card of the page's own words (card_run).

GAME STILLS. Not taken yet (marks to be set from the screenshots). The handheld a party
member carries is the xESS: BEAM DOWN turns the console into it, Act opens by itself on
each new room (a running transcript, the newest room at the foot, its choices as buttons),
and Back (top right of the ACT title line) goes to the tile sheet: Crew, Act, and Tasks
for someone holding a story of their own. Tasks lists that person's stories under their
name, then the ship's quests under Party. The bridge is told `Quest complete:` on the
strip under Helm's left panel, one line at a time (Class 2). Two games, each with Helm
left on the bridge to watch, both from the PROBE-ONLY state g_now (never shown in the
editor): Close Inspection finishes by itself a minute in (`Done when: 60 seconds` in place
of `reach derelict 500`), so nobody has to fly and Helm can sit and watch.

    Game A - the surgeon goes alone:
    python game.py c3-05-personal-quests start --state g_now --consoles server,helm,science
      1. Before the visit (first minute), Helm: the handheld icon top left, Quests,
         Account for the Crew: game_log_account.
      2. When the Boarding Party tile appears, Science (Dr Hale): handheld, Boarding Party,
         BEAM DOWN. Act opens on The Airlock: game_airlock_sci.
      3. Science: Back (top right): game_home_sci. Tasks: game_tasks_sci. Back, Act.
      4. Science presses Read the name tags on the suits. Helm, the strip, at once:
         game_strip_six; then a few seconds later the next line: game_strip_account (keep
         whichever is first as game_strip_six and note the order).
      5. Science: Back, Tasks: game_tasks_done_sci.
    Game B - the chief goes alone (a short crew):
    python game.py c3-05-personal-quests start --state g_now --consoles server,helm,engineering
      1. When the tile appears, Engineering (Chief Okoro): handheld, Boarding Party, BEAM
         DOWN. Back, Tasks: game_tasks_eng. Back, Act on The Airlock: game_airlock_eng.
      2. Engineering presses the suit tags (covering for medical). Helm: handheld, Quests,
         Account for the Crew: game_log_open.
      3. Engineering: Step back, Go aft, Read the shutdown record. Helm, the strip:
         game_strip_core.
"""
LECTURE = "c3-05-personal-quests"
TITLE = ("Class 3, Lecture 5", "Personal quests", "A story for one person")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-05-personal-quests/example"
_SIX = ("\n\n## [Side Stories](side_stories)\n\n"
        "### [Six Names](six_names)\n---\nFor: medical\nStarts when: at once\n"
        "Objective: Find out whose suits are hanging in the airlock\nDone when: signal names_read\n---\n"
        "Six suits on their hooks, and nobody in them. Somebody should read the tags.\n")
_COLD = ("\n### [A Cold Core](cold_core)\n---\nFor: engineering\nStarts when: at once\n"
         "Objective: Find out how the core was stopped\nDone when: signal core_read\n---\n"
         "A reactor does not shut itself down in the right order. Find out who did.\n")
_ACCOUNT = ("### [Account for the Crew](account)\n---\nScope: shared\nStarts when: at once\n"
            "Objective: Find out who was aboard the hulk\nDone when: signal names_known\nReward: 150 credits\n---\n"
            "Somebody crewed that ship. Command wants names.\n\n"
            "## Where names are kept\n\n"
            "- ![](icon://person) Suits. Every suit in an airlock is tagged with its owner's name.\n"
            "- ![](icon://tablet) The log. A captain's log says who is aboard.\n\n"
            "Bring the names home, and DS 1 can tell their families something.\n\n")
_TAGS = "- [Read the name tags on the suits](suits) if medical ; learn suits"
_RECORD = "- [Read the shutdown record](shutdown) if engineering ; learn shutdown"
_VISIT = 'title="The Hulk")'

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c3-02-party-and-place/example", "c3-03-everyone-gets-a-menu/example",
                       "c3-04-crew-and-skills/example")},
    # Step 1: the section, and Six Names (lint: two warnings)
    "st1": {"base": "start", "edits": [("append", FILE, _SIX)]},
    # Step 2: her own reading sends the signal (lint: one warning)
    "st2": {"base": "st1", "edits": [("replace", FILE, _TAGS + "\n", _TAGS + ", signal names_read\n")]},
    # Step 3: the card hands the stories out (lint: clean)
    "st3": {"base": "st2", "edits": [
        ("replace", MAST, _VISIT, 'title="The Hulk", stories=amd_section(MISSION_DOC, "side_stories"))')],
            "same_as": _EX + "/story.mast"},
    # Step 4: A Cold Core, and the engineer's reading sends its signal
    "st4": {"base": "st3", "edits": [("append", FILE, _COLD)]},
    "st4b": {"base": "st4", "edits": [("replace", FILE, _RECORD + "\n", _RECORD + ", signal core_read\n")]},
    # Step 5: Six Names leads on, and the ship's quest that hears it
    "st5": {"base": "st4b", "edits": [
        ("replace", FILE, "Done when: signal names_read\n---", "Done when: signal names_read\nThen: signal names_known\n---")]},
    "final": {"base": "st5", "edits": [
        ("replace", FILE, "so think about who you send.\n\n", "so think about who you send.\n\n" + _ACCOUNT)],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    # Scene 6: two slips, each undone
    "b_medcal": {"base": "final", "edits": [("replace", FILE, "For: medical", "For: medcal")]},
    "b_comma": {"base": "final", "edits": [("replace", FILE, "learn suits, signal names_read", "learn suits signal names_read")]},
    # PROBE-ONLY, for the game stills (see the docstring). Never shown in the editor.
    "g_now": {"base": "final", "edits": [
        ("replace", FILE, "Done when: reach derelict 500", "Done when: 60 seconds")]},
}

_LINT = "sbs lint MyBoarding"
_NS = {"side": False}
_M = {"side": False, "file": MAST, "wrap": True}     # the card's one long line, folded as the editor folds it
_GA = "Game A (state g_now, consoles server,helm,science; Dr Hale beamed down alone, Helm on the bridge)"
_GB = "Game B (state g_now, consoles server,helm,engineering; Chief Okoro beamed down alone, Helm on the bridge)"

STILLS = {
    "e_st1": ("vscode", "st1", 160, "big", _NS),             # lines 150 to 170: the new section and Six Names
    "e_airlock1": ("vscode", "st1", 108, "big", _NS),        # lines 98 to 118: The Airlock
    "e_airlock2": ("vscode", "st2", 108, "big", _NS),
    "e_st2_six": ("vscode", "st2", 165, "big", _NS),         # Six Names, waiting on names_read
    "e_card2": ("vscode", "st2", 115, "mid", _M),            # story.mast: the card's boarding_visit line
    "e_card3": ("vscode", "st3", 115, "mid", _M),
    "e_st4": ("vscode", "st4", 172, "big", _NS),             # A Cold Core under Six Names
    "e_st4b": ("vscode", "st4b", 121, "big", _NS),           # The Reactor Room
    "e_st5": ("vscode", "st5", 170, "big", _NS),             # Six Names with Then:
    "e_final_account": ("vscode", "final", 63, "big", _NS),  # lines 53 to 73: Account for the Crew
    "e_final_airlock": ("vscode", "final", 125, "big", _NS),
    "e_final_six": ("vscode", "final", 186, "big", _NS),     # the two stories
    "e_medcal": ("vscode", "b_medcal", 186, "big", _NS),
    "e_comma": ("vscode", "b_comma", 125, "big", _NS),
    "t_st1": ("terminal", [("st1", _LINT)]),
    "t_st2": ("terminal", [("st2", _LINT)]),
    "t_st3": ("terminal", [("st3", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_medcal": ("terminal", [("b_medcal", _LINT)]),
    "t_comma": ("terminal", [("b_comma", _LINT)]),
    # THE REAL GAME (not taken yet; see the docstring for the two games and the clicks)
    "game_log_account": ("game", _GA + ", step 1, before anyone beams down: Helm's handheld (icon top left), Quests, Account for the Crew selected: Active, Reward 150 credits, the order 'Find out who was aboard the hulk', 'Somebody crewed that ship. Command wants names.', the heading 'Where names are kept', two bullets with a person icon and a tablet icon for dots, and the closing line"),
    "game_airlock_sci": ("game", _GA + ", step 2: Science (Dr Hale), the xESS just after BEAM DOWN, Act on The Airlock: 'The outer door was never sealed...' and the buttons Read the name tags on the suits, Go aft, Go forward, Return to the ship (and the shutdown record does not show here: that is in the reactor room)"),
    "game_home_sci": ("game", _GA + ", step 3: Science, Back pressed: the xESS tile sheet - the airlock line, then three tiles Crew, Act and Tasks"),
    "game_tasks_sci": ("game", _GA + ", step 3: Science, the Tasks app: under 'Dr Hale', Six Names (Active); under 'Party', the ship's quests (Close Inspection, Account for the Crew and the rest)"),
    "game_strip_six": ("game", _GA + ", step 4: Helm, the strip under the left panel just after Dr Hale reads the tags: the first 'Quest complete:' line (Six Names or Account for the Crew - note which came first; if Six Names never appears there, say so)"),
    "game_strip_account": ("game", _GA + ", step 4, a few seconds later: Helm, the strip's next line, 'Quest complete: Account for the Crew' (or Six Names if that came second)"),
    "game_tasks_done_sci": ("game", _GA + ", step 5: Science, Tasks again: Six Names Done under 'Dr Hale', Account for the Crew Done under 'Party'"),
    "game_tasks_eng": ("game", _GB + ", step 1: Engineering, the Tasks app: under 'Chief Okoro', A Cold Core (Active), then the ship's quests under 'Party'. No Six Names anywhere: it was handed to nobody"),
    "game_airlock_eng": ("game", _GB + ", step 1: Engineering, Act on The Airlock: 'Read the name tags on the suits (covering for medical)' among the buttons"),
    "game_log_open": ("game", _GB + ", step 2, after the chief read the tags: Helm, Quests, Account for the Crew selected and still Active"),
    "game_strip_core": ("game", _GB + ", step 3: Helm, the strip under the left panel just after the chief reads the shutdown record: 'Quest complete: A Cold Core'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_for": ("card", "table", {"heading": "Step 6 - Four rules for a side story", "kicker": "What For: takes"}),
    "card_rules": ("card", "list", {"heading": "Step 6 - Four rules for a side story", "kicker": "Four rules"}),
    "card_run": ("card", "points", {"kicker": "In a command prompt in data\\missions",
                                    "items": ["sbs run server,helm,engineering,science -m MyBoarding map=0",
                                              "Fly inside 500 of the hulk. On Engineering and Science: the handheld, Boarding Party, BEAM DOWN"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 6", "sub": "Checkpoint: a short boarding quest"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_airlock_sci"},
        {"from": 1, "still": "game_tasks_sci"},
        {"from": 3, "still": "game_airlock_sci"},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_a_section_for_side_stories": {"step": 1, "beats": [
        # the game first: the story on her handheld
        {"from": 0, "still": "game_tasks_sci"},
        {"from": 4, "still": "e_st1", "marks": [("lines", 161, 168)]},
        {"from": 6, "still": "e_st1", "marks": [("lines", 159, 159)]},
        {"from": 7, "still": "e_st1", "marks": [("text", 163, "For: medical")]},
        {"from": 9, "still": "e_st1", "marks": [("lines", 161, 161)]},
        {"from": 11, "still": "e_st1", "marks": [("text", 164, "Starts when: at once")]},
        {"from": 12, "still": "e_st1", "marks": [("lines", 165, 165)]},
        {"from": 13, "still": "e_st1", "marks": [("text", 166, "Done when: signal names_read")]},
        {"from": 14, "still": "t_st1", "marks": [("part", "run1:last")]},
        {"from": 15, "still": "t_st1", "marks": [("span", 1, "unfired-signal")]},
        {"from": 16, "still": "t_st1", "marks": [("span", 1, "stories-not-handed-out")]},
        {"from": 17, "still": "e_st1", "marks": [("text", 163, "medical")]},
        {"from": 18, "still": "card_for", "marks": [("part", "r2"), ("part", "r3")]},
    ]},
    "s03_her_own_reading_finishes_it": {"step": 2, "beats": [
        # the game first: her reading, in the airlock
        {"from": 0, "still": "game_airlock_sci"},
        {"from": 3, "still": "e_airlock1", "marks": [("lines", 108, 108)]},
        {"from": 4, "still": "e_airlock2", "marks": [("text", 108, ", signal names_read")]},
        {"from": 6, "still": "e_airlock2", "marks": [("text", 108, "names_read")]},
        {"from": 6.5, "still": "e_st2_six", "marks": [("text", 166, "names_read")]},
        {"from": 7, "still": "e_airlock2", "marks": [("text", 108, ", signal")]},
        {"from": 8, "still": "t_st2", "marks": [("span", 1, "stories-not-handed-out")]},
    ]},
    "s04_hand_the_stories_to_the_visi": {"step": 3, "beats": [
        {"from": 0, "still": "e_card2", "marks": [("lines", 112, 116)]},
        {"from": 3, "still": "e_card2", "marks": [("text", 115, "boarding_visit(")]},
        {"from": 4, "still": "e_card3", "marks": [("text", 115, "stories=")]},
        {"from": 5, "still": "e_card3", "marks": [("text", 115, "\"side_stories\"")]},
        {"from": 6, "still": "e_st1", "marks": [("text", 159, "side_stories")]},
        {"from": 7, "still": "t_st3", "marks": [("part", "run1:clean")]},
        {"from": 8, "still": "game_home_sci"},
    ]},
    "s05_a_second_story_and_where_one": {"step": 4, "beats": [
        # the game first: his story on his handheld
        {"from": 0, "still": "game_tasks_eng"},
        {"from": 2, "still": "e_st4", "marks": [("lines", 170, 177)]},
        {"from": 2.5, "still": "e_st4b", "marks": [("text", 121, ", signal core_read")]},
        {"from": 3, "still": "e_st5", "marks": [("text", 167, "Then: signal names_known")]},
        {"from": 6, "still": "e_final_account", "marks": [("text", 61, "Done when: signal names_known")]},
        {"from": 7, "still": "e_final_airlock", "marks": [("text", 125, "signal names_read")]},
        {"from": 9, "still": "e_final_six", "marks": [("text", 183, "signal names_read")]},
        {"from": 10, "still": "e_final_six", "marks": [("text", 184, "Then: signal names_known")]},
        {"from": 11, "still": "e_final_account", "marks": [("text", 62, "Reward: 150 credits")]},
        {"from": 12, "still": "e_final_six", "marks": [("lines", 178, 186)]},
        # the game first: the ship's quest in the Quest Log
        {"from": 14, "still": "game_log_account"},
        {"from": 17, "still": "e_final_account", "marks": [("lines", 66, 69)]},
        {"from": 18, "still": "e_final_account", "marks": [("text", 68, "icon://person"), ("text", 69, "icon://tablet")]},
        {"from": 19, "still": "e_final_six", "marks": [("lines", 186, 186)]},
        {"from": 20, "still": "game_tasks_sci"},
    ]},
    "s06_four_rules_and_lint": {"step": 6, "beats": [
        {"from": 0, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 6, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 7, "still": "e_medcal", "marks": [("text", 180, "medcal")]},
        {"from": 7.5, "still": "t_medcal", "marks": [("span", 1, "for-nobody")]},
        {"from": 8, "still": "e_comma", "marks": [("text", 125, "learn suits signal")]},
        {"from": 8.5, "still": "t_comma", "marks": [("span", 1, "outcome-run-together")]},
    ]},
    "s07_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "card_run", "marks": [("part", "item1")]},
        {"from": 1, "still": "game_airlock_sci"},
        {"from": 2, "still": "game_home_sci"},
        {"from": 5, "still": "game_tasks_sci"},
        {"from": 6, "still": "game_airlock_sci"},
        {"from": 7, "still": "game_strip_six"},
        {"from": 8, "still": "game_strip_account"},
        {"from": 8.5, "still": "game_tasks_done_sci"},
        {"from": 9, "still": "game_tasks_eng"},
        {"from": 11, "still": "game_airlock_eng"},
        {"from": 13, "still": "game_log_open"},
        {"from": 15, "still": "game_strip_core"},
        {"from": 16, "still": "game_log_open"},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 6, "still": "card_next"},
    ]},
}
