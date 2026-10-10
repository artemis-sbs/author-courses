# C3-14 video script - Pacing an away mission

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 13's finished files** in `MyAway`. One file changes:
>   `mission.amd`, in three records. `example\` holds it.
> - **No MAST.** The clock is `Fails when:` on the starter's quest, as in Class 1.
> - **EVERY NUMBER IS A FLOOR FROM THE STAND-IN.** A script walked stand-in consoles at
>   the game's speed and pressed the instant a button appeared. Nobody has timed real
>   people on this mission. Where the page turns a floor into minutes it says "my guess":
>   half a minute a press, doubled for a first play. Do not say those as measured.

> **Measured 2026-10-10, in the mock**, on the packaged library (sbs_utils `ae05dac7`):
> path lengths from the game's own path finder; a crew member's walk timed over each
> stretch; the crawler against one and two crew standing still (7.4 s; about 12 s); one
> crew member left down for a minute with others up; a FULL shot on the crawler and on
> a calmed sentry; the clock shown in the Tasks app and on the ship's quest rows (both
> captured from the draw functions), and the loss when 25 seconds ran out; the long
> road with one console and with three, before and after Marrow's fuse (59 and 56
> seconds; 49 and 68); the short road with the comms officer alone (19 seconds, 2
> presses); 7 one-change mistakes linted, 3 of them played.
> **Taken from the Lecture 11 measurements, not re-run:** the wake-up of a party that is
> all down (between five and ten seconds, at the entry, 1 point each), a stun holding,
> a door check tried again at once.
> **Computed, not timed:** the sentry's 11 second lap (22 cells at `Speed: 2`), and the
> odds table (a ten sided die plus the skill).
> **Not measured at all:** three crew standing still against a hostile; how long a real
> person takes over a press; any real table.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 13's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` in three tabs: the Quests section, The Yard Terminal, Old Marrow |
| Paper | The sheet from the page, blank, on camera: numbers, walks, presses, three lists, three columns |
| Game | Closed. Started on camera in scene 8 with a server, Engineering, Weapons and Science, and a stopwatch |

## Confirm on camera

1. Lint is `clean` after each of the three edits. (Lint.)
2. The Tasks app shows a time under Relight Kesh Relay. (Mock, captured from the draw
   function.) The ship's quest list shows it too. (Mock, captured.)
3. With the clock set to 25 seconds the game ends with the new `Lose:` sentence while
   the party is on the ground. (Mock.)
4. After the sentry is calmed from the terminal, the one who answered holds a power
   cell. (Mock.)
5. After Marrow's cough is seen to, the one who answered holds a fuse. (Mock.)
6. The long road is won by three consoles with 11 presses, split 2, 5 and 4. (Mock.)

Not seen by anyone, or not measured. If one is not as described, stop and fix the page:

1. The clock on a real handheld, and how it reads below one minute.
2. A real crew's time for any beat. The stopwatch in scene 8 is the first.
3. Whether seven seconds is enough for a real hand to arm and fire.

## Scenes

### 1. Cold open

**Screen:** A stopwatch beside the game. Then a sheet of paper with one line on it: 45
minutes. Then the Tasks app with a time counting down.

**Say:** "How long is your mission? ||| You've played it, so you have a feeling. | A
feeling isn't a number. ||| Today we measure it with the game's own numbers. || We put a
clock on it. || We check by hand that every party can finish. || And we look at what
three people are doing in the same minute. ||| There's one warning first. | A script walked this
for us, and a script doesn't read. || So every number today is a floor. ||"

### 2. The game's numbers

**Screen:** The first table from the page, built up row by row over the map: a crew
member crossing the yard; the crawler closing on a figure that stands still.

**Say:** "A crew member walks four cells a second. || Your hostiles walk two. ||| A
hostile beside you hits after about two and a half seconds, | and then again every two
and a half. || Three hits, and you're down, | in about seven seconds. ||| If the others are still
up, you stay down until somebody brings a medkit. || If everybody's down, you all wake
at the entry a few seconds later, with one point each. ||| And a full shot puts any
hostile down in one, | whatever its hit points say. ||"

