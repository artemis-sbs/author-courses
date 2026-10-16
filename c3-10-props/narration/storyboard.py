"""Storyboard for c3-10-props: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 9's files ("start"). Each step is a state: the key (p1), the
door (p2), the toolbox (p3), the notice (p4), the panel (p5), their three rooms at the end
of the file (p6, lint's one true warning), the cistern's three marks (p7a) and the gate, the
spare cell and the gauge ("final", the page's own example files).

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders), and lint prints `ground\\...` as the student's does. The close views of
the text hide the Side Bar, as every close view of this class does.

THE TILE MAP EDITOR STILL (d_marks) is taken in the add-on's own editor ("editor": "tiles",
"view": "art"; see capture.web_steps).

GAME STILLS. Not taken yet; no marks until the screenshots exist. THREE windows: server,
science (Dr Ines Hale) and engineering (Chief Okoro), the page's
`sbs run server,engineering,science -m MyAway map=0`, state final as the page has it (no
probe-only change: Lecture 9's path behind the relay house keeps the crew five cells from
the sentry's loop): `python game.py c3-10-props start --consoles server,engineering,science`.
  1. About 15 s after the consoles are seated, both: handheld icon (top left), Boarding Party,
     Kesh Relay, BEAM DOWN.
  2. Science: walk toward the tent; the key on its peg at 14, 4 in view: game_l10_keymap.
     Click it, then open Pack: game_l10_pack (pump key).
  3. Both walk east by the path behind the relay house (click about 22, 0 first, never row 6,
     which passes three cells from the sentry's loop), then take the exit (29, 6), one at a
     time. Engineering: walk to the pump house
     door (12, 5): game_l10_door_shut. Click it: game_l10_door_open (open; the words
     `pump key fits` if they show).
  4. Science: click the toolbox (19, 8), open Pack: game_l10_fuse (fuse x2). Click the notice
     (11, 4): game_l10_notice (its scene). 'Let the pieces fall', click it again:
     game_l10_notice2 (the description only).
  5. Science: click the pump panel (16, 6): game_l10_needs ('You would need engineering for
     that.'). Engineering: click it: game_l10_panel (The Pump Panel). Press 'Leave it alone'.
  6. Engineering: the stairs (17, 5). In the cistern: game_l10_cistern (the gate shut at 14, 2,
     the gauge in the tank). Click the gauge from the walkway: game_l10_gauge.
  7. Engineering: back up, the panel, 'Throw the lever', 'Step back'. Down again:
     game_l10_drained (the gate open, the power cell in the east room at 16, 2).
"""
LECTURE = "c3-10-props"
TITLE = ("Class 3, Lecture 10", "Props", "Things to pick up, open and use")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"
CT = "ground/cistern.tiles"

_L7 = "c3-07-anatomy-of-a-long-away-mission/example"
_L8 = "c3-08-tile-map-editor-part-1/example"
_L9 = "c3-09-tile-map-editor-part-2/example"
_EX = "c3-10-props/example"
_PEOPLE = "\n\n// ---- People: someone"

_KEY = ("// ---- Lecture 10: the pump house and the cistern.\n"
        "### [Pump house key](pump_key)\n---\nArea: landing\nAt: 14, 4\nSprite: prop:keycard\nItem: pump_key\n---\n"
        "A brass key on a loop of wire, hung on a tent peg.\n")
_DOOR = ("### [Pump house door](pump_door)\n---\nArea: gully\nMark: pump_door\nSprite: prop:hatch\n"
         "Open sprite: prop:doorframe\nBlocks: yes\nOpens with: key pump_key, check engineering 8, cut\n"
         "Scan: A plain mechanical lock. No power to it at all.\n---\nA steel door, rusted at the hinges.\n")
_TOOLBOX = ("// `Qty:` is how many of the item one pickup is worth.\n"
            "### [Toolbox](toolbox)\n---\nArea: gully\nAt: 19, 8\nSprite: prop:toolbox\nItem: fuse\nQty: 2\n---\n"
            "A toolbox left open in the dust. Two heavy fuses, still in their paper.\n")
_NOTICE = ("// `Once: yes`: the scene opens the first time. After that there is only the description.\n"
           "### [Brittle notice](notice)\n---\nArea: gully\nAt: 11, 4\nSprite: prop:sign\nScene: notice\nOnce: yes\n---\n"
           "A notice pasted beside the door, gone brown and brittle. It will not survive being read twice.\n")
