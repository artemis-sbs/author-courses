"""Storyboard for c3-03-everyone-gets-a-menu: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 2's finished files ("start": the template with c3-02's
example laid over it). Only mission.amd changes: the medic's reading and its room ("m1",
"m2"), the engineer's reading and its room ("m3", "m4"), the log and the last room ("m5",
"m6"), and the bridge's two conditional lines ("final", the page's own example\\mission.amd).

GAME STILLS. Not taken yet; no marks until the screenshots exist. THREE windows, and no
Helm: state g_wait is PROBE-ONLY (never shown in the editor), Close Inspection's
`Done when: reach derelict 500` replaced by `Done when: 90 seconds`, so the party forms
90 seconds into the game with nobody flying (90, not 10: the consoles must be seated when
the visit opens, or nobody is offered a covering choice - a known library defect). The
rooms, the roster and the card are the page's. The visit is played on the HANDHELDS:
BEAM DOWN turns a console into the xESS (a bar with name, job and room over the Act app:
the room's line, kept as a running page, with the choices as buttons).

GAME A: `python game.py c3-03-everyone-gets-a-menu start --state g_wait --consoles server,engineering,science`
  1. Wait for 'Quest complete: Close Inspection' (90 s). On Engineering, the handheld icon,
     Boarding Party, BEAM DOWN. Then the same on Science.
  2. game_l3_sci_airlock (Science) and game_l3_eng_airlock (Engineering), before any press.
  3. Engineering: Go forward, to the bridge: game_l3_bridge_early (Engineering).
  4. Go back to the airlock. Science: Read the name tags on the suits: game_l3_suits
     (Science). Step back.
  5. Go aft, toward the reactor: game_l3_eng_reactor (Engineering), game_l3_sci_reactor
     (Science).
  6. Engineering: Read the shutdown record: game_l3_shutdown (Engineering). Step back, Go
     back to the airlock, Go forward, to the bridge: game_l3_bridge_late (Engineering).
  7. Answer the log: game_l3_last (Engineering).
GAME B: stop, then start again the same way. Engineering ONLY beams down; Science stays at
its own Science screen. game_l3_eng_alone (Engineering, the airlock).
"""
LECTURE = "c3-03-everyone-gets-a-menu"
TITLE = ("Class 3, Lecture 3", "Everyone gets a menu", "One word and one semicolon")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-03-everyone-gets-a-menu/example"
_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hulk"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hulk")]
_AFT = "- [Go aft, toward the reactor](reactor)\n"
_TAGS = "- [Read the name tags on the suits](suits) if medical ; learn suits\n"
_SUITS = ("### [Six Suits](suits)\n"
          "% Six suits, six names, and every one of them is here. Nobody left this ship through the airlock.\n\n"
          "- [Step back](airlock)\n\n")
_HAD_TIME = "someone who had time.\n\n"
_BACK = "- [Go back to the airlock](airlock)\n"
_RECORD = "- [Read the shutdown record](shutdown) if engineering ; learn shutdown\n"
_SHUTDOWN = ("### [The Shutdown Record](shutdown)\n"
             "% Shut down from this room, and then the restart key was taken out and carried away. "
             "Whoever did it did not mean for her to wake up.\n\n"
             "- [Step back](reactor)\n\n")
_WORD = "a single word.\n\n"
_LOG = "- [Answer the log](last_entry) if learned >= 2\n"
_LAST = ("\n### [The Last Entry](last_entry)\n"
         "% Six aboard. Core cold. Key over the side. The last entry is one word: QUARANTINE.\n\n"
         "- [Return to the ship]()\n")
_LINE0 = ("% Every station is dark but one. The log is open on the captain's chair, "
          "and the last entry is a single word.\n")
_LINES = ("%{learned < 2} Every station is dark but one. The log is open on the captain's chair, "
          "locked behind a question you cannot answer yet.\n"
          "%{learned >= 2} Every station is dark but one. The log is open on the captain's chair, "
          "and now you know what it is going to ask.\n")

