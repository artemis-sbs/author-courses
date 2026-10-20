"""Storyboard for c5-06-jobs: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 4 storyboards. Caption numbers are those of shots.py (2026-10-17). The small helpers
below only build the data and look a line number up in the text of the state, so a mark always
lands on the line it names.

The lecture starts from `MyUniverse` as Lecture 5 left it (kestrel_verge.amd = c5-05's example,
272 lines; story.mast and description.yaml from Lecture 2). The steps are typed in the video's
order: Patrol's ending ("d_patrol"), Salvage's ending and its deed ("salv_end", "salv_deed"),
the three more jobs ("j_survey", "j_relay", "j_strike"), then the sides' Offers lines
("o_hollin", then "final", the page's own example, 311 lines). Five variants of "final" are
Step 5's breakages: "b_three" (the number in words), "b_gizmo" (a good that is not there),
"b_gleaners" (the s on a side's key), "b_nocomma" (the deed with no comma), "b_icon" (a
misspelled icon).

GAME STILLS. NOT TAKEN YET: they are planned here and are taken in one sitting, by hand. NEVER
start the engine for them from this file: Open Universe rewrites the player's save. ONE game, FOUR
windows, on the sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-06-jobs start --state final --consoles server,helm,comms,science`
No probe patch. Marks are left off every game still until the stills exist. Press order:
  1. Comms: select the Assay Office (Deepwell Assembly): game_c56_assay (Wreck Survey and
     Relay Run among the buttons, each with its pay). Do not press them yet.
  2. Comms: select Hollin Compact at standing 0: game_c56_hollin0 (only Escort, 250 cr).
  3. Comms: Hail Hollin Compact, Pay the relay levy: game_c56_levy (the answer taken).
     Select the station again: game_c56_hollin_levy (Patrol 240 cr, Escort 300 cr).
  4. Comms: press both. Helm, the handheld icon, Quests: game_c56_log2 (Under Ship: Hollin
     Compact: Patrol and Hollin Compact: Escort, Patrol's objective Destroy 3 enemies).
  5. Helm: select Escort, Engage; on arrival at 3, 1: game_c56_escort_done.
  6. Comms: Assay Office, press Wreck Survey and Relay Run: game_c56_relay (the Quest Log
     with the Relay Run's briefing, the hourglass line); game_c56_briefing (Wreck Survey's
     briefing: the Assay Office drawn beside the first line); game_c56_log3 (three jobs under
     Ship).
  7. Helm: engage The Third Colony. Science: select the Tern, scan it: game_c56_tern.
  8. Helm: engage The Breaking Yard: game_c56_yard (the Gleaner hulls ahead; destroy three).
  9. Comms: the Gleaners' station, Hail The Gleaners, the bold answer. Select the station
     again: game_c56_gleaners_salvage (Salvage, 180 cr, on the list). Take it, pick up two tech.
 10. Comms: select Hollin Compact: game_c56_hollin_standing (its standing now shows the drop).
 11. Helm: engage the Relay Run, arrive at 0, 0: game_c56_relay_home. Comms, Hollin Compact:
     game_c56_hollin_again (Patrol 252 cr, Escort 315 cr).
Never caption a face or a clock time.
"""
LECTURE = "c5-06-jobs"
TITLE = ("Class 5, Lecture 6", "Jobs", "Work a crew can take again and again")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
TEMPLATE = "ou"        # game.py: the probe is made with sbs create -t ou, in the sandbox
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-06-jobs/example"

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
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example", "c5-05-the-map/example")},
       {FILE: _read("c5-05-the-map/example/" + FILE)})

_F = _read(_EX + "/" + FILE)


def _cut(a, b):
    return _F[_F.index(a):_F.index(b)]


_SURV = _cut("\n### [Wreck Survey](survey)", "\n### [Relay Run](relay_run)")
_RELAY = _cut("\n### [Relay Run](relay_run)", "\n### [Clear the Lanes](strike)")
_STRIKE = _cut("\n### [Clear the Lanes](strike)", "\n## [Regions]")

