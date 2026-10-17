"""Storyboard for c4-04-places-that-speak: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12, and Class 3's. Caption numbers are those of shots.py (2026-10-17).

The lecture starts from Lecture 3's hand-over: The Hollow with The Ring, The Way In, The
Altar and The Niche, 141 lines ("start"). The page's own example\\mission.amd (199 lines) is
the finished file; each step's state is that file with the lines of the LATER steps left
out: "s_chars" (Surveyor Rook), "s_dial" (the two scenes, the first answer not yet marked),
"s_marker" (Marker One in Quests), "s_reveal" (the first answer ends `; reveal niche`),
"s_scan" (Scene and Scan on The Altar), "final" (the example whole, with the place's own
scenes at the end). Lint's breaks are one change each on "final". Line numbers in the
marks are looked up in the state's own text (`_L`), so they follow the file.

NOT SHOWN: nothing is left out. The place's own scene (`Scene: altar_look`) cannot be
played in this lecture, as the video says, so it is shown only as text and lint.

GAME STILLS. NOT TAKEN YET: named here, to be taken in one sitting in the real engine. ONE
game, THREE windows:
`python game.py c4-04-places-that-speak start --state final --consoles server,helm,comms`
(the page's run line, `sbs run server,helm,comms -m MyRuin map=0`, on a probe copy of the
example). No probe patch. Marks are left off every game still until the stills are taken.
Press order:
  1. Helm, at once, the map zoomed out: game_c4_map (the name The Hollow at the way in).
  2. Fly in through The Mouth, through the ring, across The Nave, up the tunnel toward The
     Vault until The Altar turns gold on the map: Helm, game_c4_altar.
  3. Keep going until the ship is inside The Vault (inside 600 of The Altar): Helm,
     game_c4_vault. Comms has its row now.
  4. Comms: the Incoming Hails list with its one row, "Surveyor Rook - A recording at the
     altar": game_c4_hails.
  5. Select the row: the call open, one of the two opening takes, Back and the two answers:
     game_c4_call.
  6. Choose "Play the rest.": the rest of the recording, Back and the two answers:
     game_c4_rest.
  7. Choose "Mark the Gallery.": the call is over. Helm's map, The Niche a gold contact at
     the back of The Gallery, the ship nowhere near it: game_c4_niche.
"""
import os

LECTURE = "c4-04-places-that-speak"
TITLE = ("Class 4, Lecture 4", "Places that speak", "A recording the ship hears, and words for a person who has not arrived yet")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-04-places-that-speak/example"
_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "..", "example", "mission.amd"), encoding="utf-8", newline="") as _fh:
    _F = _fh.read().replace("\r\n", "\n").split("\n")
if _F[-1] == "":
    _F.pop()

# the lines of the finished file (1-based) that each step adds
_STEP = {"marker": set(range(41, 50)),            # Marker One in Quests, with its blank line
         "chars": set(range(153, 163)),           # the Characters section
         "dial": set(range(163, 188)),            # the Dialogue section, the two calls
         "scan": {140, 141},                      # Scene: and Scan: on The Altar
         "scenes": set(range(188, 200))}          # the place's own two scenes
_REVEAL = "- [Mark the Gallery.]() ; reveal niche"


def _have(*steps, reveal=False):
    """The finished file with every step NOT named left out; the first answer unmarked unless reveal."""
    gone = set()
    for s in _STEP:
        if s not in steps:
            gone |= _STEP[s]
    out = "".join(line + "\n" for i, line in enumerate(_F, 1) if i not in gone)
    if not reveal:
        out = out.replace(_REVEAL, "- [Mark the Gallery.]()")
    return out


_T = {"s_chars": _have("chars"),
      "s_dial": _have("chars", "dial"),
      "s_marker": _have("chars", "dial", "marker"),
      "s_reveal": _have("chars", "dial", "marker", reveal=True),
      "s_scan": _have("chars", "dial", "marker", "scan", reveal=True),
      "final": _have("chars", "dial", "marker", "scan", "scenes", reveal=True)}
_T["s_reveal"] = _have("chars", "dial", "marker", reveal=True)


def _L(state, prefix, nth=1):
    """The 1-based line of the state's mission.amd that starts with prefix (the nth such line)."""
    k = 0
    for i, line in enumerate(_T[state].split("\n"), 1):
        if line.startswith(prefix):
            k += 1
            if k == nth:
                return i
    raise ValueError(f"{state}: no line starts with {prefix!r}")


