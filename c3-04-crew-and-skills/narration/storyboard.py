"""Storyboard for c3-04-crew-and-skills: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 3's finished files ("start": the `sbs create` folder of
Class 1 Lecture 3 for the files nobody edits, with Class 3 Lecture 2's mission.amd and
story.mast and Lecture 3's mission.amd laid over it). Two Skills: lines, the sensor record
on the bridge, the check in the reactor room ("final", the page's own example\\mission.amd).

NO COMMAND STARTS THE GAME HERE. `sbs run server,helm,engineering,science -m MyBoarding
map=0` is a drawn card of the page's own words (card_run).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. The handheld a party
member carries is the xESS: BEAM DOWN turns the console into it, Act opens by itself on
each new room and shows the scene as a running transcript (the newest room at the foot,
its choices as buttons under it), and its Back (top right of the ACT title line) goes to
the xESS home: a list headed `xESS` with three full-width rows, Crew, Act and Tasks. Two games, both from the PROBE-ONLY state g_flat (never shown
in the editor): Close Inspection finishes by itself a minute in (`Done when: 60 seconds`
in place of `reach derelict 500`), so the party opens with nobody at Helm; and the die is
fixed at 5 (`boarding_checks_mode("flat")`, the library's own test switch), so Dr Hale's
try fails and Chief Okoro's works, as the page's example line says.

    Game 1 - three windows, the surgeon and the chief aboard:
    python game.py c3-04-crew-and-skills start --state g_flat --consoles server,engineering,science
      Wait for the Boarding Party tile (about a minute in). On Engineering (Chief Okoro) and
      on Science (Dr Hale): the handheld icon top left, Boarding Party, BEAM DOWN.
      1. Engineering, Act on The Airlock: game_bar_eng.
      2. Either console: Go forward, to the bridge. Science: game_bridge_sci. Engineering:
         game_bridge_eng.
      3. Either: Go back to the airlock, then Go aft, toward the reactor. Science:
         game_reactor_sci. Engineering: game_reactor_eng.
      4. SCIENCE presses Try to wake the core. Science: game_roll_sci.
      5. Either: Step back. ENGINEERING presses Try to wake the core. Engineering:
         game_roll_eng. Science, at once: game_roll_both_sci.
    Game 2 - two windows, the chief alone (the surgeon stays home):
    python game.py c3-04-crew-and-skills start --state g_flat --consoles server,engineering
      Engineering: handheld, Boarding Party, BEAM DOWN.
      1. Act on The Airlock: game_alone_airlock.
      2. Go forward, to the bridge: game_alone_bridge.
"""
LECTURE = "c3-04-crew-and-skills"
TITLE = ("Class 3, Lecture 4", "Crew and skills", "How good each person is")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-04-crew-and-skills/example"
_OKORO = "Roles: engineering\n---\n\n### [Dr Hale](hale)"
_HALE = "Roles: medical\n---\n\n\n## [Scenes](boarding)"
_SENSOR = "- [Answer the log](last_entry) if learned >= 2\n"
_SENSOR_ROOM = ("### [The Sensor Record](sensor_record)\n"
                "% One contact, closing, eleven days before the core went cold. It never arrived. It is still out there.\n\n"
                "- [Step back](bridge)\n\n")
