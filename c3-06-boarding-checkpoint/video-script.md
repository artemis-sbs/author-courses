# C3-6 video script - Checkpoint: a short boarding quest

> **CHECKED IN THE REAL ENGINE, 2026-10-04, three real consoles (Engineering, Science,
> Helm).** The whole scene ran as in the mock: Chief Okoro, Dr Hale and Mr Pell by name and
> job, both side stories handed out, the reading on Science only, the roll, the hatch at
> three facts, the wake ending, 18 presses, 350 then 650 credits, six `Quest complete`
> lines, every console home as its own station, `mast.runtime.log` empty. SEEN on a
> handheld: the roll line (`Chief Okoro - engineering 4, rolled 5: 9 vs 9, success.`)
> above the room's line, and the cabin's three answers as buttons under the transcript.
> By the cabin the transcript fills a 960-high page. NOT seen: the Tasks app in this
> scene, Crew > Beam up, the sleep ending, and the time it takes people to play.
> One run in two, `sbs run` brought the Helm window up as a second Engineering console
> (a launch race in the tool, not the mission); check the three names before recording.
>
> **Changed since this script was written (library `49ba0d94`, not yet released):** lint now
> names the conditions nobody can meet (`guard-joined`, `guard-names-a-fact`,
> `guard-learned-shape`, `guard-names-a-person`), a `%` line broken in two
> (`line-wrapped`) and an ending's quest that starts `at once`
> (`outcome-accepts-running`); `Learned` with a capital works. Step 10 of the page is
> updated; re-cut the lint scene.
>
> **DECISION WAITING ON THE USER (B80):** this page puts `Return to the ship` in the
> arrival room and the endings only, because one press of it ends the visit for everyone.
> Lecture 2 teaches "a way home in every room".

