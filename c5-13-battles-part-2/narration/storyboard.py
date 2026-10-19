"""Storyboard for c5-13-battles-part-2: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py (2026-10-18).

The lecture starts from Lecture 12's `MyUniverse` (Lecture 9's files with c5-12's three files
laid over them). The one step is the card pasted at the very end of story.mast ("card", the
page's own example: story.mast `same_as`). Two variants for scene 6: "sig" (the route written
`//signal/`, so lint warns) and "nodelay" (the `await delay_sim(1)` line taken out).
Lines are looked up in the text (_ln), never typed. The card's long `prefab_spawn` line is shown
with the editor's word wrap on, so marks on its words land on the row that holds them.

NOT SHOWN AS WRITTEN: the page's two long tables of mistakes (only a few rows of the "lint cannot
see" table are drawn). The Open Universe numbers in the lesson (245 of 400 games) are not drawn;
scene 2's narration quotes a different count ("five of the nine systems"), so the card shows
the Breakers' own `Enemy mix: 60%` line instead.

GAME STILLS. NOT TAKEN YET: planned here, to be taken in one sitting in the real engine. Open
Universe probe: built in data/missions/_sandbox, saves backed up by game.py; never start the
game by hand for it. ONE game, THREE windows:
`python game.py c5-13-battles-part-2 start --state card --consoles server,helm,comms`
(seed=7, no probe patch). Marks are left off every game still until the stills are taken.
Press order:
  1. Helm: Quest Log, Engage The Third Colony (The Tern). Then Engage The Second Colony (Assay
     Office). Comms: hail the Assay Office, "Pay the search fee and ask about the Tern". Helm,
     Quest Log: game_c13_ledger (What the Gleaners Keep has appeared, the ledger step Done).
  2. Engage What the Gleaners Keep. On arrival, once all three cards are up (the place, the
     guards, and "A Gleaner battle line is forming up between you and the Bone Pile."):
     game_c13_arrive. A few seconds later, the 3D view or map with the line of ships about
     7,000 away and the guards by the wreck: game_c13_line.
  3. Run: Engage another place from the Quest Log, then open Charted Locations with The Bone
     Pile in it: game_c13_back. Engage it again and check that there is one line, not two.
  4. game_c13_raiders: the same arrival on a seed where The Bone Pile was NOT rolled an enemy
     system (try --seed 11, 13, 17 until the arrival has the guards and nothing else: three
     raiders). Take the Helm view of them.
  5. game_c13_nowait: `python game.py c5-13-battles-part-2 start --state nodelay ...` and the
     same path to the Bone Pile: the guards' card only, no battle line, no card of ours.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.join(_HERE, "..", "..")


def _rd(*parts):
    with open(os.path.join(_ROOT, *parts), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


def _ln(text, needle, nth=1):
    """The 1-based line of the nth place `needle` starts in text."""
    at = -1
    for _ in range(nth):
        at = text.index(needle, at + 1)
    return text.count("\n", 0, at) + 1


LECTURE = "c5-13-battles-part-2"
TITLE = ("Class 5, Lecture 13", "Battles, part 2", "A battle that waits for the story")
MISSION = "MyUniverse"
FILE = "kestrel_verge.amd"
MAST = "story.mast"
TEMPLATE = "ou"

_EX = "c5-13-battles-part-2/example"
_OVER9 = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1"))

_AMD = _rd("c5-12-battles-part-1", "example", "kestrel_verge.amd")
_M0 = _rd("c5-12-battles-part-1", "example", "story.mast")
_M1 = _rd("c5-13-battles-part-2", "example", "story.mast")
_CARD = _M1[_M1.index("#\n# The Bone Pile"):]
_ROUTE_OLD = "//shared/signal/universe_arrived"
_AWAIT = "    await delay_sim(1)\n"
_M_SIG = _M1.replace(_ROUTE_OLD, "//signal/universe_arrived")
_M_ND = _M1.replace(_AWAIT, "")

# story.mast, the finished card
_END0 = _M0.count("\n")                                   # last line of the file before the paste
_C_A = _ln(_M1, "#\n# The Bone Pile")
_ROUTE = _ln(_M1, _ROUTE_OLD)
_AW = _ln(_M1, "await delay_sim(1)")
_QA = _ln(_M1, "->END if not quest_is_active")
_BAT = _ln(_M1, "battle_at = universe_cell_origin")
_PF = _ln(_M1, "prefab_spawn(")
_IC = _ln(_M1, "universe_info_card(")
_LAST = _M1.rstrip("\n").count("\n") + 1
_QA_ND = _ln(_M_ND, "->END if not quest_is_active")
# kestrel_verge.amd
_GOAL_H = _ln(_AMD, "### [Break the Bone Pile](goal_bone_pile)")
_GOAL_D = _ln(_AMD, "Done when: destroy 4 enemies")
_GOAL_P = _ln(_AMD, "Four Gleaner hulls stand between you and them.")
_BRK = _ln(_AMD, "### [The Breakers](the_breakers)")
_BRK_E = _ln(_AMD, "Enemy mix: 60%")
_PILE = _ln(_AMD, "### [The Bone Pile](bone_pile)")
_PILE_AT = _ln(_AMD, "At: -4, -3")

STATES = {
    # Lecture 12's files
    "start": {"folder": "c5-02-your-universe-file/example", "over": _OVER9},
    # Step 2: the card, pasted at the very end of story.mast. The page's own example.
    "card": {"base": "start", "edits": [("append", MAST, "\n" + _CARD)], "same_as": (_EX + "/story.mast",)},
    # Scene 6: the route written without `shared` (lint warns)
    "sig": {"base": "card", "edits": [("replace", MAST, _ROUTE_OLD, "//signal/universe_arrived")]},
    # Scene 6: the one-second wait taken out
    "nodelay": {"base": "card", "edits": [("replace", MAST, _AWAIT, "")]},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}
_MC = {"file": MAST, "side": False, "wrap": True}
_ME = {"file": MAST, "side": False}

STILLS = {
    # The editor. Each window shows the 21 lines round the line named.
    "e_goal": ("vscode", "start", _GOAL_D, "big", _NS),              # the goal Break the Bone Pile
    "e_breakers": ("vscode", "start", _BRK_E, "big", _NS),           # the Breakers: Enemy mix 60%
    "e_pile": ("vscode", "start", _PILE_AT, "big", _NS),             # the Bone Pile's At line
    "e_end": ("vscode", "start", _END0 - 2, "big", _ME),             # the end of story.mast, before the paste
    "e_card": ("vscode", "card", _BAT, "big", _MC),                  # the pasted card (word wrap on)
    "e_nodelay": ("vscode", "nodelay", _QA_ND, "big", _MC),          # the card without its wait
    # the command prompt
    "t_lint": ("terminal", [("card", _LINT)]),
    "t_sig": ("terminal", [("sig", _LINT)]),
    "t_run": ("session", ["sbs run server,helm,comms -m MyUniverse map=0 --dry-run"], {"state": "card"}),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c13_ledger": ("game", "Helm, the Quest Log: the ledger step Done and What the Gleaners Keep newly appeared"),
    "game_c13_arrive": ("game", "Helm just after arriving at The Bone Pile: the place card, the guards' Threat card and ours 'A Gleaner battle line is forming up between you and the Bone Pile.' up together"),
    "game_c13_line": ("game", "The same system a few seconds later: a line of four or five ships about 7,000 away, the guards by the wreck"),
    "game_c13_back": ("game", "Helm, the Quest Log with Charted Locations open and The Bone Pile in it, after running and before engaging it again"),
    "game_c13_raiders": ("game", "A game where The Bone Pile was not made an enemy system: on arrival only the three guards by the wreck"),
    "game_c13_nowait": ("game", "The nodelay run at The Bone Pile: the guards' card only, no line of ships and no card of ours"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_dials": ("card", "rows", {"kicker": "Lecture 12: setting the odds",
                                    "header": ["Dial", "What it sets"],
                                    "rows": [["DIFFICULTY (settings.yaml)", "How many fleets, and how big"],
                                             ["DANGER (story.mast)", "How many systems are enemy systems"],
                                             ["ENCOUNTERS (story.mast)", "How close an enemy system's fleets wait"]]}),
    "card_budget": ("card", "table", {"heading": "Step 4 - The budget again", "nth": 1, "kicker": "The Bone Pile with a set piece in it"}),
    "card_seven": ("card", "table", {"heading": "Step 2 - The card", "nth": 2, "kicker": "The words you may change"}),
    "card_when": ("card", "table", {"heading": "Step 3 - How it is tied to the story", "nth": 1, "kicker": "When the battle line is made"}),
    "card_blind": ("card", "table", {"heading": "Step 5 - Check it", "nth": 2, "rows": (1, 2, 3, 4, 5, 6),
                                     "kicker": "Lint says clean for every one of these"}),
    "card_eye": ("card", "rows", {"kicker": "Check these by eye",
                                  "header": ["Look at", "It must be"],
                                  "rows": [["The route line", "//shared/signal/universe_arrived, with the landmark's two numbers joined by and, each with two equals signs"],
                                           ["ARRIVE_I and ARRIVE_J", "In capitals"],
                                           ["await delay_sim(1)", "The first line under the route"],
                                           ["The key in quotes", "In your .amd file, in round brackets, letter for letter"],
                                           ["The side's key", "The first word inside the quotes with raider"],
                                           ["The long line", "One line"],
                                           ["The card", "In the file once, at the end"]]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "One place where the fight must be there"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 14", "sub": "The Admiral: the game from above"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "card_dials"},
        {"from": 1, "still": "card_dials", "marks": [("part", "r1"), ("part", "r2")]},
        {"from": 2, "still": "card_dials", "marks": [("part", "r3")]},
        {"from": 3, "still": "e_goal", "marks": [("lines", _GOAL_H, _GOAL_H)]},
        {"from": 4, "still": "game_c13_arrive"},
        {"from": 5, "still": "game_c13_line"},
        {"from": 6, "still": "card_title"},
    ]},
    "s02_why_the_dice_aren_t_enough": {"step": 1, "beats": [
        {"from": 0, "still": "e_goal", "marks": [("lines", _GOAL_H, _GOAL_H)]},
        {"from": 1, "still": "e_goal", "marks": [("text", _GOAL_P, "Four Gleaner hulls stand between you and them.")]},
        {"from": 2, "still": "e_goal"},
        {"from": 3, "still": "card_budget", "marks": [("part", "r1")]},
        {"from": 4, "still": "e_breakers", "marks": [("text", _BRK_E, "Enemy mix: 60%")]},
        {"from": 8, "still": "card_budget", "marks": [("part", "r2")]},
        {"from": 9, "still": "game_c13_raiders"},
    ]},
    "s03_the_card": {"step": 2, "beats": [
        {"from": 0, "still": "e_card", "marks": [("lines", _C_A, _LAST)]},
        {"from": 1, "still": "e_card"},
        {"from": 3, "still": "e_end", "marks": [("lines", _END0, _END0)]},
        {"from": 4, "still": "e_card", "marks": [("lines", _C_A, _LAST)]},
        {"from": 5, "still": "e_card", "marks": [("lines", _PF, _PF)]},
    ]},
    "s04_read_it_top_to_bottom": {"step": 2, "beats": [
        {"from": 0, "still": "e_card", "marks": [("lines", _C_A, _LAST)]},
        {"from": 1, "still": "e_card", "marks": [("text", _ROUTE, "//shared/signal/universe_arrived")]},
        {"from": 2, "still": "e_card", "marks": [("text", _ROUTE, "universe_arrived")]},
        {"from": 3, "still": "e_card", "marks": [("lines", _ROUTE, _ROUTE)]},
        {"from": 4, "still": "e_card", "marks": [("text", _ROUTE, "if ARRIVE_I == -4 and ARRIVE_J == -3")]},
        {"from": 5, "still": "e_card", "marks": [("lines", _AW, _AW)]},
        {"from": 6, "still": "e_card", "marks": [("text", _QA, "quest_is_active(universe_shared_id(), \"goal_bone_pile\")")]},
        {"from": 7, "still": "e_card", "marks": [("text", _QA, "->END if not")]},
        {"from": 8, "still": "e_card", "marks": [("lines", _QA, _QA)]},
        {"from": 9, "still": "e_card", "marks": [("lines", _BAT, _PF)]},
        {"from": 10, "still": "e_card", "marks": [("lines", _IC, _IC)]},
    ]},
    "s05_the_seven_words": {"step": 2, "beats": [
        {"from": 0, "still": "card_seven"},
        {"from": 1, "still": "card_seven", "marks": [("part", "r1")]},
        {"from": 2, "still": "e_pile", "marks": [("text", _PILE_AT, "At: -4, -3")]},
        {"from": 3, "still": "e_card", "marks": [("text", _QA, "\"goal_bone_pile\"")]},
        {"from": 4, "still": "e_card", "marks": [("text", _PF, "\"race\": \"torgoth\""), ("text", _PF, "\"fleet_difficulty\": 9")]},
        {"from": 6, "still": "e_card", "marks": [("text", _PF, "\"gleaners, raider\"")]},
        {"from": 8, "still": "e_card", "marks": [("text", _PF, "battle_at.x + 6000"), ("text", _PF, "battle_at.z + 6000")]},
        {"from": 9, "still": "e_card", "marks": [("text", _IC, "A Gleaner battle line is forming up between you and the Bone Pile.")]},
    ]},
    "s06_shared_and_one_second": {"step": 2, "beats": [
        {"from": 0, "still": "e_card", "marks": [("lines", _ROUTE, _ROUTE), ("lines", _AW, _AW)]},
        {"from": 1, "still": "e_card", "marks": [("text", _ROUTE, "shared")]},
        {"from": 2, "still": "e_card", "marks": [("lines", _ROUTE, _ROUTE)]},
        {"from": 3, "still": "e_card", "marks": [("lines", _PF, _PF)]},
        {"from": 4, "still": "t_sig", "marks": [("span", 1, "signal-side-effect-spawn")]},
        {"from": 5, "still": "e_card", "marks": [("lines", _AW, _AW)]},
        {"from": 6, "still": "card_when"},
        {"from": 7, "still": "card_when", "marks": [("part", "r2")]},
        {"from": 8, "still": "e_nodelay", "marks": [("lines", _QA_ND - 1, _QA_ND)]},
        {"from": 9, "still": "e_nodelay", "marks": [("text", _QA_ND, "quest_is_active")]},
        {"from": 10, "still": "game_c13_nowait"},
    ]},
    "s07_when_the_battle_is_there": {"step": 3, "beats": [
        {"from": 0, "still": "card_when"},
        {"from": 2, "still": "card_when", "marks": [("part", "r1")]},
        {"from": 4, "still": "card_when", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_when", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_when", "marks": [("part", "r4")]},
        {"from": 8, "still": "card_when", "marks": [("part", "r5")]},
        {"from": 9, "still": "card_budget"},
        {"from": 10, "still": "card_budget", "marks": [("part", "r3")]},
        {"from": 11, "still": "card_budget", "marks": [("part", "r4")]},
        {"from": 12, "still": "card_budget", "marks": [("part", "r4c2")]},
    ]},
    "s08_check_and_play_it": {"step": 5, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("span", 1, "0 error(s), 0 warning(s)")]},
        {"from": 1, "still": "card_blind"},
        {"from": 2, "still": "card_eye"},
        {"from": 3, "still": "t_run", "marks": [("cmd", 1, "server,helm,comms")]},
        {"from": 4, "still": "game_c13_ledger"},
        {"from": 5, "still": "game_c13_arrive"},
        {"from": 8, "still": "game_c13_back"},
        {"from": 9, "still": "game_c13_line"},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 6, "still": "card_next"},
    ]},
}
