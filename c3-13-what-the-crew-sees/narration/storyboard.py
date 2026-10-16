"""Storyboard for c3-13-what-the-crew-sees: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

The lecture starts from Lecture 12's finished files in MyAway ("start"). Four files change:
the three maps (marks renamed, "m2"; two titles, "m3") and mission.amd (item keys and two
headings "m4", three Scan lines "m5", three quest headings "m6", two side stories "m7" and
their answers "m7b", the bridge's briefing "final", the page's own example\\ files).

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders). The close views hide the Side Bar, as every close view of this class
does. The maps are shown as TEXT, as the page asks ("press Text"): capture opens a file at a
line, which is the text editor.

GAME STILLS. Taken 2026-10-16 (engine 1.3.15, sbs_utils 7ea2c918), all 32; marks set from
them. What they showed: the handheld's first screen is a LIST of eight full-width rows (Crew,
Act, Look, Pack, Tasks, Beam, Scan, Fire), not tiles; Tasks is a list with the picked quest's
page under it (State, the objective, the text, Leads); Beam on the pad reads `No other site
has a lock yet.`; Messages holds the crew's home mail (`Sam`, `Mum`) under the Report in
line; a pickup read `picked up pump key from the Pump house key.` (since 19c038f9 it names
the prop: `picked up Pump house key.`, `picked up Toolbox (fuse x2).`); Scan by the tent lists
the key and the kit too (the kit once Marrow has told of it); Marrow's cough answer is
covered whenever the medic is not BESIDE him (Hale was on the pad, six cells off).

RE-SHOOT (owner decision 2026-10-16: the bar's third slot NAMES THE MARK you stand on, and
the library is being put back to that). 7ea2c918 showed the AREA TITLE there, so these six
show the wrong word in the bar and are captioned for the mark: game_l13_tiles (pad),
game_l13_bar_hidden (Kesh Relay, right for the hidden kit, but for the wrong reason),
game_l13_bar_scrub (scrub), game_l13_bar_arrive (arrive), game_l13_bar_landing_pad (landing
pad), game_l13_bar_gully_mouth (gully mouth). Their rects box the bar's third slot and stay
right after the re-shoot. AWAITING RE-SHOOT (library defect being fixed):
game_l13_tasks_ross_after, whose page text breaks mid-sentence (`somebody will` / `have to
fly a new one down.`); captioned for the whole sentence. AWAITING RE-SHOOT (19c038f9, a
pickup names the PROP): game_l13_act_toolbox, which shows 7ea2c918's `picked up pump key
from the Pump house key.` / `picked up fuse x2 from the Toolbox.`; captioned for
`picked up Pump house key.` / `picked up Toolbox (fuse x2).` (game one, step 5).

`python game.py c3-13-what-the-crew-sees start --state start --consoles server,science,helm`
(game one) and `--state final` (game two): the probe is made from the `away` template with
every file of the state laid over it, ground\\ included; GAME_RESULTS_SAVE is false. THREE
windows: the server, Science (Dr Ines Hale, medical and science) and Helm (Lt Dana Ross).
To go down: the handheld icon (top left), the Boarding Party tile (0.15, 0.24), BEAM DOWN
(0.4, 0.25 first, 0.4, 0.375 when somebody is down). The device's first screen is its list
of apps (rows at x 0.82: Crew 0.24, Act 0.34, Look 0.44, Pack 0.54, Tasks 0.64, Beam 0.74,
Scan 0.84, Fire 0.93); a row opens an app, Back (0.94, 0.16) closes it. MIND LOOK: a row of
an open Look sits where the home rows are, and a `Further off` row WALKS you to that thing,
through the sentry's square if it is in the way (game one's first run lost Hale that way).

GAME ONE, state "start" (Lecture 12's files), about eight minutes:
  1. Science: beam down. On the pad, the list: game_l13_tiles (its bar: Dr Ines Hale,
     medical, science, pad). Open each app once and Back: game_l13_crew, game_l13_act,
     game_l13_look, game_l13_pack, game_l13_tasks_hale_before (The Caretaker's Cough),
     game_l13_beam, game_l13_scan, game_l13_fire.
  2. Helm: beam down. Tasks: game_l13_tasks_ross_before. Ross walks to Old Marrow (by the
     tent) while Hale stays on the pad; talk to him: game_l13_marrow_ross. Leave him to
     his kettle, and walk Ross back to the pad.
  3. Hale: click the scrub cell left of the pad's bottom row (the kit's cell, 6,8: click
     0.25, 0.55; nothing is there yet): game_l13_bar_hidden. Then talk to Marrow (Ross
     away from him): game_l13_marrow_hale. Ask what he has put by. Back to the kit's cell
     (click beside the kit and then onto it, without using it): game_l13_bar_scrub.
  4. Hale: Scan, in the yard near the tent: game_l13_scan_before.
  5. Hale: pick up the brass key by the tent. Walk east off the yard by the path behind
     the relay house (click about 22, 0 first, never row 6, which passes three cells from
     the sentry's loop), then the exit (29, 6), into the gully: game_l13_bar_arrive. Pick
     up the Toolbox (east of the pump house): Act, game_l13_act_toolbox; Pack,
     game_l13_pack_before.
  6. Hale: Look, Go to Kesh Relay, then Back BEFORE pressing anything else. In the yard
     beside the trail sign, Look: game_l13_look_before; Beam: game_l13_beam_before.
  7. Ross: Crew, Beam up. On Helm the handheld icon, Boarding Party: game_l13_bp. Then
     Hale: Crew, Report in. Ross: Messages (0.82, 0.24 with the Boarding Party tile
     showing), game_l13_messages; Quests, game_l13_questlist; Relight Kesh Relay
     selected, game_l13_log_relight_old.
GAME TWO, state "final", about five minutes:
  1. Both beam down. Hale's bar on the pad: game_l13_bar_landing_pad. Tasks, both:
     game_l13_tasks_hale_after, game_l13_tasks_ross_after. Hale's Scan by the tent:
     game_l13_scan_after.
  2. Hale: the brass key, east into the gully by the path behind the relay house:
     game_l13_bar_gully_mouth. The Toolbox; Pack: game_l13_pack_after. Look, Go to Kesh
     Relay, Back; Look: game_l13_look_after.
  3. Ross: Crew, Beam up. Quests, Relight Kesh Relay: game_l13_log_relight.
For the re-shoot, only the six bar stills, game_l13_tasks_ross_after and
game_l13_act_toolbox are needed: game one steps 1, 3 and 5, game two steps 1 and 2.
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


LT, GT, CT = "ground/landing.tiles", "ground/gully.tiles", "ground/cistern.tiles"

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
                       "c3-11-people-and-hostiles/example", "c3-12-scenes-on-the-ground/example")},
    # Step 2: marks named for the place
    "m2": {"base": "start", "edits": [
        ("replace", LT, "entry: pad\n", "entry: landing_pad\n"),
        ("replace", LT, "  P: pad @pad\n", "  P: pad @landing_pad\n"),
        ("replace", GT, "entry: arrive\n", "entry: gully_mouth\n"),
        ("replace", GT, "  a: dust @arrive\n", "  a: dust @gully_mouth\n"),
        ("replace", GT, "  to_cistern: cistern @foot\n", "  to_cistern: cistern @foot_of_the_stairs\n"),
        ("replace", CT, "entry: foot\n", "entry: foot_of_the_stairs\n"),
        ("replace", CT, "  f: floor @foot\n", "  f: floor @foot_of_the_stairs\n")]},
    # Step 3: two titles. The three maps are now the page's own.
    "m3": {"base": "m2", "edits": [
        ("replace", GT, "title: The Dry Gully\n", "title: Dry Gully\n"),
        ("replace", CT, "title: The Cistern\n", "title: Pump House Cistern\n")],
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
_TEXT = {"side": False}                                 # a map as text, as the page has the student press Text

STILLS = {
    # Step 2: the marks, in the three maps (as text)
    "e_land2": ("vscode", "m2", 12, "big", dict(_TEXT, file=LT)),     # lines 2 to 22: entry (12), the P line (21)
    "e_gully2": ("vscode", "m2", 12, "big", dict(_TEXT, file=GT)),      # lines 2 to 22: entry (5), the a line (16), the exit (22)
    "e_cist2": ("vscode", "m2", 9, "big", dict(_TEXT, file=CT)),      # lines 1 to 19: entry (5), the f line (14)
    "t_m3": ("terminal", [("m3", _LINT)]),
    # Step 3: two titles
    "e_gully3": ("vscode", "m3", 12, "big", dict(_TEXT, file=GT)),      # title (3)
    "e_cist3": ("vscode", "m3", 9, "big", dict(_TEXT, file=CT)),      # title (3)
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
    # THE REAL GAME (taken 2026-10-16). Two games, three windows: server, Science (Dr Hale),
    # Helm (Lt Ross). Press order in the docstring. RE-SHOOT marks the six bar stills.
    "game_l13_tiles": ("game", "Science's xESS just beamed down (game one, state start): the list of eight apps, each a full-width row with its one-line blurb (Crew, Act, Look, Pack, Tasks, Beam, Scan, Fire), and the bar: Dr Ines Hale, medical, science, pad. RE-SHOOT: 7ea2c918 drew the area title, Kesh Relay, where the mark goes"),
    "game_l13_crew": ("game", "Science's xESS, the Crew app on the pad: Kesh Relay - 1 down, the rows Artemis, Dr Ines Hale (you), Everyone, 'Artemis - ship', 'Nothing said yet.', and Report in / Beam up at the foot"),
    "game_l13_act": ("game", "Science's xESS, the Act app with nothing open yet: 'Nothing to decide here.'"),
    "game_l13_look": ("game", "Science's xESS, the Look app on the pad: 'Nothing within reach.' and nothing further off yet"),
    "game_l13_pack": ("game", "Science's xESS, the Pack app on the pad: 'You are not carrying anything.'"),
    "game_l13_tasks_hale_before": ("game", "Science's xESS, the Tasks app (state start): the list, Dr Ines Hale > The Caretaker's Cough, Active, then Party; under it the page, State Active, 'See to the caretaker', the sentence; Leads '! Old Marrow - Kesh Relay', '! The beacon - Kesh Relay'"),
    "game_l13_beam": ("game", "Science's xESS, the Beam app on the pad: 'No other site has a lock yet.' (a Beam list never names the area you are in)"),
    "game_l13_scan": ("game", "Science's xESS, the Scan app on the pad: Kesh Relay, 'Nothing in sight worth a reading.'"),
    "game_l13_fire": ("game", "Science's xESS, the Fire app: SAFE, the three settings > STUN, CUT, FULL, STUN's line, Range 6 cells, Arm"),
    "game_l13_tasks_ross_before": ("game", "Helm's xESS (Lt Ross), the Tasks app (state start): no story of her own, Party with Relight Kesh Relay Active and Hold at the Relay Done, its page, and Leads '! The beacon - Kesh Relay'"),
    "game_l13_marrow_ross": ("game", "Helm's xESS, Act, Lt Ross talking to Old Marrow while Dr Hale stands on the landing pad six cells off: five answers, the last 'Look at that cough (covering for medical)'"),
    "game_l13_marrow_hale": ("game", "Science's xESS, Act, Dr Hale talking to Old Marrow with Lt Ross away: 'Look at that cough' with no covering mark, fourth of five"),
    "game_l13_bar_hidden": ("game", "Science's xESS, Dr Hale standing on the scrub cell where the medical kit is hidden, before Marrow has told of it: the bar's third slot reads Kesh Relay. RE-SHOOT: right word, but 7ea2c918 drew the area title on every cell"),
    "game_l13_bar_scrub": ("game", "Science's xESS, Dr Hale on the kit's cell after Ask what he has put by: the bar reads scrub, the cell is empty (the step picked the kit up), Marrow's line about it and 'Dr Ines Hale picked up Medical kit.' in Act (sitting 4)"),
    "game_l13_scan_before": ("game", "Science's xESS, Scan in the yard by the tent (state start, the kit already told of): Kesh Relay, '**Tent** - no reading', the Pump house key, the Medical kit, and Old Marrow, each with its line"),
    "game_l13_bar_arrive": ("game", "Science's xESS, Dr Hale one step into the gully, on the mark's cell (state start): the bar reads Dr Ines Hale, medical, science, arrive (the cell she landed on reads The Dry Gully) (sitting 4)"),
    "game_l13_act_toolbox": ("game", "Science's xESS, Act after the kit, the brass key and the toolbox: Marrow's talk above, then 'Dr Ines Hale picked up Medical kit.', 'Dr Ines Hale picked up Pump house key.', the end of the conversation, and 'Dr Ines Hale picked up Toolbox (fuse x2).', each with its picture (sitting 4)"),
    "game_l13_pack_before": ("game", "Science's xESS, Pack after the key and the toolbox (state start): fuse x2, pump key x1"),
    "game_l13_look_before": ("game", "Science's xESS, Look back in the yard beside the trail sign (state start): Use Trail sign, 'Go to The Dry Gully', Further off '! Old Marrow - 17 W', '? Relay keycard - 10 SW'"),
    "game_l13_beam_before": ("game", "Science's xESS, Beam in the yard (state start): 'To The Dry Gully'"),
    "game_l13_bp": ("game", "Helm, beamed back up (Crew, Beam up): its handheld's Boarding Party screen: 'Going down to Kesh Relay', Lt Dana Ross, helm, In the party, Dr Ines Hale, medical, science, BEAM DOWN"),
    "game_l13_messages": ("game", "Helm's handheld, Messages, after Dr Hale presses Report in on her Crew app: the row 'Dr Ines Hale, reporting in.' at the top, and under it the crew's home mail, Sam and Mum"),
    "game_l13_questlist": ("game", "Helm's handheld, the Quest Log list: Relight Kesh Relay Active, Hold at the Relay Done, and nothing of anybody's side story"),
    "game_l13_log_relight_old": ("game", "Helm's Quest Log, Relight Kesh Relay selected (state start): State Active, 'Light the beacon at Kesh Relay', and its one sentence, 'The relay's beacon went dark nine days ago. Go down and light it.'"),
    "game_l13_bar_landing_pad": ("game", "Science's xESS just beamed down (game two, state final): the bar reads Dr Ines Hale, medical, science, landing pad. RE-SHOOT: 7ea2c918 drew Kesh Relay"),
    "game_l13_tasks_hale_after": ("game", "Science's xESS, Tasks (state final): See to Marrow's Cough, Active, its page and its leads"),
    "game_l13_tasks_ross_after": ("game", "Helm's xESS, Tasks (state final): Lt Dana Ross > Find a Place to Set Down, Active; its page, 'Ask the caretaker where a shuttle could land', 'If the beacon cannot be lit, somebody will have to fly a new one down.' AWAITING RE-SHOOT: the sentence breaks after 'will' (library defect)"),
    "game_l13_scan_after": ("game", "Science's xESS, Scan by the tent (state final): '**Tent** - Canvas, a camp bed, and a kettle that is still warm.'"),
    "game_l13_bar_gully_mouth": ("game", "Science's xESS, Dr Hale one step into the gully, on the mark's cell (state final): the bar reads gully mouth (the arrival cell reads Dry Gully) (sitting 4)"),
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

# Marks on the game stills (fractions of the 1280x960 frame). The xESS column is x 0.668..0.99.
_BAR = ("rect", 0.668, 0.058, 0.99, 0.132)          # the bar: name, jobs, and where she stands
_SLOT = ("rect", 0.875, 0.09, 0.99, 0.132)          # the bar's third slot (the mark; RE-SHOOT stills)
_HOME = ("rect", 0.668, 0.195, 0.982, 0.99)         # game_l13_tiles: the list of eight apps
_CR_LIST = ("rect", 0.668, 0.205, 0.99, 0.39)       # game_l13_crew: 1 down, Artemis, Dr Ines Hale (you), Everyone
_CR_BTN = ("rect", 0.668, 0.86, 0.99, 0.995)        # ... Report in, Beam up
_AT_ALL = ("rect", 0.672, 0.2, 0.97, 0.885)         # game_l13_act_toolbox: the whole transcript
_AT_BOTH = ("rect", 0.672, 0.55, 0.97, 0.86)        # ... the three pickup lines (kit, key, toolbox)
_AT_KEY = ("rect", 0.672, 0.625, 0.97, 0.69)        # ... 'picked up Pump house key.' (sitting 4)
_LK_ALL = ("rect", 0.668, 0.198, 0.99, 0.522)       # game_l13_look_before / _after: the buttons
_LK_GO = ("rect", 0.668, 0.267, 0.99, 0.338)        # ... 'Go to The Dry Gully' / 'Go to Dry Gully'
_PK_ALL = ("rect", 0.668, 0.198, 0.82, 0.29)        # game_l13_pack_before / _after: the two items
_PK_KEY = ("rect", 0.668, 0.255, 0.82, 0.29)        # ... pump key x1 / pump house key x1
_TH_LIST = ("rect", 0.672, 0.205, 0.965, 0.415)     # game_l13_tasks_*: her group, her story, Party
_TH_ROW = ("rect", 0.672, 0.287, 0.965, 0.372)      # ... her story's heading and state
_TH_PAGE = ("rect", 0.672, 0.52, 0.97, 0.685)       # ... the page: State, the objective, the text
_BM_MSG = ("rect", 0.668, 0.198, 0.875, 0.235)      # game_l13_beam: 'No other site has a lock yet.'
_BM_TO = ("rect", 0.668, 0.198, 0.99, 0.27)         # game_l13_beam_before: 'To The Dry Gully'
_FI_SET = ("rect", 0.668, 0.22, 0.99, 0.495)        # game_l13_fire: SAFE and the three settings
_MH_COUGH = ("rect", 0.672, 0.551, 0.842, 0.598)    # game_l13_marrow_hale: 'Look at that cough', unmarked
_MR_TWO = ("rect", 0.39, 0.345, 0.5, 0.425)         # game_l13_marrow_ross: Ross and Marrow by the tent
_MR_HALE = ("rect", 0.19, 0.3, 0.235, 0.375)        # ... Hale on the landing pad
_MR_COVER = ("rect", 0.672, 0.607, 0.988, 0.652)    # ... 'Look at that cough (covering for medical)'
_TR_PARTY = ("rect", 0.672, 0.205, 0.99, 0.44)      # game_l13_tasks_ross_before: Party, Relight, Hold, no story
_HD_HALE = ("rect", 0.232, 0.51, 0.272, 0.578)      # game_l13_bar_hidden: Hale on the kit's cell
_SC_KIT = ("rect", 0.232, 0.51, 0.272, 0.578)       # game_l13_bar_scrub: Hale on the kit's cell, empty now
_SC_TOLD = ("rect", 0.672, 0.49, 0.99, 0.67)        # ... Marrow's line about the kit
_SC_PICK = ("rect", 0.672, 0.815, 0.99, 0.87)       # ... 'Dr Ines Hale picked up Medical kit.'
_SB_ALL = ("rect", 0.668, 0.2, 0.99, 0.46)          # game_l13_scan_before: everything in sight
_SB_TENT = ("rect", 0.668, 0.243, 0.83, 0.275)      # ... 'Tent - no reading'
_SA_TENT = ("rect", 0.668, 0.243, 0.99, 0.3)        # game_l13_scan_after: the tent's Scan line
_AR_HALE = ("rect", 0.07, 0.4, 0.12, 0.475)         # game_l13_bar_arrive / _gully_mouth: Hale at the gully's entry
_BP_ALL = ("rect", 0.018, 0.11, 0.5, 0.3)           # game_l13_bp: who is going, and who is down
_BP_PARTY = ("rect", 0.018, 0.235, 0.48, 0.3)       # ... In the party, Dr Ines Hale
_MS_HALE = ("rect", 0.022, 0.118, 0.445, 0.202)     # game_l13_messages: 'Dr Ines Hale, reporting in.'
_MS_HOME = ("rect", 0.022, 0.205, 0.2, 0.45)        # ... the crew's mail from home
_QL = ("rect", 0.0, 0.142, 0.38, 0.28)              # game_l13_questlist: Relight Kesh Relay, Hold at the Relay
_LO_PAGE = ("rect", 0.385, 0.075, 0.87, 0.205)      # game_l13_log_relight_old: State, objective, the sentence
_LO_SENT = ("rect", 0.385, 0.17, 0.87, 0.205)       # ... its one sentence
_LR_PIC = ("rect", 0.385, 0.165, 0.81, 0.3)         # game_l13_log_relight: the relay's picture and line
_LR_TABLE = ("rect", 0.385, 0.36, 0.92, 0.49)       # ... the table

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l13_tiles", "marks": [_HOME]},
        {"from": 5, "still": "game_l13_bar_arrive", "marks": [_SLOT]},
        {"from": 7, "still": "card_title"},
    ]},
    "s02_the_bar_and_the_eight_apps": {"step": 1, "beats": [
        {"from": 0, "still": "game_l13_tiles", "marks": [_BAR]},
        {"from": 2, "still": "game_l13_tiles", "marks": [_HOME]},
        {"from": 3, "still": "game_l13_crew", "marks": [_CR_LIST, _CR_BTN]},
        {"from": 4, "still": "game_l13_act_toolbox", "marks": [_AT_ALL]},
        {"from": 5, "still": "game_l13_look_before", "marks": [_LK_ALL]},
        {"from": 6, "still": "game_l13_pack_before", "marks": [_PK_ALL]},
        {"from": 7, "still": "game_l13_tasks_hale_before", "marks": [_TH_LIST]},
        {"from": 8, "still": "game_l13_beam", "marks": [_BM_MSG]},
        {"from": 8.5, "still": "game_l13_fire", "marks": [_FI_SET]},
        {"from": 9, "still": "card_apps"},
        {"from": 10, "still": "card_apps", "marks": [("part", "r1c3"), ("part", "r2c3"), ("part", "r3c3"), ("part", "r4c3")]},
    ]},
    "s03_who_is_offered_what": {"step": None, "beats": [
        {"from": 0, "still": "card_offered", "marks": [("part", "r1")]},
        {"from": 1, "still": "game_l13_marrow_hale", "marks": [_MH_COUGH]},
        {"from": 3, "still": "game_l13_marrow_ross", "marks": [_MR_TWO]},
        {"from": 4, "still": "game_l13_marrow_ross", "marks": [_MR_HALE]},
        {"from": 5, "still": "game_l13_marrow_ross", "marks": [_MR_COVER]},
        {"from": 6, "still": "card_offered", "marks": [("part", "r3")]},
        {"from": 9, "still": "card_offered", "marks": [("part", "r4")]},
    ]},
    "s04_a_mark_is_a_word": {"step": 2, "beats": [
        {"from": 0, "still": "game_l13_tiles", "marks": [_SLOT]},
        {"from": 2, "still": "game_l13_bar_arrive", "marks": [_SLOT, _AR_HALE]},
        {"from": 5, "still": "e_land2", "marks": [("lines", 12, 12), ("lines", 21, 21)]},
        {"from": 5.33, "still": "e_gully2", "marks": [("lines", 5, 5), ("lines", 16, 16), ("lines", 22, 22)]},
        {"from": 5.67, "still": "e_cist2", "marks": [("lines", 5, 5), ("lines", 14, 14)]},
        {"from": 6, "still": "game_l13_bar_landing_pad", "marks": [_SLOT]},
        {"from": 6.5, "still": "game_l13_bar_gully_mouth", "marks": [_SLOT]},
        {"from": 7, "still": "game_l13_bar_hidden", "marks": [_HD_HALE]},
        {"from": 8, "still": "game_l13_bar_hidden", "marks": [_HD_HALE, _SLOT]},
        {"from": 10, "still": "game_l13_bar_hidden", "marks": [_SLOT]},
        {"from": 11, "still": "game_l13_bar_scrub", "marks": [_SC_TOLD]},
        {"from": 12, "still": "game_l13_bar_scrub", "marks": [_SLOT]},
        {"from": 13, "still": "game_l13_bar_scrub", "marks": [_SC_KIT, _SC_PICK]},
    ]},
    "s05_titles_and_what_the_pack_say": {"step": 3, "beats": [
        {"from": 0, "still": "game_l13_look_before", "marks": [_LK_GO]},
        {"from": 1.5, "still": "game_l13_beam_before", "marks": [_BM_TO]},
        {"from": 3, "still": "e_gully3", "marks": [("lines", 3, 3)]},
        {"from": 3.5, "still": "e_cist3", "marks": [("lines", 3, 3)]},
        {"from": 4, "still": "game_l13_act_toolbox", "marks": [_AT_BOTH]},
        {"from": 6, "still": "e_key0", "marks": [("lines", 248, 248)]},
        {"from": 7, "still": "game_l13_act_toolbox", "marks": [_AT_KEY]},
        {"from": 8, "still": "game_l13_pack_before", "marks": [_PK_KEY]},
        {"from": 9, "still": "e_key0", "marks": [("lines", 253, 253)]},
        {"from": 10, "still": "game_l13_pack_before", "marks": [_PK_KEY]},
        {"from": 11, "still": "e_key4", "marks": [("lines", 248, 248), ("lines", 253, 253)]},
        {"from": 12, "still": "card_key"},
        {"from": 14, "still": "t_miss", "marks": [("span", 1, "item-nothing-gives")]},
    ]},
    "s06_scan_and_a_title_that_is_the": {"step": 5, "beats": [
        {"from": 0, "still": "game_l13_scan_before", "marks": [_SB_ALL]},
        {"from": 1, "still": "game_l13_scan_before", "marks": [_SB_TENT]},
        {"from": 2, "still": "e_scan5", "marks": [("lines", 220, 220)]},
        {"from": 3, "still": "game_l13_scan_after", "marks": [_SA_TENT]},
        {"from": 4, "still": "game_l13_tasks_hale_before", "marks": [_TH_LIST]},
        {"from": 6, "still": "game_l13_tasks_hale_before", "marks": [_TH_PAGE]},
        {"from": 8, "still": "game_l13_tasks_hale_before", "marks": [_TH_ROW]},
        {"from": 9, "still": "e_cough6", "marks": [("lines", 113, 113)]},
        {"from": 10, "still": "game_l13_tasks_hale_after", "marks": [_TH_ROW]},
    ]},
    "s07_the_two_with_nothing_to_do": {"step": 7, "beats": [
        {"from": 0, "still": "game_l13_tasks_ross_before", "marks": [_TR_PARTY]},
        {"from": 2, "still": "game_l13_marrow_ross", "marks": [_MR_COVER]},
        {"from": 4, "still": "e_stories", "marks": [("lines", 145, 163)]},
        {"from": 6, "still": "t_m7", "marks": [("span", 1, "unfired-signal")]},
        {"from": 7, "still": "e_strip", "marks": [("lines", 520, 520)]},
        {"from": 7.5, "still": "game_l13_tasks_ross_after", "marks": [_TH_ROW]},
    ]},
    "s08_what_the_bridge_sees_and_you": {"step": 9, "beats": [
        {"from": 0, "still": "game_l13_bp", "marks": [_BP_ALL]},
        {"from": 2, "still": "game_l13_bp", "marks": [_BP_PARTY]},
        {"from": 3, "still": "game_l13_questlist", "marks": [_QL]},
        {"from": 4, "still": "game_l13_messages", "marks": [_MS_HALE]},
        {"from": 6, "still": "game_l13_messages", "marks": [_MS_HOME]},
        {"from": 7, "still": "game_l13_questlist", "marks": [_QL]},
        {"from": 10, "still": "game_l13_log_relight_old", "marks": [_LO_PAGE]},
        {"from": 11, "still": "game_l13_log_relight_old", "marks": [_LO_SENT]},
        {"from": 13, "still": "e_brief", "marks": [("lines", 78, 88)]},
        {"from": 14, "still": "game_l13_log_relight", "marks": [_LR_PIC]},
        {"from": 15, "still": "game_l13_log_relight", "marks": [_LR_TABLE]},
        {"from": 16, "still": "card_exercise"},
        {"from": 19, "still": "card_next"},
    ]},
}
