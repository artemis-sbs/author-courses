"""Storyboard for c5-11-a-ruin-on-the-map: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 4 storyboards. Caption numbers are those of shots.py (2026-10-17). The helpers below
only build the data and look a line number up in the text of the state.

The lecture starts from `MyUniverse` as Lecture 9 left it (six files, kestrel_verge.amd of 289
lines): the page's own example\\ is the end, built from Lecture 9's, and does NOT carry
Lecture 10's Customs House or Tally Yard. Every state is BUILT FORWARD and "final" must equal
kestrel_verge.amd (337 lines) and hollow.amd (84 lines) byte for byte ("same_as"). The steps, in
the video's order: Step 2, the ruin's file pasted whole ("h_file"); Step 3, the landmark
("l_land"); Step 4, the three steps of story ("s_lead", "s_cut", "final"). "b_slab" is Step 5's
misspelled signal (`slab_open`) on "final".

NOT SHOWN AS WRITTEN: the suit, its Nav and Fire apps and the handheld's Boarding Party app are
the game's. The note on the suit (scene 8) is a drawn card in the board's own words.

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine for
them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the
sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-11-a-ruin-on-the-map start --state final --consoles server,helm,comms`
SUIT UP closed the client until 2026-10-17 (assigned a ship in its spawn frame); wait a few
seconds after the press. Marks are left off every game still until the stills exist. Press order:
  1. Helm, at once, the handheld icon, Quests: game_c511_log4 (four leads, one of them A Hole
     in the Chart).
  2. Helm: engage A Hole in the Chart, arrive at (2, -3): game_c511_charted (the card
     Location charted: The Hollow, and Cut Through newly in the log).
  3. Helm: fly toward the way in: game_c511_approach (the way in as a contact on the map).
     Stop within 3,000 of it. The handheld, Boarding Party: game_c511_handheld (the button
     SUIT UP).
  4. Press SUIT UP: game_c511_suit (the suit's console in The Mouth, Nav listing the Gallery
     Door and The Niche). game_c511_inside (the main screen inside The Hollow, rock all round).
  5. The suit to The Gallery Door: game_c511_door (Fire lists The Fallen Slab, 450 away). Use
     BEAM: game_c511_cut. Twelve seconds on: game_c511_cut_done (Cut Through done and paid).
  6. The suit to The Niche: game_c511_niche. The bowl is taken: game_c511_bowl (What the Hollow
     Kept done, 900 credits). COME ABOARD: game_c511_aboard.
  7. Helm: fly 9,000 from the way in: game_c511_withdrawn (the button no longer reads SUIT UP).
  8. Helm: engage Kestrel Relay, then The Hollow again: game_c511_slab_open (the slab open).
Never caption a face or a clock time.
"""
import re

LECTURE = "c5-11-a-ruin-on-the-map"
TITLE = ("Class 5, Lecture 11", "A ruin on the map", "A place to fly into, and a story through its rooms")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-11-a-ruin-on-the-map/example"

#@HELP@

_M0 = _read("c5-09-organizing-a-big-universe/example/" + FILE)
_F = _read(_EX + "/" + FILE)
_x = lambda f: _read(_EX + "/" + f)

_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c5-06-jobs/example", "c5-07-narrative-and-goals/example",
                          "c5-08-captains-and-rivals/example", "c5-09-organizing-a-big-universe/example")},
       {FILE: _M0})

_HEAD = re.compile(r"(?m)^#{2,3} \[")
_i = _F.index("### [The Hollow](the_hollow)")
_k = _HEAD.search(_F, _i + 10).start()
_LM, _AFTER = _F[_i:_k], _F[_k:_k + 60]
_GOALS = "## [Goals](goals)"
_h0 = _F.index("### [A Hole in the Chart](lead_hollow)")
_h1 = _F.index(_GOALS)
_STEPS = _F[_h0:_h1]
_c0 = _STEPS.index("### [Cut Through](hollow_cut)")
_c1 = _STEPS.index("### [What the Hollow Kept](hollow_bowl)")
_LEAD, _CUT, _KEPT = _STEPS[:_c0], _STEPS[_c0:_c1], _STEPS[_c1:]
_BLANK = ""

