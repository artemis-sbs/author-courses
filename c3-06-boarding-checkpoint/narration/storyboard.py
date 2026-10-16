"""Storyboard for c3-06-boarding-checkpoint: what is on screen while each caption is spoken.

Pure data, read by _tools/picture. The format is described in the storyboards of Class 1,
Lectures 5, 6 and 12. Caption numbers are those of shots.py (2026-10-15).

The lecture starts from Lecture 5's finished files ("start": the `sbs create` folder of
Class 1 Lecture 3 for the files nobody edits, with Class 3 Lectures 2 to 5 laid over it,
and Mr Pell added to the roster as "Before you start" has the student do). The scene is
typed in layers: places (l1), readings (l2), the check (l3), the door (l4), the endings
and their quests (l5), then the two stories and the new Account for the Crew ("final", the
page's own example\\mission.amd). story.mast does not change.

THE PAPER (scenes 2 to 4) is drawn from the page's own tables; the pencil (scene 7) is
the finished Scenes section in VS Code, with marks where the pencil goes.

NO COMMAND STARTS THE GAME HERE. `sbs run server,helm,engineering,science -m MyBoarding
map=0` is a drawn card of the page's own words (card_run).

GAME STILLS. Taken in the real engine 2026-10-15; marks set from the screenshots. The handheld a party
member carries is the xESS: BEAM DOWN turns the console into it, Act opens by itself on
each new room (a running transcript, the newest room at the foot, its choices as buttons),
and Back (top right of the ACT title line) goes to the xESS home list (Crew, Act, Tasks).
A choice that nobody
present holds the job for is offered to one console as `<choice> (covering for <job>)`, LAST in the row (which
console is not predictable: in Game 1 the quartermaster cover went to the chief).
The Quest Log is a bridge console's handheld (icon top left), then Quests; `Quest
complete:` lines come on the strip under Helm's left panel. At most three windows, so the
script's "three aboard" is never on one screen: Mr Pell (Helm) stays home in every game.
All three games start from the PROBE-ONLY state g_now (never shown in the editor): Close
Inspection finishes by itself a minute in (`Done when: 60 seconds` in place of `reach
derelict 500`), so nobody has to fly.

    Game 1 - the surgeon and the chief:
    python game.py c3-06-boarding-checkpoint start --state g_now --consoles server,engineering,science
      When the Boarding Party tile appears: on Engineering (Chief Okoro) and Science (Dr
      Hale), the handheld icon, Boarding Party, BEAM DOWN.
      1. Go inboard, Go forward. Science: Read the berth monitors. Step back, Go back to the
         spine, Go below. Science: game_hold_sci. Engineering: game_hold_eng.
      2. Whoever holds Count the stores (covering for quartermaster) takes it. Step back,
         Go back to the spine, Go aft. Engineering: Read the engine log. Step back, Go back
         to the spine. Open the captain's hatch. Science: game_cabin_sci. Engineering:
         game_cabin_eng.
      3. Throw the switch and wake them, then Return to the ship. Both consoles are put
         back at their stations. Within 30 seconds, Science: handheld, Quests, Stand By the
         Sleepers: game_log_standby.
    Game 2 - the chief alone, Helm on the bridge:
    python game.py c3-06-boarding-checkpoint start --state g_now --consoles server,helm,engineering
      1. Before the visit, Helm: handheld, Quests, Account for the Crew: game_log_account6.
      2. Engineering: handheld, Boarding Party, BEAM DOWN. Go inboard: game_alone_spine.
      3. Go forward: game_alone_berths. Take the covered reading. Helm, the strip:
         game_alone_strip.
      4. Step back, Go back to the spine, Go aft, Read the engine log, Step back, Go back
         to the spine, Go below: game_alone_hold. Take the covered stores, Step back, Go
         back to the spine: game_alone_spine_open.
      5. Open the captain's hatch, Leave them sleeping and go for help: game_alone_end.
         Helm: handheld, Quests, Carry Word Home: game_log_carry.
    Game 3 - walk away:
    python game.py c3-06-boarding-checkpoint start --state g_now --consoles server,engineering
      1. Engineering: handheld, Boarding Party, BEAM DOWN: game_walk_airlock.
      2. Return to the ship. Engineering is put back on its station. The handheld icon:
         game_walk_gone.
"""
LECTURE = "c3-06-boarding-checkpoint"
TITLE = ("Class 3, Lecture 6", "Checkpoint: a short boarding quest", "Plan it, type it, check it, play it")
MISSION = "MyBoarding"
FILE = "mission.amd"
MAST = "story.mast"

