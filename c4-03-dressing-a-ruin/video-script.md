# C4-3 video script - Dressing a ruin

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`** as Lecture 2 left it: a fresh
>   `sbs create MyRuin -t amd` mission with the Relics section of
>   `c4-02-a-ruin-is-a-place\example\mission.amd` at the end of its `mission.amd` (92
>   lines). The game is started with `sbs run server,helm -m MyRuin map=0`.
> - **`mission.amd` only.** `story.mast` is never opened.
> - **`example\` holds the one file that differs from the start:** `mission.amd` (141
>   lines).
> - **No art pack.** The lesson uses only art that ships with the game. Do not add the
>   `ruins` pack for this recording.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's seven steps were
> typed one at a time onto Lecture 2's finished file, with lint after each. Then 105
> one-change variants of the finished file: each linted, each played headless by a probe
> that counts the objects the game made round the ruin by the art each one uses, reads the
> cloud's color, the set piece's place, size and facing, the name on the map and the three
> places' markers. Every number in the page's tables is from those runs. Since the first
> version: `Walls: rib` is a row; a comma or a word for a size after `Dress:`, and a role
> of two words, are new rows under "What lint cannot see".

> **CHECKED IN THE REAL ENGINE, 2026-10-04** (on the first version of this file; the
> Relics section has not changed). By script: the same 453 wall pieces as the mock, the
> purple cloud, the three places and their gold contacts. SEEN: the cloud on the main
> screen, and the ruin's name on Science. Not seen close up: plates, blocks, ribs, the
> ring, and which consoles draw a place's name.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 2 leaves it: The Hollow with The Mouth, The Nave and The Vault. The Gallery from Lecture 2's exercise may or may not be there; scene 2 adds it |
| Lint | `sbs lint MyRuin` says `clean` |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab scrolled to the Relics section, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 10 with a server and a Helm console. Add a Science console if the gold contacts are to be selected |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library, and a probe counted what the game made. "Engine" is the run of 2026-10-04 in the
note above. If an item fails while recording, stop and fix the page.

1. Lint is `clean` after each of the seven steps. (Lint.)
2. The finished file builds 3 chambers, 1 box and 3 passages, and 453 scenery objects: 67
   `generic-cube` pieces round The Gallery, 1 `generic-torus`, 355 asteroids round the
   other rooms and passages, and 30 loose rocks. Both logs empty. (Mock, Engine.) After
   Step 3, 60 of the 67 rocks within 800 of The Altar are `plain_asteroid_9`. (Mock.)
3. `Walls:` on the whole ruin, with the dials left out and no room of its own: `rock` 448
   pieces, `plates` 373, `blocks` 373, `ribs` 373 and 14 bars (all 14 in The Gallery),
   `none` 0. Each plus 60 loose rocks. `Walls: Plates` is `plates`. (Mock.)
4. `Seed: 12` gave the same layout with the runner started on two different seeds.
   `Seed: 7` and no `Seed:` line gave one other layout, the same as each other. (Mock.)
5. `Debris:` 0, 30, not written, 200 made 423, 453, 483 and 623 objects. `Gaps:` 0, not
   written, 0.2, 0.5, 1 left 82, 77, 67, 41 and 0 blocks in The Gallery, and the round
   rooms did not change. (Mock.)
6. `Atmosphere:` made exactly one cloud object, in the color written, for each of the
   seven colors and for `Purple`. `none`, and no line, made none. (Mock.)
7. The ring: one `generic-torus` at `1400, 0, 20000`, size 4, looking along `+x`, toward
   The Nave. With `Facing: mouth`, and with no `Facing:` line, it looks along `-x`. Each
   of the six shapes in the page's table was placed. (Mock.)
8. The name `The Hollow` on the map is at `0, 0, 19300`. Without an `entrance` point it
   is at `0, 0, 20000`. (Mock.)
9. Three invisible markers stand at the three places. With the ship 1300 from The Altar
   its marker was dark; at 1100 it was selectable and gold, and the other two were still
   dark. At 1100 from The Niche, that one turned too. (Mock.)
10. Every row of both tables in Step 8: lint for all of them, and the mock for what the
    game builds. (Lint, Mock.)
11. The exercise: ribs on The Gallery are 67 plates and 14 bars, and 36 and 14 with
    `Gaps: 0.6`; the piece on the altar; The Well; a new seed gave the same layout twice.
    (Lint, Mock.)
12. The Relic Plan's own code reads the finished file as 3 chambers, 1 box, 3 passages
    and 3 points, and the page it makes names The Way In and The Altar and not The Ring.
    (Run in node, outside VS Code.)

Read in the library's code, not measured: the ring is 210 across at size 1; a passage
always wears the ruin's `Walls:`; every piece of scenery is non-solid.

Not seen by anyone. If one is not as described, stop and fix the page:

1. What `rock`, `plates`, `blocks` and `ribs` look like, from inside and from outside.
   The page says cave, hull plating, masonry, bored shaft. Those words are the library
   documentation's.
2. That the flat pieces are plain grey. The page says "flat grey blocks".
3. Holes in The Gallery's walls at `Gaps: 0.2`, and that they read as damage.
4. The ring: that it is a hoop, that it stands across the tunnel and not along it, that
   it is big enough to fly through, and that the ship passes through it with no bump.
5. The ruin's name on Helm's map at the way in. Lecture 2 saw the name drawn at the
   middle of The Mouth; the new spot has not been seen.
6. The gold contact: which consoles draw it, whether its name is shown, and the moment
   it appears as the ship comes up the tunnel.
7. The Relic Plan with three points on it and no ring.

> Keep off camera: kits. Nothing in this recording should load the art pack. And do not
> type `Plate: 20`: the game makes 280 blocks for it where the lesson's ruin has 67.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. The ship inside The Nave: haze, rock, the ring behind, the block
walls of The Gallery off to one side. Cut to `mission.amd` at the Relics section.

**Say:** "Last time, this was three balls of rock. || Today it's a cave, with a hall
somebody built in it, | a haze, a gate, and places with names. || I didn't model any of
it. ||| I added about twenty lines to the same file. ||"

### 2. A built room

**Screen:** `mission.amd`. Add The Gallery below The Vault, or show that it is there.

**Say:** "Two of today's fields only show on flat walls, | so the ruin needs one box. ||
If you did last lecture's exercise, you have it already. | If not, add it now. || It has
six numbers: | the middle, then half the width, half the height, half the length. || And
it has a passage to the Nave. ||"

### 3. What the walls are made of

**Screen:** The Hollow's fence. Type `Walls: rock` under `Loc:`. Show the table of five
words from the page. Change `rock` to `plates`, then back.

**Say:** "This line goes on the ruin, and it names a look. || There are five words. ||
Rock is asteroids, and it's what you had already. || Plates are flat pieces laid over
every wall, | and blocks are the same with thickness. || Ribs are plates with bars across
them, | and none is no walls at all. ||| The game builds a wall from a few hundred small
pieces: | about four hundred and fifty rocks for this ruin, | or three hundred and seventy
plates. || I'm keeping rock, because this place is a cave. ||"

### 4. One room that differs

**Screen:** Type `Walls: blocks` in The Gallery's fence. Then `Art: plain_asteroid_9` in
The Vault's.

**Say:** "Now I say only where it changes. || The Gallery was built later, so the Gallery
gets blocks. || Every room without a line of its own takes the ruin's, | and so do the
tunnels, always. ||| Now for the Vault. || Art names the piece itself. | The game has six
asteroid shapes, | and a rock wall mixes them. || With this line, the Vault is cut from
just one. || So Art picks the piece, and Walls picks the look. ||"

### 5. Three dials

**Screen:** Back to The Hollow. Type `Seed: 12`, `Debris: 30`, `Gaps: 0.2`. Show the
`Gaps:` table from the page.

**Say:** "Next come three dials, all on the ruin. || Seed decides which rock goes where. |
The same number builds the same ruin every time, | so you and your players are looking at
the same place. || Debris is the loose rock drifting inside the rooms. | It's sixty if you
say nothing, and I want thirty. ||| Gaps is how much of a built wall is missing. || It's a
number from zero to one, and not a percentage, | so zero point two is one piece in five.
|| It only touches flat walls, which here means the Gallery. ||"

### 6. Haze

**Screen:** Type `Atmosphere: purple` in The Hollow's fence. Show the list of seven
colors.

**Say:** "One more line on the ruin. || Atmosphere fills the whole place with one cloud, |
in one of seven colors. || Leave the line out, or write none, and there's no cloud. ||"

### 7. A set piece

**Screen:** End of the file. Type The Ring. Then show the short list of shapes, and the
two list lines from "What an art pack adds".

**Say:** "Here's a new kind of record. || It has three hashes and a Relic line, like a
room, | but this is a prop, a thing standing in the ruin. || Prop says where it stands, | and
fourteen hundred along is the middle of the first tunnel. || Dress says what, and how big:
| a ring, at four times its size, | which makes it a little wider than the tunnel. ||
Facing says which way it looks, and that's at the Nave. ||| A prop takes no space, so you
fly straight through it. || These plain shapes come with the game. | Real gates and
statues come in an art pack, | and your mission doesn't have one yet. || But you can write
a list, | and the game takes the first word it knows. ||"

### 8. Named places

**Screen:** Type The Way In, The Altar and The Niche. Then the table from Step 7.

**Say:** "The last kind of record is a point, which is a named spot. || It has three
numbers, inside a room, | and it has roles, which say what it's for. || One role means
something to the game, and that's entrance. | The ruin's name on the map moves to this
point. ||| Any other role is a word of my own. || So the Altar goes in the middle of the
Vault. | The game stands an invisible marker there, | and when a ship gets close, | it
turns into a contact with this name. || The Niche is the same, and it's hidden. || Hidden
is for a crew in suits, later in this class. | For a ship, it changes nothing. ||"

### 9. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Change `Walls: blocks` to
`Walls: bloks`, save, lint, read the warning, undo. Delete a number from The Altar's
`Point:`, save, lint, read the warning, undo. Change `Dress: generic-torus 4` to
`Dress: generic-tortus 4`, save, lint: clean. Undo.

**Say:** "So I run lint, and it's clean. || Now I misspell a style, | and lint tells me,
and asks if I meant blocks. || I take a number out of a point, | and it tells me the place
won't be made. ||| Now I misspell the name of the ring, and lint says clean. || Lint
doesn't check that word, | and the game would simply build no ring. || The game does say
so, in its log file, after you play. || So read your Dress and Art lines yourself, letter
by letter. ||"

### 10. Play it

**Screen:** Command prompt: `sbs run server,helm -m MyRuin map=0`. Helm's map: The
Hollow. Fly in. The ring. The Nave. Up the tunnel to The Vault until The Altar appears.
Back, and into The Gallery.

**Say:** "The name is at the way in now. || Inside, there's the haze, | and there's the
ring, across the tunnel. || Through it we go, and this is the Nave. ||| Now up to the
Vault. | And there's the Altar, on the map, | because I'm close enough. || And this is the
Gallery, with built walls, and pieces missing. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Change the Gallery to ribs, and take more of it away. ||
Put something on the altar, | because a point can be dressed too. || Add a hidden place of
your own. || Then break one line where lint can see it, | and one where it can't. ||| Next
time, a place says something when the ship arrives. ||"
