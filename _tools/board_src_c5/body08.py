"""Storyboard for c5-08-captains-and-rivals: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 4 storyboards. Caption numbers are those of shots.py (2026-10-17). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 7 left it (kestrel_verge.amd = c5-07's example,
393 lines). The steps are typed in the video's order, each state one step on the one before:
Step 2, the Captains chapter above the Jobs chapter (Edda "k_edda", then Sable "k_sable");
Step 3, Edda's hail ("h_edda"), then her three answers ("h_edda2"); Step 4, Sable's hail
("h_sable"), then her four answers ("final", the page's own example, 481 lines). "b_roams" is
Step 4's rule about `Roams:` (Sable moved to the Bone Pile, which has no station; lint says clean).

NOT SHOWN AS WRITTEN: the map grid of Lecture 5 (scene 4) is a drawn card of the two rows it
would show, "card_roams". The note about `Rival when:` (scene 7) is a drawn card, "card_rival".

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine for
them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the
sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-08-captains-and-rivals start --state final --consoles server,helm,comms`
Marks are left off every game still until the stills exist. Press order:
  1. Comms: select Hollin Compact: game_c58_edda_btn (the button Hail Edda Brake, the Relay
     Warden, beside the station's own).
  2. Comms: Hail Edda Brake at standing 0: game_c58_edda_greet (the short greeting, two
     answers, no third). Give her the news: game_c58_edda_news.
  3. Hail her again: game_c58_edda_again (the other greeting, three answers). Ask about the
     bookkeeper: game_c58_edda_tip.
  4. Helm: engage The Breaking Yard: game_c58_yard (Gleaner space, the yard ahead).
  5. Comms: the Gleaners' station: game_c58_sable_btn (Hail Sable Orrin, the Tallyman).
     Hail her, pay the toll: game_c58_sable_paid. Hail again: game_c58_sable_tern (the answer
     about the Tern is there).
  6. Hail, Tell her to bill the Compact, twice: game_c58_sable_cross (the answer taken).
     Hail again: game_c58_sable_cold (the cold greeting, and no answer about the Tern).
Never caption a face or a clock time.
"""
LECTURE = "c5-08-captains-and-rivals"
TITLE = ("Class 5, Lecture 8", "Captains and rivals", "People with a name, and a line you chose")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-08-captains-and-rivals/example"

#@HELP@

_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c5-06-jobs/example", "c5-07-narrative-and-goals/example")},
       {FILE: _read("c5-07-narrative-and-goals/example/" + FILE)})

_F = _read(_EX + "/" + FILE)
_CAPT = _F[_F.index("## [Captains](captains)"):_F.index("// ---- Job types")]
_CAPT_E = _CAPT[:_CAPT.index("### [Sable Orrin](sable)")]
_ALL = _F[_F.index("\n### [Edda Brake](edda_hail)"):]
_EH = _ALL[:_ALL.index("\n### [News](edda_news)")]
_ER = _ALL[len(_EH):_ALL.index("\n### [Sable Orrin](sable_hail)")]
_SH = _ALL[len(_EH) + len(_ER):_ALL.index("\n### [Paid](sable_paid)")]
_SR = _ALL[len(_EH) + len(_ER) + len(_SH):]
_TAIL = "% Assay Office out.\n"
_JT = "// ---- Job types"

_chain("start", [
    ("k_edda", [(_JT, _CAPT_E + _JT)]),
    ("k_sable", [(_CAPT_E, _CAPT)]),
    ("h_edda", [(_TAIL, _TAIL + _EH)]),
    ("h_edda2", [(_EH, _EH + _ER)]),
    ("h_sable", [(_ER, _ER + _SH)]),
    ("final", [(_SH, _SH + _SR)]),
])
_same("final", FILE)
_chain("final", [("b_roams", [("Roams: -3, -2", "Roams: -4, -3")])])

