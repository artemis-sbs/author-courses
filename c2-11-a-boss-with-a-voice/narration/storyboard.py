"""Storyboard for c2-11-a-boss-with-a-voice: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5 and 6 (c1-05's docstring has every kind of still and mark). Written 2026-10-15.

TWO PLACES, as in Lecture 10. The boss file is in data\\missions\\common_data\\bosses
(MISSION). The hook card is Lecture 10's, unchanged except for the test wait (CARDS):
LegendaryMissions\\corsair_queen\\__init__.mast. Every still that lints, or shows the card or
the file's place, is made by the Class 2 helper (scratchpad c2sbx\\c2pic.py, from C2PIC;
("derived", ...) in STILLS), which writes the state's boss file and the named card first,
or takes the card's folder away for None.

The boss file starts as Lecture 10 left it ("start"), takes this lecture's test numbers
(`Low: 100%`, `Fails when: 3 minutes`; the card's wait 10 seconds), and "final" is this
lecture's example, byte for byte.

GAME STILLS (all seven taken 2026-10-15 in one game, s_turn + card10; marks are rects measured on them). LegendaryMissions' own Siege,
Difficulty 5, Boss: Corsair Queen, consoles server, helm, comms:
    sbs run server,helm,comms -m LegendaryMissions
Put the boss file and the card of the state a note names into the game's own data\\missions
with the helper:
    python c2pic.py c2-11-a-boss-with-a-voice --place <state> <card or None> --to <data\\missions>
With the test states she arrives about four seconds in. The call waits on Comms in the list
named Incoming Hails, its row "<speaker> - <Title>"; choosing the row opens it in the
middle of the console, and the list becomes Back / Continue, then the answers. The
Morrigan's message is a Comms message titled with the objective's name (where on Comms it
is drawn is not confirmed from the code). Read in the library code; nobody has seen it yet.
"""
import os as _os

LECTURE = "c2-11-a-boss-with-a-voice"
TITLE = ("Class 2, Lecture 11", "A boss with a voice", "Capstone: her clock, her call, her answer")
MISSION = "common_data\\bosses"
FILE = "corsair_queen.amd"

_HERE = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))


def _read(*p):
    with open(_os.path.join(_HERE, *p), encoding="utf-8", newline="") as f:
        return f.read().replace("\r\n", "\n")


_L = _read("example", FILE).split("\n")
_BEAT = "\n".join(_L[91:99])            # lines 92 to 99: The Queen Calls (the Beat)
_TURN = "\n".join(_L[100:125])          # lines 101 to 125: Turn the Badb, The Badb Turns
_SECTIONS = "\n".join(_L[126:157])      # lines 127 to 157: Characters, Dialogue, the first answer
_ANSWER2 = _L[157]                      # line 158: the answer that leads to Orla
_ORLA = "\n".join(_L[158:168])          # lines 159 to 168: a blank line, The Badb Answers
_NOTES10 = "\n".join(_L[0:8])
_NOTES = "\n".join(_L[0:12])
_LOSE = "Lose: The Morrigan broke the line. The sector is hers."
_VOICE = "Speaker: morrigan\nSignal says: You have {time}, little ship. Then this sector is mine."
_FIRST = "- [We do not stand down.]() ; completes parley"

