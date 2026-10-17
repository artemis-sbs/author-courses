"""Storyboard for c4-05-what-is-inside: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12 and in _tools/picture/README.md. Caption numbers are those of shots.py.

The lecture starts from Lecture 4's file: `MyRuin` as `sbs create MyRuin -t amd` made it, with
`mission.amd` replaced by c4-04's example (199 lines) and the template's `story.mast`, which is
never opened. The steps are typed in the video's order: the canister item ("items"), the
Cache ("cache"), the quest that waits for it ("quest1"), the bowl item ("bowl_item"), the
Niche's role ("niche_role") and its Item line ("niche"), then The Bowl ("final", the page's own
example, 251 lines). Two variants: "q_three" (`collect 3 canister`, the catch of Step 4) and
"noart" (the canister without its Art line, scene 8).

GAME STILLS. NOT TAKEN YET: they are planned here and are taken in one scouting sitting.
ONE game, THREE windows:
`python game.py c4-05-what-is-inside start --state final --consoles server,helm,comms`.
No probe patch: Helm flies. Nothing is clicked on Comms except step 5. Press order:
  1. Helm, at once: the handheld icon (top left), Quests: game_c5_quests (both quests in the
     list, Active). Close it.
  2. Helm: fly in through The Mouth into The Nave and stop about 700 from The Cache
     (3600, 0, 500): game_c5_cache (the three canisters drawn, nothing taken).
  3. Helm: fly inside 500 of The Cache: game_c5_pickup (the corner toast `Pickup: Survey
     Canister x3`, and the strip line `Quest complete: What the Survey Left` if it is up).
  4. Helm: the handheld icon, Quests: game_c5_left_done (What the Survey Left Done, The Bowl
     still Active).
  5. Helm: fly to The Altar (inside 600 of the Vault's middle). Comms: open Rook at the
     Altar, Play the rest, Mark the Gallery. Helm: fly through The Gallery to 700 from The
     Niche (3000, 0, -2500): game_c5_bowl (the bowl drawn at the back of the built room).
  6. Helm: fly inside the bowl's pick-up range: game_c5_bowl_taken (the toast `Pickup: The
     Stone Bowl` and the strip line `Quest complete: The Bowl`).
  7. Helm: the handheld icon, Quests: game_c5_bowl_done (both quests Done).
No marks are set on the game stills yet: set them from the screenshots once they exist.
"""
LECTURE = "c4-05-what-is-inside"
TITLE = ("Class 4, Lecture 5", "What is inside", "Things to take aboard, and the word the game sends")
MISSION = "MyRuin"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c4-05-what-is-inside/example"
_SCANS = "// ---- Science scans. `Scan of:` names a ROLE, so one record covers every object wearing\n"
_CHARS = "// ---- Characters. The voices in the story.\n"
_CAN = ("// ---- Items. The things a crew can find and carry away.\n## [Items](items)\n\n"
        "### [Survey Canister](canister)\n---\nType: item/quest\nArt: container_small_1a\n---\n"
        "A sealed sample tube from the first survey. The label has faded.\n")
_BOWL_ITEM = ("\n### [The Stone Bowl](stone_bowl)\n---\nType: item/quest\nArt: alien_small_2a\n---\n"
              "A shallow bowl of gray stone. It fits the hollow worn into the top of the altar.\n")
_CACHE = ("### [The Cache](cache)\n---\nRelic: hollow\nPoint: 3600, 0, 500\nRoles: cache\nItem: canister\nQty: 3\n---\n"
          "A stack of sample tubes against the wall of the Nave. The first survey left them.\n")
_LEFT = ("### [What the Survey Left](left)\n---\nScope: shared\nStarts when: at once\n"
         "Objective: Pick up the survey canisters in The Nave\nDone when: collect canister\nReward: 60 credits\n---\n"
         "The first survey left its samples behind. Bring them out.\n\n"
         "A stack of sealed tubes stands against the wall of The Nave, where the first survey set them down forty years ago. "
         "Nobody at DS 1 knows what is in them.\n")
_BOWL_Q = ("\n### [The Bowl](bowl)\n---\nScope: shared\nStarts when: at once\n"
           "Objective: Take the stone bowl out of the niche\nDone when: signal hollow_taken\nReward: 200 credits\n---\n"
           "Something small and heavy sits in the niche at the back of The Gallery.\n\n"
           "It is the one thing in The Hollow worth the trip. Whatever else the crew finds in there, "
           "this is what DS 1 sent them for.\n")
