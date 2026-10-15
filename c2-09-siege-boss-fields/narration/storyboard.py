"""Storyboard for c2-09-siege-boss-fields: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5 and 6 (c1-05's docstring has every kind of still and mark). Written 2026-10-15.

THE FOLDER is data\\missions\\common_data\\bosses (MISSION), as in Lecture 8, and the lecture
starts from Lecture 8's finished file ("start"). The six lines change one at a time, in the
order the script changes them; "final" is this lecture's example, byte for byte. File
stills are taken with the Side Bar hidden.

GAME STILLS (taken 2026-10-15; marks are rects measured on them. game_kralien_sci and game_log_pirates
were NOT taken: the board does without the first, and draws the log as card_log_pirates). LegendaryMissions' own Siege,
Difficulty 5, Boss: Corsair Queen, consoles server, helm, science:
    sbs run server,helm,science -m LegendaryMissions
with common_data\\bosses\\corsair_queen.amd as the state each note names. The states with
`Low: 100%` (s_low100 and after) bring her about four seconds in with nothing destroyed, so
no flying and no kills are needed. Science's contact list reads `unknown` for an unscanned ship:
the raider chip, then each row and Queue Scan, then the race chip (`pirate-o`, `kralien-o`)
lists the scanned ships of that race. game_last_sci is Lecture 8's game_morrigan_sci, and
game_options_d5 is Lecture 8's game_queen_chosen (the same files).
"""
LECTURE = "c2-09-siege-boss-fields"
TITLE = ("Class 2, Lecture 9", "A Siege boss, part 2", "Six lines, and every number is yours")
MISSION = "common_data\\bosses"
FILE = "corsair_queen.amd"

_NOTES_OLD = ("// The Corsair Queen - my first Siege boss. A copy of the Warlord with new names.\n"
              "// She arrives when the raiders thin out, with two escort fleets and one named flagship.")
_NOTES_NEW = ("// The Corsair Queen - my Siege boss.\n"
              "// She arrives when 4 raiders in 10 are left: two named ships and three escort fleets,\n"
              "// two levels above the game's difficulty. Three games in four the fleets are her own\n"
              "// pirates. One game in four she has hired Kraliens.")
_TWO = "Named: Morrigan pirate_brigantine, Badb pirate_strongbow"

STATES = {
    "start": {"folder": "c2-08-siege-boss/example", "same_as": "c2-08-siege-boss/example/corsair_queen.amd"},
    # Step 1: arrive at once (the test setting)
    "s_low100": {"base": "start", "edits": [("replace", FILE, "Low: 25%", "Low: 100%")]},
    # Steps 4 and 5: fleets, and who flies them
    "s_fleets": {"base": "s_low100", "edits": [("replace", FILE, "Fleets: 2", "Fleets: 3")]},
    "s_flies": {"base": "s_fleets", "edits": [
        ("replace", FILE, "Flies: 50% Kralien, 50% Torgoth", "Flies: 75% Pirate, 25% Kralien")]},
    # Step 6: difficulty
    "s_diff": {"base": "s_flies", "edits": [("replace", FILE, "Difficulty: +1", "Difficulty: +2")]},
    # Step 7: her own ships
    "s_named": {"base": "s_diff", "edits": [("replace", FILE, "Named: Morrigan kralien_dreadnought", _TWO)]},
    # Step 8: what lint cannot check, and a number to try
    "s_pirates": {"base": "s_named", "edits": [("replace", FILE, "75% Pirate,", "75% Pirates,")]},
    "s_d11": {"base": "s_named", "edits": [("replace", FILE, "Difficulty: +2", "Difficulty: 11")]},
    # Step 10: her real arrival, and the notes
    "s_low40": {"base": "s_named", "edits": [("replace", FILE, "Low: 100%", "Low: 40%")]},
    "final": {"base": "s_low40", "edits": [("replace", FILE, _NOTES_OLD, _NOTES_NEW)],
              "same_as": "c2-09-siege-boss-fields/example/corsair_queen.amd"},
}

_LINT = "sbs lint common_data\\bosses"
_NS = {"side": False}

# The runtime log of the s_pirates game (R:\\cosmos\\courses\\c2_09\\game\\s_pirates.mast.runtime.log):
# the same line three times, one per fleet. A drawn page, since a log is not a console.
_LOG_LINE = ("fleet_create: no fleet table for race 'pirates', so no fleet was made (is it in the "
             "NPC_RACES setting? registered: arvonian, kralien, pirate, skaraan, torgoth, ximni)")