STATES = {
    "start": {"folder": "c2-10-siege-boss-quests/example", "skip": ("corsair_queen",),
              "same_as": "c2-10-siege-boss-quests/example/corsair_queen.amd"},
    # Step 1: the test numbers
    "s_test": {"base": "start", "edits": [("replace", FILE, "Low: 40%", "Low: 100%"),
                                          ("replace", FILE, "Fails when: 10 minutes", "Fails when: 3 minutes")]},
    # Step 2: her voice on the clock
    "s_voice": {"base": "s_test", "edits": [("replace", FILE, _LOSE + "\n", _LOSE + "\n" + _VOICE + "\n")]},
    # Step 4: the Beat that places the call
    "s_beat": {"base": "s_voice", "edits": [("append", FILE, "\n" + _BEAT + "\n")]},
    # Step 5: her people and her scene, at the very end
    "s_cast": {"base": "s_beat", "edits": [("append", FILE, "\n" + _SECTIONS + "\n")]},
    # Step 8: the answer that matters, and the two records above Characters
    "s_turn": {"base": "s_cast", "edits": [
        ("replace", FILE, _FIRST + "\n", _FIRST + "\n" + _ANSWER2 + "\n" + _ORLA + "\n"),
        ("replace", FILE, "\n## [Characters](characters)", "\n" + _TURN + "\n\n## [Characters](characters)")]},
    # Step 11: the real numbers, and the notes
    "final": {"base": "s_turn", "edits": [("replace", FILE, "Low: 100%", "Low: 40%"),
                                           ("replace", FILE, "Fails when: 3 minutes", "Fails when: 10 minutes"),
                                           ("replace", FILE, _NOTES10, _NOTES)],
              "same_as": "c2-11-a-boss-with-a-voice/example/corsair_queen.amd"},
}

_CARD = _read("..", "c2-10-siege-boss-quests", "example", "corsair_queen", "__init__.mast")
CARDS = {
    "card10": _CARD.replace("await delay_sim(90)", "await delay_sim(10)"),     # Step 1: the test wait
    "card_final": _CARD,                                                        # Lecture 10's, unchanged
}
CARD_SAME_AS = {"card_final": "c2-10-siege-boss-quests/example/corsair_queen/__init__.mast"}
CARD_START = "card_final"

_BOSS = "sbs lint common_data\\bosses"
_LM = "sbs lint LegendaryMissions"
_NS = {"side": False}
_CARDF = {"folder": ".", "file": "LegendaryMissions\\corsair_queen\\__init__.mast"}
_BOSSF = {"folder": ".", "file": "common_data\\bosses\\corsair_queen.amd"}

C2PIC = {
    "v_card": ("vscode", "s_cast", "card10", 5, "big", _CARDF),
    "v_boss_place": ("vscode", "final", "card_final", 14, "mid", _BOSSF),
    "v_card_place": ("vscode", "final", "card_final", 5, "mid", _CARDF),
    "t_voice": ("term", [("s_voice", "card10", _BOSS)]),
    "t_beat": ("term", [("s_beat", "card10", _BOSS)]),
    "t_cast": ("term", [("s_cast", "card10", _BOSS)]),
    "t_turn_boss": ("term", [("s_turn", "card10", _BOSS)]),
    "t_turn_lm": ("term", [("s_turn", "card10", _LM)], {"tail": 18}),
    "t_alone": ("term", [("final", None, _BOSS)]),
}