_chain("start", [
    ("h_file", [("write", "hollow.amd", _x("hollow.amd"))]),
    ("l_land", [(_AFTER, _LM + _AFTER)]),
    ("s_lead", [(_GOALS, _BLANK + _LEAD + _GOALS)]),
    ("s_cut", [(_LEAD, _LEAD + _CUT)]),
    ("final", [(_CUT, _CUT + _KEPT)]),
])
_same("final", FILE, "hollow.amd")
_chain("final", [("b_slab", [("Done when: signal slab_opened", "Done when: signal slab_open")])])

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_HF = "hollow.amd"
_E("e_hollow_top", "h_file", "# [The Hollow](hollow_file)", off=2, file=_HF)
_E("e_hollow_rooms", "h_file", "### [The Nave](nave)", off=3, file=_HF)
_E("e_hollow_way", "h_file", "### [The Way In](way_in)", off=5, file=_HF)
_E("e_hollow_slab", "h_file", "### [The Fallen Slab](slab)", off=5, file=_HF)
_E("e_hollow_niche", "h_file", "### [The Niche](niche)", off=6, file=_HF)
_E("e_hollow_item", "h_file", "### [The Stone Bowl](stone_bowl)", off=4, file=_HF)
_E("e_lm", "l_land", "### [The Hollow](the_hollow)", off=4)
_E("e_lead", "s_lead", "### [A Hole in the Chart](lead_hollow)", off=6)
_E("e_cut", "s_cut", "### [Cut Through](hollow_cut)", off=6)
_E("e_kept", "final", "### [What the Hollow Kept](hollow_bowl)", off=6)
_E("e_slab_bad", "b_slab", "Done when: signal slab_open", off=3)
_term("t_lint", "final")
_term("t_slab", "b_slab")

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c511_inside", "The main screen inside The Hollow: rock all round the ship, well spaced")
_game("game_c511_handheld", "A crew member's handheld, Boarding Party: the button SUIT UP")
_game("game_c511_log4", "Helm, the handheld icon then Quests: four leads, one of them A Hole in the Chart")
_game("game_c511_charted", "Helm at (2, -3): the card Location charted: The Hollow, and Cut Through newly in the log")
_game("game_c511_approach", "Helm, the ship flying toward the way in, shown as a contact on the map")
_game("game_c511_suit", "The suit's console in The Mouth: the Nav app listing The Gallery Door and The Niche")
_game("game_c511_door", "The suit at The Gallery Door: the Fire app listing The Fallen Slab, 450 away")
_game("game_c511_cut", "The suit using BEAM on the slab: the banner for the twelve seconds of cutting")
_game("game_c511_cut_done", "Helm, Quests: Cut Through done and paid")
_game("game_c511_niche", "The suit at The Niche, the stone bowl in reach")
_game("game_c511_bowl", "The bowl taken: What the Hollow Kept done, and the crew's credits at 900")
_game("game_c511_aboard", "The handheld: COME ABOARD, the crew member back at Comms")
_game("game_c511_withdrawn", "The handheld with the ship 9,000 from the way in: the button no longer reads SUIT UP")
_game("game_c511_slab_open", "The Hollow on the second arrival: the slab already open")

# drawn
_card("card_needs", "table", heading="Step 1 - What a universe needs of a ruin", nth=1, kicker="What the universe needs of a ruin")
_card("card_sends", "table", heading="Step 1 - What a universe needs of a ruin", nth=2, kicker="The two words the game sends")
_card("card_checked", "rows", kicker="How this page was checked", header=["Checked by", "Nobody watched"],
      rows=[["A script, in the game's stand-in", "Not a screen"]])
_card("card_suit", "rows", kicker="The exosuit and older games", header=["Older versions of the game", "Now"],
      rows=[["A console could close the first time it met a suit mid-game", "Fixed. If yours is older, the way round is on the page"]])
