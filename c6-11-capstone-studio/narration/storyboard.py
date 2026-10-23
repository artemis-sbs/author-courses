"""Storyboard for c6-11-capstone-studio: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in the
Class 5 storyboards. Caption numbers are those of shots.py (2026-10-22).

The lecture starts from the campaign folder, `KestrelVerge`, as Lecture 10 left it: Class 5's files
with c6-01..c6-08's laid over them (kestrel_verge.amd = c6-08's example). The states are the
page's steps typed in the video's order (after "l2": Lecture 2's three lines and two records, which
the page's Before-you-start says are already in the file; c6-08's example lacks them), each one on the one before; every inserted block is cut
out of the lecture's own finished file (example\\kestrel_verge.amd), and the last state must equal
it ("final", `same_as`): "e4" Step 3 (Four of Five's Then line and the two new steps), "e5a" Step 4
(Five of Five's Then line and The Skua's Price), "e5b" the two held-back answers, "e5c" the two
reply records, "tt" Step 5 (the title), "f1" Step 6's Then line on Five Boats, "final" While They
Read. "camp" is "final" with the page's own campaign.md laid in, for the editor only.

NOT SHOWN AS WRITTEN. (1) The Quest Log of scenes 1, 3, 7 and 8 and the game's hail of scene 8 are
not shown: Class 6 stays off the game. Cards show the page's own rows of what each sitting
measured, and the first scene shows campaign.md instead of the Quest Log. (2) Scene 4's "is that
safe for the save" is a card in the page's own words (the reasons under Step 3's last paragraph).
(3) Scene 9's "table of sittings" is the page's text only as far as campaign.md has it: the
editor shows campaign.md's own "Act One, as played" (unmarked, the file wraps); the page's Step 10
rule table is drawn for the single win. (4) The lint terminal is marked on words the page shows it
printing; check them when the still is taken.

GAME STILLS. None.
"""
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))


def _rd(rel):
    with open(os.path.join(_ROOT, rel), encoding="utf-8", newline="") as fh:
        return fh.read().replace("\r\n", "\n")


LECTURE = "c6-11-capstone-studio"
TITLE = ("Class 6, Lecture 11", "Capstone studio", "Build it, play it, write down what happened")
MISSION = "KestrelVerge"
TEMPLATE_BASE = "ou"
TEMPLATE = "ou"
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c6-11-capstone-studio/example"
_NS = {"side": False}

_OVER = tuple(f"{d}/example" for d in (
    "c5-03-sides-diplomacy-goods", "c5-04-reputation", "c5-05-the-map", "c5-06-jobs",
    "c5-07-narrative-and-goals", "c5-08-captains-and-rivals", "c5-09-organizing-a-big-universe",
    "c5-12-battles-part-1", "c5-13-battles-part-2",
    "c6-01-from-one-session-to-twenty", "c6-02-what-the-game-remembers", "c6-03-designing-a-session",
    "c6-04-the-episode", "c6-05-campaign-architecture", "c6-06-reputation-arcs",
    "c6-07-mixing-the-play-styles", "c6-08-playtesting"))

_A0 = _rd("c6-08-playtesting/example/kestrel_verge.amd")
_FIN = _rd(_EX + "/kestrel_verge.amd")
_CAMP = _rd(_EX + "/campaign.md")
_TEXT = {"start": {FILE: _A0}}
STATES = {"start": {"folder": "c5-02-your-universe-file/example", "over": _OVER}}


def _cut(text, first, upto):
    a = text.index(first)
    return text[a:text.index(upto, a)]


def _state(name, base, edits, **extra):
    texts = dict(_TEXT[base])
    out = []
    for e in edits:
        if e[0] == "write":
            texts[e[1]] = e[2]
            out.append(e)
            continue
        f, o, n = e
        assert texts[f].count(o) == 1, (name, f, o[:60], texts[f].count(o))
        texts[f] = texts[f].replace(o, n)
        out.append(("replace", f, o, n))
    _TEXT[name] = texts
    STATES[name] = dict({"base": base, "edits": out}, **extra)


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


_FIVE = "### [The Long Count: Five of Five](s05_go)"
_BOATS = "### [The Long Count: Five Boats](act1_close)"
_BACK = "- [Back away](gleaner_bye)"
_DLG = "## [Dialogue](dialogue)"
_REC = _FIN[_FIN.index("### [The Skua's Log](gleaner_skua)"):]

