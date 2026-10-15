"""Storyboard for c2-10-siege-boss-quests: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5 and 6 (c1-05's docstring has every kind of still and mark). Written 2026-10-15.

TWO PLACES. The boss file is in data\\missions\\common_data\\bosses (MISSION; make.py writes
every state there). Her hook card is LegendaryMissions\\corsair_queen\\__init__.mast, outside
that folder, so its text at each moment is in CARDS, and every still that needs the card in
place, or needs it gone, is made by the Class 2 helper (scratchpad c2sbx\\c2pic.py, from
C2PIC; they are ("derived", ...) in STILLS). The helper writes the state's boss file AND the
named card (or takes the card's folder away for None) before each one. That matters for
lint too: `sbs lint common_data\\bosses` reads LegendaryMissions to see who sends a signal.

The boss file starts as Lecture 9 left it ("start") and keeps the test numbers (`Low:
100%`, the 10-second wait on the card) until "final", which is this lecture's example, byte
for byte; "card_final" is the example's card, byte for byte (CARD_SAME_AS).

GAME STILLS (all ten taken 2026-10-15; marks are rects measured on them. game_three_obj, game_red_line
and game_nemain_sci needed a probe-only card patch, a 45 s delay before the broadcast and the wait
10 -> 40, since with map= the Nemain arrives before the consoles have joined). LegendaryMissions' own Siege,
Difficulty 5, Boss: Corsair Queen, consoles server, helm, science:
    sbs run server,helm,science -m LegendaryMissions
The boss file and the card for the state each note names can be put into the game's own
data\\missions with the helper:
    python c2pic.py c2-10-siege-boss-quests --place <state> <card or None> --to <data\\missions>
(take the card folder away again after: --place start None). The test states bring her
about four seconds in with nothing destroyed. The red line is the ship's log strip under the
left panel of a crew console (read in the library code; nobody has seen it yet). Sinking a
ship needs a crew; no game still here does.
"""
import os as _os

LECTURE = "c2-10-siege-boss-quests"
TITLE = ("Class 2, Lecture 10", "A Siege boss, part 3", "Objectives, a way to lose, and a hook")
MISSION = "common_data\\bosses"
FILE = "corsair_queen.amd"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))


