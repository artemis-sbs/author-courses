# C4-7 video script - Quests through a ruin

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script).** All 73 report lines
> as in the mock: the door at 600, the altar at 500 finishing the step and placing the
> call together, "Mark the Gallery." lighting the niche, the niche at 300, the second call,
> "Take it aboard.", WIN with 500 credits; `mast.runtime.log` empty. ONE DIFFERENCE: in
> the engine The Altar's scan text was already there on the first read, so the ship's
> sensors scan a place by themselves once it is lit. Step 6 stands. Nothing was looked at
> on a console: can Science SELECT a place, the quest list, the end screen, and whether
> 20 minutes is enough to fly it are all unseen.
>
> **Changed since this script was written (sbs_utils `503ac681`):** `When:` where
> `Done when:` was meant is named by lint (`quest-never-finishes`); `collect` is no longer
> told "nothing wears" its item; a scan record typed in the Relics section is called a
> scan record. Step 7 is updated.
>
> **For the user:** the shipped `stormsbeacon.amd` writes its chain steps the old way (33
> of them); see B86 in the plan.

> **MOCK ONLY, 2026-10-04.** Nothing in this lesson has been run in the real game engine,
> and nobody has looked at a screen. Every claim below was measured by script in the mock
> (57 variants of the file, 60 headless runs, 23 of them to a won or lost game) on the
> released library built into `data\missions\__lib__` (sbs_utils `488df12c`,
> LegendaryMissions `abab230`), without `--use-working-tree`. An engine check by script is
> requested in the pilot's report (`_c47_probe`).
>
> **The one thing to see before recording:** Step 6. Whether the Science console can
> select a place in a ruin and show the reading written for its role. In the mock the
> contact becomes selectable when it lights, and a forced scan returns the text. Whether the
> engine lets Science select it, and whether the ship's sensors scan it by themselves, has
> not been seen. If Science cannot read a place, cut scene 7 and Step 6 of the page.
>
> **Do not teach the spelling in Storm's Beacon's `EPISODE_TEMPLATE.md`.** It writes
> `State: secret` and `When: reach <role> <n>` for a step. Measured in this mission: such a
> step appears when the ship arrives and never finishes, and lint says clean. The page
> says so in its Further reading.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 4 mission, lint clean: The Hollow, three places, Surveyor Rook, Marker One, Rook at the Altar, The Rest of It. Lecture 4's exercise NOT done (no Marker Two, no What Rook Left, no Rook at the Niche) |
| Files touched | `mission.amd` only |
| Template | `story.mast` is the current `amd` template, unchanged. `example\story.mast` is that file. It has one line more than Lecture 4's example: the line that reads a Sides section |
| Library | The released library in `data\missions\__lib__`, sbs_utils `488df12c` or later |
| Art pack | None |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console, a Comms console and a Science console |
| Game records | Scene 9 ends a game. A recording take adds a line to `game_results.yaml`. That is fine for a real play; say nothing about it |

## Confirm on camera

**By script, in the mock, with the lesson's own files.** A probe moved the ship, called the
game's own functions and printed what they returned.

- The finished file: lint `clean` (`1 amd + 1 mast file(s): 0 error(s), 0 warning(s)`),
  `sbs compile` prints nothing, a headless run passes with labels 59 of 422, and
  `mast.runtime.log` is empty.
- At the start the quest list for the shared story holds The Hollow Survey and one step,
  Find the Way In. The other three steps are hidden.
- The ship 1500 from The Way In: nothing. At 600: Find the Way In is done, the side has
  50 credits, The First Marker is running.
- 900 from The Altar: the contact is lit and the step is not done. At 500: The First
  Marker is done (100 credits), The Second Marker is running, and one call is waiting,
  "Surveyor Rook - A recording at the altar".
- "Play the rest." then "Mark the Gallery." lights The Niche.
- 900 from The Niche: not done. At 300: The Second Marker is done (200 credits), What Rook
  Put Back is running, and a second call is waiting, "Surveyor Rook - A second recording".
  With the first call unanswered, the second is listed above it.
- "Take it aboard." closes the call, sends `hollow_taken`, finishes the step (500
  credits) and the arc, and ends the game as a win with the `Win:` sentence. The same
  through "What is it?" first.
- The crew is told, in this order: `Quest complete: Find the Way In`, `Quest complete: The
  First Marker`, `Quest complete: The Second Marker`, `Quest complete: What Rook Put Back`,
  `Mission complete: The Hollow Survey`.
- With `Fails when: 20 seconds` and the ship sitting still, the game ends as a loss with
  the `Lose:` sentence, and the crew is told `Mission failed: The Hollow Survey`.
- The niche before the altar: nothing is finished. After the altar, back at the niche: The
  Second Marker finishes.