_MAN = "- [Ask to see the Tern's manifest](hollin_manifest)"
_SELL = "- [Sell them a copy of the Count](gleaner_sold)"
_state("l2", "start", [
    (FILE, "Done when: reach 3, 1\n---\nThe Deepwell Assembly keeps",
     "Done when: reach 3, 1\nThen: learn the assay office buys salvage\n---\nThe Deepwell Assembly keeps"),
    (FILE, _MAN, _cut(_FIN, "- [Report what the Gleaners said]", _MAN) + _MAN),
    (FILE, _SELL, _cut(_FIN, "- [Ask what became of the Tern's boats]", _SELL) + _SELL),
    (FILE, "### [The Manifest](hollin_manifest)",
     _cut(_FIN, "### [The Boats](gleaner_boats)", "### [The Manifest](hollin_manifest)") + "### [The Manifest](hollin_manifest)")])
_state("e4", "l2", [
    (FILE, "Done when: reach 4, -2\nThen: reveal s05_go", "Done when: reach 4, -2\nThen: reveal s04_scan"),
    (FILE, _FIVE, _cut(_FIN, "### [The Long Count: Her Beacon](s04_scan)", _FIVE) + _FIVE)])
_state("e5a", "e4", [
    (FILE, "Done when: reach -3, -2\nThen: reveal act1_close", "Done when: reach -3, -2\nThen: reveal s05_ask"),
    (FILE, _BOATS, _cut(_FIN, "### [The Long Count: The Skua's Price](s05_ask)", _BOATS) + _BOATS)])
_state("e5b", "e5a", [(FILE, _BACK, _cut(_FIN, "- [Buy the Skua's log]", _BACK) + _BACK)])
_state("e5c", "e5b", [("write", FILE, _TEXT["e5b"][FILE] + "\n" + _REC)])
_state("tt", "e5c", [(FILE, "### [The Long Count: Three of Five](s03_go)", "### [The Long Count: The Plover](s03_go)")])
_state("f1", "tt", [(FILE, "Done when: reach 0, 0\nReward: 1000 credits",
                     "Done when: reach 0, 0\nThen: reveal act2_wait\nReward: 1000 credits")])
_state("final", "f1", [(FILE, _DLG, _cut(_FIN, "### [The Long Count: While They Read](act2_wait)", _DLG) + _DLG)],
       same_as=(_EX + "/kestrel_verge.amd",))
assert _TEXT["final"][FILE] == _FIN, "the chain does not end at the page's example"
_state("camp", "final", [("write", "campaign.md", _CAMP)], same_as=(_EX + "/kestrel_verge.amd", _EX + "/campaign.md"))

STILLS = {}


def _E(name, state, needle, off=0, file=FILE, **extra):
    opts = dict(_NS)
    opts["file"] = file
    opts.update(extra)
    STILLS[name] = ("vscode", state, _L(state, needle, 1, file) + off, "big", opts)


_E("e_e4a", "e4", "Then: reveal s04_scan", off=2)
_E("e_e4b", "e4", "### [The Long Count: Her Beacon](s04_scan)", off=6)
_E("e_e5a", "e5a", "### [The Long Count: The Skua's Price](s05_ask)", off=5)
_E("e_e5b", "e5b", "- [Buy the Skua's log]", off=-3)
_E("e_e5c", "e5c", "### [The Skua's Log](gleaner_skua)", off=5)
_E("e_title", "tt", "(s03_go)", off=2)
_E("e_boats", "f1", "Then: reveal act2_wait", off=4)
_E("e_wait", "final", "### [The Long Count: While They Read](act2_wait)", off=6)
_E("e_camp1", "camp", "## Act One, as played", off=8, file="campaign.md", wrap=True)
_E("e_camp2", "camp", "## Act Two - The Buyers (outline)", off=8, file="campaign.md", wrap=True)
_E("e_camp4", "camp", "## Act Four - The Fourth Colony (outline)", off=8, file="campaign.md", wrap=True)
_E("e_camp_top", "camp", "## Act One - Five Boats", off=8, file="campaign.md", wrap=True)

