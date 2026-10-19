"""Storyboard for c5-10-a-boarding-site-on-the-map: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in _tools/picture/README.md and in
the Class 3 and 4 storyboards (subfolders, tile files). Caption numbers are those of shots.py
(2026-10-17). The helpers below only build the data and look a line number up in the text of
the state.

The lecture starts from `MyUniverse` as Lecture 9 left it (six files: kestrel_verge.amd of 289
lines, jobs.amd, lore.amd and the three dialogue files), plus the mission's story.json and
settings.yaml. The page's own example\\ holds the seven files the lecture changes and is the end,
so every state is BUILT FORWARD from the start and "final" must equal them byte for byte
("same_as"). The two starting files are the example's, with only the lines Step 7 adds taken out
(story.json without the two Cosmos-Tiles packs and the comma, settings.yaml without TILE_ART).
The steps, in the video's order: Step 1, the Customs House landmark ("l_customs"); Step 2, the
site's file ("c_file"); Step 3, the step of story ("n_cus", without its Then line); Step 7, the
art packs ("m_json", "m_settings"); Step 8, the ground ("m_tileset", "m_tiles"); Step 9, the
yard's file ("m_site"); Step 10, the landmark ("m_land"), the Then line ("m_then") and The Short
Count ("final"). "b_area" is Step 11's broken rule: the map's first line `area: yard`.

NOT SHOWN AS WRITTEN: the handheld's Boarding Party app and the map as the crew walks it are the
game's; the save file's lines (scene 10) are drawn as a card of the three things the page names,
not as the file. The tiles file is shown as text, and once as the Tile Map Editor's picture
("e_tiles_pic", needs the add-on in the capture profile).

GAME STILLS. NOT TAKEN YET: planned here, taken in one sitting by hand. NEVER start the engine for
them from this file: Open Universe rewrites the player's save. ONE game, THREE windows, on the
sandbox probe (README: an Open Universe probe is built in data/missions/_sandbox/):
`python game.py c5-10-a-boarding-site-on-the-map start --state final --consoles server,helm,comms,weapons`
Marks are left off every game still until the stills exist. Press order:
  1. Helm: dock with Customs House (at 0, 0). Comms: the call: game_c510_ccall (the clerk's
     line, the two answers). Press Assemble a boarding party: game_c510_cparty (the handheld,
     Boarding Party, CUSTOMS HOUSE, BEAM DOWN). Press it: game_c510_ccounter (The Counter, three
     choices). Read the manifest: game_c510_cmanifest. Back to the counter: game_c510_ccounter2
     (the other line, the manifest face down). Helm, Quests: game_c510_cdone (Nothing to
     Declare done and paid, The Short Count newly there). Beam back up.
  2. Helm: dock with Tally Yard: game_c510_ydock. Comms: the yard's call: game_c510_ycall.
     Assemble the party. Weapons: handheld, BEAM DOWN: game_c510_ybeam (the yard's map, the pad).
  3. Walk: game_c510_yside (the side story offered), game_c510_loader (the loader frame),
     game_c510_door_shut (the door refusing), game_c510_keycard (the keycard in the yard),
     game_c510_door_open, game_c510_ledger (inside the tally house), game_c510_done (The Short
     Count done and paid), BEAM UP: game_c510_up.
  4. Dock again, go down: game_c510_door_still (the door still open, the loader still down).
  5. For the cold open: game_c510_handheld (the Customs House on the handheld, three choices) and
     game_c510_ymap (the handheld showing the yard's map).
Never caption a face or a clock time.
"""
import re

LECTURE = "c5-10-a-boarding-site-on-the-map"
TITLE = ("Class 5, Lecture 10", "A boarding site on the map", "A place of rooms, and a map the crew walks")
MISSION = "MyUniverse"
TEMPLATE_BASE = "ou"   # capture lays the template's files (script.py, story.json...) under each state
FILE = "kestrel_verge.amd"
MAST = "story.mast"
_EX = "c5-10-a-boarding-site-on-the-map/example"

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


_M0 = _read("c5-09-organizing-a-big-universe/example/" + FILE)
_F = _read(_EX + "/" + FILE)
_x = lambda f: _read(_EX + "/" + f)
_J = _x("story.json")
_Y = _x("settings.yaml")
_SNIP = ',\n        "artemis-sbs.Cosmos-Tiles.frontier.v0.4.2.zip",\n        "artemis-sbs.Cosmos-Tiles.station.v0.4.2.zip"\n'
assert _J.count(_SNIP) == 1
_J0 = _J.replace(_SNIP, "\n")
_Y0 = _Y[:_Y.index("# The art a walked site's ground is drawn with.")]

