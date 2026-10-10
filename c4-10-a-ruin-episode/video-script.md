# C4-10 video script - Capstone: a ruin episode

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released** (2026-10-09). The page is written for
>   Artemis Cosmos 1.4.0, installed from Steam or itch.io, with a current tool and
>   libraries.
> - **NOBODY HAS PLAYED THIS EPISODE.** It has been walked by a script, end to end, in
>   the mock. No suit has been flown by a person, no repair has been done at a console.
>   Record Lectures 8 and 9 first; this recording depends on everything they find.
> - **The student's mission is `MyRuin`** as Lecture 9 left it:
>   `c4-09-station-repair\example\mission.amd` (526 lines) and Lecture 6's `story.mast`
>   (116 lines). The game is started with `sbs run server,helm,comms -m MyRuin map=0`.
> - **`mission.amd` only.**
> - **`example\` holds the one file that differs from the start:** `mission.amd` (552
>   lines). It is the whole class in one file.
> - **Scenes 6 to 8 are one take of about twenty minutes of play, cut down,** and they
>   end a game. A recording take adds a line to the game's own `game_results.yaml`. That is
>   fine for a real play; say nothing about it.
> - **A PERSONAL SIDE STORY IS AN OPTIONAL PART OF THE PAGE, NOT OF THE CAPSTONE.** A
>   `For:` story in the ruin's own Side Stories section is handed to the crew member who
>   suits up, starts at once and finishes on its signal (fixed in the library after the
>   first version of this lecture; re-measured 2026-10-10 on sbs_utils `ae05dac7`). The
>   page has it as "One more thing", after the walk. Lint still says
>   `stories-not-handed-out` about it, wrongly, and the page says so. The capstone file,
>   the walk and its credits are unchanged.
> - **The exosuit can close a client** the first time it appears (an engine fault,
>   reported). Lecture 8's page has the one line that switches to a stock hull.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `e84602e7`, Legendary Missions `b37a320`).
> The page's steps were typed one at a time onto Lecture 9's finished file, with lint
> after each. The finished file was then walked end to end, and 19 one-change variants
> were linted and most of them played.
>
> **What the script did.** One stand-in console, connected the way the mock's own browser
> bridge connects one. It went outside twice, each time through the function behind the
> Boarding Party app's button: at DS 1 (the offer was DS 1 Worksite) and at the door (the
> offer was The Hollow). Places were picked from the suit's own list; scenes were read
> from the Act transcript and answered; the beam was used through `eva_use`, which is
> what a press in the Fire app calls; the calls on Comms were opened and answered with
> the game's own functions; COME ABOARD was the app's own function. The ship was moved
> by the script. FOR EVERY LEG the suit was put at the place and one autopilot pass was
> run: nothing in this lecture was flown. (Lecture 8 flew one leg; Lecture 9 flew one.)
> The cutscene at the cairn was started by Lecture 6's card and had no main screen to
> play on.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 9 leaves it, lint clean. `mission.amd` has 526 lines |
| `story.mast` | Lecture 6's, 116 lines. Never opened in this lecture |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 6 with a server, a Helm console and a Comms console |
| People | Two, or one person who can reach both consoles |
| The walk table | Step 5 of the page, printed or on a second screen, to tick off on camera |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library, driven as described above. If an item fails while recording, stop and fix the
page.

1. Lint is `clean` after Step 2 and after Step 3. (Lint.)
2. At the start the quest list holds The Hollow Survey and one step, Raise the Mast.
   Every other step, The One Who Stayed and Forty-One are hidden. (Mock.)
3. All fifteen rows of the walk table in Step 5, with the credits in its last column: 40
   after the mast, 90 at the door, 140 at the altar, 220 after the count, 320 after the
   slab, 420 at the niche, 720 with the bowl, and a win with 820 at DS 1. `mast.runtime.log`
   empty. (Mock.)
4. In that walk the facts were filed on two lists: `names`, from the ring call, on the
   game's own list, and `tally`, from the altar's scene, on The Hollow's. With the
   cairn's answer changed to `if learned >= 2` it was NOT offered; changed to
   `if learned names` it was. (Mock, 2026-10-10. The first version of this lecture
   measured one shared list; the library changed.)
5. A crew member who does not read the marks is offered one answer at the cairn, "Leave
   her be", and Forty-One stays hidden. (Mock.)
6. With `Fails when: 20 seconds` and nobody moving, the game ends as a loss with the
   `Lose:` sentence. (Mock.)
7. The ruin first: with the ship at the door before the mast is mended, nothing changes.
   After the mast, back at the door, Find the Way In completes. (Mock.)
8. Every row of the two tables in Step 4: lint for all of them, and the mock for what the
   game does. (Lint, Mock.)
9. "One more thing": a `## [Side Stories]` section with one `For: comms` story. Lint:
   `stories-not-handed-out`, on line 524. In the game, with the Comms officer suiting up
   at The Hollow: nobody holds the story before; it is on that crew member's list and
   running the moment they suit up; after **Log it** at the cairn it is done, the crew is
   told `Quest complete: The Tally`, and the ship has 80 more. (Lint, Mock.) With a Helm
   officer suiting up, the story was not on that crew member's list, and it was still
   announced complete and paid at the cairn: who holds it then was not found out.

Not seen by anyone. If one is not as described, stop and fix the page:

1. Everything in Lecture 8's and Lecture 9's lists.
2. How long the episode takes with people. Nothing was flown here; the forty minutes is a
   guess built on one flown leg (about three minutes from the door to the altar at
   Cruise). TIME IT on the first take and change the number in Lectures 8 and 10 if it is
   wrong.
