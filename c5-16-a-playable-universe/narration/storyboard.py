"""Storyboard for c5-16-a-playable-universe: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the storyboards of Class 4. Caption numbers are those of shots.py (2026-10-18).

The lecture starts from Lecture 13's `MyUniverse`: Lecture 9's files with c5-12's three files and
c5-13's story.mast laid over them. Its only edit is the session card pasted at the very top of
kestrel_verge.amd ("final", the page's own example, `same_as`: ten lines of `//` notes and one
empty line). Everything else on the page is played, not typed, so the lecture is cards and game
stills around one editor view and one lint. Lines are looked up in the text (_ln).

NOT SHOWN AS WRITTEN: nothing is skipped in the editor. The run-through tables are drawn from the
page (rows 1 to 12 and 13 to 18), and the page's "if something goes wrong" table is not read in
the narration.

GAME STILLS. TAKEN 2026-10-22 in the real engine (exe of 10-22 16:09), 10/10. Probe-only
help, never on screen: the ship is moved beside the Assay Office on arrival (it sits beyond
Comms range), and for game_c16_win a third sitting from the same save reported four Gleaner
kills through quest_on_kill_shared, so the end screen's stats read 0 destroyed. The VICTORY
hail was already gone under the end screen when it was shot. game_c16_line shows the four
ships in front; the guards by the wreck were out of view.
Planned: Open
Universe probe: built in data/missions/_sandbox, saves backed up by game.py; never start the
game by hand for it. ONE game, FOUR windows, TWO sittings:
`python game.py c5-16-a-playable-universe start --state final --consoles server,helm,comms,weapons`
(seed=7, no probe patch). Marks are left off every game still until the stills are taken.
THE TWO SITTINGS: the probe is sandboxed, so its save is in _sandbox/common_data/saves and
survives a stop. Every start CLEARS that folder (a new game) unless PIC_RESUME_SAVES=1: start
sitting 2 with `PIC_RESUME_SAVES=1 python game.py c5-16-a-playable-universe start ...` and
it Continues sitting 1. Press order, sitting 1:
  1. Helm, at once: the handheld icon, Quests: game_c16_log (the three leads: The Second Colony,
     The Breaking Yard, The Third Colony; Kestrel Relay under Charted Locations).
  2. Comms: select Hollin Compact, Hail Hollin Compact: game_c16_levy (the answers, "Pay the
     relay levy" among them). Pay it. Select Hollin Compact again: game_c16_escort (Patrol and
     "Escort (300 cr)" in the list). Take the escort.
  3. Helm: Engage The Third Colony. On arrival: game_c16_tern (the Tern card and the orange
     Threat card "The Tern is guarded - hostiles on approach.").
  4. Quest Log: game_c16_ledger_open (The Third Colony Done, The Assay Ledger appeared).
  5. Engage The Second Colony. On arrival: game_c16_assay (the Assay Office card, the escort
     paid out). Comms: select Assay Office, Hail Deepwell Assembly: game_c16_fee (three answers,
     the first "Pay the search fee and ask about the Tern"). Pay it. Quest Log: game_c16_keep
     (The Assay Ledger Done, What the Gleaners Keep appeared).
  6. Close the game, all three windows, WITHOUT deleting the save (see the warning).
Sitting 2 (the same run line, same save):
  7. game_c16_continue: the crew at Assay Office where they stopped, the Quest Log as left.
  8. Engage What the Gleaners Keep. On arrival, all three cards up (the place, the guards, and
     "A Gleaner battle line is forming up between you and the Bone Pile."): game_c16_pile.
  9. A few seconds later, count the ships: game_c16_line (three guards by the wreck, four or
     five in front of the ship). Do not wait for more.
 10. game_c16_win (the VICTORY card and the end screen with "The Bone Pile is broken, and what
     was taken from the Tern is going home.") is NOT playable by hand: the page's own check
     told the game four Gleaner ships were destroyed. Take it the same way, with the devqueue
     or a probe patch that does it, and say so in the notes.
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


LECTURE = "c5-16-a-playable-universe"
TITLE = ("Class 5, Lecture 16", "A playable universe", "One whole evening, planned, played in two sittings and checked")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
FILE = "kestrel_verge.amd"
MAST = "story.mast"
TEMPLATE = "ou"

_EX = "c5-16-a-playable-universe/example"
_OVER = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1", "c5-13-battles-part-2"))

_F = _rd("c5-16-a-playable-universe", "example", "kestrel_verge.amd")
_CARD = _F[:_F.index("// One authored file")]

_W3 = _ln(_F, "//            system -4, -3")
_CARD_LAST = _W3 + 1
_CREW = _ln(_F, "// CREW")
_BUD = _ln(_F, "// BUDGET")
_BUD2 = _BUD + 1
_S1 = _ln(_F, "// SITTING 1")
_S2 = _ln(_F, "// SITTING 2")
_WORDS = _ln(_F, "// WORDS")

STATES = {
    # Lecture 13's files
    "start": {"folder": "c5-02-your-universe-file/example", "over": _OVER},
    # Step 2: the session card, at the very top, with one empty line after it. The page's own example.
    "final": {"base": "start", "edits": [("replace", FILE, "// One authored file", _CARD + "// One authored file")],
              "same_as": (_EX + "/kestrel_verge.amd",)},
}

_LINT = "sbs lint MyUniverse"
_NS = {"side": False}

STILLS = {
    # The editor. Each window shows the 21 lines round the line named.
    "e_card": ("vscode", "final", 11, "big", _NS),                  # lines 1 to 21: the session card at the top
    # the command prompt
    "t_lint": ("terminal", [("final", _LINT)]),
    "t_run2": ("session", ["sbs run server,helm,comms,weapons -m MyUniverse map=0 --dry-run"], {"state": "final"}),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c16_log": ("game", "Helm, the Quest Log open: the three leads, Kestrel Relay under Charted Locations"),
    "game_c16_levy": ("game", "Comms with Hollin Compact selected: the hail answers, 'Pay the relay levy' among them"),
    "game_c16_escort": ("game", "Comms with Hollin Compact selected again: Patrol and 'Escort (300 cr)' now offered"),
    "game_c16_tern": ("game", "Comms just after arriving at The Tern, the ship's own channel: the orange Threat line 'The Tern is guarded - hostiles on approach.' and the Tern charted"),
    "game_c16_ledger_open": ("game", "Helm, the Quest Log: The Third Colony Done and The Assay Ledger newly appeared"),
    "game_c16_assay": ("game", "Comms just after arriving at the Assay Office: the ship beside it, Assay Office charted, 'Quest complete: Hollin Compact: Escort'"),
    "game_c16_fee": ("game", "Comms with Assay Office selected, Hail Deepwell Assembly: three answers, 'Pay the search fee and ask about the Tern' first"),
    "game_c16_keep": ("game", "Helm, the Quest Log: The Assay Ledger Done and What the Gleaners Keep newly appeared"),
    "game_c16_continue": ("game", "The second sitting's first screen: Helm, the crew beside the Assay Office where they stopped"),
    "game_c16_pile": ("game", "Comms just after arriving at The Bone Pile: the guards' Threat line, the Bone Pile charted, and ours 'A Gleaner battle line is forming up...'"),
    "game_c16_line": ("game", "Weapons a few seconds later, zoomed out: the battle line of four Gleaner ships closing on the ship"),
    "game_c16_win": ("game", "The end screen on Comms: Game results, and the goal's own sentence 'The Bone Pile is broken, and what was taken from the Tern is going home.'"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_plan": ("card", "table", {"heading": "Step 1 - Plan the evening on paper", "nth": 1, "kicker": "One evening, two sittings"}),
    "card_rules": ("card", "list", {"heading": "Step 1 - Plan the evening on paper", "kicker": "Three rules for a plan"}),
    "card_checks": ("card", "table", {"heading": "Step 3 - Before you play", "nth": 1, "kicker": "Four checks before you play"}),
    "card_run1": ("card", "table", {"heading": "Step 4 - The run-through, first sitting", "nth": 1, "kicker": "First sitting: tick each row"}),
    "card_save": ("card", "rows", {"kicker": "The save between the sittings",
                                   "header": ["File", "Where", "Between sittings"],
                                   "rows": [["universe_save_the_kestrel_verge_1.yaml", "common_data\\saves", "Leave it alone"]]}),
    "card_run2": ("card", "table", {"heading": "Step 5 - The run-through, second sitting", "nth": 1, "kicker": "Second sitting: do not delete the save"}),
    "card_after": ("card", "table", {"heading": "Step 6 - After you play", "nth": 1, "kicker": "Three things to read afterward"}),
    "card_notyet": ("card", "table", {"heading": "Step 7 - What this universe does not do yet", "nth": 1, "kicker": "What this universe does not do yet"}),
    "card_rubric": ("card", "table", {"heading": "The capstone rubric", "nth": 1, "kicker": "Ten points make a universe you can put in front of a crew"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your own evening"}),
    "card_end": ("card", "title", {"kicker": "Class 5", "title": "A playable universe", "sub": "Well done"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "card_title"},
        {"from": 3, "still": "card_plan"},
        {"from": 4, "still": "card_run1"},
        {"from": 5, "still": "game_c16_win"},
        {"from": 6, "still": "card_notyet"},
    ]},
    "s02_plan_the_evening": {"step": 1, "beats": [
        {"from": 0, "still": "card_plan"},
        {"from": 4, "still": "card_plan", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 5, "still": "card_plan", "marks": [("part", "r4")]},
        {"from": 6, "still": "card_plan", "marks": [("part", "r6"), ("part", "r7")]},
        {"from": 7, "still": "card_rules"},
        {"from": 8, "still": "card_rules", "marks": [("part", "item1")]},
        {"from": 9, "still": "card_rules", "marks": [("part", "item2")]},
        {"from": 11, "still": "card_rules", "marks": [("part", "item3")]},
    ]},
    "s03_the_session_card": {"step": 2, "beats": [
        {"from": 0, "still": "e_card", "marks": [("lines", 1, _CARD_LAST)]},
        {"from": 1, "still": "e_card", "marks": [("text", 1, "//"), ("text", _CREW, "//")]},
        {"from": 2, "still": "e_card"},
        {"from": 3, "still": "e_card", "marks": [("lines", _CREW, _CREW)]},
        {"from": 4, "still": "e_card", "marks": [("lines", _BUD, _BUD2)]},
        {"from": 5, "still": "e_card", "marks": [("lines", _S1, _S2)]},
        {"from": 6, "still": "e_card", "marks": [("lines", _WORDS, _W3)]},
        {"from": 8, "still": "e_card", "marks": [("text", _WORDS, "signal ledger_read")]},
        {"from": 9, "still": "e_card", "marks": [("lines", _WORDS, _W3)]},
    ]},
    "s04_before_you_play": {"step": 3, "beats": [
        {"from": 0, "still": "card_checks"},
        {"from": 1, "still": "t_lint", "marks": [("span", 1, "0 error(s), 0 warning(s)")]},
        {"from": 2, "still": "card_checks", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_checks", "marks": [("part", "r3")]},
        {"from": 4, "still": "card_checks", "marks": [("part", "r4")]},
    ]},
    "s05_the_first_sitting": {"step": 4, "beats": [
        {"from": 0, "still": "card_run1"},
        {"from": 1, "still": "game_c16_log"},
        {"from": 2, "still": "game_c16_levy"},
        {"from": 3, "still": "game_c16_escort"},
        {"from": 5, "still": "card_run1", "marks": [("part", "r7")]},
        {"from": 6, "still": "game_c16_tern"},
        {"from": 7, "still": "game_c16_ledger_open"},
        {"from": 8, "still": "game_c16_assay"},
        {"from": 9, "still": "card_run1", "marks": [("part", "r9")]},
        {"from": 10, "still": "game_c16_fee"},
        {"from": 11, "still": "card_run1", "marks": [("part", "r11")]},
        {"from": 12, "still": "game_c16_keep"},
        {"from": 13, "still": "card_run1", "marks": [("part", f"r{i}c4") for i in range(1, 13)]},
    ]},
    "s06_close_it": {"step": 4, "beats": [
        {"from": 0, "still": "card_plan", "marks": [("part", "r4")]},
        {"from": 2, "still": "card_save"},
    ]},
    "s07_the_second_sitting": {"step": 5, "beats": [
        {"from": 0, "still": "t_run2", "marks": [("cmd", 1, "server,helm,comms,weapons")]},
        {"from": 1, "still": "game_c16_continue"},
        {"from": 2, "still": "game_c16_keep"},
        {"from": 3, "still": "card_run2", "marks": [("part", "r3")]},
        {"from": 4, "still": "game_c16_pile"},
        {"from": 6, "still": "game_c16_line"},
        {"from": 10, "still": "card_run2", "marks": [("part", "r4")]},
        {"from": 12, "still": "card_run2", "marks": [("part", "r6")]},
        {"from": 14, "still": "card_run2", "marks": [("part", "r6c3")]},
        {"from": 16, "still": "card_run2", "marks": [("part", "r6")]},
    ]},
    "s08_after_you_play": {"step": 6, "beats": [
        {"from": 0, "still": "card_after"},
        {"from": 1, "still": "card_after", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_after", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_after", "marks": [("part", "r3")]},
        {"from": 4, "still": "card_notyet"},
        {"from": 5, "still": "card_notyet", "marks": [("part", "r1")]},
        {"from": 6, "still": "card_notyet", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_notyet"},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item1"), ("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 7, "still": "card_rubric"},
        {"from": 8, "still": "card_end"},
    ]},
}