STILLS = {
    # the boss file, Side Bar hidden
    "e_voice": ("vscode", "s_voice", 32, "big", _NS),        # lines 22 to 42: Sink the Morrigan's fence
    "e_beat": ("vscode", "s_beat", 88, "big", _NS),          # the Beat at the end
    "e_cast_chars": ("vscode", "s_cast", 103, "big", _NS),   # lines 93 to 113: Characters
    "e_cast_dlg": ("vscode", "s_cast", 118, "big", _NS),     # lines 108 to 128: Dialogue, the first answer
    "e_turn_top": ("vscode", "s_turn", 110, "mid", _NS),     # Turn the Badb, The Badb Turns, the Characters line
    "e_turn_end": ("vscode", "s_turn", 155, "big", _NS),     # lines 145 to 165: the second answer, The Badb Answers
    "e_final": ("vscode", "final", 10, "big", _NS),
    "v_card": ("derived", "made by c2pic.py: the card, untouched, test wait"),
    "v_boss_place": ("derived", "made by c2pic.py: the boss file in common_data\\bosses, in the Side Bar"),
    "v_card_place": ("derived", "made by c2pic.py: the card in LegendaryMissions\\corsair_queen, in the Side Bar"),
    "t_voice": ("derived", "made by c2pic.py: lint the boss, the one warning"),
    "t_beat": ("derived", "made by c2pic.py: lint the boss, two warnings"),
    "t_cast": ("derived", "made by c2pic.py: lint the boss, back to one"),
    "t_turn_boss": ("derived", "made by c2pic.py: lint the boss, finished story"),
    "t_turn_lm": ("derived", "made by c2pic.py: lint LegendaryMissions, finished story (its end)"),
    "t_alone": ("derived", "made by c2pic.py: lint the boss with the card's folder gone"),
    # The game. None taken yet; see the docstring.
    "game_queen_hail": ("game", "Comms: Incoming Hails with the row 'The Corsair Queen - The Corsair Queen', just after she arrives. State s_cast (or s_turn), card10"),
    "game_queen_open": ("game", "Comms: the Queen's call opened: her face, her name, one take of her first block; then after Continue her offer 'Stand your ships down...' and the answers. State s_turn, card10. Take two: the first block, and the offer with both answers"),
    "game_queen_offer": ("game", "Comms: the Queen's call after Continue: her offer and the two answers 'We do not stand down.' and 'Badb, this is the TSN...'. State s_turn, card10"),
    "game_orla": ("game", "Comms: after 'Badb, this is the TSN...': First Mate Orla's face and name above her line, and the answers 'Then fly with us.' and 'Then stay out of our way.'. State s_turn, card10"),
    "game_turned_log": ("game", "Helm: the ship's log strip after 'Then fly with us.': Quest complete: The Queen Calls, Quest complete: Turn the Badb, Quest failed: Sink the Badb (whatever of them the one-line strip holds; the info panel's log tab shows them all). State s_turn, card10"),
    "game_badb_turns_log": ("game", "Helm's handheld, Quests: The Badb Turns selected, the pirate_strongbow drawn at the top and 'The Badb, flying with you'. State s_turn, card10, after 'Then fly with us.'"),
    "game_morrigan_msg": ("game", "Comms: the message from the Morrigan titled Sink the Morrigan, 'You have 2:00, little ship. Then this sector is mine.' (the engine said 2:00; the mock 1:59), about a minute after she arrives, read by clicking the header 'Morrigan (pirate)'. State s_voice, card10; do nothing after she arrives"),
    # Cards
    "card_title": ("card", "title", {}),
    "card_times": ("card", "table", {"heading": "Step 2 - Her voice on the clock", "nth": 2,
                                     "kicker": "When she calls the clock"}),
    "card_reads": ("card", "table", {"heading": "Step 6 - What the Siege does with her file",
                                     "kicker": "The Siege reads her file itself"}),
    "card_friend": ("card", "table", {"heading": "Hand her to a friend", "kicker": "What your friend gets"}),
    "card_rubric": ("card", "points", {"kicker": "The capstone rubric",
                                       "items": ["She is yours", "She is checked", "She plays", "She travels"]}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Class 3", "sub": "What a boarding party is"}),
}


# Marks on the game stills (fractions of the 1280x960 frame, measured on the taken stills)
_SPEAKER = ("rect", 0.27, 0.445, 0.9, 0.86)          # Comms: the face, the name and the line
_LINE = ("rect", 0.27, 0.775, 0.9, 0.86)             # Comms: the name and the line
_ANS1 = ("rect", 0.0, 0.878, 0.27, 0.92)             # Comms: the first answer on view
_ANS2 = ("rect", 0.0, 0.922, 0.27, 0.99)             # Comms: the second answer on view
_ANS_BOTH = ("rect", 0.0, 0.875, 0.27, 0.99)         # Comms: both answers on view
_HAIL = ("rect", 0.0, 0.85, 0.275, 0.94)             # Comms: Incoming Hails, 'The Corsair Queen - The Corsair Queen'
_MSG_HEAD = ("rect", 0.27, 0.05, 0.51, 0.099)        # Comms: the message header 'Morrigan (pirate)'
_MSG_TITLE = ("rect", 0.51, 0.262, 0.66, 0.29)       # the message's title, 'Sink the Morrigan'
_MSG_TEXT = ("rect", 0.51, 0.26, 0.995, 0.345)       # the message: title and 'You have 2:00, little ship...'
_STRIP = ("rect", 0.015, 0.49, 0.275, 0.53)          # Helm: the one-line strip, 'Quest complete: The Badb Turns'
_BT_ROW = ("rect", 0.0, 0.795, 0.36, 0.862)          # Quest Log: The Badb Turns, Done
_BT_SHIP = ("rect", 0.385, 0.175, 0.7, 0.3)          # its caption and the strongbow in 3D
_BT_FOUR = ("rect", 0.0, 0.65, 0.36, 0.93)           # Quest Log: The Queen Calls, Turn the Badb, The Badb Turns Done; Sink the Badb Failed

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_queen_open", "marks": [_SPEAKER]},
        {"from": 2, "still": "v_boss_place"},
        {"from": 3, "still": "game_queen_offer", "marks": [_ANS_BOTH]},
        {"from": 4, "still": "card_title"},
        {"from": 5, "still": "e_final", "marks": [("lines", 9, 12)]},
    ]},
    "s02_her_voice_on_the_clock": {"step": 2, "beats": [
        {"from": 0, "still": "e_voice", "marks": [("lines", 32, 34)]},
        {"from": 2, "still": "game_morrigan_msg", "marks": [_MSG_TEXT]},
        {"from": 3, "still": "game_morrigan_msg", "marks": [_MSG_HEAD]},
        {"from": 4, "still": "game_morrigan_msg", "marks": [_MSG_TITLE]},
        {"from": 5, "still": "e_voice", "marks": [("lines", 35, 36)]},
        {"from": 6, "still": "e_voice", "marks": [("lines", 35, 35)]},
        {"from": 7, "still": "e_voice", "marks": [("text", 35, "morrigan")]},
        {"from": 8, "still": "e_voice", "marks": [("lines", 36, 36)]},
        {"from": 9, "still": "e_voice", "marks": [("text", 36, "{time}")]},
        {"from": 11, "still": "card_times"},
    ]},
    "s03_the_one_warning_you_keep": {"step": None, "beats": [
        {"from": 0, "still": "t_voice", "marks": [("part", "run1:cmd")]},
        {"from": 1, "still": "t_voice", "marks": [("out", 1, 2)]},
        {"from": 3, "still": "e_voice", "marks": [("text", 35, "morrigan")]},
        {"from": 7, "still": "t_voice", "marks": [("span", 1, "dangling-speaker")]},
        {"from": 9, "still": "t_voice", "marks": [("span", 1, "`morrigan`")]},
    ]},
    "s04_hear_her": {"step": 3, "beats": [
        {"from": 0, "still": "e_voice", "marks": [("lines", 32, 32)]},
        {"from": 2, "still": "game_morrigan_msg", "marks": [_MSG_HEAD]},
        {"from": 3, "still": "game_morrigan_msg", "marks": [_MSG_TITLE]},
        {"from": 4, "still": "game_morrigan_msg", "marks": [_MSG_TEXT]},
        {"from": 6, "still": "e_voice", "marks": [("lines", 35, 36)]},
        {"from": 8, "still": "v_boss_place"},
    ]},
    "s05_place_the_call": {"step": 4, "beats": [
        {"from": 0, "still": "game_queen_hail"},
        {"from": 1, "still": "game_queen_hail", "marks": [_HAIL]},
        {"from": 3, "still": "e_beat", "marks": [("lines", 88, 95)]},
        {"from": 7, "still": "e_beat", "marks": [("lines", 92, 93)]},
        {"from": 8, "still": "t_beat", "marks": [("out", 1, 3)]},
        {"from": 9, "still": "t_beat", "marks": [("span", 1, "dangling-action-ref")]},
        {"from": 10, "still": "e_beat", "marks": [("text", 93, "queen_calls")]},
    ]},
    "s06_her_people_and_her_scene": {"step": 5, "beats": [
        {"from": 0, "still": "game_queen_offer", "marks": [_SPEAKER]},
        {"from": 1, "still": "game_queen_offer", "marks": [_LINE, _ANS_BOTH]},
        {"from": 2, "still": "e_cast_chars", "marks": [("lines", 97, 110)]},
        {"from": 5, "still": "e_cast_dlg", "marks": [("lines", 111, 127)]},
        {"from": 6, "still": "e_cast_chars", "marks": [("hashes", 97), ("hashes", 99), ("hashes", 105)]},
        {"from": 8, "still": "e_cast_dlg", "marks": [("lines", 113, 127)]},
        {"from": 10, "still": "e_cast_dlg", "marks": [("lines", 127, 127)]},
        {"from": 11, "still": "t_cast", "marks": [("out", 1, 3)]},
    ]},
    "s07_what_the_siege_does_with_her": {"step": 6, "beats": [
        {"from": 0, "still": "card_reads"},
        {"from": 8, "still": "v_card"},
    ]},
    "s08_an_answer_that_matters": {"step": 8, "beats": [
        {"from": 0, "still": "e_turn_end", "marks": [("lines", 154, 154)]},
        {"from": 1, "still": "game_orla", "marks": [_SPEAKER, _ANS_BOTH]},
        {"from": 3, "still": "e_turn_end", "marks": [("lines", 154, 154)]},
        {"from": 4, "still": "e_turn_end", "marks": [("lines", 156, 164)]},
        {"from": 5, "still": "e_turn_end", "marks": [("lines", 163, 163)]},
        {"from": 6, "still": "e_turn_end", "marks": [("text", 163, "; completes parley, completes turn_badb, fails sink_badb")]},
        {"from": 7, "still": "e_turn_end", "marks": [("text", 163, "completes parley")]},
        {"from": 8, "still": "e_turn_top", "marks": [("lines", 102, 102)]},
        {"from": 9, "still": "e_turn_top", "marks": [("lines", 114, 115)]},
        {"from": 10, "still": "e_turn_top", "marks": [("text", 115, "badb joins tsn")]},
        {"from": 12, "still": "game_badb_turns_log", "marks": [_BT_ROW]},
        {"from": 13, "still": "game_badb_turns_log", "marks": [_BT_SHIP]},
        {"from": 14, "still": "e_turn_top", "marks": [("lines", 97, 121), ("lines", 123, 123)]},
    ]},
    "s09_play_every_road": {"step": 10, "beats": [
        {"from": 0, "still": "t_turn_lm", "marks": [("part", "run1:last")]},
        {"from": 1, "still": "game_queen_hail", "marks": [_HAIL]},
        {"from": 3, "still": "game_queen_offer", "marks": [_LINE]},
        {"from": 4, "still": "game_queen_offer", "marks": [_ANS2]},
        {"from": 5, "still": "game_orla", "marks": [_ANS1]},
        {"from": 6, "still": "game_turned_log", "marks": [_STRIP]},
        {"from": 8, "still": "game_badb_turns_log", "marks": [_BT_FOUR]},
        {"from": 12, "still": "game_queen_offer", "marks": [_ANS1]},
    ]},
    "s10_hand_her_to_a_friend": {"step": None, "beats": [
        {"from": 0, "still": "v_boss_place"},
        {"from": 6, "still": "v_card_place"},
        {"from": 9, "still": "card_friend"},
        {"from": 11, "still": "t_alone", "marks": [("out", 1, 2), ("out", 1, 3)]},
    ]},
    "s11_the_rubric_and_what_comes_ne": {"step": None, "beats": [
        {"from": 0, "still": "card_rubric"},
        {"from": 6, "still": "card_next"},
    ]},
}
