"""Storyboard for c3-15-boarding-an-enemy-ship: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-15).

The lecture starts from Lecture 14's finished files in MyAway ("start"). Two files change.
The states are built BACKWARDS from the page's own example\\ files ("final"), taking each
step's block out again: the scenes ("s6"), the four records ("s5"), the card and its line
("s4"), the three quests ("s3"), the ship ("s2"), the side ("s1", the same text as
"start"). So every block on screen is the page's own, byte for byte.

2026-10-15: example\\mission.amd carried four of the starter's old mark lines (see
Lecture 14's storyboard); they now match Lecture 13. The script and page were corrected
for the library released after they were written: nothing aboard is ever shut in, a shot
never removes a prop, the finished files lint clean, `Take as prize` finishes the quest,
a landing party with nobody on the ground gives way. From the library's documentation and
lint only; nobody has re-played the deck since.

THE GROUND IS LAID FLAT, as in Lectures 12 to 14 (the tool reads one folder level).

GAME STILLS. Not taken yet; no marks until the screenshots exist. game.py cannot start this
mission (it makes its probe from the `amd` template and copies only mission.amd and
story.mast). Build a real MyAway folder for state "final" WITH its ground\\ folder (Lecture
7's example\\ with the example\\ folders of Lectures 8 to 15 laid over it, subfolders
included), `sbs fetch MyAway --update-libs` once (the station art: without it there is no
button), then `sbs run server,helm,comms -m MyAway map=0` with COSMOS_SETTINGS
'{"GAME_RESULTS_SAVE": false}'. THREE windows: the server, Helm (Lt Dana Ross) and Comms
(Ens Tam Vale). Nobody beams down at the relay. ENGINE 1.3.15 ON COMMS: select only the
Black Gull all game, and never press Cancel (either bug takes the 2D map away). About ten
minutes:
  1. Helm: the handheld icon, Quests, Run Down the Black Gull: game_l15_log_chase (the
     brigantine at the top of its page).
  2. Comms: the Black Gull from the contact list (about 7,100 out): game_l15_comms_gull
     (Hail, Taunt, Surrender now).
  3. Helm: fly to her, inside 1500 (about a minute at full impulse). She strikes; Come Back
     to Kesh Relay joins the quest list.
  4. Comms: her buttons now: game_l15_comms_struck (Take as prize, Send a boarding party).
     Send a boarding party: game_l15_comms_hove ('We are hove to. Send your party
     across: Boarding Party, on the ePADD.').
  5. Helm: the handheld icon, Boarding Party: game_l15_bp_gull ('Going down to Black
     Gull'). BEAM DOWN: game_l15_deck_arrive (her deck, her crew standing about, the
     boarding kit a step away). Comms: BEAM DOWN too.
  6. Ross: walk to the brig with the strongbox (Look lists it further off; pressing it
     walks there): game_l15_deck_brig (the strongbox in the brig, the bar's place word).
  7. Vale: talk to Mate Oduya, in the other brig: game_l15_oduya.
  8. Ross: use the strongbox: game_l15_strongbox (four answers). Take her as a prize. Both
     are home. Helm's Quest Log, Take the Black Gull: game_l15_log_prize (Done, 200
     credits).
"""
import os as _os

LECTURE = "c3-15-boarding-an-enemy-ship"
TITLE = ("Class 3, Lecture 15", "Boarding an enemy ship", "A deck nobody draws")
MISSION = "MyAway"
FILE = "mission.amd"
MAST = "story.mast"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
_COURSES = _os.path.dirname(_HERE)