- "Shut it off." at the altar: The Niche stays dark. At 1100 from it the contact lights.
  At 300 the step finishes.
- The second call left unanswered, the ship sent away and brought back: still one copy of
  the call.
- Science, by a forced scan of the place's contact: before the contact lights it is marked
  as not selectable; after, it is selectable; the `scan` tab reads the Altar Reading text,
  and with the exercise's record the `intel` tab reads its text.
- Every row of the four tables in Step 7 and the four "not mistakes": lint on that exact
  file with no probe in the folder, then a headless run of it.
- The exercise as written (items 1, 2 and 3 together): lint clean. "Take it aboard." pays
  to 500 and does not end the game; back at DS 1 the game is won with 600. "Leave it where
  he put it." ends the game as a loss with the reworded sentence.
- The page followed literally: the blocks of Steps 2 to 6, typed into Lecture 4's file
  where the page says, give `example\mission.amd` byte for byte. Lint is clean after every
  step.

**By reading the code, not by measuring.**

- The game looks for `reach` every two seconds (`quests\quest_driver.mast` in
  LegendaryMissions, the `quest_fail_watch` loop). The page's "keep the number at 300 or
  more" is advice built on that. A ship passing through a small circle was not measured.
- An answer's `; reveal` makes the contact selectable the same way coming close does
  (`amd_relics.py`, `_relic_light`).
- `reach` counts any player ship, and from Lecture 8 a crew member's suit
  (`quest_driver.py`, `quest_tick_reach`).
- Twenty minutes: the clock was measured at 20 seconds only.

**Not seen by anyone. If one is not as described, stop and fix the page.**

1. The quest list on a console: The Hollow Survey with its steps under it, and each new
   step appearing.
2. Science selecting The Altar and reading the `scan` tab. See the note at the top.
3. Whether the ship's own sensors scan a place without anybody at Science.
4. The second call at the top of the Incoming Hails list, above the first.
5. The end screen with the `Win:` sentence, and with the `Lose:` sentence.
6. Where the three `Quest complete:` lines are drawn.
7. How long the flight takes. Nobody has flown it. If twenty minutes is tight on camera,
   say so and change the number in the page.
8. Everything Lecture 4's script lists as unseen: the call's row, the open call, The Niche
   turning gold on Helm's map.

**Keep off camera.** Suits. Picking anything up. A step that finishes on a scan
(`Done when: scan 1 altar`): it worked in the mock with a forced scan, and Class 1,
Lecture 10 already tells the student why not to write one.

## Scenes

### 1. Cold open (0:00 - 0:50)

**Screen:** The game. The quest list: The Hollow Survey, one step. Cut to Helm flying into
The Vault, then the quest list with three steps. Cut to Comms: "Take it aboard." Cut to the
end screen.

**Say:** "Last time the ruin could talk. Today it has a story. Four steps, one after
another, each in a different part of the ruin. The crew is paid for each, and the last one
ends the game. I did not open the script file once."

### 2. What an episode is (0:50 - 2:40)

**Screen:** The first table from Step 1 of the page, then the second.

**Say:** "There is a shipped campaign called Storm's Beacon, and it is made of ruins like
this one. Each ruin is one episode, and every episode is the same chain. The approach: the
crew comes up to the way in. A call: somebody who knows the place tells them something. A
room. A call. A room. And at the end, the piece: they take away what the ruin was hiding.
You can already write every link in that chain. A step that finishes when the ship gets
somewhere is Class 1. A call when the ship gets somewhere is last lecture. A step that
waits for a word is Class 1 again. Here is what is new today: where the word comes from.
Nobody can leave the ship until next lecture, so today Comms says it."

### 3. The heading (2:40 - 4:00)

**Screen:** `mission.amd`, Quests section. Below Marker One, type The Hollow Survey.

**Say:** "The story needs a heading. An arc: three hashes, and the word `Arc` alone on the
first line. It starts at once. It fails after twenty minutes. A `Win` sentence for when it
is finished, a `Lose` sentence for when it fails. All of that is Class 1. Nobody warns the
crew about the clock, so I say twenty minutes in the description."

### 4. The way in (4:00 - 6:30)

**Screen:** Type Find the Way In. Then scroll to The Way In in the Relics section and
point at `Roles: entrance`, then at `(way_in)`.

**Say:** "The first step. Four hashes, so it belongs to the arc. And this line:
`Done when: reach entrance 1000`. Last time I wrote `Starts when: reach altar 600`, to
start a beat. This is the same sentence in a `Done when` line, so it finishes a step. The
rules have not changed. `entrance` is a role: the word on the place's `Roles` line. This
place's key is `way_in`. The key does not work here, and lint will tell you. A thousand is
how close. And always write the number. Without it the game uses five thousand, and the
step is finished before the crew has seen the ruin. One more thing for numbers inside a
ruin: the game looks every two seconds, so do not go below about three hundred."

