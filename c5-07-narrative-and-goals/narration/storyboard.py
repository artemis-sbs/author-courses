"""Storyboard for c5-07-narrative-and-goals: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 4 storyboards. Caption numbers are those of shots.py (2026-10-17). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 6 left it (kestrel_verge.amd = c5-06's example,
311 lines). The steps are typed in the video's order, each state one step on the one before:
Step 2, the chain: the Third Colony's `Then:` line ("c_then"), The Assay Ledger ("c_ledger"),
What the Gleaners Keep made `revealed` with its `Then:` and reward ("c_keep"), its new
briefing ("c_brief"); Step 3, the call to the miners ("d_hail", then "d_ledger" with its three
answers); Step 4, the Goals chapter ("final", the page's own example, 393 lines). "b_typo" is
Step 5's chain break (`tern_leger`), on "final".

NOT SHOWN AS WRITTEN: the page's tables inside the code blocks (the `## What the ledger leaves
out` and `## [Goals](goals)` lines in them end a heading's section for the picture tool), so the
cards for Step 2's and Step 4's tables are drawn as rows in the board's own words. "card_note" is
the page's note under Step 3 (the deed on the beat or in the answer), also as rows.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine for
them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the
sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-07-narrative-and-goals start --state final --consoles server,helm,comms`
Marks are left off every game still until the stills exist. Press order:
  1. Helm, at once, the handheld icon, Quests: game_c57_log3 (three entries, no Assay Ledger).
  2. Helm: engage The Third Colony, arrive at (1, -2): game_c57_tern (the wreck ahead).
  3. Helm, Quests: game_c57_ledger (The Assay Ledger newly in the log, its briefing).
  4. Comms: Assay Office, Hail: game_c57_hail (the two answers, Pay the search fee and
     Demand the entry). Pay the fee: game_c57_paid (the Ledger done, the payment).
  5. Helm, Quests: game_c57_keep (What the Gleaners Keep, with its briefing and table).
  6. Helm: engage What the Gleaners Keep, at (-4, -3): game_c57_pile (the Bone Pile ahead);
     Quests: game_c57_goal (Break the Bone Pile newly in the log).
  7. Fight the four hulls: game_c57_fight. When the last goes: game_c57_end (the end-of-game
     screen, the Win sentence and the citation under it). TAKEN 2026-10-22 with the kills
     reported by a probe (stats read 0 destroyed). There is no VICTORY hail: the end screen
     shows the citation.
Never caption a face or a clock time.
"""
LECTURE = "c5-07-narrative-and-goals"
TITLE = ("Class 5, Lecture 7", "Narrative and goals", "A story in chapters, and a last page")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-07-narrative-and-goals/example"

import os
_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
_NS = {"side": False}


def _read(rel):
    """A file of the course folder, with plain newlines."""
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as _fh:
        return _fh.read().replace("\r\n", "\n")


_TEXT = {}      # state -> {file: text}, kept so marks can find their lines
_OF = {}        # still -> (state, file)
STATES = {}
STILLS = {}


def _chain(base, steps):
    """Each step (name, [edits]) is one state on the one before it. An edit is (old, new) on FILE,
    (file, old, new), or ("write", file, text). Every old text must occur exactly once."""
    prev = base
    for name, edits in steps:
        texts = dict(_TEXT[prev])
        out = []
        for e in edits:
            if e[0] == "write":
                texts[e[1]] = e[2]
                out.append(("write", e[1], e[2]))
                continue
            if len(e) == 2:
                e = (FILE, e[0], e[1])
            f, o, n = e
            assert texts[f].count(o) == 1, (name, f, o[:50], texts[f].count(o))
            texts[f] = texts[f].replace(o, n)
            out.append(("replace", f, o, n))
        _TEXT[name] = texts
        STATES[name] = {"base": prev, "edits": out}
        prev = name


def _start(name, spec, texts):
    STATES[name] = spec
    _TEXT[name] = texts


def _same(state, *files):
    """The state must equal these files of the page's example, byte for byte."""
    for f in files:
        assert _TEXT[state][f] == _read(_EX + "/" + f), ("not the example", state, f)
    STATES[state]["same_as"] = tuple(_EX + "/" + f for f in files)


def _L(state, needle, nth=1, file=None):
    t = _TEXT[state][file or FILE]
    i = -1
    for _ in range(nth):
        i = t.find(needle, i + 1)
        assert i >= 0, (state, file, needle[:50], nth)
    return t.count("\n", 0, i) + 1


