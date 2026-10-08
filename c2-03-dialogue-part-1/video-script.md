# C2-3 video script - Dialogue, part 1

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **The student's mission is `MyMission`** as Lecture 2 of this class left it
>   (`c2-02-characters-and-faces\example\mission.amd`, with Lecture 1's `story.mast`). The
>   game is started with `sbs run server,helm,comms -m MyMission map=0`.
> - **`example\` holds the one file that differs from that start:** `mission.amd`.
> - **What changed from the first version of this lecture.** The class now chains, so
>   Close Inspection is a step of the arc Salvage Run, and its one `Then:` line is spent on
>   Find the Lifeboat. The beat that places the call therefore starts on a trigger of its
>   own, `Starts when: reach derelict 500`, in place of `Starts when: revealed` and a
>   `Then: reveal` on the quest. Three ways were tried in the mock: this one; `Action:`
>   typed on Find the Lifeboat; and a beat revealed by Quick Work. All three place the
>   call at the hulk and leave the story's win alone. This one was chosen because it
>   needs no edit to any other record and does not fail when the bonus does. The
>   Characters section, and the two lines of `story.mast` the first version pasted, are
>   already there.
> - **A trigger after `Starts when:` works on a beat only** (measured). On a record with
>   no `Beat` word the same line starts nothing: the record is listed under Available
>   Quests and no call is placed. The page says so, in Step 4 and in its tables.


> **Re-measured 2026-10-08, in the mock.** Tool as installed in `data\missions`, library
> as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were applied one at a
> time to the Lecture 2 example with lint after each. Then one-change variants of the
> finished file: each linted, each played headless by a probe that puts the ship 300 from
> the hulk, reads the rows the Comms hail list would show (the same function the list
> calls), opens the call and presses what the list offers. Every line of tool output in a
> code block on the page is a line a run printed (`verify_page.py`).

> **CHECKED IN THE REAL ENGINE, 2026-10-03, by a script, on the first version** (a server
> and a Comms console; the script called the game's own functions and wrote what they
> returned to a file): no call before the quest finished; one call after; the row
> `Harbormaster Quill - About that hulk`; she has a face; one take from each block; the
> list titled `Incoming Hails`, then her name while the call is open; `Back` and
> `Continue`, then `Back` and `Close`; a take with curly brackets is drawn. The scene has
> not changed since. What starts the beat has: `Starts when: reach derelict 500` on a beat
> has NOT been run in the engine. In Class 1 the engine finished `Done when: reach
> derelict 500` for a ship put 300 from the hulk.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 2 leaves it: `mission.amd` ends with Captain Sable's description, and Quick Work is the last record of the Quests section |
| Lint | `sbs lint MyMission` says `clean` |
| VS Code | `MyMission` folder open, `mission.amd` in one tab scrolled to the end, `story.mast` in another at line 49 |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 8 with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless play with the packaged library.
"Engine" is the run of 2026-10-03 in the note above. If an item fails while recording,
stop and fix the page.

1. Lint is `clean` after Step 1, Step 3 and Step 4. (Lint.)
2. With the scene written and no beat, no call is ever placed. (Mock.)
3. On the finished file: no call waits at the start. With the ship 300 from the hulk,
   Close Inspection completes and one call waits, on the row `Harbormaster Quill - About
   that hulk`. (Mock. Engine, with the first version's beat.)
4. Opened, the list is titled `Harbormaster Quill`, she has a face, and the rows are
   `Back` and `Continue`; then `Back` and `Close`. One take from each block is said.
   (Mock, Engine.)
5. `Back` returns the call to the list. Twenty seconds later it is still there. Opened
   again it starts at her first block with the same takes. (Mock.)
6. Over four plays with different seeds, more than one opening take came up. (Mock.)
7. DS 1 Calls is not in the list the Quest Log is filled from, before or after the call.
   (Mock.)
8. The whole story still plays to its win with the call answered: 500 credits. (Mock.)
9. Every row of the four tables in Step 5. (Lint for all, Mock for all.)
10. The exercise: a second beat with `Starts when: reach lifeboat 500` places a second
    call at the lifeboat. (Lint, Mock.)

Not seen by anyone, and to watch for while recording:

1. The Incoming Hails list on a real Comms console, and where on the screen it sits.
2. The open call: her face, the title, her name, the line.
3. The call on the main screen as well as on Comms.
4. Which the crew notices first: Close Inspection showing `Done`, or the call.
5. A second game showing a different take. It is chance, so it can take a few tries.
6. What a caller with no portrait looks like (`Face: woman`).

## Scenes

### 1. Cold open

**Screen:** The Comms console. The ship closes on the hulk. A row appears in the hail
list: Harbormaster Quill - About that hulk. It opens: her face, her line.

**Say:** "You've got a cast now, | and so far nobody has said a word. || Today the
harbormaster picks up the microphone. || When the crew gets close to the hulk, she calls
the ship, | and what she says is different from one game to the next. ||| It's one scene
and one short record, | all in your fact sheet. ||"

### 2. The scene

**Screen:** `story.mast`, line 49 highlighted. Then `mission.amd`, the end of the file. Two
blank lines. Type the note, the section line and the scene with three takes. Save. Lint:
clean.

**Say:** "First, the last of the lines that Lecture 11 marked for Class 2. || It reads
every scene in a section called dialogue, | so that's the section I write. ||| A scene is
a record, like everything else. || Speaker is who's talking, and it takes her key. || When
hail means this is a call that comes in to the ship. || And the title is what the call is
about, | which the crew reads before they answer. || Below the fence come the lines she
says, | and each one starts with a percent sign. ||"

### 3. Takes

**Screen:** Highlight the three `%` lines one after another. Then the three rules on the
page.

**Say:** "I wrote three of those lines, | but she won't say all three. || Each one is a
take, | which means one way of saying the same thing. || Every time the scene plays, the
game picks one. ||| So write two or three, | and she stops sounding like a recording. ||
Just keep each take on one line, | however long it gets. ||"

### 4. A second thing to say

**Screen:** Type `@quill` above the three takes. Blank line. Type the second `@quill`
block. Save. Lint: clean.

**Say:** "But what if she has two things to say, one after the other? || Then I write
blocks. || A block starts with an at sign and her key, | with nothing else on that line.
|| So here's her greeting, | and here's her question. ||| The game takes one take from
each block. || The crew reads the first, presses Continue, | and reads the second. ||"

### 5. Nobody calls yet

**Screen:** Lint, clean. Then the Quests section: scroll to Quick Work, the last record.

**Say:** "Lint is clean, and yet if I played this now, nobody would call. || A scene is only
words on a page | until something in the story places the call. || And the thing that
places it lives up here, among my quests. ||"

### 6. The beat

**Screen:** Below Quick Work's description, a blank line, then type DS 1 Calls. Highlight
`Beat`, then `Starts when: reach derelict 500`, then the two `Action:` lines. Save. Lint:
clean.

**Say:** "It's a record with three hashes, | so it stands by itself, outside the arc. ||
The first line of the fence is the word Beat, | alone, the way the word Arc was in Lecture
9. || A beat is a moment in the story. | It isn't a job, and it's not in the Quest Log.
||| Now, when does the moment come? || Until today, after Starts when, | you've written at once,
or revealed. ||
 But that line takes the same words as Done when. || So I write
reach, derelict, five hundred, | and those are the very words that finish Close
Inspection. ||| Then Action, which is what happens when the beat starts. || On the next
line, two spaces and a dash, | and then who calls, the word hails, and the scene's key.
||"

### 7. What lint cannot see

**Screen:** In the beat, delete the `Starts when:` line. Save. Lint: clean. Show the row
on the page. `Ctrl+Z`. Then change `@quill` in the second block to `@Harbormaster Quill`.
Lint: clean. `Ctrl+Z`. Lint: clean.

**Say:** "Lint knows this lecture well, | and the page has its tables. || But two mistakes
get past it, and you'll make both. || If I leave out the Starts when line, lint says
clean, | and the call arrives the moment the game starts. ||| And if I write her name
after the at sign, in place of her key, | lint says clean again. || Now that line isn't
the start of a block, | so it becomes one more take, | and every so often she says it out
loud. ||"

### 8. Play it

**Screen:** Server, Helm and Comms. Comms: the empty list. Helm: fly inside 500 of the
hulk. Comms: the row. Select it: her face, her line. Continue. Close.

**Say:** "Here's Comms before I've flown anywhere, | and nobody is calling. || So in we
go, toward the hulk. || Close Inspection is done, | and there's the call, with her name
and my title. || I open it, and there she is, | with one of my three greetings. || I
press Continue, and she asks her question. || Then Close, and the call is over. ||"

### 9. Back, and again

**Screen:** Start again. Open the call, press Back: the row is in the list again. Open it.
Then a third start: a different opening take.

**Say:** "Two more things to see. || This time I open the call and press Back, | and it
goes back in the list, unanswered. || So Comms can read a call | and save it for when the
captain is ready. ||| And when I start the mission over, | the takes are picked again, |
so she may greet me with a different line. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: give her a second call. || Write a second scene, | and a
second beat that starts at the lifeboat. ||| Next time, the crew gets to answer her. ||"
