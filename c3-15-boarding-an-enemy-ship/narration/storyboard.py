"""Storyboard for c3-15-boarding-an-enemy-ship: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and the kinds of still in _tools/picture/README.md. Caption numbers
are those of shots.py (2026-10-16).

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

THE GROUND FOLDER. A state holds `ground\\` as the student has it (states.py reads, diffs and
writes subfolders).

2026-10-16, HULL: the Black Gull is a `pirate_strongbow`, not a `pirate_brigantine` (owner's
decision). The brigantine is a light carrier (ship data `baycount` 6, role `carrier`), and
LM's npc_cag launched six `Black Gull NN` fighters that shot at the Artemis all game, after
she struck and after she was taken. The strongbow has no bay and no `carrier` role, is about
the same size (mesh about 52 x 75 against 49 x 61), and has the same kinds of room: two
brigs, a boat bay, a plunder hold, a surgery, captains-cabin and crew-berths (plus a
grog-locker and a mess-deck). Changed: story.mast's npc_spawn art, mission.amd's picture
line and two sentences ("A pirate raider", "A raider is worth more"), and the comment over
Mate Oduya (it said the game puts her crew aboard). Mock, --use-working-tree, 2026-10-16:
no carrier role, bay_count 0; her deck builds (52 x 52 tiles, planned from the grid text);
the strongbox in the WEST brig (17, 23), Oduya in the EAST brig (35, 23), the kit on the
arrival (26, 33), Brakk in the boat bay (25, 41). Brakk (Notice 4, she must see you) only
notices the four cells in front of the bay's door (26..28, 40); she can be shot only from
(28, 39) (5 cells) and (29, 39) (6), the first cells of the hallway on the right of the bay
from which she is in sight. Those are reachable from the arrival unseen.

GAME STILLS. Taken 2026-10-16 on the BRIGANTINE (server, Helm Lt Dana Ross, Comms Ens Tam
Vale): what they showed is in the captions, except where the hull or a library fix changes
it. EVERY ONE NEEDS TAKING AGAIN on the strongbow, and its marks checking after:
game_l15_log_chase (her picture and the brigantine sentence), game_l15_comms_gull,
game_l15_comms_struck and game_l15_comms_hove (Threats 7 / 6 and shields shot down: her
fighters), game_l15_deck_arrive, game_l15_deck_brig, game_l15_strongbox and game_l15_oduya
(her deck; the bar's raw `room:brig` key and Look's bare `Captain's strongbox` line are
library defects being fixed), game_l15_log_prize (the brigantine sentence). game_l15_bp_gull
names no hull and may be kept (no beat uses it). SITTING 4 (2026-10-16): all taken again on
the strongbow. Once she has struck her crew stand down: Brakk never attacked, so
game_l15_medkit was never taken and its beat (and step 7 and the medkit part of step 8
below) is dropped. game_l15_brakk_fire shows Vale armed FULL with a calm Brakk in sight.
Generated `Pirate crew` figures stand calm in the Plunder Hold and Crew Berths.
State "final": `python game.py c3-15-boarding-an-enemy-ship start --consoles server,helm,comms`.
Nobody beams down at the relay. ENGINE 1.3.15 ON COMMS: select only the Black Gull, never press
Cancel, and DO NOT TOUCH COMMS from step 2 until she has struck (re-clicking her to refresh the
menu took the 2D map away). About fifteen minutes:
  1. Helm: the handheld icon, Quests (0.15, 0.55), Run Down the Black Gull (0.12, 0.24):
     game_l15_log_chase (her picture under 'The Black Gull, out past the relay.').
  2. Comms: click the Black Gull on the 2D map (she starts about 5K out; her name red):
     game_l15_comms_gull (Black Gull (pirate), Hail, Taunt, Surrender now). Hands off Comms.
  3. Helm: 3rd magnifier (0.465, 0.07), click her marker, full impulse: inside 1500 in about
     25 s. The strip: Quest complete: Run Down the Black Gull; her marker turns yellow.
  4. Comms: her menu now: game_l15_comms_struck (Take as prize, Send a boarding party).
     Send a boarding party, then click the `Black Gull (pirate)` header (0.38, 0.064):
     game_l15_comms_hove.
  5. Helm, then Comms: handheld (0.15, 0.24), Boarding Party, BEAM DOWN:
     game_l15_deck_arrive (Helm: the deck, nobody else in view, the kit a step away).
  6. Vale: take the boarding kit. Ross: Look, `? Captain's strongbox` (it walks him to the
     west brig): game_l15_deck_brig. Vale: Look, `? Mate Oduya` (east brig): game_l15_oduya.
  7. Ross: walk to the cells in front of the boat bay's door (26..28, 40): Brakk hits him,
     `Hit by Gunner Brakk - you are DOWN.` (the medkit still needs him down).
  8. Vale: from the arrival walk aft down the hallway on the RIGHT of the boat bay, one cell
     at a time; stop where Brakk comes into sight (28, 39). Fire, FULL, Arm:
     game_l15_brakk_fire (armed FULL, Brakk in sight through the door). Click her: down for
     good, a power cell where she fell. Vale beside Ross: Pack, `Use medkit on Lt Dana Ross`:
     game_l15_medkit. Press it: back on his feet.
  9. Ross: Look, Use Captain's strongbox: game_l15_strongbox. Take her as a prize. Both are
     home. Helm's Quest Log, Take the Black Gull: game_l15_log_prize (Done, 200 credits).
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
_ODUYA = _cut(_A, "// ---- Lecture 15. Aboard the Black Gull, in her brig", "\n// ---- Hostiles")
_BRAKK = _cut(_A, "// ---- Lecture 15. The captain struck.", "\n// ---- Scenes")
_SHIP = _cut(_M, "    # THE BLACK GULL.", "    await task_schedule(spawn_players)")
_CARD = _cut(_M, "\n\n#\n# Come Back to Kesh Relay")
_GUARD = "    ->END if party_ship is None\n"

STATES = {
    # Lecture 14's finished files
    "start": {"folder": "c3-07-anatomy-of-a-long-away-mission/example",
              "over": ("c3-09-tile-map-editor-part-2/example", "c3-10-props/example",
                       "c3-11-people-and-hostiles/example", "c3-12-scenes-on-the-ground/example",
                       "c3-13-what-the-crew-sees/example", "c3-14-pacing-an-away-mission/example")},
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
    # THE REAL GAME. Taken 2026-10-16 on the brigantine: all to take again on the strongbow
    # (docstring). State final, three windows: server, Helm (Lt Ross), Comms (Ens Vale).
    "game_l15_log_chase": ("game", "Helm's ePADD Quest Log, Run Down the Black Gull selected: her picture (the strongbow) under 'The Black Gull, out past the relay.', the two paragraphs; Take the Black Gull, Relight Kesh Relay (with its time) and Hold at the Relay in the list"),
    "game_l15_comms_gull": ("game", "Comms, the Black Gull picked on the 2D map before she strikes: Black Gull (pirate), her name red on the map, and the buttons Hail, Taunt, Surrender now, Cancel"),
    "game_l15_comms_struck": ("game", "Comms, the Black Gull after Helm closed inside 1500 and she struck: the buttons Take as prize and Send a boarding party"),
    "game_l15_comms_hove": ("game", "Comms after Send a boarding party: her answer 'We are hove to. Send your party across: Boarding Party, on the ePADD.'"),
    "game_l15_bp_gull": ("game", "Helm's handheld, the Boarding Party tile pressed: 'Going down to Black Gull', Lt Dana Ross, helm, and BEAM DOWN"),
    "game_l15_deck_arrive": ("game", "Helm's console aboard the Black Gull, just beamed across: the generated deck on the map, nobody else in view, the boarding kit a step from the arrival, the xESS home beside it"),
    "game_l15_deck_brig": ("game", "Helm's console aboard her, Lt Ross in the west brig: the strongbox in the brig on the map, the bar naming the room (Brig), Look's Use Captain's strongbox and the box's description"),
    "game_l15_oduya": ("game", "Comms' xESS aboard her, Act, talking to Mate Oduya: 'Tender Halcyon, out of Kesh...', and Ask what the tender was carrying, Ask who is still armed, Tell her she is going home"),
    "game_l15_brakk_fire": ("game", "Comms' xESS aboard her, Ens Vale three cells from Gunner Brakk in the boat bay: FIRE armed, FULL, Brakk in sight"),
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

# Marks on the game stills (fractions of the 1280 x 960 frame), measured 2026-10-16 on the
# sitting-4 (strongbow) stills.
_CS_SEND = ("rect", 0.27, 0.67, 0.62, 0.755)        # game_l15_comms_struck: Send a boarding party
_CS_STRIP = ("rect", 0.018, 0.49, 0.27, 0.56)       # ... the strip: Quest complete: Run Down the Black Gull
_CG_HER = ("rect", 0.63, 0.655, 0.74, 0.76)         # game_l15_comms_gull: her marker, Black Gull
_CG_BTNS = ("rect", 0.27, 0.555, 0.645, 0.795)      # ... Hail, Taunt, Surrender now
_CH_SAYS = ("rect", 0.51, 0.255, 1.0, 0.35)         # game_l15_comms_hove: her answer
_DA_DECK = ("rect", 0.265, 0.105, 0.435, 0.84)      # game_l15_deck_arrive: the deck, nobody about
_OD_LINE = ("rect", 0.67, 0.33, 0.99, 0.49)         # game_l15_oduya: her face and her line
_OD_MAP = ("rect", 0.315, 0.655, 0.39, 0.74)         # ... Mate Oduya on the map, in the east brig
_SB_ALL = ("rect", 0.67, 0.205, 0.99, 0.57)         # game_l15_strongbox: its line and four answers
_SB_THREE = ("rect", 0.67, 0.355, 0.85, 0.515)      # ... Take her, Open her sea cocks, Go back
_LC_ROW = ("rect", 0.0, 0.215, 0.38, 0.285)         # game_l15_log_chase: Run Down the Black Gull
_LC_PIC = ("rect", 0.385, 0.17, 0.74, 0.305)        # ... her picture and its caption
_DB_BOX = ("rect", 0.225, 0.63, 0.28, 0.695)        # game_l15_deck_brig: the strongbox in the brig
_DB_DECK = ("rect", 0.035, 0.105, 0.665, 0.995)       # ... the whole deck
_LP_DONE = ("rect", 0.385, 0.075, 0.575, 0.145)     # game_l15_log_prize: Done, 200 credits
_BF_BRAKK = ("rect", 0.185, 0.52, 0.245, 0.64)      # game_l15_brakk_fire: Gunner Brakk, in the boat bay
_BF_MAP = ("rect", 0.185, 0.49, 0.36, 0.64)         # ... Ens Vale and Brakk, three cells apart
_BF_ARMED = ("rect", 0.67, 0.21, 0.99, 0.495)       # ... ARMED - FULL, > FULL

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_l15_comms_struck", "marks": [_CS_SEND]},
        {"from": 3, "still": "game_l15_deck_arrive", "marks": [_DA_DECK]},
        {"from": 5, "still": "game_l15_oduya", "marks": [_OD_LINE]},
        {"from": 6, "still": "game_l15_strongbox", "marks": [_SB_ALL]},
        {"from": 7, "still": "card_title"},
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
        {"from": 0, "still": "game_l15_comms_gull", "marks": [_CG_HER]},
        {"from": 2, "still": "game_l15_comms_gull", "marks": [_CG_BTNS]},
        {"from": 3, "still": "e_sides", "marks": [("lines", 683, 689)]},
        {"from": 4, "still": "e_sides", "marks": [("lines", 688, 688)]},
        {"from": 5, "still": "m_ship", "marks": [("lines", 66, 67)]},
        {"from": 7, "still": "m_ship", "marks": [("text", 66, '"pirate_strongbow"')]},
        {"from": 10, "still": "m_ship", "marks": [("lines", 66, 67)]},
        {"from": 11, "still": "m_ship", "marks": [("text", 66, "20000, 0, 20000")]},
        {"from": 12, "still": "m_ship", "marks": [("text", 67, "6000, 0, 4000")]},
        {"from": 13, "still": "m_ship", "marks": [("lines", 64, 65)]},
    ]},
    "s04_three_quests_and_a_card": {"step": 4, "beats": [
        # the game first: the chase in the Quest Log
        {"from": 0, "still": "game_l15_log_chase", "marks": [_LC_ROW]},
        {"from": 1, "still": "game_l15_log_chase", "marks": [_LC_PIC]},
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
        {"from": 0, "still": "game_l15_deck_brig", "marks": [_DB_BOX]},
        {"from": 1, "still": "e_strong", "marks": [("lines", 437, 438)]},
        {"from": 2, "still": "e_strong", "marks": [("lines", 437, 437)]},
        {"from": 3, "still": "e_strong", "marks": [("lines", 438, 438)]},
        {"from": 5, "still": "card_kinds"},
        {"from": 7, "still": "card_rooms"},
        {"from": 10, "still": "card_stood"},
        {"from": 11, "still": "card_kinds"},
    ]},
    "s06_her_own_crew_and_the_walk": {"step": None, "beats": [
        {"from": 0, "still": "game_l15_deck_arrive", "marks": [_DA_DECK]},
        {"from": 3, "still": "game_l15_oduya", "marks": [_OD_MAP]},
        {"from": 4, "still": "game_l15_deck_brig", "marks": [_DB_BOX]},
        {"from": 5, "still": "game_l15_deck_brig", "marks": [_DB_DECK]},
        {"from": 10, "still": "card_rule", "marks": [("part", "item1")]},
    ]},
    "s07_three_endings": {"step": 9, "beats": [
        {"from": 0, "still": "game_l15_comms_gull", "marks": [_CG_HER]},
        {"from": 1, "still": "game_l15_comms_struck", "marks": [_CS_STRIP]},
        {"from": 2, "still": "game_l15_comms_hove", "marks": [_CH_SAYS]},
        # the gunner (sitting 4: she stands down with her crew; no medkit beat)
        {"from": 3, "still": "game_l15_brakk_fire", "marks": [_BF_BRAKK]},
        {"from": 8, "still": "game_l15_brakk_fire", "marks": [_BF_ARMED, _BF_MAP]},
        {"from": 10, "still": "game_l15_strongbox", "marks": [_SB_THREE]},
        {"from": 11, "still": "card_endings", "marks": [("part", "r1")]},
        {"from": 12, "still": "game_l15_log_prize", "marks": [_LP_DONE]},
        {"from": 13, "still": "card_endings", "marks": [("part", "r2")]},
        {"from": 14, "still": "card_endings", "marks": [("part", "r3")]},
        {"from": 15, "still": "card_endings", "marks": [("part", "r1c2"), ("part", "r2c2"), ("part", "r3c2")]},
        {"from": 16, "still": "card_endings", "marks": [("part", "r1c5"), ("part", "r2c5"), ("part", "r3c5")]},
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