_EX = "c3-06-boarding-checkpoint/example"
_PELL = "\n### [Mr Pell](pell)\n---\nConsole: helm\nFace: terran_male\nRoles: quartermaster\nSkills: quartermaster 3\n---\n"

# Lecture 5's rooms, which Step 3 deletes (everything under the Scenes heading)
_OLD_ROOMS = (
    "### [The Airlock](airlock)\n"
    "% The outer door was never sealed. Frost on the inside of the glass, and a row of suits still on their hooks.\n\n"
    "- [Read the name tags on the suits](suits) if medical ; learn suits, signal names_read\n"
    "- [Go aft, toward the reactor](reactor)\n"
    "- [Go forward, to the bridge](bridge)\n"
    "- [Return to the ship]()\n\n"
    "### [Six Suits](suits)\n"
    "% Six suits, six names, and every one of them is here. Nobody left this ship through the airlock.\n\n"
    "- [Step back](airlock)\n\n"
    "### [The Reactor Room](reactor)\n"
    "% Cold. The core was shut down by hand, in the right order, by someone who had time.\n\n"
    "- [Read the shutdown record](shutdown) if engineering ; learn shutdown, signal core_read\n"
    "- [Try to wake the core](core_wakes) ; check engineering 9 else core_dead, learn lockout\n"
    "- [Go back to the airlock](airlock)\n\n"
    "### [The Shutdown Record](shutdown)\n"
    "% Shut down from this room, and then the restart key was taken out and carried away. Whoever did it did not mean for her to wake up.\n\n"
    "- [Step back](reactor)\n\n"
    "### [The Core Turns Over](core_wakes)\n"
    "% The board lights for four seconds. Long enough to read one line: MANUAL LOCKOUT, CAPTAIN'S KEY.\n\n"
    "- [Step back](reactor)\n\n"
    "### [The Board Stays Dark](core_dead)\n"
    "% Nothing. Not a flicker. Whatever you tried, the core did not notice.\n\n"
    "- [Step back](reactor)\n\n"
    "### [The Bridge](bridge)\n"
    "%{learned < 2} Every station is dark but one. The log is open on the captain's chair, locked behind a question you cannot answer yet.\n"
    "%{learned >= 2} Every station is dark but one. The log is open on the captain's chair, and now you know what it is going to ask.\n\n"
    "- [Answer the log](last_entry) if learned >= 2\n"
    "- [Pull the sensor record](sensor_record) if skill science >= 3 ; learn sensors\n"
    "- [Go back to the airlock](airlock)\n\n"
    "### [The Sensor Record](sensor_record)\n"
    "% One contact, closing, eleven days before the core went cold. It never arrived. It is still out there.\n\n"
    "- [Step back](bridge)\n\n"
    "### [The Last Entry](last_entry)\n"
    "% Six aboard. Core cold. Key over the side. The last entry is one word: QUARANTINE.\n\n"
    "- [Return to the ship]()\n")
# Step 3: five places
_PLACES = (
    "### [The Airlock](airlock)\n"
    "% The inner door stands open. The air beyond is thin and very cold, and every light is the dull red of a ship running on her last cell.\n\n"
    "- [Go inboard, to the spine](spine)\n"
    "- [Return to the ship]()\n\n"
    "### [The Spine](spine)\n"
    "% One long corridor, bow to stern, frost on every hatch. The captain's hatch is sealed.\n\n"
    "- [Go forward, to the berth deck](berths)\n"
    "- [Go aft, to the engine room](engine)\n"
    "- [Go below, to the hold](hold)\n"
    "- [Go back to the airlock](airlock)\n\n"
    "### [The Berth Deck](berths)\n"
    "% Twelve cold berths in two rows, lids down, frost on the glass. There is a shape behind every lid.\n\n"
    "- [Go back to the spine](spine)\n\n"
    "### [The Engine Room](engine)\n"
    "% The main cell is dark. One small cell in the corner is still warm, and every cable in the room runs to it.\n\n"
    "- [Go back to the spine](spine)\n\n"
    "### [The Hold](hold)\n"
    "% Racks from deck to overhead, and nearly all of them bare. Somebody ate their way through this hold very slowly.\n\n"
    "- [Go back to the spine](spine)\n")
_BACK = "- [Go back to the spine](spine)\n"
_LID = "every lid.\n\n"
_CABLE = "runs to it.\n\n"
_SLOW = "very slowly.\n\n"
_MONITORS = "- [Read the berth monitors](monitors) if medical ; learn alive, signal berths_read\n"
_LOG = "- [Read the engine log](engine_log) if engineering ; learn rationed, signal log_read\n"
_HOLD2 = ("- [Count the stores](stores) if quartermaster ; learn stores\n"
          "- [Pull the cargo scanner's last sweep](sweep) if skill science >= 3 ; learn sweep\n")
