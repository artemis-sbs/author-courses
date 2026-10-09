# C3-6 video script - Checkpoint: a short boarding quest

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0 from
>   Steam or itch.io, with a current tool and libraries.
> - **A method lecture.** Almost nothing new is taught: three sentences, a beat sheet, a
>   drawing, a facts table, the scene typed in layers, five checks with a pencil, three
>   plays. The one new word is `accepts`, on the two endings.
> - **Starts from Lecture 5's finished files** in `MyBoarding`. `story.mast` does not
>   change, so `example\` holds `mission.amd` only.
> - **The way home is in the arrival room and the endings**, which is Lecture 2's rule.
>   An earlier draft of this lecture called that a departure; Lecture 2 now teaches it.
> - **The page is long and the video is not.** The video shows the method on the finished
>   scene. The typing is on the page.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae2bbf4a`). The steps were typed onto Lecture 5's files and linted at each
> one. The finished file was played headless with stand-in consoles five ways: the
> engineer alone to one ending and home, three aboard to the other, two aboard, a party
> that walks away, and one person beaming up and coming back. Then the earlier pilot's 57
> one-change variants again: each linted with the installed tool, and every party of one,
> two or three walked through it with the library's own choice and answer functions. No
> engine, no window.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyBoarding` with Lecture 5's files. Lint clean |
| Paper | One sheet with the three sentences, the beat sheet, the drawing and the facts table already written, to hold up |
| VS Code | `MyBoarding` folder open, `mission.amd` in one tab, the finished file ready to paste in stages |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 8 with a server, Helm, Engineering and Science |

## Confirm on camera

1. Lint after each step is what the page says: two `unfired-signal` warnings once the
   practice rooms are gone, those and two `signal-no-route` from Step 4 to Step 7, and
   `clean` after Step 8. (Lint.)
2. The engineer alone: the berth monitors and the stores come to him marked as covering;
   Account for the Crew completes on the covered reading; Twelve Berths is handed to
   nobody; 16 presses to an ending and home; Carry Word Home completes back at DS 1 with
   500 credits. (Mock.)
3. Three aboard, everything read, the main cell tried once: 20 presses, nothing marked as
   covering, 350 credits on leaving and 650 thirty-four seconds later when Stand By the
   Sleepers completes. The other ending's quest never appears. (Mock.)
4. Return to the ship in the airlock ends the visit for everyone at one press, and no
   party is on offer afterwards. One person beaming up by the handheld's own way home
   leaves the visit open, and they come back down into the room the party is in. (Mock.)
5. Every party of one, two or three reaches both endings. (Walked by script.)
6. Every row of the tables in Step 10. (Lint, and every party walked.)

Seen on a real screen by the earlier pilot, with three real consoles, start to finish:
the roll line, and the cabin's two endings as buttons.

Not seen by anyone. If one is not as described, stop and fix the page:

1. This rewrite's files in the real game.
2. The Crew app's Beam up button, and a console coming back down.
3. The time. Fourteen to twenty presses is a count. "About ten minutes" is a guess, and
   the page says so.

## Scenes

### 1. Cold open

**Screen:** Three handhelds in the captain's cabin, with the two endings as buttons.

**Say:** "Twelve people asleep behind frosted glass, one switch, | and a note that says
don't. ||| Three of my crew are standing in front of it, | and whichever button they
press, the ship gets a different quest. || This is the checkpoint for the first half of
the class. | You'll plan one away scene on paper, type it, check it, and play it. ||"

### 2. Three sentences

**Screen:** The sheet of paper: the question, the answer, the choice.

**Say:** "Before any rooms, three sentences. || The question the scene asks. | Why is this
hulk drifting, with nobody at the controls? || The answer, which the party finds in
pieces. | Her crew put themselves to sleep, to wait for help that never came. || And the
choice they make at the end. | Wake them now, or leave them and fetch a doctor. ||| The
pieces of the answer become your readings, | and the choice becomes your two endings. ||
If you can't write the third sentence, | you have a tour, and not a scene. ||"

### 3. The beat sheet and the drawing

**Screen:** The beat sheet on the page, then the drawing: airlock, spine, and four places
hanging from the spine.

**Say:** "Next, how much of everything. Six places. | Three readings, one for each job on
my roster. | One reading for a skill, and one check. | Five facts in all, and a door that
asks for three. ||| Then I draw it, with one room in the middle, | and every other place
leads back to that room. || The way home goes in the room they arrive in, | and at each
ending, and nowhere else. ||"

### 4. The facts table

**Screen:** The facts table on paper: five rows, and the column headed Sure.

**Say:** "This is the table that saves you. || For every fact I write where it is, who's
offered it, | and whether it's sure. ||| A fact is sure when every party can get it. || A
reading for a job on my roster is sure, | because when that person stays home, somebody
covers. || A reading for a skill isn't, | and neither is anything behind a roll. ||| I
have three sure facts. | So my door may ask for three, and no more. ||"

### 5. Type it in layers

**Screen:** `mission.amd`. The practice rooms deleted; five places typed; lint, two
warnings. Then in quick cuts: the readings, the check, the door, the endings, the
stories; lint after each. End on clean.

**Say:** "Now I type, in layers, and I run lint after each one. Places first, | and I've
torn out my practice rooms to make space. || Lint warns about two signals, | and it's
right, because the rooms that sent them are gone. Then the readings. Then the check. |
Then the door, with a line that tells an early party why it's shut. Then the endings. |
Each ending is a quest the ship doesn't have yet, | a choice that starts it, with the new
word accepts, | and a last room with one way out. ||| Then the two stories. | And lint is
clean. ||"

### 6. A quest any party can finish

**Screen:** Account for the Crew: its `Done when:` line. Then the page's table of the
two ways to wire it.

**Say:** "One change to the ship's quest. || Last time, it waited for the surgeon's story
to finish. | But a story is handed to nobody when its person stays home, | so a short crew
could never complete it. ||| Now it waits for the reading's own signal. || The surgeon's
press finishes her story and the ship's quest together, | and when she's not there, the
covered reading still finishes the ship's. ||"

### 7. Five checks with a pencil

**Screen:** The printed Scenes section and a pencil. Tick each heading. Circle each key.
Cross out the choices with a skill or a check. Trace the walk to an ending.

**Say:** "Lint has passed, and lint checks your spelling. | It doesn't walk through your
rooms. || So I do, with a pencil. ||| One: every room has a way out with no condition. ||
Two: every room has a way in. || Three: the door asks for no more than the sure facts, |
and every fact has its own name. ||| Four is the big one. | I cross out everything that
needs a skill or a roll, | and with what's left I walk to each ending. || If I can, every
crew can. ||| Five: each story's reading belongs to its person, | and each ending's quest
starts hidden. ||"

### 8. Play it three times

**Screen:** `sbs run server,helm,engineering,science -m MyBoarding map=0`. Engineering
alone aboard: a covering button, the hatch, an ending. Cut to three aboard in the hold:
three different menus. Cut to the cabin. Cut to the airlock: one press of Return to the
ship, and the visit is gone.

**Say:** "Then I play it three times, with a watch beside me. || Alone, I'm the chief, |
and two readings come to me marked as covering. || Sixteen presses, and I'm home with an
ending. ||| With everyone aboard, nothing is covered, | and reading it all takes twenty.
||| And once, I walk away. | One press in the airlock, | and the visit is over for
everybody, with nothing finished. || That's why the way home is where it is. ||"

### 9. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now write your own. || Three sentences, a beat sheet, a drawing, a facts table,
| and then the typing. || Do the five checks, | and break it three times on purpose, to
see lint say clean when the scene is wrong. ||| Then play it with everyone you can find, |
and write down how long it took. ||"