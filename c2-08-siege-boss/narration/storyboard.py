"""Storyboard for c2-08-siege-boss: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5 and 6 (c1-05's docstring has every kind of still and mark). Written 2026-10-15.

THE FOLDER is not a mission of the student's: it is data\\missions\\common_data\\bosses, and
the one file in it is corsair_queen.amd (MISSION below; make.py writes every state there).
"start" is the copy, before a word is changed: LegendaryMissions' warlord.amd under the new
file name (its text is _WARLORD, as the game ships it on 2026-10-15). Each step is a state;
"final" is this lecture's example, byte for byte. A file-only still is taken with the Side
Bar hidden, so the window's title names the folder `bosses`, not `missions`.

STILLS OF THE FILE LIST (made by the Class 2 helper, scratchpad c2sbx\\c2pic.py, from C2PIC;
they are ("derived", ...) in STILLS): VS Code opened on data\\missions itself, as the page
has the student do, with the Side Bar showing where the file is. The helper writes the
state's file first, so each shows the state it names.

NO COMMAND STARTS THE GAME HERE. `sbs run server,helm,weapons -m LegendaryMissions` is a
drawn card of the page's own words (card_run); what it opens is game_start_lm.

GAME STILLS (all eight taken 2026-10-15; marks are rects measured on them). All are LegendaryMissions' own
Siege, Difficulty 5, with consoles server, helm, science:
    sbs run server,helm,science -m LegendaryMissions
(the script plays with weapons; Science is here because a ship is picked from its contact
list). The Boss line is on the Options panel at the right of the server's start screen.
To skip the start screen (tried 2026-10-15, works): add `map=siege var.BOSS_SELECT=Warlord`.
Two of them need the boss ON THE MAP quickly. Probe-only, never what the student does: a copy
of LegendaryMissions (or the file put back after) with `Low: 100%`, so the boss arrives about
four seconds in with nothing destroyed (Lecture 9 measures this).
"""
LECTURE = "c2-08-siege-boss"
TITLE = ("Class 2, Lecture 8", "A Siege boss, part 1", "Copy the Warlord, change the words")
MISSION = "common_data\\bosses"
FILE = "corsair_queen.amd"

_WARLORD = """// The Warlord - a named enemy flagship and reinforcement fleets that warp in when
// the siege's raiders thin out. Authored in the shared AMD quest vocabulary (the
// same grammar Open Universe uses). Drop another .amd in maps/bosses/ and it appears
// in the siege BOSS dropdown automatically - no code change.

# [Warlord](warlord)
---
Boss
Trigger: enemies_low
Low: 25%
Flies: 50% Kralien, 50% Torgoth
Fleets: 2
Difficulty: +1
Named: Warlord kralien_dreadnought
---
A raider warlord and their honor guard warp in to break the defenders.

## [Defeat the Warlord](defeat_warlord)
---
Quest
Scope: shared
State: active
Parent: siege_mission
Required: true
Done when: signal siege_won
Reward: 500 credits
---
Destroy the raider Warlord to break the siege for good.
"""

_NOTES_OLD = _WARLORD.split("\n\n# [")[0]
_NOTES_NEW = ("// The Corsair Queen - my first Siege boss. A copy of the Warlord with new names.\n"
              "// She arrives when the raiders thin out, with two escort fleets and one named flagship.")