_R_MONITORS = ("\n### [Twelve Heartbeats](monitors)\n"
               "% Twelve heartbeats, four to the minute. They are not dead. They are asleep, and the berths are keeping them that way on almost nothing.\n\n"
               "- [Step back](berths)\n")
_R_LOG = ("\n### [The Engine Log](engine_log)\n"
          "% She was never wrecked. Someone shut down everything but the berths, by hand, to make one small cell last for years.\n\n"
          "- [Step back](engine)\n")
_R_HOLD = ("\n### [Nine Days](stores)\n"
           "% Food for twelve people for nine days. Water for six. Whatever they were waiting for, they could not wait for it awake.\n\n"
           "- [Step back](hold)\n\n"
           "### [The Last Sweep](sweep)\n"
           "% The scanner logged one thing leaving this hold: the ship's only boat, with nobody in it and a beacon tied to the seat. They sent for help. It never came.\n\n"
           "- [Step back](hold)\n")
_CHECK = "- [Try to bring up the main cell](cell_up) ; check engineering 9 else cell_down, learn reserve\n"
_R_CELL = ("\n### [The Main Cell Holds](cell_up)\n"
           "% The main cell catches and holds. The lights come up white along the spine, and somewhere forward a pump begins to turn.\n\n"
           "- [Step back](engine)\n\n"
           "### [The Main Cell Drops Out](cell_down)\n"
           "% The main cell coughs twice and drops out. The red lights dim, then steady. It was worth a try.\n\n"
           "- [Step back](engine)\n")
_SPINE_OLD = "% One long corridor, bow to stern, frost on every hatch. The captain's hatch is sealed.\n"
_SPINE_NEW = ("%{learned < 3} One long corridor, bow to stern, frost on every hatch. The captain's hatch is sealed, and the panel beside it asks a question you cannot answer yet.\n"
              "%{learned >= 3} One long corridor, bow to stern, frost on every hatch. The captain's hatch is sealed, and now you know what the panel beside it wants to hear.\n")
_R_CABIN = ("\n### [The Captain's Cabin](cabin)\n"
            "% The captain's last order is taped to the desk: DO NOT WAKE US WITHOUT A DOCTOR. Under it is the master switch for the berths.\n\n"
            "- [Go back to the spine](spine)\n")
_ENDQ = ("### [Stand By the Sleepers](stand_by)\n---\nScope: shared\nStarts when: revealed\n"
         "Objective: Hold station for 30 seconds while the crew wakes\nDone when: 30 seconds\nReward: 300 credits\n---\n"
         "Twelve people are waking up cold. Stay close until they can stand.\n\n"
         "![](icon://hourglass) Thirty seconds, while the last of the lids come up.\n\n"
         "They went to sleep to make one small cell last. Nobody has told them yet how long it lasted.\n\n"
         "### [Carry Word Home](carry_word)\n---\nScope: shared\nStarts when: revealed\n"
         "Objective: Return to within 1000 of DS 1\nDone when: reach station 1000\nReward: 200 credits\n---\n"
         "They asked for a doctor. Go and get one.\n\n"
         "![](ship://starbase_command) DS 1, and the nearest doctor. Within 1000 of her is close enough.\n\n"
         "The sleepers are safe for as long as their one cell lasts. Nobody aboard knows how long that is.\n\n")
_ENDINGS = ("- [Throw the switch and wake them](woken) ; accepts stand_by\n"
            "- [Leave them sleeping and go for help](asleep) ; accepts carry_word\n")
_R_END = ("\n### [Twelve Lids](woken)\n"
          "% The lids lift one at a time. Twelve people, grey and shaking, and the first of them asks what year it is.\n\n"
          "- [Return to the ship]()\n\n"
          "### [Lights Out](asleep)\n"
          "% You close the hatch on twelve sleepers and the cold. Somebody at DS 1 is going to have to send a hospital ship.\n\n"
          "- [Return to the ship]()\n")
_FAMILIES = "Bring the names home, and DS 1 can tell their families something.\n\n"
_OLD_ACC = ("Objective: Find out who was aboard the hulk\nDone when: signal names_known\nReward: 150 credits\n---\n"
            "Somebody crewed that ship. Command wants names.\n\n"
            "## Where names are kept\n\n"
            "- ![](icon://person) Suits. Every suit in an airlock is tagged with its owner's name.\n"
            "- ![](icon://tablet) The log. A captain's log says who is aboard.\n\n" + _FAMILIES)