def _E(name, state, needle, nth=1, off=0, file=None):
    """An editor still centered on the line holding needle (plus off)."""
    line = _L(state, needle, nth, file) + off
    opts = {"side": False}
    if file and file != FILE:
        opts["file"] = file
    STILLS[name] = ("vscode", state, line, "big", opts)
    _OF[name] = (state, file or FILE)


def _tx(still, needle, words=None, nth=1):
    s, f = _OF[still]
    return ("text", _L(s, needle, nth, f), words or needle)


def _ln(still, needle, count=1, nth=1):
    s, f = _OF[still]
    a = _L(s, needle, nth, f)
    return ("lines", a, a + count - 1)


def _b(frm, still, *marks, **extra):
    d = {"from": frm, "still": still}
    if marks:
        d["marks"] = list(marks)
    d.update(extra)
    return d


def _sc(step, *beats):
    return {"step": step, "beats": list(beats)}


def _term(name, state, cmd="sbs lint " + "{M}"):
    STILLS[name] = ("terminal", [(state, cmd.replace("{M}", MISSION))])


def _game(name, what):
    STILLS[name] = ("game", what)


def _card(name, kind, **opts):
    STILLS[name] = ("card", kind, opts)


_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c5-06-jobs/example")},
       {FILE: _read("c5-06-jobs/example/" + FILE)})

_F = _read(_EX + "/" + FILE)
_LEDGER = _F[_F.index("### [The Assay Ledger](tern_ledger)"):_F.index("### [What the Gleaners Keep](lead_bone_pile)")]
_KEEPB = _F[_F.index("![](face://zim"):_F.index("## [Goals](goals)")].rstrip("\n") + "\n"
_GOALS = _F[_F.index("## [Goals](goals)"):_F.index("## [Dialogue](dialogue)")].rstrip("\n") + "\n"
_DH = _F[_F.index("\n### [Deepwell Hail](deepwell_hail)"):]
_HAIL = _DH[:_DH.index("\n### [The Ledger](deepwell_ledger)")]
_REST = _DH[len(_HAIL):]
_PEOPLE = "nobody buys people.\n"
_GO = "There is a place at (-4, -3) the Gleaners will not talk about. Go armed.\n"
_SECOND = "Starts when: at once\nDone when: reach -4, -3\n---\n"

_chain("start", [
    ("c_then", [("Done when: reach 1, -2\n---\n", "Done when: reach 1, -2\nThen: reveal tern_ledger\n---\n")]),
    ("c_ledger", [("### [What the Gleaners Keep](lead_bone_pile)", _LEDGER + "### [What the Gleaners Keep](lead_bone_pile)")]),
    ("c_keep", [(_SECOND, "Starts when: revealed\nDone when: reach -4, -3\nThen: reveal goal_bone_pile\nReward: 400 credits\n---\n")]),
    ("c_brief", [(_GO, _KEEPB)]),
    ("d_hail", [("% Run along, then.\n", "% Run along, then.\n" + _HAIL)]),
    ("d_ledger", [(_HAIL, _HAIL + _REST)]),
    ("final", [(_PEOPLE, _PEOPLE + "\n" + _GOALS)]),
])
_same("final", FILE)
_chain("final", [("b_typo", [("Then: reveal tern_ledger", "Then: reveal tern_leger")])])

_A1 = "[Pay the search fee and ask about the Tern](deepwell_ledger)"
_A2 = "[Demand the Tern's entry, now](deepwell_ledger_cold)"
_SHIP = "![](ship://wreck) The Tern, at (1, -2)."
_FACE = "![](face://zim"

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_then", "c_then", "Then: reveal tern_ledger", off=3)
_E("e_ledger", "c_ledger", _SHIP, off=1)
_E("e_keep0", "c_keep", "Then: reveal goal_bone_pile", off=2)
_E("e_keep", "c_brief", _FACE, off=2)
_E("e_hail", "d_ledger", "### [Deepwell Hail](deepwell_hail)", off=6)
_E("e_ans", "d_ledger", _A1, off=1)
STILLS["e_ans"] = STILLS["e_ans"][:3] + ("mid",) + STILLS["e_ans"][4:]
_E("e_goal", "final", "Win: The Bone Pile", off=1)
_E("e_goalthen", "final", "Then: reveal goal_bone_pile", off=2)
_E("e_typo", "b_typo", "Then: reveal tern_leger", off=3)
_term("t_final", "final")
_term("t_typo", "b_typo")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c57_log3", "Helm, the handheld icon then Quests: three entries, and no sign of The Assay Ledger")
_game("game_c57_tern", "Helm on arrival at (1, -2): the card reading The Tern with its line")
_game("game_c57_ledger", "Helm, Quests: The Assay Ledger newly in the log, its briefing with the table under it")
_game("game_c57_hail", "Comms, the Assay Office selected, Hail Deepwell Assembly: the greeting and the answers, Pay the search fee and Demand the entry")
_game("game_c57_paid", "Helm, Quests: The Assay Ledger done and paid, the Deepwell's standing a little higher")
_game("game_c57_keep", "Helm, Quests: What the Gleaners Keep newly in the log, with its briefing and the table of the ledger")
_game("game_c57_pile", "Helm on arrival at (-4, -3): the card reading The Bone Pile with its line")
_game("game_c57_goal", "Helm, Quests: Break the Bone Pile newly in the log, as the last chapter")
_game("game_c57_fight", "Helm, the four Gleaner hulls at the Bone Pile, the fight under way")
_game("game_c57_end", "The end-of-game screen: Game results, the Win sentence and the citation under it")