STATES = {
    "start": {"folder": "c2-08-siege-boss/example", "edits": [("write", FILE, _WARLORD)]},
    # Step 3 and 4: the boss's name, then the flagship's
    "s_name": {"base": "start", "edits": [("replace", FILE, "# [Warlord](warlord)", "# [Corsair Queen](corsair_queen)")]},
    "s_named": {"base": "s_name", "edits": [("replace", FILE, "Named: Warlord ", "Named: Morrigan ")]},
    "s_iron": {"base": "s_named", "edits": [("replace", FILE, "Named: Morrigan ", "Named: Iron Duke ")]},
    # Step 5 and 6: her words
    "s_desc": {"base": "s_named", "edits": [(
        "replace", FILE, "A raider warlord and their honor guard warp in to break the defenders.",
        "The Corsair Queen watched the siege falter from the dark. Now she brings her own ships to finish it.")]},
    "s_obj": {"base": "s_desc", "edits": [
        ("replace", FILE, "## [Defeat the Warlord](defeat_warlord)", "## [Sink the Morrigan](sink_morrigan)"),
        ("replace", FILE, "Reward: 500 credits", "Reward: 600 credits"),
        ("replace", FILE, "Destroy the raider Warlord to break the siege for good.",
         "The Queen's flagship Morrigan leads the last assault. Destroy her and every raider with her.")]},
    # Step 7: the notes at the top
    "final": {"base": "s_obj", "edits": [("replace", FILE, _NOTES_OLD, _NOTES_NEW)],
              "same_as": "c2-08-siege-boss/example/corsair_queen.amd"},
    # Step 10: for testing
    "s_low90": {"base": "final", "edits": [("replace", FILE, "Low: 25%", "Low: 90%")]},
}

_LINT = "sbs lint common_data\\bosses"
_NS = {"side": False}
_TREE = {"folder": ".", "file": "common_data\\bosses\\corsair_queen.amd"}

C2PIC = {
    # VS Code on data\missions, the Side Bar showing the file's place
    "v_warlord": ("vscode", "start", None, 14, "mid",
                  {"folder": ".", "file": "LegendaryMissions\\maps\\bosses\\warlord.amd"}),
    "v_copy": ("vscode", "start", None, 6, "mid", _TREE),
    "v_final": ("vscode", "final", None, 10, "mid", _TREE),
}