_SIDE = "Side: hollin\nTitle: the Relay Warden"
_G_VAL = "Values: fearsome 40, resourceful 30"
_E_NEWS = "[Give her the news from down the lanes](edda_news)"
_E_TIP = "[Ask who keeps the Gleaners' books](edda_tip) if standing >= 20"
_S_PAID = "[Pay the yard's docking toll](sable_paid)"
_S_CROSS = "[Tell her to bill the Compact](sable_crossed)"
_S_TIP = "[Ask who was aboard the Tern](sable_tip) if standing >= 20"

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_capt", "k_edda", "Values: honest 40, kind 20")
_E("e_capt2", "k_sable", "Values: honest 40, by-the-book 30")
_E("e_gl", "k_sable", _G_VAL)
_E("e_roams", "b_roams", "Roams: -4, -3")
_E("e_ehail", "h_edda", "### [Edda Brake](edda_hail)", off=6)
_E("e_shail", "h_sable", "### [Sable Orrin](sable_hail)", off=6)
_term("t_final", "final")
_term("t_roams", "b_roams")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c58_edda_btn", "Comms, Hollin Compact selected: the button Hail Edda Brake, the Relay Warden, beside the station's own buttons")
_game("game_c58_edda_greet", "Comms, Edda's short greeting at standing 0: two answers, the news and Sign off")
_game("game_c58_edda_news", "Comms, the answer after the news is given: her reply, Come back when you want something")
_game("game_c58_edda_again", "Comms, Edda's other greeting on the second hail: three answers, the new one asks who keeps the Gleaners' books")
_game("game_c58_edda_tip", "Comms, Edda's reply about Sable Orrin, and to settle up first")
_game("game_c58_yard", "Helm, at The Breaking Yard: Gleaner space, the yard ahead")
_game("game_c58_sable_btn", "Comms, the Gleaners' station selected: the button Hail Sable Orrin, the Tallyman")
_game("game_c58_sable_paid", "Comms, Sable's reply after the docking toll is paid: Entered")
_game("game_c58_sable_tern", "Comms, Sable's plain greeting after the toll: four answers, including the one about who was aboard the Tern")
_game("game_c58_sable_cross", "Comms, Sable's reply to Tell her to bill the Compact")
_game("game_c58_sable_cold", "Comms, Sable's cold greeting after being crossed: no answer about the Tern")

# drawn
_card("card_what", "list", heading="Step 1 - What a captain is", kicker="A captain is three things")
_card("card_gap", "rows", kicker="The gap is the character", header=["Who", "Values"],
      rows=[["The Gleaners", "fearsome, resourceful"],
            ["Sable Orrin, their bookkeeper", "honest, by-the-book"]])
_card("card_roams", "rows", kicker="Roams needs a station", header=["Roams", "What is there", "Can she be hailed?"],
      rows=[["-3, -2", "The Gleaners' home, with a station", "Yes"],
            ["-4, -3", "The Bone Pile, no station", "No, and lint says nothing"]])
_card("card_line", "table", heading="Step 4 - A captain who can be crossed", nth=1, kicker="Where the line is")
_card("card_rival", "rows", kicker="The line that does nothing", header=["You write", "What the game does today"],
      rows=[["Rival when: standing < 50", "Lint accepts it. The game does not read it, and nothing changes"],
            ["Guards on greetings and answers", "What a rival really is in this class"]])
