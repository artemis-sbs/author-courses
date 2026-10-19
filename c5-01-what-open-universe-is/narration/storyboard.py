"""Storyboard for c5-01-what-open-universe-is: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and
in the storyboards of Class 4. Caption numbers are those of shots.py.

This lecture writes nothing, so it has no STATES: the student plays Open Universe and READS
`silver_reach.amd`, the mission's own file. Those editor stills are the file as it is on
disk, in the stand-in's `OpenUniverse` folder ("folder" + "file", no state). Its lines are
those of the file on the v1.4.0_dev branch (364 lines): the title record on line 6, the
Lantern Combine on 17 to 29, Lighthouse Station on 202 to 210.

NOT IN THE STAND-IN YET: the stand-in's data\\missions has no OpenUniverse folder. Copy it
there (the committed files of the v1.4.0_dev branch) before --capture, or the three editor
stills of silver_reach.amd stop the run. The save file (universe_save_the_silver_reach_1.yaml)
is drawn as a card from the page's own words, because no real save is kept for the page.

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine, by a
person who knows it will rewrite their slot-1 save. NEVER start the engine for these from a
script. ONE game, TWO windows: `sbs run server,helm,comms -m OpenUniverse`, no map=0, the
start screen first, Universe set to The Silver Reach. Marks are left off every game still
until the stills are taken. Never caption a face. Press order:
  1. Server start screen, the mission picked: game_c51_universes (the Universe list open,
     four on it: Default, The Silver Reach, The Fading Signal, Skirmish - The Broken Accord).
  2. The Silver Reach chosen, the settings visible: game_c51_continue (the Start setting
     reading Continue, Universe reading The Silver Reach).
  3. Press Start Mission, take Helm and Comms. Helm at once: game_c51_home (the card naming
     Home Port, the one station, Starbase, in view).
  4. Comms, select the station: game_c51_comms (Market, Accept Cargo Run, Transport a
     passenger among its buttons). Press Accept Cargo Run.
  5. Helm: the handheld icon, Quests: game_c51_quests (The Dimming: A Cold Lane, Break the
     Veil, and the Cargo Run, all three in the list).
  6. Helm: select the cargo run: game_c51_noengage (no Engage button, the line "Manage
     quests at the Admiral or Comms console." in its place).
"""
LECTURE = "c5-01-what-open-universe-is"
TITLE = ("Class 5, Lecture 1", "What Open Universe is", "A whole galaxy, from one file")
MISSION = "OpenUniverse"
TEMPLATE = "ou"               # game.py: sandboxed (Open Universe writes saves)
PROBE_FROM = "OpenUniverse"   # game.py: the probe is the mission itself
FILE = "silver_reach.amd"

STATES = {}

_OU = {"folder": "OpenUniverse", "file": FILE, "side": False}