_chain("start", [
    ("d_patrol", [("Tier: 2\nReward: 200 credits\n", "Tier: 2\nDone when: destroy 3 enemies\nReward: 200 credits\n")]),
    ("salv_end", [("Reward: 150 credits\n---\nRecover", "Done when: recover 2 tech\nReward: 150 credits\n---\nRecover")]),
    ("salv_deed", [("Reward: 150 credits\n", "Reward: 150 credits, earns hollin selfish 20\n")]),
    ("j_survey", [("do not ask where it came from.\n", "do not ask where it came from.\n" + _SURV)]),
    ("j_relay", [(_SURV, _SURV + _RELAY)]),
    ("j_strike", [(_RELAY, _RELAY + _STRIKE)]),
    ("o_hollin", [("Offers: patrol, escort\n", "Offers: patrol, escort, strike\n")]),
    ("final", [("Offers: escort\n", "Offers: survey, relay_run\n")]),
])
_same("final", FILE)
_chain("final", [("b_three", [("destroy 3 enemies", "destroy three enemies")])])
_chain("final", [("b_gizmo", [("recover 2 tech", "recover 2 gizmos")])])
_chain("final", [("b_gleaners", [("destroy 3 enemies", "destroy 3 gleaners")])])
_chain("final", [("b_nocomma", [("Reward: 150 credits, earns", "Reward: 150 credits earns")])])
_chain("final", [("b_icon", [("icon://hourglass", "icon://hourglas")])])

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_jobs0", "start", "### [Escort](escort)", off=3)
_E("e_patrol", "d_patrol", "Done when: destroy 3 enemies")
_E("e_salv_end", "salv_end", "Done when: recover 2 tech")
_E("e_salv", "salv_deed", "Reward: 150 credits, earns hollin selfish 20")
_E("e_nocomma", "b_nocomma", "Reward: 150 credits earns")
_E("e_survey", "j_survey", "The Assembly wants", off=1)
_E("e_relay", "j_relay", "Done when: reach 0, 0", off=2)
_E("e_strike", "j_strike", "Tier: 3", off=3)
_E("e_sides_pre", "start", "Offers: patrol, escort", off=6)
_E("e_sides_h", "o_hollin", "Offers: patrol, escort, strike", off=6)
_E("e_sides", "final", "Offers: survey, relay_run", off=-6)
_E("e_escort", "final", "Done when: reach 3, 1")
_E("e_three", "b_three", "destroy three enemies")
_E("e_gizmo", "b_gizmo", "recover 2 gizmos")
_E("e_gleaners", "b_gleaners", "destroy 3 gleaners")
_E("e_patrol_f", "final", "Done when: destroy 3 enemies")

_term("t_final", "final")
_term("t_three", "b_three")
_term("t_nocomma", "b_nocomma")
_term("t_icon", "b_icon")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c56_assay", "Comms, the Assay Office selected: Wreck Survey and Relay Run among the buttons, each with its pay")
_game("game_c56_hollin0", "Comms, Hollin Compact at standing 0: one job button, Escort (250 cr), and no Patrol")
_game("game_c56_levy", "Comms, Hail Hollin Compact: the answer Pay the relay levy taken")
_game("game_c56_hollin_levy", "Comms, Hollin Compact selected again: Patrol (240 cr) and Escort (300 cr)")
_game("game_c56_log2", "Helm, the handheld icon then Quests: under Ship, Hollin Compact: Patrol and Hollin Compact: Escort, Patrol's objective Destroy 3 enemies")
_game("game_c56_escort_done", "Helm, the ship arrived at 3, 1: the Escort done and paid")
_game("game_c56_relay", "Helm, Quest Log: the Relay Run taken, its hourglass line and the clock running")
_game("game_c56_briefing", "Helm, Quest Log: Wreck Survey's briefing, the Assay Office's picture beside its first line")
_game("game_c56_log3", "Helm, Quest Log: three jobs under Ship")
_game("game_c56_tern", "Science, the Tern selected and scanned: a dead ship in the list")
_game("game_c56_yard", "Helm, at The Breaking Yard: the Gleaner hulls ahead, the patrol still to finish")
_game("game_c56_gleaners_salvage", "Comms, the Gleaners' station after the bold answer: Salvage (180 cr) among the buttons")
_game("game_c56_hollin_standing", "Comms, Hollin Compact selected: the standing lower than before the salvage")
_game("game_c56_relay_home", "Helm, the ship home at 0, 0: the Relay Run done inside its ten minutes")
_game("game_c56_hollin_again", "Comms, Hollin Compact selected again: Patrol (252 cr) and Escort (315 cr), back on the list")