### 3. Distance is not pressure

**Screen:** The walks table. A line drawn across the yard, counted: 28 cells, 7 seconds.
Then the whole long road traced across three maps.

**Say:** "Now walk your own map. | Count the cells and divide by four. ||| The landing
pad to the way east is seven seconds. || The whole long road, out to the spare cell and
back, | is under a minute. ||| So distance isn't what makes a mission long. || A door on
the far side of the map costs your crew seven seconds. ||| What costs them time is
reading, and deciding. | So that's what we count next. ||"

### 4. Count the presses

**Screen:** The scenes table. Then the three plays: 2 presses, 11, and 11 between three.
Circle the 2.

**Say:** "Thirty-one rooms, and nine hundred words. ||| Three plays, by script. || The
long road alone is eleven presses. || With three crew it's still eleven, between them. |||
And look at this one. | The comms officer, alone, wins in two presses. || Shoot the
sentry, take its cell, light the beacon. | That's the starter's design, and it's a kind
one. | Just know it's there. ||| To turn presses into minutes, I have to guess. || Half a
minute a press, | and double it for a first play. || Write your own guess beside mine. ||"

### 5. A clock

**Screen:** The Quests section: one line typed above `Win:`, and the `Lose:` line
rewritten. Lint clean. Then the Tasks app: the time under the quest.

**Say:** "You have four ways to press on a crew. || A clock, a patrol, | a key that's
somewhere else, and a thing that's hidden. ||| The clock is one line, and you wrote it in
the first class. || Fails when, thirty minutes. ||| The Lose sentence has to change with
it. | It used to say the beacon was slag. || Now it's read when the clock runs out too, |
so it has to be true every way. ||| And the clock starts when the quest starts. | This
one starts with the game. ||"

### 6. Can every party get there?

**Screen:** Three lists on the sheet of paper: every area, every item, every ending,
with a word beside each: anyone, a job, a skill, luck. Then the terminal's answer, and
`give power_cell` typed onto it.

**Say:** "Lint doesn't walk your map. | You do, on paper, in three lists. ||| Every area,
every item, every ending. | And beside each one, who can do it. ||| Now find a party the
lists leave stuck. || A scientist and a guard, and no engineer. ||| She pulls the door
code, and calms the sentry. | That's the clever answer. || But the sentry keeps its cell,
| and nobody here can run the pump. ||| The clever answer left them with nothing. || So
fix it where it broke. | The sentry hands its cell over. | One outcome, after a comma. ||"

### 7. Three columns

**Screen:** The first three-column table: one column full, two nearly empty. Then the
cough answer with `give fuse` typed onto it. Then the second table, all three columns
busy.

**Say:** "Three columns, one for each console. | What is each person doing? ||| This is
the mission as you left it. || The chief makes eight presses out of twelve. | The doctor
is finished in ten seconds. ||| What you have there is a chain. | Every step waits for the one before, |
so only one person is ever busy. ||| The cure is a join. | Make the thing in the middle
need pieces from three places. ||| Your pump needs three fuses. | So give Marrow one to
pay the doctor with. || Now three people each carry something to the pump house, | and
nobody presses more than five times. ||"

### 8. The beat sheet, and your turn

**Screen:** The beat sheet with two columns of times. Then the game with three consoles
and a stopwatch running. Then the blank sheet for 45 minutes. Then the exercise.

**Say:** "Put it together in a beat sheet. || One column is the stand-in's clock, | and that one is measured. || The other is my guess for a first play. ||| Now play it with a
stopwatch, | and write your own times over mine. ||| For forty-five minutes, write the
sheet first. || Five for the landing. | Twenty for three tracks. | Eight for the join. ||
Seven for the last area, | and five for the ending. ||| That sheet is where your own
mission starts. ||"

> Builder: the stopwatch run in this scene is the first time anybody has timed this
> mission with people. Put the real times on screen beside the guesses, and change the
> page if they differ by much.