3. The cutscene at the cairn playing on the main screen while a crew member is outside,
   and the cairn's own scene opening on the suit at the same moment.
4. The quest list with ten finished rows.
5. The end screen for this mission.

> Keep off camera: the place's own marker in the Fire app at the niche (Lecture 8's note).
> The `For:` story is optional on camera: if it is shown, show lint's warning and say it is
> wrong for a ruin.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game, cut fast. A suit at the station's mast. The ship at the door of The
Hollow. A suit at the altar. The cairn. The Fire app on the slab. The bowl. The end
screen.

**Say:** "This is the last lecture of the class, | and there's almost nothing new in it.
||| Everything you've written since Lecture one is about to become one episode. || It has
a beginning at the station, | a middle inside the ruin, | and an ending back home. || And
today you learn to check it, from the first line to the last. ||"

### 2. The episode on one page

**Screen:** The table from Step 1 of the page. Scroll it slowly.

**Say:** "Before I change anything, I read what I have. || This table is the whole
episode. || Each row is something that happens. | It says where it happens, who does it, |
and what finishes it. ||| Seven of the rows are the story, | and the game is won when
those seven are done. || The other five are what a curious crew finds on the way. ||| Draw
a table like this for every episode you write. | Draw it first, before any record. ||
Every row needs something that finishes it, | and somebody who's able to. ||"

### 3. The mast is the first step

**Screen:** `mission.amd`, Quests. Delete Raise the Mast. Under the arc's description,
type the step Raise the Mast. Change Find the Way In to `Starts when: revealed`.

**Say:** "Last time the mast was a quest by itself. || Now it opens the episode. ||| So I
delete that quest, | and I type it again inside the arc, with four hashes. || It gets
three more lines: | a Then, to reveal the next step, | and the two lines that make it
count toward winning. ||| And the way in is no longer first, | so it starts when it's
revealed. ||"

### 4. A clue for the crew who go inside

**Screen:** Quests: type Forty-One below The One Who Stayed. Dialogue: add `; learn tally,
accepts forty_one` to the altar's answer. Relics: add `Scene:` and `Scan:` to The Cairn.
Dialogue: type At the Cairn and The Count.

**Say:** "Earlier the ship got a clue chain. | Comms logged some names, | and a later call
had one more answer. ||| This is the same idea, for somebody in a suit. || At the altar,
the answer that reads the marks | now learns a fact, and starts a quest. || Then the cairn
gets a scene of its own. || And one of its answers says if learned, at least one. ||| So a
crew member who read the marks can count the stones against them. | One who didn't just
sees a pile of stones. || And the count sends the word that finishes the quest. ||"

### 5. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Change `accepts forty_one` to
`accepts fourty_one`, save, lint, read the warning, undo.

**Say:** "I run lint, and it's clean. || I misspell the quest on the answer, | and lint
names the line. ||| But lint only reads a file. | It can't play an episode. || So the last
check isn't lint at all. ||"

### 6. The walk

**Screen:** The walk table from Step 5 of the page, beside the game. Start the game with
`sbs run server,helm,comms -m MyRuin map=0`. Play rows 1 to 5: the quest list, the
worksite offer, the mast, the door.

**Say:** "The last check is a walk. || Every row of the episode, in order, | with what I
expect written down before I start. ||| In row one, the quest list has one step, the mast.
|| In row two, near the station, the app offers the worksite. || I go out, I weld the
mast, | and the next step appears. || I've got forty credits, and the table says forty.
||| Then I come aboard and fly to the door. | Ninety credits, and the table says ninety.
||"

### 7. Inside

**Screen:** Rows 6 to 11: the ring call, the altar and its scene, the altar call, the
cairn, its cutscene and its scene, the count.

**Say:** "Now I suit up again, and this time the app names the Hollow. ||| At the ring,
Comms logs the names. || At the altar the step is done, | and I read the marks on the rim.
|| There's the new quest in the list. ||| Comms plays the entry for Dace, | and marks the
side room and the Gallery. || At the cairn, the side story finishes, | and the cutscene
plays on the main screen. || And on my suit, there's the answer I earned. || I count the
stones, | and there are forty-one. ||"

### 8. The bowl, and home

**Screen:** Rows 12 to 15: the slab, the niche, Comms opens it, the bowl, come aboard, fly
home, the end screen.

**Say:** "Then the slab, twelve seconds with the beam. || Then it's the niche. | Comms
opens it, and I take the bowl. ||| I come aboard, and we fly home. || Eight hundred and
twenty credits, | and the table says eight hundred and twenty. || Every row has agreed.
||| Then I check the other ending. || I set the clock to twenty seconds, and I sit still.
| There's my Lose sentence. || And the log file is empty after both. ||"

### 9. One more thing, and what you don't have yet

**Screen:** The section "One more thing - a story for one person" on the page, then the
table "What this class has not given you".

**Say:** "Here's one more thing before you go. || In Class three you wrote a story for
one person. || A ruin can carry one too, in a section of its own, | and the game hands it
to the crew member who suits up. ||| The page shows you one to type, | and it tells you
about one lint warning that's wrong here. || Then it lists three things this class
hasn't given you, | so you don't go looking for them. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "And now the class project. || Make a new mission, and write an episode of your
own. ||| Draw the table first. || Build the ruin, give it a voice, and hide a piece in it.
|| Write the arc, with a win, a loss and a clock. ||| Then write your walk, and walk it.
|| You're finished when your table and your game agree on every row. ||"