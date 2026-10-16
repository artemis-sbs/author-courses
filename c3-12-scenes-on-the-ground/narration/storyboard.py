"""Storyboard for c3-12-scenes-on-the-ground: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

The lecture starts from Lecture 11's finished files in MyAway ("start": Lecture 7's
starter with the example\\ folders of Lectures 8 to 11 laid over it). Only mission.amd
changes: a quest, a person and a prop are added, two scenes are rewritten and two of the
starter's get a line ("r1" .. "r6", then "final", the page's own example\\mission.amd).

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders): the example\\ folders laid over the starter bring the latest of each
ground file, from Lectures 9 to 11. The close views of the text hide the Side Bar, as every
close view of this class does.

GAME STILLS. Taken 2026-10-16 (all 16 kept), library 7ea2c918, marks set from them. State
"final" as the page has it, started with
`python game.py c3-12-scenes-on-the-ground start --consoles server,engineering,weapons`
(the probe is made from the `away` template, every file of the state laid over it, ground\\
included; GAME_RESULTS_SAVE is false). THREE windows: the server, Engineering (Chief Okoro) and
Weapons (Lt Sam Reyes, `security` on his bar). The ship starts beside the relay, so the party
is offered at once: on each console the handheld icon (top left), the Boarding Party tile, BEAM
DOWN. The console becomes the xESS: the map, and beside it the device (tiles Crew, Act, Look,
Pack, Tasks, Beam, Scan, Fire). A click on a prop or a person walks there and uses it; Look
lists the same things as buttons, and Go to <area>. The bar's third slot reads the AREA title
(`Kesh Relay`, `The Dry Gully`) in these stills; no caption here talks about that slot.
What they showed: the "brass key" is the Pump house key, a small blue key by the tent's foot
(no peg); Act logs `Chief Okoro picked up pump key from the Pump house key.`. Faces are random
per game, and `pim` (gully) and `pim_yard` (by the tent) have two different faces: no caption
claims a face. Roll lines wrap to three lines (cosmetic). The squashed xESS home after Back
(library defect, R:\\cosmos\\courses\\c3_12\\game\\defect_home_squash.png) is in no beat.

GAME ONE, the long road (about 28 minutes). Press order, as played:
  1. Weapons (Reyes): Fire, FULL, Arm, click the sentry (it walks the 18..25 loop east of the
     yard). ONE FULL shot put it down, clicking the cell it had just ENTERED on its west leg
     (18, 9 / 18, 10) from beside the tent; a shot at where it is now usually misses, and no
     app says hit or miss. It drops a power cell; leave it.
  2. Engineering (Okoro): the terminal beside the relay door, Force the service port (a
     roll; on Dead Screen, Look, Use Yard terminal again), Copy it down. The terminal re-opens
     at once: game_l12_terminal_update. Step back.
  3. Okoro: pick up the Pump house key (14, 4, the small blue key by the foot of the tent).
     Reyes: talk to Old Marrow (by the tent): game_l12_marrow_key. Leave him to his kettle.
  4. Okoro: to The Dry Gully by the trail sign, then the exit. NOT Look's first row: with the
     relay door and terminal in reach Look lists Use Relay door, Use Yard terminal first (a
     press there rolls at the door). Pick up the Toolbox (two fuses). Use the Brittle notice
     beside the pump house door; Let the pieces fall.
  5. Okoro: talk to Pim (lower left): game_l12_pim_notice. Ask if she has anything for a
     fight; on Under the Rock, Okoro's map shows the kit by the rock (4, 9): game_l12_stash.
     Ask her something else, Ask what stopped her: game_l12_promise. Promise to bring it back.
  6. Reyes: Crew, Beam up. On Weapons, the handheld icon, Quests (0.15, 0.55), Pim's Tablet
     (0.12, 0.24): game_l12_log_tablet. Reyes stays aboard from here.
  7. Okoro: the pump house door (the key opens it), the pump panel inside (a click at 0.642,
     0.5 walks him in): game_l12_panel_two. Leave it alone.
  8. Okoro: the stairs in the pump house (Go to The Cistern). From the foot, Fire, FULL, Arm,
     click the crawler on the walkway as it enters 12, 1 / 13, 1: one shot. Pick up the drop
     (`Chief Okoro picked up tablet.`). Go to The Dry Gully.
  9. Okoro: talk to Pim: game_l12_pim_give. Give her the tablet: game_l12_thanks. Watch
     her go (she leaves the gully at once).
 10. Okoro: the pump panel: game_l12_panel_three. Fit three fuses and throw the lever;
     Step back. Go to The Cistern, through the open sluice, pick up the spare cell.
 11. Okoro: Go to Kesh Relay. Look, on Okoro's map of the yard, Pim by the tent (11, 4, beside
     Marrow at 12, 5): game_l12_pim_yard. Talk to her: game_l12_pim_home. Ask her to open the
     relay house; Thank her. (Look's `! The beacon` row walks him through the door to it.)
 12. Okoro: the beacon: game_l12_beacon. Fit the power cell, Call it in. The server's last
     screen: game_l12_won.
GAME TWO, the loss (about three minutes): server, engineering. Okoro only: the key, the path
behind the house to the gully, the pump house door, the pump panel (no fuses: only Jam a
crowbar and Leave it alone), Jam a crowbar across all three clips, Run. The server's last
screen: game_l12_lost.
"""
import os as _os

