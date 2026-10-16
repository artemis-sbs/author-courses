"""Storyboard for c3-11-people-and-hostiles: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 10's files ("start"). Each step is a state: Pim's mark in
the gully (h1), Pim (h2), her two rooms at the end of the file (h3), the sump crawler (h4)
and The Thing in the Sump ("final", the page's own example files).

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders), and lint prints `ground\\...` as the student's does. The close views of
the text hide the Side Bar, as every close view of this class does.

THE TILE MAP EDITOR STILL (d_crawler) is taken in the add-on's own editor ("editor": "tiles",
"view": "art"; see capture.web_steps).

GAME STILLS. Not taken yet; no marks until the screenshots exist. The page plays with FOUR
windows (server, engineering, weapons, science); the stills are taken in two games of THREE.
Both use state final as the page has it (no probe-only change): the crew walks east by
Lecture 9's path behind the relay house, five cells clear of the sentry's loop.
`python game.py c3-11-people-and-hostiles start --consoles server,science,engineering`
(GAME A), `--consoles server,engineering,weapons` (GAME B).
GAME A: server, science (Dr Ines Hale), engineering (Chief Okoro).
  1. About 15 s after the consoles are seated, both: handheld icon (top left), Boarding
     Party, Kesh Relay, BEAM DOWN.
  2. Engineering: open Tasks: game_l11_tasks (The Thing in the Sump, not done).
  3. Science: click the path behind the relay house (about 22, 0; never row 6), then the
     exit (29, 6). In the gully walk toward Pim's camp in the scrub (5, 8): game_l11_pim.
     Click her: game_l11_pim_talk (her room).
GAME B: server, engineering (Chief Okoro), weapons (Lt Sam Reyes).
  1. Both beam down and walk to the gully. Open the pump house door: Okoro clicks it until
     his check makes 8 (it can be tried again at once), or Reyes shoots it with CUT.
  2. Both take the stairs (17, 5) and stop at the foot: game_l11_crawler (Engineering: the
     crawler on the far walkway, about 12-13, 1-5).
  3. Engineering: open Scan: game_l11_scan (the crawler's line among what is in sight).
  4. Weapons: open Fire, STUN, Arm: game_l11_fire. Click the crawler within six cells. Then
     CUT, Arm, click; CUT again; FULL. When it falls: game_l11_down (the crawler gone, the
     tablet where it fell).
  5. Engineering: open Tasks: game_l11_done (The Thing in the Sump done).
"""
LECTURE = "c3-11-people-and-hostiles"
TITLE = ("Class 3, Lecture 11", "People and hostiles", "One line between them")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"
GT, CT = "ground/gully.tiles", "ground/cistern.tiles"

_L7 = "c3-07-anatomy-of-a-long-away-mission/example"
_L8 = "c3-08-tile-map-editor-part-1/example"
_L9 = "c3-09-tile-map-editor-part-2/example"
_L10 = "c3-10-props/example"
_EX = "c3-11-people-and-hostiles/example"

_PIM = ("// ---- Lecture 11.\n### [Pim](pim)\n---\nArea: gully\nMark: camp\nSprite: fig:junker_f\nFace: female\n"
        "Calm: yes\nTalk scene: pim\nScan: One human, young. Cold, and not hurt.\n---\n"
        "Marrow's apprentice, wrapped in a survey blanket with her back to a rock.\n")
_ROOMS = ("\n\n// ---- Lecture 11: somebody to talk to.\n### [Pim](pim)\n"
          "% \"You are from the ship.\" She does not get up. \"I came out here to start the pump, nine days ago. I got as far as the door.\"\n\n"
          "- [Ask what stopped her](pim_why)\n- [Leave her be]()\n\n"
          "### [What Stopped Her](pim_why)\n"
          "% \"There is something on the walkway down there. It took my tablet out of my hand and I ran. I have been working up to going back for it ever since.\"\n\n"
          "- [Ask her something else](pim)\n- [Leave her be]()\n")
_CRAWLER = ("// ---- Lecture 11. A hostile is a person without `Calm: yes`.\n### [Sump crawler](crawler)\n---\n"
            "Area: cistern\nAt: 13, 3\nSprite: fig:glassback\nHP: 3\nDamage: 1\nNotice: 3\nStun: 8\nSpeed: 2\n"
            "Patrol: 12 1; 13 5; 12 5; 13 1\nDrops: tablet\n"
            "Scan: Silicate shell, about the size of a dog. It has something flat in its jaws.\n---\n"
            "Something low and glassy that has had the walkway to itself for nine days.\n")
_SUMP = ("### [The Thing in the Sump](sump)\n---\nFor: engineering\nStarts when: at once\n"
         "Objective: Clear the cistern walkway\nDone when: signal hostile_down_crawler\nLeads to: crawler\n---\n"
         "Whatever is living in the cistern has been at the pump lines.\n")


