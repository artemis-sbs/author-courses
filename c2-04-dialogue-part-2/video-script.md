# C2-4 video script - Dialogue, part 2

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **The student's mission is `MyMission`** as Lecture 3 of this class left it
>   (`c2-03-dialogue-part-1\example\mission.amd`, with Lecture 1's `story.mast`). The game
>   is started with `sbs run server,helm,comms -m MyMission map=0`.
> - **`example\` holds the one file that differs from that start:** `mission.amd`.
> - **What changed from the first version.** The lecture teaches the same things. The
>   file is the chained one: the beat DS 1 Calls starts on its own trigger (Lecture 3), so
>   Tag the Hulk is typed below that beat, as a record of its own beside the arc Salvage
>   Run. Three of the page's steps now show the warning lint prints half way through
>   them, because lint has learned to say what is still missing: `dangling-choice`,
>   `never-revealed`, then `dangling-reveal` and `dangling-action-ref`. The mistake tables
>   have a third column, lint's code, and most rows that were silent in the first version
>   have one now.

> **Re-measured 2026-10-08, in the mock.** Tool as installed in `data\missions`, library
> as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were applied one at a
> time to the Lecture 3 example, with lint after each and after each half step. Then
> one-change variants of the finished file: each linted, each played headless by a probe
> that reads the rows the Comms hail list would show, picks rows by their first words,
> and prints every quest's state, the side's credits and the calls waiting. Every line of
> tool output in a code block on the page is a line a run printed (`verify_page.py`).

> **CHECKED IN THE REAL ENGINE, 2026-10-04, with a real Comms console, on the first
> version:** the whole conversation, the job taken, the call back, and 250 credits in all
> (100 for Close Inspection, 150 for the beacon; that file had no bonus step). The four
> scenes and the two quest records have not changed since, but for one sentence that now
> names the Breakers. The hail list itself was not seen.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 3 leaves it. `mission.amd` has 283 lines and ends with Quill's take "So. Is anybody home?". The beat DS 1 Calls is the last record of the Quests section |
| Lint | `sbs lint MyMission` says `clean` |
| VS Code | `MyMission` folder open, `mission.amd` in one tab scrolled to the end |
| Command prompt | Open in `data\missions`, cleared, wide enough that a finding fits on three lines |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless play with the packaged library.
"Engine" is the run of 2026-10-04 in the note above. If an item fails while recording,
stop and fix the page.

1. Lint after each step is `clean`. Half way through Step 2 it prints the
   `dangling-choice` line on the page, with `line 285:39`. Half way through Step 4 it
   prints the `never-revealed` line, with `line 138`. In Step 6 it says `dangling-reveal`,
   then `dangling-action-ref`, then `clean`. (Lint.)
2. On the finished file, the road through the question: the rows are Back and the three
   answers; then Back and two answers; then Back and the two answers of The Offer. "We
   will tag her." ends the call, Tag the Hulk is running, and DS 1 Calls is complete.
   (Mock, Engine.)
3. About 30 seconds later Tag the Hulk is complete, the side has 150 credits more, and
   one call waits: `Harbormaster Quill - Your beacon`. Its one answer ends it. (Mock,
   Engine.)
4. "Find someone else, DS 1.": no job, and 36 seconds later no second call. "Not now, DS
   1. Artemis out.": the call is gone and does not come back. (Mock.)
5. **Back** in the middle: the call returns to the list; opened again it is at the scene
   the crew had reached. (Mock.)
6. The job taken and the story played to its win: 650 credits. (Mock.)
7. Every row of the five tables in Step 8. (Lint for all, Mock for all.)
8. The exercise: an answer with `; signal told_truth` completes a quest that says
   `Done when: signal told_truth`, and lint is `clean`. (Lint, Mock.)

Not seen by anyone, and to watch for while recording:

1. The answers in the list on a real Comms console: how a long answer is drawn, and
   where Back sits.
2. Where the crew reads that a job has started.
3. A fifth answer: the page says it is never offered. The mock agrees. Nobody has looked.
4. Quill saying a broken answer line out loud, brackets and all.

## Scenes

### 1. Cold open

**Screen:** The Comms console. Quill's call open, three answers in the list. One is
picked. The Quest Log gains Tag the Hulk.

**Say:** "Last time, the harbormaster called, | and all the crew could do was listen. ||
Today they get to answer. || One answer asks her for more, | one takes a job, | and one hangs up.
||| And the answer they give changes the story. ||"

### 2. An answer

**Screen:** `mission.amd`, the scene Quill Checks In. Below her last take, a blank line,
then type the two answers. Highlight the dash, the square brackets, the round brackets.
Save. Lint: clean.

**Say:** "An answer is one line, | and you already know its shape. || It's a dash and a
space, | then the words in square brackets, | then round brackets, with no space between.
|| It's a heading's name and key, | with a dash where the hashes go. ||| The square
brackets hold what Comms reads and picks. || The round brackets say where the conversation
goes next, | and when they're empty, the call is over. ||"

### 3. An answer that leads somewhere

**Screen:** Type `quill_offer` in the first answer's round brackets. Save. Lint: the
`dangling-choice` warning. Then, at the end of the file, type The Offer. Save. Lint:
clean.

**Say:** "Now I put a key in those round brackets, | the key of a scene I haven't written
yet. || And lint tells me so: | this answer points at something that isn't there. ||| So I
write it, at the end of the file. || It's a scene like the first one, with three hashes, |
but it has no When line and no title. || Nothing in the story places it as a call. || The
only way in is the answer that names it. ||"

### 4. A second way in

**Screen:** Add the middle answer to Quill Checks In. Type What DS 1 Knows above The
Offer. Highlight the two answers that both lead to `quill_offer`.

**Say:** "A conversation can branch, and it can come back together. || I add an answer
that asks her what she knows, | and I write the scene for it. || And from there, one
answer leads on to the same offer. ||| So a crew that asks first hears a little more, |
and ends up in the same place. || Just don't write more than four answers in a scene, |
because a fifth is never offered. ||"

### 5. The job

**Screen:** The Quests section. Below DS 1 Calls, type Tag the Hulk. Save. Lint: the
`never-revealed` warning; highlight the words "and no answer". Then The Offer: add
`; accepts tag_hulk`. Save. Lint: clean.

**Say:** "So far an answer moves the conversation, | or it ends it. || Now one is going to
change the story. || First I need the job she's offering, | so I write it up here among my
quests. || It starts when revealed, | which keeps it hidden until something starts it.
||| Lint warns me that nothing does, | and look what it lists: | a Then line, or an
answer. || So lint already knows where this is going. || I go back to the offer, | and
after the round brackets I type a semicolon, | then accepts, and the job's key. ||
Everything after that semicolon is what the answer does. ||"

### 6. Two things at once

**Screen:** Change the two answers of The Offer to the lines with `completes ds1_calls`.
Then the table of four words on the page.

**Say:** "An answer can do two things, | with one semicolon, and a comma between them. ||
Whichever way the crew answers, they've answered her, | so I mark that moment done as
well. ||| There are four words you can write after the semicolon. || Accepts starts a
job, | completes finishes one and pays it, | fails does what it says, | and signal sends a
word into the story. ||"

### 7. The call that comes back

**Screen:** Tag the Hulk: add `Then: reveal beacon_set`. Lint: `dangling-reveal`. Type the
beat Beacon Set. Lint: `dangling-action-ref`. Type Quill Calls Back at the end of the
file. Lint: clean.

**Say:** "What the crew said can come back to them later. || When the beacon is set, I
want her to call again, | and that takes three pieces. || Watch lint walk me from each one
to the next. ||| First, a Then line on the job, | and lint says it reveals something that
isn't there. || So I write that, a beat like last time's, | and lint says the beat calls a
scene that isn't there. || So I write the scene, and now it's clean. ||| And here's the
point of it. || Only a crew that took the job, and finished it, | ever hears this call.
||"

### 8. If, and why not yet

**Screen:** The table in Step 7 of the page. Then the line with `if some_name >= 10`.

**Say:** "So that's two ways to make an answer depend on the story. || You put it in a
scene that only one answer leads to, | or in a call that only comes later. ||| You'll see
a third way in other pages, | a condition written on the answer itself. || Don't use it in
this mission. || It can't read your quests or your credits, | so the answer would never be
offered, | and lint can't tell. || We'll use it properly in Class 3. ||"

### 9. Play it

**Screen:** Server, Helm and Comms. Fly inside 500 of the hulk. Open the call, Continue.
Three answers. Pick What do you know. Pick She is cold. Pick We will tag her. The Quest
Log: Tag the Hulk. Wait. The second call. Answer it.

**Say:** "In we go, and here's her call. || She asks her question, | and now there are
three answers in the list. || I'll ask what she knows first, | then I tell her the hulk is
cold, | and there's the offer. ||| We will tag her. || The call is over, | and the job is
in the Quest Log. || Thirty seconds later it's done and paid, | and she's calling back.
||"

### 10. The other roads

**Screen:** Start again: pick Find someone else. Wait: nothing. Start again: pick Not now.
Then once more: open the call and press Back.

**Say:** "Now the other roads. || If I tell her to find someone else, | there's no job,
and no second call. || And if I say not now, | the call is gone, and it doesn't come back.
||| But Back is a different thing. || It puts the call back in the list, unanswered,
 | and nothing in
the story changes. || So the crew always has a way to wait. || Only write an answer that
hangs up | when your story can go on without the call. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: give your second call some answers. || Make one of them send
a word into the story, | and write a quest that waits for that word. ||| Next time, a step
the crew can only finish by reporting in. ||"