# drawn
_card("card_have", "table", heading="Step 1 - What you already have, and what is missing", kicker="Three lines you know")
_card("card_paper", "rows", kicker="The story as three lines on paper", header=["Chapter", "What the crew learns"],
      rows=[["One", "The third colony's ship is found, and she has been stripped"],
            ["Two", "The miners' ledger says who sold her cargo"],
            ["Three", "A place the Gleaners will not talk about"]])
_card("card_toc", "rows", kicker="Read down the Then lines", header=["Chapter", "Its Then line"],
      rows=[["The Third Colony", "Then: reveal tern_ledger"],
            ["The Assay Ledger", "Then: reveal lead_bone_pile"],
            ["What the Gleaners Keep", "Then: reveal goal_bone_pile"]])
_card("card_note", "rows", kicker="The deed: on the beat, or in the answer", header=["Where you write it", "Who gets it"],
      rows=[["On the beat", "Every ship in the game, whoever finished it, and whichever way"],
            ["In the answer", "The ship that gave the answer, and nobody else"],
            ["Rule of thumb", "The story's verdict goes on the beat. A choice goes in the answer"]])
_card("card_ending", "rows", kicker="A universe that does not have to end", header=["Your file", "What the crew gets"],
      rows=[["A Goals chapter, with Win:", "The game ends, won, on a last screen with your sentence"],
            ["No Goals chapter", "A sandbox, for as long as the crew likes"]])