def _before(heading, rec):
    """One more record at the end of a section: a blank line, the record, before the next section's note."""
    return ("replace", FILE, "\n\n" + heading, "\n" + rec + "\n\n" + heading)


STATES = {
    # Lecture 10's files
    "start": {"folder": _L7, "over": (_L8, _L9, _L10)},
    # Step 1: a mark for a person
    "h1": {"base": "start", "edits": [
        ("replace", GT, "  p: floor @pump\n", "  p: floor @pump\n  m: scrub @camp\n"),
        ("replace", GT, "^#...,,..............#^^", "^#...m,..............#^^")]},
    "h2": {"base": "h1", "edits": [_before("// ---- Hostiles: someone", _PIM)]},          # Step 2: a person
    "h3": {"base": "h2", "edits": [("append", FILE, _ROOMS)]},                             # Step 3: what she says
    "h4": {"base": "h3", "edits": [_before("// ---- Scenes: what", _CRAWLER)]},             # Step 4: a hostile
    # Step 5: a quest it finishes. The page's own files.
    "final": {"base": "h4", "edits": [_before("// ---- Props: things", _SUMP)],
              "same_as": (_EX + "/mission.amd", _EX + "/ground/gully.tiles")},
    # Step 8 / scene 8
    "b_nocalm": {"base": "final", "edits": [("replace", FILE, "Face: female\nCalm: yes\n", "Face: female\n")]},
    "b_water": {"base": "final", "edits": [("replace", FILE, "At: 13, 3\n", "At: 6, 3\n")]},
    "b_signal": {"base": "final", "edits": [("replace", FILE, "signal hostile_down_crawler", "signal hostile_down_crawlr")]},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}


def _lint(state):
    """sbs lint on the state, as the student types it."""
    return ("session", [_LINT], {"state": state})