_start("start", {"folder": "c5-02-your-universe-file/example",
                 "over": ("c5-03-sides-diplomacy-goods/example", "c5-04-reputation/example",
                          "c5-05-the-map/example", "c5-06-jobs/example", "c5-07-narrative-and-goals/example",
                          "c5-08-captains-and-rivals/example", "c5-09-organizing-a-big-universe/example"),
                 "edits": [("write", "story.json", _J0), ("write", "settings.yaml", _Y0)]},
       {FILE: _M0, "story.json": _J0, "settings.yaml": _Y0})

_HEAD = re.compile(r"(?m)^#{2,3} \[")
_i = _F.index("### [Customs House](customs_house)")
_j = _F.index("### [Tally Yard](tally_yard_station)")
_k = _HEAD.search(_F, _j + 10).start()
_CH, _TY, _AFTER = _F[_i:_j], _F[_j:_k], _F[_k:_k + 60]
_n = _F.index("### [Nothing to Declare](lead_customs)")
_m = _F.index("### [The Short Count](yard_count)")
_o = _HEAD.search(_F, _m + 10).start()
_NCUS, _NSH, _NAFTER = _F[_n:_m], _F[_m:_o], _F[_o:_o + 60]
_PEOPLE_OLD = "nobody buys people." + chr(10) * 2
_PEOPLE_NEW = "nobody buys people." + chr(10)
_NCUS0 = _NCUS.replace("Then: reveal yard_count\n", "")

_chain("start", [
    ("l_customs", [(_AFTER, _CH + _AFTER)]),
    ("c_file", [("write", "customs.amd", _x("customs.amd"))]),
    ("n_cus", [(_PEOPLE_OLD, _PEOPLE_NEW + _NCUS0)]),
    ("m_json", [("write", "story.json", _J)]),
    ("m_settings", [("write", "settings.yaml", _Y)]),
    ("m_tileset", [("write", "ground/starter.tileset", _x("ground/starter.tileset"))]),
    ("m_tiles", [("write", "ground/tally_yard.tiles", _x("ground/tally_yard.tiles"))]),
    ("m_site", [("write", "tally_yard.amd", _x("tally_yard.amd"))]),
    ("m_land", [(_CH, _CH + _TY)]),
    ("m_then", [("Reward: 50 credits\n---", "Reward: 50 credits\nThen: reveal yard_count\n---")]),
    ("final", [(_NCUS, _NCUS + _NSH)]),
])
_same("final", FILE, "customs.amd", "tally_yard.amd", "story.json", "settings.yaml",
      "ground/starter.tileset", "ground/tally_yard.tiles")
_chain("final", [("b_area", [("ground/tally_yard.tiles", "area: tally_yard\n", "area: yard\n")])])

_CUS = "customs.amd"
_LEARN = "[Read the manifest on the counter](customs_manifest) ; learn the manifest, signal manifest_read"
_BEAM = "- [Assemble a boarding party]() ; signal boarding_down"
_SHIP = "![](ship://starbase_civil) The Customs House, beside Kestrel Relay"

# The editor. A window shows 21 lines: the one named, ten above and ten below.
_E("e_lm", "l_customs", "### [Customs House](customs_house)", off=4)
_E("e_cust0", "c_file", "// Customs House: a place", off=0, file=_CUS)
_E("e_cust_hails", "c_file", _BEAM, off=-2, file=_CUS)
_E("e_cust_rooms", "c_file", "## [Scenes](boarding)", off=8, file=_CUS)
_E("e_cust_counter", "c_file", _LEARN, off=-1, file=_CUS)
_E("e_cust_office", "c_file", "(customs_initial) if learned the manifest", off=1, file=_CUS)
_E("e_nothing", "n_cus", "### [Nothing to Declare](lead_customs)", off=8)
_E("e_json", "m_json", "artemis-sbs.Cosmos-Tiles.frontier", off=-4, file="story.json")
_E("e_settings", "m_settings", "TILE_ART: frontier, station", off=-4, file="settings.yaml")
_E("e_tileset", "m_tileset", "tileset: starter", off=0, file="ground/starter.tileset")
_E("e_tiles_top", "m_tiles", "area: tally_yard", off=10, file="ground/tally_yard.tiles")
_E("e_tiles_map", "m_tiles", "#..===.......WWWWWWW...#", off=5, file="ground/tally_yard.tiles")
STILLS["e_tiles_pic"] = ("vscode", "m_tiles", 1, "mid", {"file": "ground/tally_yard.tiles", "editor": "tiles"})
_OF["e_tiles_pic"] = ("m_tiles", "ground/tally_yard.tiles")
_E("e_ty_top", "m_site", "// Tally Yard: a place", off=0, file="tally_yard.amd")
_E("e_ty_hails", "m_site", "signal boarding_down", off=-3, file="tally_yard.amd")
_E("e_ty_props", "m_site", "### [Tally house door](yard_door)", off=-1, file="tally_yard.amd")
_E("e_ty_keys", "m_site", "### [Yard keycard](yard_keycard)", off=4, file="tally_yard.amd")
_E("e_ty_people", "m_site", "### [Keeper Kell](yard_keeper)", off=6, file="tally_yard.amd")
_E("e_ty_host", "m_site", "### [Loader frame](yard_loader)", off=6, file="tally_yard.amd")
_E("e_tylm", "m_land", "### [Tally Yard](tally_yard_station)", off=3)
_E("e_then", "m_then", "Then: reveal yard_count", off=3)
_E("e_short", "final", "### [The Short Count](yard_count)", off=6)
_E("e_area", "b_area", "area: yard", off=10, file="ground/tally_yard.tiles")

