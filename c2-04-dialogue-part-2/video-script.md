# C2-4 video script - Dialogue, part 2

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 3 mission: Harbormaster Quill, the scene **Quill Checks In** with two blocks, the beat **DS 1 Calls**. Lint clean. No answers yet |
| Library | sbs_utils v1.4.0 as released on 2026-10-03 or later. It needs that day's fixes: an answer's `accepts` / `completes` / `fails` are known to lint, and a call that could not be placed is written to `mast.runtime.log`. One row of the page's lint table (two hashes on a scene with scenes below it) needs the lint change committed that evening (`e3b2a6a8`); on an older library that row reads `clean` |
| Template | The mission must come from the `amd` template that already reads the Characters and Dialogue sections (build item B53: fixed in the starter repo, not pushed when this was written) |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, scrolled to Quill Checks In |
| Game | Closed. Started on camera in scene 10 with a server, a Helm console and a Comms console |

## Confirm on camera

Checked on 2026-10-03 by a script that called the game's own functions: the function that
builds the rows of the Comms hail list, and the function that list calls when a row is
picked. First in headless runs (the mock), then IN THE REAL ENGINE with a server and one
real Comms console (sbs_utils `27aaa520`): the whole road below, from the first call to
the call back and 250 credits, matched the mock line for line, and `mast.runtime.log` was
empty. One screenshot of the Comms console was taken after the last answer: its message
area reads `Harbormaster Quill - About that hulk - answered (We will tag her.)`. The hail
list itself, with its rows, has not been seen.

What the runs showed:

- Inside 500 of the hulk, one call waits: `Harbormaster Quill - About that hulk`.
- Opened: one take of her first block, rows `Back` and `Continue`. Then one take of her
  second block, and the rows are `Back` and the three answers, in the order they are
  written in the file.
- `What do you know about her?` moves to the second scene: one of its two takes, rows
  `Back` and two answers. `She is cold, DS 1. No power, no lights.` moves to the offer:
  rows `Back`, `We will tag her.`, `Find someone else, DS 1.`
- `We will tag her.` closes the call. Tag the Hulk goes from hidden to running, and DS 1
  Calls goes to complete. The function that fills the Quests tab then lists
  `Tag the Hulk` (running) and `DS 1 Calls` (complete); DS 1 Calls was not listed before.
- 20 seconds later the job is still running. By 36 seconds it is complete, the side's
  credits have gone from 100 to 250, and a second call waits:
  `Harbormaster Quill - Your beacon`. Opened, it has rows `Back` and one answer.
- `Find someone else, DS 1.`: DS 1 Calls completes, no job, no second call.
- `Not now, DS 1. Artemis out.`: nothing changes, and no call comes back.
- `Back` after moving to another scene: the call returns to the waiting list, and opened
  again it shows that scene, not the first one.
- The exercise, followed as written: the quest completes when the answer with
  `; signal told_truth` is picked, and pays its reward.
- Every row of the lint table on the page was produced by making that mistake and running
  `sbs lint`.

Not seen by anyone. If one of these is not as described, stop and fix the page:

1. The answers as rows in the Comms list. The longest is 39 characters
   (`She is cold, DS 1. No power, no lights.`). If it does not fit a row, shorten the
   lesson's answers and add a line about length to Step 1.
2. Where the answers sit beside her face and her line, and what the main screen shows
   while Comms is choosing. The code builds a read-only list of the answers there.
3. The Quests tab after `We will tag her.`: Tag the Hulk running and DS 1 Calls done.
   The page says a finished beat is listed as done; only the function behind the tab has
   said so.
4. Whether the crew gets a notice when a job starts from an answer, and when it completes.
5. The second call arriving about 30 seconds later, and which comes first for the crew:
   the "quest complete" notice or the call.
6. `Back` in the middle of the call, and the call reopening at the scene the crew had
   reached.

Known, and kept out of the lesson on purpose:

- A condition on an answer. Since 2026-10-03 the library answers a few names from the
  first scene on: the answering ship's roles (`if tsn`), `learned`, and `skill <name>`.
  It still cannot read a quest's state or the side's credits, so `if some_name >= 10` is
  never offered and lint is clean. Scene 8 says so and teaches the two things that do
  work. Guard words for quest state are a design question for the user (build item B66);
  when they exist, re-cut scene 8 and Step 7.
- Curly brackets in an answer's words. Fixed 2026-10-03: the words are drawn as typed. In
  the engine, a real Comms console drew a row reading `Call me {Captain}, DS 1.` and the
  log stayed empty.
- A second voice in the same call is shown under the first speaker's name (build item
  B51). Every scene here is Quill's.

## Scenes

### 1. Cold open (0:00 - 0:50)

**Screen:** The Comms console. Quill's call is open on her question. Three answers in the
list. Pick the first. She makes an offer. Pick "We will tag her." The quest list gains a
job.

**Say:** "Last time, she talked and the crew listened. This time they answer. One answer
got us a job. Another would have hung up on her. Every one of those is a single line in
your file, and today you write them."

### 2. Something to say (0:50 - 3:00)

**Screen:** `mission.amd`, Quill Checks In. Below her last take, a blank line, then type
the two answers with empty round brackets. Point at the dash, the square brackets, the
round brackets.

