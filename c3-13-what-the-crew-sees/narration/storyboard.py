"""Storyboard for c3-13-what-the-crew-sees: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

The lecture starts from Lecture 12's finished files in MyAway ("start"). Four files change:
the three maps (marks renamed, "m2"; two titles, "m3") and mission.amd (item keys and two
headings "m4", three Scan lines "m5", three quest headings "m6", two side stories "m7" and
their answers "m7b", the bridge's briefing "final", the page's own example\\ files).

THE GROUND IS LAID FLAT, as in Lecture 12's storyboard: the tool reads one folder level, so
ground\\ files are written beside mission.amd (`sbs lint` prints the same either way). No
still shows the Side Bar. The maps are shown as TEXT, as the page asks ("press Text"): the
stills open .tiles files with the plain text editor (`workbench.editorAssociations`), so the
Tile Map Editor is not in them.

GAME STILLS. Not taken yet; no marks until the screenshots exist. This lecture is mostly the
game. game.py cannot start this mission (it makes its probe from the `amd` template and
copies only mission.amd and story.mast). Build a real MyAway folder for the state, WITH its
ground\\ folder (Lecture 7's example\\ with the example\\ folders of Lectures 8 to 12 laid
over it, subfolders included; for "final" add Lecture 13's), `sbs fetch MyAway
--update-libs` once, and run `sbs run server,science,helm -m MyAway map=0` with
COSMOS_SETTINGS '{"GAME_RESULTS_SAVE": false}'. THREE windows: the server, Science (Dr Ines
Hale, medical and science) and Helm (Lt Dana Ross). To go down: the handheld icon (top
left), the Boarding Party tile, BEAM DOWN. The device's first screen is its tile sheet;
a tile opens an app, Back closes it.

GAME ONE, state "start" (Lecture 12's files), about eight minutes:
  1. Science: beam down. On the pad, the tile sheet: game_l13_tiles (its bar reads Dr Ines
     Hale, medical, science, pad). Open each tile once and Back: game_l13_crew,
     game_l13_act, game_l13_look, game_l13_pack, game_l13_tasks_hale_before (The
     Caretaker's Cough), game_l13_beam, game_l13_scan, game_l13_fire.
  2. Helm: beam down. Tasks: game_l13_tasks_ross_before. Ross walks to Old Marrow (by the
     tent) while Hale stays on the pad; talk to him: game_l13_marrow_ross. Leave him to
     his kettle, and walk Ross back to the pad.
  3. Hale: click the scrub cell left of the pad's bottom row (the kit's cell, 6,8; click
     the ground, nothing is there yet): game_l13_bar_hidden. Then talk to Marrow (Ross
     away from him): game_l13_marrow_hale. Ask what he has put by. Back to the kit's cell
     (click beside the kit and then onto it, without using it): game_l13_bar_scrub.
  4. Hale: Scan, in the yard near the tent: game_l13_scan_before.
  5. Hale: pick up the brass key on the tent peg. Walk east off the yard (the right edge,
     row 6) into the gully: game_l13_bar_arrive. Pick up the Toolbox (east of the pump
     house): Act, game_l13_act_toolbox; Pack, game_l13_pack_before.
  6. Hale: Look, Go to Kesh Relay. In the yard, Look: game_l13_look_before; Beam:
     game_l13_beam_before.
  7. Ross: Crew, Beam up. On Helm the handheld icon, Boarding Party: game_l13_bp. Then
     Hale: Crew, Report in. Ross: Messages, game_l13_messages; Quests, game_l13_questlist;
     Relight Kesh Relay selected, game_l13_log_relight_old.
GAME TWO, state "final", about five minutes:
  1. Both beam down. Hale's bar on the pad: game_l13_bar_landing_pad. Tasks, both:
     game_l13_tasks_hale_after, game_l13_tasks_ross_after. Hale's Scan by the tent:
     game_l13_scan_after.
  2. Hale: the brass key, east into the gully: game_l13_bar_gully_mouth. The Toolbox; Pack:
     game_l13_pack_after. Look, Go to Kesh Relay; Look: game_l13_look_after.
  3. Ross: Crew, Beam up. Quests, Relight Kesh Relay: game_l13_log_relight.
"""
import os as _os