_NEW_ACC = ("Objective: Find out what became of the hulk's crew\nDone when: signal berths_read\nReward: 150 credits\n---\n"
            "Somebody crewed that ship. Command wants to know what became of them.\n\n"
            "| What | What DS 1 knows |\n|---|---|\n"
            "| Her registry | Not on any list DS 1 keeps |\n"
            "| Her last call | None on record. She went quiet without a word |\n"
            "| Her power | One small cell, still warm. Everything else is cold |\n\n"
            "If anybody is still aboard her, they have been there a long time.\n\n")
_OLD_STORIES = ("### [Six Names](six_names)\n---\nFor: medical\nStarts when: at once\n"
                "Objective: Find out whose suits are hanging in the airlock\nDone when: signal names_read\nThen: signal names_known\n---\n"
                "Six suits on their hooks, and nobody in them. Somebody should read the tags.\n\n"
                "### [A Cold Core](cold_core)\n---\nFor: engineering\nStarts when: at once\n"
                "Objective: Find out how the core was stopped\nDone when: signal core_read\n---\n"
                "A reactor does not shut itself down in the right order. Find out who did.\n")
_NEW_STORIES = ("### [Twelve Berths](twelve_berths)\n---\nFor: medical\nStarts when: at once\n"
                "Objective: Find out whether anyone in the berths is alive\nDone when: signal berths_read\nReward: 50 credits\n---\n"
                "A shape behind every lid. Somebody should look at the monitors.\n\n"
                "### [The Last Watch](last_watch)\n---\nFor: engineering\nStarts when: at once\n"
                "Objective: Find out why the main cell is dark\nDone when: signal log_read\nReward: 50 credits\n---\n"
                "A ship does not go dark this neatly by accident. Find out who did it, and why.\n")

STATES = {
    "start": {"folder": "c1-03-editor-and-first-run/example",
              "over": ("c3-02-party-and-place/example", "c3-03-everyone-gets-a-menu/example",
                       "c3-04-crew-and-skills/example", "c3-05-personal-quests/example"),
              # Before you start: the third person on the roster
              "edits": [("replace", FILE, "Skills: medical 4, science 3\n---\n", "Skills: medical 4, science 3\n---\n" + _PELL)]},
    # Step 3: the practice rooms out, five places in (lint: two unfired-signal)
    "l1": {"base": "start", "edits": [("replace", FILE, _OLD_ROOMS, _PLACES)]},
    # Step 4: the readings and their rooms
    "l2": {"base": "l1", "edits": [
        ("replace", FILE, _LID + _BACK, _LID + _MONITORS + _BACK + _R_MONITORS),
        ("replace", FILE, _CABLE + _BACK, _CABLE + _LOG + _BACK + _R_LOG),
        ("replace", FILE, _SLOW + _BACK, _SLOW + _HOLD2 + _BACK + _R_HOLD)]},
    # Step 5: the check, and its two rooms below The Engine Log
    "l3": {"base": "l2", "edits": [
        ("replace", FILE, _LOG, _LOG + _CHECK),
        ("replace", FILE, "for years.\n\n- [Step back](engine)\n", "for years.\n\n- [Step back](engine)\n" + _R_CELL)]},
    # Step 6: the door, the spine's two lines, the cabin at the end of the rooms
    "l4": {"base": "l3", "edits": [
        ("replace", FILE, "- [Go forward, to the berth deck](berths)\n",
         "- [Open the captain's hatch](cabin) if learned >= 3\n- [Go forward, to the berth deck](berths)\n"),
        ("replace", FILE, _SPINE_OLD, _SPINE_NEW),
        ("replace", FILE, "It never came.\n\n- [Step back](hold)\n", "It never came.\n\n- [Step back](hold)\n" + _R_CABIN)]},
    # Step 7: two ending quests, the cabin's two choices, the two last rooms
    "l5": {"base": "l4", "edits": [
        ("replace", FILE, _FAMILIES, _FAMILIES + _ENDQ),
        ("replace", FILE, "for the berths.\n\n" + _BACK, "for the berths.\n\n" + _ENDINGS + _BACK + _R_END)]},
    # Step 8: two new stories, and Account for the Crew rewritten. The page's own file.
    "final": {"base": "l5", "edits": [
        ("replace", FILE, _OLD_STORIES, _NEW_STORIES),
        ("replace", FILE, _OLD_ACC, _NEW_ACC)],
              "same_as": (_EX + "/mission.amd", "c3-05-personal-quests/example/story.mast")},
    # PROBE-ONLY, for the game stills (see the docstring). Never shown in the editor.
    "g_now": {"base": "final", "edits": [
        ("replace", FILE, "Done when: reach derelict 500", "Done when: 60 seconds")]},
}