_CORE = "- [Read the shutdown record](shutdown) if engineering ; learn shutdown\n"
_CORE_ROOMS = ("### [The Core Turns Over](core_wakes)\n"
               "% The board lights for four seconds. Long enough to read one line: MANUAL LOCKOUT, CAPTAIN'S KEY.\n\n"
               "- [Step back](reactor)\n\n"
               "### [The Board Stays Dark](core_dead)\n"
               "% Nothing. Not a flicker. Whatever you tried, the core did not notice.\n\n"
               "- [Step back](reactor)\n\n")

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c3-02-party-and-place/example", "c3-03-everyone-gets-a-menu/example")},
    # Step 1: a Skills: line on each person
    "k1": {"base": "start", "edits": [
        ("replace", FILE, _OKORO, "Roles: engineering\nSkills: engineering 4, science 1\n---\n\n### [Dr Hale](hale)")]},
    "k2": {"base": "k1", "edits": [
        ("replace", FILE, _HALE, "Roles: medical\nSkills: medical 4, science 3\n---\n\n\n## [Scenes](boarding)")]},
    # Step 3: the bridge's new choice, then its room (below the bridge, above The Last Entry)
    "s3a": {"base": "k2", "edits": [
        ("replace", FILE, _SENSOR, _SENSOR + "- [Pull the sensor record](sensor_record) if skill science >= 3 ; learn sensors\n")]},
    "s3b": {"base": "s3a", "edits": [
        ("replace", FILE, "### [The Last Entry](last_entry)", _SENSOR_ROOM + "### [The Last Entry](last_entry)")]},
    # Step 4: the reactor's check, then its two rooms (below The Shutdown Record)
    "s4a": {"base": "s3b", "edits": [
        ("replace", FILE, _CORE, _CORE + "- [Try to wake the core](core_wakes) ; check engineering 9 else core_dead, learn lockout\n")]},
    "final": {"base": "s4a", "edits": [
        ("replace", FILE, "### [The Bridge](bridge)", _CORE_ROOMS + "### [The Bridge](bridge)")],
              "same_as": _EX + "/mission.amd"},
    # Scene 6: three slips, each undone
    "b_skill": {"base": "final", "edits": [("replace", FILE, "Skills: medical 4", "Skill: medical 4")]},
    "b_check": {"base": "final", "edits": [("replace", FILE, "check engineering 9 else", "check engineering else")]},
    "b_sience": {"base": "final", "edits": [("replace", FILE, "medical 4, science 3", "medical 4, sience 3")]},
    # PROBE-ONLY, for the game stills (see the docstring). Never shown in the editor.
    "g_flat": {"base": "final", "edits": [
        ("replace", FILE, "Done when: reach derelict 500", "Done when: 60 seconds"),
        ("replace", MAST, "    task_schedule(watch_for_arrival)\n",
         "    boarding_checks_mode(\"flat\")\n    task_schedule(watch_for_arrival)\n")]},
}

_LINT = "sbs lint MyBoarding"
_NS = {"side": False}
_G1 = "Game 1 (state g_flat, consoles server,engineering,science; both beamed down)"
_G2 = "Game 2 (state g_flat, consoles server,engineering; Chief Okoro beamed down alone)"