STILLS = {
    "t_final": _lint("final"),
    # person-talks-but-attacks: sbs_utils 4beddf8c, released 2026-10-15.
    "t_nocalm": _lint("b_nocalm"),
    "t_water": _lint("b_water"),
    "t_signal": _lint("b_signal"),
    "e_camp": ("vscode", "h1", 22, "mid", {"side": False, "file": GT}),   # lines 8 to 36
    "e_pim": ("vscode", "h2", 339, "big", _NS),             # lines 329 to 349: Pim
    "e_rooms": ("vscode", "h3", 494, "big", _NS),          # lines 484 to 500: her rooms
    "e_crawler": ("vscode", "h4", 376, "big", _NS),        # lines 366 to 386: the crawler
    "e_sump": ("vscode", "final", 125, "big", _NS),        # lines 115 to 135: the story
    "e_nocalm": ("vscode", "b_nocalm", 349, "big", _NS),   # lines 339 to 359
    # cistern.tiles in the Tile Map Editor, Art, Things on: the crawler at 13, 3 and its dashed patrol loop
    "d_crawler": ("vscode", "final", 1, "mid", dict(_NS, file=CT, editor="tiles", view="art", zoom=48)),
    # THE REAL GAME (not taken yet). State final, two games of three windows; see the docstring
    "game_l11_pim": ("game", "GAME A, Science (Dr Hale) in the gully: Pim sitting in the scrub at her camp (5, 8), at the west end"),
    "game_l11_pim_talk": ("game", "GAME A, Science, Pim clicked: her line '\"You are from the ship.\" She does not get up...' with her face, and two buttons, Ask what stopped her / Leave her be"),
    "game_l11_tasks": ("game", "GAME A, Engineering (Chief Okoro): the Tasks app, The Thing in the Sump listed, 'Clear the cistern walkway', not done"),
    "game_l11_crawler": ("game", "GAME B, Engineering at the foot of the cistern stairs: the crawler on the far walkway at the east end of the tank"),
    "game_l11_scan": ("game", "GAME B, Engineering: the Scan app, what is in sight, the crawler's line 'Silicate shell, about the size of a dog...'"),
    "game_l11_fire": ("game", "GAME B, Weapons (Lt Reyes) at the foot of the stairs: the Fire app, STUN chosen, Arm"),
    "game_l11_down": ("game", "GAME B, Weapons, after stun, cut, cut and full: the crawler gone, the tablet lying where it fell"),
    "game_l11_done": ("game", "GAME B, Engineering: the Tasks app, The Thing in the Sump done"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_pim": ("card", "table", {"heading": "Step 2 - A person", "kicker": "A person"}),
    "card_hostile": ("card", "table", {"heading": "Step 4 - A hostile", "kicker": "A hostile"}),
    "card_settings": ("card", "table", {"heading": "Step 6 - A fight", "kicker": "The Fire app"}),
    "card_up": ("card", "points", {"kicker": "Down, and back up", "items": [
        "Every crew member on the ground has 3 HP. At 0 they are down",
        "A medical kit, from the next cell: back on their feet with 2 HP",
        "Everybody down: the whole party comes round at the entry eight seconds later, 1 HP each"]}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 2, "kicker": "Lint says clean, and"}),
    "card_run": ("card", "points", {"kicker": "Three consoles", "items": ["sbs run server,engineering,weapons,science -m MyAway map=0"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Tougher, then gentler"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 12", "sub": "Scenes on the ground"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l11_pim"},
        {"from": 2, "still": "game_l11_crawler"},
        {"from": 3, "still": "e_crawler", "marks": [("lines", 368, 383)]},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_a_person": {"step": 1, "beats": [
        # the game first: Pim at her camp
        {"from": 0, "still": "game_l11_pim"},
        {"from": 2, "still": "e_camp", "marks": [("lines", 20, 20), ("text", 32, "m")]},
        {"from": 4, "still": "e_pim", "marks": [("lines", 333, 344)]},
        {"from": 5, "still": "e_pim", "marks": [("lines", 336, 337)]},
        {"from": 7, "still": "e_pim", "marks": [("lines", 338, 338)]},
        {"from": 8, "still": "e_pim", "marks": [("lines", 339, 339)]},
        {"from": 9, "still": "e_pim", "marks": [("lines", 340, 341)]},
        {"from": 10, "still": "e_pim", "marks": [("lines", 340, 340)]},
        {"from": 12, "still": "e_pim", "marks": [("lines", 341, 341)]},
        {"from": 13, "still": "card_pim", "marks": [("part", "r4")]},
    ]},
    "s03_what_she_says": {"step": 3, "beats": [
        # the game first: her room on the handheld
        {"from": 0, "still": "game_l11_pim_talk"},
        {"from": 2, "still": "e_rooms", "marks": [("lines", 489, 500)]},
        {"from": 4, "still": "e_rooms", "marks": [("lines", 491, 491)]},
        {"from": 5, "still": "e_rooms", "marks": [("lines", 497, 497)]},
    ]},
    "s04_a_hostile": {"step": 4, "beats": [
        # the game first: the crawler downstairs
        {"from": 0, "still": "game_l11_crawler"},
        {"from": 1, "still": "e_crawler", "marks": [("lines", 368, 383)]},
        {"from": 2, "still": "e_pim", "marks": [("lines", 340, 340)]},
        {"from": 3, "still": "e_crawler", "marks": [("lines", 370, 382)]},
        {"from": 5, "still": "card_hostile", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_hostile", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_hostile", "marks": [("part", "r3")]},
        {"from": 8, "still": "card_hostile", "marks": [("part", "r6")]},
        {"from": 9, "still": "card_hostile", "marks": [("part", "r7")]},
        {"from": 10, "still": "d_crawler"},
        {"from": 14, "still": "e_crawler", "marks": [("lines", 371, 371), ("lines", 379, 379)]},
        {"from": 17, "still": "game_l11_crawler"},
    ]},
    "s05_a_quest_it_finishes": {"step": 5, "beats": [
        # the game first: the engineer's Tasks app
        {"from": 0, "still": "game_l11_tasks"},
        {"from": 3, "still": "e_sump", "marks": [("lines", 126, 126)]},
        {"from": 5, "still": "e_sump", "marks": [("text", 126, "hostile_down_crawler")]},
        {"from": 6, "still": "e_sump", "marks": [("lines", 121, 129)]},
        {"from": 8, "still": "e_sump", "marks": [("lines", 123, 123)]},
        {"from": 9, "still": "e_sump", "marks": [("lines", 127, 127)]},
    ]},
    "s06_a_fight_and_getting_hurt": {"step": 6, "beats": [
        {"from": 0, "still": "game_l11_fire"},
        {"from": 5, "still": "card_settings", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_settings", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_settings", "marks": [("part", "r3")]},
        {"from": 9, "still": "card_settings"},
        {"from": 11, "still": "card_up", "marks": [("part", "item1")]},
        {"from": 14, "still": "card_up", "marks": [("part", "item2")]},
        {"from": 15, "still": "card_up", "marks": [("part", "item3")]},
        {"from": 18, "still": "card_up"},
    ]},
    "s07_play_it": {"step": 9, "beats": [
        {"from": 0, "still": "card_run"},
        {"from": 1, "still": "game_l11_pim_talk"},
        {"from": 2, "still": "game_l11_crawler"},
        {"from": 4, "still": "game_l11_scan"},
        {"from": 5, "still": "game_l11_fire"},
        {"from": 7, "still": "game_l11_down"},
        {"from": 9, "still": "game_l11_done"},
    ]},
    "s08_what_lint_can_t_see_and_your": {"step": 8, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "t_signal", "marks": [("span", 1, "unfired-signal")]},
        {"from": 2, "still": "t_water", "marks": [("span", 1, "tiles-unwalkable")]},
        {"from": 3, "still": "e_nocalm", "marks": [("lines", 349, 350)]},
        {"from": 4, "still": "t_nocalm", "marks": [("span", 1, "person-talks-but-attacks")]},
        {"from": 7, "still": "card_cannot", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 12, "still": "card_next"},
    ]},
}