_RUN = "sbs run server,helm,comms,science,weapons -m KestrelVerge map=0 --dry-run"
STILLS.update({
    "t_run": ("session", [_RUN], {"state": "final"}),
    "t_lint": ("terminal", [("final", "sbs lint KestrelVerge")]),
    "card_title": ("card", "title", {}),
    "card_plan": ("card", "table", {"heading": "Step 1 - The plan", "nth": 1, "kicker": "Three sittings, on one save"}),
    "card_walk": ("card", "list", {"heading": "Step 2 - Sitting one", "kicker": "Sitting one: a walk, as fast as you can"}),
    "card_stop1": ("card", "table", {"heading": "Step 2 - Sitting one", "nth": 1, "kicker": "When I stopped"}),
    "card_safe": ("card", "points", {"kicker": "Is that safe against the live save?", "items": [
        "Four of Five is still hidden, so the crew has not finished it.",
        "Its new Then: line will be read when they do.",
        "The two new steps are ahead of the crew, not behind them."]}),
    "card_mist": ("card", "table", {"heading": "Step 7 - Check it", "nth": 1, "kicker": "Mistakes lint finds"}),
    "card_s2": ("card", "table", {"heading": "Step 8 - Sitting two", "nth": 1, "kicker": "Sitting two: do not delete the save"}),
    "card_stop2": ("card", "table", {"heading": "Step 8 - Sitting two", "nth": 2, "kicker": "When I stopped"}),
    "card_s3": ("card", "table", {"heading": "Step 9 - Sitting three", "nth": 1, "kicker": "Sitting three: the same line again"}),
    "card_rules": ("card", "table", {"heading": "Step 10 - The other three acts", "nth": 1, "kicker": "Four rules shaped the outline"}),
    "card_rubric": ("card", "table", {"heading": "Step 11 - The rubric", "nth": 1, "kicker": "Mark yourself against the rubric"}),
    "card_nobody": ("card", "table", {"heading": "What nobody has played", "nth": 1, "kicker": "What nobody has played"}),
    "card_end": ("card", "title", {"kicker": "Class 6", "title": "Capstone studio", "sub": "Go and write evening six"}),
})


def _tx(still, needle, words=None, nth=1):
    state, file = STILLS[still][1], STILLS[still][4]["file"]
    return ("text", _L(state, needle, nth, file, STILLS[still][2] - 4), words or needle)


def _ln(still, needle, count=1):
    state, file = STILLS[still][1], STILLS[still][4]["file"]
    a = _L(state, needle, 1, file, STILLS[still][2] - 4)
    return ("lines", a, a + count - 1)


def _b(frm, still, *marks):
    d = {"from": frm, "still": still}
    if marks:
        d["marks"] = list(marks)
    return d


BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        _b(0, "card_title"),
        _b(1, "card_plan"),
        _b(3, "e_camp_top"),
        _b(4, "e_camp2"),
    ]},
    "s02_the_plan": {"step": 1, "beats": [
        _b(0, "card_plan"),
        _b(1, "card_plan", ("part", "r1")),
        _b(3, "card_plan", ("part", "r1")),
        _b(7, "card_plan", ("part", "r2"), ("part", "r3")),
    ]},
    "s03_sitting_one": {"step": 2, "beats": [
        _b(0, "t_run", ("cmd", 1, "-m KestrelVerge")),
        _b(1, "card_walk", ("part", "item1")),
        _b(2, "card_walk", ("part", "item2")),
        _b(3, "card_walk", ("part", "item3")),
        _b(4, "card_stop1"),
        _b(5, "card_stop1", ("part", "r4")),
        _b(6, "card_stop1", ("part", "r5")),
        _b(8, "card_walk", ("part", "item4")),
    ]},
    "s04_write_evening_four": {"step": 3, "beats": [
        _b(0, "e_e4a"),
        _b(1, "e_e4a", _tx("e_e4a", "(s04_go)")),
        _b(2, "e_e4a", _tx("e_e4a", "Then: reveal s04_scan")),
        _b(3, "e_e4b", _ln("e_e4b", "### [The Long Count: Her Beacon](s04_scan)", 9)),
        _b(4, "card_safe"),
        _b(6, "card_safe", ("part", "item1")),
        _b(7, "card_safe", ("part", "item2")),
        _b(8, "card_safe", ("part", "item3")),
    ]},
    "s05_write_evening_five": {"step": 4, "beats": [
        _b(0, "e_e5a", _tx("e_e5a", "Objective: Hail the Gleaners on Comms")),
        _b(1, "e_e5b", _ln("e_e5b", "- [Buy the Skua's log]", 2)),
        _b(2, "e_e5c", _ln("e_e5c", "### [The Skua's Log](gleaner_skua)", 5)),
        _b(3, "e_e5b", _tx("e_e5b", "if learned the gleaners broke a boat")),
        _b(4, "e_e5b", _tx("e_e5b", "if learned the gleaners broke a boat", nth=2)),
        _b(5, "e_e5b", _ln("e_e5b", "- [Buy the Skua's log]", 2)),
        _b(6, "e_e5a", _tx("e_e5a", "Ask them first what became of the Tern's boats")),
        _b(7, "e_e5b", _tx("e_e5b", "learn the skua was emptied")),
        _b(9, "e_e5a", _tx("e_e5a", "They will not sell what they have not owned up to")),
        _b(10, "e_e5a", _tx("e_e5a", "Ask them first what became of the Tern's boats")),
    ]},
    "s06_one_change_they_ll_notice": {"step": 5, "beats": [
        _b(0, "e_title"),
        _b(1, "e_title", _tx("e_title", "(s03_go)", "The Plover")),
        _b(3, "e_title", _tx("e_title", "(s03_go)", "(s03_go)")),
        _b(4, "e_boats", _tx("e_boats", "Then: reveal act2_wait")),
        _b(5, "e_wait", _ln("e_wait", "### [The Long Count: While They Read](act2_wait)", 8)),
        _b(7, "e_wait", _tx("e_wait", "Until they do, the Verge still has work in it.")),
        _b(9, "e_wait", _ln("e_wait", "- ![](icon://flag)", 2)),
        _b(10, "t_lint", ("cmd", 1, "sbs lint KestrelVerge")),
        _b(11, "t_lint", ("span", 1, "unfired-signal")),
        _b(12, "t_lint", ("span", 1, "act2_begins")),
        _b(13, "card_mist", ("part", "r1")),
    ]},
    "s07_sitting_two": {"step": 8, "beats": [
        _b(0, "t_run", ("cmd", 1, "map=0")),
        _b(1, "card_s2", ("part", "r1")),
        _b(3, "card_s2", ("part", "r2"), ("part", "r3"), ("part", "r4")),
        _b(4, "card_s2", ("part", "r5")),
        _b(6, "e_e4b", _ln("e_e4b", "### [The Long Count: Her Beacon](s04_scan)", 9)),
        _b(7, "card_s2", ("part", "r6"), ("part", "r7")),
        _b(8, "card_s2", ("part", "r7")),
        _b(9, "card_stop2", ("part", "r3")),
    ]},
    "s08_sitting_three": {"step": 9, "beats": [
        _b(0, "card_s3"),
        _b(1, "card_s3", ("part", "r1"), ("part", "r2")),
        _b(2, "card_s3", ("part", "r2")),
        _b(4, "card_s3", ("part", "r3")),
        _b(7, "card_s3", ("part", "r4")),
        _b(10, "card_s3", ("part", "r5")),
        _b(11, "card_s3", ("part", "r6")),
    ]},
    "s09_the_other_three_acts": {"step": 10, "beats": [
        _b(0, "e_camp1"),
        _b(1, "e_camp1"),
        _b(4, "e_camp2"),
        _b(6, "e_camp4"),
        _b(7, "card_rules"),
        _b(8, "card_rules", ("part", "r2")),
    ]},
    "s10_the_rubric_and_what_nobody_h": {"step": 11, "beats": [
        _b(0, "card_rubric"),
        _b(1, "card_nobody"),
        _b(2, "card_nobody", ("part", "r1")),
        _b(3, "card_nobody", ("part", "r2")),
        _b(5, "card_rubric", ("part", "r9")),
        _b(6, "card_rubric", ("part", "r9")),
    ]},
    "s11_close": {"step": None, "beats": [
        _b(0, "e_camp2"),
        _b(4, "card_end"),
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
        if lo < t[2] - 6 or hi > t[2] + 5:
            a, z = hi - 5, lo + 6
            assert a <= z, ("marks do not fit one window", name, lo, hi)
            STILLS[name] = t[:2] + (min(max(t[2], a), z),) + t[3:]


_fit()