STILLS = {
    # lines 1 to 26 until the notes grow to four lines; the fence is lines 5 to 13
    "e_start": ("vscode", "start", 10, "big", _NS),
    "e_low100": ("vscode", "s_low100", 10, "big", _NS),
    "e_fleets": ("vscode", "s_fleets", 10, "big", _NS),
    "e_flies": ("vscode", "s_flies", 10, "big", _NS),
    "e_diff": ("vscode", "s_diff", 10, "big", _NS),
    "e_named": ("vscode", "s_named", 10, "big", _NS),
    "e_pirates": ("vscode", "s_pirates", 10, "big", _NS),
    "e_d11": ("vscode", "s_d11", 10, "big", _NS),
    "e_low40": ("vscode", "s_low40", 10, "big", _NS),
    "e_final": ("vscode", "final", 11, "big", _NS),          # lines 1 to 21: the four notes, the fence 7 to 15
    "t_clean": ("terminal", [("s_named", _LINT)]),
    "t_pirates": ("terminal", [("s_pirates", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    # The game. None taken yet; see the docstring.
    "game_last_sci": ("game", "Science, Siege with Boss: Corsair Queen as LECTURE 8 left her (state start, probe-only Low: 100%): the Morrigan picked from the contact list, a kralien_dreadnought, her Kralien or Torgoth escorts among the contacts"),
    "game_options_d5": ("game", "Server, the start screen, Siege: the Options panel with Difficulty at 5 and Corsair Queen on the Boss line, Start Mission in view"),
    "game_two_sci": ("game", "Science, state s_named (Low: 100%), a pirate night: the contact list with two named ships, Morrigan and Badb, and three small pirate fleets; the Morrigan picked. Restart until the fleets are pirate"),
    "game_kralien_sci": ("game", "NOT TAKEN, not on the board. Science, state s_named, a Kralien night (about one start in four): three Kralien fleets of four to six ships in the contact list, the Morrigan and the Badb with them. Restart until it rolls Kralien"),
    "game_no_fleets": ("game", "Science, state s_pirates ('75% Pirates' with an S): the Morrigan and the Badb in the contact list and NO escort fleets"),
    "game_log_pirates": ("game", "NOT TAKEN, not on the board (card_log_pirates instead). Not a console: LegendaryMissions\\mast.runtime.log after the s_pirates game, open in VS Code, the line `fleet_create: no fleet table for race 'pirates', so no fleet was made ...` in view (copy the log before the next start)"),
    # Cards
    "card_title": ("card", "title", {}),
    "card_log_pirates": ("card", "page", {"kicker": "LegendaryMissions\\mast.runtime.log - this line three times, one per fleet",
                                          "text": [_LOG_LINE], "find": ["race 'pirates'"]}),
    "card_levels": ("card", "table", {"heading": "Step 6 - `Difficulty:` - how big each fleet is", "nth": 2,
                                      "kicker": "Ships in one fleet, by level"}),
    "card_keys": ("card", "table", {"heading": "Step 7 - `Named:` - her own ships", "kicker": "The raider ships"}),
    "card_cannot": ("card", "table", {"heading": "Step 8 - Check it", "nth": 3, "kicker": "Lint says clean, and"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 10", "sub": "A Siege boss, part 3"}),
}


# Marks on the game stills (fractions of the 1280x960 frame, measured on the taken stills)
_SCI_TITLE = ("rect", 0.698, 0.055, 1.0, 0.1)        # Science read-out: the Morrigan's name in red, and 'raider'
_DIFF = ("rect", 0.565, 0.462, 0.97, 0.503)          # start screen: the Difficulty line (5)
_BOSS = ("rect", 0.6, 0.508, 0.97, 0.552)            # start screen: the Boss line (Corsair Queen)
_START = ("rect", 0.0, 0.948, 1.0, 1.0)              # start screen: Start Mission
_P_CHIP = ("rect", 0.698, 0.281, 0.803, 0.318)       # game_two_sci: the pirate-o chip, pressed
_P_BADB = ("rect", 0.698, 0.481, 0.93, 0.519)        # game_two_sci: the Badb's row
_P_MORR = ("rect", 0.698, 0.643, 0.93, 0.68)         # game_two_sci: the Morrigan's row
_P_LIST = ("rect", 0.698, 0.36, 0.93, 0.763)         # game_two_sci: all ten pirates
_NF_TWO = ("rect", 0.698, 0.643, 0.93, 0.722)        # game_no_fleets: Morrigan and Badb, the only pirates
_NF_LIST = ("rect", 0.698, 0.36, 0.93, 0.83)         # game_no_fleets: the raider list, Kralien and Skaraan around them

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_two_sci"},
        {"from": 1, "still": "game_last_sci", "marks": [_SCI_TITLE]},
        {"from": 3, "still": "e_final", "marks": [("lines", 7, 15)], "dim": True},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_the_six_lines": {"step": None, "beats": [
        {"from": 0, "still": "game_last_sci", "marks": [_SCI_TITLE]},
        {"from": 3, "still": "e_start", "marks": [("lines", 5, 13)]},
        {"from": 4, "still": "e_start", "marks": [("lines", 7, 7)]},
        {"from": 5, "still": "e_start", "marks": [("lines", 8, 8)]},
        {"from": 6, "still": "e_start", "marks": [("lines", 9, 11)]},
        {"from": 7, "still": "e_start", "marks": [("lines", 12, 12)]},
        {"from": 8, "still": "game_options_d5", "marks": [_BOSS]},
        {"from": 11, "still": "game_options_d5", "marks": [_START]},
    ]},
    "s03_make_her_arrive_at_once": {"step": 1, "beats": [
        {"from": 0, "still": "e_start", "marks": [("lines", 8, 8)]},
        {"from": 2, "still": "e_low100", "marks": [("text", 8, "100%")]},
        {"from": 5, "still": "game_last_sci", "marks": [_SCI_TITLE]},
        {"from": 7, "still": "e_low100", "marks": [("lines", 8, 8)]},
    ]},
    "s04_fleets_and_who_flies_them": {"step": 4, "beats": [
        {"from": 0, "still": "e_fleets", "marks": [("lines", 10, 10)]},
        {"from": 2, "still": "e_flies", "marks": [("lines", 9, 9)]},
        {"from": 4, "still": "e_flies", "marks": [("text", 9, "75% Pirate, 25% Kralien")]},
        {"from": 6, "still": "game_two_sci", "marks": [_P_LIST]},
        {"from": 10, "still": "e_flies", "marks": [("text", 9, "25% Kralien")]},
    ]},
    "s05_difficulty": {"step": 6, "beats": [
        {"from": 0, "still": "game_options_d5", "marks": [_DIFF]},
        {"from": 1, "still": "e_diff", "marks": [("lines", 11, 11)]},
        {"from": 2, "still": "e_diff", "marks": [("text", 11, "+2")]},
        {"from": 4, "still": "card_levels"},
        {"from": 5, "still": "card_levels", "marks": [("part", "r4")]},
        {"from": 7, "still": "card_levels", "marks": [("part", "r4")]},
    ]},
    "s06_her_own_ships": {"step": 7, "beats": [
        {"from": 0, "still": "e_diff", "marks": [("lines", 12, 12)]},
        {"from": 2, "still": "game_two_sci", "marks": [_P_MORR, _P_BADB]},
        {"from": 4, "still": "e_named", "marks": [("text", 12, "Morrigan pirate_brigantine")]},
        {"from": 6, "still": "e_named", "marks": [("text", 12, "Badb pirate_strongbow")]},
        {"from": 7, "still": "e_named", "marks": [("text", 12, "pirate_brigantine"), ("text", 12, "pirate_strongbow")]},
        {"from": 8, "still": "card_keys", "marks": [("part", "r5")]},
        {"from": 9, "still": "e_named", "marks": [("text", 12, "pirate_brigantine"), ("text", 12, "pirate_strongbow")]},
    ]},
    "s07_check_it_and_what_lint_can_t": {"step": 8, "beats": [
        {"from": 0, "still": "t_clean", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_clean", "marks": [("out", 1, 2)]},
        {"from": 4, "still": "card_cannot"},
        {"from": 5, "still": "e_pirates", "marks": [("text", 9, "Pirates")]},
        {"from": 5.5, "still": "t_pirates", "marks": [("out", 1, 2)]},
        {"from": 6, "still": "game_no_fleets", "marks": [_NF_TWO]},
        {"from": 8, "still": "game_no_fleets", "marks": [_NF_LIST]},
        {"from": 9, "still": "card_log_pirates"},
        {"from": 10, "still": "card_log_pirates", "marks": [("part", "find1")]},
        {"from": 13, "still": "card_cannot", "marks": [("part", "r1"), ("part", "r2")]},
    ]},
    "s08_play_it_and_count": {"step": 9, "beats": [
        {"from": 0, "still": "game_options_d5", "marks": [_DIFF, _BOSS]},
        {"from": 1, "still": "game_two_sci", "marks": [_P_CHIP]},
        {"from": 2, "still": "game_two_sci", "marks": [_P_MORR, _P_BADB]},
        {"from": 3, "still": "game_two_sci", "marks": [_P_LIST]},
        {"from": 5, "still": "game_options_d5", "marks": [_START]},
        {"from": 7, "still": "e_d11", "marks": [("text", 11, "11")]},
        {"from": 9, "still": "card_levels", "marks": [("part", "r6")]},
    ]},
    "s09_her_real_arrival": {"step": 10, "beats": [
        {"from": 0, "still": "e_low40", "marks": [("text", 8, "40%")]},
        {"from": 6, "still": "e_final", "marks": [("lines", 1, 4)]},
        {"from": 8, "still": "t_final", "marks": [("out", 1, 2)]},
        {"from": 9, "still": "card_next"},
    ]},
}