STATES = {
    # Lecture 2's finished files
    "start": {"folder": "c1-03-editor-and-first-run/example", "over": ("c3-02-party-and-place/example",),
              "edits": _TITLED},
    # Step 1: the medic's reading, then its room
    "m1": {"base": "start", "edits": [("replace", FILE, _AFT, _TAGS + _AFT)]},
    "m2": {"base": "m1", "edits": [("replace", FILE, "- [Return to the ship]()\n\n### [The Reactor Room]",
                                    "- [Return to the ship]()\n\n" + _SUITS + "### [The Reactor Room]")]},
    # Step 2: the engineer's reading, then its room
    "m3": {"base": "m2", "edits": [("replace", FILE, _HAD_TIME + _BACK, _HAD_TIME + _RECORD + _BACK)]},
    "m4": {"base": "m3", "edits": [("replace", FILE, _RECORD + _BACK + "\n### [The Bridge]",
                                    _RECORD + _BACK + "\n" + _SHUTDOWN + "### [The Bridge]")]},
    # Step 3: the log, then the last room at the end of the file
    "m5": {"base": "m4", "edits": [("replace", FILE, _WORD + _BACK, _WORD + _LOG + _BACK)]},
    "m6": {"base": "m5", "edits": [("append", FILE, _LAST)]},
    # Step 4: the line that changes. The page's own file.
    "final": {"base": "m6", "edits": [("replace", FILE, _LINE0, _LINES)], "same_as": _EX + "/mission.amd"},
    # Step 6: two slips lint catches, and one it does not
    "b_lern": {"base": "final", "edits": [("replace", FILE, "; learn suits", "; lern suits")]},
    "b_sign": {"base": "final", "edits": [("replace", FILE, "if learned >= 2\n", "if learned => 2\n")]},
    "b_medcal": {"base": "final", "edits": [("replace", FILE, "if medical ;", "if medcal ;")]},
    # PROBE-ONLY, for the game stills: the party forms 90 s in, with nobody flying. Never shown in the editor.
    "g_wait": {"base": "final", "edits": [
        ("replace", FILE, "Done when: reach derelict 500", "Done when: 90 seconds")]},
}

_LINT = "sbs lint MyBoarding"
_NS = {"side": False}