_LINT = "sbs lint MyBoarding"
_NS = {"side": False}
_G1 = "Game 1 (state g_now, consoles server,engineering,science; Dr Hale and Chief Okoro aboard, Mr Pell home)"
_G2 = "Game 2 (state g_now, consoles server,helm,engineering; Chief Okoro aboard alone, Helm on the bridge)"
_G3 = "Game 3 (state g_now, consoles server,engineering; Chief Okoro aboard alone)"

STILLS = {
    "e_l1": ("vscode", "l1", 144, "mid", _NS),               # lines 130 to 158: the five places
    "e_l2": ("vscode", "l2", 158, "mid", _NS),               # lines 144 to 172: the readings
    "e_l3": ("vscode", "l3", 160, "big", _NS),               # the engine room's check and its rooms
    "e_l4": ("vscode", "l4", 140, "big", _NS),               # the spine: the door and its two lines
    "e_l5_cabin": ("vscode", "l5", 228, "big", _NS),         # the cabin's two endings and the last rooms
    "e_l5_q": ("vscode", "l5", 86, "mid", _NS),              # lines 72 to 100: the two ending quests
    "e_l5_acc": ("vscode", "l5", 64, "big", _NS),            # Account for the Crew as Lecture 5 left it
    "e_final_acc": ("vscode", "final", 64, "big", _NS),      # lines 54 to 74: Account for the Crew, new
    "e_final_endq": ("vscode", "final", 86, "mid", _NS),
    "e_final_berths": ("vscode", "final", 178, "big", _NS),
    "e_final_stories": ("vscode", "final", 252, "big", _NS),  # lines 242 to 262: the two stories
    "e_sc1": ("vscode", "final", 172, "mid", _NS),           # the pencil: lines 158 to 186
    "e_sc2": ("vscode", "final", 199, "mid", _NS),           # lines 185 to 213
    "e_sc3": ("vscode", "final", 226, "mid", _NS),           # lines 212 to 240
    "t_l1": ("terminal", [("l1", _LINT)]),
    "t_final": ("terminal", [("final", _LINT)]),
    # THE REAL GAME (taken 2026-10-15; see the docstring for the three games and the clicks)
    "game_cabin_sci": ("game", _G1 + ", step 2: Science (Dr Hale), Act on The Captain's Cabin: 'The captain's last order is taped to the desk: DO NOT WAKE US WITHOUT A DOCTOR...' and the buttons Throw the switch and wake them, Leave them sleeping and go for help, Go back to the spine"),
    "game_cabin_eng": ("game", _G1 + ", step 2, the same moment: Engineering (Chief Okoro), Act on The Captain's Cabin: the same line and the same three buttons"),
    "game_hold_sci": ("game", _G1 + ", step 1: Science (Dr Hale), Act on The Hold: 'Racks from deck to overhead...' and her buttons - Pull the cargo scanner's last sweep is hers alone (and Count the stores (covering for quartermaster) if the cover came to her)"),
    "game_hold_eng": ("game", _G1 + ", step 1, the same moment: Engineering (Chief Okoro), Act on The Hold: no sweep; Go back to the spine (and Count the stores (covering for quartermaster) if the cover came to him)"),
    "game_log_standby": ("game", _G1 + ", step 3: Science back at its station, the handheld, Quests, Stand By the Sleepers selected (Active if opened inside 30 seconds of the choice, else Done): Reward 300 credits, the order 'Hold station for 30 seconds while the crew wakes', the line, the hourglass icon with 'Thirty seconds, while the last of the lids come up.', and the last paragraph"),
    "game_log_account6": ("game", _G2 + ", step 1, before the visit: Helm's handheld, Quests, Account for the Crew selected: Active, Reward 150 credits, 'Find out what became of the hulk's crew', the sentence, the two-column table What / What DS 1 knows with three rows (registry, last call, power), and the closing line"),
    "game_alone_spine": ("game", _G2 + ", step 2: Engineering, Act on The Spine, nothing learned yet: '...The captain's hatch is sealed, and the panel beside it asks a question you cannot answer yet.' and four buttons (forward, aft, below, back to the airlock) - no captain's hatch"),
    "game_alone_berths": ("game", _G2 + ", step 3: Engineering, Act on The Berth Deck: Go back to the spine, then 'Read the berth monitors (covering for medical)' LAST"),
    "game_alone_strip": ("game", _G2 + ", step 3, after the chief takes the covered reading: Helm, the strip under the left panel, 'Quest complete: Account for the Crew'"),
    "game_alone_hold": ("game", _G2 + ", step 4: Engineering, Act on The Hold: Go back to the spine, then 'Count the stores (covering for quartermaster)' LAST. The scanner's sweep is not offered at all"),
    "game_alone_spine_open": ("game", _G2 + ", step 4, back on The Spine with three facts: '...and now you know what the panel beside it wants to hear.' and Open the captain's hatch at the top of the buttons"),
    "game_alone_end": ("game", _G2 + ", step 5: Engineering after Leave them sleeping and go for help: Lights Out's line 'You close the hatch on twelve sleepers and the cold...' and the one button Return to the ship"),
    "game_log_carry": ("game", _G2 + ", step 5, at once: Helm, Quests, Carry Word Home selected, Active: Reward 200 credits, 'Return to within 1000 of DS 1', the line, 'DS 1, and the nearest doctor. Within 1000 of her is close enough.' over a small picture of DS 1, and the last paragraph. Stand By the Sleepers is not in the list"),
    "game_walk_airlock": ("game", _G3 + ", step 1: Engineering, Act on The Airlock: 'The inner door stands open...' and the buttons Go inboard, to the spine and Return to the ship"),
    "game_walk_gone": ("game", _G3 + ", step 2, after one press of Return to the ship: Engineering back at its station with its handheld open - no Boarding Party tile any more (the visit is over and cannot be joined again)"),
    # drawn: the paper, and the rest
    "card_title": ("card", "title", {}),
    "card_sentences": ("card", "table", {"heading": "Step 1 - Three sentences", "kicker": "Three sentences, before any rooms"}),
    "card_beats": ("card", "table", {"heading": "Step 2 - The beat sheet", "kicker": "The beat sheet"}),
    "card_drawing": ("card", "points", {"kicker": "The drawing: one room in the middle",
                                        "items": ["airlock - spine", "spine - berth deck", "spine - engine room",
                                                  "spine - hold", "spine - captain's cabin (locked)"]}),
    "card_drawrules": ("card", "list", {"heading": "Step 3 - The places", "kicker": "Three rules for the drawing"}),
    "card_facts": ("card", "table", {"heading": "Step 4 - The facts table", "kicker": "The facts table"}),
    "card_wire": ("card", "table", {"heading": "Step 8 - Two stories, and a quest any party can finish", "nth": 2, "kicker": "Two ways to wire the ship's quest"}),
    "card_checks": ("card", "table", {"heading": "Step 9 - Five checks with a pencil", "kicker": "My scene, checked with a pencil"}),
    "card_run": ("card", "points", {"kicker": "In a command prompt in data\\missions",
                                    "items": ["sbs run server,helm,engineering,science -m MyBoarding map=0",
                                              "Fly inside 500 of the hulk. On each console going: the handheld, Boarding Party, BEAM DOWN"]}),
    "card_exercise": ("card", "list", {"heading": "Exercise", "kicker": "Now write your own"}),
}