LECTURE = "c3-13-what-the-crew-sees"
TITLE = ("Class 3, Lecture 13", "What the crew sees", "Your mission, read from the handheld")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_COURSES = _os.path.dirname(_HERE)


def _read(*parts):
    with open(_os.path.join(_COURSES, *parts), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_GROUND = [("write", "starter.tileset", _read("c3-09-tile-map-editor-part-2", "example", "ground", "starter.tileset")),
           ("write", "landing.tiles", _read("c3-09-tile-map-editor-part-2", "example", "ground", "landing.tiles")),
           ("write", "cistern.tiles", _read("c3-10-props", "example", "ground", "cistern.tiles")),
           ("write", "gully.tiles", _read("c3-11-people-and-hostiles", "example", "ground", "gully.tiles"))]

_FINAL = _read(LECTURE, "example", "mission.amd")


def _cut(a, b):
    i = _FINAL.index(a)
    return _FINAL[i:_FINAL.index(b, i)]


_EX = LECTURE + "/example"
_STORIES = _cut("### [Find a Place to Set Down](strip)", "\n// ---- Props")
_CALL_ROOM = _cut("### [The Last Call](terminal_call)", "### [Nine Days](terminal_log)")
_STRIP_ROOM = _cut("### [The Old Strip](marrow_strip)", "### [The Keycard](marrow_key)")
_BRIEF = _cut("![](ship://starbase_civil)", "// `reach relay 6000`")
_UPDATE = "- [Send the sentry its recognition update](terminal_update) if learned codes ; calm sentry\n"
_SHOW = "- [Show him the brass key](marrow_pump) if party pump_house_key\n"

STATES = {
    # Lecture 12's finished files
    "start": {"folder": "c3-07-anatomy-of-a-long-away-mission/example",
              "over": ("c3-09-tile-map-editor-part-2/example", "c3-10-props/example",
                       "c3-11-people-and-hostiles/example", "c3-12-scenes-on-the-ground/example"),
              "edits": _GROUND},
    # Step 2: marks named for the place
    "m2": {"base": "start", "edits": [
        ("replace", "landing.tiles", "entry: pad\n", "entry: landing_pad\n"),
        ("replace", "landing.tiles", "  P: pad @pad\n", "  P: pad @landing_pad\n"),
        ("replace", "gully.tiles", "entry: arrive\n", "entry: gully_mouth\n"),
        ("replace", "gully.tiles", "  a: dust @arrive\n", "  a: dust @gully_mouth\n"),
        ("replace", "gully.tiles", "  to_cistern: cistern @foot\n", "  to_cistern: cistern @foot_of_the_stairs\n"),
        ("replace", "cistern.tiles", "entry: foot\n", "entry: foot_of_the_stairs\n"),
        ("replace", "cistern.tiles", "  f: floor @foot\n", "  f: floor @foot_of_the_stairs\n")]},
    # Step 3: two titles. The three maps are now the page's own.
    "m3": {"base": "m2", "edits": [
        ("replace", "gully.tiles", "title: The Dry Gully\n", "title: Dry Gully\n"),
        ("replace", "cistern.tiles", "title: The Cistern\n", "title: Pump House Cistern\n")],
        "same_as": (_EX + "/ground/landing.tiles", _EX + "/ground/gully.tiles", _EX + "/ground/cistern.tiles")},
    # Step 4: item keys the same words as the headings, and two headings
    "m4": {"base": "m3", "edits": [
        ("replace", FILE, "Opens with: key relay_key,", "Opens with: key relay_keycard,"),
        ("replace", FILE, "Using it puts `relay_key` in", "Using it puts `relay_keycard` in"),
        ("replace", FILE, "Item: relay_key\n", "Item: relay_keycard\n"),
        ("replace", FILE, "Item: pump_key\n", "Item: pump_house_key\n"),
        ("replace", FILE, "Opens with: key pump_key,", "Opens with: key pump_house_key,"),
        ("replace", FILE, "if party pump_key\n", "if party pump_house_key\n"),
        ("replace", FILE, "### [Toolbox](toolbox)", "### [Two fuses](toolbox)"),
        ("replace", FILE, "### [Pim's stash](stash)", "### [Pim's medical kit](stash)")]},
    # Step 5: scenery gets a Scan line
    "m5": {"base": "m4", "edits": [
        ("replace", FILE, "Mark: tent\nSprite: prop:tent\nBlocks: yes\n",
         "Mark: tent\nSprite: prop:tent\nBlocks: yes\nScan: Canvas, a camp bed, and a kettle that is still warm.\n"),
        ("replace", FILE, "Sprite: prop:machinery\nBlocks: yes\n",
         "Sprite: prop:machinery\nBlocks: yes\nScan: A two stage pump. No power to it, and nothing wrong with it.\n"),
        ("replace", FILE, "Sprite: prop:crate\nBlocks: yes\n",
         "Sprite: prop:crate\nBlocks: yes\nScan: Empty. Somebody has been using it as a seat.\n")]},
    # Step 6: on the ground a title is the whole task
    "m6": {"base": "m5", "edits": [
        ("replace", FILE, "### [The Caretaker's Cough](cough)", "### [See to Marrow's Cough](cough)"),
        ("replace", FILE, "### [The Thing in the Sump](sump)", "### [Clear the Cistern Walkway](sump)"),
        ("replace", FILE, "### [Pim's Tablet](pim_tablet)", "### [Bring Pim Her Tablet](pim_tablet)")]},
    # Step 7: two stories (lint warns twice), then their answers
    "m7": {"base": "m6", "edits": [("replace", FILE, "has been at the pump lines.\n\n",
                                    "has been at the pump lines.\n\n" + _STORIES)]},
    "m7b": {"base": "m7", "edits": [
        ("replace", FILE, _UPDATE, _UPDATE + "- [Play back the last call it sent](terminal_call) if comms ; signal last_call_heard\n"),
        ("replace", FILE, "### [Nine Days](terminal_log)", _CALL_ROOM + "### [Nine Days](terminal_log)"),
        ("replace", FILE, _SHOW, _SHOW + "- [Ask where a shuttle could set down](marrow_strip) if helm ; signal strip_found\n"),
        ("replace", FILE, "### [The Keycard](marrow_key)", _STRIP_ROOM + "### [The Keycard](marrow_key)")]},
    # Step 9: the bridge's briefing. The page's own files.
    "final": {"base": "m7b", "edits": [
        ("replace", FILE, "The relay's beacon went dark nine days ago. Go down and light it.\n\n// `reach relay 6000`",
         _BRIEF + "// `reach relay 6000`")],
        "same_as": (_EX + "/mission.amd", _EX + "/ground/landing.tiles", _EX + "/ground/gully.tiles",
                    _EX + "/ground/cistern.tiles")},
    # Step 10: one of the three lines missed
    "b_miss": {"base": "final", "edits": [("replace", FILE, "Opens with: key pump_house_key,", "Opens with: key pump_key,")]},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}
_TEXT = {"side": False, "settings": {"workbench.editorAssociations": {"*.tiles": "default", "*.tileset": "default"}}}

STILLS = {
    # Step 2: the marks, in the three maps (as text)
    "e_land2": ("vscode", "m2", 12, "big", dict(_TEXT, file="landing.tiles")),     # lines 2 to 22: entry (12), the P line (21)
    "e_gully2": ("vscode", "m2", 12, "big", dict(_TEXT, file="gully.tiles")),      # lines 2 to 22: entry (5), the a line (16), the exit (22)
    "e_cist2": ("vscode", "m2", 9, "big", dict(_TEXT, file="cistern.tiles")),      # lines 1 to 19: entry (5), the f line (14)
    "t_m3": ("terminal", [("m3", _LINT)]),
    # Step 3: two titles
    "e_gully3": ("vscode", "m3", 12, "big", dict(_TEXT, file="gully.tiles")),      # title (3)
    "e_cist3": ("vscode", "m3", 9, "big", dict(_TEXT, file="cistern.tiles")),      # title (3)
    # Step 4: the key's three lines, and the headings
    "e_key0": ("vscode", "start", 258, "big", _NS),        # lines 248 to 268: Pump house key (248), Item: pump_key (253), the door's Opens with (264)
    "e_key4": ("vscode", "m4", 258, "big", _NS),           # the same lines after Step 4; Two fuses (270) just below
    "t_miss": ("terminal", [("b_miss", _LINT)]),
    # Step 5: a Scan line on the tent
    "e_scan5": ("vscode", "m5", 222, "big", _NS),          # lines 212 to 232: Tent (214), its Scan line (220)
    # Step 6: three headings
    "e_cough6": ("vscode", "m6", 118, "big", _NS),         # lines 108 to 128: See to Marrow's Cough (113)
    # Step 7: two stories, and their answers
    "e_stories": ("vscode", "m7", 154, "big", _NS),        # lines 144 to 164: Find a Place to Set Down (145), Hear the Last Call (155)
    "t_m7": ("terminal", [("m7", _LINT)]),
    "e_strip": ("vscode", "m7b", 525, "big", _NS),         # lines 515 to 535: Marrow's new answer (520), The Old Strip (530)
    "t_m7b": ("terminal", [("m7b", _LINT)]),
    # Step 9: the bridge's briefing
    "e_brief": ("vscode", "final", 80, "big", _NS),        # lines 70 to 90: the ship line (78), the table (82 to 86), the last line (88)
    # THE REAL GAME (not taken yet). Two games, three windows: server, Science (Dr Hale), Helm
    # (Lt Ross). Press order in the docstring.
    "game_l13_tiles": ("game", "Science's xESS just beamed down (game one, state start): the tile sheet, eight tiles with their one-line blurbs (Crew, Act, Look, Pack, Tasks, Beam, Scan, Fire), and the bar: Dr Ines Hale, medical, science, pad"),
    "game_l13_crew": ("game", "Science's xESS, the Crew app on the pad: the ship, each person down and where they stand, Everyone, and the buttons"),
    "game_l13_act": ("game", "Science's xESS, the Act app with nothing open yet"),
    "game_l13_look": ("game", "Science's xESS, the Look app on the pad: what is in reach (likely 'Nothing within reach.'), then Further off"),
    "game_l13_pack": ("game", "Science's xESS, the Pack app on the pad, empty"),
    "game_l13_tasks_hale_before": ("game", "Science's xESS, the Tasks app (state start): Dr Ines Hale, The Caretaker's Cough, Active, then the party's quests and Leads ('! Old Marrow - Kesh Relay')"),
    "game_l13_beam": ("game", "Science's xESS, the Beam app on the pad: To Kesh Relay"),
    "game_l13_scan": ("game", "Science's xESS, the Scan app on the pad"),
    "game_l13_fire": ("game", "Science's xESS, the Fire app: SAFE, the three settings STUN, CUT, FULL, and Arm"),
    "game_l13_tasks_ross_before": ("game", "Helm's xESS (Lt Ross), the Tasks app (state start): no story of her own, Party with Relight Kesh Relay and Hold at the Relay, and Leads"),
    "game_l13_marrow_ross": ("game", "Helm's xESS, Act, Lt Ross talking to Old Marrow while Dr Hale stands on the landing pad: the answers, one of them 'Look at that cough (covering for medical)'"),
    "game_l13_marrow_hale": ("game", "Science's xESS, Act, Dr Hale talking to Old Marrow with Lt Ross away: 'Look at that cough' with no covering mark"),
    "game_l13_bar_hidden": ("game", "Science's xESS, Dr Hale standing on the scrub cell where the medical kit is hidden, before Marrow has told of it: the bar's third slot reads Kesh Relay"),
    "game_l13_bar_scrub": ("game", "Science's xESS, Dr Hale on the same cell after Ask what he has put by: the kit drawn there now, and the bar reads scrub"),
    "game_l13_scan_before": ("game", "Science's xESS, Scan in the yard by the tent (state start): '**Tent** - no reading', then Old Marrow with his Scan line"),
    "game_l13_bar_arrive": ("game", "Science's xESS, Dr Hale just walked into the gully (state start): the bar reads Dr Ines Hale, medical, science, arrive"),
    "game_l13_act_toolbox": ("game", "Science's xESS, Act after picking up the brass key and the toolbox: the transcript lines 'Dr Ines Hale picked up Pump house key.' and 'Dr Ines Hale picked up Toolbox.'"),
    "game_l13_pack_before": ("game", "Science's xESS, Pack after the key and the toolbox (state start): fuse x2, pump key x1"),
    "game_l13_look_before": ("game", "Science's xESS, Look back in the yard after the gully was found (state start): 'Go to The Dry Gully' among the buttons"),
    "game_l13_beam_before": ("game", "Science's xESS, Beam in the yard (state start): 'To The Dry Gully'"),
    "game_l13_bp": ("game", "Helm, beamed back up (Crew, Beam up): its handheld's Boarding Party screen: 'Going down to Kesh Relay', Lt Dana Ross, helm, In the party, Dr Ines Hale, medical, science, BEAM DOWN"),
    "game_l13_messages": ("game", "Helm's handheld, Messages, after Dr Hale presses Report in on her Crew app: the one line 'Dr Ines Hale, reporting in.'"),
    "game_l13_questlist": ("game", "Helm's handheld, the Quest Log list: Relight Kesh Relay Active, Hold at the Relay Done, and nothing of anybody's side story"),
    "game_l13_log_relight_old": ("game", "Helm's Quest Log, Relight Kesh Relay selected (state start): its one sentence, 'The relay's beacon went dark nine days ago. Go down and light it.'"),
    "game_l13_bar_landing_pad": ("game", "Science's xESS just beamed down (game two, state final): the bar reads Dr Ines Hale, medical, science, landing pad"),
    "game_l13_tasks_hale_after": ("game", "Science's xESS, Tasks (state final): See to Marrow's Cough, Active, and its lead"),
    "game_l13_tasks_ross_after": ("game", "Helm's xESS, Tasks (state final): Lt Dana Ross, Find a Place to Set Down, Active"),
    "game_l13_scan_after": ("game", "Science's xESS, Scan by the tent (state final): '**Tent** - Canvas, a camp bed, and a kettle that is still warm.'"),
    "game_l13_bar_gully_mouth": ("game", "Science's xESS, Dr Hale just walked into the gully (state final): the bar reads gully mouth"),
    "game_l13_pack_after": ("game", "Science's xESS, Pack after the key and the toolbox (state final): fuse x2, pump house key x1"),
    "game_l13_look_after": ("game", "Science's xESS, Look back in the yard (state final): 'Go to Dry Gully'"),
    "game_l13_log_relight": ("game", "Helm's Quest Log, Relight Kesh Relay selected (state final): the station picture with 'Kesh Relay, the only light on the Kesh run.', the sentence, the three-row table What / What the ship knows, and 'Every convoy on the Kesh run steers by that lamp.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_apps": ("card", "table", {"heading": "The eight apps", "kicker": "Which of your words each app shows"}),
    "card_offered": ("card", "table", {"heading": "Who is offered what", "kicker": "Who is offered what"}),
    "card_key": ("card", "rows", {"kicker": "Three lines name the pump house key", "header": ["In the record", "The line"],
                                  "rows": [["Pump house key", "Item: pump_house_key"],
                                           ["Pump house door", "Opens with: key pump_house_key, check engineering 8, cut"],
                                           ["Old Marrow", "- [Show him the brass key](marrow_pump) if party pump_house_key"]]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Play it to read"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 14", "sub": "Pacing an away mission"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l13_tiles"},
        {"from": 5, "still": "game_l13_bar_arrive"},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_the_bar_and_the_eight_apps": {"step": 1, "beats": [
        {"from": 0, "still": "game_l13_tiles"},
        {"from": 3, "still": "game_l13_crew"},
        {"from": 4, "still": "game_l13_act"},
        {"from": 5, "still": "game_l13_look"},
        {"from": 6, "still": "game_l13_pack"},
        {"from": 7, "still": "game_l13_tasks_hale_before"},
        {"from": 8, "still": "game_l13_beam"},
        {"from": 8.5, "still": "game_l13_fire"},
        {"from": 9, "still": "card_apps"},
        {"from": 10, "still": "card_apps", "marks": [("part", "r1c3"), ("part", "r2c3"), ("part", "r3c3"), ("part", "r4c3")]},
    ]},
    "s03_who_is_offered_what": {"step": None, "beats": [
        {"from": 0, "still": "card_offered", "marks": [("part", "r1")]},
        {"from": 1, "still": "game_l13_marrow_hale"},
        {"from": 3, "still": "game_l13_marrow_ross"},
        {"from": 6, "still": "card_offered", "marks": [("part", "r3")]},
        {"from": 9, "still": "card_offered", "marks": [("part", "r4")]},
    ]},
    "s04_a_mark_is_a_word": {"step": 2, "beats": [
        {"from": 0, "still": "game_l13_tiles"},
        {"from": 2, "still": "game_l13_bar_arrive"},
        {"from": 5, "still": "e_land2", "marks": [("lines", 12, 12), ("lines", 21, 21)]},
        {"from": 5.5, "still": "e_gully2", "marks": [("lines", 5, 5), ("lines", 16, 16), ("lines", 22, 22)]},
        {"from": 6, "still": "e_cist2", "marks": [("lines", 5, 5), ("lines", 14, 14)]},
        {"from": 6.5, "still": "game_l13_bar_landing_pad"},
        {"from": 7, "still": "game_l13_bar_hidden"},
        {"from": 9, "still": "game_l13_bar_scrub"},
        {"from": 10, "still": "game_l13_bar_hidden"},
    ]},
    "s05_titles_and_what_the_pack_say": {"step": 3, "beats": [
        {"from": 0, "still": "game_l13_look_before"},
        {"from": 1.5, "still": "game_l13_beam_before"},
        {"from": 3, "still": "e_gully3", "marks": [("lines", 3, 3)]},
        {"from": 3.5, "still": "e_cist3", "marks": [("lines", 3, 3)]},
        {"from": 4, "still": "game_l13_act_toolbox"},
        {"from": 6, "still": "game_l13_pack_before"},
        {"from": 8, "still": "e_key0", "marks": [("lines", 248, 248)]},
        {"from": 9, "still": "game_l13_pack_before"},
        {"from": 10, "still": "e_key0", "marks": [("lines", 253, 253)]},
        {"from": 11, "still": "e_key4", "marks": [("lines", 248, 248), ("lines", 253, 253)]},
        {"from": 12, "still": "card_key"},
        {"from": 14, "still": "t_miss", "marks": [("span", 1, "item-nothing-gives")]},
    ]},
    "s06_scan_and_a_title_that_is_the": {"step": 5, "beats": [
        {"from": 0, "still": "game_l13_scan_before"},
        {"from": 2, "still": "e_scan5", "marks": [("lines", 220, 220)]},
        {"from": 3, "still": "game_l13_scan_after"},
        {"from": 4, "still": "game_l13_tasks_hale_before"},
        {"from": 7, "still": "e_cough6", "marks": [("lines", 113, 113)]},
        {"from": 8, "still": "game_l13_tasks_hale_after"},
    ]},
    "s07_the_two_with_nothing_to_do": {"step": 7, "beats": [
        {"from": 0, "still": "game_l13_tasks_ross_before"},
        {"from": 2, "still": "game_l13_marrow_ross"},
        {"from": 4, "still": "e_stories", "marks": [("lines", 145, 163)]},
        {"from": 6, "still": "t_m7", "marks": [("span", 1, "unfired-signal")]},
        {"from": 7, "still": "e_strip", "marks": [("lines", 520, 520)]},
        {"from": 7.5, "still": "game_l13_tasks_ross_after"},
    ]},
    "s08_what_the_bridge_sees_and_you": {"step": 9, "beats": [
        {"from": 0, "still": "game_l13_bp"},
        {"from": 3, "still": "game_l13_questlist"},
        {"from": 4, "still": "game_l13_messages"},
        {"from": 6, "still": "game_l13_questlist"},
        {"from": 9, "still": "game_l13_log_relight_old"},
        {"from": 12, "still": "e_brief", "marks": [("lines", 78, 88)]},
        {"from": 13, "still": "game_l13_log_relight"},
        {"from": 15, "still": "card_exercise"},
        {"from": 18, "still": "card_next"},
    ]},
}
