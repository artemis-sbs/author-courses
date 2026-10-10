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
>   drawn deck can stand in for an area.
> - **`sbs create` and `sbs fetch` were not run** to write this. The start files are
>   Lecture 7's starter with `description.yaml` retitled the way `sbs create` does it.
> - **A FULL shot destroys any prop** in the released game, and the game says nothing.
>   Scene 6 says so plainly. Do not soften it.

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
| Game | Closed. Started on camera in scene 7 with a server, Science, Weapons and Engineering |

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
7. A FULL shot removes the lift gate, and the party can walk through. A FULL shot
   removes the rock fall, and the game then ends by the clock. (Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. Any of the three maps drawn, and whether `prop:rubble`, `prop:crate_ammo`,
   `prop:generator` and `prop:machine_part` look like what the records say they are.
2. The quest list changing on a console left aboard.
3. Any real crew's time.

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

**Screen:** The drawing: camp, works, gallery, and what joins them. Then `works.tiles`
in Text view. Highlight `known: no`, then the marks.

**Say:** "Three areas, and one decision each. || The camp is where they land. || The lift
house has to be found once. | After that the ship can put you there. || And the gallery
can't be beamed into at all. | That's what makes the lift matter. ||| Look at the map
with last week's eyes. || Every mark is the name of a place. | Nothing hidden stands on a
mark. || And the titles read well after the words go to. ||"

### 4. Three people nobody can replace

**Screen:** The three columns. Then the three lines: `if skill medical >= 3`, `Needs:
engineering`, `if skill security >= 3`. Then the table of three roads.

**Say:** "Draw three columns before you write a single prop. | Who's doing what, in each
beat? ||| Then the hard part of the brief. | Each job gets one thing nobody else can do.
|| There are two ways to write that. | A skill on an answer, or needs on a prop. || It can't be a job, | because a job is covered by whoever's in the scene. ||| And here's the rule that keeps it
fair. || A thing only one person can do | must never be the only road. ||| So the cheap
ending is open to anybody. || The good ending has two doors, | and each one needs
somebody. ||"

### 5. The quest tree

**Screen:** The Quests section: the arc and its four steps. Then the bridge's quest list
at three moments: before Ada's answer, after it, and after the lift.

**Say:** "Now the quest tree. | Remember what the bridge gets: the shared quests, and
nothing else. || So this tree is the story the bridge follows. ||| One arc, with the clock
on it. || The arc waits, and the first answer on the ground starts it. | So nobody loses
time choosing a console. ||| Each step is news for the ship. || And the two endings are
the last two steps, | each with its own winning sentence. ||| I got this wrong the first
time. | I had the endings outside the arc. || The arc finished early, and the clock
stopped with it. | Keep the endings inside, and waiting. ||"

### 6. Two endings, and a full shot

**Screen:** The Rock Fall's room, then Four Charges. Then the map: a shot at the lift
gate, and the gate gone. A shot at the rock fall, and it gone too.

**Say:** "Both endings live in one room. || A choice has one condition, | so a thing that
needs two takes two rooms. | Facts in the first, and the jacks in the second. ||| Now
something you have to plan for. || A full shot destroys any prop it hits. | The game
doesn't stop, and it doesn't tell anyone. ||| Shoot the lift gate, and you can walk
through it. || Shoot the rock fall, and no ending is left. ||| So ask two questions of
your own mission. | Which props hold an ending? | And which doors does only a signal
open? ||| Mine still ends, because the clock runs out. | That's the best reason to have
one. ||"

### 7. Twelve checks, and the walk

**Screen:** The sheet of twelve checks, mine filled in. Then the game with three
consoles: the dig ending, cut to its turns. Then one console alone: the blast ending.

**Say:** "Lint reads your spelling. | It doesn't walk your map. || So here are the
checks of the whole class, on one sheet. | Twelve of them, in order. ||| Ways in and ways
out. | Keys and names that join. | Signals with two ends. || Then the worst party, and the three columns. | The screen, a full shot, and the clock. ||| Then walk it, every road. || Three
people dig them out. || One person, with no skill at all, blasts them out. ||| The times
on the page are floors from a script. | Walk yours with people, and write down what you
get. ||"

### 8. The rubric, and your turn

**Screen:** The rubric, ten lines. Then a blank sheet of paper, and a pencil.

**Say:** "Here's the rubric, in ten lines, | and each one has a way to know. ||| Three
areas. A quest tree. Two endings and a way to lose. || Three jobs nobody can replace. | A
clock that starts on the ground. || An ending for the smallest party. | And work for
three at once. ||| You're done when every line is ticked, | and when somebody who didn't
write it | has played it to an ending without asking you anything. ||| That's the end of Boarding Parties. | Now go and write yours. ||"
