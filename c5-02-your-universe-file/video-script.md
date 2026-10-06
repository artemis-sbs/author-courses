# C5-2 video script - Your universe file

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | None yet. `MyUniverse` is made on camera in scene 2. There must be no `MyUniverse` folder already |
| Saves | No file named `universe_save_the_kestrel_verge_1.yaml` in `missions\common_data\saves`. If one is there, the first start on camera continues an old game instead of beginning a new one |
| Library | sbs_utils, LegendaryMissions and Open Universe v1.4.0 as released on 2026-10-03, or later. Checked against the sbs_utils working tree between `9a8fa4f5` and `0d127f6e` |
| Template | The `ou` template WITH the two travel lines (`QUEST_ENGAGE_ENABLED`, `WAYPOINTS_ENABLED`) under `UNIVERSE_SELECT`: starter repo commit `f60c78c`, 2026-10-03, committed and NOT yet pushed. A mission from `sbs create -t ou` today does not have them and has no way to leave home; type them in before recording (the note in Step 7, part 4) |
| VS Code | Open on the `missions` folder, with the Artemis AMD extension. A terminal panel open at the bottom |
| Game | Closed. Started on camera in scene 9 with a server, a Comms console and a Helm console |

## Confirm on camera

Nobody has looked at any screen in this lesson. This is what was checked, and how.

**In the real engine (2026-10-03, sbs_utils `27aaa520`), a server with a Helm and a Comms
console, by a probe that calls the game's own functions and writes to a file.** Two
launches of the lesson's mission, with its own save slot:

- Launch 1, a new game: mode `story`; the arrival card is handed `Kestrel Relay` and the
  lesson's line; two stations at home; Engage on, charted places on; Helm is offered
  Engage on an accepted cargo run and Comms is offered Abandon; the ship jumps to the
  run's system, the run completes, credits go from 500 to 900; the save file is written
  with that system in it; `mast.runtime.log` is empty.
- Launch 2, Start on Continue: the same seed, the same system, the run still complete,
  credits still 900. The charted way home is engaged: the ship is back at 0, 0, the card
  is handed `Kestrel Relay` again, and both stations are there.

So the save and Continue round trip is proved in the engine for this small case. The
user's own saves were not touched: the probe used its own title and slot 6, and its file
was deleted afterwards.

**By script, in the mock (headless runs on 2026-10-03), with the lesson's own files:**

- A mission fresh from `sbs create -t ou`, with nothing changed: `sbs lint` says clean, and
  a headless run passes with 79 labels run, so the story compiled.