LECTURE = "c3-12-scenes-on-the-ground"
TITLE = ("Class 3, Lecture 12", "Scenes on the ground", "Holding, party, and the words that move things")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_COURSES = _os.path.dirname(_HERE)


def _read(*parts):
    with open(_os.path.join(_COURSES, *parts), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_FINAL = _read(LECTURE, "example", "mission.amd")


def _cut(a, b):
    """The page's own block: the text of the finished file from a up to (not including) b."""
    i = _FINAL.index(a)
    return _FINAL[i:_FINAL.index(b, i)]


_TABLET = _cut("// A quest that waits.", "\n// ---- Side stories")
_STASH = _cut("// Hidden until a scene shows it", "\n// ---- People")
_PIM_YARD = _cut("// Pim again, by the tent.", "\n// ---- Hostiles")
_PIM_OLD = ("### [Pim](pim)\n% \"You are from the ship.\" She does not get up. \"I came out here to start the pump, nine "
            "days ago. I got as far as the door.\"\n\n- [Ask what stopped her](pim_why)\n- [Leave her be]()\n\n"
            "### [What Stopped Her](pim_why)\n% \"There is something on the walkway down there. It took my tablet out "
            "of my hand and I ran. I have been working up to going back for it ever since.\"\n\n"
            "- [Ask her something else](pim)\n- [Leave her be]()\n")
_PIM_NEW = _FINAL[_FINAL.index("### [Pim](pim)\n%"):]
_PUMP_OLD = ("### [The Pump Panel](pump_panel)\n% The dial sits at zero. The lever is stiff, and it moves.\n\n"
             "- [Throw the lever](pump_run) ; signal cistern_drained\n- [Leave it alone]()\n\n"
             "### [The Pump Runs](pump_run)\n% The pump coughs, catches, and settles to a hammering you can feel "
             "through the floor. Somewhere under your feet, a great deal of water starts to move.\n\n- [Step back]()\n")
_PUMP_NEW = _cut("### [The Pump Panel](pump_panel)", "\n\n// ---- Lecture 11: somebody to talk to.")
_SENT = "- [Send the door code](terminal_sent) if learned codes ; signal relay_unlocked\n"
_UPDATE = "- [Send the sentry its recognition update](terminal_update) if learned codes ; calm sentry\n"
_UPDATE_ROOM = _cut("### [Recognition Update](terminal_update)", "### [Nine Days](terminal_log)")
_CACHE = "- [Ask what he has put by](marrow_cache) ; signal cache_known\n"
_SHOW = "- [Show him the brass key](marrow_pump) if party pump_key\n"
_KEY_ROOM = _cut("### [The Brass Key](marrow_pump)", "### [The Keycard](marrow_key)")
_EX = LECTURE + "/example"

STATES = {
    # Lecture 11's finished files: where this lecture starts
    "start": {"folder": "c3-07-anatomy-of-a-long-away-mission/example",
              "over": ("c3-09-tile-map-editor-part-2/example", "c3-10-props/example",
                       "c3-11-people-and-hostiles/example")},
    # Step 1: a quest that waits
    "r1": {"base": "start", "edits": [("replace", FILE, "transporter lock.\n\n", "transporter lock.\n\n" + _TABLET)]},
    # Step 2: Pim, by the tent
    "r2": {"base": "r1", "edits": [("replace", FILE, "with her back to a rock.\n\n",
                                    "with her back to a rock.\n\n" + _PIM_YARD)]},
    # Step 3: a stash
    "r3": {"base": "r2", "edits": [("replace", FILE, "The needle reads FULL.\n\n", "The needle reads FULL.\n\n" + _STASH)]},
    # Step 4: Pim's two rooms become eight
    "r4": {"base": "r3", "edits": [("replace", FILE, _PIM_OLD, _PIM_NEW)]},
    # Step 5: the pump, with fuses
    "r5": {"base": "r4", "edits": [("replace", FILE, _PUMP_OLD, _PUMP_NEW)]},
    # Step 6: the sentry stands down
    "r6": {"base": "r5", "edits": [("replace", FILE, _SENT, _SENT + _UPDATE),
                                    ("replace", FILE, "### [Nine Days](terminal_log)",
                                     _UPDATE_ROOM + "### [Nine Days](terminal_log)")]},
    # Step 7: what the party carries. The page's own file.
    "final": {"base": "r6", "edits": [("replace", FILE, _CACHE, _CACHE + _SHOW),
                                       ("replace", FILE, "### [The Keycard](marrow_key)",
                                        _KEY_ROOM + "### [The Keycard](marrow_key)")],
              "same_as": _EX + "/mission.amd"},
    # Step 9: discover, tried and given back
    "b_discover": {"base": "final", "edits": [("replace", FILE, "](pim_spare) if learned spare\n",
                                               "](pim_spare) if learned spare ; discover cistern\n")]},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}

STILLS = {
    # Step 1: the quest
    "e_q0": ("vscode", "start", 88, "big", _NS),           # lines 78 to 98: the end of Hold at the Relay
    "e_tab": ("vscode", "r1", 100, "big", _NS),            # lines 90 to 110: Pim's Tablet, 95 to 105
    "t_r1": ("terminal", [("r1", _LINT)]),
    # Steps 2 and 3: the two hidden records
    "e_yard": ("vscode", "r2", 376, "big", _NS),           # lines 366 to 386: the second Pim, 370 to 382
    "e_stash": ("vscode", "r3", 343, "big", _NS),          # lines 333 to 353: the gauge, then the stash, 339 to 348
    # Step 4: Pim's scene
    "e_pim0": ("vscode", "r3", 561, "big", _NS),           # lines 551 to 571: her two rooms as Lecture 11 left them
    "e_r4a": ("vscode", "r4", 563, "big", _NS),            # lines 553 to 573: Pim (556 to 564), What Stopped Her (566 to 571)
    "e_r4b": ("vscode", "r4", 594, "big", _NS),            # lines 584 to 604: Nine Days of Readings to The Remote
    # Step 5: the pump
    "e_pump0": ("vscode", "r4", 546, "big", _NS),          # lines 536 to 556: the pump's two rooms, before
    "e_r5": ("vscode", "r5", 554, "mid", _NS),             # about lines 540 to 568: the four rooms, 543 to 565
    # Step 6: the terminal
    "e_term0": ("vscode", "r5", 455, "big", _NS),          # lines 445 to 465: The Yard Terminal, before
    "e_r6": ("vscode", "r6", 456, "big", _NS),             # the new answer (456) and its room (459 to 462)
    # Step 7: Marrow
    "e_marrow": ("vscode", "final", 491, "big", _NS),      # lines 481 to 501: Old Marrow (484), the new answer (490), The Brass Key (494 to 498)
    # Step 8: the endings
    "e_relight": ("vscode", "final", 75, "big", _NS),      # lines 65 to 85: Relight Kesh Relay, Win and Lose (75, 76)
    "e_burn": ("vscode", "final", 572, "big", _NS),        # lines 562 to 582: Fire in the Pump House, Run (578)
    "e_beacon": ("vscode", "final", 532, "big", _NS),      # lines 522 to 542: The Beacon (526), Fit the power cell (529)
    # Step 9: discover, tried
    "e_discover": ("vscode", "b_discover", 586, "big", _NS),
    "t_discover": ("terminal", [("b_discover", _LINT)]),
    # THE REAL GAME (not taken yet). State final, three windows: server, Engineering (Chief
    # Okoro), Weapons (Lt Reyes). Press order in the docstring.
    "game_l12_terminal_update": ("game", "Engineering's xESS, Act, the Yard Terminal again after Copy it down (game one, press 2): the DOOR SEALED line with 'now you have one to give it', and among the buttons Send the door code and, under it, Send the sentry its recognition update"),
    "game_l12_marrow_key": ("game", "Weapons' xESS (Lt Reyes), Act, talking to Old Marrow while Chief Okoro carries the brass key (game one, press 3): Marrow's line, and Show him the brass key among the buttons (with Look at that cough marked as covering for medical)"),
    "game_l12_pim_notice": ("game", "Engineering's xESS, Act, talking to Pim in the gully after the Brittle notice was read (game one, press 5): her line, then Ask what stopped her, Ask about the spare cell, Ask if she has anything for a fight, Leave her be (no tablet buttons)"),
    "game_l12_stash": ("game", "Engineering's map of The Dry Gully just after Ask if she has anything for a fight: the medical crate now drawn by the rock beside Pim (cell 4, 9), the device on Under the Rock"),
    "game_l12_promise": ("game", "Engineering's xESS, Act, What Stopped Her: her line about the walkway, then Promise to bring it back, Ask her something else, Leave her be"),
    "game_l12_log_tablet": ("game", "Weapons, beamed back up (Crew, Beam up), its ePADD Quest Log with Pim's Tablet selected after the promise (game one, press 6): State Active, Reward 100 credits, 'Bring Pim her survey tablet', and the two paragraphs, the second about who Pim is"),
    "game_l12_panel_two": ("game", "Engineering's xESS, Act, the pump panel with two fuses in Okoro's pack (game one, press 7): 'Three fuse clips, all empty. The lever will not do anything until they are full.', then Fit two, and bridge the third clip with wire, Jam a crowbar across all three clips, Leave it alone"),
    "game_l12_pim_give": ("game", "Engineering's xESS, Act, talking to Pim with the tablet in Okoro's pack (game one, press 9): Give her the tablet and Tell her the tablet is yours now among the buttons"),
    "game_l12_thanks": ("game", "Engineering's xESS after Give her the tablet: Nine Days of Readings, her line about the fuse from her lamp, and the one button Watch her go"),
    "game_l12_panel_three": ("game", "Engineering's xESS, Act, the pump panel with three fuses in the pack (game one, press 10): the line '...and three fuses between you', and Fit three fuses and throw the lever as the first button"),
    "game_l12_pim_yard": ("game", "Engineering's map of the yard (Kesh Relay) after Watch her go (game one, press 11): Pim's figure standing beside the tent"),
    "game_l12_pim_home": ("game", "Engineering's xESS, Act, talking to Pim by the tent: Pim, at Home, her line about the remote, and Ask her to open the relay house, Leave her to her tea"),
    "game_l12_beacon": ("game", "Engineering's xESS, Act, the beacon in the relay house with the spare cell in Okoro's pack (game one, press 12): the beacon's line, then Fit the power cell, Bring it up by hand on the standby coil, Pull the governor and run it wide open, Leave it dark for now"),
    "game_l12_won": ("game", "The server's last screen after Call it in (game one): Game results, and the starter's Win sentence 'The beacon is lit. Every convoy on the Kesh run has its way home again.'"),
    "game_l12_lost": ("game", "The server's last screen after the crowbar and Run (game two): Game results, and the starter's Lose sentence 'The beacon is slag. The Kesh run stays dark, and the convoys must find another road.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_conditions": ("card", "table", {"heading": "The words, all of them", "kicker": "Conditions: who is offered it"}),
    "card_outcomes": ("card", "table", {"heading": "The words, all of them", "nth": 2, "kicker": "Outcomes: what it does"}),
    # Step 11's eleven steps, cut down to the script's turns (the page's own list is too long for one card)
    "card_route": ("card", "points", {"kicker": "The long way round (Step 11)", "items": [
        "Reyes: **Fire**, **FULL**, **Arm**, click the sentry. One shot drops it. Expect to miss",
        "Okoro picks up the pump house key. Reyes shows Marrow the key",
        "The gully: the toolbox, the notice, Pim's promise. Reyes beams up",
        "The pump panel with two fuses: neither the wire nor the crowbar",
        "From the foot of the stairs, **FULL** on the crawler. The tablet",
        "**Give her the tablet**: a fuse. She goes home",
        "**Fit three fuses and throw the lever**. The spare cell",
        "Pim, by the tent, opens the relay house. **Fit the power cell**"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 13", "sub": "What the crew sees"}),
}

# Marks on the game stills (fractions of the 1280x960 console window; the device column is x 0.67..0.98)
_GV_GIVE = ("rect", 0.67, 0.765, 0.845, 0.82)        # game_l12_pim_give: Give her the tablet
_GV_TWO = ("rect", 0.67, 0.765, 0.935, 0.875)        # ... Give her the tablet, Tell her the tablet is yours now
_GV_GOT = ("rect", 0.67, 0.3, 0.945, 0.365)          # ... Chief Okoro picked up tablet.
_P2_LINE = ("rect", 0.67, 0.625, 0.97, 0.72)         # game_l12_panel_two: Three fuse clips, all empty...
_P2_OFFER = ("rect", 0.67, 0.74, 0.965, 0.875)       # ... the wire and the crowbar
_P2_BAR = ("rect", 0.67, 0.825, 0.965, 0.875)        # ... Jam a crowbar across all three clips
_P3_LINE = ("rect", 0.67, 0.455, 0.97, 0.51)         # game_l12_panel_three: ...and three fuses between you
_P3_FIT = ("rect", 0.67, 0.565, 0.96, 0.615)         # ... Fit three fuses and throw the lever, first
_LOST = ("rect", 0.015, 0.215, 0.265, 0.315)         # game_l12_lost: the starter's Lose sentence
_WON = ("rect", 0.015, 0.215, 0.25, 0.315)           # game_l12_won: the starter's Win sentence
_LT_ROW = ("rect", 0.004, 0.217, 0.38, 0.285)        # game_l12_log_tablet: Pim's Tablet, Active
_LT_PAGE = ("rect", 0.383, 0.075, 0.96, 0.31)        # ... State, Reward 100 credits, objective, two paragraphs
_PY_PIM = ("rect", 0.075, 0.305, 0.118, 0.375)       # game_l12_pim_yard: Pim beside the tent (11, 4)
_ST_KIT = ("rect", 0.155, 0.64, 0.195, 0.69)         # game_l12_stash: the medical crate by the rock (4, 9)
_PN_LINE = ("rect", 0.67, 0.455, 0.97, 0.61)         # game_l12_pim_notice: Pim's line
_PN_READ = ("rect", 0.67, 0.24, 0.835, 0.29)         # ... Let the pieces fall: the notice was read
_PN_SPARE = ("rect", 0.67, 0.683, 0.88, 0.73)        # ... Ask about the spare cell
_TU_SEALED = ("rect", 0.67, 0.565, 0.965, 0.66)      # game_l12_terminal_update: DOOR SEALED ... one to give it
_TU_COPY = ("rect", 0.67, 0.498, 0.8, 0.543)         # ... Copy it down
_TU_NEW = ("rect", 0.67, 0.785, 0.967, 0.89)         # ... Send the door code, and under it the sentry's update
_MK_SHOW = ("rect", 0.67, 0.552, 0.875, 0.6)         # game_l12_marrow_key: Show him the brass key
_MK_WHO = ("rect", 0.668, 0.06, 0.79, 0.13)          # ... Lt Sam Reyes, the one talking
_MK_OKORO = ("rect", 0.31, 0.355, 0.35, 0.42)        # ... Okoro (gold suit), who carries the key
_PR_PROMISE = ("rect", 0.67, 0.79, 0.88, 0.84)       # game_l12_promise: Promise to bring it back
_BC_FIT = ("rect", 0.67, 0.59, 0.97, 0.82)           # game_l12_beacon: the beacon's line and Fit the power cell
_PH_OPEN = ("rect", 0.67, 0.74, 0.935, 0.787)        # game_l12_pim_home: Ask her to open the relay house

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l12_pim_give", "marks": [_GV_GIVE]},
        {"from": 3, "still": "game_l12_panel_two", "marks": [_P2_LINE]},
        {"from": 4, "still": "game_l12_panel_two", "marks": [_P2_BAR]},
        {"from": 4.5, "still": "game_l12_lost", "marks": [_LOST]},
        {"from": 5, "still": "card_title"},
    ]},
    "s02_the_words": {"step": None, "beats": [
        {"from": 0, "still": "card_conditions"},
        {"from": 2, "still": "card_conditions", "marks": [("part", "r5"), ("part", "r6")]},
        {"from": 3, "still": "card_conditions", "marks": [("part", "r5")]},
        {"from": 4, "still": "card_conditions", "marks": [("part", "r6")]},
        {"from": 5, "still": "card_outcomes"},
        {"from": 6, "still": "card_outcomes", "marks": [("part", "r5"), ("part", "r6")]},
        {"from": 7, "still": "card_outcomes", "marks": [("part", "r7"), ("part", "r8")]},
        {"from": 8, "still": "card_outcomes", "marks": [("part", "r9"), ("part", "r10"), ("part", "r11"), ("part", "r12")]},
    ]},
    "s03_a_quest_that_waits_and_two_h": {"step": 1, "beats": [
        # the game first: the quest in the Quest Log
        {"from": 0, "still": "game_l12_log_tablet", "marks": [_LT_ROW]},
        {"from": 3, "still": "game_l12_log_tablet", "marks": [_LT_PAGE]},
        {"from": 4, "still": "e_tab", "marks": [("lines", 98, 98)]},
        {"from": 6, "still": "e_tab", "marks": [("lines", 105, 105)]},
        {"from": 8, "still": "t_r1", "marks": [("span", 1, "never-revealed")]},
        # the game first: Pim by the tent
        {"from": 10, "still": "game_l12_pim_yard", "marks": [_PY_PIM]},
        {"from": 13, "still": "e_yard", "marks": [("lines", 372, 382)]},
        {"from": 14, "still": "e_yard", "marks": [("text", 372, "(pim_yard)")]},
        {"from": 15, "still": "e_yard", "marks": [("lines", 380, 380)]},
        # the game first: the kit by the rock
        {"from": 16, "still": "game_l12_stash", "marks": [_ST_KIT]},
        {"from": 18, "still": "e_stash", "marks": [("lines", 340, 348)]},
        {"from": 19, "still": "e_stash", "marks": [("lines", 346, 346)]},
    ]},
    "s04_pim_s_scene": {"step": 4, "beats": [
        # the game first: her scene on the engineer's handheld
        {"from": 0, "still": "game_l12_pim_notice", "marks": [_PN_LINE]},
        {"from": 4, "still": "game_l12_pim_notice", "marks": [_PN_READ]},
        {"from": 5, "still": "game_l12_pim_notice", "marks": [_PN_SPARE]},
        {"from": 6, "still": "e_r4a", "marks": [("text", 560, "if learned spare")]},
        {"from": 8, "still": "e_r4a", "marks": [("text", 561, "; reveal stash")]},
        {"from": 9, "still": "e_r4a", "marks": [("lines", 569, 569)]},
        # the game first: the tablet in his pack
        {"from": 10, "still": "game_l12_pim_give", "marks": [_GV_GOT]},
        {"from": 12, "still": "game_l12_pim_give", "marks": [_GV_TWO]},
        {"from": 13, "still": "e_r4a", "marks": [("text", 562, "if holding tablet")]},
        {"from": 14, "still": "e_r4a", "marks": [("text", 562, "; take tablet, completes pim_tablet, give fuse")]},
        {"from": 16, "still": "e_r4a", "marks": [("lines", 563, 563)]},
        {"from": 19, "still": "e_r4b", "marks": [("lines", 588, 588)]},
        {"from": 20, "still": "e_r4b", "marks": [("text", 588, "dismiss pim")]},
        {"from": 21, "still": "e_r4b", "marks": [("text", 588, "summon pim_yard")]},
    ]},
    "s05_the_pump_with_fuses": {"step": 5, "beats": [
        # the game first: the panel with two fuses, then three
        {"from": 0, "still": "game_l12_panel_two", "marks": [_P2_LINE]},
        {"from": 3, "still": "game_l12_panel_two", "marks": [_P2_OFFER]},
        {"from": 4, "still": "game_l12_panel_three", "marks": [_P3_LINE]},
        {"from": 5, "still": "game_l12_panel_three", "marks": [_P3_FIT]},
        {"from": 6, "still": "e_r5", "marks": [("text", 547, "if holding fuse >= 3")]},
        {"from": 7, "still": "e_r5", "marks": [("text", 547, "; take fuse 3")]},
        {"from": 8, "still": "e_r5", "marks": [("text", 547, "if holding fuse >= 3"), ("text", 547, "; take fuse 3")]},
        {"from": 10, "still": "e_r5", "marks": [("text", 547, "holding")]},
        {"from": 11, "still": "e_r5", "marks": [("lines", 544, 545)]},
        {"from": 13, "still": "e_r5", "marks": [("text", 544, "party"), ("text", 545, "party")]},
        {"from": 14, "still": "e_r5", "marks": [("lines", 548, 548)]},
        {"from": 16, "still": "e_r5", "marks": [("text", 548, "check engineering 10 else pump_spark")]},
        {"from": 17, "still": "e_r5", "marks": [("lines", 555, 555)]},
        {"from": 18, "still": "e_r5", "marks": [("text", 547, "(pump_run)"), ("text", 548, "(pump_run)")]},
        {"from": 19, "still": "e_r5", "marks": [("lines", 555, 555)]},
    ]},
    "s06_two_more_uses_for_old_rooms": {"step": 6, "beats": [
        # the game first: the terminal's new button
        {"from": 0, "still": "game_l12_terminal_update", "marks": [_TU_SEALED]},
        {"from": 2, "still": "game_l12_terminal_update", "marks": [_TU_COPY]},
        {"from": 3, "still": "game_l12_terminal_update", "marks": [_TU_NEW]},
        {"from": 4, "still": "e_r6", "marks": [("lines", 456, 456)]},
        {"from": 5, "still": "e_r6", "marks": [("text", 456, "; calm sentry")]},
        {"from": 6, "still": "e_r6", "marks": [("lines", 459, 462)]},
        # the game first: Marrow on the weapons officer's handheld
        {"from": 7, "still": "game_l12_marrow_key", "marks": [_MK_SHOW]},
        {"from": 8, "still": "game_l12_marrow_key", "marks": [_MK_WHO]},
        {"from": 9, "still": "game_l12_marrow_key", "marks": [_MK_OKORO]},
        {"from": 10, "still": "e_marrow", "marks": [("text", 490, "if party pump_key")]},
        {"from": 11, "still": "e_marrow", "marks": [("lines", 494, 498)]},
    ]},
    "s07_the_endings_and_one_more_wor": {"step": 8, "beats": [
        {"from": 0, "still": "e_relight", "marks": [("lines", 75, 76)]},
        # the game first: the loss
        {"from": 3, "still": "game_l12_lost", "marks": [_LOST]},
        {"from": 5, "still": "e_burn", "marks": [("lines", 578, 578)]},
        {"from": 6, "still": "e_burn", "marks": [("text", 578, "; fails relight")]},
        # the game first: the beacon with the spare in the pack
        {"from": 7, "still": "game_l12_beacon", "marks": [_BC_FIT]},
        {"from": 8, "still": "e_beacon", "marks": [("lines", 529, 529)]},
        {"from": 9, "still": "e_beacon", "marks": [("text", 529, "if holding power_cell ; take power_cell")]},
        {"from": 10, "still": "game_l12_won", "marks": [_WON]},
        {"from": 11, "still": "e_discover", "marks": [("text", 586, "; discover cistern")]},
        {"from": 13, "still": "t_discover", "marks": [("part", "run1:clean")]},
    ]},
    "s08_play_it_and_your_turn": {"step": 11, "beats": [
        {"from": 0, "still": "card_route"},
        {"from": 1, "still": "card_route", "marks": [("part", "item1")]},
        {"from": 5, "still": "game_l12_marrow_key", "marks": [_MK_SHOW]},
        {"from": 6, "still": "game_l12_promise", "marks": [_PR_PROMISE]},
        {"from": 7, "still": "card_route", "marks": [("part", "item5")]},
        {"from": 9, "still": "game_l12_pim_give", "marks": [_GV_GIVE]},
        {"from": 10, "still": "game_l12_panel_three", "marks": [_P3_FIT]},
        {"from": 12, "still": "game_l12_pim_home", "marks": [_PH_OPEN]},
        {"from": 13, "still": "game_l12_won", "marks": [_WON]},
        {"from": 14, "still": "game_l12_lost", "marks": [_LOST]},
        {"from": 15, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 16, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 17, "still": "card_next"},
    ]},
}