STILLS = {
    "e_roster": ("vscode", "start", 88, "big", _NS),      # lines 78 to 98: the roster, both Roles lines
    "e_m1": ("vscode", "m1", 108, "big", _NS),
    "e_m2": ("vscode", "m2", 108, "big", _NS),            # the airlock, Six Suits, the reactor room
    "e_m3": ("vscode", "m3", 120, "big", _NS),            # lines 110 to 130: the reactor room
    "e_m4": ("vscode", "m4", 120, "big", _NS),
    "e_m4b": ("vscode", "m4", 127, "big", _NS),           # lines 117 to 137: the bridge before the lock
    "e_m5": ("vscode", "m5", 127, "big", _NS),
    "e_m6": ("vscode", "m6", 127, "big", _NS),
    "e_final": ("vscode", "final", 127, "big", _NS),
    "e_medcal": ("vscode", "b_medcal", 108, "big", _NS),
    "t_final": ("terminal", [("final", _LINT)]),
    "t_lern": ("terminal", [("b_lern", _LINT)]),
    "t_sign": ("terminal", [("b_sign", _LINT)]),
    "t_medcal": ("terminal", [("b_medcal", _LINT)]),
    # THE REAL GAME (not taken yet). State g_wait, consoles server,engineering,science (see the docstring)
    "game_l3_sci_airlock": ("game", "GAME A, Science (Dr Hale), both consoles just beamed down: the handheld's bar Dr Hale, medical, The Airlock; the airlock's line; FOUR buttons, the first 'Read the name tags on the suits', then Go aft, Go forward, Return to the ship"),
    "game_l3_eng_airlock": ("game", "GAME A, Engineering (Chief Okoro), the same moment: the bar Chief Okoro, engineering, The Airlock; the same line; THREE buttons, no name tags"),
    "game_l3_bridge_early": ("game", "GAME A, Engineering, Go forward, to the bridge pressed before any reading: the bar The Bridge; the line '...locked behind a question you cannot answer yet.'; one button, Go back to the airlock, no Answer the log"),
    "game_l3_suits": ("game", "GAME A, Science, back in the airlock, 'Read the name tags on the suits' pressed: Dr Hale and her choice on the page, then Six Suits' line and its one button, Step back"),
    "game_l3_eng_reactor": ("game", "GAME A, Engineering, Go aft, toward the reactor pressed: the bar The Reactor Room; its line; two buttons, 'Read the shutdown record' and Go back to the airlock"),
    "game_l3_sci_reactor": ("game", "GAME A, Science, the same moment: the reactor room's line and ONE button, Go back to the airlock"),
    "game_l3_shutdown": ("game", "GAME A, Engineering, 'Read the shutdown record' pressed: Chief Okoro and his choice on the page, then The Shutdown Record's line and Step back"),
    "game_l3_bridge_late": ("game", "GAME A, Engineering, at the bridge again after both readings: the line '...and now you know what it is going to ask.' and two buttons, Answer the log and Go back to the airlock"),
    "game_l3_last": ("game", "GAME A, Engineering, Answer the log pressed: The Last Entry's line ('...The last entry is one word: QUARANTINE.') and one button, Return to the ship"),
    "game_l3_eng_alone": ("game", "GAME B, Engineering the only console down (Science left at its own screen): the airlock with FOUR buttons, the first 'Read the name tags on the suits (covering for medical)'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_rules": ("card", "list", {"heading": "Step 5 - Three rules for a menu", "kicker": "Three rules for a menu"}),
    "card_cannot": ("card", "table", {"heading": "Step 6 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (1, 2)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "A reading for your third person"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 4", "sub": "Crew and skills"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l3_sci_airlock"},
        {"from": 2, "still": "game_l3_eng_airlock"},
        {"from": 3, "still": "game_l3_bridge_early"},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_a_choice_for_one_job": {"step": 1, "beats": [
        # the game first: two menus in one room
        {"from": 0, "still": "game_l3_sci_airlock"},
        {"from": 3, "still": "game_l3_eng_airlock"},
        {"from": 4, "still": "e_m1", "marks": [("lines", 106, 106)]},
        {"from": 5, "still": "e_m1", "marks": [("text", 106, "if medical ; learn suits")]},
        {"from": 6, "still": "e_m1", "marks": [("text", 106, "if medical")]},
        {"from": 8, "still": "e_roster", "marks": [("lines", 97, 97)]},
        {"from": 9, "still": "e_roster", "marks": [("lines", 93, 97)]},
        {"from": 10, "still": "e_m1", "marks": [("text", 106, ";")]},
        {"from": 11, "still": "e_m1", "marks": [("text", 106, "learn suits")]},
        {"from": 13, "still": "e_m1", "marks": [("text", 106, "(suits)")]},
        {"from": 14, "still": "e_m2", "marks": [("lines", 111, 114)]},
        {"from": 15, "still": "e_m2", "marks": [("lines", 114, 114)]},
        {"from": 16, "still": "game_l3_suits"},
    ]},
    "s03_the_other_job": {"step": 2, "beats": [
        # the game first: the reactor room, two handhelds
        {"from": 0, "still": "game_l3_eng_reactor"},
        {"from": 1.6, "still": "game_l3_sci_reactor"},
        {"from": 2, "still": "e_m3", "marks": [("lines", 119, 119)]},
        {"from": 3, "still": "e_m3", "marks": [("text", 119, "learn shutdown")]},
        {"from": 4, "still": "e_m4", "marks": [("lines", 122, 125)]},
        {"from": 5, "still": "game_l3_shutdown"},
        {"from": 6, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 7, "still": "e_m4", "marks": [("lines", 119, 119), ("lines", 122, 125)]},
    ]},
    "s04_a_door_that_opens_when_they_": {"step": 3, "beats": [
        # the game first: the lock, open
        {"from": 0, "still": "game_l3_bridge_late"},
        {"from": 2, "still": "e_m4b", "marks": [("lines", 127, 130)]},
        {"from": 2.6, "still": "e_m5", "marks": [("lines", 130, 130)]},
        {"from": 3, "still": "e_m5", "marks": [("text", 130, "if learned >= 2")]},
        {"from": 4, "still": "e_m5", "marks": [("text", 130, "learned")]},
        {"from": 8, "still": "e_m5", "marks": [("lines", 130, 130)]},
        {"from": 10, "still": "e_m6", "marks": [("lines", 133, 136)]},
        {"from": 11, "still": "e_m6", "marks": [("lines", 136, 136)]},
    ]},
    "s05_a_line_that_changes": {"step": 4, "beats": [
        # the game first: the same room, early and late
        {"from": 0, "still": "game_l3_bridge_early"},
        {"from": 5, "still": "game_l3_bridge_late"},
        {"from": 6, "still": "e_final", "marks": [("lines", 128, 129)]},
        {"from": 7, "still": "e_final", "marks": [("text", 128, "{learned < 2}"), ("text", 129, "{learned >= 2}")]},
        {"from": 8, "still": "e_final", "marks": [("lines", 128, 128)]},
    ]},
    "s06_three_rules_and_lint": {"step": 5, "beats": [
        {"from": 0, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 1, "still": "e_final", "marks": [("lines", 132, 132)]},
        {"from": 2, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_rules", "marks": [("part", "item3")]},
        {"from": 4, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 5, "still": "t_lern"},
        {"from": 6, "still": "t_sign"},
        {"from": 7, "still": "e_medcal", "marks": [("text", 106, "medcal")]},
        {"from": 8, "still": "t_medcal", "marks": [("part", "run1:clean")]},
        {"from": 9, "still": "card_cannot", "marks": [("part", "r1")]},
        {"from": 10, "still": "e_final", "marks": [("text", 131, "learned")]},
        {"from": 11, "still": "e_roster", "marks": [("lines", 90, 90), ("lines", 97, 97)]},
    ]},
    "s07_play_it": {"step": 7, "beats": [
        {"from": 0, "still": "game_l3_sci_airlock"},
        {"from": 1, "still": "game_l3_bridge_early"},
        {"from": 3, "still": "game_l3_suits"},
        {"from": 4, "still": "game_l3_shutdown"},
        {"from": 5, "still": "game_l3_bridge_late"},
        {"from": 6, "still": "game_l3_eng_alone"},
        {"from": 9, "still": "game_l3_last"},
        {"from": 10, "still": "e_roster", "marks": [("lines", 90, 90), ("lines", 97, 97)]},
        {"from": 12, "still": "card_cannot", "marks": [("part", "r1")]},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_next"},
    ]},
}
