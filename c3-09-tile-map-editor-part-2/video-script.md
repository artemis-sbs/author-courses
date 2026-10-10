# C3-9 video script - The Tile Map Editor, part 2

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries, and the VS Code add-on 0.9.4.
> - **Starts from Lecture 8's finished files** in `MyAway`. Five files change:
>   `ground\landing.tiles`, `ground\gully.tiles`, `ground\starter.tileset`,
>   `ground\cistern.tiles` (new) and `mission.amd`. `example\` holds those five.
> - **`known:` and `beam:` are taught here**, though the plan's list for Lecture 8 does
>   not name them. They have to be: the handheld's Beam app puts a crew member into any
>   area that is known and not `beam: no`, which would let a party skip every door in
>   the class.
> - **THE EDITOR HAS NOT BEEN SEEN.** Every editor step was read from the add-on's source
>   and its help pages. The list is below.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The ten steps were typed in order and linted at each one. The
> finished files were walked headless by a stand-in console: yard to gully to cistern
> and back, with the Beam app's list read at each stop. Then 31 one-change variants,
> each linted, and the ones lint is silent about played. No engine, no window, no VS
> Code.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 8's `ground\gully.tiles`. Lint clean |
| VS Code | `MyAway` folder open; `landing.tiles` and `gully.tiles` in two tabs, `mission.amd` in a third |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 8 with a server and Engineering |

## Confirm on camera

1. Lint is `clean` after every one of the ten steps. (Lint.)
2. At the start the transporter reaches the yard only. A click on the exit at 29, 6 puts
   the stand-in at cell 1, 4 of the gully, and then the transporter reaches the gully
   too. The stairs at 17, 5 put it at 2, 1 of the cistern, which the transporter never
   reaches. Going back, it stands at 17, 4 of the gully and 29, 5 of the yard. (Mock.)
3. A click on the water walks to the edge and stops. A click on the pump or the crate
   walks up to it and does nothing more. (Mock.)
4. The sentry walks the longer loop. (Mock: seen at 18, 11, then 24, 11, then 22, 9.)
5. Every row of the page's tables. (Lint, Mock.)

Read from the add-on's source, NOT seen. If one is not as described, stop and fix the
page:

1. An exit mark is outlined in blue and labelled with the area it leads to.
2. `starter.tileset` opens as a table (the Tileset Editor) with Walk, See and Tall
   boxes, a Look field, and a **+ Kind** button that adds a kind that can be walked and
   seen across.
3. **Things** draws the props, people and hostiles of `mission.amd` on the map: an amber
   square for a prop in Kinds, its picture in Art.
4. **Move** drags a thing placed by `At:` and rewrites that line in `mission.amd`;
   **Undo move** puts it back; Ctrl+Z does not.
5. **Move** on a thing placed by `Mark:` moves the mark in the map file instead.
6. A patrol is a dashed loop with a dot at each cell, and a dot can be dragged.
7. The editor has no way to edit the `exits:` block, `known:` or `beam:`.
8. The handheld's Look app lists `Go to` and an area's title for each way out to an area
   the party knows.

## Scenes

### 1. Cold open

**Screen:** Three maps side by side in the editor: the yard, the gully, the cistern, their
exits outlined. A figure walks off the east edge of one and onto the next.

**Say:** "One map is a place. || Three maps joined together are somewhere to go. ||| Today
the crew walks out of the yard, | through your pump house, | and down a flight of stairs
to a tank of standing water. || And you stand the first things on your maps. ||"

### 2. A way out, and a way back

**Screen:** `landing.tiles`: + Entry, dust, to_gully, `>`. Paint cell 29, 6. Then
`gully.tiles`: + Entry, dust, to_landing, `<`. Paint cell 1, 5. The blue outlines.

**Say:** "An exit is a mark with a special name. || It starts with the word to, | then an
underscore, and then the key of the area it leads to. ||| So in the yard I add a legend
line, | with the mark to gully, | and paint one cell at the east edge. || Then the same in
the gully, | with a mark that leads back. ||| Three things to know about exits. || An exit
takes whoever stops on it, | so click the exit itself. || Each person goes through alone.
|| And they arrive beside the way back, | never on top of it. ||"

### 3. What the ship knows

**Screen:** `gully.tiles` as text. Type `known: no` under `entry:`. Then the table of two
header lines from the page.

**Say:** "Last time, the transporter put you straight into the gully. || That would spoil
things now. | A crew that can beam anywhere never has to find the way. ||| Two lines in
the header decide it. || Known, and then no, | means the ship doesn't know this area
exists | until somebody has walked into it. || And beam, followed by no, | means the
transporter can never lock on there at all. ||| The gully gets the first one. | You type
it yourself, | because the editor has no box for it. ||"

### 4. Water, and a third map

**Screen:** `starter.tileset` in the Tileset Editor, then as text: the `water` line typed
under `cliff`. Then a new file `cistern.tiles`: type it. Look at it in the editor.

**Say:** "The cistern needs water, | and the tileset has no such kind. || So I add one
line to the tileset. | Water can be seen across, | and it can't be walked on. ||| That
pair is what makes a map readable. | You can see the far side, | and getting there is the
puzzle. ||| Then a new area file, | typed the way you typed the gully. || A walkway round
a tank, | and a small room at the east end. || It carries both header lines, | so the only
way in is on foot. ||"

### 5. Stairs, and where they arrive

**Screen:** `gully.tiles`: + Entry, floor, to_cistern, `v`. Paint cell 17, 5. Then Text:
type the `exits:` block under the legend.

**Say:** "The stairs are one more exit, | inside the pump house against the east wall. |||
Now, an area file can also say where its exits lead. || It's a block of its own, called
exits, | after the legend and before the dashes. ||| Read this line as: | the mark to
cistern leads to the area cistern, | and you arrive beside the mark called foot. || You
only need the block when the usual arrival isn't right. | And the editor can't edit it, so
you type it. ||"

### 6. A thing at a cell

**Screen:** `mission.amd`, the end of Props. Type the Trail sign. Highlight `Area:` and
`At:`. Then `landing.tiles` in the editor: the sign on the map. Move it; show the `At:`
line change; Undo move.

**Say:** "Now the fact sheet. || A record that stands on a map says where in two fields. |
The first is always Area. || The second is one of two. | At takes a cell: | how far
across, a comma, and how far down. ||| So here's a trail sign, | at twenty-eight across
and five down, in the yard. || Open the yard's map, | and the editor draws the sign where
the record put it. || With Move I can drag it, | and the editor rewrites that line in the
fact sheet for me. ||"

### 7. A thing on a mark, and a patrol

**Screen:** `gully.tiles`: + Entry, floor, pump, `p`; paint cell 15, 4. `mission.amd`:
type the pump and the crate. Then the sentry: change the `Patrol:` line; the dashed loop
in the editor.

**Say:** "The pump belongs to the pump house, | so it gets a mark of its own. || And its
record says Mark, | and the mark's name. ||| Here's the rule that's easy to break. | A
mark's name goes in Mark, | and never in At. || At reads numbers only, | so a word there
reads as nothing, | and the thing is never placed. ||| Neither of these two has any words
under its fence. | That makes them scenery. | They're drawn, and they're in the way. |||
Last comes the sentry. || Its patrol is a list of cells, | with a semicolon between each
pair. || I've made its loop longer, | and the editor draws it as a dashed line. ||"

### 8. Lint, play it, and your turn

**Screen:** Lint: clean. Misspell `to_landing`; lint; undo. Write the pump's mark in
`At:`; lint; undo. Then the game: beam down, the Beam app empty, walk east, the gully, the
stairs, the cistern.

**Say:** "Lint knows about exits. | Misspell one of them, | and it tells you there's no
such area. || Put a mark's name in At, | and it tells you that too. ||| It can't tell you
an area is cut off, though. | It only says a mark was never drawn. ||| So play it through.
|| Beam down, and open Beam. | There's nowhere else to go. || Walk east, and take the
exit. | Now the gully is on the list. || Go down the stairs, | and you're standing by the
water. ||| For the exercise, stand a crate in the cistern, | and add a second way down.
||| Next time, these maps get things you can use. ||"