_card("card_exercise", "list", heading="Exercise", kicker="A story in three lines")
_card("card_next", "title", kicker="Next", title="Lecture 8", sub="Captains and rivals")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c57_log3"),
        _b(6, "game_c57_ledger")),
    "s02_three_lines_on_paper": _sc(None,
        _b(0, "card_paper"),
        _b(1, "card_paper", ("part", "r1")),
        _b(2, "card_paper", ("part", "r2")),
        _b(3, "card_paper", ("part", "r3")),
        _b(4, "card_paper"),
        _b(5, "card_paper")),
    "s03_the_chain": _sc(2,
        _b(0, "card_have"),
        _b(1, "card_have", ("part", "r1")),
        _b(2, "card_have", ("part", "r2")),
        _b(3, "e_then", _tx("e_then", "Starts when: at once\nDone when: reach 1, -2", "Starts when: at once")),
        _b(4, "e_then", _tx("e_then", "Then: reveal tern_ledger")),
        _b(5, "e_ledger", _ln("e_ledger", "### [The Assay Ledger](tern_ledger)", 8)),
        _b(6, "e_ledger", _tx("e_ledger", "Then: reveal lead_bone_pile")),
        _b(7, "e_keep0", _ln("e_keep0", "### [What the Gleaners Keep](lead_bone_pile)", 8)),
        _b(8, "e_keep0", _tx("e_keep0", "Starts when: revealed\nDone when: reach -4, -3", "Starts when: revealed"), _tx("e_keep0", "Reward: 400 credits")),
        _b(9, "card_toc"),
        _b(10, "card_toc", ("part", "r1"), ("part", "r2"), ("part", "r3"))),
    "s04_the_briefing": _sc(2,
        _b(0, "e_ledger", _ln("e_ledger", _SHIP, 11)),
        _b(1, "e_ledger", _ln("e_ledger", _SHIP, 11)),
        _b(2, "e_ledger", _ln("e_ledger", "The Tern's holds are bare", 1)),
        _b(3, "e_ledger", _tx("e_ledger", "Hail the Assay Office at (3, 1) and ask.")),
        _b(4, "e_ledger", _tx("e_ledger", "Hail the Assay Office at (3, 1) and ask.", "(3, 1)")),
        _b(5, "e_ledger", _tx("e_ledger", "Done when: signal ledger_read")),
        _b(7, "e_ledger", _tx("e_ledger", "Done when: signal ledger_read", "signal ledger_read")),
        _b(8, "game_c57_ledger"),
        _b(9, "e_ledger", _tx("e_ledger", "Hail the Assay Office at (3, 1) and ask.")),
        _b(10, "e_ledger", _ln("e_ledger", "| What you found | What it tells you |", 5)),
        _b(11, "e_ledger", _tx("e_ledger", _SHIP)),
        _b(12, "e_ledger", _ln("e_ledger", "| What you found | What it tells you |", 5)),
        _b(13, "e_keep", _tx("e_keep", _FACE, "![](face://")),
        _b(15, "e_keep", _ln("e_keep", _FACE, 1)),
        _b(16, "e_keep", _tx("e_keep", "## What the ledger leaves out")),
        _b(18, "e_keep", _ln("e_keep", "The ledger has the Tern's cargo", 1)),
        _b(19, "e_keep", _ln("e_keep", "The ledger has the Tern's cargo", 1))),
    "s05_a_chapter_that_ends_in_a_cal": _sc(3,
        _b(0, "e_ledger", _tx("e_ledger", "Done when: signal ledger_read")),
        _b(1, "e_hail", _ln("e_hail", "### [Deepwell Hail](deepwell_hail)", 5)),
        _b(2, "e_hail", _ln("e_hail", "### [Deepwell Hail](deepwell_hail)", 5)),
        _b(3, "e_ans", _tx("e_ans", _A1, "signal ledger_read")),
        _b(5, "e_ans", _ln("e_ans", _A1, 2)),
        _b(6, "e_ans", _tx("e_ans", _A1, "signal ledger_read"), _tx("e_ans", _A2, "signal ledger_read")),
        _b(7, "e_ans", _tx("e_ans", _A1, "earns deepwell by-the-book 20, earns deepwell peaceful 20")),
        _b(9, "e_ans", _tx("e_ans", _A2, "earns deepwell resourceful 20, earns deepwell violent 20")),
        _b(11, "e_ans", _ln("e_ans", _A1, 2)),
        _b(12, "e_ans", _tx("e_ans", _A1, "earns deepwell by-the-book 20"), _tx("e_ans", _A2, "earns deepwell resourceful 20"))),
    "s06_on_the_beat_or_in_the_answer": _sc(3,
        _b(0, "card_note"),
        _b(1, "card_note", ("part", "r1")),
        _b(3, "card_note", ("part", "r1")),
        _b(5, "card_note", ("part", "r2")),
        _b(7, "card_note"),
        _b(8, "card_note", ("part", "r3")),
        _b(10, "e_ans", _ln("e_ans", _A1, 2))),
    "s07_the_last_page": _sc(4,
        _b(0, "e_goal", _ln("e_goal", "### [Break the Bone Pile](goal_bone_pile)", 7)),
        _b(1, "e_goal", _tx("e_goal", "Win: The Bone Pile", "Win:")),
        _b(2, "e_goal", _tx("e_goal", "Win: The Bone Pile", "The Bone Pile is broken, and what was taken from the Tern is going home.")),
        _b(4, "e_goal", _tx("e_goal", "Citation: Forty years late", "Citation:")),
        _b(5, "e_goal", _tx("e_goal", "Starts when: revealed\nDone when: destroy 4 enemies", "Starts when: revealed")),
        _b(6, "e_goalthen", _tx("e_goalthen", "Then: reveal goal_bone_pile")),
        _b(8, "t_final", ("part", "run1:clean")),
        _b(9, "e_typo", _tx("e_typo", "Then: reveal tern_leger", "tern_leger")),
        _b(10, "t_typo", ("out", 1, 1))),
    "s08_play_the_story": _sc(6,
        _b(0, "game_c57_log3"),
        _b(1, "game_c57_tern"),
        _b(2, "game_c57_ledger"),
        _b(4, "game_c57_hail"),
        _b(5, "game_c57_paid"),
        _b(7, "game_c57_keep")),
    "s09_the_end": _sc(6,
        _b(0, "game_c57_pile"),
        _b(1, "game_c57_goal"),
        _b(2, "game_c57_fight"),
        _b(3, "game_c57_end"),
        _b(5, "card_ending"),
        _b(6, "card_ending", ("part", "r1")),
        _b(7, "card_ending", ("part", "r2")),
        _b(8, "e_goal", _tx("e_goal", "Win: The Bone Pile", "Win:"))),
    "s10_your_turn": _sc(None,
        _b(0, "card_exercise"),
        _b(1, "card_exercise", ("part", "item1")),
        _b(2, "card_exercise", ("part", "item2")),
        _b(3, "card_exercise", ("part", "item3")),
        _b(5, "card_exercise", ("part", "item5")),
        _b(6, "card_next")),
}
