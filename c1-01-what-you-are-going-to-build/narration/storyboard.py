"""Storyboard for c1-01-what-you-are-going-to-build: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Lectures
5 and 6, and the new kinds of still in _tools/picture/README.md. Caption numbers are those
of the narration REWRITTEN FOR THE EAR (2026-10-06).

The lecture types nothing: it is a tour.

- The game stills g_* are REAL, taken 2026-10-06 on the developer install by starting the
  game with no arguments and clicking through it (eng.ps1): the first screen, Start Server,
  Choose Mission, Legendary Missions' start screen with Siege, the Boss list, Start Mission,
  a second copy with Start Client, Connect to Cosmos Server, the ship-and-console screen,
  Helm, the handheld, the Quest Log. GAME_RESULTS_SAVE was false; nobody played. The
  mission list is the DEVELOPER'S (long, with two "Legendary Missions" lines and missions a
  player does not have); the version reads 1.3.14, not 1.4.0.
- The stills old_board_* (the boarding party) were NOT taken for this lecture. They are
  real screenshots of the game from 2026-10-03, kept in the scratch folder by the session
  that built that feature: "shown, not played". What the page describes and no still
  shows (two consoles side by side, the Warlord arriving) is a card in the page's words.
- REWORK 2026-10-14 (say what the crew sees). The ruin is now The Voice, from Storm's
  Beacon (relics/voice.amd, `Walls: torgoth, plates`), map `stormsbeacon_voice` ("Test:
  The Voice (relic)"), run from a SANDBOX COPY of Storm's Beacon only (it rewrites the
  slot-1 save), GAME_RESULTS_SAVE false, EXTRA_SHIP_DATA on: the vo_* stills, taken
  2026-10-14. The older ruin stills (old_ruin_*) and their card are gone. Stop 6 gains three
  game stills from Lecture 11's finished example (g_close_*, g_tug_helm), taken 2026-10-14.
  v_voice_* open StormsBeacon/relics/voice.amd, which the stand-in needs a copy of.
- VS Code is real: the two files of Legendary Missions in the stand-in's copy of it, and
  Lecture 11's finished mission. File Explorer is real.
"""
LECTURE = "c1-01-what-you-are-going-to-build"
TITLE = ("Class 1, Lecture 1", "What you are going to build", "A quest, a boss, a boarding party and a ruin")
MISSION = "MyMission"
FILE = "mission.amd"
MAST = "story.mast"

STATES = {
    # the mission as Class 1 ends: Lecture 11's finished files, and the five the template made
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c1-05-the-shape-of-a-record/example", "c1-07-roles-and-signals/example",
                       "c1-08-first-quest/example", "c1-09-chains-and-trees/example",
                       "c1-10-things-quests-point-at/example", "c1-11-just-enough-mast/example"),
              "same_as": ("c1-11-just-enough-mast/example/mission.amd", "c1-11-just-enough-mast/example/story.mast")},
}

_LM = {"folder": "LegendaryMissions", "side": False}
_SB = {"folder": "StormsBeacon", "side": False}       # a copy in the stand-in: see the docstring