_term("t_lint7", "n_cus")
_term("t_lint8", "final")
_term("t_area", "b_area")
STILLS["t_fetch"] = ("session", ['sbs fetch "MyUniverse" --update-libs'], {"state": "m_settings"})

# THE REAL GAME (planned; not taken yet - see the docstring for the press order)
_game("game_c510_handheld", "The handheld on the Customs House's visit: three choices on it")
_game("game_c510_ymap", "The handheld showing the yard's map, the landing pad on the left")
_game("game_c510_cdock", "Helm, the ship docked with Customs House")
_game("game_c510_ccall", "Comms, the call from the Customs House: the clerk's line and two answers, Assemble a boarding party and Stay aboard")
_game("game_c510_cparty", "The handheld, Boarding Party: a party open for CUSTOMS HOUSE, the button BEAM DOWN")
_game("game_c510_ccounter", "The Counter: the clerk's line and three choices")
_game("game_c510_cmanifest", "The Manifest: the line about forty crates, Back to the counter and Beam back up")
_game("game_c510_ccounter2", "The Counter again: the other line, the manifest turned face down")
_game("game_c510_cdone", "Helm, Quests: Nothing to Declare done and paid, The Short Count newly in the log")
_game("game_c510_ydock", "Helm, the ship docked with Tally Yard")
_game("game_c510_ycall", "Comms, the call from Tally Yard: the keeper's line and the answer that sends a party")
_game("game_c510_ybeam", "Weapons, the handheld: BEAM DOWN, then the yard's map with the party on the pad")
_game("game_c510_yside", "The yard, the side story offered to the one who went down")
_game("game_c510_loader", "The yard, the loader frame ahead of the party, attacking")
_game("game_c510_door_shut", "The yard, the tally house door refusing the party")
_game("game_c510_keycard", "The yard, the keycard lying on the ground, picked up")
_game("game_c510_door_open", "The yard, the tally house door open")
_game("game_c510_ledger", "Inside the tally house, the ledger")
_game("game_c510_done", "Helm, Quests: The Short Count done and paid")
_game("game_c510_up", "The handheld: the last of the party beamed up, the visit over")
_game("game_c510_door_still", "The yard on a second visit: the door still open, the loader still down")

# drawn
_card("card_three_ch", "rows", kicker="The site's file: three chapters", header=["Chapter", "Its key", "What it is"],
      rows=[["Voices", "voices", "Who is speaking: a name, a face, a color"],
            ["Hails", "hails", "The call that comes when the ship docks"],
            ["Scenes", "boarding", "The rooms. The key is boarding, not scenes"]])
_card("card_rule", "rows", kicker="One rule", header=["The landmark says", "The map's first line says"],
      rows=[["Site: tally_yard", "area: tally_yard"]])
_card("card_needs", "table", heading="Step 6 - One rule", nth=1, kicker="A walked site needs five things")
_card("card_chapters", "rows", kicker="The yard's file: what stands on the map", header=["Chapter", "What is in it"],
      rows=[["Hails", "The call, exactly as in Part 1"],
            ["Props", "Things on the map: a terminal, a door, a keycard, a ledger"],
            ["People", "Somebody calm to talk to"],
            ["Hostiles", "Somebody who attacks"],
            ["Scenes", "The rooms, opened by a crew member on the map"],
            ["Side Stories", "A small quest for one member of the party"]])