STILLS = {
    # The editor: silver_reach.amd as it is on disk. A still shows 21 lines: the one named, ten above and below
    "e_top": ("vscode", None, 11, "big", _OU),             # lines 1 to 21: the notes, the title record, the Sides chapter
    "e_lantern": ("vscode", None, 23, "big", _OU),         # lines 13 to 33: the Lantern Combine, whole
    "e_lighthouse": ("vscode", None, 206, "big", _OU),     # lines 196 to 216: Lighthouse Station, the landmark
    # THE REAL GAME. Not taken yet (see the docstring)
    "game_c51_universes": ("game", "The server start screen with Open Universe picked: the Universe list open, four on it (Default, The Silver Reach, The Fading Signal, Skirmish - The Broken Accord)"),
    "game_c51_continue": ("game", "The same screen with The Silver Reach chosen: the Start setting reading Continue, ready to press Start Mission"),
    "game_c51_home": ("game", "Helm in the first system: the card naming Home Port, the one station in view"),
    "game_c51_comms": ("game", "Comms with the station selected: Market, Accept Cargo Run and Transport a passenger among its buttons"),
    "game_c51_quests": ("game", "Helm, the handheld icon then Quests: The Dimming: A Cold Lane, Break the Veil and a Cargo Run in the list"),
    "game_c51_noengage": ("game", "Helm's Quest Log with a job selected: no Engage button, and the words 'Manage quests at the Admiral or Comms console.'"),
    # drawn: the page's own tables and words
    "card_title": ("card", "title", {}),
    "card_start": ("card", "rows", {"kicker": "Start it, leaving map=0 off", "header": ["Command", "Why"],
                                    "rows": [["sbs run server,helm,comms -m OpenUniverse", "No map=0, so the server shows the start screen"]]}),
    "card_universes": ("card", "table", {"heading": "Stop 2 - Start it, and choose a universe", "nth": 1, "kicker": "Four universes in the list"}),
    "card_questlog": ("card", "table", {"heading": "Stop 3 - The first system", "nth": 1, "kicker": "The Quest Log holds three things"}),
    "card_chapters": ("card", "table", {"heading": "Stop 4 - The file behind it", "nth": 1, "kicker": "One record, ten chapters"}),
    "card_there": ("card", "table", {"heading": "Stop 4 - The file behind it", "nth": 2, "kicker": "What the crew would find there"}),
    "card_kept": ("card", "table", {"heading": "Stop 5 - What is kept", "nth": 1, "kicker": "Two things outlive a session"}),
    "card_save": ("card", "rows", {"kicker": "universe_save_the_silver_reach_1.yaml", "header": ["Find", "What it holds"],
                                   "rows": [["universe_seed", "The one number the galaxy is made from"],
                                            ["current_system", "0 and 0, the system the ship is in"],
                                            ["The rest", "The systems seen, jobs, credits, sides at peace, what each side thinks"]]}),
    "card_bargain": ("card", "rows", {"kicker": "The bargain of this class", "header": ["You write", "The game supplies"],
                                      "rows": [["The people", "The stars and the empty systems"],
                                               ["The places", "The nebulae and the stations nobody named"],
                                               ["The events", "The raiders and the cargo drifting between them"]]}),
    "card_modes": ("card", "table", {"heading": "Stop 6 - Choose your mode", "nth": 1, "kicker": "One word says what kind of game"}),
    "card_exercise": ("card", "points", {"kicker": "Two things, both on paper", "items": [
        "Read the file: open silver_reach.amd and answer the five questions on the page. Each answer is one line of it.",
        "Plan yours: three sentences about your own universe. Who lives there, who shoots first, what the crew is there to do. Then write down your mode."]}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 2", "sub": "Your universe file"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c51_quests"},
        {"from": 2, "still": "game_c51_home"},
        {"from": 5, "still": "game_c51_universes"},
        {"from": 7, "still": "e_top"},
        {"from": 9, "still": "card_title"},
    ]},
    "s02_start_it_and_choose_a_univer": {"step": 2, "beats": [
        {"from": 0, "still": "card_start", "marks": [("part", "r1")]},
        {"from": 4, "still": "game_c51_universes"},
        {"from": 5, "still": "card_universes", "marks": [("part", "r2")]},
        {"from": 7, "still": "game_c51_continue"},
    ]},
    "s03_the_first_system": {"step": 3, "beats": [
        {"from": 0, "still": "game_c51_home"},
        {"from": 3, "still": "game_c51_comms"},
        {"from": 4, "still": "game_c51_quests"},
        {"from": 5, "still": "card_questlog", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_questlog", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_questlog", "marks": [("part", "r3")]},
        {"from": 8, "still": "game_c51_quests"},
        {"from": 9, "still": "game_c51_noengage"},
    ]},
    "s04_one_file": {"step": 4, "beats": [
        {"from": 0, "still": "e_top"},
        {"from": 2, "still": "e_top", "marks": [("lines", 6, 12)]},
        {"from": 4, "still": "card_chapters"},
        {"from": 5, "still": "card_chapters", "marks": [("part", "r2")]},
        {"from": 6, "still": "card_chapters", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_chapters", "marks": [("part", "r4"), ("part", "r5")]},
        {"from": 9, "still": "card_chapters", "marks": [("part", "r7"), ("part", "r8")]},
        {"from": 10, "still": "card_chapters", "marks": [("part", "r9"), ("part", "r10")]},
        {"from": 11, "still": "card_chapters", "marks": [("part", "r11")]},
        {"from": 12, "still": "card_chapters"},
    ]},
    "s05_from_a_record_to_a_place": {"step": 4, "beats": [
        {"from": 0, "still": "e_lantern"},
        {"from": 1, "still": "e_lantern", "marks": [("text", 17, "The Lantern Combine")]},
        {"from": 3, "still": "e_lantern", "marks": [("text", 17, "###"), ("text", 18, "---"), ("lines", 19, 26), ("text", 27, "---")]},
        {"from": 4, "still": "e_lantern", "marks": [("text", 22, "Home: -4, 2")]},
        {"from": 5, "still": "card_there", "marks": [("part", "r1")]},
        {"from": 8, "still": "e_lighthouse", "marks": [("text", 204, "At: -4, 2")]},
        {"from": 9, "still": "e_lantern", "marks": [("text", 24, "Offers: escort, bounty")]},
        {"from": 10, "still": "card_there", "marks": [("part", "r3")]},
        {"from": 11, "still": "card_there"},
    ]},
    "s06_what_isn_t_in_the_file": {"step": 5, "beats": [
        {"from": 0, "still": "e_top"},
        {"from": 4, "still": "card_kept", "marks": [("part", "r1")]},
        {"from": 7, "still": "card_save", "marks": [("part", "r1")]},
        {"from": 8, "still": "card_save", "marks": [("part", "r2")]},
        {"from": 9, "still": "card_save", "marks": [("part", "r3")]},
        {"from": 10, "still": "card_bargain"},
    ]},
    "s07_choose_your_mode": {"step": 6, "beats": [
        {"from": 0, "still": "card_modes"},
        {"from": 2, "still": "card_modes", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_modes", "marks": [("part", "r3")]},
        {"from": 5, "still": "card_modes", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_modes", "marks": [("part", "r4"), ("part", "r5")]},
        {"from": 8, "still": "card_modes", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 9, "still": "card_modes"},
    ]},
    "s08_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 7, "still": "card_next"},
    ]},
}