**Say:** "An answer is a line that starts with a dash. Square brackets: the words Comms
reads and picks. Round brackets, straight after, no space: where the conversation goes
next. Empty round brackets mean the call is over. Two rules. An answer is one line. And
answers go at the end, below her last take, because that is when the crew gets them."

### 3. An answer that leads somewhere (3:00 - 5:30)

**Screen:** Put `quill_offer` in the first answer's round brackets. Go to the end of the
file. Type The Offer: heading, fence with `Speaker: quill`, two takes, two answers.

**Say:** "Put a scene's key in the round brackets, and the call goes on there. So I need
that scene. Three hashes, a name, the key I just used. Speaker, her key. Two takes. And
two answers of its own. Notice what is missing: no When, no Title. Nothing places this
scene as a call. The only way in is the answer that names it. And three hashes, like the
first scene. Never four. A scene does not go inside another scene."

### 4. A second way in (5:30 - 7:00)

**Screen:** Add the middle answer to Quill Checks In. Type What DS 1 Knows above The
Offer.

**Say:** "One more answer: the crew asks a question of their own. That goes to a scene
where she tells them what she knows, and from there, on to the offer. Two answers lead to
the same scene. That is fine. One limit: four answers in a scene. A fifth is never
shown."

### 5. An answer that does something (7:00 - 9:45)

**Screen:** Scroll up to the Quests section. Below DS 1 Calls, type Tag the Hulk. Then go
back to The Offer and add `; accepts tag_hulk` to the first answer.

**Say:** "So far an answer moves the conversation. Now one that changes the story. First
the job she is offering. Starts when revealed, so it is hidden. Done when thirty seconds.
A reward. Now the answer. A semicolon. Everything after the semicolon is what the answer
does. Accepts, and the key of the quest. The key, not the name. When Comms says we will
tag her, the job starts."

### 6. Two things, four words (9:45 - 11:45)

**Screen:** Change the two answers in The Offer to the final form. Then show the table of
four words on the companion page.

**Say:** "An answer can do two things. One semicolon, then a comma between the things.
Not a second semicolon: that looks right and does nothing. The second thing here finishes
the beat from last time, DS 1 Calls. She has been answered, so that moment is over, and a
finished beat shows up in the quest list as done. There are four words. Accepts starts a
quest. Completes finishes one. Fails fails one. Signal sends a word into the story, and
any quest waiting on that word hears it."

### 7. A call that comes back (11:45 - 13:45)

**Screen:** Add `Then: reveal beacon_set` to Tag the Hulk. Type the Beacon Set beat below
it. At the end of the file, type Quill Calls Back.

**Say:** "What the crew said should come back to them. When the job is done: then, reveal
beacon_set. A beat, the same pattern as last time: starts when revealed, and its action
places a call. And the scene. This one is a call of its own, so it has When hail and a
Title again."

### 8. Answers that depend on the story (13:45 - 15:00)

**Screen:** Highlight "We will tag her." Then highlight "Glad to help". Then show the
`if` line from Step 7 of the companion page.

**Say:** "Look at what you have. This answer is only offered to a crew that reported the
hulk was cold. This one is only offered to a crew that took the job and finished it. That
is how you make an answer depend on the story: put it somewhere the crew can only reach
when it is true. You will see another way in the documentation, the word if on the
answer. Do not use it in this mission. It cannot read your quests or your credits, so
the answer is never offered, and lint will not warn you. It comes into its own in Class 3."

### 9. Lint (15:00 - 16:45)

**Screen:** Terminal: `sbs lint MyMission`, clean. Misspell `quill_offer` in an answer,
lint, show the warning, undo. Type `acepts`, lint, show the warning, undo. Misspell the
quest key after `accepts`, lint: no quest has that key. Undo. Delete the round brackets
from the hang-up answer, lint: it looks like an answer and is read as a spoken line. Undo.
Put a fourth hash on The Offer, lint: the scene above it disappears. Undo.

**Say:** "Lint. Clean. A scene key that is not there. A word that is not one of the four.
A quest key that is not there: the answer would end the call and start nothing. No round
brackets: that line is no longer an answer. It is one more thing for her to say, and one
day she would say it, brackets and all. And a scene with one hash too many, which takes
the scene above it out of the game. Lint reads every one of these. What it cannot read is
your intention: a job with no way to finish still lints clean."

### 10. Play it (16:45 - 19:15)

**Screen:** Server, Helm and Comms. Fly inside 500. Open the call. Continue. Choose "What
do you know about her?", then "She is cold, DS 1.", then "We will tag her." Show the
quest list. Wait for the job to complete. Open the second call and answer. Then restart,
and this time choose "Find someone else, DS 1." and wait: no second call.

**Say:** "Her question, and my three answers. I ask first. Then I tell her. The offer.
We will tag her. Call over, and there is the job. Thirty seconds. Done, paid, and she is
calling back. Now the other road. Find someone else. No job. And she does not call. Same
file, two different evenings."

### 11. Your turn (19:15 - 19:50)

**Screen:** The exercise on the companion page.

**Say:** "You wrote a second call last time. Give it answers, and make one of them send a
word into the story that finishes a quest. Next time: a job the crew can only get by
picking up the call."