_TITLED = [("replace", "description.yaml", "Visible Mission Name: The Cold Hulk", "Visible Mission Name: The Hollow"),
           ("replace", "description.yaml", "Description: The Cold Hulk", "Description: The Hollow")]

STATES = {
    # Lecture 3's hand-over
    "start": {"folder": "c1-03-editor-and-first-run/example", "edits": _TITLED, "over": ("c4-03-dressing-a-ruin/example",)},
    "s_chars": {"base": "start", "edits": [("write", FILE, _T["s_chars"])]},
    "s_dial": {"base": "start", "edits": [("write", FILE, _T["s_dial"])]},
    "s_marker": {"base": "start", "edits": [("write", FILE, _T["s_marker"])]},
    "s_reveal": {"base": "start", "edits": [("write", FILE, _T["s_reveal"])]},
    "s_scan": {"base": "start", "edits": [("write", FILE, _T["s_scan"])]},
    "final": {"base": "start", "edits": [("write", FILE, _T["final"])], "same_as": (_EX + "/mission.amd",)},
    # Step 7: the breaks lint names, and the one it does not
    "b_alter": {"base": "final", "edits": [("replace", FILE, "reach altar 600", "reach alter 600")]},
    "b_altlok": {"base": "final", "edits": [("replace", FILE, "Scene: altar_look", "Scene: altar_lok")]},
    "b_nich": {"base": "final", "edits": [("replace", FILE, "; reveal niche", "; reveal nich")]},
    "b_gallery": {"base": "final", "edits": [("replace", FILE, "; reveal niche", "; reveal gallery")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

# line numbers, looked up in the states themselves
_C = _L("s_chars", "### [Surveyor Rook]")              # the character
_D = _L("s_dial", "### [Rook at the Altar]")           # the first call
_R = _L("s_dial", "### [The Rest of It]")              # the second
_M = _L("s_marker", "### [Marker One]")                # the beat
_AR = _L("s_marker", "Roles: altar")                   # the Altar's role
_WR = _L("s_marker", "Roles: entrance")                # The Way In's role
_V = _L("s_reveal", "- [Mark the Gallery.]")           # the answer that reveals
_N = _L("s_reveal", "### [The Niche]")                 # the place revealed
_SC = _L("s_scan", "Scene: altar_look")                # the place's scene line
_A = _L("final", "### [At the Altar]")                 # the place's own scene
_FM = _L("final", "Starts when: reach altar 600")      # in the finished file
_FSC = _L("final", "Scene: altar_look")
_FV = _L("final", "- [Mark the Gallery.]")

STILLS = {
    # VS Code, real. A still shows 21 lines: the one named, ten above and ten below
    "e_chars": ("vscode", "s_chars", _C + 3, "big", _NS),         # the Characters section and Surveyor Rook
    "e_dial_a": ("vscode", "s_dial", _D + 7, "big", _NS),         # Rook at the Altar, and the top of The Rest of It
    "e_dial_b": ("vscode", "s_dial", _R + 4, "big", _NS),         # The Rest of It
    "e_marker": ("vscode", "s_marker", _M + 4, "big", _NS),       # Marker One, under Study the Derelict
    "e_altar": ("vscode", "s_marker", _AR, "big", _NS),           # The Altar's record, Roles: altar
    "e_way": ("vscode", "s_marker", _WR, "big", _NS),             # The Way In's record, Roles: entrance
    "e_reveal": ("vscode", "s_reveal", _V, "big", _NS),           # the answer with `; reveal niche`
    "e_niche": ("vscode", "s_reveal", _N + 3, "big", _NS),        # The Niche and its key
    "e_scan": ("vscode", "s_scan", _SC, "big", _NS),              # Scene: and Scan: on The Altar
    "e_scenes": ("vscode", "final", _A + 5, "big", _NS),          # the place's own two scenes
    "e_f_marker": ("vscode", "final", _FM, "big", _NS),           # the finished beat
    "e_alter": ("vscode", "b_alter", _FM, "big", _NS),            # reach alter 600
    "e_altlok": ("vscode", "b_altlok", _FSC, "big", _NS),         # Scene: altar_lok
    "e_nich": ("vscode", "b_nich", _FV, "big", _NS),              # ; reveal nich
    "e_gallery": ("vscode", "b_gallery", _FV, "big", _NS),        # ; reveal gallery
    # the command prompt
    "t_lint": ("terminal", [("final", _LINT)]),
    "t_alter": ("terminal", [("b_alter", _LINT)]),
    "t_altlok": ("terminal", [("b_altlok", _LINT)]),
    "t_nich": ("terminal", [("b_nich", _LINT)]),
    "t_gallery": ("terminal", [("b_gallery", _LINT)]),
    # THE REAL GAME. Not taken yet (see the docstring). State final, consoles server,helm,comms
    "game_c4_map": ("game", "Helm, the map at the start: the hulk, and past it the name The Hollow at the way in"),
    "game_c4_altar": ("game", "Helm's map with the ship in the tunnel up to The Vault: The Altar a gold contact with its name, Comms empty"),
    "game_c4_vault": ("game", "Helm's map with the ship inside The Vault, on top of The Altar"),
    "game_c4_hails": ("game", "Comms: the Incoming Hails list with its one row, 'Surveyor Rook - A recording at the altar'"),
    "game_c4_call": ("game", "Comms, the row selected: the call open with the caller's name and one of the two opening takes, and Back and the two answers, 'Play the rest.' and 'Shut it off.'"),
    "game_c4_rest": ("game", "Comms after 'Play the rest.': the rest of the recording, and Back and the two answers, 'Mark the Gallery.' and 'End playback.'"),
    "game_c4_niche": ("game", "Helm's map after 'Mark the Gallery.': The Niche a gold contact at the back of The Gallery, the ship nowhere near it"),
    # drawn
    "card_title": ("card", "title", {}),
    "card_two": ("card", "table", {"heading": "Step 1 - Two ways a place can speak", "kicker": "Two listeners"}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Your turn"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 5", "sub": "What is inside"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c4_vault"},
        {"from": 3, "still": "game_c4_hails"},
        {"from": 4, "still": "game_c4_call"},
        {"from": 5, "still": "e_dial_a", "marks": [("text", _D + 2, "Speaker: rook"), ("lines", _D + 6, _D + 7)]},
        {"from": 6, "still": "e_marker", "marks": [("text", _M + 3, "reach altar 600")]},
    ]},
    "s02_two_listeners": {"step": 1, "beats": [
        {"from": 0, "still": "card_two"},
        {"from": 1, "still": "card_two", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_two", "marks": [("part", "r3")]},
        {"from": 3, "still": "card_two", "marks": [("part", "r1")]},
        {"from": 5, "still": "card_two", "marks": [("part", "r3")]},
        {"from": 6, "still": "card_two", "marks": [("part", "r5")]},
        {"from": 7, "still": "card_two"},
        {"from": 8, "still": "card_two", "marks": [("part", "r6")]},
    ]},
    "s03_a_voice": {"step": 2, "beats": [
        {"from": 0, "still": "e_chars", "marks": [("lines", _C - 2, _C - 2)]},
        {"from": 2, "still": "e_chars", "marks": [("lines", _C, _C + 4)]},
        {"from": 3, "still": "e_chars", "marks": [("lines", _C + 4, _C + 4)]},
        {"from": 5, "still": "e_chars", "marks": [("text", _C + 2, "Face: terran_male")]},
        {"from": 6, "still": "e_chars", "marks": [("text", _C, "(rook)")]},
    ]},
    "s04_what_he_says": {"step": 3, "beats": [
        {"from": 0, "still": "e_dial_a", "marks": [("lines", _D, _D + 10)]},
        {"from": 1, "still": "e_dial_a", "marks": [("text", _D + 2, "Speaker: rook")]},
        {"from": 2, "still": "e_dial_a", "marks": [("text", _D + 3, "When: hail")]},
        {"from": 3, "still": "e_dial_a", "marks": [("text", _D + 4, "Title: A recording at the altar")]},
        {"from": 4, "still": "e_dial_a", "marks": [("lines", _D + 6, _D + 7)]},
        {"from": 5, "still": "e_dial_a", "marks": [("lines", _D + 9, _D + 10)]},
        {"from": 6, "still": "e_dial_a", "marks": [("text", _D + 9, "(rook_more)")]},
        {"from": 7, "still": "e_dial_a", "marks": [("text", _D + 10, "()")]},
        {"from": 8, "still": "e_dial_b", "marks": [("lines", _R + 1, _R + 3)]},
    ]},
    "s05_the_place_makes_the_call": {"step": 4, "beats": [
        {"from": 0, "still": "e_marker", "marks": [("lines", _M, _M + 7)]},
        {"from": 2, "still": "e_marker", "marks": [("text", _M + 3, "Starts when:")]},
        {"from": 3, "still": "e_marker", "marks": [("text", _M, "###"), ("text", _M + 2, "Beat")]},
        {"from": 5, "still": "e_marker", "marks": [("text", _M + 3, "Starts when: reach altar 600")]},
        {"from": 7, "still": "e_marker", "marks": [("text", _M + 3, "altar")]},
        {"from": 8, "still": "e_altar", "marks": [("text", _AR, "Roles: altar")]},
        {"from": 10, "still": "e_way", "marks": [("text", _WR - 4, "(way_in)"), ("text", _WR, "Roles: entrance")]},
        {"from": 12, "still": "e_marker", "marks": [("text", _M + 3, "600")]},
        {"from": 17, "still": "e_marker", "marks": [("text", _M + 3, "reach altar 600")]},
        {"from": 19, "still": "e_marker", "marks": [("lines", _M + 4, _M + 5)]},
        {"from": 20, "still": "e_marker", "marks": [("text", _M + 5, "rook hails rook_altar")]},
    ]},
    "s06_an_answer_that_changes_the_m": {"step": 5, "beats": [
        {"from": 0, "still": "e_reveal", "marks": [("text", _V, "Mark the Gallery.")]},
        {"from": 2, "still": "e_reveal", "marks": [("text", _V, "reveal")]},
        {"from": 3, "still": "e_niche", "marks": [("lines", _N, _N + 7)]},
        {"from": 5, "still": "e_reveal", "marks": [("text", _V, "; reveal niche")]},
        {"from": 8, "still": "e_niche", "marks": [("text", _N, "(niche)")]},
        {"from": 9, "still": "e_reveal", "marks": [("text", _V, "niche")]},
        {"from": 10, "still": "e_reveal", "marks": [("text", _V, "reveal niche")]},
    ]},
    "s07_the_place_s_own_words": {"step": 6, "beats": [
        {"from": 0, "still": "e_scan", "marks": [("lines", _SC - 6, _SC + 2)]},
        {"from": 3, "still": "e_scan", "marks": [("lines", _SC, _SC + 1)]},
        {"from": 4, "still": "e_scan", "marks": [("text", _SC, "altar_look")]},
        {"from": 5, "still": "e_scan", "marks": [("text", _SC + 1, "Scan:")]},
        {"from": 7, "still": "e_scenes", "marks": [("lines", _A, _A + 5)]},
        {"from": 10, "still": "e_scenes", "marks": [("lines", _A + 4, _A + 5)]},
        {"from": 11, "still": "e_scenes", "marks": [("text", _A + 5, "()")]},
        {"from": 13, "still": "e_scenes", "marks": [("lines", _A, _A + 5)]},
        {"from": 14, "still": "e_scenes"},
    ]},
    "s08_lint": {"step": 7, "beats": [
        {"from": 0, "still": "t_lint", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_alter", "marks": [("text", _FM, "alter")]},
        {"from": 2, "still": "t_alter", "marks": [("span", 1, "role-nothing-wears")]},
        {"from": 3, "still": "e_altlok", "marks": [("text", _FSC, "altar_lok")]},
        {"from": 5, "still": "t_altlok", "marks": [("span", 1, "dangling-scene")]},
        {"from": 7, "still": "e_nich", "marks": [("text", _FV, "nich")]},
        {"from": 8, "still": "t_nich", "marks": [("span", 1, "ground-verb-target")]},
        {"from": 10, "still": "e_gallery", "marks": [("text", _FV, "reveal gallery")]},
        {"from": 11, "still": "t_gallery", "marks": [("part", "run1:clean")]},
        {"from": 13, "still": "e_gallery", "marks": [("text", _FV, "gallery")]},
        {"from": 14, "still": "e_f_marker", "marks": [("text", _FM, "altar 600")]},
    ]},
    "s09_play_it": {"step": 8, "beats": [
        {"from": 0, "still": "game_c4_map"},
        {"from": 1, "still": "game_c4_altar"},
        {"from": 3, "still": "game_c4_vault"},
        {"from": 4, "still": "game_c4_hails"},
        {"from": 6, "still": "game_c4_call"},
        {"from": 7, "still": "game_c4_rest"},
        {"from": 8, "still": "game_c4_niche"},
    ]},
    "s10_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 5, "still": "card_next"},
    ]},
}
