"""Storyboard for c6-09-revising-between-sessions: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in the
Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22).

The lecture starts from `MyUniverse` as Lecture 8 left it: Class 5's files with c6-01..c6-08's laid
over them (kestrel_verge.amd = c6-08's example, campaign.md, playtest.md). The mission is drawn as
the lab, `RevisionLab` (MISSION), because every command on screen names the lab. The states:
"start" is the folder as the lab is copied; "lab" adds the one SAVE_SLOT line to story.mast;
"r1" is Step 4's round one (changes 1 to 7 of the page, built from the page's own text);
"strand" is Step 5's change 10 on "start" (the open step deleted); "cure" is Step 6's change 13
(the stranded step under a new key, `at once`). Lines are looked up in the text.

NOT SHOWN AS WRITTEN. (1) Scene 1 and the end of scene 7 say "the Quest Log": the book has no
screenshots for them and Class 6 stays off the game, so the editor shows the file (the gap where
the open step was, then the cure) and a card shows the page's own row of what the continued game
showed. (2) Scene 2 says "the save file beside kestrel_verge.amd": the book has no save text, so a
card says what a save holds (keys and states, no words) beside the file with a key marked.
(3) Scene 3's copy and rename in File Explorer is drawn by its result: the folder RevisionLab
beside MyUniverse. (4) The walk of scene 4 is not played; the page's table of where the lab stands
is drawn instead. (5) Round one is built from changes 1 to 7 as the page states them; the lint
terminal is the lab's own lint of that state (its mark is on a word lint prints for any warnings;
check it when the still is taken).

GAME STILLS. None.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))


def _rd(rel):
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


LECTURE = "c6-09-revising-between-sessions"
TITLE = ("Class 6, Lecture 9", "Revising between sessions", "What you may change while a crew is partway through")
MISSION = "RevisionLab"
TEMPLATE_BASE = "ou"
TEMPLATE = "ou"
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c6-09-revising-between-sessions/example"
_NS = {"side": False}

_OVER = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1", "c5-13-battles-part-2",
    "c6-01-from-one-session-to-twenty", "c6-02-what-the-game-remembers", "c6-03-designing-a-session",
    "c6-04-the-episode", "c6-05-campaign-architecture", "c6-06-reputation-arcs",
    "c6-07-mixing-the-play-styles", "c6-08-playtesting"))

_A0 = _rd("c6-08-playtesting/example/kestrel_verge.amd")
_M0 = _rd("c5-13-battles-part-2/example/story.mast")
_TEXT = {"start": {FILE: _A0, MAST: _M0}}
STATES = {"start": {"folder": "c5-02-your-universe-file/example", "over": _OVER}}


def _cut(text, first, upto):
    a = text.index(first)
    b = text.index(upto, a)
    return text[a:b]


def _state(name, base, edits):
    texts = dict(_TEXT[base])
    out = []
    for f, o, n in edits:
        assert texts[f].count(o) == 1, (name, f, o[:60], texts[f].count(o))
        texts[f] = texts[f].replace(o, n)
        out.append(("replace", f, o, n))
    _TEXT[name] = texts
    STATES[name] = {"base": base, "edits": out}


def _L(state, needle, nth=1, file=FILE, after=0):
    t = _TEXT[state][file]
    i = -1
    if after > 1:
        i = sum(len(x) + 1 for x in t.split(chr(10))[:after - 1]) - 1
        if t.find(needle, i + 1) < 0:
            i = -1
    for _ in range(nth):
        i = t.find(needle, i + 1)
        assert i >= 0, (state, needle[:50])
    return t.count("\n", 0, i) + 1


# Step 2: the one line under the title line
_state("lab", "start", [(MAST, 'default shared UNIVERSE_SELECT = "The Kestrel Verge"\n',
                         'default shared UNIVERSE_SELECT = "The Kestrel Verge"\ndefault shared SAVE_SLOT = 6\n')])
if _TEXT["lab"][MAST] == _rd(_EX + "/story.mast"):
    STATES["lab"]["same_as"] = (_EX + "/story.mast",)

# Step 4: round one
_GONE = _cut(_A0, "### [The Long Count: Enter It](s01_home)", "### [The Long Count: Two of Five](s02_go)")
_LEAD = """### [A Lamp for the Wren](x_lamp)
---
Scope: shared
Starts when: at once
Done when: reach 2, 2
Reward: 100 credits
---
The Compact wants a marker lamp left at the Wren, at (2, 2), so that nobody else has to find her by accident.