def _read(*p):
    with open(_os.path.join(_HERE, *p), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_FIN = _read("example", FILE)
_L = _FIN.split("\n")
_BADB = "\n".join(_L[43:56])            # lines 44 to 56 of the finished file: Sink the Badb
_TWO = "\n".join(_L[57:84])             # lines 58 to 84: Her Reserve and Sink the Nemain
_PAGE = "\n".join(_L[36:42])            # lines 37 to 42: the Morrigan's page
_NOTES9 = "\n".join(_L[0:4])            # Lecture 9's four note lines are the first four here
_NOTES = "\n".join(_L[0:8])

_OLD_DONE = "Done when: signal siege_won\nReward: 600 credits"
_OBJ = "Objective: Destroy the Morrigan\nDone when: destroy 1 morrigan"
_LOSE = "Fails when: 30 seconds\nFatal: true\nLose: The Morrigan broke the line. The sector is hers."
_OLD_DESC = "The Queen's flagship Morrigan leads the last assault. Destroy her and every raider with her."
_NAMED = "Named: Morrigan pirate_brigantine, Badb pirate_strongbow"

STATES = {
    "start": {"folder": "c2-09-siege-boss-fields/example",
              "same_as": "c2-09-siege-boss-fields/example/corsair_queen.amd"},
    # Step 1: the test setting
    "s_low100": {"base": "start", "edits": [("replace", FILE, "Low: 40%", "Low: 100%")]},
    # Step 3: the objective means what it says
    "s_obj": {"base": "s_low100", "edits": [("replace", FILE, _OLD_DONE, _OBJ + "\nReward: 600 credits")]},
    # Step 4: a bonus
    "s_badb": {"base": "s_obj", "edits": [("append", FILE, "\n" + _BADB + "\n")]},
    # Step 5: a way to lose, then the real limit and the page
    "s_lose30": {"base": "s_badb", "edits": [("replace", FILE, _OBJ + "\n", _OBJ + "\n" + _LOSE + "\n")]},
    "s_page": {"base": "s_lose30", "edits": [
        ("replace", FILE, "Fails when: 30 seconds", "Fails when: 10 minutes"),
        ("replace", FILE, "Objective: Destroy the Morrigan\n", "Objective: Destroy the Morrigan within ten minutes\n"),
        ("replace", FILE, _OLD_DESC, _PAGE)]},
    # Step 7: the hook that comes with the game; Step 9: her own
    "s_bio": {"base": "s_page", "edits": [("replace", FILE, _NAMED + "\n", _NAMED + "\nHook: biomech_infestation\n")]},
    "s_hook": {"base": "s_bio", "edits": [("replace", FILE, "Hook: biomech_infestation", "Hook: corsair_queen_hook")]},
    # Step 10: the two objectives the hook drives
    "s_reserve": {"base": "s_hook", "edits": [("append", FILE, "\n" + _TWO + "\n")]},
    # Step 13: the real numbers, and the notes
    "final": {"base": "s_reserve", "edits": [("replace", FILE, "Low: 100%", "Low: 40%"),
                                              ("replace", FILE, _NOTES9, _NOTES)],
              "same_as": "c2-10-siege-boss-quests/example/corsair_queen.amd"},
}

_CARD_FINAL = _read("example", "corsair_queen", "__init__.mast")
_CL = _CARD_FINAL.split("\n")
_CARD7 = "\n".join(_CL[0:6]) + "\n    ->END\n"
_CARD10 = _CARD_FINAL.replace("await delay_sim(90)", "await delay_sim(10)")
CARDS = {
    "card7": _CARD7,                                                  # Step 9: the smallest hook
    "card10": _CARD10,                                                # Step 10: the reserve, test wait
    "card_quote": _CARD10.replace('"#f33")', '"#f33)'),   # Step 11: a quote mark out
    "card_final": _CARD_FINAL,
}
CARD_SAME_AS = {"card_final": "c2-10-siege-boss-quests/example/corsair_queen/__init__.mast"}

_BOSS = "sbs lint common_data\\bosses"
_LM = "sbs lint LegendaryMissions"
_NS = {"side": False}
_CARDF = {"folder": ".", "file": "LegendaryMissions\\corsair_queen\\__init__.mast"}
_BOSSF = {"folder": ".", "file": "common_data\\bosses\\corsair_queen.amd"}

C2PIC = {
    # VS Code on data\missions: the Siege's quests, the card, the two places
    "v_siege_quests": ("vscode", "s_low100", None, 24, "wide",
                       {"folder": ".", "file": "LegendaryMissions\\maps\\siege_quests.amd"}),
    "v_card7": ("vscode", "s_hook", "card7", 5, "big", _CARDF),
    "v_card10": ("vscode", "s_reserve", "card10", 5, "big", _CARDF),
    "v_card_quote": ("vscode", "s_reserve", "card_quote", 5, "big", _CARDF),
    "v_card_final": ("vscode", "final", "card_final", 5, "big", _CARDF),
    "v_boss_place": ("vscode", "final", "card_final", 10, "mid", _BOSSF),
    # the command prompt, with the card in place (or gone)
    # LegendaryMissions' listing is long: its prompts show the last 18 rows, where the summary is
    "t_hook_boss": ("term", [("s_hook", "card7", _BOSS)]),
    "t_hook_lm": ("term", [("s_hook", "card7", _LM)], {"tail": 18}),
    "t_reserve_boss": ("term", [("s_reserve", "card10", _BOSS)]),
    "t_reserve_lm": ("term", [("s_reserve", "card10", _LM)], {"tail": 18}),
    "t_quote": ("term", [("s_reserve", "card_quote", _LM)], {"tail": 18}),
    "t_gone": ("term", [("final", None, _BOSS)]),
}

STILLS = {
    # the boss file, Side Bar hidden
    "e_start": ("vscode", "start", 18, "big", _NS),
    "e_obj": ("vscode", "s_obj", 21, "big", _NS),
    "e_badb": ("vscode", "s_badb", 34, "big", _NS),
    "e_lose30": ("vscode", "s_lose30", 22, "big", _NS),
    "e_page": ("vscode", "s_page", 30, "big", _NS),
    "e_bio": ("vscode", "s_bio", 12, "big", _NS),
    "e_hook": ("vscode", "s_hook", 12, "big", _NS),
    "e_reserve": ("vscode", "s_reserve", 67, "mid", _NS),
    "e_final": ("vscode", "final", 14, "big", _NS),
    "v_siege_quests": ("derived", "made by c2pic.py: VS Code on data\\missions, siege_quests.amd"),
    "v_card7": ("derived", "made by c2pic.py: the seven-line card, in its folder"),
    "v_card10": ("derived", "made by c2pic.py: the card with the reserve, ten-second wait"),
    "v_card_quote": ("derived", "made by c2pic.py: the card with one quote mark taken out"),
    "v_card_final": ("derived", "made by c2pic.py: the finished card"),
    "v_boss_place": ("derived", "made by c2pic.py: the finished boss file, in common_data\\bosses"),
    "t_hook_boss": ("derived", "made by c2pic.py: lint the boss, the seven-line card in place"),
    "t_hook_lm": ("derived", "made by c2pic.py: lint LegendaryMissions, the seven-line card in place (its end)"),
    "t_reserve_boss": ("derived", "made by c2pic.py: lint the boss, the reserve in place"),
    "t_reserve_lm": ("derived", "made by c2pic.py: lint LegendaryMissions, the reserve in place (its end)"),
    "t_quote": ("derived", "made by c2pic.py: lint LegendaryMissions with a quote mark out of the card"),
    "t_gone": ("derived", "made by c2pic.py: lint the boss with the card's folder gone"),
    # The game. None taken yet; see the docstring.
    "game_siege_log": ("game", "Helm's handheld, Quests, a Siege with Boss: None: the Quest Log with the Siege's own quests, Repel the Siege, Break the Siege, Hold the Starbases, Break It in Time (all four Active with the default Survive Clock)"),
    "game_morrigan_log9": ("game", "Helm's handheld, Quests: Sink the Morrigan selected, as Lecture 9 left her (state s_low100, no card): no Objective line, the sentence 'The Queen's flagship Morrigan leads the last assault...'"),
    "game_badb_page": ("game", "Helm's handheld, Quests: Sink the Badb selected, its page with the pirate_strongbow drawn in 3D at the top and 'The Badb, the Queen's second ship' as her caption, centered ABOVE her. State s_reserve, card10"),
    "game_lost": ("game", "The end screen (any crew console) after Sink the Morrigan fails: the left rail with 'The Morrigan broke the line. The sector is hers.'. State s_lose30, no card: start, choose her, sit still about 32 seconds"),
    "game_morrigan_page": ("game", "Helm's handheld, Quests: Sink the Morrigan selected: State, Reward 600, the order 'Destroy the Morrigan within ten minutes', the brigantine in 3D, the paragraph, and the hourglass and skull lines. State s_reserve, card10"),
    "game_biomechs": ("game", "Science: the biomech chip on, its rows (all 'unknown': unscanned), the swarm that came with her. State s_bio, no card"),
    "game_red_line": ("game", "Helm: the red line 'The Corsair Queen has entered the sector.' in the ship's log strip under the left panel, just after she arrives. State s_reserve, card10"),
    "game_three_obj": ("game", "Helm's handheld, Quests: the list with Sink the Morrigan, Sink the Badb and Her Reserve beside the Siege's quests; no Sink the Nemain yet. State s_reserve, card10, within ten seconds of her arrival"),
    "game_nemain_sci": ("game", "Science: the Nemain selected on the MAP (her name in red at the top), about ten seconds after the Queen. State s_reserve, card10"),
    "game_nemain_log": ("game", "Helm's handheld, Quests: Her Reserve Done, Sink the Nemain in the list and selected, its brigantine drawn at the top. State s_reserve, card10, after the Nemain arrives"),
    # Cards
    "card_title": ("card", "title", {}),
    "card_tree": ("card", "table", {"heading": "Step 2 - Read how a Siege ends", "kicker": "The Siege's tree"}),
    "card_places": ("card", "table", {"heading": "Step 8 - A place for her own hook", "kicker": "Two places"}),
    "card_ship_line": ("card", "table", {"heading": "Step 10 - Hold a ship in reserve", "nth": 2,
                                         "kicker": "On the ship line, change four things"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 11", "sub": "A boss with a voice"}),
}


# Marks on the game stills (fractions of the 1280x960 frame, measured on the taken stills)
_RED = ("rect", 0.0, 0.49, 0.24, 0.555)              # Helm: the red line under the left panel
_SCI_TITLE = ("rect", 0.698, 0.055, 1.0, 0.1)        # Science read-out: the ship's name in red, and 'raider'
_QL_ROW5 = ("rect", 0.0, 0.433, 0.38, 0.5)           # Quest Log: Sink the Morrigan, the fifth row
_QL_SENT = ("rect", 0.385, 0.152, 0.995, 0.22)       # Quest Log: Lecture 9's sentence, 'every raider with her'
_SIEGE_FOUR = ("rect", 0.0, 0.146, 0.38, 0.43)       # Quest Log: the Siege's four quests
_BADB_ROW = ("rect", 0.0, 0.505, 0.38, 0.573)        # Quest Log: Sink the Badb
_BADB_SHIP = ("rect", 0.385, 0.2, 0.76, 0.335)       # the Badb's caption and her ship in 3D
_BADB_CAP = ("rect", 0.48, 0.2, 0.75, 0.24)          # the caption, centered above her
_LOST = ("rect", 0.015, 0.215, 0.27, 0.285)          # end screen: the Lose: sentence on the left rail
_MORR_PAGE = ("rect", 0.385, 0.07, 0.995, 0.515)     # Sink the Morrigan's page: time left, order, ship, icons
_BIO_CHIP = ("rect", 0.803, 0.238, 0.91, 0.278)      # Science: the biomech chip, pressed
_BIO_LIST = ("rect", 0.698, 0.4, 0.93, 0.81)         # Science: its rows (unscanned, so 'unknown')
_THREE = ("rect", 0.0, 0.437, 0.38, 0.643)           # Quest Log: Sink the Morrigan, Sink the Badb, Her Reserve
_NEM_TWO = ("rect", 0.0, 0.578, 0.38, 0.715)         # Quest Log: Sink the Nemain, and Her Reserve Done

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_red_line", "marks": [_RED]},
        {"from": 1, "still": "game_morrigan_log9", "marks": [_QL_SENT]},
        {"from": 3, "still": "card_title"},
        {"from": 4, "still": "game_nemain_sci", "marks": [_SCI_TITLE]},
        {"from": 5, "still": "e_reserve", "marks": [("lines", 54, 81)]},
        {"from": 6, "still": "v_card_final", "marks": [("lines", 5, 11)]},
    ]},
    "s02_how_a_siege_ends": {"step": 2, "beats": [
        {"from": 0, "still": "game_siege_log"},
        {"from": 2, "still": "game_siege_log", "marks": [_SIEGE_FOUR]},
        {"from": 4, "still": "v_siege_quests", "marks": [("hashes", 8), ("hashes", 16), ("hashes", 26), ("hashes", 37)]},
        {"from": 5, "still": "v_siege_quests", "marks": [("lines", 8, 14)]},
        {"from": 6, "still": "v_siege_quests", "marks": [("lines", 16, 24)]},
        {"from": 7, "still": "v_siege_quests", "marks": [("lines", 26, 35), ("lines", 37, 42)]},
        {"from": 8, "still": "e_start", "marks": [("lines", 18, 28)]},
        {"from": 9, "still": "e_start", "marks": [("lines", 23, 23)]},
        {"from": 10, "still": "e_start", "marks": [("lines", 24, 24)]},
        {"from": 11, "still": "card_tree"},
    ]},
    "s03_make_it_mean_what_it_says": {"step": 3, "beats": [
        {"from": 0, "still": "game_morrigan_log9", "marks": [_QL_ROW5]},
        {"from": 1, "still": "e_start", "marks": [("lines", 25, 25)]},
        {"from": 3, "still": "e_obj", "marks": [("lines", 25, 25)]},
        {"from": 4, "still": "e_obj", "marks": [("lines", 26, 26)]},
        {"from": 5, "still": "e_obj", "marks": [("text", 26, "morrigan")]},
        {"from": 7, "still": "e_start", "marks": [("text", 14, "Morrigan")]},
    ]},
    "s04_a_bonus_and_a_way_to_lose": {"step": 4, "beats": [
        {"from": 0, "still": "game_badb_page", "marks": [_BADB_ROW]},
        {"from": 1, "still": "game_badb_page", "marks": [_BADB_SHIP]},
        {"from": 2, "still": "e_badb", "marks": [("lines", 31, 44)]},
        {"from": 4, "still": "e_badb", "marks": [("lines", 41, 41)]},
        {"from": 5, "still": "e_badb", "marks": [("text", 41, "pirate_strongbow")]},
        {"from": 6, "still": "e_badb", "marks": [("text", 41, "The Badb, the Queen's second ship")]},
        {"from": 7, "still": "game_badb_page", "marks": [_BADB_CAP]},
        {"from": 8, "still": "e_lose30", "marks": [("lines", 27, 29)]},
        {"from": 9, "still": "e_lose30", "marks": [("lines", 27, 27)]},
        {"from": 10, "still": "e_lose30", "marks": [("lines", 28, 28)]},
        {"from": 11, "still": "e_lose30", "marks": [("lines", 29, 29)]},
        {"from": 12, "still": "e_lose30", "marks": [("lines", 27, 29)]},
        {"from": 13, "still": "game_lost"},
        {"from": 16, "still": "game_lost", "marks": [_LOST]},
        {"from": 17, "still": "e_page", "marks": [("lines", 27, 27)]},
        {"from": 18, "still": "e_page", "marks": [("lines", 25, 25)]},
        {"from": 20, "still": "e_page", "marks": [("lines", 32, 37)]},
        {"from": 21, "still": "game_morrigan_page", "marks": [_MORR_PAGE]},
        {"from": 22, "still": "e_page", "marks": [("lines", 32, 32), ("lines", 34, 34)]},
        {"from": 23, "still": "e_page", "marks": [("lines", 36, 37)]},
        {"from": 24, "still": "e_page", "marks": [("text", 36, "hourglass")]},
        {"from": 25, "still": "e_page", "marks": [("text", 37, "skull")]},
        {"from": 26, "still": "e_page", "marks": [("lines", 36, 37)]},
    ]},
    "s05_a_hook_that_is_already_writt": {"step": 7, "beats": [
        {"from": 0, "still": "e_page", "marks": [("lines", 25, 30)]},
        {"from": 2, "still": "e_bio", "marks": [("lines", 15, 15)]},
        {"from": 6, "still": "game_biomechs", "marks": [_BIO_CHIP, _BIO_LIST]},
        {"from": 8, "still": "e_bio", "marks": [("text", 15, "biomech_infestation")]},
    ]},
    "s06_where_a_hook_lives": {"step": 8, "beats": [
        {"from": 0, "still": "card_places"},
        {"from": 1, "still": "v_boss_place"},
        {"from": 2, "still": "card_places", "marks": [("part", "r2")]},
        {"from": 4, "still": "v_card7"},
        {"from": 8, "still": "card_places", "marks": [("part", "r2")]},
    ]},
    "s07_the_smallest_hook": {"step": 9, "beats": [
        {"from": 0, "still": "game_red_line", "marks": [_RED]},
        {"from": 3, "still": "v_card7", "marks": [("lines", 5, 7)]},
        {"from": 4, "still": "v_card7", "marks": [("lines", 5, 5)]},
        {"from": 5, "still": "v_card7", "marks": [("lines", 6, 6)]},
        {"from": 6, "still": "v_card7", "marks": [("lines", 7, 7)]},
        {"from": 7, "still": "e_hook", "marks": [("lines", 15, 15)]},
        {"from": 9, "still": "t_hook_boss", "marks": [("part", "run1:cmd"), ("out", 1, 2)]},
        {"from": 10, "still": "t_hook_lm"},
        {"from": 12, "still": "t_hook_lm", "marks": [("part", "run1:last")]},
        {"from": 14, "still": "t_hook_lm", "marks": [("span", 1, "`Civilian`"), ("span", 1, '"send_general_message"')]},
    ]},
    "s08_hold_a_ship_in_reserve": {"step": 10, "beats": [
        {"from": 0, "still": "game_nemain_sci", "marks": [_SCI_TITLE]},
        {"from": 3, "still": "v_card10", "marks": [("lines", 7, 10)]},
        {"from": 4, "still": "v_card10", "marks": [("lines", 7, 7)]},
        {"from": 5, "still": "v_card10", "marks": [("lines", 8, 8)]},
        {"from": 6, "still": "v_card10", "marks": [("lines", 9, 9)]},
        {"from": 7, "still": "v_card10", "marks": [("lines", 10, 10)]},
        {"from": 8, "still": "card_ship_line"},
    ]},
    "s09_the_objectives_the_hook_driv": {"step": None, "beats": [
        {"from": 0, "still": "game_nemain_log", "marks": [_NEM_TWO]},
        {"from": 2, "still": "e_reserve", "marks": [("lines", 61, 61)]},
        {"from": 3, "still": "e_reserve", "marks": [("lines", 62, 62)]},
        {"from": 5, "still": "e_reserve", "marks": [("text", 62, "sink_nemain")]},
        {"from": 6, "still": "e_reserve", "marks": [("lines", 72, 72)]},
    ]},
    "s10_check_it": {"step": 11, "beats": [
        {"from": 0, "still": "t_reserve_boss", "marks": [("part", "run1:cmd"), ("out", 1, 2)]},
        {"from": 1, "still": "t_reserve_lm", "marks": [("part", "run1:last")]},
        {"from": 2, "still": "v_card_quote", "marks": [("lines", 6, 6)]},
        {"from": 3, "still": "t_quote", "marks": [("part", "run1:last")]},
        {"from": 7, "still": "v_card10"},
        {"from": 9, "still": "t_reserve_lm", "marks": [("part", "run1:last")]},
    ]},
    "s11_play_it": {"step": 12, "beats": [
        {"from": 0, "still": "game_red_line", "marks": [_RED]},
        {"from": 2, "still": "game_three_obj", "marks": [_THREE]},
        {"from": 4, "still": "game_morrigan_page", "marks": [_QL_ROW5]},
        {"from": 5, "still": "game_morrigan_page", "marks": [_MORR_PAGE]},
        {"from": 6, "still": "game_nemain_sci", "marks": [_SCI_TITLE]},
        {"from": 7, "still": "game_nemain_log", "marks": [_NEM_TWO]},
        {"from": 8, "still": "e_final", "marks": [("lines", 14, 14)]},
        {"from": 9, "still": "v_card_final", "marks": [("lines", 7, 7)]},
    ]},
    "s12_keep_it_safe": {"step": None, "beats": [
        {"from": 0, "still": "v_boss_place"},
        {"from": 1, "still": "v_card_final"},
        {"from": 2, "still": "card_places"},
        {"from": 5, "still": "t_gone", "marks": [("span", 1, "unfired-signal")]},
        {"from": 7, "still": "v_card_final"},
        {"from": 9, "still": "card_next"},
    ]},
}