_PANEL = ("// `Needs:` is who may use it at all. Nobody covers for a `Needs:`.\n"
          "### [Pump panel](pump_panel)\n---\nArea: gully\nAt: 16, 6\nSprite: prop:console\nScene: pump_panel\n"
          "Blocks: yes\nNeeds: engineering\nScan: Three fuse clips, all empty. The pump below it is sound.\n---\n"
          "The pump's control panel: one lever, one dial, and a row of fuse clips.\n")
_ROOMS = ("\n\n// ---- Lecture 10: what the new props open.\n"
          "### [The Notice](notice)\n"
          "% SPARE BEACON CELL KEPT BELOW, IN THE COLD. DRAIN THE TANK FIRST. The paper comes apart in your fingers as you read the last line.\n\n"
          "- [Let the pieces fall]() ; learn spare\n\n"
          "### [The Pump Panel](pump_panel)\n"
          "% The dial sits at zero. The lever is stiff, and it moves.\n\n"
          "- [Throw the lever](pump_run) ; signal cistern_drained\n"
          "- [Leave it alone]()\n\n"
          "### [The Pump Runs](pump_run)\n"
          "% The pump coughs, catches, and settles to a hammering you can feel through the floor. Somewhere under your feet, a great deal of water starts to move.\n\n"
          "- [Step back]()\n")
_DOWNSTAIRS = ("// A door only a signal opens: nobody on the ground can force it.\n"
               "### [Sluice gate](sluice)\n---\nArea: cistern\nMark: sluice\nSprite: prop:hatch\nOpen sprite: prop:doorframe\n"
               "Blocks: yes\nOpens with: signal cistern_drained\nScan: Held shut by the weight of the water behind it.\n---\n"
               "An iron gate across the walkway, wet to the top.\n\n"
               "### [Spare power cell](spare_cell)\n---\nArea: cistern\nMark: crate\nSprite: prop:power_cell\n"
               "Item: power_cell\nHidden until: cistern_drained\n---\n"
               "A beacon cell in a sealed case, left where the water would keep it cool.\n\n"
               "// `Reach: 2`: it can be used from two cells away. It stands in the water, where\n"
               "// nobody can stand beside it.\n"
               "### [Depth gauge](gauge)\n---\nArea: cistern\nMark: gauge\nSprite: prop:scanner\nReach: 2\n"
               "Scan: Four meters of water over the tank floor.\n---\n"
               "A brass depth gauge on a post in the middle of the tank. The needle reads FULL.\n")


def _add(rec):
    """One more record at the end of the Props section, a blank line before it."""
    return ("replace", FILE, _PEOPLE, "\n" + rec + _PEOPLE)


STATES = {
    # Lecture 9's files
    "start": {"folder": _L7, "over": (_L8, _L9)},
    "p1": {"base": "start", "edits": [_add(_KEY)]},           # Step 1: a pickup
    "p2": {"base": "p1", "edits": [_add(_DOOR)]},             # Step 2: a door
    "p3": {"base": "p2", "edits": [_add(_TOOLBOX)]},          # Step 3: a pickup worth two
    "p4": {"base": "p3", "edits": [_add(_NOTICE)]},           # Step 4: a thing to read, once
    "p5": {"base": "p4", "edits": [_add(_PANEL)]},            # Step 5: a terminal
    "p6": {"base": "p5", "edits": [("append", FILE, _ROOMS)]},  # Step 6: their scenes
    # Step 7: three marks in the cistern, then the three props. The page's own files.
    "p7a": {"base": "p6", "edits": [
        ("replace", CT, "  f: floor @foot\n", "  f: floor @foot\n  s: floor @sluice\n  c: floor @crate\n  g: water @gauge\n"),
        ("replace", CT, "W_~~~~~~~~~~_____W\nW_~~~~~~~~~~__W__W", "W_~~~~~~~~~~__s_cW\nW_~~~~g~~~~~__W__W")]},
    "final": {"base": "p7a", "edits": [_add(_DOWNSTAIRS)],
              "same_as": (_EX + "/mission.amd", _EX + "/ground/cistern.tiles")},
    # Step 8 / scene 8: a key's name and a signal's name misspelled
    "b_key": {"base": "final", "edits": [("replace", FILE, "Item: pump_key", "Item: pumphouse_key")]},
    "b_signal": {"base": "final", "edits": [("replace", FILE, "Opens with: signal cistern_drained", "Opens with: signal cistern_draind")]},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}
_CT = {"side": False, "file": CT}


def _lint(state):
    """sbs lint on the state, as the student types it."""
    return ("session", [_LINT], {"state": state})