_PRE = "knows what is in them.\n"

STATES = {
    # Lecture 4's file: the template's story.mast, c4-04's mission.amd
    "start": {"folder": "c1-03-editor-and-first-run/example", "over": ("c4-04-places-that-speak/example",)},
    # Step 2: the Items section, above the Characters comment
    "items": {"base": "start", "edits": [("replace", FILE, _CHARS, _CAN + "\n" + _CHARS)]},
    # Step 3: the Cache, below the Niche
    "cache": {"base": "items", "edits": [
        ("replace", FILE, "A recess at the back of the Gallery. Easy to miss.\n\n",
         "A recess at the back of the Gallery. Easy to miss.\n\n" + _CACHE + "\n")]},
    # Step 4: the quest that waits for it, above the Scans comment
    "quest1": {"base": "cache", "edits": [("replace", FILE, _SCANS, _LEFT + "\n" + _SCANS)]},
    "q_three": {"base": "quest1", "edits": [
        ("replace", FILE, "Done when: collect canister", "Done when: collect 3 canister")]},
    # Step 5: the bowl item, then the Niche's role, then its Item line
    "bowl_item": {"base": "quest1", "edits": [
        ("replace", FILE, "The label has faded.\n", "The label has faded.\n" + _BOWL_ITEM)]},
    "niche_role": {"base": "bowl_item", "edits": [
        ("replace", FILE, "Roles: niche\nHidden: yes\n", "Roles: niche, relic_piece\nHidden: yes\n")]},
    "niche": {"base": "niche_role", "edits": [
        ("replace", FILE, "Roles: niche, relic_piece\nHidden: yes\n---\n",
         "Roles: niche, relic_piece\nHidden: yes\nItem: stone_bowl\n---\n")]},
    # Step 6: the second quest. The page's own example.
    "final": {"base": "niche", "edits": [("replace", FILE, _PRE, _PRE + _BOWL_Q)],
              "same_as": (_EX + "/mission.amd",)},
    # Scene 8: the Art line taken out of the canister (lint says clean)
    "noart": {"base": "final", "edits": [
        ("replace", FILE, "Type: item/quest\nArt: container_small_1a\n", "Type: item/quest\n")]},
}

_LINT = "sbs lint MyRuin"
_NS = {"side": False}