_card("card_save", "rows", kicker="What the save keeps", header=["Thing", "Kept"],
      rows=[["The door", "Open"], ["The keycard", "Taken"], ["The loader", "Down"],
            ["What was learned in each place", "Kept, place by place"]])
_card("card_checked", "rows", kicker="How this page was checked", header=["Checked by", "Nobody watched"],
      rows=[["A script, in the game's stand-in", "Not a screen"]])
_card("card_nocall", "rows", kicker="Always give a site a call", header=["A site with no call", "What happens"],
      rows=[["The party", "Opens the moment the ship docks, and nobody asked the crew first"],
            ["A crew that casts off without going down", "That visit just ends"]])
_card("card_exercise", "list", heading="Exercise", kicker="Rename it, add a room, walk the yard")
_card("card_next", "title", kicker="Next", title="Lecture 11", sub="A ruin on the map")

BOARD = {
    "s01_cold_open": _sc(None,
        _b(0, "game_c510_handheld"),
        _b(4, "game_c510_ymap"),
        _b(5, "e_lm", _tx("e_lm", "Site: customs"))),
    "s02_one_line_on_a_landmark": _sc(1,
        _b(0, "e_lm", _ln("e_lm", "### [Customs House](customs_house)", 8)),
        _b(1, "e_lm", _tx("e_lm", "At: 0, 0"+chr(10)+"Prefab: station"+chr(10)+"Art: starbase_civil", "At: 0, 0")),
        _b(3, "e_lm", _tx("e_lm", "Site: customs")),
        _b(5, "e_lm", _tx("e_lm", "Site: customs")),
        _b(6, "e_lm", _tx("e_lm", "Site: customs", "customs")),
        _b(7, "e_cust0", _ln("e_cust0", "# [Customs House](customs)", 1))),
    "s03_the_site_s_file": _sc(2,
        _b(0, "e_cust0", _ln("e_cust0", "// Customs House: a place", 3)),
        _b(2, "card_three_ch"),
        _b(3, "card_three_ch", ("part", "r1")),
        _b(4, "card_three_ch", ("part", "r2")),
        _b(5, "e_cust_hails", _tx("e_cust_hails", _BEAM, "[Assemble a boarding party]()")),
        _b(6, "e_cust_hails", _tx("e_cust_hails", _BEAM, "; signal boarding_down")),
        _b(8, "e_cust_hails", _tx("e_cust_hails", _BEAM, "signal boarding_down")),
        _b(9, "e_cust_rooms", _tx("e_cust_rooms", "## [Scenes](boarding)", "(boarding)")),
        _b(10, "e_cust_rooms", _ln("e_cust_rooms", "### [The Counter](customs_counter)", 1)),
        _b(11, "e_cust_rooms", _tx("e_cust_rooms", "- [Beam back up]()", "Beam back up")),
        _b(12, "e_cust_rooms", _tx("e_cust_rooms", "- [Beam back up]()", "Beam back up"))),
    "s04_a_fact_and_a_step_of_story": _sc(3,
        _b(0, "e_cust_counter", _ln("e_cust_counter", _LEARN, 1)),
        _b(1, "e_cust_counter", _tx("e_cust_counter", _LEARN, "learn the manifest")),
        _b(3, "e_cust_counter", _ln("e_cust_counter", "%{learned the manifest < 1}", 2)),
        _b(4, "e_cust_counter", _tx("e_cust_counter", "%{learned the manifest < 1}", "%{learned the manifest < 1}")),
        _b(5, "e_cust_office", _tx("e_cust_office", "(customs_initial) if learned the manifest", "if learned the manifest")),
        _b(6, "e_cust_counter", _tx("e_cust_counter", _LEARN, "signal manifest_read")),
        _b(8, "e_nothing", _ln("e_nothing", "### [Nothing to Declare](lead_customs)", 8)),
        _b(9, "e_nothing", _tx("e_nothing", "Done when: signal manifest_read", "signal manifest_read")),
        _b(11, "e_nothing", _tx("e_nothing", _SHIP, "![](ship://starbase_civil)")),
        _b(12, "e_lm", _tx("e_lm", "Art: starbase_civil"))),
    "s05_lint_and_play": _sc(4,
        _b(0, "t_lint7", ("part", "run1:clean")),
        _b(3, "e_cust_hails", _tx("e_cust_hails", _BEAM, "signal boarding_down")),
        _b(4, "e_cust_counter", _tx("e_cust_counter", _LEARN, "signal manifest_read")),
        _b(5, "e_nothing", _tx("e_nothing", "Done when: signal manifest_read", "signal manifest_read")),
        _b(6, "game_c510_cdock"),
        _b(7, "game_c510_ccall"),
        _b(8, "game_c510_cparty"),
        _b(9, "game_c510_ccounter"),
        _b(10, "game_c510_cmanifest"),
        _b(11, "game_c510_cdone"),
        _b(12, "game_c510_ccounter2")),
    "s06_the_same_idea_walked": _sc(6,
        _b(0, "card_rule"),
        _b(2, "e_tylm", _tx("e_tylm", "Site: tally_yard")),
        _b(3, "e_tiles_top", _tx("e_tiles_top", "area: tally_yard")),
        _b(4, "card_rule", ("part", "r1")),
        _b(6, "card_needs", ("part", "r1")),
        _b(8, "e_json", _ln("e_json", '"artemis-sbs.LegendaryMissions.media.v1.4.0.zip",', 3)),
        _b(9, "e_json", _tx("e_json", '"artemis-sbs.LegendaryMissions.media.v1.4.0.zip",', ","),
           _tx("e_json", '"artemis-sbs.Cosmos-Tiles.frontier.v0.4.2.zip",', ",")),
        _b(10, "e_settings", _ln("e_settings", "# The art a walked site's ground", 2)),
        _b(11, "t_fetch")),
    "s07_the_map_and_its_file": _sc(8,
        _b(0, "e_tileset", _ln("e_tileset", "tileset: starter", 8)),
        _b(2, "e_tiles_pic"),
        _b(3, "e_tiles_map", _ln("e_tiles_map", "#..===.......WWWWWWW...#", 3)),
        _b(4, "e_tiles_map", _tx("e_tiles_map", "#............WWWDWWW...#", "D")),
        _b(5, "e_tiles_top", _tx("e_tiles_top", "area: tally_yard")),
        _b(6, "e_ty_top", _ln("e_ty_top", "// Tally Yard: a place", 3)),
        _b(7, "e_ty_hails", _tx("e_ty_hails", "signal boarding_down")),
        _b(8, "card_chapters"),
        _b(9, "e_ty_props", _tx("e_ty_props", "### [Tally house door](yard_door)")),
        _b(10, "e_ty_people", _tx("e_ty_people", "### [Keeper Kell](yard_keeper)")),
        _b(11, "e_ty_host", _tx("e_ty_host", "### [Loader frame](yard_loader)")),
        _b(12, "e_ty_keys", _tx("e_ty_keys", "### [Yard keycard](yard_keycard)", "yard_keycard"))),
    "s08_the_landmark_the_step_and_li": _sc(10,
        _b(0, "e_tylm", _ln("e_tylm", "### [Tally Yard](tally_yard_station)", 7)),
        _b(1, "e_short", _ln("e_short", "### [The Short Count](yard_count)", 8)),
        _b(2, "e_then", _tx("e_then", "Then: reveal yard_count")),
        _b(3, "t_lint8", ("part", "run1:clean")),
        _b(5, "e_area", _tx("e_area", "area: yard")),
        _b(6, "t_area", ("out", 1, 1))),
    "s09_walk_it": _sc(12,
        _b(0, "game_c510_ydock"),
        _b(1, "game_c510_ycall"),
        _b(2, "game_c510_ybeam"),
        _b(3, "game_c510_yside"),
        _b(4, "game_c510_loader"),
        _b(5, "game_c510_door_shut"),
        _b(7, "game_c510_keycard"),
        _b(8, "game_c510_door_open"),
        _b(9, "game_c510_ledger"),
        _b(10, "game_c510_done"),
        _b(11, "game_c510_up")),
    "s10_it_remembers": _sc(12,
        _b(0, "game_c510_door_still"),
        _b(8, "card_save"),
        _b(9, "card_save", ("part", "r1"), ("part", "r2"), ("part", "r3")),
        _b(10, "card_save", ("part", "r4"))),
    "s11_an_honest_word_and_your_turn": _sc(None,
        _b(0, "card_checked"),
        _b(3, "card_nocall"),
        _b(4, "card_nocall", ("part", "r1")),
        _b(6, "card_nocall", ("part", "r2")),
        _b(8, "card_exercise"),
        _b(9, "card_exercise", ("part", "item1")),
        _b(10, "card_exercise", ("part", "item2")),
        _b(11, "card_exercise", ("part", "item4"))),
}
