# C4-2 video script - A ruin is a place

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`**, a mission of its own for this class: made with
>   `sbs create MyRuin -t amd --title "The Hollow"`, its libraries brought up to date with
>   `sbs fetch "MyRuin" --update-libs`, and nothing typed into it. Lecture 1 makes it,
>   borrows a ruin for ten minutes and deletes it again. The game is started with
>   `sbs run server,helm -m MyRuin map=0`.
> - **No card.** The template's `story.mast` builds every ruin in `mission.amd` (line 62).
>   The first version of this lecture pasted that line.
> - **`example\` holds the one file that differs from the start:** `mission.amd`.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were typed one
> at a time onto a fresh `sbs create -t amd` mission, with lint after each. Then 49
> one-change variants of the finished files: each linted, each played headless by a probe
> that asks the library what it built (the rooms and passages, the wall objects, the name
> on the map). Every line of tool output printed on the page is a line a run printed
> (`verify_page.py` in the harness folder). Since the first version: the table has the
> code lint prints; a passage with a comma before its number, and a `#` in front of the
> `relics_spawn` line, are new rows under "What lint cannot see"; a long dash is read as a
> minus by the game.

> **SEEN IN THE REAL ENGINE, 2026-10-03** (on the first version of these files; the ruin's
> five records have not changed), one screenshot each, with the ship parked in The Mouth
> by a probe. Helm's map draws the ruin: the wall props are tan rock blips, the two lobes
> of The Mouth and The Nave and the neck of the passage between them read as a floor plan,
> and the marker **The Hollow** is drawn in blue with its name at the middle of The Mouth.
> The main view from inside The Mouth: asteroid-sized rocks all around the ship, spaced
> well apart, with open sky between them. It reads as a rock field, not as a wall. By
> script in the same run: 3 chambers and 2 passages in one piece, 534 wall props, and a
> ship put on a wall prop was not pushed off it and reported no collision.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin`, fresh from `sbs create MyRuin -t amd`. `mission.amd` has 60 lines and ends with Derelict Materials, or the line numbers 65 and 90 on the page are wrong. `story.mast` has 105 lines and `relics_spawn` on line 62 |
| Lint | `sbs lint MyRuin` says `clean` |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab scrolled to the end, `story.mast` in another at line 62. Artemis AMD add-on installed (it has **Artemis AMD: Show Relic Plan**) |
| Mouse | One with a middle button, if the orbit in scene 6 is wanted. The Top, Front and Right buttons do not need one |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server and a Helm console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. "Node" means the add-on's own code was run outside VS Code on the lesson's file.
"Engine" is the run of 2026-10-03 in the note above. If an item fails while recording,
stop and fix the page.

1. Lint is `clean` on the fresh mission and after each of Steps 2, 3 and 4. (Lint.)
2. The finished file: the ruin `hollow` is built at `0, 0, 20000` with three chambers
   (radius 900, 1100, 700) and two passages (radius 350, 300); 534 rock objects stand
   round it; one name on the map, `The Hollow`, at `0, 0, 20000`; both logs empty. (Mock,
   Engine.)
3. Every row of the Step 7 table and of "What lint cannot see": lint for all of them, and
   the mock for what the game builds. (Lint, Mock.)
4. The two lint lines printed on the page, word for word, with `line 90` and `line 65`.
   (Lint.)
5. The exercise: the box that overlaps is `clean` and builds; moved to `-1900` it is
   `relic-disconnected`; with `Passage to: nave 300` it is `clean` and the game builds
   three passages. (Lint, Mock.)
6. The Relic Plan reads one relic, three chambers and two passages from the finished
   file. The page it makes carries the labels, the hover texts `The Mouth r900` and
   `nave - mouth: 3000u`, and the buttons Top, Undo, Preview and Live. With no `Loc:`
   line it reads `No relic in this file.` (Node.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. The Relic Plan panel itself: that the command is in the palette under that name, that
   the panel opens beside the file tilted, that **Top** gives a plan, and what the three
   rooms look like in it.
2. A tooltip on hover. The text is in the page the add-on makes; a tooltip has not been
   seen.
3. Clicking a room opens the box of numbers at the bottom right; `800` in `r` and Enter
   changes one line of the file; the panel's **Undo** puts it back.
4. The ruin from outside, and from how far away the rock starts to draw.
5. A helm officer getting a light cruiser down a passage 700 across.
6. The game not stalling while 534 objects are made at the start of the map.
7. `sbs run server,helm -m MyRuin map=0` for THIS mission. The same line was seen working
   for a Class 1 mission.

> Keep off camera: the panel's **Add** buttons (a new record lands above the last room's
> note), and **Preview** and **Live**.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The Relic Plan, top view, three rooms and two passages. Cut to the game: the
marker on Helm's map, then rock all round the ship.

**Say:** "This is a ruin. || It has three rooms and two tunnels, | and it's older than
anyone who could have built it. || I didn't model it, | and I didn't place a single rock.
|| All I did was write down where the empty space is. ||| Today, you write yours. ||"

### 2. Space, not walls

**Screen:** The table from Step 1 of the companion page.

**Say:** "A ruin is hollow, so what you describe is the hollow. || A chamber is a ball of
open space, and that's a room. || A passage is a tube of open space between two rooms, |
and that's a tunnel. || A box is a block with flat sides, a built room, | and you'll add
one yourself at the end. ||| And whatever you don't describe is wall. ||"

### 3. The ruin itself

**Screen:** `mission.amd`, the end of the file. Two blank lines. Type the Relics heading
and The Hollow.

**Say:** "I go to the very end of the file, | and I start a new section. || Its key has to
be the word relics, | because that's the word the game looks for. || Then comes the ruin
itself, | with a name for people and a key for the file. || And it has one field, called
Loc, which is where it stands: across, height, along. ||| The station is at zero, zero,
zero, | and the hulk is nine thousand along, | so this is past the hulk, on the same line.
|| The sentence underneath is a note to myself, | and no player ever reads it. ||"

### 4. The first room

**Screen:** Type The Mouth.

**Say:** "Now a room, and it has three hashes, the same as the ruin, not four. || A room
isn't written inside the ruin. | It's written beside it, | and this line says whose it is.
|| That's the ruin's key, and not its name. ||| Then Chamber, with four numbers. || The
first three say where, measured from the ruin, | so three zeros is the ruin's own spot. ||
The fourth is the radius, nine hundred, | so the room is eighteen hundred across. || My
ship is about a hundred. ||"

### 5. Two more rooms and the tunnels

**Screen:** Type The Nave and The Vault. Highlight `Passage to: mouth 350`.

**Say:** "The Nave is three thousand to one side, and it's bigger. || And it has a passage
line: | passage to mouth, three fifty. || That's the tunnel, and the word is the other
room's key, | and the number is the tunnel's radius. || There's a space between them, and
no comma. ||| I write each tunnel once, on either of its two rooms. || The Vault is
twenty-eight hundred further along from the Nave, | with a passage back to it, | so the
ruin turns a corner. ||"

### 6. Look at it

**Screen:** Save. `mission.amd` in front. Command palette, type Relic Plan, choose
**Artemis AMD: Show Relic Plan**. Press **Top**. Hover a room, hover a passage. Click The
Vault, type `800` in `r`, show the line change in the file, press **Undo**.

**Say:** "With the file in front, | I open the command palette and ask for the Relic Plan.
|| And there it is, drawn from the file, | and the game isn't even running. || Top looks
straight down, and each square is a thousand. || I can hover over a room for its size, |
and over a tunnel for its length. ||| Now I click the Vault, and I make it eight hundred.
|| Look at the file: one line has changed. || So the picture and the file are the same
thing. | I press Undo, and it's back. ||"

### 7. Nothing to paste

**Screen:** `story.mast`, line 62. Highlight it. Do not edit.

**Say:** "The file says what the ruin is. || And this line, which has been in your
mission since the day you made it, | builds every ruin the file holds. || It makes the
space, it puts rock around it, | and it writes the ruin's name on the map. || You don't
touch it. ||| And if there's no ruin in the file, it does nothing. ||"

### 8. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Change `nave` to `crypt` in The
Vault's passage, save, lint, read the warning, undo. Put a fourth hash on The Vault, save,
lint: the warning that says to give the heading three hashes. Show the plan still drawing
three rooms. Undo. Delete the `Loc:` line, save, lint: clean. Undo.

**Say:** "So I run lint, and it's clean. || Now I point a passage at a room that doesn't
exist, | and lint tells me so, by name. || Read the end of that sentence: | with this one
going nowhere, the game doesn't build the ruin at all. ||| Next, a fourth hash on the
Vault. || The plan still shows three rooms, but lint isn't fooled. | It says the room is
nested, and the game won't read it. || So it's three hashes on the ruin, and three on
every room. ||| And here's one thing lint can't see. || I take the Loc line away, and lint
says clean, | because it can't know where I meant. || The ruin would be built on top of
the station, | so keep the line. ||"

### 9. Play it

**Screen:** Command prompt: `sbs run server,helm -m MyRuin map=0`. Helm's map: the marker
past the hulk. Fly to it. Rock around the ship. Through the passage to The Nave.

**Say:** "I start the game with a server and a Helm console. || And there, past the hulk,
is The Hollow. || That marker is the middle of the Mouth. ||| And this is my wall. || From
inside it looks like a field of rocks, | and it's scenery today, so it won't stop me. ||
Through the tunnel we go, and this is the Nave. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. | Add a fourth room, and make it a box, | a built room with
flat walls. || Join it by overlapping the room next to it. || Then move it away, | and
watch lint tell you the ruin is in two pieces. || And then join it again, with a passage.
||| Next time, we decide what these walls are made of. ||"