STILLS = {
    # the real game, 2026-10-06 (see the docstring)
    "g_first": ("game", "the first screen"),
    "g_choose": ("game", "Start Server: Choose Mission"),
    "g_row": ("game", "Legendary Missions selected"),
    "g_siege": ("game", "Legendary Missions' start screen: Siege, Options, Start Mission"),
    "g_bosslist": ("game", "the Boss list open"),
    "g_warlord": ("game", "Boss set to Warlord"),
    "g_notice": ("game", "the server after Start Mission: the notice"),
    "g_client": ("game", "a second copy, Start Client: Detected game server list"),
    "g_consoles": ("game", "the ship-and-console screen"),
    "g_helm_sel": ("game", "Helm selected"),
    "g_helm": ("game", "the Helm console, Siege under way"),
    "g_padd": ("game", "the handheld"),
    "g_quests": ("game", "the Quest Log: four lines under Game, two under Ship"),
    "g_break": ("game", "Break the Siege selected"),
    # real, older, not taken for this lecture (see the docstring)
    "old_board_tile": ("game", "the Boarding Party tile: BEAM DOWN (2026-10-03)"),
    "old_board_room": ("game", "a console as a handheld: Chief Okoro, engineering, a room (2026-10-03)"),
    # The Voice, from Storm's Beacon (see the docstring): taken 2026-10-14
    "vo_arrive": ("game", "The Voice (Storm's Beacon, map stormsbeacon_voice, sandbox copy): the main screen as the ship arrives, the station ahead in its purple cloud"),
    "vo_throat": ("game", "The Voice: Helm, the ship flying up to the docking throat (the way in, the mouth)"),
    "vo_inside": ("game", "The Voice: the main screen inside one of the boxes (the concourse or the freight hall): the Torgoth kit walls, floor, trim and corner pillars"),
    "vo_suit": ("game", "The Voice: a console's handheld near the way in, the Boarding Party app offering SUIT UP"),
    # Lecture 11's finished example, in the game: taken 2026-10-14
    "g_close_log": ("game", "Salvage Run (c1-11 example), the Quest Log on Helm's handheld: Close Inspection selected, Active; the pane shows Reward 100 credits, 'Close to within 500 of the hulk' and the body"),
    "g_close_done": ("game", "the same Quest Log after the ship is inside 500 of the hulk: Close Inspection Done"),
    "g_tug_helm": ("game", "Salvage Run, Helm's map about 20 s after Wait for the Tug starts: the contact Salvage Tug"),
    # VS Code, real
    "v_break": ("vscode", None, 16, "big", dict(_LM, file="maps\\siege_quests.amd")),
    "v_warlord": ("vscode", None, 10, "big", dict(_LM, file="maps\\bosses\\warlord.amd")),
    "v_close": ("vscode", "start", 66, "big", {"side": False}),
    "v_card": ("vscode", "start", 105, "big", {"file": MAST, "side": False}),
    "v_voice_walls": ("vscode", None, 121, "big", dict(_SB, file="relics\\voice.amd")),
    "v_voice_box": ("vscode", None, 146, "big", dict(_SB, file="relics\\voice.amd")),
    # File Explorer, real
    "x_mission": ("explorer", "data\\missions\\MyMission", {"state": "start"}),
    # drawn
    "card_title": ("card", "title", {}),
    "card_boss": ("card", "points", {"kicker": "The Warlord arrives (from the page; not captured)", "items": [
        "A boss does not come at the start. The Warlord waits until the crew has destroyed three raiders in every four.",
        "Then the flagship arrives with her fleets.",
        "A new quest joins the list: **Defeat the Warlord**, worth 500 credits."]}),
    "card_two": ("card", "points", {"kicker": "Two of the crew in one room (from the page; not captured)", "items": [
        "A second crew member, at another console, is in the same room and has different buttons.",
        "The surgeon is offered things the engineer is not.",
        "When the party returns to the ship, every console goes back to its station by itself."]}),
    "card_classes": ("card", "table", {"heading": "Stop 7 - The six classes", "kicker": "Six classes"}),
    "card_exercise": ("card", "table", {"heading": "Exercise", "kicker": "Your turn: play ten minutes of Siege"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 2", "sub": "Files, folders and the command prompt"}),
}

# on the game's windows (fractions of the 4:3 picture), from the screenshots
_BUTTONS = ("rect", 0.02, 0.855, 0.44, 0.99)
_B_SERVER = ("rect", 0.02, 0.855, 0.16, 0.99)
_B_CLIENT = ("rect", 0.16, 0.855, 0.30, 0.99)
_LM_ROW = ("rect", 0.035, 0.188, 0.81, 0.25)
_INIT = ("rect", 0.86, 0.92, 1.0, 1.0)
_SIEGE = ("rect", 0.02, 0.30, 0.49, 0.52)
_OPTIONS = ("rect", 0.505, 0.345, 0.99, 0.945)
_START = ("rect", 0.0, 0.948, 1.0, 1.0)
_BOSS = ("rect", 0.535, 0.505, 0.97, 0.55)
_BOSS_LIST = ("rect", 0.648, 0.348, 0.97, 0.515)
_CONNECT = ("rect", 0.017, 0.105, 0.685, 0.162)
_CONSOLES = ("rect", 0.5, 0.155, 0.97, 0.87)
_C_HELM = ("rect", 0.5, 0.185, 0.97, 0.25)
_C_SOME = [("rect", 0.5, 0.185, 0.97, 0.325), ("rect", 0.5, 0.42, 0.97, 0.48)]
_C_MORE = [("rect", 0.5, 0.335, 0.97, 0.405), ("rect", 0.5, 0.495, 0.97, 0.56)]
_READY = ("rect", 0.80, 0.92, 0.99, 0.99)
_Q_FOUR = ("rect", 0.0, 0.145, 0.38, 0.43)
_Q_THREE = ("rect", 0.0, 0.218, 0.38, 0.43)
_Q_TILE = ("rect", 0.0, 0.395, 0.32, 0.56)
_BEAM = ("rect", 0.02, 0.215, 0.98, 0.29)
_ROOM_BAR = ("rect", 0.0, 0.055, 0.98, 0.135)
_ROOM_TEXT = ("rect", 0.0, 0.2, 0.98, 0.295)
_VO_STATION = ("rect", 0.27, 0.0, 0.785, 0.69)          # vo_arrive: the dark station ahead
_VO_MOUTH = ("rect", 0.575, 0.497, 0.66, 0.53)          # vo_throat: the label "the mouth" on Helm's map
_VO_SUIT = ("rect", 0.02, 0.235, 0.98, 0.292)           # vo_suit: the SUIT UP button
_CLOSE_ROW = ("rect", 0.025, 0.36, 0.38, 0.43)          # g_close_log: Close Inspection, Active
_CLOSE_PANE = ("rect", 0.385, 0.075, 0.99, 0.452)       # g_close_log / g_close_done: State to the last line
_CLOSE_DONE_ROW = ("rect", 0.025, 0.503, 0.38, 0.573)   # g_close_done: Close Inspection, Done
_CLOSE_STATE = ("rect", 0.385, 0.075, 0.58, 0.108)      # g_close_done: State Done

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "g_break"},
        {"from": 1, "still": "g_warlord", "marks": [_BOSS]},
        {"from": 2, "still": "old_board_room"},
        {"from": 3, "still": "vo_arrive"},
        {"from": 4, "still": "v_break", "marks": [("lines", 16, 24)]},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_what_the_game_is": {"step": None, "beats": [
        {"from": 0, "still": "g_first"},
        {"from": 1, "still": "g_notice"},
        {"from": 2, "still": "g_consoles", "marks": [_CONSOLES]},
        {"from": 3, "still": "g_consoles", "marks": _C_SOME},
        {"from": 4, "still": "g_consoles", "marks": _C_MORE},
        {"from": 5, "still": "g_helm"},
        {"from": 6, "still": "g_choose"},
        {"from": 7, "still": "v_break"},
    ]},
    "s03_stop_1_start_it_and_choose_s": {"step": None, "beats": [
        {"from": 0, "still": "g_first"},
        {"from": 2, "still": "g_first", "marks": [_BUTTONS]},
        {"from": 3, "still": "g_first", "marks": [_B_SERVER]},
        {"from": 4, "still": "g_choose"},
        {"from": 5, "still": "g_row", "marks": [_LM_ROW]},
        {"from": 6, "still": "g_row", "marks": [_INIT]},
        {"from": 7, "still": "g_siege", "marks": [_SIEGE]},
        {"from": 8, "still": "g_row", "marks": [_LM_ROW]},
        {"from": 9, "still": "g_siege", "marks": [_SIEGE]},
        {"from": 10, "still": "g_siege", "marks": [_START]},
        {"from": 11, "still": "g_notice"},
        {"from": 12, "still": "g_first", "marks": [_B_CLIENT]},
        {"from": 13, "still": "g_client", "marks": [_CONNECT]},
        {"from": 13.35, "still": "g_helm_sel", "marks": [_C_HELM, _READY]},
        {"from": 13.75, "still": "g_helm"},
    ]},
    "s04_stop_2_the_quest": {"step": None, "beats": [
        {"from": 0, "still": "g_padd", "marks": [_Q_TILE]},
        {"from": 0.5, "still": "g_quests"},
        {"from": 1, "still": "g_quests", "marks": [_Q_FOUR]},
        {"from": 2, "still": "g_quests", "marks": [_Q_THREE]},
        {"from": 4, "still": "v_break", "marks": [("lines", 16, 24)]},
        {"from": 5, "still": "v_break", "marks": [("text", 16, "[Break the Siege]")]},
        {"from": 6, "still": "v_break", "marks": [("lines", 24, 24)]},
        {"from": 7, "still": "g_break"},
        {"from": 8, "still": "v_break", "marks": [("lines", 21, 21)]},
        {"from": 9, "still": "v_break", "marks": [("lines", 16, 24)]},
        {"from": 10, "still": "g_break"},
    ]},
    "s05_stop_3_the_boss": {"step": None, "beats": [
        {"from": 0, "still": "g_siege"},
        {"from": 1, "still": "g_bosslist", "marks": [_BOSS_LIST]},
        {"from": 2, "still": "g_warlord", "marks": [_BOSS]},
        {"from": 3, "still": "card_boss", "marks": [("part", "item1")]},
        {"from": 5, "still": "card_boss", "marks": [("part", "item2"), ("part", "item3")]},
        {"from": 6, "still": "v_warlord", "marks": [("lines", 6, 16)]},
        {"from": 7, "still": "v_warlord", "marks": [("lines", 10, 10)]},
        {"from": 8, "still": "v_warlord", "marks": [("lines", 12, 12), ("lines", 14, 14)]},
        {"from": 9, "still": "v_warlord", "marks": [("lines", 6, 16)]},
        {"from": 10, "still": "g_bosslist", "marks": [_BOSS_LIST]},
    ]},
    "s06_stop_4_the_boarding_party": {"step": None, "beats": [
        {"from": 0, "still": "old_board_tile"},
        {"from": 2, "still": "old_board_tile", "marks": [_BEAM]},
        {"from": 3, "still": "old_board_room", "marks": [_ROOM_BAR]},
        {"from": 4, "still": "old_board_room", "marks": [_ROOM_TEXT]},
        {"from": 5, "still": "card_two"},
        {"from": 6, "still": "card_two", "marks": [("part", "item1")]},
        {"from": 7, "still": "card_two", "marks": [("part", "item2")]},
        {"from": 8, "still": "old_board_room"},
        {"from": 9, "still": "card_classes", "marks": [("part", "r3")]},
    ]},
    "s07_stop_5_the_ruin": {"step": None, "beats": [
        {"from": 0, "still": "vo_arrive"},
        {"from": 3, "still": "vo_arrive", "marks": [_VO_STATION]},
        {"from": 4, "still": "vo_throat", "marks": [_VO_MOUTH]},
        {"from": 5, "still": "vo_inside"},
        {"from": 6, "still": "vo_suit", "marks": [_VO_SUIT]},
        {"from": 8, "still": "v_voice_box", "marks": [("lines", 143, 149)]},
        {"from": 9, "still": "v_voice_box", "marks": [("lines", 146, 146)]},
        {"from": 10, "still": "v_voice_walls", "marks": [("lines", 125, 125)]},
        {"from": 11, "still": "vo_inside"},
        {"from": 12, "still": "vo_arrive"},
        {"from": 13, "still": "card_classes", "marks": [("part", "r4")]},
    ]},
    "s08_stop_6_a_mission_is_three_th": {"step": None, "beats": [
        {"from": 0, "still": "x_mission"},
        {"from": 1, "still": "x_mission", "marks": [("part", "rows")]},
        {"from": 2, "still": "x_mission", "marks": [("part", "row:__lib__.json"), ("part", "row:description.yaml"),
                                                   ("part", "row:script.py"), ("part", "row:settings.yaml"),
                                                   ("part", "row:story.json")]},
        {"from": 3, "still": "x_mission", "marks": [("part", "row:mission.amd"), ("part", "row:story.mast")]},
        {"from": 4, "still": "v_close"},
        {"from": 5, "still": "g_close_log", "marks": [_CLOSE_ROW]},
        {"from": 6, "still": "g_close_log", "marks": [_CLOSE_PANE]},
        {"from": 7, "still": "g_close_done", "marks": [_CLOSE_DONE_ROW, _CLOSE_STATE]},
        {"from": 9, "still": "v_close"},
        {"from": 10, "still": "v_close", "marks": [("lines", 61, 61)]},
        {"from": 10.5, "still": "v_close", "marks": [("lines", 62, 71)]},
        {"from": 11, "still": "v_close", "marks": [("lines", 72, 72)]},
        {"from": 12, "still": "v_close", "marks": [("lines", 66, 66)]},
        {"from": 14, "still": "v_card"},
        {"from": 15, "still": "g_tug_helm"},
        {"from": 17, "still": "v_card", "marks": [("lines", 108, 115)]},
        {"from": 18, "still": "v_card", "marks": [("lines", 111, 112)]},
        {"from": 19, "still": "v_card", "marks": [("lines", 113, 114)]},
        {"from": 20, "still": "v_card", "marks": [("lines", 108, 115)]},
    ]},
    "s09_stop_7_the_six_classes": {"step": None, "beats": [
        {"from": 0, "still": "card_classes"},
        {"from": 1, "still": "card_classes", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_classes", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_classes", "marks": [("part", "r3"), ("part", "r4"), ("part", "r5")]},
        {"from": 4, "still": "card_classes", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 5, "still": "card_classes", "marks": [("part", "r5")]},
        {"from": 6, "still": "card_classes", "marks": [("part", "r6")]},
        {"from": 7, "still": "card_classes"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "g_helm"},
        {"from": 1, "still": "card_exercise"},
        {"from": 3, "still": "card_exercise", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 4, "still": "card_next"},
    ]},
}