### 5. Room by room (6:30 - 9:15)

**Screen:** Type The First Marker and The Second Marker. Go back to Find the Way In and
add `Then: reveal survey/first`. Scroll up to Marker One and put the two `reach altar 600`
lines side by side, or highlight each.

**Say:** "Two more steps. Both say `Starts when: revealed`, so they are asleep. The way in
reveals the first. The first reveals the second. The full address every time: the arc, a
slash, the step. Now look. `reach altar 600` is in my file twice. On the beat, in a
`Starts when` line, it starts the call. On the step, in a `Done when` line, it finishes
the step. They happen together: the ship comes into the Vault, the step is done and Rook
is on Comms. The second step sends the ship to the Niche, the place I hid. The crew can
find it because Rook tells them, or because they go and look. So if Comms shuts the
recording off, the story can still be finished."

### 6. The step that waits for a word (9:15 - 12:30)

**Screen:** Type What Rook Put Back. Add `Then: reveal survey/take` to The Second Marker.
Go to the end of the Dialogue section and type Rook at the Niche and What It Is. Highlight
`signal hollow_taken` in the step and in both answers.

**Say:** "The last step is the piece. Somebody takes the thing. Nobody can leave the ship
today, so this is a decision Comms makes. The step says `Done when: signal hollow_taken`.
It waits for a word. `hollow_taken` is my word. And `Action`: the moment the step starts,
Rook calls with a second recording. Now the scene. Two takes. Two answers. One asks what
it is, and leads to a second scene. One says take it aboard, and after the semicolon:
`signal hollow_taken`. That sends the word. The step hears it, pays, and it was the last
step, so the game is won. Look at the ways out of this conversation. There are two, and
both send the word. That is on purpose. If I add an answer that just hangs up, a crew that
picks it has spent the call, and the step can never be finished. The crew's way of saying
not now is the Back button. Why a word, and not `completes`, the way Class 2 did it?
Because the step does not care who says the word. Next lecture a crew member can go and
take the bowl by hand, and this step will not change by one letter."

### 7. What Science reads (12:30 - 13:45)

**Screen:** The Scans section. Type Altar Reading and Niche Reading. Then show The Altar's
fence in Relics and point at its `Scan:` line.

**Say:** "Last time I put a `Scan` line on the Altar. That is for a person standing there.
The Science console on the ship does not show it. Science reads scan records, the ones
from Class 1. A place wears a role, and a role is all a scan record needs. `Scan of`, the
role, a tab, a reading. One on the place for a person. One in Scans for the ship."

### 8. Lint (13:45 - 15:45)

**Screen:** Terminal: `sbs lint MyMission`, clean. Then three breaks, each undone. Change
`reach entrance 1000` to `reach way_in 1000`, lint, read the warning. Change
`Then: reveal survey/first` to `Then: reveal first`, lint, read the warning. Delete
`Part of:` and `Required:` from What Rook Put Back, lint: clean.

**Say:** "Lint. Clean. Now I use the key where the role goes. Nothing in this mission
wears a role called `way_in`. Good: that step would never have finished. Put it back. Now
I drop the arc from a `reveal`. It tells me the step is `survey/first` to the game, and to
write that. Put it back. Now I take these two lines off the last step. Clean. And this one
matters. The other three steps still say they are required. So the game decides the arc is
finished when those three are, and the crew wins at the niche with the last call still
ringing. Lint cannot see that. Read your steps: all of them have the two lines, or none of
them."

### 9. Play it (15:45 - 18:30)

**Screen:** Server, Helm, Comms and Science. The quest list. Fly to The Hollow: the first
step completes. In through The Mouth, The Nave, up the tunnel: the second completes, Comms
has the call. Science: select The Altar. Comms: Play the rest, Mark the Gallery. Fly to
The Gallery: the third completes, the second call arrives. Take it aboard. The end screen.

**Say:** "One step in the list. Fly to the door. Done, and paid, and here is the next. In
through the Mouth, the Nave, up the tunnel. Done again, and Rook is calling. Science: the
Altar, and there is my reading. Comms: play the rest. Mark the Gallery. Back across the
Nave, into the built room, to the far end. Third step. A second recording. Take it aboard.
And that is the game."

### 10. Your turn (18:30 - 19:15)

**Screen:** The exercise on the companion page.

**Say:** "Give the Altar a second tab. Add a fifth step that carries the bowl home. Give
the crew a way to lose on purpose. Then break one line where lint can see it and one where
it cannot. Next time, the crew goes outside."