"""
_LOCKERS = """### [The Long Count: The Dunlin's Lockers](s02_log)
---
Scope: shared
Starts when: revealed
Done when: reach 4, 4
Then: reveal s03_go
---
Have the Dunlin's lockers counted at Kestrel Relay before anything else.

"""
_TWICE = ("### [The Long Count: Enter It Twice](s02_home)\n---\nScope: shared\nStarts when: revealed\n"
          "Done when: reach 0, 0\nThen: reveal s03_go")
_state("r1", "start", [
    (FILE, "### [The Long Count: Three of Five](s03_go)", "### [The Long Count: The Plover](s03_go)"),
    (FILE, "### [The Long Count: One of Five](s01_go)", "### [The Long Count: The Wren](s01_go)"),
    (FILE, "## [Dialogue](dialogue)", _LEAD + _LOCKERS + "## [Dialogue](dialogue)"),
    (FILE, _GONE, ""),
    (FILE, _TWICE, "### [The Long Count: Enter It Twice](s02_enter)\n---\nWas: s02_home\nScope: shared\n"
                   "Starts when: revealed\nDone when: reach 0, 0\nThen: reveal s02_log"),
    (FILE, "### [The Long Count: Her Log](s01_scan)", "### [The Long Count: Her Log](s01_log)"),
    (FILE, "Then: reveal s01_scan", "Then: reveal s01_log"),
])

# Step 5, change 10: the step the crew is on, deleted
_state("strand", "start", [(FILE, _cut(_A0, "### [The Long Count: Three of Five](s03_go)",
                                       "### [The Long Count: The Plover's Price](s03_ask)"), "")])
# Step 6, change 13: the stranded step under a new key, at once
_state("cure", "strand", [(FILE, "### [The Long Count: The Plover's Price](s03_ask)\n---\nScope: shared\nStarts when: revealed",
                           "### [The Long Count: The Plover's Price](s03_price)\n---\nScope: shared\nStarts when: at once")])

STILLS = {}


def _E(name, state, needle, off=0, file=FILE):
    opts = dict(_NS)
    if file != FILE:
        opts["file"] = file
    STILLS[name] = ("vscode", state, _L(state, needle, 1, file) + off, "big", opts)


_E("e_key", "start", "### [The Long Count: Three of Five](s03_go)")
_E("e_slot", "lab", "default shared SAVE_SLOT = 6", file=MAST)
_E("e_r1_plover", "r1", "(s03_go)", off=2)
_E("e_r1_wren", "r1", "(s01_go)", off=2)
_E("e_r1_lead", "r1", "### [A Lamp for the Wren](x_lamp)", off=1)
_E("e_r1_gap", "r1", "Then: reveal s01_home", off=2)
_E("e_r1_was", "r1", "Was: s02_home", off=1)
_E("e_r1_log", "r1", "(s01_log)", off=2)
_E("e_r1_lockers", "r1", "(s02_log)", off=1)
_E("e_strand", "strand", "(s03_ask)", off=-3)
_E("e_cure", "cure", "(s03_price)", off=3)
STILLS.update({
    "t_lint_lab": ("terminal", [("lab", "sbs lint RevisionLab")]),
    "t_lint_r1": ("terminal", [("r1", "sbs lint RevisionLab")]),
    "x_lab": ("explorer", "data\\missions", {"state": "lab", "add": {"MyUniverse": "dir"}}),
    "card_title": ("card", "title", {}),
    "card_halves": ("card", "points", {"kicker": "Two halves, joined by key", "items": [
        "The save holds what the crew did: keys and a state for each, no words.",
        "Your file holds what there is to do: the words, and the keys.",
        "Change your words and the crew sees new words. Change a key and the save does not know the record."]}),
    "card_stands": ("card", "table", {"heading": "Step 3 - Give the lab a campaign in progress", "nth": 1,
                                      "kicker": "Where the lab stands after two evenings"}),
    "card_lintwarn": ("card", "table", {"heading": "Step 4 - Round one: seven changes", "nth": 1,
                                        "kicker": "Round one: two warnings, both about the step deleted"}),
    "card_r1": ("card", "table", {"heading": "Step 4 - Round one: seven changes", "nth": 2,
                                  "kicker": "Round one: what the continued game showed"}),
    "card_r2": ("card", "table", {"heading": "Step 5 - Round two: putting back, and two traps", "nth": 1,
                                  "kicker": "Round two: what the continued game showed"}),
    "card_r3": ("card", "table", {"heading": "Step 6 - Round three: what gets a stranded step back", "nth": 1,
                                  "kicker": "Round three: the guide's cure, and a new key"}),
    "card_r3b": ("card", "table", {"heading": "Step 6 - Round three: what gets a stranded step back", "nth": 2,
                                   "kicker": "The same cure for the stranded step"}),
    "card_list": ("card", "table", {"heading": "Step 8 - The list", "nth": 1, "kicker": "What you may change between evenings"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your own lab"}),
})


def _tx(still, needle, words=None, nth=1, file=None):
    state = STILLS[still][1]
    file = file or STILLS[still][4].get("file", FILE)
    return ("text", _L(state, needle, nth, file, STILLS[still][2] - 10), words or needle)


def _ln(still, needle, count=1, file=FILE):
    state = STILLS[still][1]
    a = _L(state, needle, 1, file, STILLS[still][2] - 10)
    return ("lines", a, a + count - 1)


def _b(frm, still, *marks):
    d = {"from": frm, "still": still}
    if marks:
        d["marks"] = list(marks)
    return d


BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        _b(0, "card_title"),
        _b(3, "e_strand", _tx("e_strand", "(s03_ask)", "s03_ask")),
        _b(6, "card_r2", ("part", "r3")),
        _b(7, "e_cure"),
        _b(8, "card_list", ("part", "r11"), ("part", "r12")),
    ]},
    "s02_two_halves": {"step": 1, "beats": [
        _b(0, "card_halves"),
        _b(1, "card_halves", ("part", "item1")),
        _b(2, "e_key", _tx("e_key", "(s03_go)", "s03_go")),
        _b(3, "card_halves", ("part", "item1")),
        _b(4, "e_key", _tx("e_key", "(s03_go)", "s03_go")),
        _b(5, "card_halves"),
        _b(7, "card_halves", ("part", "item3")),
    ]},
    "s03_make_the_lab": {"step": 2, "beats": [
        _b(0, "card_halves"),
        _b(1, "x_lab"),
        _b(3, "e_slot"),
        _b(6, "e_slot", _tx("e_slot", "default shared SAVE_SLOT = 6")),
        _b(7, "e_slot", _tx("e_slot", "default shared SAVE_SLOT = 6", "SAVE_SLOT = 6")),
        _b(8, "t_lint_lab"),
    ]},
    "s04_a_campaign_in_progress": {"step": 3, "beats": [
        _b(0, "card_stands"),
        _b(3, "card_stands", ("part", "r4")),
        _b(4, "card_stands", ("part", "r5")),
        _b(5, "card_stands", ("part", "r6")),
        _b(6, "card_stands", ("part", "r7")),
        _b(7, "card_stands"),
    ]},
    "s05_round_one": {"step": 4, "beats": [
        _b(0, "e_r1_plover"),
        _b(1, "e_r1_plover", _tx("e_r1_plover", "(s03_go)", "The Plover")),
        _b(2, "e_r1_wren", _tx("e_r1_wren", "(s01_go)", "The Wren")),
        _b(3, "e_r1_lead", _ln("e_r1_lead", "### [A Lamp for the Wren](x_lamp)", 9)),
        _b(4, "e_r1_gap", _tx("e_r1_gap", "Then: reveal s01_home", "reveal s01_home")),
        _b(5, "e_r1_was", _tx("e_r1_was", "(s02_enter)")),
        _b(6, "e_r1_was", _tx("e_r1_was", "Was: s02_home")),
        _b(7, "e_r1_log", _tx("e_r1_log", "(s01_log)")),
        _b(8, "e_r1_lockers", _ln("e_r1_lockers", "### [The Long Count: The Dunlin's Lockers](s02_log)", 9)),
        _b(9, "t_lint_r1", ("span", 1, "warning(s)")),
        _b(10, "card_lintwarn", ("part", "r1"), ("part", "r2")),
        _b(11, "card_lintwarn"),
        _b(12, "card_r1"),
        _b(13, "card_r1", ("part", "r1"), ("part", "r2")),
        _b(14, "card_r1", ("part", "r3")),
        _b(15, "card_r1", ("part", "r4")),
        _b(16, "card_r1", ("part", "r5")),
        _b(17, "card_r1", ("part", "r6")),
        _b(18, "card_r1", ("part", "r7")),
    ]},
    "s06_round_two": {"step": 5, "beats": [
        _b(0, "card_r2", ("part", "r1")),
        _b(3, "card_r2", ("part", "r2")),
        _b(6, "e_strand"),
        _b(7, "e_strand", _tx("e_strand", "(s03_ask)", "s03_ask")),
        _b(8, "card_r2", ("part", "r3")),
    ]},
    "s07_getting_it_back": {"step": 6, "beats": [
        _b(0, "card_r3"),
        _b(1, "card_r3", ("part", "r1")),
        _b(2, "e_cure"),
        _b(5, "e_cure", _tx("e_cure", "(s03_price)", "s03_price")),
        _b(6, "e_cure", ("text", _L("cure", "(s03_price)") + 3, "Starts when: at once")),
        _b(7, "card_r3b", ("part", "r1")),
    ]},
    "s08_the_list": {"step": 8, "beats": [
        _b(0, "card_list"),
        _b(1, "card_list", ("part", "r1")),
        _b(2, "card_list", ("part", "r2"), ("part", "r3")),
        _b(4, "card_list", ("part", "r4")),
        _b(5, "card_list", ("part", "r10")),
        _b(6, "card_list", ("part", "r11")),
        _b(7, "card_list", ("part", "r12")),
    ]},
    "s09_your_turn": {"step": None, "beats": [
        _b(0, "card_exercise"),
        _b(1, "card_exercise", ("part", "item1")),
        _b(2, "card_exercise", ("part", "item4")),
        _b(4, "card_exercise", ("part", "item5")),
        _b(6, "card_exercise", ("part", "item6")),
    ]},
}


def _fit():
    """Every mark of an editor still must be inside the 14 lines it shows (T-10 .. T+3)."""
    rng = {}
    for sc in BOARD.values():
        for b in sc["beats"]:
            if STILLS[b["still"]][0] != "vscode":
                continue
            for m in b.get("marks", []):
                if m[0] == "lines":
                    lo, hi = m[1], m[2]
                elif m[0] == "text":
                    lo = hi = m[1]
                else:
                    continue
                a, z = rng.get(b["still"], (lo, hi))
                rng[b["still"]] = (min(a, lo), max(z, hi))
    for name, (lo, hi) in rng.items():
        t = STILLS[name]
        if lo < t[2] - 10 or hi > t[2] + 3:
            a, z = hi - 3, lo + 10
            assert a <= z, ("marks do not fit one window", name, lo, hi)
            STILLS[name] = t[:2] + (min(max(t[2], a), z),) + t[3:]


_fit()
