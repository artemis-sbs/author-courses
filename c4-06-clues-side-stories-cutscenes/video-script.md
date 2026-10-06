# C4-6 video script - Clues, side stories and cutscenes

> **CHECKED IN THE REAL ENGINE, 2026-10-04** (by script with the server alone, then with
> server, Helm and Comms and the probe walking the lesson by itself). The report matched
> the mock's line for line: both calls, the fact kept, the third answer, the side story
> hidden, running and done, the cutscene played with 2 shots, the lens at 540 and
> 1440 to 540, and an empty `mast.runtime.log`.
>
> **The cutscene was watched on the main screen** (the server's window, seven pictures
> two seconds apart). Seen:
>
> - Black bars across the top and the bottom for the whole cutscene.
> - Under shot 1, in a dark band low on the screen: `The Altar` in blue, and below it
>   `The tally on the rim stops at forty-one.` in white. Under shot 2: `The Cairn` and
>   `Forty-one stones. One for each day.` Each line fitted on one line.
> - The camera DOES ride a place: no crash and no black screen. What it shows is the rock
>   and the walls around the place, and in shot 2 the crew's own ship in the distance.
>   The place's marker itself is not a thing you can see.
> - When it ends the main screen is back on the ship's own view.
> - `Quest complete: The One Who Stayed` is drawn at the left of the main screen and stays
>   up through the cutscene.
> - **One wart.** The main screen's ship panel (top left) stays up during the cutscene and
>   reads the SUBJECT: the name `The Altar`, then `The Cairn`, with `Energy 0` and both
>   shields `0`. It is the ship's own panel pointed at the thing the camera is on.
> - With NO console connected, the engine's own "connect a client" notice covers the
>   middle of the main screen and the captions are behind it. Connect one console before
>   you record.
>
> **Helm and Comms during the cutscene** (a second run, pictures of all three windows
> every two seconds): neither changes. Helm keeps its own map and controls, Comms its
> own view; only the main screen is taken. Both show `Quest complete: The One Who
> Stayed` at the left. On Helm's map the places are drawn as named contacts in yellow -
> The Ring Plate, The Altar, The Niche, The Cairn - among the rock of the walls, with
> the ship beside The Cairn.
>
> Not looked at: the cone on The Cairn, and the third answer on Comms (the probe
> answers the calls by itself). Measured in the mock on the released
> library built into `data\missions\__lib__` (sbs_utils `6103ee7d`, LegendaryMissions
> `1fec027`): 151 variants of the two files, 145 lint runs, 157 headless runs.
>
> **Re-measured the same evening, after the fixes this lesson's first report caused**
> (sbs_utils `947e3f8a`, LegendaryMissions `298ffb3`, lint from sbs_cli `f28e7f1`): every
> variant linted again and run again in the mock (160 variants, 159 lint runs, 140 headless
> runs), and the page changed where the tools did. Three things are different from the
> first draft. A Cutscenes section that no line
> reads is now a lint warning, so Step 7 starts from that warning. A cutscene the game
> cannot find, and a shot it leaves out, now each write a line to `mast.runtime.log`, and
> the page prints both. And a still shot after a moving shot is filmed on its own
> subject, so the page's old rule "put a shot that moves last" is gone.
>
> **A third, short pass on sbs_utils `0c4c0fae`** (the rows the last fixes touch, every
> variant linted once more, and the lesson's own files run again). One row moved: a
> shot's fields typed below its closing `---` are `clean` in lint again, as in the first
> draft, so that row is back in the table of things nothing reports. On `947e3f8a` lint
> called it an error, and the error was the tool's own mistake.
>
> **The page needs an `sbs.pyz` built from sbs_cli `f28e7f1` or later, which is not
> released.** With the installed tool, lint does not compile `story.mast`, so the two rows
> of Step 8 that say `mast-compile` and `mast-unreachable` print nothing, and the sentence
> "nothing about `story.mast`" means nothing. Every lint line on the page was measured
> with the tool run from source. The library the page needs is sbs_utils `0c4c0fae` or
> later, which is released: without it there is no `section-not-loaded` for a Cutscenes
> section, no `never-revealed`, and nothing in `mast.runtime.log` for a cutscene.
>
> **This lesson hands the student a new recipe card.** The plan has no card for a
> cutscene. Nothing in the `amd` template reads a Cutscenes section, and nothing a writer
> can put in `mission.amd` starts one. The card is one line in the map block and a
> three-line block at the end of `story.mast`. If the template gains the line and the
> library gains a word for it (`Then: cutscene <key>`, say), Step 7 shrinks to one line of
> `mission.amd`.
>
> **Say the wart out loud in scene 10.** The ship panel in the corner of the main screen
> reads `The Altar` and `Energy 0` during the cutscene. A viewer will take it for a
> mistake in the file. It is not, and the page says so in Step 9.
>
> **Side stories for one person are not in this lecture.** The plan's source,
> `relics\sink.amd`, has a Side Stories section of `For:` quests. Those are handed to a
> crew member who goes into the ruin in a suit, which needs Lecture 8. The page shows one
> and says so. What the student builds is a side story for the ship: an ordinary quest
> that a clue starts.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 4 mission, lint clean: The Hollow with The Ring, The Way In, The Altar and The Niche, Surveyor Rook, Marker One, Rook at the Altar, The Rest of It. Lecture 4's exercise NOT done |
| Files touched | `mission.amd`, and `story.mast` (one line in the map block, one block at the end) |
| Template | `story.mast` starts as the current `amd` template, the one with the line that reads a Sides section |
| Library | The released library in `data\missions\__lib__`, sbs_utils `0c4c0fae` or later |
| Command-line tool | An `sbs.pyz` built from sbs_cli `f28e7f1` or later |
| Art pack | None |
| VS Code | `MyMission` folder open, `mission.amd` and `story.mast` in two tabs, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 10 as a server with a Helm console and a Comms console. The server's window must be showing the main screen. At least one console must be connected before the cutscene: with none, the engine's own notice covers the captions |
| Game records | Nothing in this lesson ends a game |

## Confirm on camera

**By script, in the mock, with the lesson's own files.** A probe moved the ship, called the
game's own functions and printed what they returned. Where a cutscene is involved, the
run was started the way a server starts a map, so that the server's window is a main
screen as it is in the game.

- The finished files: lint `clean` (`1 amd + 1 mast file(s): 0 error(s), 0 warning(s)`), a
  headless run passes with labels 63 of 425, and `mast.runtime.log` is empty.
- The page followed literally: the blocks of Steps 2 to 7, typed into Lecture 4's file and
  the template where the page says, give `example\mission.amd` and `example\story.mast`
  byte for byte. Lint is clean after every step except the two the page shows, both in
  Step 7: with the Cutscenes section typed and no map line, the `section-not-loaded` line
  quoted there (line 269); with the `Then:` line typed and no block, the `signal-no-route`
  line quoted there (line 65).
- At the ring a call is waiting, "Surveyor Rook - A recording at the ring", with the
  answers "Log the names." and "Shut it off.". "Log the names." puts `names` on the list
  of what the crew knows.
- At the altar, with the names logged, the call offers three answers. With the ring call
  shut off, two.
- "Play the entry keyed to Dace." leads to the entry. "Mark the side room." lights The
  Cairn, starts The One Who Stayed (it is now in the quest list as Active), and goes on to
  The Rest of It, where "Mark the Gallery." lights The Niche.
- 900 from the cairn: nothing. 300 from it: The One Who Stayed is Done, the crew is told
  `Quest complete: The One Who Stayed`, and the card plays the cutscene to one console,
  the server.
- The cutscene on that console: black bars go up; the console rides The Altar for 4
  seconds with the name `The Altar` and the line `The tally on the rim stops at
  forty-one.`; then The Cairn for 6 seconds with `The Cairn` and `Forty-one stones. One
  for each day.`; then it is put back on the ship. Ten seconds. The lens was 540 from the
  altar, and went from 1440 to 540 from the cairn. With `Framing: huge`, a word the game
  does not know, the lens was 990: that is `medium`.
- The two shots the other way round, the moving one first: the console rides The Altar,
  then The Cairn, then the ship. (In the first draft the still shot was filmed at the
  moving shot's place. That is fixed.)
- What the game writes to `mast.runtime.log`, through the card alone: for
  `cutscene_amd("cairn_scen", ...)`, one line, `Cutscene 'cairn_scen' is not declared in
  any loaded AMD`; for `Subject: carin`, one line, `Cutscene shot 'cairn_shot_2': Subject
  'carin' is neither cast nor a role - shot dropped`. The same first line, with
  `'cairn_scene'`, when the section is not read at all. Nothing for `Cutscene: cairn_scen`
  on a shot, for a shot's fields typed below its closing `---`, for a missing or
  misspelled `Overlay:`, `Framing:` or `Seconds:`, or for `to=role("main screen")`.
- The crew that shuts the ring recording off: no entry, no side room, no side story, and
  flying into The Crypt does nothing.
- The crew that opens the altar call first, presses Back, logs the names and opens it
  again: still two answers.
- With both calls waiting, the altar call is listed above the ring call. With `Priority:
  5` on Rook at the Ring, the ring call is listed first.
- Every row of the five tables in Step 8 and the five "not mistakes": lint on that exact
  file with no probe in the folder, then a headless run of it.
- The exercise as written, items 1 to 3 together: lint clean; the crew that knows hears
  the second take and the crew that does not hears the first; the side is paid 150; the
  cutscene has three shots and lasts fourteen seconds.
- What starts a cutscene: `Then: signal` on a quest; `; signal` on an answer; Card 1's
  route with `quest_succeeded`. Also measured and not on the page: `quest_started` for a
  quest an answer starts, and `relic_marker_lit` for a place lighting, both play it; a
  beat that starts on `reach` sends no `quest_started`, so that route never runs.
- `Subject:` as `altar`, `cairn`, `plate`, `entrance`, `station`, `derelict`, `__player__`:
  each resolved to the thing the page says.
- Lecture 7 on top: its steps typed into this lecture's finished file lint clean, and both
  stories play in one run: the side story and its cutscene, then the survey to a win with
  500 credits.

**By reading the code, not by measuring.**

- The crew has no way to skip a cutscene: `Skippable:` is read, and nothing in the template
  or in LegendaryMissions calls `cutscene_skip`.
- A list of what was learned is kept until the mission is restarted (`boarding.py`,
  `_FACTS`).
- A call's lines and answers are fixed the first time each scene is opened
  (`hail.py`, `_hail_resolve_scene`); Back keeps them (`hail_defer`).
- The server's window wears the `mainscreen` role once it shows the main view
  (`consoles\server_console.mast` in LegendaryMissions). In the mock it did.
- `to=role("__player__")` would take every console on the ship, not only the main screen
  (`camera.py`, `camera_track` assigns each console in the audience). Not measured: the
  mock run had one console.
- A line that does not fit is split against that screen's width (`overlay.py`). The 45
  letters measured are the mock's screen, not a real one. In the engine the page's two
  lines, 40 and 35 letters, each fitted on one line.

**Seen in the real engine** (the server's window, by the coordinator; see the note at the
top).

1. The cutscene itself. The camera rides a place: no crash, no black screen. The picture
   is the rock and the walls around the place, and in the second shot the crew's own ship
   in the distance. The place's marker is not a thing you can see.
2. The black bars top and bottom for the whole cutscene. Under each shot, in a dark band
   low on the screen, the name in blue and the line in white, each on one line.
3. The main screen back on the ship's own view when it ends.
4. `Quest complete: The One Who Stayed` at the left of the main screen, staying up through
   the cutscene.
5. The wart: the main screen's ship panel stays up and reads the subject, `The Altar` and
   then `The Cairn`, with `Energy 0` and both shields `0`.
6. With no console connected, the engine's own notice covers the middle of the main screen
   and the captions are behind it.

**Not seen by anyone. If one is not as described, stop and fix the page.**

1. Helm, Comms and the other consoles during the cutscene. Only the main screen should
   change.
2. The cone on The Cairn, and whether a ship in The Crypt can see it.
3. The Ring Plate and The Cairn as contacts on Helm's map.
4. The third answer on Comms, between the other two.
5. Whether a ship flying the passage at full impulse is caught by `reach plate 500`. The
   ship was moved, not flown.
6. Everything Lecture 4's script lists as unseen: the call's row, the open call, a place
   turning into a contact after an answer.

**Keep off camera.** `Lens:` and `Move:`: they are spots in the whole map, and a writer
who types numbers measured from the ruin puts the camera twenty thousand away. A Side
Stories section: lint warns about it until Lecture 8. `Presentation: orbit` on a call:
it works with no card (measured: the main screen rides the subject while the call is
open), and it belongs to Class 2, Lecture 5.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The game. Comms: the altar call with three answers. Cut to Helm's map, a new
contact. Cut to the main screen: black bars, a caption. Cut back to the bridge.

**Say:** "Last time the ruin could talk. Today it keeps a secret. A crew that listens at
the door gets one more answer further in. That answer opens a side room, and a small
story of its own. And when they find what is in the room, the main screen stops being a
window and becomes a film, for ten seconds."

### 2. What a clue is (0:45 - 2:45)

**Screen:** The table from Step 1 of the page. Then the four rules, one at a time.

**Say:** "A clue is something the crew learns in one place that changes what happens in
another. You already wrote one: Mark the Gallery put a place on the map. Today, two new
words. `learn`, on an answer, writes a word down for this crew. `learned`, on another
answer, counts the words. That is all it does: it counts. It cannot ask for a word by
name. There is one list for the whole ship. And the rule that shapes everything: the game
reads the count when the crew opens the scene, once. If they open a call too early, going
away and coming back does not help. So the clue has to come first on the road."

### 3. The first clue (2:45 - 5:00)

**Screen:** `mission.amd`. Type The Ring Plate below The Niche. Type Marker Zero below
Marker One. Type Rook at the Ring below The Rest of It. Highlight `; learn names`.

**Say:** "Every ship flies through the ring. So the first clue goes there. A place, on
the same spot as the ring, with a role: `plate`. A beat, the same as last time: when a
ship is within five hundred of the plate, Rook calls. And the scene. One take, two
answers. Here is the new part. `Log the names`, semicolon, `learn names`. `names` is my
word. The crew never sees it. They see Log the names."

### 4. The clue opens an answer (5:00 - 7:00)

**Screen:** Rook at the Altar. Add the middle answer. Highlight `if learned >= 1`. Type
The Entry for Dace.

**Say:** "Now the altar. One new answer, between the two that are there. Play the entry
keyed to Dace, and after the round brackets: `if learned` is at least one. A crew that
knows nothing gets two answers. A crew that logged the names gets three. The answer leads
to a new scene. One take: Dace did not come out, and there is a cairn in a side room. One
answer, and it leads on to The Rest of It, so this crew still hears the main recording."

### 5. A side room, and the place in it (7:00 - 8:45)

**Screen:** Relics section. Type The Crypt and The Cairn. Then add `; reveal cairn` to
Mark the side room. Highlight `cairn` in the heading and in the answer.

**Say:** "He said a side room, so there has to be one. A chamber, six hundred, with a
passage to the Nave. That is Lecture 2. And a place in the middle of it, with a cone
standing on it. That is Lecture 3. Now the answer shows it: `reveal cairn`. The key of the
place. Not `crypt`: a room is not a place, and lint will not tell you."

### 6. The side story (8:45 - 10:30)

**Screen:** Quests section. Type The One Who Stayed below Marker Zero. Add `, accepts
stayed` to the answer. Then the "other kind" table from the page, with the Storm's Beacon
record above it.

**Say:** "A side story is a quest that is not part of the main story. Three hashes. It
starts when revealed, so it is asleep and out of the list. It is done when a ship is
within four hundred of the cairn. And the answer starts it: a comma, `accepts stayed`.
Two things after one semicolon. Now, if you open Storm's Beacon you will find a section
called Side Stories, and those are a different animal. Each one says `For`, and a job.
They belong to one person, and they are handed over when that person leaves the ship. We
get there in Lecture 8. Do not type that section today: lint will tell you nothing hands
it out, and lint is right."

### 7. The cutscene: what you write (10:30 - 13:00)

**Screen:** The end of `mission.amd`. Type the Cutscenes section: the cutscene, then the
two shots. Highlight `Cutscene: cairn_scene` on each shot, then `Subject:`, then
`Framing:`, then the line under each fence.

**Say:** "A cutscene is a list of shots. A new section, and its key has to be
`cutscenes`. The first record is the cutscene: its key, and `Letterbox: yes` for the black
bars. Then one record for each shot. Which cutscene it belongs to. What the camera looks
at: a role, the same word I write after `reach`. How near: close, medium or wide. Two
words with a comma is a move: wide, then close. How many seconds. And `Overlay`,
`lower_third`: words at the bottom. A name, and under the fence, the line. Everywhere else
in this file that line is my own note. Here the crew reads it: the name in blue, the line
in white. Two rules. Keep it short: the crew cannot skip it. And keep each line short."

### 8. The card (13:00 - 15:15)

**Screen:** Terminal: `sbs lint MyMission`, the `section-not-loaded` warning. Switch to
`story.mast`. Paste the two lines under `relics_spawn`. Lint: clean. Back to `mission.amd`:
add `Then: signal cairn_found` to The One Who Stayed. Lint: the `signal-no-route` warning.
`story.mast` again: scroll to the end, paste the block. Lint: clean.

**Say:** "Lint first. Nothing in this mission reads a section keyed `cutscenes`. It is
right, and the end of its sentence is the fix: add the line that reads it. That is a
card, in two parts. Part one, in the map block, under the line that builds the ruin: read
the Cutscenes section. I do not change a letter. Lint: clean. It is read now, and still
nothing plays it. So the quest has to say when: `Then: signal cairn_found`. My word. Lint
again: the word is sent and nothing hears it. Part two, at the very end of the script
file: when the word `cairn_found` is sent, play the cutscene with this key, on every main
screen. Two things here are mine: the word, and the key. Lint. Clean."

### 9. Lint (15:15 - 16:45)

**Screen:** Three breaks, each undone. Change `if learned >= 1` to `if learned names`,
lint, read the warning. Change `Subject: cairn` to `Subject: carin`, lint: clean; then
show the line from `mast.runtime.log` on the page. Change `Overlay: lower_third` to
`Overlay: lowerthird`, lint: clean.

**Say:** "Lint. I ask for the word by name. It tells me `learned` only counts. Good: that
answer would never have been offered. Put it back. Now I misspell a subject. Clean. Lint
reads the outside of a cutscene, not the inside of a shot. That shot would be left out.
The game does say so, in one line, in the runtime log, after you have played it. Put it
back. Now I misspell the overlay. Clean again, and this time nothing says anything: the
shot plays with no words. There is a table on the page of the ones nothing tells you
about. Read it before you play."

### 10. Play it (16:45 - 19:00)

**Screen:** Server, Helm and Comms. Fly to The Hollow, through the ring: the call. Log
the names. On to The Vault: the call, three answers. The entry, Mark the side room, Mark
the Gallery. Helm's map. The quest list. Back across The Nave into The Crypt. The main
screen: the bars, the altar and its two lines, the cairn and its two lines, the ship's
view again. Point at the panel in the top left corner while it reads `The Altar`.

**Say:** "Through the ring. Rook, at the ring. Log the names. Across the Nave, up the
tunnel. Rook, at the altar, and there is my third answer. The entry for Dace. Mark the
side room. And the rest of it: mark the Gallery. A new contact on the far side of the
Nave, and a new quest in the list. Back down, straight across, into the side room. And
there it goes. Bars. The altar: the tally on the rim stops at forty-one. The cairn:
forty-one stones, one for each day. And back. One thing you will notice: that panel in
the corner says The Altar, Energy zero. It is the ship's own panel reading whatever the
camera is on. It is not in my file, and I cannot take it away."

### 11. Your turn (19:00 - 19:30)

**Screen:** The exercise on the companion page.

**Say:** "Give Rook a line that only a crew who knows will hear. Pay for the side story.
Add a third shot. Then break one line where lint can see it and one where it cannot. Next
time, the main story."