_card("card_again", "table", heading="Step 7 - The ruin remembers", nth=1, kicker="On the second arrival")
_card("card_continue", "table", heading="Step 7 - The ruin remembers", nth=2, kicker="After Continue")
_card("card_later", "table", heading="What changes in later lectures", kicker="Three small things read differently later")
_card("card_exercise", "list", heading="Exercise", kicker="Make the ruin yours")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c511_inside"),
        _b(3, "game_c511_handheld"),
        _b(5, "e_lm", _tx("e_lm", "Relic: hollow")),
        _b(6, "e_cut", _ln("e_cut", "### [Cut Through](hollow_cut)", 8))),
    "s02_what_a_universe_needs_of_a_r": _sc(1,
        _b(0, "card_needs"),
        _b(3, "card_needs", ("part", "r2")),
        _b(4, "card_needs", ("part", "r1")),
        _b(5, "card_needs", ("part", "r3")),
        _b(6, "card_needs", ("part", "r4"), ("part", "r5")),
        _b(7, "card_needs", ("part", "r4")),
        _b(8, "card_needs", ("part", "r5"))),
    "s03_the_ruin_s_file": _sc(2,
        _b(0, "e_hollow_top", _ln("e_hollow_top", "// The Hollow: a ruin", 3)),
        _b(1, "e_hollow_top", _tx("e_hollow_top", "# [The Hollow](hollow_file)")),
        _b(3, "e_hollow_rooms", _tx("e_hollow_rooms", "### [The Mouth](mouth)"), _tx("e_hollow_rooms", "### [The Nave](nave)"), _tx("e_hollow_rooms", "### [The Gallery](gallery)")),
        _b(4, "e_hollow_way", _tx("e_hollow_way", "Roles: entrance")),
        _b(5, "e_hollow_slab", _ln("e_hollow_slab", "### [The Fallen Slab](slab)", 7)),
        _b(6, "e_hollow_niche", _tx("e_hollow_niche", "Item: stone_bowl")),
        _b(7, "e_hollow_item", _ln("e_hollow_item", "### [The Stone Bowl](stone_bowl)", 5))),
    "s04_the_landmark": _sc(3,
        _b(0, "e_lm", _ln("e_lm", "### [The Hollow](the_hollow)", 7)),
        _b(2, "e_lm", _tx("e_lm", "Relic: hollow")),
        _b(4, "e_lm", _tx("e_lm", "Relic file: hollow.amd")),
        _b(5, "e_lm", _ln("e_lm", "Relic: hollow", 2)),
        _b(6, "e_lm", _ln("e_lm", "At: 2, -3", 4))),
    "s05_three_steps_of_story": _sc(4,
        _b(0, "e_lead", _ln("e_lead", "### [A Hole in the Chart](lead_hollow)", 11)),
        _b(1, "e_lead", _ln("e_lead", "### [A Hole in the Chart](lead_hollow)", 11)),
        _b(2, "e_cut", _tx("e_cut", "Done when: signal slab_opened", "signal slab_opened")),
        _b(3, "e_kept", _tx("e_kept", "Done when: signal hollow_taken", "signal hollow_taken")),
        _b(4, "e_cut", _tx("e_cut", "Done when: signal slab_opened", "signal slab_opened")),
        _b(8, "card_sends"),
        _b(9, "card_sends", ("part", "r1")),
        _b(10, "e_cut", _ln("e_cut", "A slab has come down", 5)),
        _b(11, "e_cut", _tx("e_cut", "- ![](icon://person)", "icon://person"), _tx("e_cut", "- ![](icon://lightning)", "icon://lightning")),
        _b(12, "e_kept", _tx("e_kept", "## What the Tern saw"))),
    "s06_lint": _sc(5,
        _b(0, "t_lint", ("part", "run1:clean")),
        _b(2, "e_hollow_slab", _tx("e_hollow_slab", "### [The Fallen Slab](slab)", "slab")),
        _b(3, "card_sends", ("part", "r1")),
        _b(4, "e_slab_bad", _tx("e_slab_bad", "Done when: signal slab_open", "slab_open")),
        _b(5, "t_slab", ("out", 1, 1)),
        _b(7, "t_lint", ("part", "run1:clean"))),
    "s07_play_it": _sc(6,
        _b(0, "game_c511_log4"),
        _b(3, "game_c511_charted"),
        _b(5, "game_c511_approach"),
        _b(6, "game_c511_handheld"),
        _b(8, "game_c511_suit"),
        _b(11, "game_c511_door"),
        _b(12, "game_c511_cut"),
        _b(13, "game_c511_cut_done"),
        _b(14, "game_c511_niche"),
        _b(15, "game_c511_bowl"),
        _b(16, "game_c511_aboard")),
    "s08_an_honest_word": _sc(6,
        _b(0, "card_checked"),
        _b(3, "card_suit"),
        _b(5, "game_c511_suit")),
    "s09_the_ruin_remembers": _sc(7,
        _b(0, "card_again"),
        _b(2, "card_again", ("part", "r1")),
        _b(3, "game_c511_slab_open"),
        _b(4, "card_again", ("part", "r3")),
        _b(5, "card_again", ("part", "r4")),
        _b(6, "card_continue"),
        _b(8, "card_continue", ("part", "r2"))),
    "s10_your_turn": _sc(None,
        _b(0, "card_later"),
        _b(4, "card_exercise"),
        _b(5, "card_exercise", ("part", "item1")),
        _b(6, "card_exercise", ("part", "item4")),
        _b(7, "card_exercise", ("part", "item4"))),
}