Target length: 20 minutes. One continuous screen recording with voice-over, cut at scene
boundaries, plus a camera on a sheet of paper for scenes 2, 4 and 9. The companion page is
`lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 5 mission, with a third person on the roster (Mr Pell, Helm, `Roles: quartermaster`). Lint clean |
| Library | sbs_utils `ae376b8b` or later, LegendaryMissions `9968243` or later |
| A copy | `mission.amd` from Lecture 5 saved outside the mission folder |
| Paper | One sheet, ruled into four boxes: three sentences, beat sheet, places, facts table. A pencil. A printout of the finished Scenes section for scene 9 |
| VS Code | `MyMission` folder open, `mission.amd` in one tab. `story.mast` is not opened in this lecture |
| Game | Closed. Started on camera in scene 10: first a server and ONE console (Engineering), then a server and THREE (Engineering, Science, Helm) |
| A watch | In shot for scene 10 |

## Confirm on camera

**Nothing in this lecture has been run in the real game, and no screen has been seen.**

Checked on 2026-10-04 in the mock only, with the packaged library (sbs_utils `ae376b8b`),
by a probe that stood in consoles, moved the ship alongside so the lesson's own quest and
card ran, beamed the party down with the same two calls the BEAM DOWN button makes, pressed
choices by their words, and printed what the game's own functions returned:

1. Three consoles, everything read, wake ending: 20 presses. Both side stories and Account
   for the Crew complete on the readings. `Stand By the Sleepers` starts at the choice and
   completes 30 seconds later. Credits 0, then 100, 350, 650. The ship's log holds six
   `Quest complete:` lines. Run passed, `mast.runtime.log` empty.
2. Three consoles, sleep ending: 20 presses. `Carry Word Home` starts at the choice and
   completes when the ship is put back beside DS 1. Credits 550. The other ending's quest
   stays hidden.
3. Two consoles (Engineering, Science), the three sure facts only: 16 presses. The stores
   are taken by Engineering, marked as covering.
4. One console, at each of the three seats: 16 presses on the sure facts (18 for
   Engineering trying the main cell as well). Each reaches both endings. Account for the
   Crew completes on a covering press. A story whose person stayed behind is handed to
   nobody.
5. Walking away: one press of `Return to the ship` in the airlock ends the visit; no party
   is on offer afterward and a second BEAM DOWN takes nobody.
6. Every row of the lesson's tables: the real `sbs lint` on each mistake, and a second
   script that walked every party (seven of them) through each mistake using the game's own
   choice and answer functions. That second script runs outside a mission, on the working
   tree, which differs from the packaged library in one file that has nothing to do with
   boarding.
7. The lesson's steps were followed literally from the Lecture 5 example file. The result is
   the example, and lint is clean at the end. Between Step 3 and Step 8 lint warns only
   about signals, as the page says.

NOT seen. If one is not as described, stop and fix the page:

8. **The handheld's own way home.** The page says the Crew app can take one person home
   and leave the visit open. That is read from the library's code and its documentation,
   and the call behind the button was measured (the visit stayed open, the others carried
   on, the person came back with BEAM DOWN). The button itself has not been seen. On
   camera: Crew, the ship's row, Beam up.
9. What a console on the bridge shows when an ending starts its quest: is the new quest in
   the quest list, and is there a line in the ship's log?
10. Three real handhelds in one room: the surgeon's reading on Science only, the
    quartermaster's on Helm only.
11. A room with two conditions on its line (the spine): the "cannot answer yet" line before
    three facts, the other after.
12. The last room of an ending: one line and one button.
13. **How long it takes.** 16 to 20 presses is a count, not a time. Time the three-console
    play with the watch and say the number. If it is far from ten minutes, change the
    numbers in Step 2 of the page before publishing.
14. The Tasks app on the surgeon's and the engineer's handhelds, each with its own story.

Known and not taught here: a visit cannot be reopened once the party has returned; a party
may try a check as often as it likes; a person cannot see their own skill numbers; a quest
has one `Then:` line.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** Three consoles side by side in the captain's cabin. Two buttons: Throw the
switch and wake them, Leave them sleeping and go for help. Nobody presses.

**Say:** "Three people, one room, and a decision none of them was ready for. It took them
a dozen choices to get here, and every crew can get here: three of them, or one of them
alone. Today you build this, and you learn how to be sure of that last part before anyone
plays it."

### 2. Three sentences and a beat sheet (0:45 - 3:00)

**Screen:** The sheet of paper. Write the three sentences. Then the beat sheet table from
the companion page, filled in by hand.

**Say:** "No rooms yet. Three sentences. The question: why is this ship drifting? The
answer, which the party will find in pieces: her crew put themselves to sleep to wait for
help. And the choice: wake them, or go and get a doctor. If you cannot write the third
sentence you have a tour, not a scene. Now the beat sheet. It is just how much of
everything. Six places. One reading for each person on my roster, so three. One reading
for a skill. One check. That is five facts. The locked door will ask for three. Two
endings. Keep to these numbers the first time."

### 3. The places (3:00 - 5:30)

**Screen:** The paper: draw the airlock, the spine, and four rooms hanging off the spine.
Then `mission.amd`: select every room under the Scenes heading and delete. Type the five
places. Terminal: `sbs lint MyMission`, two warnings.

**Say:** "One room in the middle, and everything hangs off it. Every room has a way back.
And look where the way home is: in the airlock, and nowhere else yet. In Lecture 2 every
room had one. Here is what I found when I measured it. One press of Return to the ship, by
anybody, ends the visit for everybody, and the place cannot be entered again. In a
ten-minute scene with three people, that is one thumb away from no ending at all. So home
is a walk. Now I delete my practice rooms, all of them, and type five places. Lint. Two
warnings: my old stories are waiting for signals from rooms I just deleted. Lint is right.
I will clear them in a few minutes."

### 4. The facts table and the readings (5:30 - 8:00)

**Screen:** The paper: the facts table, five rows, the last column filled in last. Then
type the four readings and their four short rooms.

**Say:** "Before I type a reading, I list them. What the fact is, where it is, who is
offered it. And one more column, the one that matters: is it sure? A fact is sure when any
party at all can get it. A reading for a job is sure, because when the doctor stays home
somebody covers for her. A reading for a skill is not. Nobody covers for a skill. And a
fact behind a check takes luck. Three sure. Remember that number. Now the readings. Same
shape as Lecture 3. Two of them also send a signal, and that is for later."

### 5. The check (8:00 - 9:15)

**Screen:** Type the check in the engine room and its two rooms.

**Say:** "One check. Anyone may try the main cell. It goes where the party is passing
through anyway, never in front of an ending, and what it teaches is a spare. Both rooms
lead back to the engine room."

### 6. The locked door (9:15 - 11:15)

**Screen:** The spine: type the hatch choice and replace the line with two. Type the
cabin. Then the three-row table of shapes from the companion page.

**Say:** "The captain's hatch opens at three facts. Three, because I have three sure
facts. The number on the door is never more than the sure facts. The other two are spares.
And two lines on the spine, so a party that gets here early is told why the hatch is shut.
Now a warning, because you will want to write more than this. A condition has three
shapes. A job. A skill and a number. How many facts. That is all. There is no `and`. You
cannot ask for one fact by its name. Write any of those and lint says clean, and the
choice is never offered to anyone."

### 7. Two endings (11:15 - 13:15)

**Screen:** The Quests section: type the two hidden quests. The cabin: type the two
choices. Then the two last rooms.

**Say:** "An ending is three things. A quest the ship does not have yet: `Starts when:
revealed`, so it is hidden. A choice that starts it: semicolon, `accepts`, the quest's key.
You used `accepts` on an answer in Class 2, and it works the same here. And a last room,
with one line and one way out, and that way out is home. Do not give a last room a way
back. I tried it. The party took both endings."

### 8. Stories, and a quest any crew can finish (13:15 - 14:45)

**Screen:** Side Stories: delete the two old stories, type the two new ones. Quests:
rewrite Account for the Crew. Zoom on its `Done when:` line. Terminal: lint, clean.

**Say:** "Two stories, the same shape as last time: `For`, a job, and a signal that
person's own reading sends. Now the ship's quest, and one change from Lecture 5. Last time
it waited for the doctor's story. So with the doctor at home, it stayed open for good.
This time it waits for the reading's own signal. The doctor's press finishes both. And if
she is not there, whoever covers for her finishes the ship's quest. Lint. Clean."

### 9. Five checks with a pencil (14:45 - 17:15)

**Screen:** The printout and the pencil. Tick every heading that has an open way out.
Circle each key where a choice names it. Count the sure facts against the door. Cross out
the skill line and the check, and walk a finger from the airlock to each ending. Then the
editor: change the door to 4. Terminal: lint, clean. Back to the paper: check 3 finds it.
Undo.

**Say:** "Lint is clean. Lint has checked my spelling. It has not walked through my rooms,
and it never will. So, five checks. One: every room has a way out with no `if`. Fourteen
headings, fourteen ticks. Two: every room has a way in. Three: the door asks for three, I
have three sure. Four, the important one: I cross out everything that needs a skill or
luck, and I walk it. Airlock, spine, three readings, cabin, ending, home. If the worst
crew can do it, every crew can. Five: each story is finished by its own person's reading,
and each last room has one way out. Now watch. I make the door ask for four. Lint: clean.
But check three: four is more than three. That scene only opens for a lucky party. Lint
could not tell me. The pencil could."

### 10. Play it (17:15 - 19:30)

**Screen:** A server and one Engineering console. Alongside, beam down, and walk the short
way: the covering readings, the hatch, an ending. Cut. A server and three consoles, the
watch in shot: read everything, the other ending. Then the bridge: the new quest. Stop the
watch.

**Say:** "Alone first, as the chief. The doctor's reading comes to me marked as covering.
So does the quartermaster's. Three facts, the hatch, an ending. Sixteen presses. Now all
three, and the watch is running. Each reading goes to its own person. Nothing is marked as
covering. They choose. And on the bridge, the ship has a quest it did not have a minute
ago. Stop the watch."

### 11. Your turn (19:30 - 20:00)

**Screen:** The exercise on the companion page.

**Say:** "Now yours. Three sentences, a beat sheet, the places, the facts table, and only
then the rooms. Do the five checks. Break it three times on purpose and find each one with
the pencil. Then play it, and write down how long it took. Next time, we open up a long
away mission and see how its files fit together."
