# C2-6 video script - Reputation, a first look

> **STATE ON 2026-10-10. First version of this lecture.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **The student works in a COPY of the mission**, a folder called `MyStanding`, made
>   from `MyMission` as Lecture 5 left it (`c2-05-hails\example\mission.amd`, with
>   Lecture 1's `story.mast`). Lecture 7 starts from Lecture 5's file line for line, so
>   today's lines stay out of `MyMission`. The game is started with
>   `sbs run server,helm,comms -m MyStanding map=0`.
> - **`example\` holds the one file that differs from that start:** `mission.amd`.
> - **No MAST.** Six kinds of line, all in `mission.amd`: `Values:` on a side, `Side:` on a
>   character, `earns` in a `Reward:`, `earns` on an answer, a guard on a line, a guard on
>   an answer.

> **Measured 2026-10-10, in the mock.** Tool as installed in `data\missions`, library as
> packaged in `__lib__` (sbs_utils `ae05dac7`). The page's steps were applied one at a
> time to Lecture 5's example, with lint after each. Then four walks of the finished
> file, and one-change variants of it: each linted, each played headless by a probe that
> flies the ship, reads the rows the Comms hail list would show, picks rows by their first
> words, and prints each ship's scores and standing with the Guild, the game's own answer
> to "would this side's fleets leave this ship alone", every quest's state and the
> credits. The two-ship walk set the number of player ships to two. Every line of tool
> output in a code block on the page is a line a run printed.

> **SEEN IN THE REAL GAME'S SERVER, with no console attached, on the same lines in
> another probe folder:** standing 0, then 30 after the generous answer; the warm line
> spoken and the extra answer offered, through the real hail path. **Nobody has read
> either line on a Comms console.**

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | A folder `MyStanding` that is a copy of `MyMission` as Lecture 5 leaves it. Scene 2 shows making it; have a second, finished copy ready for scene 9 |
| Lint | `sbs lint MyStanding` says `clean` |
| VS Code | `MyStanding` open and trusted, `mission.amd` in one tab, scrolled to the Sides section |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started twice on camera in scene 9, with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless play with the packaged library.
"Server" is the engine-server run in the note above. If an item fails while recording,
stop and fix the page.

1. Lint is `clean` after each of Steps 1 to 6. (Lint.)
2. A ship that flies straight to the Guild Yard has standing 0. The call
   `Harbormaster Quill - The Guild yard` opens on the cold line, with one answer. (Mock.)
3. After the report with the plain answer the ship's honest score is 30 and its standing
   with the Guild is 17. At the yard: the cold line, one answer. (Mock.)
4. After the report with the generous answer the scores are honest 30 and generous 30,
   and standing is 30. At the yard: the warm line, and two answers. (Mock, Server.)
5. Both answers of the report call complete Report to DS 1, and the side is paid 150
   either way. (Mock.)
6. Two ships, the Artemis gives the generous answer: Artemis 30, Intrepid 17. The Artemis
   gets the warm line and two answers, the Intrepid the cold line and one. (Mock.)
7. With scores of 30 and 30 the fleets part of LegendaryMissions answers that Guild
   fleets would leave the ship out of their targets; with 30 alone it answers that they
   would not. No fleet was watched. (Mock.)
8. Every row of the tables in Step 9. (Lint for all, Mock where the row says what the
   game does.)

Not seen by anyone, and to watch for while recording:

1. Either of Quill's lines on a Comms console, and the list with one answer or two.
2. The call on the main screen.
3. Anything with two ships.
4. A fleet holding its fire. This mission has no fleets.

## Scenes

### 1. Cold open

**Screen:** Comms, the call "The Guild yard", twice. First: the cold line, one answer.
Then: the warm line, two answers.

**Say:** "Here's the same call, in two different games. || In the first one, Quill tells
the crew to hold outside the markers. || In the second, she opens the yard, | and there's
an answer that wasn't there before. ||| Nothing in the story changed between them. || What
changed is what the Guild thinks of this ship. || Today you'll teach a side to keep score,
| and you won't write a line of script to do it. ||"

### 2. A copy to work in

**Screen:** File Explorer, `data\missions`. Copy `MyMission`, paste, rename the copy
`MyStanding`. VS Code: Open Folder, `MyStanding`. Command prompt: `sbs lint MyStanding`.
Clean.

**Say:** "Before I type anything, I make a copy of my mission folder. || The next lecture
starts from the file exactly as Lecture 5 left it, | so today's lines go in a copy. || I
call it MyStanding, | I open it in VS Code, | and I run lint on it. ||| It's clean, and
it's the same mission. || From here on, everything happens in the copy. ||"

### 3. What the Guild values

**Screen:** The table of seven trait pairs on the page. Then the Sides section: type the
`Values:` line on Harbor Guild. Save. Lint: clean.

**Say:** "The game measures a ship on seven pairs of traits. || Honest or liar, generous or selfish, | fearsome or cowardly, and so on. || Neither end is the good one, | because
that depends on who's judging. ||| So I tell the game what the Harbor Guild cares about.
|| On its record I write Values, | then honest forty, a comma, generous thirty. || Those
numbers are weights. || They say honesty counts a bit more than generosity, | and they
don't have to add up to anything. ||"

### 4. Who speaks for the Guild

**Screen:** The Characters section: add `Side: guild` under Quill's `Face:` line. Save.
Lint: clean.

**Say:** "Standing is always somebody's opinion. || So when Quill asks about it, | the
game has to know whose opinion she's giving. || I tell it on her record, with one line: |
Side, and the Guild's key. ||| You've typed that line before, on a landmark. || On a
person it means, this character speaks for that side. || Leave it off, and she speaks for
nobody, | and the number she reads is always zero. ||"

### 5. Two deeds

**Screen:** Report to DS 1: change the `Reward:` line. Then Quill Calls Back: add the
second answer. Highlight the comma in each. Save. Lint: clean.

**Say:** "Now the crew needs a way to earn something. || A deed is the word earns, | and
then three more: a side, a trait and a number. ||| The first one goes on the quest. ||
After the credits I put a comma, | and then earns guild honest thirty. || The crew did the
job and came back to say so, | and the Guild calls that honest. ||| The second deed goes
on an answer. || I add a way to report that gives the fee to the tug crews, | and after
the semicolon it earns generous thirty. || Both answers still finish the step, | because
that's the rule from last time. ||"

### 6. A call that reads standing

**Screen:** Type the beat The Yard Calls, then the scene The Guild Yard with its two
guarded lines and one answer. Highlight the curly brackets. Save. Lint: clean.

**Say:** "So far the Guild is keeping score, and nobody's reading it. || I add a beat that
places a call when the ship comes near the Guild's yard, | and I write the scene for it.
||| Look at Quill's two lines. || Until today, two lines in a block were two takes, | and
the game picked one. || These two each have a guard, in curly brackets, right after the
percent sign. || The first can only be said to a ship below thirty. || The second can only
be said at thirty or more. ||| Between them they cover every ship, and that matters. ||
If no line can be said, the call opens with no words at all. ||"

### 7. An answer that needs standing

**Screen:** Add the second answer to The Guild Yard, with `if standing >= 30` between the
round brackets and the semicolon. Save. Lint: clean.

**Say:** "An answer can have a guard too. || After the round brackets I write if and the condition, | and only then the semicolon. ||| A ship below thirty doesn't see this
answer greyed out. || It doesn't see it at all. ||| Back in Lecture 4, I told you to leave
this kind of condition alone, | because there was almost nothing it could read. || Now
there is something: standing, with the side the speaker speaks for. ||"

### 8. How the number works

**Screen:** The table in Step 7 of the page, row by row. Then the two-ship table in
Step 8.

**Say:** "Here's the part that surprises people. || The quest earns honest thirty, | and
the ship's standing after it is seventeen. ||| That's because standing isn't one score.
|| It's the average of everything the side values, | weighted by those numbers on the
Values line. || Honesty alone gets this crew about half way. || Add the generous answer, |
and both scores are thirty, so standing is thirty. ||| And the number belongs to a ship.
|| With two ships, the quest pays them both, | but the answer pays only the ship that gave
it. || So one crew gets the berth, | and the crew beside them is told to hold outside. ||"

### 9. Play it

**Screen:** Game one: fly straight to the Guild Yard. The call, the cold line, one
answer. Close. Game two: the hulk, the job, the report call with two answers, the
generous one. Then the yard: the warm line, two answers.

**Say:** "Let's play it twice. || First I fly straight to the yard, having done nothing.
|| There's the call, with the cold line, | and there's my one answer. ||| Now a new
game. || I take the job, I wait for the beacon, | and this time the report call offers me
two answers. || I give the fee away. || Then I fly to the yard. ||| And there's the other
line, | and a second answer under it. ||"

### 10. What lint can and cannot see

**Screen:** Change `guild` to `gild` in the `Reward:` line. Lint: the warning. Put it
back. Then delete `Side: guild` from Quill. Lint: clean. Put it back. Show the tables on
the page.

**Say:** "Lint knows your sides and it knows the traits. || If I misspell the side after
earns, | it tells me, and it lists the sides I do have. ||| But now watch what happens | when I take the
Side line off Quill, | and lint says clean. || In the game she now speaks for nobody, |
the number is always zero, | and the yard never opens. || So that line you check with your
own eyes. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Give the crew a selfish way to report, | and work out the
standing before you play it. || Then change what the Guild values, | and watch the same answer land differently. |||
Next time, we go back to your own mission folder, | and look at the tools that show you
the whole story at once. ||"