STILLS = {
    "t_p6": _lint("p6"),
    "t_final": _lint("final"),
    "t_key": _lint("b_key"),
    "t_signal": _lint("b_signal"),
    # mission.amd as it is typed (the line each still is centered on is in BOARD's marks)
    "e_key": ("vscode", "p1", 226, "big", _NS),
    "e_door": ("vscode", "p2", 238, "big", _NS),
    "e_toolbox": ("vscode", "p3", 249, "big", _NS),
    "e_notice": ("vscode", "p4", 260, "big", _NS),
    "e_panel": ("vscode", "p5", 272, "big", _NS),
    "e_rooms": ("vscode", "p6", 432, "big", _NS),
    "e_marks": ("vscode", "p7a", 13, "mid", _CT),          # the whole cistern, 25 lines
    "e_gate": ("vscode", "final", 285, "big", _NS),        # lines 275 to 295: the sluice gate
    "e_cell": ("vscode", "final", 303, "big", _NS),        # lines 293 to 313: the cell, the gauge
    # cistern.tiles (p7a) in the Tile Map Editor, Art, Marks on: sluice, crate and gauge outlined
    "d_marks": ("vscode", "p7a", 1, "mid", dict(_NS, file=CT, editor="tiles", view="art", zoom=48)),
    # THE REAL GAME (not taken yet). State final, consoles server,engineering,science; see the docstring
    "game_l10_keymap": ("game", "Science (Dr Hale) in the yard near the tent: the pump house key drawn on its peg at 14, 4"),
    "game_l10_pack": ("game", "Science, the key clicked: the Pack app open, holding the pump key; the key gone from the map"),
    "game_l10_door_shut": ("game", "Engineering (Chief Okoro) in the gully beside the pump house door (12, 5), shut"),
    "game_l10_door_open": ("game", "Engineering, the door clicked with the key in Dr Hale's pack: the door open (the doorframe picture), the words 'pump key fits' if the handheld shows them"),
    "game_l10_fuse": ("game", "Science, the toolbox (19, 8) clicked: the Pack app reading fuse x2"),
    "game_l10_notice": ("game", "Science, the notice (11, 4) clicked: The Notice's line 'SPARE BEACON CELL KEPT BELOW...' and one button, Let the pieces fall"),
    "game_l10_notice2": ("game", "Science, the notice clicked a second time: only its description, '...It will not survive being read twice.'"),
    "game_l10_needs": ("game", "Science, the pump panel (16, 6) clicked: 'You would need engineering for that.'"),
    "game_l10_panel": ("game", "Engineering, the pump panel clicked: The Pump Panel's line and two buttons, Throw the lever / Leave it alone"),
    "game_l10_cistern": ("game", "Engineering in the cistern before the lever: the sluice gate shut across the walkway (14, 2), the gauge out in the tank (6, 3), the east room empty"),
    "game_l10_gauge": ("game", "Engineering, the gauge clicked from the walkway two cells off: its description, 'The needle reads FULL.'"),
    "game_l10_drained": ("game", "Engineering in the cistern after 'Throw the lever': the sluice gate open, the spare power cell in the east room (16, 2)"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_questions": ("card", "table", {"heading": "What a prop does", "kicker": "Four questions, in order"}),
    "card_door": ("card", "table", {"heading": "Step 2 - A door", "kicker": "A door"}),
    "card_terms": ("card", "table", {"heading": "Step 2 - A door", "nth": 2, "kicker": "Four ways in"}),
    "card_marks": ("card", "table", {"heading": "Step 7 - A gate, a hidden cell and a gauge", "kicker": "Three marks in the cistern"}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 2, "kicker": "Lint says clean, and", "rows": (2, 3)}),
    "card_run": ("card", "points", {"kicker": "A server and two consoles", "items": ["sbs run server,engineering,science -m MyAway map=0"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Keys and doors"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 11", "sub": "People and hostiles"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l10_door_shut"},
        {"from": 2, "still": "game_l10_door_open"},
        {"from": 4, "still": "game_l10_panel"},
        {"from": 5, "still": "e_door", "marks": [("lines", 233, 243)]},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_what_a_prop_does": {"step": None, "beats": [
        {"from": 0, "still": "card_questions"},
        {"from": 2, "still": "card_questions", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_questions", "marks": [("part", "r2")]},
        {"from": 4, "still": "card_questions", "marks": [("part", "r3")]},
        {"from": 5, "still": "card_questions", "marks": [("part", "r4")]},
        {"from": 6, "still": "card_questions"},
        # the game first: the key, then the pack
        {"from": 9, "still": "game_l10_keymap"},
        {"from": 10, "still": "game_l10_pack"},
        {"from": 11, "still": "e_key", "marks": [("lines", 224, 231)]},
        {"from": 12, "still": "e_key", "marks": [("lines", 229, 229)]},
        {"from": 14, "still": "game_l10_pack"},
    ]},
    "s03_a_door": {"step": 2, "beats": [
        # the game first: the door, shut and open
        {"from": 0, "still": "game_l10_door_shut"},
        {"from": 1, "still": "game_l10_door_open"},
        {"from": 2, "still": "e_door", "marks": [("lines", 233, 243)]},
        {"from": 3, "still": "e_door", "marks": [("lines", 239, 239)]},
        {"from": 5, "still": "e_door", "marks": [("lines", 240, 240)]},
        {"from": 7, "still": "card_terms", "marks": [("part", "r1")]},
        {"from": 9, "still": "card_terms", "marks": [("part", "r2")]},
        {"from": 11, "still": "card_terms", "marks": [("part", "r3")]},
        {"from": 12, "still": "e_door", "marks": [("text", 240, "key pump_key"), ("text", 240, "check engineering 8")]},
        {"from": 15, "still": "card_terms", "marks": [("part", "r2")]},
    ]},
    "s04_two_more_pickups_and_a_notic": {"step": 3, "beats": [
        # the game first: two fuses, and the notice's scene
        {"from": 0, "still": "game_l10_fuse"},
        {"from": 2, "still": "game_l10_notice"},
        {"from": 3, "still": "e_toolbox", "marks": [("lines", 245, 254)]},
        {"from": 4, "still": "e_toolbox", "marks": [("lines", 252, 252)]},
        {"from": 5, "still": "e_notice", "marks": [("lines", 256, 265)]},
        {"from": 6, "still": "e_notice", "marks": [("lines", 262, 262)]},
        {"from": 8, "still": "e_notice", "marks": [("lines", 263, 263)]},
        {"from": 10, "still": "game_l10_notice"},
        {"from": 11, "still": "game_l10_notice2"},
        {"from": 12, "still": "e_notice", "marks": [("lines", 263, 263)]},
    ]},
    "s05_a_terminal_with_a_needs": {"step": 5, "beats": [
        # the game first: the doctor refused
        {"from": 0, "still": "game_l10_needs"},
        {"from": 2, "still": "e_panel", "marks": [("lines", 267, 278)]},
        {"from": 4, "still": "e_panel", "marks": [("lines", 275, 275)]},
        {"from": 5, "still": "game_l10_needs"},
        {"from": 7, "still": "e_panel", "marks": [("lines", 275, 275)]},
        {"from": 11, "still": "e_panel", "marks": [("lines", 276, 276)]},
    ]},
    "s06_their_rooms_and_a_true_warni": {"step": 6, "beats": [
        {"from": 0, "still": "e_rooms", "marks": [("lines", 423, 438)]},
        {"from": 2, "still": "e_rooms", "marks": [("text", 427, "; learn spare")]},
        {"from": 3, "still": "e_rooms", "marks": [("text", 432, "; signal cistern_drained")]},
        {"from": 4, "still": "t_p6", "marks": [("span", 1, "signal-no-route")]},
        {"from": 5, "still": "t_p6"},
    ]},
    "s07_a_gate_a_hidden_cell_and_a_g": {"step": 7, "beats": [
        # the game first: downstairs, before the lever
        {"from": 0, "still": "game_l10_cistern"},
        {"from": 2, "still": "e_marks", "marks": [("lines", 15, 17)]},
        {"from": 3, "still": "card_marks"},
        {"from": 4, "still": "e_gate", "marks": [("lines", 280, 291)]},
        {"from": 5, "still": "e_gate", "marks": [("lines", 288, 288)]},
        {"from": 7, "still": "e_cell", "marks": [("lines", 299, 299)]},
        {"from": 9, "still": "e_cell", "marks": [("lines", 293, 301)]},
        {"from": 10, "still": "game_l10_drained"},
        {"from": 13, "still": "e_cell", "marks": [("lines", 303, 313)]},
        {"from": 14, "still": "e_cell", "marks": [("lines", 310, 310)]},
        {"from": 15, "still": "game_l10_gauge"},
        {"from": 16, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s08_what_lint_can_t_see_and_play": {"step": 8, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "t_key", "marks": [("span", 1, "item-nothing-gives")]},
        {"from": 4, "still": "t_signal", "marks": [("span", 1, "ground-signal-unsent")]},
        {"from": 5, "still": "card_cannot", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 8, "still": "card_run"},
        {"from": 9, "still": "game_l10_pack"},
        {"from": 10, "still": "game_l10_door_open"},
        {"from": 11, "still": "game_l10_needs"},
        {"from": 11.5, "still": "game_l10_panel"},
        {"from": 12, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 14, "still": "card_next"},
    ]},
}
