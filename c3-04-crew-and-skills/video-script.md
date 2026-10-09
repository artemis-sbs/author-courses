# C3-4 video script - Crew and skills

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0 from
>   Steam or itch.io, with a current tool and libraries.
> - **Starts from Lecture 3's finished files** in `MyBoarding`. Only `mission.amd`
>   changes, so `example\` holds that one file.
> - **No recipe card.** The game reads `Skills:` with the rest of the roster.
>   `story.mast` is not opened in this lecture.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae2bbf4a`). The steps were typed onto Lecture 3's files and linted. The
> finished file was played headless with stand-in consoles, the die fixed at 5 for the
> two tries the page describes, then with real dice for the counts. Then 29 one-change
> variants: each linted with the installed tool, and every party walked through it with
> the library's own choice and answer functions, a check forced both ways. No engine, no
> window.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyBoarding` with Lecture 3's files. Lint clean |
| VS Code | `MyBoarding` folder open, `mission.amd` in one tab |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 7 with a server, Helm, Engineering and Science, the last two side by side |

## Confirm on camera

1. Lint is `clean` after each step. (Lint.)
2. On the bridge, Pull the sensor record is offered to Dr Hale and not to Chief Okoro.
   (Mock.)
3. In the reactor room, Try to wake the core is offered to both. With the die at 5, Dr
   Hale's page line is `Dr Hale - engineering 0, rolled 5: 5 vs 9, failure.`, she lands
   in The Board Stays Dark and the party learns nothing; Chief Okoro's is
   `Chief Okoro - engineering 4, rolled 5: 9 vs 9, success.`, he lands in The Core Turns
   Over and the party learns `lockout`. Both lines are on both pages. (Mock.)
4. With no `Skills:` lines at all, Chief Okoro's engineering is 2 and Dr Hale's is 0.
   (Mock.)
5. Engineering alone: the suit tags marked as covering, no sensor record, the core still
   offered. (Mock.)
6. Every row of both tables on the page. (Lint, and every party walked.)

Seen on a real screen by the earlier pilot, with two real consoles on the bridge of the
hulk: the two bars, two buttons on Engineering and three on Science, and roll lines one to
a line above the room's own line.

Not seen by anyone. If one is not as described, stop and fix the page:

1. A real roll made by pressing the button, and the room that follows it.
2. This rewrite's files in the real game.

## Scenes

### 1. Cold open

**Screen:** The reactor room on two consoles. The Science console tries the core. A roll
line appears, then The Board Stays Dark. The Engineering console tries. Another roll line,
then The Core Turns Over.

**Say:** "Same button. Two people. || One of them is the chief engineer and one of them is
a surgeon, | and the hulk can tell the difference. ||| Last time, a choice asked what your
job is. || This time it asks how good you are. ||"

### 2. Say what each person is good at

**Screen:** `mission.amd`, the crew roster. Add a `Skills:` line to Chief Okoro, then to
Dr Hale. Highlight `science 3` on Dr Hale.

**Say:** "I open my roster, | and I give each person one new line, under their job. It's a
list: | a word, a space and a number, | with commas in between. ||| The chief is
engineering four, and science one. || The doctor is medical four, and science three. ||
Now look at that last one. | Science isn't her job. | She's simply good at it. || And
that's what a skill is for. ||| There's nothing to paste this time. | The game reads these
lines along with the rest of the roster. || A job with no number counts as two, | so
before today the chief's engineering was two, and this line makes it four. ||"

### 3. A choice for someone good enough

**Screen:** The Bridge. Type the `Pull the sensor record` choice, then The Sensor Record
room. Then show the page's table of three kinds of choice.

**Say:** "On the bridge I add a choice with a new kind of condition. It says if, | then
the word skill, then science, | then at least three. ||| Dr Hale has science three, so
she's offered it. | The chief has one, so he isn't. || And here's the thing to remember.
||| When a choice asks for a job, | and that person stayed on the ship, | somebody covers
for them. || When a choice asks for a skill, nobody covers. || With the doctor at home,
that record isn't on anyone's menu. ||"

### 4. A choice anyone may try

**Screen:** The Reactor Room. Type the `Try to wake the core` choice. Type the two rooms.
Highlight `check engineering 9`, then `else core_dead`, then `, learn lockout`.

**Say:** "In the reactor room, a different idea. || This choice has no condition, | so
everyone is offered it. || What differs is how it turns out. ||| After the semicolon it
says check, then a skill, | then a target of nine. || The game picks a number from one to
ten, | adds that person's skill, | and nine or more works. ||| Then else, and a second
room, | which is where a failure goes. || And after a comma, what the party learns, | but
only when it worked. ||| So the chief wakes the core six times in ten, | and the doctor
manages it twice in ten. || And the page shows the roll to everyone in the room, | so the
whole party sees who tried and how close it was. ||"

### 5. Four rules

**Screen:** The four rules on the companion page.

**Say:** "Four rules. A skill choice is a bonus, and never the only way, | because nobody
covers for a skill. || A check always has an else, | and both rooms lead back. || What
comes after the check happens only on success. || And the numbers belong to the person on
the roster. ||| A party may try again, by the way. | The roll is there for drama. | It
isn't a lock. ||"

### 6. Lint

**Screen:** Command prompt: `sbs lint MyBoarding`, clean. Change `Skills:` to `Skill:`,
lint, undo. Remove the number from the check, lint, undo. Change `science 3` to
`sience 3` on the roster, lint: clean. Undo.

**Say:** "Lint is clean, and it names nearly every slip you can make here. || Leave the s
off Skills, and it tells you. || Leave the number out of a check, | and it tells you
nothing would be rolled. ||| The one it can't catch is a skill misspelled on the roster
itself, | because you're allowed to invent skills. || So read your roster once, slowly.
||"

### 7. Play it

**Screen:** `sbs run server,helm,engineering,science -m MyBoarding map=0`. Alongside.
Both beam down. Bridge: the sensor record on Science only. Reactor: Science tries, then
Engineering tries. Point at the number in each roll line.

**Say:** "Both aboard. On the bridge, the doctor has the sensor record, | and the chief
doesn't. ||| In the reactor room, they both have the same button. || The doctor tries
first, | and the page shows her roll, with engineering nought in it. || Then the chief
tries, | and his line says engineering four. ||| That number is the one to watch. | If the
chief's line says two, | the game isn't reading his Skills line, | and lint will say why.
|| One more thing you'll notice. | Nothing on the handheld tells a player their own
numbers. | The only place a number shows is in a roll. ||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Give your third person some skills. || Add one choice that only they're good
enough for, | and one check on a skill that nobody has. Then break it. | Take the s off
Skills, read the warning, | and play it once anyway. ||| Next time, one person gets a
quest of their own. ||"