# Game stills, 1280x960, marks as fractions of the frame (taken 2026-10-15)
_CB_SWITCH = ("rect", 0.01, 0.855, 0.945, 0.95)      # game_cabin_sci / _eng: DO NOT WAKE US, and the three buttons
_CB_ENDS = ("rect", 0.01, 0.9, 0.588, 0.95)          # ... Throw the switch, Leave them sleeping
_LS_PAGE = ("rect", 0.385, 0.075, 0.97, 0.355)       # game_log_standby: Stand By the Sleepers' page
_LS_ROW = ("rect", 0.0, 0.288, 0.38, 0.36)           # ... its row, Active
_LS_HOUR = ("rect", 0.395, 0.24, 0.785, 0.285)       # ... the hourglass line
_LC_PAGE = ("rect", 0.385, 0.075, 0.99, 0.455)       # game_log_carry: Carry Word Home's page
_LC_PIC = ("rect", 0.385, 0.24, 0.965, 0.35)         # ... DS 1's line over its picture
_LA_TABLE = ("rect", 0.385, 0.24, 0.875, 0.38)       # game_log_account6: the What / What DS 1 knows list
_LA_ROW = ("rect", 0.0, 0.36, 0.38, 0.43)            # ... Account for the Crew, Active
_SO_HATCH = ("rect", 0.01, 0.755, 0.225, 0.88)       # game_alone_spine_open: the line, Open the captain's hatch
_SP_FOUR = ("rect", 0.01, 0.39, 0.875, 0.52)         # game_alone_spine: 'cannot answer yet', four buttons
_BE_COVER = ("rect", 0.195, 0.65, 0.574, 0.7)        # game_alone_berths: the covering button, last
_ST_LINE = ("rect", 0.015, 0.49, 0.275, 0.56)        # game_alone_strip: 'Quest complete: Account for the Crew'
_AH_COVER = ("rect", 0.195, 0.9, 0.565, 0.95)        # game_alone_hold: Count the stores (covering ...), last
_AE_END = ("rect", 0.01, 0.855, 0.83, 0.95)          # game_alone_end: Lights Out, Return to the ship
_HS_SWEEP = ("rect", 0.01, 0.9, 0.3, 0.95)           # game_hold_sci: Pull the cargo scanner's last sweep
_HE_NONE = ("rect", 0.01, 0.9, 0.565, 0.95)          # game_hold_eng: no sweep
_WA_HOME = ("rect", 0.222, 0.26, 0.388, 0.31)        # game_walk_airlock: Return to the ship
_WG_TILES = ("rect", 0.0, 0.12, 0.99, 0.72)          # game_walk_gone: the ePADD, no Boarding Party tile