STILLS = {
    "e_roster0": ("vscode", "start", 92, "big", _NS),       # lines 82 to 102: the crew roster
    "e_k1": ("vscode", "k1", 92, "big", _NS),
    "e_k2": ("vscode", "k2", 92, "big", _NS),
    "e_s3a": ("vscode", "s3a", 134, "big", _NS),             # lines 124 to 144: The Bridge
    "e_s3b": ("vscode", "s3b", 136, "big", _NS),             # the bridge and The Sensor Record
    "e_s4a": ("vscode", "s4a", 122, "big", _NS),             # lines 112 to 132: The Reactor Room
    "e_final_reactor": ("vscode", "final", 128, "mid", _NS),  # lines 114 to 142: the reactor and its two new rooms
    "e_final_roster": ("vscode", "final", 92, "big", _NS),
    "e_bskill": ("vscode", "b_skill", 92, "big", _NS),
    "e_bcheck": ("vscode", "b_check", 122, "big", _NS),
    "e_bsience": ("vscode", "b_sience", 92, "big", _NS),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_bskill": ("terminal", [("final", _LINT), ("b_skill", _LINT)]),
    "t_bcheck": ("terminal", [("b_check", _LINT)]),
    "t_bsience": ("terminal", [("b_sience", _LINT)]),
    # THE REAL GAME (taken 2026-10-15; see the docstring for the two games and the clicks)
    "game_bar_eng": ("game", _G1 + ", step 1: Engineering, the xESS just after BEAM DOWN, Act open on The Airlock. The bar at the top reads 'Chief Okoro' and under it 'engineering' (and the room, if the bar shows one); the airlock line 'The outer door was never sealed...' with Go aft, Go forward and Return to the ship as buttons. No suit tags here: they are Dr Hale's"),
    "game_bridge_sci": ("game", _G1 + ", step 2: Science (Dr Hale), Act, the party on The Bridge: the bridge line ('...locked behind a question you cannot answer yet.') at the foot of the transcript, and the buttons Pull the sensor record and Go back to the airlock (Answer the log is not offered yet)"),
    "game_bridge_eng": ("game", _G1 + ", step 2, the same moment: Engineering (Chief Okoro), Act on The Bridge: the same line, and only Go back to the airlock. No sensor record"),
    "game_reactor_sci": ("game", _G1 + ", step 3: Science (Dr Hale), Act, The Reactor Room: 'Cold. The core was shut down by hand...' and the buttons Try to wake the core and Go back to the airlock (no shutdown record: the chief is aboard)"),
    "game_reactor_eng": ("game", _G1 + ", step 3, the same moment: Engineering (Chief Okoro), Act, The Reactor Room: Read the shutdown record, Try to wake the core, Go back to the airlock"),
    "game_roll_sci": ("game", _G1 + ", step 4: Science after DR HALE pressed Try to wake the core: her name (and face: did not draw, awaiting a re-shoot after the library fix) over the pick, the roll line 'Dr Hale - engineering 0, rolled 5: 5 vs 9, failure.', then The Board Stays Dark's line 'Nothing. Not a flicker...' and Step back"),
    "game_roll_eng": ("game", _G1 + ", step 5: Engineering after Step back and then CHIEF OKORO pressed Try to wake the core: 'Chief Okoro - engineering 4, rolled 5: 9 vs 9, success.', then The Core Turns Over's line 'The board lights for four seconds... MANUAL LOCKOUT, CAPTAIN'S KEY.' and Step back. If it fits, Dr Hale's failed roll a few lines above"),
    "game_roll_both_sci": ("game", _G1 + ", step 5, the same moment on Science: Dr Hale's page with BOTH roll lines (her failure above, the chief's success below), so everyone in the room sees both. If both do not fit on the screen, keep the one with the chief's roll and say so"),
    "game_alone_airlock": ("game", _G2 + ", step 1: Engineering, Act on The Airlock: 'Read the name tags on the suits (covering for medical)' as the LAST button, on a row of its own - the chief covers for the surgeon who stayed home"),
    "game_alone_bridge": ("game", _G2 + ", step 2: Engineering, Act on The Bridge: only Go back to the airlock. With the doctor at home nobody is offered Pull the sensor record - a skill is never covered"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_scale": ("card", "table", {"heading": "Step 1 - Say what each person is good at", "nth": 2, "kicker": "A scale that works well"}),
    "card_kinds": ("card", "table", {"heading": "Step 3 - A choice for someone good enough", "nth": 2, "kicker": "Three kinds of choice"}),
    "card_odds": ("card", "table", {"heading": "Step 4 - A choice anyone may try", "nth": 2, "kicker": "How often a check works"}),
    "card_rules": ("card", "list", {"heading": "Step 5 - Four rules for skills", "kicker": "Four rules"}),
    "card_run": ("card", "points", {"kicker": "In a command prompt in data\\missions",
                                    "items": ["sbs run server,helm,engineering,science -m MyBoarding map=0",
                                              "Fly inside 500 of the hulk. On Engineering and Science: the handheld, Boarding Party, BEAM DOWN"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 5", "sub": "Personal quests"}),
}

# Game stills, 1280x960, marks as fractions of the frame (taken 2026-10-15)
_BAR = ("rect", 0.005, 0.06, 0.2, 0.13)              # game_bar_eng: 'Chief Okoro' / 'engineering'
_BS_REC = ("rect", 0.01, 0.44, 0.203, 0.49)          # game_bridge_sci: Pull the sensor record
_BE_ONE = ("rect", 0.01, 0.44, 0.2, 0.49)            # game_bridge_eng, game_alone_bridge: only Go back
_RE_WAKE = ("rect", 0.24, 0.8, 0.42, 0.845)          # game_reactor_eng: Try to wake the core
_RS_WAKE = ("rect", 0.01, 0.8, 0.192, 0.845)         # game_reactor_sci: Try to wake the core
_RO_HALE = ("rect", 0.01, 0.82, 0.5, 0.89)           # game_roll_sci: her roll line, then the room's line
_RO_HALE0 = ("rect", 0.01, 0.82, 0.36, 0.85)         # ... 'engineering 0'
_RE_OKORO = ("rect", 0.01, 0.795, 0.4, 0.83)         # game_roll_eng / game_roll_both_sci: 'engineering 4 ... success'
_RE_HALE = ("rect", 0.01, 0.39, 0.36, 0.42)          # ... Dr Hale's failed roll above it
_AL_COVER = ("rect", 0.01, 0.315, 0.443, 0.362)      # game_alone_airlock: the covering button, last

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_reactor_eng", "marks": [_RE_WAKE]},
        {"from": 1, "still": "game_roll_sci", "marks": [_RO_HALE]},
        {"from": 2, "still": "game_roll_eng", "marks": [_RE_OKORO]},
        {"from": 3, "still": "game_reactor_eng"},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_say_what_each_person_is_good": {"step": 1, "beats": [
        # the game first: the roster, as the handheld's bar shows it
        {"from": 0, "still": "game_bar_eng"},
        {"from": 1, "still": "game_bar_eng", "marks": [_BAR]},
        {"from": 2, "still": "e_roster0", "marks": [("lines", 86, 98)]},
        {"from": 4, "still": "e_k1", "marks": [("lines", 91, 91)]},
        {"from": 5, "still": "e_k1", "marks": [("text", 91, "engineering 4")]},
        {"from": 6, "still": "e_k1", "marks": [("text", 91, ",")]},
        {"from": 7, "still": "e_k1", "marks": [("text", 91, "engineering 4, science 1")]},
        {"from": 8, "still": "e_k2", "marks": [("text", 99, "medical 4, science 3")]},
        {"from": 9, "still": "e_k2", "marks": [("text", 99, "science 3")]},
        {"from": 10, "still": "e_k2", "marks": [("text", 98, "medical")]},
        {"from": 11, "still": "e_k2", "marks": [("text", 99, "science 3")]},
        {"from": 13, "still": "e_k2", "marks": [("lines", 86, 100)]},
        {"from": 15, "still": "card_scale", "marks": [("part", "r3")]},
        {"from": 16, "still": "e_k2", "marks": [("text", 91, "engineering 4")]},
    ]},
    "s03_a_choice_for_someone_good_en": {"step": 3, "beats": [
        # the game first: the bridge on both handhelds
        {"from": 0, "still": "game_bridge_sci"},
        {"from": 1, "still": "game_bridge_sci", "marks": [_BS_REC]},
        {"from": 1.5, "still": "game_bridge_eng", "marks": [_BE_ONE]},
        {"from": 2, "still": "e_s3a", "marks": [("lines", 134, 134)]},
        {"from": 3, "still": "e_s3a", "marks": [("text", 134, "if skill science >= 3")]},
        {"from": 4, "still": "e_s3a", "marks": [("text", 134, "skill")]},
        {"from": 5, "still": "e_s3b", "marks": [("text", 134, "science >= 3"), ("lines", 137, 140)]},
        {"from": 6, "still": "game_bridge_sci", "marks": [_BS_REC]},
        {"from": 7, "still": "game_bridge_eng", "marks": [_BE_ONE]},
        {"from": 8, "still": "card_kinds"},
        {"from": 9, "still": "card_kinds", "marks": [("part", "r1")]},
        {"from": 10, "still": "game_alone_airlock"},
        {"from": 11, "still": "game_alone_airlock", "marks": [_AL_COVER]},
        {"from": 12, "still": "card_kinds", "marks": [("part", "r2")]},
        {"from": 13, "still": "game_alone_bridge", "marks": [_BE_ONE]},
    ]},
    "s04_a_choice_anyone_may_try": {"step": 4, "beats": [
        # the game first: the reactor on both handhelds
        {"from": 0, "still": "game_reactor_sci"},
        {"from": 1, "still": "game_reactor_sci", "marks": [_RS_WAKE]},
        {"from": 1.5, "still": "game_reactor_eng", "marks": [_RE_WAKE]},
        {"from": 3, "still": "e_s4a", "marks": [("lines", 122, 122)]},
        {"from": 4, "still": "e_s4a", "marks": [("text", 122, "[Try to wake the core](core_wakes)")]},
        {"from": 5, "still": "e_s4a", "marks": [("lines", 122, 122)]},
        {"from": 6, "still": "e_s4a", "marks": [("text", 122, "check engineering")]},
        {"from": 7, "still": "e_s4a", "marks": [("text", 122, "9")]},
        {"from": 8, "still": "e_s4a", "marks": [("text", 122, "check engineering 9")]},
        {"from": 11, "still": "e_final_reactor", "marks": [("text", 122, "else core_dead")]},
        {"from": 12, "still": "e_final_reactor", "marks": [("lines", 135, 138)]},
        {"from": 13, "still": "e_final_reactor", "marks": [("text", 122, ", learn lockout")]},
        {"from": 14, "still": "e_final_reactor", "marks": [("text", 122, ", learn lockout"), ("lines", 130, 133)]},
        {"from": 15, "still": "card_odds", "marks": [("part", "r2c4")]},
        {"from": 16, "still": "card_odds", "marks": [("part", "r2c2")]},
        {"from": 17, "still": "game_roll_sci", "marks": [_RO_HALE]},
        {"from": 18, "still": "game_roll_both_sci", "marks": [_RE_HALE, _RE_OKORO]},
    ]},
    "s05_four_rules": {"step": 5, "beats": [
        {"from": 0, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 4, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_rules", "marks": [("part", "item4")]},
        {"from": 6, "still": "card_rules"},
    ]},
    "s06_lint": {"step": 6, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_bskill", "marks": [("text", 99, "Skill:")]},
        {"from": 1.5, "still": "t_bskill", "marks": [("span", 2, "unknown-field")]},
        {"from": 2, "still": "e_bcheck", "marks": [("text", 122, "check engineering else")]},
        {"from": 3, "still": "t_bcheck", "marks": [("span", 1, "check-shape")]},
        {"from": 4, "still": "e_bsience", "marks": [("text", 99, "sience 3")]},
        {"from": 5, "still": "t_bsience", "marks": [("part", "run1:clean")]},
        {"from": 6, "still": "e_final_roster", "marks": [("lines", 86, 100)]},
    ]},
    "s07_play_it": {"step": 7, "beats": [
        {"from": 0, "still": "card_run", "marks": [("part", "item1")]},
        {"from": 0.5, "still": "game_bridge_sci", "marks": [_BS_REC]},
        {"from": 1, "still": "game_bridge_eng", "marks": [_BE_ONE]},
        {"from": 2, "still": "game_reactor_eng", "marks": [_RE_WAKE]},
        {"from": 3, "still": "game_roll_sci"},
        {"from": 4, "still": "game_roll_sci", "marks": [_RO_HALE0]},
        {"from": 5, "still": "game_roll_eng"},
        {"from": 6, "still": "game_roll_eng", "marks": [_RE_OKORO]},
        {"from": 8, "still": "e_final_roster", "marks": [("text", 91, "Skills:")]},
        {"from": 10, "still": "t_bskill", "marks": [("span", 2, "unknown-field")]},
        {"from": 11, "still": "game_bar_eng"},
        {"from": 12, "still": "game_bar_eng", "marks": [_BAR]},
        {"from": 13, "still": "game_roll_both_sci", "marks": [_RE_HALE, _RE_OKORO]},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 5, "still": "card_next"},
    ]},
}