_card("card_check", "table", heading="Step 5 - Check it", nth=2, kicker="The rest of the check")
_card("card_exercise", "list", heading="Exercise", kicker="A friend and a rival")
_card("card_next", "title", kicker="Next", title="Lecture 9", sub="Organizing a big universe")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c58_sable_btn"),
        _b(3, "game_c58_edda_btn"),
        _b(6, "game_c58_sable_btn")),
    "s02_what_a_captain_is_and_isn_t": _sc(1,
        _b(0, "card_what"),
        _b(1, "card_what", ("part", "item1")),
        _b(2, "card_what", ("part", "item2")),
        _b(3, "card_what", ("part", "item3")),
        _b(4, "card_what"),
        _b(7, "card_what")),
    "s03_the_captains_chapter": _sc(2,
        _b(0, "e_capt", _tx("e_capt", "## [Captains](captains)")),
        _b(1, "e_capt", _ln("e_capt", _SIDE, 4)),
        _b(2, "e_capt", _tx("e_capt", "Side: hollin")),
        _b(3, "e_capt", _tx("e_capt", "Title: the Relay Warden")),
        _b(4, "e_capt", _tx("e_capt", "Values: honest 40, kind 20")),
        _b(6, "e_capt", _tx("e_capt", "Roams: 0, 0")),
        _b(7, "e_capt2", _tx("e_capt2", "Values: honest 40, by-the-book 30")),
        _b(8, "e_gl", _tx("e_gl", _G_VAL)),
        _b(9, "e_capt2", _tx("e_capt2", "Values: honest 40, by-the-book 30")),
        _b(10, "card_gap", ("part", "r2")),
        _b(11, "card_gap")),
    "s04_roams_needs_a_station": _sc(2,
        _b(0, "e_capt2", _tx("e_capt2", "Roams: -3, -2")),
        _b(3, "card_roams"),
        _b(6, "card_roams", ("part", "r1")),
        _b(7, "e_roams", _tx("e_roams", "Roams: -4, -3")),
        _b(8, "t_roams", ("part", "run1:clean"))),
    "s05_a_captain_s_voice": _sc(3,
        _b(0, "e_ehail", _ln("e_ehail", "### [Edda Brake](edda_hail)", 7)),
        _b(1, "e_ehail", _tx("e_ehail", "Speaker: edda\nWhen: comms", "Speaker: edda")),
        _b(3, "e_ehail", _tx("e_ehail", "%{standing >= 20} Captain.", "%{standing >= 20}")),
        _b(5, "e_ehail", _tx("e_ehail", "[Give her the news from down the lanes](edda_news) ; earns edda honest 20, earns edda kind 20", "earns edda honest 20, earns edda kind 20")),
        _b(7, "e_ehail", _tx("e_ehail", _E_TIP, "if standing >= 20")),
        _b(8, "e_ehail", _ln("e_ehail", _E_TIP)),
        _b(10, "e_ehail", _ln("e_ehail", _E_TIP)),
        _b(11, "e_ehail", _ln("e_ehail", _E_NEWS))),
    "s06_a_captain_who_can_be_crossed": _sc(4,
        _b(0, "e_shail", _ln("e_shail", "%{standing >= -20}", 2)),
        _b(1, "e_shail", _tx("e_shail", _S_PAID, "costs 100 credits")),
        _b(2, "e_shail", _tx("e_shail", _S_PAID, "earns sable honest 20, earns sable by-the-book 20")),
        _b(3, "e_shail", _tx("e_shail", _S_CROSS, "earns sable liar 25, earns sable resourceful 25")),
        _b(5, "e_shail", _ln("e_shail", "%{standing >= -20}", 2)),
        _b(6, "e_shail", _tx("e_shail", _S_TIP, "if standing >= 20")),
        _b(8, "card_line"),
        _b(9, "card_line", ("part", "r1"))),
    "s07_the_line_that_does_nothing": _sc(None,
        _b(0, "card_rival", ("part", "r1")),
        _b(3, "card_rival", ("part", "r1")),
        _b(6, "card_rival", ("part", "r2")),
        _b(7, "t_final", ("part", "run1:clean")),
        _b(8, "card_check")),
    "s08_make_a_friend": _sc(6,
        _b(0, "game_c58_edda_btn"),
        _b(2, "game_c58_edda_greet"),
        _b(3, "game_c58_edda_news"),
        _b(4, "game_c58_edda_again"),
        _b(6, "game_c58_edda_tip")),
    "s09_make_a_rival": _sc(6,
        _b(0, "game_c58_yard"),
        _b(1, "game_c58_sable_btn"),
        _b(2, "game_c58_sable_paid"),
        _b(3, "game_c58_sable_tern"),
        _b(4, "game_c58_sable_cross"),
        _b(6, "game_c58_sable_cold"),
        _b(10, "e_shail", _ln("e_shail", "%{standing >= -20}", 2))),
    "s10_your_turn": _sc(None,
        _b(0, "card_exercise"),
        _b(1, "card_exercise", ("part", "item1")),
        _b(3, "card_exercise", ("part", "item2")),
        _b(5, "card_exercise", ("part", "item5")),
        _b(6, "card_next")),
}