BOARD = {
    "s01_cold_open": {"step": None, "beats": [
        {"from": 0, "still": "game_cabin_sci", "marks": [_CB_SWITCH]},
        {"from": 2, "still": "game_cabin_eng", "marks": [_CB_ENDS]},
        {"from": 3, "still": "game_log_standby", "marks": [_LS_PAGE]},
        {"from": 3.5, "still": "game_log_carry", "marks": [_LC_PAGE]},
        {"from": 4, "still": "card_title"},
    ]},
    "s02_three_sentences": {"step": 1, "beats": [
        {"from": 0, "still": "card_sentences"},
        {"from": 1, "still": "card_sentences", "marks": [("part", "r1")]},
        {"from": 3, "still": "card_sentences", "marks": [("part", "r2")]},
        {"from": 5, "still": "card_sentences", "marks": [("part", "r3")]},
        {"from": 7, "still": "card_sentences", "marks": [("part", "r2")]},
        {"from": 8, "still": "card_sentences", "marks": [("part", "r3")]},
        {"from": 9, "still": "card_sentences"},
    ]},
    "s03_the_beat_sheet_and_the_drawi": {"step": 2, "beats": [
        {"from": 0, "still": "card_beats", "marks": [("part", "r1")]},
        {"from": 1, "still": "card_beats", "marks": [("part", "r2")]},
        {"from": 2, "still": "card_beats", "marks": [("part", "r3"), ("part", "r4")]},
        {"from": 3, "still": "card_beats", "marks": [("part", "r5"), ("part", "r6")]},
        {"from": 4, "still": "card_drawing"},
        {"from": 6, "still": "card_drawrules", "marks": [("part", "item3")]},
    ]},
    "s04_the_facts_table": {"step": 4, "beats": [
        {"from": 0, "still": "card_facts"},
        {"from": 1, "still": "card_facts", "marks": [("part", "head")]},
        {"from": 3, "still": "card_facts"},
        {"from": 4, "still": "card_facts", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
        {"from": 6, "still": "card_facts", "marks": [("part", "r4"), ("part", "r5")]},
        {"from": 8, "still": "card_facts", "marks": [("part", "r1"), ("part", "r2"), ("part", "r3")]},
    ]},
    "s05_type_it_in_layers": {"step": None, "beats": [
        # the game first: where the typing is going
        {"from": 0, "still": "game_alone_spine_open"},
        {"from": 1, "still": "game_alone_spine_open", "marks": [_SO_HATCH]},
        {"from": 2, "still": "e_l1", "marks": [("hashes", n) for n in (130, 136, 144, 149, 154)]},
        {"from": 4, "still": "t_l1", "marks": [("span", 1, "unfired-signal")]},
        {"from": 5.6, "still": "e_l2", "marks": [("lines", 147, 147), ("lines", 158, 158), ("lines", 169, 170)]},
        {"from": 5.85, "still": "e_l3", "marks": [("lines", 159, 159)]},
        {"from": 6, "still": "e_l4", "marks": [("lines", 137, 138), ("lines", 140, 140)]},
        {"from": 6.75, "still": "e_l5_cabin", "marks": [("lines", 227, 228)]},
        {"from": 7, "still": "e_l5_q", "marks": [("lines", 73, 85)]},
        {"from": 8, "still": "e_l5_cabin", "marks": [("text", 227, "accepts stand_by")]},
        {"from": 9, "still": "e_l5_cabin", "marks": [("lines", 231, 234)]},
        # the game first: the two ending pages in the Quest Log
        {"from": 10, "still": "game_log_standby", "marks": [_LS_ROW]},
        {"from": 11, "still": "game_log_standby", "marks": [_LS_PAGE]},
        {"from": 12, "still": "game_log_carry", "marks": [_LC_PAGE]},
        {"from": 13, "still": "game_log_standby", "marks": [_LS_HOUR]},
        {"from": 13.5, "still": "e_l5_q", "marks": [("text", 83, "icon://hourglass")]},
        {"from": 14, "still": "game_log_carry", "marks": [_LC_PIC]},
        {"from": 14.5, "still": "e_l5_q", "marks": [("text", 97, "ship://starbase_command")]},
        {"from": 15, "still": "e_final_stories", "marks": [("lines", 245, 262)]},
        {"from": 16, "still": "t_final", "marks": [("part", "run1:clean")]},
    ]},
    "s06_a_quest_any_party_can_finish": {"step": 8, "beats": [
        # the game first: the ship's quest's new page
        {"from": 0, "still": "game_log_account6"},
        {"from": 1, "still": "game_log_account6", "marks": [_LA_ROW]},
        {"from": 2, "still": "game_log_account6", "marks": [_LA_TABLE]},
        {"from": 2.5, "still": "e_final_acc", "marks": [("lines", 66, 70)]},
        {"from": 3, "still": "e_final_acc", "marks": [("text", 61, "Done when: signal berths_read")]},
        {"from": 4, "still": "e_l5_acc", "marks": [("text", 61, "Done when: signal names_known")]},
        {"from": 5, "still": "card_wire", "marks": [("part", "r2")]},
        {"from": 7, "still": "e_final_berths", "marks": [("text", 178, "signal berths_read")]},
        {"from": 8, "still": "card_wire", "marks": [("part", "r1")]},
        {"from": 9, "still": "game_alone_berths", "marks": [_BE_COVER]},
        {"from": 9.5, "still": "game_alone_strip", "marks": [_ST_LINE]},
    ]},
    "s07_five_checks_with_a_pencil": {"step": 9, "beats": [
        {"from": 0, "still": "t_final", "marks": [("part", "run1:clean")]},
        {"from": 1, "still": "e_sc1"},
        {"from": 2, "still": "card_checks"},
        {"from": 3, "still": "e_sc1", "marks": [("lines", 162, 162), ("lines", 173, 173), ("lines", 179, 179), ("lines", 184, 184)]},
        {"from": 4, "still": "e_sc2", "marks": [("hashes", n) for n in (186, 193, 198, 203, 208)]},
        {"from": 5, "still": "e_sc1", "marks": [("text", 169, "if learned >= 3")]},
        {"from": 6, "still": "e_sc2", "marks": [("text", 189, "learn rationed"), ("text", 190, "learn reserve")]},
        {"from": 8, "still": "e_sc2", "marks": [("lines", 190, 190)]},
        {"from": 8.5, "still": "e_sc3", "marks": [("lines", 212, 212)]},
        {"from": 9, "still": "e_sc3", "marks": [("lines", 225, 230)]},
        {"from": 10, "still": "card_checks", "marks": [("part", "r4")]},
        {"from": 11, "still": "e_final_stories", "marks": [("text", 247, "For: medical"), ("text", 257, "For: engineering")]},
        {"from": 11.5, "still": "e_sc1", "marks": [("text", 178, "if medical")]},
        {"from": 12, "still": "e_final_endq", "marks": [("text", 77, "Starts when: revealed"), ("text", 91, "Starts when: revealed")]},
    ]},
    "s08_play_it_three_times": {"step": 11, "beats": [
        {"from": 0, "still": "card_run", "marks": [("part", "item1")]},
        {"from": 1, "still": "game_alone_spine", "marks": [_SP_FOUR]},
        {"from": 2, "still": "game_alone_berths", "marks": [_BE_COVER]},
        {"from": 2.5, "still": "game_alone_hold", "marks": [_AH_COVER]},
        {"from": 3, "still": "game_alone_end", "marks": [_AE_END]},
        {"from": 4, "still": "game_hold_sci"},
        {"from": 5, "still": "game_hold_sci", "marks": [_HS_SWEEP]},
        {"from": 5.5, "still": "game_hold_eng", "marks": [_HE_NONE]},
        {"from": 6, "still": "card_beats", "marks": [("part", "r10")]},
        {"from": 8, "still": "game_walk_airlock"},
        {"from": 9, "still": "game_walk_airlock", "marks": [_WA_HOME]},
        {"from": 10, "still": "game_walk_gone", "marks": [_WG_TILES]},
        {"from": 11, "still": "e_sc1", "marks": [("lines", 162, 163)]},
    ]},
    "s09_your_turn": {"step": None, "beats": [
        {"from": 0, "still": "card_exercise"},
        {"from": 1, "still": "card_exercise", "marks": [("part", "item1")]},
        {"from": 2, "still": "card_exercise", "marks": [("part", "item4")]},
        {"from": 3, "still": "card_exercise", "marks": [("part", "item6")]},
        {"from": 4, "still": "card_exercise", "marks": [("part", "item7")]},
        {"from": 5, "still": "card_exercise", "marks": [("part", "item8")]},
    ]},
}