# drawn
_card("card_title", "title")
_card("card_life", "table", heading="Step 1 - The life of a job", kicker="The life of a job")
_card("card_ends", "table", heading="Step 2 - Five endings", kicker="Five endings")
_card("card_lines", "table", heading="Step 3 - Three more jobs", nth=1, kicker="The new lines")
_card("card_icons", "table", heading="Step 3 - Three more jobs", nth=2, kicker="What the briefing draws")
_card("card_mistakes", "table", heading="Step 5 - Check it", nth=1, kicker="What lint catches")
_card("card_silent", "table", heading="Step 5 - Check it", nth=2, kicker="What lint does not read")
_card("card_fact1", "table", heading="Step 6 - Play it", nth=1, rows=(1, 1), kicker="What to know about jobs")
_card("card_fact2", "table", heading="Step 6 - Play it", nth=1, rows=(2, 2), kicker="What to know about jobs")
_card("card_exercise", "list", heading="Exercise", kicker="A job for each side")
_card("card_next", "title", kicker="Next", title="Lecture 7", sub="Narrative and goals")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c56_assay"),
        _b(4, "game_c56_log3"),
        _b(6, "game_c56_hollin_again")),
    "s02_the_life_of_a_job": _sc(1,
        _b(0, "card_life"),
        _b(1, "card_life", ("part", "r1")),
        _b(2, "card_life", ("part", "r2")),
        _b(3, "card_life", ("part", "r3")),
        _b(5, "card_life", ("part", "r4")),
        _b(6, "card_life", ("part", "r5")),
        _b(7, "e_jobs0", _ln("e_jobs0", "### [Patrol](patrol)", 18)),
        _b(8, "e_jobs0", _ln("e_jobs0", "### [Patrol](patrol)", 5), _ln("e_jobs0", "### [Salvage](salvage)", 5)),
        _b(9, "e_jobs0", _tx("e_jobs0", "Done when: reach 3, 1"))),
    "s03_five_endings": _sc(2,
        _b(0, "card_ends"),
        _b(2, "card_ends", ("part", "r1")),
        _b(3, "card_ends"),
        _b(4, "card_ends", ("part", "r1")),
        _b(5, "e_patrol", _tx("e_patrol", "Done when: destroy 3 enemies")),
        _b(6, "e_patrol", _tx("e_patrol", "enemies")),
        _b(8, "game_c56_log2"),
        _b(9, "e_patrol", _tx("e_patrol", "Done when: destroy 3 enemies"))),
    "s04_a_reward_that_costs_somethin": _sc(3,
        _b(0, "e_salv_end", _ln("e_salv_end", "### [Salvage](salvage)", 7)),
        _b(1, "e_salv_end", _tx("e_salv_end", "Done when: recover 2 tech")),
        _b(2, "e_salv_end", _tx("e_salv_end", "tech", nth=1)),
        _b(3, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", "Reward:")),
        _b(4, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", ",")),
        _b(5, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", "earns hollin selfish 20")),
        _b(7, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", "earns hollin selfish 20")),
        _b(8, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", "hollin")),
        _b(10, "e_salv", _tx("e_salv", "Reward: 150 credits, earns hollin selfish 20", ",")),
        _b(11, "e_nocomma", _tx("e_nocomma", "Reward: 150 credits earns", "credits earns")),
        _b(12, "t_nocomma", ("out", 1, 1))),
    "s05_three_more_jobs": _sc(3,
        _b(0, "e_survey", _ln("e_survey", "### [Wreck Survey](survey)", 5)),
        _b(1, "e_survey", _tx("e_survey", "Done when: scan 1 derelict")),
        _b(2, "e_relay", _ln("e_relay", "### [Relay Run](relay_run)", 6)),
        _b(3, "e_relay", _tx("e_relay", "Fails when: 10 minutes")),
        _b(4, "e_relay", _tx("e_relay", "Penalty: 60 credits")),
        _b(5, "card_lines", ("part", "r2")),
        _b(6, "e_strike", _tx("e_strike", "Tier: 3")),
        _b(7, "card_lines", ("part", "r4")),
        _b(8, "e_relay", _tx("e_relay", "Done when: reach 0, 0")),
        _b(9, "e_relay", _tx("e_relay", "reach 0, 0"))),
    "s06_the_briefing": _sc(3,
        _b(0, "e_survey", _ln("e_survey", "![](ship://starbase_industry)", 5)),
        _b(2, "card_lines", ("part", "r5")),
        _b(3, "game_c56_assay"),
        _b(4, "game_c56_briefing"),
        _b(5, "e_survey", _tx("e_survey", "![](ship://starbase_industry)")),
        _b(6, "card_icons", ("part", "r1")),
        _b(7, "game_c56_briefing"),
        _b(8, "e_survey", _ln("e_survey", "The Assembly wants", 3)),
        _b(9, "e_survey", _ln("e_survey", "The Assembly wants", 1)),
        _b(10, "e_survey", _ln("e_survey", "A scan is all they ask", 1)),
        _b(11, "card_icons", ("part", "r2"), ("part", "r3")),
        _b(12, "e_relay", _tx("e_relay", "icon://hourglass")),
        _b(13, "e_strike", _tx("e_strike", "icon://crosshair")),
        _b(14, "t_icon", ("out", 1, 1)),
        _b(15, "e_survey", _tx("e_survey", "starbase_industry")),
        _b(16, "card_icons", ("part", "r1"))),
    "s07_on_offer": _sc(4,
        _b(0, "e_sides_pre", _ln("e_sides_pre", "Offers: patrol, escort")),
        _b(1, "e_sides_pre", _tx("e_sides_pre", "Offers: patrol, escort"), _tx("e_sides_pre", "Offers: escort", nth=1) if False else _ln("e_sides_pre", "Offers: escort\n")),
        _b(2, "e_sides_h", _tx("e_sides_h", "strike")),
        _b(3, "e_sides", _tx("e_sides", "survey, relay_run")),
        _b(4, "e_sides_h", _ln("e_sides_h", "Offers: escort\n")),
        _b(5, "e_sides", _tx("e_sides", "Offers: survey, relay_run")),
        _b(6, "e_escort", _tx("e_escort", "reach 3, 1")),
        _b(7, "e_sides", _ln("e_sides", "Offers: survey, relay_run"))),
    "s08_check": _sc(5,
        _b(0, "t_final", ("part", "run1:clean")),
        _b(1, "card_silent"),
        _b(2, "card_mistakes", ("part", "r1")),
        _b(3, "card_mistakes", ("part", "r1")),
        _b(4, "card_silent"),
        _b(5, "e_three", _tx("e_three", "three")),
        _b(6, "t_three", ("part", "run1:clean")),
        _b(7, "e_gizmo", _tx("e_gizmo", "gizmos")),
        _b(8, "card_silent", ("part", "r4")),
        _b(9, "e_gleaners", _tx("e_gleaners", "3 gleaners")),
        _b(10, "card_silent", ("part", "r4")),
        _b(12, "e_patrol_f", _tx("e_patrol_f", "enemies"))),
    "s09_work_the_board": _sc(6,
        _b(0, "game_c56_hollin0"),
        _b(1, "game_c56_levy"),
        _b(2, "game_c56_hollin_levy"),
        _b(3, "game_c56_log2"),
        _b(4, "game_c56_escort_done"),
        _b(5, "game_c56_assay"),
        _b(6, "game_c56_relay"),
        _b(7, "game_c56_tern"),
        _b(9, "game_c56_yard")),
    "s10_paid_and_offered_again": _sc(6,
        _b(0, "game_c56_gleaners_salvage"),
        _b(2, "game_c56_hollin_standing"),
        _b(5, "game_c56_relay_home"),
        _b(6, "game_c56_hollin_again"),
        _b(8, "card_fact1"),
        _b(10, "card_fact2")),
    "s11_your_turn": _sc(None,
        _b(0, "card_exercise"),
        _b(1, "card_exercise", ("part", "item1")),
        _b(2, "card_exercise", ("part", "item2")),
        _b(3, "card_exercise", ("part", "item3")),
        _b(4, "card_exercise", ("part", "item4")),
        _b(5, "card_next")),
}