- The lesson's steps were applied to a fresh template by a script that does exactly what
  the page says. The result is the same, byte for byte, as the files in `example\`. The two
  searches find 4 and 2.
- The finished mission: lint clean, `sbs compile` silent, a headless run passes (82 labels
  when the test runner starts the map, 114 when the server screen's own start path does),
  and `mast.runtime.log` is empty.
- `Mode: story` is read as `story`. With no Scenario chapter the mode is `sandbox`.
- The name and the line handed to the arrival card at home are `Kestrel Relay` and `The
  last relay anyone still maintains. Everything past it is rumor.` With the line split over
  two lines, only the first is handed over.
- Two stations are at home, Kestrel Relay and Starbase, both on the players' side.
- The start screen's mission list is handed the title `The Kestrel Verge` and the two
  description lines.
- With the card, the Engage switch and the charted-places switch are both on. Without it
  (the template as it ships) both are off.
- The Quests tab's own decision function, asked about an accepted cargo run: Helm is
  offered Engage, Comms is offered Abandon.
- The function behind **Accept Cargo Run** was called, then the signal the **Engage**
  button sends. The ship arrived in system 2, -3, the run completed, and credits went from
  500 to 900.
- The save file `universe_save_the_kestrel_verge_1.yaml` was written on the first start.
  After the jump it held `current_system` 2, -3. A second run with Start on Continue began
  in 2, -3 with 900 credits and the completed run. Engaging the charted Kestrel Relay
  brought the ship back to 0, 0, with both stations there.
- A run with Start on New Game replaced the save: new seed, 500 credits, no quests.
- A run after changing the title wrote a second, empty save and left the first alone.
- A second mission with the same title, run after the first, began in the first mission's
  system with the first mission's seed.
- Every row of the four tables in Step 8: by `sbs lint`, by `sbs compile`, and by a
  headless run of the broken file.

**Read in the code, not run:**

- The button words: **Start Mission**, **Accept Cargo Run**, **Engage**, and the Start
  choices **Continue** and **New Game**.
- That `story`, `campaign` and `sandbox` behave alike in a mission with no fleet game. The
  only places the engine asks for the mode are the fleet game, and two checks for
  `skirmish` and `war`.
- That nothing in the game reads the title record's heading, its `Display:` line or its
  prose. In headless runs, changing the heading and the `Display:` line changed nothing,
  and so did removing the `Display:` line and removing the whole fence. The prose was not
  tested that way; no code reads it.

**Run as a function, not as the command:** the title check inside `sbs create`. It refuses
a colon, a leading hyphen and more than 40 characters. It accepts a hyphen in the middle.

**From the crash notes of 2026-09-20, not run again:** a hyphen in `description.yaml`
stops the engine at start-up for every mission. Do not test this on the recording machine.

**NOT seen by anyone.** If one is not as the page says, stop and fix the page:

1. `sbs create MyUniverse -t ou --title "..."` typed without `-y`: what it asks, and what
   it prints.
2. In VS Code, `Ctrl+H` shows how many it found (the page says 4 and 2), and Rename is on
   the right-click menu of a file.
3. The start screen: the title, the two lines, and four options named Start, Player
   Ships, Difficulty and Seed. Start reads Continue.
4. The arrival card: where on the screen it is drawn, on which consoles, and for how
   long. That it shows `Kestrel Relay` and the line.
5. Comms: selecting a station offers **Accept Cargo Run**. Check both stations.
6. Helm's Quests tab: the cargo run is listed, **Engage** is there, and a group named
   **Charted Locations** holds Kestrel Relay.
7. The jump: what the crew sees, and the card on arrival. In the mock the system the run
   leads to was unnamed, so its card would read `Uncharted (2, -3)`. The numbers depend on
   the seed.
8. After Continue, the crew is in that system, and Engage on Kestrel Relay brings them
   home.
9. What a player sees when the universe file was not loaded. The mock shows only the line
   in `mast.runtime.log`.
10. What the start screen looks like with curly brackets in a description line. The mock
    reports an error there and draws nothing more.
11. Whether the crew can dock at Kestrel Relay. The code wires docking for the game's own
    Starbase at home; it was not checked for the landmark.
12. In the real engine, that a mission WITHOUT the two travel lines has no Engage button.
    The mock says so, and so does a note in the shipped mission Storm's Beacon. The
    engine run above had the lines.

Known and not in the lesson: with the word `await` anywhere in `story.mast`, `sbs lint`
ends in a long error on an Open Universe mission. The lesson's `story.mast` has no such
word. A later lecture's card may.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The arrival card reading Kestrel Relay, then Helm's Quests tab with Charted
Locations open.

**Say:** "Last time you played somebody else's universe. This is the first minute of
yours. A title, a place to start with a name you gave it, and a save file, so the game
you stop tonight is still there tomorrow. One file of your own, and a few words changed
in another."

### 2. Make the mission (0:45 - 2:30)

**Screen:** The terminal. Type `sbs create MyUniverse -t ou --title "The Kestrel Verge"`.
Then `sbs lint MyUniverse`.

**Say:** "`ou` is the Open Universe template. The title goes in the mission list. Keep it
to letters, numbers and spaces. No hyphen, no colon, no apostrophe. That is not fussiness:
the title is copied into a small settings file, and a hyphen in that file stops the whole
game from starting. Lint. Clean, and I have not written a word yet."

### 3. What is in the folder (2:30 - 3:30)

**Screen:** The file list in VS Code. Point at `my_universe.amd`, `story.mast`,
`description.yaml`.

**Say:** "Three files matter today. The universe itself, which I write. `story.mast`,
which tells the game which universe file to load and what to call it. And
`description.yaml`, which already has my title. The rest is machinery."

### 4. The file and its title record (3:30 - 6:00)

**Screen:** Right-click `my_universe.amd`, Rename, `kestrel_verge.amd`. Open it. Retype
the `#` record.

