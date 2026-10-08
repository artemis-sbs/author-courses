# C2-5 video script - Hails

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **The student's mission is `MyMission`** as Lecture 4 of this class left it
>   (`c2-04-dialogue-part-2\example\mission.amd`, with Lecture 1's `story.mast`). The game
>   is started with `sbs run server,helm,comms -m MyMission map=0`.
> - **`example\` holds the one file that differs from that start:** `mission.amd`.
> - **What changed from the first version.** The lecture teaches the same things on the
>   chained file. Chief Ives is no longer typed here: he has been in the Characters
>   section since Lecture 2, with a face that stays. The exercise is new: it works on the
>   lesson's own calls. The first version's exercise turned a beat into a step the crew
>   can see by taking out its `Beat` line. In the chained file that beat starts on a
>   trigger (`Starts when: reach lifeboat 500`), and the same line on an ordinary quest
>   starts nothing: the quest sits on offer for good, and no call is placed (measured;
>   reported). Lint's only word for it is `quest-never-finishes`.


> **Re-measured 2026-10-08, in the mock.** Tool as installed in `data\missions`, library
> as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were applied one at a
> time to the Lecture 4 example, with lint after each. Then one-change variants of the
> finished file: each linted, each played headless by a probe that takes the job, waits
> for the beacon, reads the rows the Comms hail list would show, picks rows by their
> first words, and prints every quest's state, the side's credits, the calls waiting, the
> list the Quest Log is filled from, the kept calls and the ship's log. Two-ship runs set
> the number of player ships to two. Every line of tool output in a code block on the
> page is a line a run printed (`verify_page.py`).

> **CHECKED IN THE REAL ENGINE, 2026-10-04, a real Comms console and a main screen, on
> the first version.** The lesson's walk matched the mock line for line: the call on the
> list, Quill then Chief Ives by name, the report finishing the step, the credits,
> `mast.runtime.log` empty. SEEN on Comms: Chief Ives's face and name, the title "Your
> beacon", the dial and the Audio box, the two answers. NOT seen: the Hails tab of the
> info panel, the Quest Log's row, anything with two ships. Seen since, in other
> lectures' checks: `At start: posting` shows the Available Quests tile and its row says
> how it is taken; `Presentation: orbit` with `Subject: derelict` films the hulk on the
> main screen.
>
> **Still true, and a decision for the course owner:** `Scope: ship` does nothing in a
> template mission, because the template grants every quest to the shared story.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 4 leaves it: Quill's call with answers, the job **Tag the Hulk** taken by "We will tag her.", the beat **Beacon Set** and the scene **Quill Calls Back**. `mission.amd` has 338 lines |
| Lint | `sbs lint MyMission` says `clean` |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, scrolled to Tag the Hulk |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console. Scene 6 is a table on the page; a second start with two player ships is optional |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless play with the packaged library.
"Engine" is the run of 2026-10-04 in the note above. If an item fails while recording,
stop and fix the page.

1. Lint is `clean` after each of Steps 1 to 4. Half way through Step 1, with Tag the Hulk
   changed and the beat not yet replaced, it says `dangling-reveal` and `never-revealed`.
   (Lint.)
2. After "We will tag her.": Tag the Hulk is running. About 30 seconds later it is
   complete, Report to DS 1 is running, nothing has been paid for the beacon, and one call
   waits: `Harbormaster Quill - Your beacon`. (Mock, Engine.)
3. The list the Quest Log is filled from has Report to DS 1 as active at that moment.
   With the `Beat` line left in, it does not. (Mock.)
4. Opened, the call shows one of Quill's two takes with rows `Back` and `Continue`. After
   Continue the list's heading and the speaker are `Chief Ives`, with a face, and the rows
   are `Back` and the one answer. (Mock, Engine.)
5. `Back` on Ives's block puts the call back in the list and leaves the step running.
   Opened again it starts at Quill's block. A minute unanswered: the call is still
   waiting. (Mock.)
6. The answer closes the call. Report to DS 1 is complete and the side has 150 credits
   more. The ship's log gets the line on the page. The record of finished calls holds
   both conversations. (Mock, Engine.)
7. Two calls waiting: the newer one is first. With `Priority: 5` on the older one, the
   older one is first. (Mock.)
8. The dial: `off`, `console`, `main` and `both` are accepted. It starts at `both`.
   (Mock. Engine: the dial was seen.)
9. Two player ships: both get each call. One ship's yes starts the job for both. Both get
   the report call; the first report pays 150 and the second pays nothing. A yes from the
   second ship after the job was finished changes nothing. (Mock.)
10. Every row of the three tables in Step 7. (Lint for all, Mock for all.)
11. The exercise: an `@ives` block between Quill's two blocks and an `@sable` block in
    The Offer; lint is `clean`, and the name changes twice in the call. (Lint, Mock.)

Not seen by anyone, and to watch for while recording:

1. The Hails tab of the info panel, and reading a finished call again.
2. The Quest Log's row for Report to DS 1 while the call waits.
3. The call on the main screen, and what the dial does to it.
4. Anything with two ships.
5. Where the ship's log is read on a console.

## Scenes

### 1. Cold open

**Screen:** The Quest Log: Report to DS 1, running. Comms: Harbormaster Quill - Your
beacon in the list. It opens on Quill, then Chief Ives. One answer. The credits tick up.

**Say:** "Last time, the job paid by itself, | and the call afterward was just manners. ||
Today the job isn't over until the crew reports in. || And when they do, | a second voice
comes on the line. ||| Along the way you'll learn which call sits on top, | which ships
get called, | and what Comms can do with a call that's waiting. ||"

### 2. A step only an answer can finish

**Screen:** Tag the Hulk: delete the `Reward:` line, change `Then:` to
`reveal report_in`, add the sentence. Then select the whole beat Beacon Set and type
Report to DS 1 over it. Highlight: no `Beat`, `Objective:`, `Reward:`, `Action:`, and the
missing `Done when:`. Save. Lint: clean.

**Say:** "I start with the job. || I take its reward off, | and I point its Then line at
a new key. || Then I replace the beat below it with a quest. ||| Look at what's different.
|| There's no Beat line, so the crew will see it in the Quest Log. || There's an
objective, which sends them to Comms. || The reward has moved here. || The Action lines
are the same two as before, | because Action works on any quest. ||| And look at what's
missing: there's no Done when. || Nothing in the game finishes this step by itself. ||"

### 3. The answer that finishes it

**Screen:** The scene Quill Calls Back: change the two takes, and the answer to
`; completes report_in`. Save. Lint: clean.

**Say:** "So what does finish it? | An answer from the crew does. || Quill
 should be asking now, not
congratulating, | so I change her lines. ||
 And on the crew's answer, after the semicolon,
| I write completes, and the step's key. ||| Now here's the rule for a call that a step is
waiting on. || Every answer that ends the call has to finish the step. || If I add an
answer that just hangs up, | the call is gone, and the step stays in the Quest Log for
good. || And lint can't see that. ||"

### 4. A second voice

**Screen:** In Quill Calls Back, type `@quill` above her takes, then the `@ives` block.
Scroll up to show Chief Ives in the Characters section. Save. Lint: clean.

**Say:** "A call can have more than one person on the line. || Chief Ives has been in my
cast since Lecture 2, | with nothing to say. || So I give him a block: | an at sign, his
key, and two takes of his own. ||| The call still belongs to Quill, | and it's her name on
the list. || But when Comms presses Continue, | the name and the face change to his. ||
Remember that the line is an at sign and a key, and nothing else. || Write his full name
there, and his block is gone, | and lint says clean. ||"

### 5. Which call is on top

**Screen:** The table in Step 4 of the page. Then add `Priority: 5` to Quill Calls Back.
Save. Lint: clean.

**Say:** "Calls wait in a list, and the newest one is on top. || So a call that matters
can get pushed down by a later one. || A call never times out, | and only one is open at
a time. ||| To keep a call on top, I give its scene a priority. || A higher number sits
above a lower one, | and a call with no priority counts as zero. || Use it for a call that
a step is waiting on, | and leave the others alone. ||"

### 6. Who gets called

**Screen:** The table in Step 5 of the page, row by row.

**Say:** "I've never said which ship she calls, | and I don't have to, | because every
player ship is called. || With one ship, that's all there is to it. ||| With two, each
ship gets its own copy of the call. || But the job is shared, so there's only one of it.
|| One crew says yes, and it starts for everybody. || And the first crew to report gets
the side paid, just once. ||| So write your lines for any ship that might hear them, | and
keep jobs like this for missions flown by one ship. ||"

### 7. What Comms can do

**Screen:** The table in Step 6 of the page.

**Say:** "This part has nothing to type. || It's what the person at Comms can do with what
you wrote. || They can leave a call waiting, | they can open it, | and they can press
Back. || There's a dial that chooses where the conversation is drawn. || And every
finished call is kept, | so it can be read again. ||| So an answer is a decision the crew
makes once. || Everything else lets them put it off, or look back at it. ||"

### 8. What lint cannot see

**Screen:** Take `; completes report_in` off the answer. Save. Lint: clean. Put it back.
Then type `Beat` back into Report to DS 1. Lint: clean. Take it out. Show the table on
the page.

**Say:** "Lint names ten mistakes in this lecture, | and the page lists them. || These two
it can't see. || If I take the completes off the answer, lint says clean, | and the step
can never be finished. ||| And if I leave the Beat line in, lint says clean again. || The
step still works and pays, | but the crew is never told to report. || So check both of
those with your own eyes. ||"

### 9. Play it

**Screen:** Server, Helm and Comms. The hulk, the first call, We will tag her. The Quest
Log: Tag the Hulk. Wait. Report to DS 1 appears; the new call. Open it: Quill. Continue:
Ives. Back. Open again. Continue. The answer. The credits. The ship's log line.

**Say:** "Let's play it through. || I take the job, the way we did last time. || Thirty
seconds later the beacon is set, | and there's my new step, telling me to report. || And
there's the call. ||| It opens on Quill, | and when I press Continue, that's Chief Ives.
|| I press Back, and the call waits, and so does the step. || I open it again, and this
time I give the answer. || The step is done, and now the job has paid. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: put more voices on your calls. || Give Ives a block in the
first call, | and let Captain Sable listen in on the offer. || Then break the report on
purpose, and watch what lint doesn't say. ||| Next time, a side that remembers what the
crew did. ||"