STILLS = {
    # the copy, and each step (lines 1 to 28 at the start; 1 to 26 once the notes are two lines)
    "e_start": ("vscode", "start", 14, "big", _NS),
    "e_name": ("vscode", "s_name", 14, "big", _NS),
    "e_named": ("vscode", "s_named", 14, "big", _NS),
    "e_iron": ("vscode", "s_iron", 14, "big", _NS),
    "e_desc": ("vscode", "s_desc", 16, "big", _NS),
    "e_obj": ("vscode", "s_obj", 18, "big", _NS),
    "e_final": ("vscode", "final", 14, "wide", _NS),
    "e_low90": ("vscode", "s_low90", 14, "big", _NS),
    "t_dup": ("terminal", [("start", _LINT)]),
    "t_iron": ("terminal", [("s_iron", _LINT)]),
    "t_clean": ("terminal", [("final", _LINT)]),
    "v_warlord": ("derived", "made by c2pic.py: VS Code on data\\missions, warlord.amd open, its folder in the Side Bar"),
    "v_copy": ("derived", "made by c2pic.py: the copy in common_data\\bosses, in the Side Bar"),
    "v_final": ("derived", "made by c2pic.py: the finished file in common_data\\bosses, in the Side Bar"),
    # The game. None taken yet; see the docstring for how to start it.
    "game_start_lm": ("game", "Server, LegendaryMissions' start screen: Siege selected in the list on the left, the Options panel on the right with its Boss line (closed). No boss file in common_data\\bosses"),
    "game_boss_list_old": ("game", "Server, the start screen, Siege: the Boss drop-down OPEN, showing the game's own list (None, Continuous, Infestation, Ragnarok, Warlord). Before the copy exists: common_data\\bosses empty or absent"),
    "game_boss_list": ("game", "Server, the start screen, Siege: the Boss drop-down OPEN with Corsair Queen at the TOP, above the game's own four. common_data\\bosses holds this lecture's example file"),
    "game_queen_chosen": ("game", "Server, the start screen, Siege: the Options panel with Corsair Queen chosen on the Boss line (the page asks for this one)"),
    "game_warlord_sci": ("game", "Science, a Siege with Boss: Warlord after he has arrived: his flagship, named Warlord, picked from the contact list (probe-only Low: 100% in warlord.amd, so he comes about four seconds in)"),
    "game_warlord_log": ("game", "Helm's handheld (icon top left), Quests: the Quest Log with Defeat the Warlord selected, Active, Reward 500 credits, its sentence 'Destroy the raider Warlord...' in the pane. Same game as game_warlord_sci"),
    "game_morrigan_sci": ("game", "Science, a Siege with Boss: Corsair Queen after she has arrived: the Morrigan selected (her name in red at the top of the read-out). Unscanned raiders read `unknown` in the list; she was found with the `kralien-o` chip, so no escorts are named in the still. This lecture's example; probe-only Low: 100% (the script's Low: 90% needs two kills)"),
    "game_morrigan_log": ("game", "Helm's handheld, Quests: Sink the Morrigan selected, Active, Reward 600 credits, the sentence 'The Queen's flagship Morrigan leads the last assault...'. Same game as game_morrigan_sci"),
    # Cards
    "card_title": ("card", "title", {}),
    "card_folders": ("card", "table", {"heading": "Step 2 - Make your copy", "kicker": "Two folders of bosses"}),
    "card_run": ("card", "points", {"kicker": "In a command prompt in data\\missions",
                                    "items": ["sbs run server,helm,weapons -m LegendaryMissions",
                                              "No map= on the end: the server stops at the start screen"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 9", "sub": "A Siege boss, part 2"}),
}


# Marks on the game stills (fractions of the 1280x960 frame, measured on the taken stills)
_SCI_TITLE = ("rect", 0.698, 0.055, 1.0, 0.1)        # Science read-out: the boss's name in red, and 'raider'
_QL_ROW5 = ("rect", 0.0, 0.433, 0.38, 0.5)           # Quest Log: the boss's objective, the fifth row
_QL_SENT = ("rect", 0.385, 0.152, 0.995, 0.22)       # Quest Log: the objective's sentence in the pane
_SIEGE = ("rect", 0.02, 0.35, 0.49, 0.51)            # start screen: the Siege card on the left
_BOSS = ("rect", 0.6, 0.508, 0.97, 0.552)            # start screen: the Boss line
_BOSS_FOUR = ("rect", 0.65, 0.352, 0.96, 0.483)      # the open Boss list: Warlord, Ragnarok, Infestation, Continuous
_WARLORD_ROW = ("rect", 0.65, 0.352, 0.96, 0.385)    # the open Boss list: Warlord
_QUEEN_ROW = ("rect", 0.65, 0.32, 0.96, 0.352)       # the open Boss list: Corsair Queen, at the top

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_morrigan_sci", "marks": [_SCI_TITLE]},
        {"from": 1, "still": "game_morrigan_log", "marks": [_QL_ROW5]},
        {"from": 2, "still": "e_final", "marks": [("lines", 4, 26)], "dim": True},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_what_a_boss_is": {"step": None, "beats": [
        {"from": 0, "still": "game_start_lm", "marks": [_SIEGE]},
        {"from": 3, "still": "game_start_lm", "marks": [_BOSS]},
        {"from": 5, "still": "game_boss_list_old", "marks": [_BOSS_FOUR]},
        {"from": 6, "still": "v_warlord"},
    ]},
    "s03_read_the_warlord": {"step": 1, "beats": [
        {"from": 0, "still": "game_boss_list_old", "marks": [_WARLORD_ROW]},
        {"from": 2, "still": "game_warlord_sci", "marks": [_SCI_TITLE]},
        {"from": 4, "still": "game_warlord_log", "marks": [_QL_ROW5]},
        {"from": 5, "still": "v_warlord", "marks": [("lines", 6, 16), ("lines", 18, 28)]},
        {"from": 8, "still": "v_warlord", "marks": [("lines", 6, 16)]},
        {"from": 9, "still": "v_warlord", "marks": [("text", 6, "[Warlord]")]},
        {"from": 10, "still": "v_warlord", "marks": [("lines", 8, 8)]},
        {"from": 12, "still": "v_warlord", "marks": [("lines", 9, 10)]},
        {"from": 14, "still": "v_warlord", "marks": [("lines", 11, 12)]},
        {"from": 15, "still": "v_warlord", "marks": [("lines", 14, 14)]},
        {"from": 17, "still": "v_warlord", "marks": [("lines", 18, 28)]},
        {"from": 18, "still": "game_warlord_log", "marks": [_QL_ROW5]},
        {"from": 20, "still": "v_warlord", "marks": [("lines", 23, 23)]},
        {"from": 21, "still": "v_warlord", "marks": [("lines", 24, 24)]},
        {"from": 22, "still": "v_warlord", "marks": [("lines", 25, 25)]},
    ]},
    "s04_make_the_copy": {"step": 2, "beats": [
        {"from": 0, "still": "v_warlord"},
        {"from": 1, "still": "card_folders"},
        {"from": 3, "still": "v_copy"},
    ]},
    "s05_lint_it_before_you_change_a_": {"step": None, "beats": [
        {"from": 0, "still": "t_dup", "marks": [("part", "run1:cmd")]},
        {"from": 2, "still": "t_dup", "marks": [("out", 1, 2)]},
        {"from": 3, "still": "e_start", "marks": [("text", 6, "[Warlord]")]},
        {"from": 4, "still": "game_boss_list_old", "marks": [_BOSS_FOUR]},
        {"from": 5, "still": "t_dup", "marks": [("span", 1, "duplicate-boss-name")]},
    ]},
    "s06_rename_the_boss_and_the_flag": {"step": 3, "beats": [
        {"from": 0, "still": "e_name", "marks": [("text", 6, "[Corsair Queen]")]},
        {"from": 1, "still": "e_name", "marks": [("text", 6, "(corsair_queen)")]},
        {"from": 3, "still": "game_warlord_sci", "marks": [_SCI_TITLE]},
        {"from": 5, "still": "e_named", "marks": [("text", 14, "Morrigan")]},
        {"from": 6, "still": "e_iron", "marks": [("lines", 14, 14)]},
        {"from": 8, "still": "e_iron", "marks": [("text", 14, "Iron Duke")]},
        {"from": 9, "still": "e_iron", "marks": [("text", 14, "Iron")]},
        {"from": 10, "still": "e_iron", "marks": [("text", 14, "Duke")]},
        {"from": 12, "still": "t_iron", "marks": [("out", 1, 2)]},
        {"from": 13, "still": "t_iron", "marks": [("span", 1, "Write `Iron_Duke kralien_dreadnought`")]},
    ]},
    "s07_write_her_words": {"step": 5, "beats": [
        {"from": 0, "still": "e_desc", "marks": [("lines", 16, 16)]},
        {"from": 4, "still": "game_warlord_log", "marks": [_QL_ROW5, _QL_SENT]},
        {"from": 6, "still": "e_obj", "marks": [("lines", 18, 18), ("lines", 26, 26), ("lines", 28, 28)]},
        {"from": 8, "still": "e_obj", "marks": [("lines", 21, 25)]},
        {"from": 9, "still": "e_obj", "marks": [("text", 26, "credits")]},
        {"from": 10, "still": "e_final", "marks": [("lines", 1, 2)]},
        {"from": 11, "still": "t_clean", "marks": [("out", 1, 2), ("out", 1, 3)]},
    ]},
    "s08_see_her_in_the_list": {"step": 9, "beats": [
        {"from": 0, "still": "card_run"},
        {"from": 3, "still": "game_start_lm"},
        {"from": 4, "still": "game_start_lm", "marks": [_SIEGE]},
        {"from": 5, "still": "game_start_lm", "marks": [_BOSS]},
        {"from": 6, "still": "game_boss_list", "marks": [_QUEEN_ROW]},
        {"from": 7, "still": "game_boss_list", "marks": [_BOSS_FOUR]},
        {"from": 8, "still": "v_final"},
        {"from": 10, "still": "game_queen_chosen", "marks": [_BOSS]},
    ]},
    "s09_meet_her": {"step": 10, "beats": [
        {"from": 0, "still": "e_final", "marks": [("lines", 8, 8)]},
        {"from": 1, "still": "e_low90", "marks": [("lines", 8, 8)]},
        {"from": 4, "still": "game_morrigan_sci", "marks": [_SCI_TITLE]},
        {"from": 7, "still": "game_morrigan_log", "marks": [_QL_ROW5, _QL_SENT]},
        {"from": 8, "still": "game_morrigan_sci"},
        {"from": 11, "still": "e_final", "marks": [("lines", 8, 8)]},
    ]},
    "s10_keep_it_safe_and_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "v_final"},
        {"from": 7, "still": "card_exercise"},
        {"from": 8, "still": "card_next"},
    ]},
}
