# C3-16 video script - Capstone: a long boarding mission

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **The capstone is the student's own mission.** This lecture is a method and one
>   finished example, **Corvin's Claim**, made as a second mission:
>   `sbs create MyClaim -t away --title "Corvin's Claim"`. `example\` holds the whole
>   finished mission: the starter's files, with `mission.amd` rewritten, three maps in
>   place of `landing.tiles`, and two words changed on the card in `story.mast`.
> - **It does not depend on Lecture 15.** One sentence under "Before you start" says a
>   boarded ship can be one more place: a party of its own, not an area.
> - **`sbs create` and `sbs fetch` were not run** to write this. The start files are
>   Lecture 7's starter with `description.yaml` retitled the way `sbs create` does it.
> - **CORRECTED 2026-10-15: a shot never removes a prop.** The library released after this
>   page was measured (sbs_utils a2d63d66) leaves every prop where it was, and opens only a
>   prop whose `Opens with:` lists `cut`. Scene 6 and Step 8 were rewritten from the
>   library's documentation. Not re-played.
> - **PLAYED IN THE ENGINE 2026-10-16** (Artemis Cosmos 1.3.15, sbs_utils 7ea2c918), two
>   games: Science and Engineering to the dig, and Science alone to the blast. What it
>   showed that this page did not say: the coupling is had by stopping the ore hauler, one
>   FULL shot from the works gate (outside its Notice of 3, inside the shot's range of 6);
>   a shot at the lift gate leaves no note anywhere; the lift house is in fog from the
>   works gate; the arc's time stands where its state would. What a clock reads depends on how long
>   the crew took, so the page never quotes one.

> **Measured 2026-10-10, in the mock**, on the packaged library (sbs_utils `ae05dac7`),
> with stand-in consoles driven by a script. Walked end to end on the finished files:
> the dig ending with three consoles (44 seconds of walking and waiting, 18 presses,
> split 9, 2 and 7); the blast ending with the helm officer alone (33 seconds, 12
> presses); the shaped charge with the guard, put at the fall by the probe with the
> charges in his pack. On a copy with the clock at 40 seconds: a FULL shot at the lift
> gate and at the rock fall, then the loss when the time ran out. Fourteen one-change
> mistakes linted; none of them played.
> **Captured from the apps' draw functions:** the ship's quest rows before and after Ada
> Corvin's answer, after the lift, and at the rock fall; the Tasks app; the pack.
> **Seen in an earlier draft and not kept as a capture:** with the two endings written
> as quests outside the arc, the arc finished when its two steps did and the clock
> stopped; and a step that started `at once` put its lead on the Tasks app before
> anybody had spoken to Ada.
> **Guesses, said as guesses:** every time in minutes.

The companion page is `lesson.md`; the finished mission is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | A folder `MyClaim` holding the files in `example\`. Lint clean |
| VS Code | `MyClaim` open; `mission.amd` at the Quests section and at The Rock Fall; `ground\works.tiles` in Text view; `story.mast` at the card |
| Paper | Two sheets on camera: the beat sheet, and the twelve checks with mine filled in |
| Game | Closed. Started on camera in scene 7 with a server, Science and Engineering (Dr Hale and Chief Okoro) |

## Confirm on camera

1. `sbs lint MyClaim` says `clean`. (Lint.)
2. Before anybody talks to Ada Corvin the ship's quest list has one line. After her
   first answer it has the arc and its first step. (Mock, captured.)
3. When the lift runs, the first step is `Done` and the second appears, with a time
   under the arc. At the rock fall both are `Done` and the time is still there. (Mock,
   captured.)
4. Three consoles reach the dig ending and read its `Win:` sentence. (Mock.)
5. One console, the helm officer, reaches the blast ending. She is refused at the
   ventilator and is not offered `Set his leg`. (Mock.)
6. The guard is offered `Shape them to spare the roof`, and it ends with the first
   `Win:` sentence. (Mock.)
7. A FULL shot leaves the lift gate shut and the rock fall standing; it opens the stores
   door, which lists `cut`. (Library documentation; not re-played.)

Seen in the engine on 2026-10-16: the maps drawn, the quest list changing on a console
beamed back up, the arc's description with its table and hourglass line, both endings,
and the hauler stopped by one FULL shot from the works gate.

Not seen by anyone. If one is not as described, stop and fix the page:

1. Any real crew's time, played by people who did not write it.
2. A shot at the stores door opening it (only the lift gate was shot).

## Scenes

### 1. Cold open

**Screen:** The three maps of Corvin's Claim side by side. Then the bridge's quest list
with a time counting down. Then the two last screens, one after the other.

**Say:** "This is the last lecture of the class, | and it teaches no new word. ||| You're
going to write your own long away mission. || Three areas, a quest tree, and two
endings. | Three jobs, each with something only that person can do. ||| I'll show you
mine, start to finish. | It's small on purpose, so you can read all of it. ||| Then you
write yours. ||"

### 2. Three sentences and a beat sheet

**Screen:** A sheet of paper: the three sentences. Then the beat sheet, five rows with
minutes.

**Say:** "Start on paper, with the same three sentences as the sixth lecture. || The question, and the answer found in pieces. | And the choice at the end. ||| Mine is a mine.
| Four diggers behind a rock fall. || Dig them out and keep the mine, | or blast them out
and lose it. ||| Then the beat sheet from last time. || A landing, three tracks, a join, |
a last area, and an ending. | With minutes beside each one. ||"

### 3. Three areas

**Screen:** The game first: the Lift House area on the Engineering console's map, Chief
Okoro at the works gate and the ore hauler in the yard; the house itself not drawn yet.
Then the drawing: camp, works, gallery, and what joins them. Then `works.tiles` in Text
view. Highlight `known: no`, then the marks.

**Say:** "Here's my middle area on the engineer's console, | the chief at the gate, and
the ore hauler in the yard. || The lift house itself is still in fog. ||| In the files, three areas, and one decision each. || The camp is where
they land. || The lift
house has to be found once. | After that the ship can put you there. || And the gallery
can't be beamed into at all. | That's what makes the lift matter. ||| Look at the map
with last week's eyes. || Every mark is the name of a place. | Nothing hidden stands on a
mark. || And the titles read well after the words go to. ||"

### 4. Three people nobody can replace

**Screen:** The three columns. Then the game: Jo Reth's scene on the Science console's
handheld, with Set his leg. Then the three lines: `if skill medical >= 3`, `Needs:
engineering`, `if skill security >= 3`. Then the table of three roads.

**Say:** "Draw three columns before you write a single prop. | Who's doing what, in each
beat? ||| Then the hard part of the brief. | Each job gets one thing nobody else can do.
|| Here's one, on the doctor's handheld. | Only someone that good is offered Set his leg.
||| There are two ways to write that. | A skill on an answer, or needs on a prop. || It can't be a job, | because a job is covered by whoever's in the scene. ||| And here's the rule that keeps it
fair. || A thing only one person can do | must never be the only road. ||| So the cheap
ending is open to anybody. || The good ending has two doors, | and each one needs
somebody. ||"

### 5. The quest tree

**Screen:** The game first: the bridge's quest list after the lift, a time under the arc.
Then the Quests section: the arc and its four steps. Then the bridge's quest list at three
moments: before Ada's answer, after it, and after the lift. Then the arc selected, its
description shown: the table and the hourglass line.

**Say:** "Now the quest tree. | Remember what the bridge gets: the shared quests, and
nothing else. || So this tree is the story the bridge follows. ||| One arc, with the clock
on it. || The arc waits, and the first answer on the ground starts it. | So nobody loses
time choosing a console. ||| Each step is news for the ship. || And the two endings are
the last two steps, | each with its own winning sentence. ||| I got this wrong the first
time. | I had the endings outside the arc. || The arc finished early, and the clock
stopped with it. | Keep the endings inside, and waiting. ||| And the arc's description is
the bridge's briefing. || Nobody aboard hears Ada Corvin, | so the arc says what she said.
|| Who's where, in a table, | and the air she counted, on an hourglass line. ||"

### 6. Two endings, and a full shot

**Screen:** The game first: the rock fall on the engineer's handheld, with the party's
four facts. Then The Rock Fall's room, then Four Charges. Then the game: after a FULL shot
at the lift gate, the gate still shut, and Look's last line still the pickup before the
shot. Then Step 8's table.

**Say:** "Both endings live in one room. || Here's the rock fall on the engineer's
handheld, | once the party knows all four things. ||| In the file, a choice has one
condition, | so a thing that needs two takes two rooms. | Facts in the first, and the
jacks in the second. ||| Now something to plan for. || A shot never removes a prop. ||
Shoot the lift gate, and it stays shut, | because only the lift's own signal opens it. ||
And nothing on the handheld mentions the shot. | Look still shows the last thing picked
up. || Shoot the rock fall, and both endings are still there. ||| A door opens to a shot | only
when its Opens with line says cut. || So ask one question of your own mission. | Which
doors should the crew be able to force? ||"

### 7. Twelve checks, and the walk

**Screen:** The sheet of twelve checks, mine filled in. Then the game with two
consoles, Science and Engineering: the gallery, then the engineer at the works gate with
the ore hauler in the yard, then the dig ending. Then one console alone: the blast ending.

**Say:** "Lint reads your spelling. | It doesn't walk your map. || So here are the
checks of the whole class, on one sheet. | Twelve of them, in order. ||| Ways in and ways
out. | Keys and names that join. | Signals with two ends. || Then the worst party, and the three columns. | The screen, a full shot, and the clock. ||| Then walk it, every road. || On the way,
somebody has to stop the hauler for its coupling. | Stand on the works gate, outside its
notice, and fire one full shot. || Click the cell it has just stepped onto, | as it walks
up the west side of its square. || Shots miss a lot, | and no app tells you a shot hit or
missed. ||| A doctor and an engineer dig them out. || One person alone, using no skill at
all, blasts them out. ||| The times
on the page are floors from a script. | Walk yours with people, and write down what you
get. ||"

### 8. The rubric, and your turn

**Screen:** The rubric, ten lines. Then a blank sheet of paper, and a pencil.

**Say:** "Here's the rubric, in ten lines, | and each one has a way to know. ||| Three
areas. A quest tree. Two endings and a way to lose. || Three jobs nobody can replace. | A
clock that starts on the ground. || An ending for the smallest party. | And work for
three at once. ||| You're done when every line is ticked, | and when somebody who didn't
write it | has played it to an ending without asking you anything. ||| That's the end of Boarding Parties. | Now go and write yours. ||"