STILLS = {
    # The editor. Each window shows the 20 lines round the line named.
    "e_chars": ("vscode", "start", 155, "big", _NS),          # lines 145 to 165: the Characters comment
    "e_items": ("vscode", "items", 160, "big", _NS),         # lines 150 to 170: the Items section, the canister
    "e_cache": ("vscode", "cache", 158, "big", _NS),         # lines 148 to 168: the Cache below the Niche
    "e_quest": ("vscode", "quest1", 56, "big", _NS),         # lines 46 to 66: What the Survey Left
    "e_q3": ("vscode", "q_three", 56, "big", _NS),           # the same lines: `collect 3 canister`
    "e_bowl_item": ("vscode", "bowl_item", 190, "big", _NS), # lines 180 to 200: the Stone Bowl item
    "e_niche_role": ("vscode", "niche_role", 161, "big", _NS),   # lines 151 to 171: Roles: niche, relic_piece
    "e_niche": ("vscode", "niche", 162, "big", _NS),         # lines 152 to 172: the Item line too
    "e_bowlq": ("vscode", "final", 68, "big", _NS),          # lines 58 to 78: The Bowl
    "e_hollow": ("vscode", "final", 98, "big", _NS),         # lines 88 to 108: The Hollow's key
    "e_niche_f": ("vscode", "final", 173, "big", _NS),       # lines 163 to 183: the Niche and the Cache
    "e_noart": ("vscode", "noart", 195, "big", _NS),         # lines 185 to 205: the canister with no Art line
    "e_art": ("vscode", "final", 196, "big", _NS),           # lines 186 to 206: the Art line put back
    "t_final": ("terminal", [("final", _LINT)]),
    "t_q3": ("terminal", [("q_three", _LINT)]),
    "t_noart": ("terminal", [("noart", _LINT)]),
    # THE REAL GAME (planned; not taken yet - see the docstring for the press order)
    "game_c5_quests": ("game", "Helm, the handheld icon then Quests: What the Survey Left and The Bowl in the list, both Active"),
    "game_c5_cache": ("game", "Helm in The Nave, about 700 from The Cache: the three sample canisters drawn ahead, nothing taken"),
    "game_c5_pickup": ("game", "Helm, the ship inside 500 of The Cache: the corner toast 'Pickup: Survey Canister x3'"),
    "game_c5_left_done": ("game", "Helm, the handheld icon then Quests: What the Survey Left Done, The Bowl still Active"),
    "game_c5_bowl": ("game", "Helm at the back of The Gallery, about 700 from The Niche: the stone bowl drawn in its place"),
    "game_c5_bowl_taken": ("game", "Helm, the bowl taken: the corner toast 'Pickup: The Stone Bowl' and the strip line 'Quest complete: The Bowl'"),
    "game_c5_bowl_done": ("game", "Helm, the handheld icon then Quests: both quests Done"),
    # drawn
    "card_three": ("card", "table", {"heading": "Step 1 - A thing, a place, and a word", "nth": 1, "kicker": "Three records make a thing you can take"}),
    "card_wait": ("card", "table", {"heading": "Step 1 - A thing, a place, and a word", "nth": 2, "kicker": "Two ways a quest can wait"}),
    # the page's table under Step 2: the code block above it holds a `##` line, which ends the heading's section for the tool
    "card_art": ("card", "rows", {"kicker": "These shapes can be taken", "header": ["Family", "Keys"],
                                  "rows": [["Containers", "container_1a to container_5c, and container_small_1a to container_small_4c"],
                                           ["Strange objects", "alien_1a to alien_5c, and alien_small_1a to alien_small_5c"]]}),
    "card_made": ("card", "table", {"heading": "Step 6 - The word the game sends", "nth": 1, "kicker": "How the word is made"}),
    "card_when": ("card", "table", {"heading": "Step 6 - The word the game sends", "nth": 2, "kicker": "When the word is sent"}),
    "card_names": ("card", "table", {"heading": "Step 7 - Check it", "nth": 2, "kicker": "Lint names these two", "rows": (2, 3)}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Two caches, two conditions, two breaks"}),
    "card_next": ("card", "title", {"kicker": "Next", "title": "Lecture 8", "sub": "The crew goes in by hand"}),
}

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_c5_cache"},
        {"from": 3, "still": "game_c5_bowl"},
        {"from": 4, "still": "game_c5_pickup"},
        {"from": 5, "still": "game_c5_bowl_taken"},
        {"from": 6, "still": "game_c5_bowl_done"},
    ]},
    "s02_a_thing_a_place_and_a_word": {"step": 1, "beats": [
        {"from": 0, "still": "card_three"},
        {"from": 1, "still": "card_three", "marks": [("part", "r1")]},
        {"from": 2, "still": "card_three", "marks": [("part", "r2")]},
        {"from": 3, "still": "card_three", "marks": [("part", "r3")]},
        {"from": 4, "still": "card_wait"},
        {"from": 5, "still": "card_wait", "marks": [("part", "r1")]},
        {"from": 7, "still": "card_wait", "marks": [("part", "r2")]},
    ]},
    "s03_the_items_section": {"step": 2, "beats": [
        {"from": 0, "still": "e_items", "marks": [("lines", 155, 156)]},
        {"from": 1, "still": "e_chars", "marks": [("lines", 155, 155)]},
        {"from": 2, "still": "e_items", "marks": [("lines", 155, 163)]},
        {"from": 3, "still": "e_items", "marks": [("lines", 156, 156), ("lines", 158, 158)]},
        {"from": 4, "still": "e_items", "marks": [("text", 158, "(canister)")]},
        {"from": 6, "still": "e_items", "marks": [("lines", 160, 160)]},
        {"from": 8, "still": "e_items", "marks": [("lines", 161, 161)]},
        {"from": 10, "still": "card_art"},
        {"from": 13, "still": "e_items", "marks": [("lines", 161, 161)]},
        {"from": 14, "still": "game_c5_cache"},
        {"from": 15, "still": "t_noart", "marks": [("part", "run1:clean")]},
    ]},
    "s04_a_place_that_holds_it": {"step": 3, "beats": [
        {"from": 0, "still": "e_cache"},
        {"from": 1, "still": "e_cache", "marks": [("lines", 154, 162)]},
        {"from": 2, "still": "e_cache", "marks": [("lines", 159, 160)]},
        {"from": 3, "still": "e_cache", "marks": [("lines", 159, 159)]},
        {"from": 4, "still": "e_cache", "marks": [("lines", 160, 160)]},
        {"from": 6, "still": "e_cache", "marks": [("lines", 154, 154)]},
        {"from": 7, "still": "game_c5_pickup"},
        {"from": 8, "still": "e_cache", "marks": [("lines", 160, 160)]},
    ]},
    "s05_a_quest_that_waits_for_it": {"step": 4, "beats": [
        {"from": 0, "still": "e_quest", "marks": [("lines", 51, 61)]},
        {"from": 1, "still": "e_quest", "marks": [("lines", 53, 57)]},
        {"from": 2, "still": "e_quest", "marks": [("lines", 56, 56)]},
        {"from": 3, "still": "e_quest", "marks": [("text", 56, "canister")]},
        {"from": 5, "still": "game_c5_pickup"},
        {"from": 6, "still": "e_cache", "marks": [("lines", 159, 160)]},
        {"from": 7, "still": "e_cache", "marks": [("lines", 154, 154)]},
        {"from": 8, "still": "e_q3", "marks": [("lines", 56, 56)]},
        {"from": 11, "still": "t_q3", "marks": [("part", "run1:clean")]},
        {"from": 12, "still": "e_quest", "marks": [("lines", 56, 56)]},
        {"from": 13, "still": "e_quest", "marks": [("lines", 59, 61)]},
        {"from": 14, "still": "e_quest", "marks": [("lines", 59, 59)]},
        {"from": 15, "still": "e_quest", "marks": [("lines", 61, 61)]},
    ]},
    "s06_the_piece": {"step": 5, "beats": [
        {"from": 0, "still": "game_c5_bowl"},
        {"from": 1, "still": "e_bowl_item", "marks": [("lines", 187, 192)]},
        {"from": 2, "still": "e_niche", "marks": [("lines", 161, 161), ("lines", 163, 163)]},
        {"from": 3, "still": "e_niche_role", "marks": [("text", 161, "relic_piece")]},
        {"from": 8, "still": "e_niche", "marks": [("lines", 163, 163)]},
        {"from": 9, "still": "e_niche", "marks": [("lines", 161, 161), ("lines", 163, 163)]},
        {"from": 10, "still": "e_niche_role", "marks": [("lines", 161, 161)]},
        {"from": 11, "still": "e_niche", "marks": [("lines", 163, 163)]},
    ]},
    "s07_the_word_the_game_sends": {"step": 6, "beats": [
        {"from": 0, "still": "e_bowlq", "marks": [("lines", 63, 73)]},
        {"from": 1, "still": "e_bowlq", "marks": [("lines", 68, 68)]},
        {"from": 2, "still": "e_bowlq", "marks": [("text", 68, "hollow_taken")]},
        {"from": 3, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 4, "still": "game_c5_bowl_taken"},
        {"from": 5, "still": "e_hollow", "marks": [("text", 98, "(hollow)")]},
        {"from": 6, "still": "card_made"},
        {"from": 7, "still": "e_hollow", "marks": [("text", 98, "(hollow)")]},
        {"from": 8, "still": "e_niche_f", "marks": [("text", 169, "(niche)"), ("text", 175, "stone_bowl")]},
        {"from": 9, "still": "card_names"},
        {"from": 10, "still": "card_when"},
        {"from": 11, "still": "e_bowlq", "marks": [("lines", 66, 66)]},
    ]},
    "s08_lint_and_play": {"step": 7, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_noart", "marks": [("lines", 195, 195)]},
        {"from": 2, "still": "t_noart", "marks": [("part", "run1:clean")]},
        {"from": 3, "still": "e_art", "marks": [("lines", 196, 196)]},
        {"from": 4, "still": "game_c5_quests"},
        {"from": 6, "still": "game_c5_cache"},
        {"from": 7, "still": "game_c5_pickup"},
        {"from": 8, "still": "game_c5_bowl"},
        {"from": 10, "still": "game_c5_bowl_taken"},
        {"from": 11, "still": "game_c5_bowl_done"},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item2")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item3")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item5")]},
        {"from": 6, "still": "card_next"},
    ]},
}