def _read(*parts):
    with open(_os.path.join(_COURSES, *parts), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_L13 = ("c3-13-what-the-crew-sees", "example", "ground")
_GROUND = [("write", "starter.tileset", _read("c3-09-tile-map-editor-part-2", "example", "ground", "starter.tileset")),
           ("write", "landing.tiles", _read(*_L13, "landing.tiles")),
           ("write", "cistern.tiles", _read(*_L13, "cistern.tiles")),
           ("write", "gully.tiles", _read(*_L13, "gully.tiles"))]

_A = _read(LECTURE, "example", "mission.amd")
_M = _read(LECTURE, "example", "story.mast")


def _cut(text, a, b=None):
    i = text.index(a)
    return text[i:] if b is None else text[i:text.index(b, i)]


_EX = LECTURE + "/example"
_SCENES = _cut(_A, "\n\n// ---- Lecture 15: aboard the Black Gull. The three", "\n\n// ---- Sides")
_SIDES = _cut(_A, "\n\n// ---- Sides")
_QUESTS = _cut(_A, "// ---- Lecture 15. `reach gull", "\n// ---- Side stories")
_PROPS = _cut(_A, "// ---- Lecture 15: aboard the Black Gull. `Area: deck`", "\n// ---- People")
_ODUYA = _cut(_A, "// ---- Lecture 15. The Black Gull's own crew", "\n// ---- Hostiles")
_BRAKK = _cut(_A, "// ---- Lecture 15. The captain struck.", "\n// ---- Scenes")
_SHIP = _cut(_M, "    # THE BLACK GULL.", "    await task_schedule(spawn_players)")
_CARD = _cut(_M, "\n\n#\n# Come Back to Kesh Relay")
_GUARD = "    ->END if party_ship is None\n"

STATES = {
    # Lecture 14's finished files
    "start": {"folder": "c3-07-anatomy-of-a-long-away-mission/example",
              "over": ("c3-09-tile-map-editor-part-2/example", "c3-10-props/example",
                       "c3-11-people-and-hostiles/example", "c3-12-scenes-on-the-ground/example",
                       "c3-13-what-the-crew-sees/example", "c3-14-pacing-an-away-mission/example"),
              "edits": _GROUND},
    # The page's own files, and back from there one step at a time
    "final": {"base": "start", "edits": [("write", FILE, _A), ("write", MAST, _M)],
              "same_as": (_EX + "/mission.amd", _EX + "/story.mast")},
    "s6": {"base": "final", "edits": [("replace", FILE, _SCENES, "")]},                    # before Step 7
    "s5": {"base": "s6", "edits": [("replace", FILE, _PROPS, ""), ("replace", FILE, _ODUYA, ""),
                                   ("replace", FILE, _BRAKK, "")]},                         # before Step 6
    "s4": {"base": "s5", "edits": [("replace", MAST, _CARD, ""),
                                   ("replace", MAST, _GUARD + "    boarding_visit_end()\n", _GUARD)]},  # before Step 5
    "s3": {"base": "s4", "edits": [("replace", FILE, _QUESTS, "")]},                       # before Step 4
    "s2": {"base": "s3", "edits": [("replace", MAST, _SHIP, "")]},                         # before Step 3
    "s1": {"base": "s2", "edits": [("replace", FILE, _SIDES, "")],                         # before Step 2: Lecture 14's text
           "same_as": ("c3-14-pacing-an-away-mission/example/mission.amd",)},
}

_LINT = "sbs lint MyAway"
_NS = {"side": False}
_MS = {"side": False, "file": MAST}

STILLS = {
    # Step 2: a side
    "e_sides": ("vscode", "s2", 683, "big", _NS),          # lines 673 to 693: the Sides section (680 to 691), Enemies: tsn (688)
    # Step 3: the ship
    "m_ship": ("vscode", "s3", 66, "big", _MS),            # lines 56 to 76: the relay's line (62), the two new lines (66, 67)
    # Step 4: three quests
    "e_chase": ("vscode", "s4", 132, "big", _NS),          # lines 122 to 142: Run Down the Black Gull (124 to 136)
    "e_back": ("vscode", "s4", 145, "big", _NS),           # lines 135 to 155: Come Back to Kesh Relay (141 to 148)
    "e_prize": ("vscode", "s4", 154, "big", _NS),          # lines 144 to 164: Come Back (141 to 148), Take the Black Gull (152 to 165)
    "t_s4": ("terminal", [("s4", _LINT)]),
    # Step 5: the card
    "m_card": ("vscode", "s5", 101, "big", _MS),           # lines 91 to 111: the starter's card's new line (92), the new card (97 to 110)
    # Step 6: what is aboard
    "e_strong": ("vscode", "s6", 442, "big", _NS),         # lines 432 to 452: the strongbox (435 to 444), Area: deck and Mark: brig (437, 438)
    # Step 7: the scenes
    "e_scenes": ("vscode", "final", 793, "big", _NS),      # lines 783 to 803: The Strongbox (785 to 791), Mate Oduya (793)
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME (not taken yet). State final, three windows: server, Helm (Lt Ross),
    # Comms (Ens Vale). Press order in the docstring.
    "game_l15_log_chase": ("game", "Helm's ePADD Quest Log, Run Down the Black Gull selected: the brigantine drawn with 'The Black Gull, out past the relay.', the two paragraphs; Take the Black Gull and Relight Kesh Relay (with its time) in the list"),
    "game_l15_comms_gull": ("game", "Comms, the Black Gull picked from the contact list before she strikes: her name, red, and the buttons Hail, Taunt, Surrender now"),
    "game_l15_comms_struck": ("game", "Comms, the Black Gull after Helm closed inside 1500 and she struck: the buttons Take as prize and Send a boarding party"),
    "game_l15_comms_hove": ("game", "Comms after Send a boarding party: her answer 'We are hove to. Send your party across: Boarding Party, on the ePADD.'"),
    "game_l15_bp_gull": ("game", "Helm's handheld, the Boarding Party tile pressed: 'Going down to Black Gull', Lt Dana Ross, helm, and BEAM DOWN"),
    "game_l15_deck_arrive": ("game", "Helm's console aboard the Black Gull, just beamed across: the generated deck on the map, her own crew standing in her rooms, the boarding kit a step from the arrival, the xESS beside it"),
    "game_l15_deck_brig": ("game", "Helm's console aboard her, Lt Ross at the brig: the strongbox in the brig on the map, and the bar's place word"),
    "game_l15_oduya": ("game", "Comms' xESS aboard her, Act, talking to Mate Oduya: 'Tender Halcyon, out of Kesh...', and Ask what the tender was carrying, Ask who is still armed, Tell her she is going home"),
    "game_l15_strongbox": ("game", "Helm's xESS, Act, the strongbox: its line, and Take her as a prize, Open her sea cocks, Go back to the ship, Leave it for now"),
    "game_l15_log_prize": ("game", "Helm's ePADD Quest Log after Take her as a prize, both crew home: Take the Black Gull Done, Reward 200 credits; Come Back to Kesh Relay Active"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_needs": ("card", "points", {"kicker": "Send a boarding party: the button needs four things", "items": [
        "A ship that has struck", "A hull with a plan", "The station art, which your starter has",
        "No other party out"]}),
    "card_refused": ("card", "page", {"kicker": "What Comms answers, with anybody still down at the relay", "text": [
        "We cannot take a party aboard while your people are elsewhere."]}),
    "card_fix": ("card", "points", {"kicker": "One party at a time", "items": [
        "When she strikes, the landing party comes home", "When the ship comes back, the relay opens again"]}),
    "card_kinds": ("card", "table", {"heading": "Step 6 - What is aboard", "kicker": "Mark: on a deck is a kind of room"}),
    "card_stood": ("card", "table", {"heading": "Step 6 - What is aboard", "nth": 2, "kicker": "Where the game stood them, on the Black Gull"}),
    "card_rooms": ("card", "rows", {"kicker": "Her rooms have names of their own", "header": ["Kind", "On the Black Gull"],
                                    "rows": [["cargo", "plunder-hold"], ["sickbay", "surgery"],
                                             ["quarters", "captains-cabin, crew-berths"], ["bay", "boat-bay"]]}),
    "card_rule": ("card", "points", {"kicker": "One rule", "items": [
        "After every change to what is aboard, go aboard and walk to each thing"]}),
    "card_endings": ("card", "table", {"heading": "Step 7 - The scenes, and three endings", "kicker": "Three endings"}),
    "card_warn": ("card", "points", {"kicker": "Before your crew finds them", "items": [
        "A shot never removes a prop: the strongbox is safe",
        "Take as prize, on Comms: the quest pays, and nobody goes aboard",
        "What the gunner drops is lost if nobody picks it up",
        "From her deck, Beam still offers To Kesh Relay"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 16", "sub": "A long boarding mission"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l15_comms_struck"},
        {"from": 3, "still": "game_l15_deck_arrive"},
        {"from": 6, "still": "game_l15_oduya"},
        {"from": 7, "still": "game_l15_strongbox"},
        {"from": 8, "still": "card_title"},
    ]},
    "s02_one_party_at_a_time": {"step": 1, "beats": [
        {"from": 0, "still": "card_needs"},
        {"from": 1, "still": "card_needs", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_needs", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_needs", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_needs", "marks": [("part", "item4")]},
        {"from": 8, "still": "card_refused", "marks": [("part", "sheet")]},
        {"from": 11, "still": "card_fix"},
        {"from": 12, "still": "card_fix", "marks": [("part", "item1")]},
        {"from": 13, "still": "card_fix", "marks": [("part", "item2")]},
    ]},
    "s03_a_side_and_a_ship": {"step": 2, "beats": [
        # the game first: the Black Gull on Comms
        {"from": 0, "still": "game_l15_comms_gull"},
        {"from": 3, "still": "e_sides", "marks": [("lines", 683, 689)]},
        {"from": 4, "still": "e_sides", "marks": [("lines", 688, 688)]},
        {"from": 5, "still": "m_ship", "marks": [("lines", 66, 67)]},
        {"from": 8, "still": "m_ship", "marks": [("text", 66, "20000, 0, 20000")]},
        {"from": 9, "still": "m_ship", "marks": [("text", 67, "6000, 0, 4000")]},
        {"from": 10, "still": "m_ship", "marks": [("lines", 64, 65)]},
    ]},
    "s04_three_quests_and_a_card": {"step": 4, "beats": [
        # the game first: the chase in the Quest Log
        {"from": 0, "still": "game_l15_log_chase"},
        {"from": 2, "still": "e_chase", "marks": [("lines", 124, 130)]},
        {"from": 3, "still": "e_chase", "marks": [("lines", 129, 130)]},
        {"from": 4, "still": "e_back", "marks": [("lines", 141, 148)]},
        {"from": 5, "still": "e_prize", "marks": [("lines", 157, 157)]},
        {"from": 6, "still": "e_chase", "marks": [("lines", 132, 132)]},
        {"from": 8, "still": "e_prize", "marks": [("lines", 164, 164)]},
        {"from": 9, "still": "m_card", "marks": [("lines", 106, 110)]},
        {"from": 12, "still": "m_card", "marks": [("lines", 107, 109)]},
        {"from": 14, "still": "m_card", "marks": [("lines", 92, 92)]},
    ]},
    "s05_kinds_of_room": {"step": 6, "beats": [
        # the game first: the strongbox in her brig
        {"from": 0, "still": "game_l15_deck_brig"},
        {"from": 1, "still": "e_strong", "marks": [("lines", 437, 438)]},
        {"from": 2, "still": "e_strong", "marks": [("lines", 437, 437)]},
        {"from": 3, "still": "e_strong", "marks": [("lines", 438, 438)]},
        {"from": 5, "still": "card_kinds"},
        {"from": 7, "still": "card_rooms"},
        {"from": 10, "still": "card_stood"},
        {"from": 11, "still": "card_kinds"},
    ]},
    "s06_her_own_crew_and_the_walk": {"step": None, "beats": [
        {"from": 0, "still": "game_l15_deck_arrive"},
        {"from": 5, "still": "game_l15_deck_brig"},
        {"from": 9, "still": "card_rule", "marks": [("part", "item1")]},
    ]},
    "s07_three_endings": {"step": 9, "beats": [
        {"from": 0, "still": "game_l15_comms_gull"},
        {"from": 1, "still": "game_l15_comms_struck"},
        {"from": 2, "still": "game_l15_comms_hove"},
        {"from": 3, "still": "game_l15_strongbox"},
        {"from": 4, "still": "card_endings", "marks": [("part", "r1")]},
        {"from": 5, "still": "game_l15_log_prize"},
        {"from": 6, "still": "card_endings", "marks": [("part", "r2")]},
        {"from": 7, "still": "card_endings", "marks": [("part", "r3")]},
        {"from": 8, "still": "card_endings", "marks": [("part", "r1c2"), ("part", "r2c2"), ("part", "r3c2")]},
        {"from": 9, "still": "card_endings", "marks": [("part", "r1c5"), ("part", "r2c5"), ("part", "r3c5")]},
    ]},
    "s08_what_to_warn_your_crew_about": {"step": 8, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 2, "still": "card_warn", "marks": [("part", "item1")]},
        {"from": 5, "still": "card_warn", "marks": [("part", "item2")]},
        {"from": 8, "still": "card_warn", "marks": [("part", "item3")]},
        {"from": 9, "still": "card_warn", "marks": [("part", "item4")]},
        {"from": 10, "still": "card_warn"},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 5, "still": "card_next"},
    ]},
}