**Say:** "My file, my name: small letters, underscores. Inside, one record with a single
hash. That is the universe itself. The name in square brackets, a key in round ones, and
under the fence, what this place is. I am writing this for me and for whoever writes with
me. Players never see this record. It is the title page of the manuscript. What players
read comes in a minute."

### 5. The scenario (6:00 - 7:30)

**Screen:** Type the Scenario chapter under the title record.

**Say:** "Two hashes: a chapter. Its key has to be `scenario`, because that is the word
the game looks for. And one fact: `Mode`. Story is one ship and an ending. Campaign is one
ship over many nights. Sandbox is an open world. Today those three play alike. The word
starts to matter when we add fleets, late in this class. Write the one that is true."

### 6. Name the place they start (7:30 - 9:30)

**Screen:** Scroll past Sides and Jobs to the end. Type the Landmarks chapter and Kestrel
Relay.

**Say:** "Sides and Jobs came with the template. I leave them for the next lectures. At
the end, a new chapter: Landmarks. One place. `At: 0, 0` is home, where every new game
starts. `Kind: station`. And one line under the fence. That line is the first thing my
crew reads when they arrive, so it stays on one line: the card shows the first line and
nothing after it."

### 7. Tell the game about it (9:30 - 13:00)

**Screen:** `story.mast`. `Ctrl+H`: `My Universe`, found 4, Replace All. Then
`my_universe.amd`, found 2, Replace All. Retype the two lines under `@map/`. Point at the
two travel lines under the first `UNIVERSE_SELECT` line. Do not edit them.

**Say:** "Four changes. The title: search, four found, replace all. The file name: two
found, replace all. If those numbers are not four and two, stop and look. Third, the two
lines that start with a double quote. These are what players read on the start screen, so
these are worth writing well. No curly brackets in them. And fourth, two lines I leave
alone. The first gives Helm an Engage button. The second keeps a list of the named places
the crew has been. Without them, your universe is one system with no way out."

### 8. Check it (13:00 - 15:30)

**Screen:** `sbs lint MyUniverse`: clean. `sbs compile MyUniverse`: nothing. Then three
breaks, each undone: `Mode: storey` and lint (a warning); one hash on Scenario and lint
(clean); one letter changed on the `display:` line, then lint and compile (clean, and
nothing).

**Say:** "Two commands now. Lint reads my universe file. Compile reads `story.mast`, and
when it is happy it says nothing at all. Watch what each one catches. A misspelled mode:
lint tells me. One hash too few on Scenario: lint says clean, and in the game every
chapter below it would be gone. And a single letter different in the title here: both
commands are happy, and the game would start with no universe in it. So I count hashes by
eye, one, two, three, and I never retype the title. I search and replace it."

### 9. Play it (15:30 - 18:30)

**Screen:** Start the server, Comms and Helm. The start screen. Start Mission. The
arrival card. Comms: select a station, Accept Cargo Run. Helm: Quests, the cargo run,
Engage. Arrive. Quests: Charted Locations. Stop the game. Open
`common_data\saves\universe_save_the_kestrel_verge_1.yaml`. Start again, Continue. Helm:
Engage on Kestrel Relay.

**Say:** "My title. My two lines. Start is on Continue, and there is nothing to continue,
so this is a new game. And there is the card: Kestrel Relay, and my line. Comms takes a
cargo run. Helm engages it. We are somewhere else. And in the quest list, a charted
location: Kestrel Relay, the way home. Now I stop, here, away from home. This is the save.
It is named after my title, and it knows where I stopped. Start again. Continue. Same
system, same money. Engage the way home. Kestrel Relay. Two warnings about that file. Its
name comes from the title, so a new title is a new, empty game. And New Game on the start
screen replaces it without asking."

### 10. Your turn (18:30 - 19:15)

**Screen:** The exercise on the companion page.

**Say:** "Now make it yours. Your title, your file, your two lines, your front door. Then
break it once on purpose, one letter, and learn where the game tells you about it. Next
time we throw out the two factions that came in the box and write three of your own."
