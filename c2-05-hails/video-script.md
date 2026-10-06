# C2-5 video script - Hails

> **CHECKED IN THE REAL ENGINE, 2026-10-04, a real Comms console and a main screen.** The
> lesson's walk matched the mock line for line: the call on the list, Quill then Chief Ives
> by name, the report finishing the step, 100 then 250 credits, `mast.runtime.log` empty.
> SEEN on Comms: Chief Ives's face and name, the title "Your beacon", the dial and the
> Audio box, the two answers. NOT seen: the Hails tab of the info panel, the quest list
> row, anything with two ships.
>
> **Changed since this script was written (library `98725836`, not yet released when this
> note was written):** `At start: posting` now shows the Available Quests tile and the row
> says how it is taken (seen); `Presentation: orbit` with `Subject: derelict` films the
> hulk on the main screen with the speaker's band under it (seen); `Starts when: 5 seconds`
> starts; a late answer no longer restarts a finished job or un-fails a failed step. The
> page's Step 5 table and its "left out" table are updated.
>
> **Still true, and a decision for the user (B82):** `Scope: ship` does nothing in a
> template mission, because the template grants every quest to the shared story.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 4 mission: Quill's call with answers, the job **Tag the Hulk** taken by "We will tag her.", the beat **Beacon Set** and the scene **Quill Calls Back**. Lint clean |
| Library | sbs_utils v1.4.0 at `49ba0d94` or later and LegendaryMissions at `e61b415` or later, as built into `data\missions\__lib__` on 2026-10-04. Everything on the page was measured on that packaged library, not on a working tree |
| Template | The mission must come from the `amd` template that reads the Characters and Dialogue sections itself (build items B38 and B53: fixed in the starter repo, not pushed when this was written) |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, scrolled to Tag the Hulk |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console. For scene 6, a second start with two player ships is optional (see "Not seen by anyone", item 7) |

## Confirm on camera

Checked on 2026-10-04 in headless runs (the mock) on the packaged library, by a script
that called the game's own functions: the function that builds the rows of the Comms hail
list, the dispatch that list does when a row is picked, the functions that fill Available
Quests and Quests, and the function that counts jobs for the Available Quests tile. The
console was a stand-in that holds the Comms role. Nothing here has been run in the real
engine, and no screen has been seen.

What the runs showed:

- The lesson's steps, applied literally to the Lecture 4 example, give the file in
  `example\`. Lint is clean after every finished step. Between the two halves of Step 1 it
  warns that `report_in` is not there yet.
- After "We will tag her.": Tag the Hulk is running and the side has 100 credits. About 30
  seconds later Tag the Hulk is complete, Report to DS 1 is running, the side still has
  100 credits, and one call waits: `Harbormaster Quill - Your beacon`.
- The function that fills Quests lists `Report to DS 1 (Active)` at that moment. With the
  `Beat` line left in, it does not list it until it is done.
- Opened, the call shows one of Quill's two takes with rows `Back` and `Continue`. After
  Continue the list's heading and the speaker are `Chief Ives`, with a face, and the rows
  are `Back` and the one answer.
- The answer closes the call. Report to DS 1 is complete and the side has 250 credits.
- `Back` on Ives's block puts the call back in the waiting list and leaves the step
  running. Opened again it starts at Quill's block. Sixty seconds unanswered: the call is
  still waiting, and nothing else changed.
- The ship's log gets `Harbormaster Quill - Your beacon - answered (It is ours, DS 1. The
  beacon is set.)`. The record of finished calls holds both conversations, line by line.
- Two calls waiting: the newer one is first. With `Priority: 5` on the older one, the
  older one is first.
- The dial: `off`, `console`, `main` and `both` are accepted. It starts at `both`.
  `console` and `off` turn the main-screen half off.
- Two player ships: both get each call. One ship's yes starts the job for both. Both get
  the report call; the first report pays 150 and the second pays nothing. A yes from the
  second ship after the job was finished and paid started it again, and 34 seconds and
  one more report later the side had 400 credits.
- `Scope: ship` on any of the records: every quest is still held by the shared story, and
  both ships are still called.
- The exercise, followed as written on a stand-in for a student's own file: both endings
  complete the step and pay, and the ending with its `; completes` removed leaves the step
  running with lint clean.
- Every row of the two tables in Step 7 was produced by making that one change, running
  `sbs lint` with nothing but the lesson's files in the folder, and running the game.

Not seen by anyone. If one of these is not as described, stop and fix the page:

1. Report to DS 1 in the quest list while the call waits, and its objective sentence
   beside it. Only the function behind the list has said so.
2. The name and the face changing to Chief Ives on **Continue**, on Comms and on the main
   screen. `Face: terran_male` has not been looked at. If it does not draw a face, pick
   one in the Face Builder (Lecture 2) and change the page.
3. The main screen during a call: the code draws the face, the title, the name, the line
   and a numbered, read-only list of the answers over the view.
4. The dial above the Incoming Hails list, its four words, and the Audio box beside it.
5. The Hails tab of the Comms info panel: the two finished calls, and one of them read
   again.
6. The `answered` line in the ship's log, and where on the Comms console it is read.
7. Two ships. Start the server with Player Ships set to 2 and put a Comms console on each.
   The page's table in Step 5 was measured through function calls only.
8. Whether a crew gets any notice that a step started when Report to DS 1 appears. The
   log has no "started" line; it has `Quest complete: Tag the Hulk`.

Known, and kept out of the lesson on purpose:

- `At start: posting`. It works as data: the job is granted as Posted, the function that
  fills Available Quests lists it as `Tag the Hulk (Posted)` with no Accept, the 30 second
  clock does not run until an answer accepts it. But the Available Quests tile is only
  offered when the board holds a job that can be accepted, and a posted job does not
  count. In this mission the tile's count is 0, so the posted job would be on no screen.
  The page says so in "Further reading". When that is fixed, posting is a three-minute
  step between scenes 2 and 3.
- `Scope: ship`, `Presentation:` and `Audio:`. See the page's "Further reading" table.
- A call placed on a clock. `Starts when: 5 seconds` on a beat never starts it (measured:
  the beat stays running and no call comes; lint clean). The Lecture 3 exercise's way,
  a timed quest with `Then: reveal`, is the one that works.
- A deadline on the report step. The step fails and charges, the call stays in the list,
  and a late answer completes the step and pays. It is a row in Step 7, not a step.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The Comms console. The quest list shows Report to DS 1. One row in Incoming
Hails: Harbormaster Quill - Your beacon. Open it. Quill asks. Continue. Chief Ives. Pick
the answer. The step completes.

**Say:** "Last time she called to say well done, and nothing depended on it. This time the
job is not finished until the crew picks up and says so. And she is not alone on the
line."

### 2. A step only an answer can finish (0:45 - 4:15)

**Screen:** `mission.amd`, Tag the Hulk. Delete the `Reward:` line. Change `Then: reveal
beacon_set` to `Then: reveal report_in`. Add the sentence to the description. Then select
the whole Beacon Set record and type Report to DS 1 over it. Point at each line of the
table on the companion page.

**Say:** "Three changes to the job. The reward comes off. Then, reveal report_in. And one
more sentence, so the crew knows the pay comes later. Now the beat below it. I am
replacing it with a quest. No Beat line: so it is in the quest list while it runs, and a
beat is not. An objective, which sends the crew to Comms. The reward, which has moved
here. The same Action as before: Action works on any quest, the moment it starts. And
look at what is missing. No Done when. Nothing in the game finishes this step. Only an
answer can."

### 3. The answer that finishes it (4:15 - 6:30)

**Screen:** End of the file, Quill Calls Back. Replace the two takes. Replace the answer
with `- [It is ours, DS 1. The beacon is set.]() ; completes report_in`. Then type a
second answer, `- [Not now, DS 1.]()`, pause on it, and delete it.

**Say:** "She should be asking now. Two takes, both questions. And the answer: completes
report_in. That is the word from last time. It finishes the step and pays it. Now a
mistake that looks like good manners. A second answer: not now. A crew that picks it has
ended the call. It does not come back, and the step sits in the quest list for the rest
of the game. So the rule: every answer that ends this call finishes the step. The crew
already has a way to say not now. It is the Back button."

### 4. A second voice (6:30 - 9:30)

**Screen:** Characters section. Type Chief Ives below Quill. Back to Quill Calls Back. Add
`@quill` above her takes, then a blank line, `@ives`, and his two takes. Then show the
four rules on the companion page. Type `@Chief Ives` in place of `@ives`, pause, undo.

**Say:** "A call can have more than one person on it. First the person: a heading, a key,
a face. Now the scene. At quill starts her block, as it did in lecture three. At ives
hands the call to him. His own takes. The crew reads her, presses Continue, and reads
him, under his name and his face. Four things. The call is still Quill's in the list. The
line is the at sign and a key, nothing else. Write his name there, or a space, or a
colon, and it stops being a block: his lines become more takes for her, and lint will not
tell you. Each block has its own takes. And the answers come with the last block."

### 5. Which call is on top (9:30 - 11:00)

**Screen:** The table in Step 4 of the companion page. Then add `Priority: 5` to the fence
of Quill Calls Back.

**Say:** "You have several calls now, so here is how the list works. Newest on top. A row
is a name and a title, so every call you place wants a title. A call never times out. And
one call is open at a time. If a call must not be buried, give its scene a priority. A
whole number. Higher sits above lower, however new the others are. I use it for the call
a step is waiting on, and for nothing else."

### 6. Who gets called (11:00 - 13:00)

**Screen:** The table in Step 5 of the companion page. Then highlight `Artemis, DS 1.` in
Quill Checks In. Then highlight `Scope: shared` on Tag the Hulk.

**Say:** "Who does she call? Every player ship. With one ship, that is the whole story.
With two, each ship gets its own copy of the call and answers for itself. But the job is
shared: one yes starts it for everyone. Both ships get the report call, and the first to
report is paid. Two things for you as the writer. This take says Artemis. The Intrepid
reads it too. And look at the last row: a ship that says yes after the job is finished
starts it again. So a job handed out by a call belongs in a mission flown by one ship.
You will see Scope ship in the documentation. In this mission it changes nothing. Leave
it shared."

### 7. What Comms can do with a call (13:00 - 14:30)

**Screen:** The table in Step 6 of the companion page.

**Say:** "Nothing to type here. This is what the person at Comms can do with what you
wrote. Leave it: it waits. Open it: the bridge sees it on the main screen too. Back: it
goes back in the list and nothing in the story has changed. The dial moves where it is
drawn. The Hails tab keeps every finished call. And the ship's log gets one line per
call. So an answer is a decision made once. Everything else lets the crew put it off, or
look back at it."

### 8. Lint (14:30 - 16:15)

**Screen:** Terminal: `sbs lint MyMission`, clean. Misspell `report_in` after `completes`,
lint, show the warning, undo. Change `@ives` to `@ivse`, lint, show the warning, undo.
Change `Priority` to `Priorty`, lint, undo. Then change `@ives` to `@Chief Ives`, lint:
clean. Undo. Delete `; completes report_in` from the answer, lint: clean. Undo.

**Say:** "Lint. Clean. A key that is not a quest: it tells you the answer does nothing. A
voice that is nobody in the cast. A field it does not know. Now two it cannot see. His
name where his key goes: clean, and his block is gone. And an answer that finishes
nothing: clean, and the job never ends. Those two you check by eye. The page has the
whole list."

### 9. Play it (16:15 - 19:00)

**Screen:** Server, Helm and Comms. Fly inside 500. Take the job. Show the quest list.
Wait for the beacon. Show Report to DS 1 in the list and the new call. Open it, Continue,
then Back. Show the call back in the list and the step still running. Open again,
Continue, answer. Show the step done and the log line. Open the Hails tab.

**Say:** "We will tag her. The job is running. Thirty seconds. Done, and not paid. The
list says report to DS 1, and there is the call. Quill. Continue. Chief Ives. Now Back.
The call is waiting, the step is waiting. Open it again: it starts with her. Continue.
It is ours. Paid. One line in the log. And here, every call we have had, to read again."

### 10. Your turn (19:00 - 19:40)

**Screen:** The exercise on the companion page.

**Say:** "Your second call, the one your timer places. Turn its beat into a step the crew
can see, make every ending finish it, and put a second voice on the line. Then break it
on purpose, so you have seen what a call that finishes nothing looks like. Next time:
reputation."
