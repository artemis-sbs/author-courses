# C3-8 video script - The Tile Map Editor, part 1

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries, and the VS Code add-on 0.9.4.
> - **Starts from Lecture 7's untouched starter** in `MyAway`. One new file is made:
>   `ground\gully.tiles`. `example\` holds that file and nothing else.
> - **The file is the ground truth.** Every step is given as text to type, and the
>   editor's way is given beside it. The student must end with the exact file at the end
>   of Step 6, because later lectures place things on it by cell numbers.
> - **THE EDITOR HAS NOT BEEN SEEN.** Nobody on the project has described this screen
>   from life. Every button name, every label and every behavior on the page was read
>   from the add-on's source (`media\tilesEditor.js`, `media\tilesModel.js`, the editor's
>   page in `src\extension.ts`) and its two help pages. Check each one against the real
>   editor before recording. The list is below.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The four steps of the file were typed in order and linted at
> each one. The finished file was played headless with a stand-in console: the Beam
> app's own button into the gully, three map clicks, and back. Then 27 one-change
> variants, each linted, and the ones lint has nothing to say about played. No engine,
> no window, no VS Code.

The companion page is `lesson.md`; the finished file is in `example\ground\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` as Lecture 7 left it. Lint clean. No `ground\gully.tiles` |
| VS Code | `MyAway` folder open and trusted, the file list showing, `ground` opened |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 8 with a server and Engineering |

## Confirm on camera

1. After Step 2, lint is `clean` and does not name the new file. After Steps 4, 5 and 6
   it is still `clean`. (Lint.)
2. Beamed down, the Beam app's button puts the stand-in at cell 2, 5 of the gully, with
   the words `Energizing - The Dry Gully.`; a click at 14, 5 walks in through the gap;
   a click on the wall at 12, 3 stops beside it at 11, 3. (Mock, by script.)
3. Every row of the page's two tables. (Lint, Mock.)

Read from the add-on's source, NOT seen. If one is not as described, stop and fix the
page:

1. A new `.tiles` file opens in the Tile Map Editor, and an empty one shows the words
   `No map yet.`
2. The toolbar: Paint, Rect, Fill, Pick, Entry, Move, Kinds, Art, `-`, `+`, Grid, Marks,
   Chars, Things, Face S, two boxes and Resize, Refresh, Text, and the word
   Experimental.
3. **Text** opens the plain text; the button back is on the text editor's title bar and
   its tip reads `Open in Tile Map / Tileset Editor (experimental)`.
4. **+ Entry** opens a form with Kind, Mark (optional) and Character, OK and Cancel; the
   new row is selected afterwards; it writes one legend line after the last one.
5. A paint stroke rewrites only the map rows it changed.
6. The bottom line reads `0, 0  cliff  blocks, see` over the top left cell, and shows
   the area's name and size and the art sets found.
7. Kinds hatches what cannot be walked; Art draws with the packs; `A` switches.
8. The **Entry** tool writes `entry: x, y`, not a mark's name; a green star marks the
   entry.
9. The Problems list, the red corner on a cell, and magenta for a character that is not
   in the legend.
10. The right mouse button erases to nothing. Ctrl+Z undoes a stroke.
11. The Beam app on the handheld, and its button `To The Dry Gully`.

## Scenes

### 1. Cold open

**Screen:** The finished gully in the Tile Map Editor, Art view. Then the same file as
text. Then a figure walking through the gap in the pump house wall.

**Say:** "This is a map you'll draw today: | a dry gully, with a pump house in the middle
of it. || And this is the same map as the game reads it. | Twenty-eight lines of text. |||
You can paint it with the mouse, or type it, | and it's the same file either way. ||"

### 2. A new file, and the header

**Screen:** VS Code. Right-click `ground`, New File, `gully.tiles`. The empty editor.
Press Text. Type the comment line and the four header lines.

**Say:** "Right-click the ground folder, new file, | and call it gully dot tiles. || It
opens in the Tile Map Editor, | and there's nothing to draw yet, | so press the Text
button. ||| The top of an area file is its header. || Area is the key, | the name the rest
of your mission knows it by. || Title is what the crew sees. || Tileset names the file
that lists the kinds of ground. || And size is how many cells across, | then a small x,
and how many down. ||"

### 3. The legend and the ground

**Screen:** Type `legend:` and its six lines, the three dashes, and the twelve rows. Save.
Lint: clean. Hover over a row to count twenty-four.

**Say:** "Next comes the legend. || Each line is one character, a colon, | and a kind of
ground from the tileset. || A dot is dust. | A capital W is wall. ||| Then a line of three
dashes, | and under them the map itself, | one character for each cell. || There are
twelve rows, | and each one is twenty-four characters long. ||| Save it, and run lint. ||
It comes back clean. | And notice that lint doesn't mention the new file at all. | It only
speaks up about a map when something's wrong with it. ||"

### 4. Look at it

**Screen:** The title-bar button back to the editor. Kinds, then Art. Move the mouse along
a row, the bottom line changing. Stop on the west wall of the pump house.

**Say:** "Now go back to the picture, | with this button at the top of the text. ||| Two
ways to look. || Kinds colors each cell by what it is, | and hatches the ones nobody can
walk on. || Art draws it the way the game will. ||| Move the mouse over it, | and the
bottom line tells you which cell you're over, | and what it is. || And look at the pump
house. | It's a box with no way in. ||"

### 5. A door

**Screen:** Press + Entry. Fill in floor, pump_door, D. OK. Paint. Click cell 12, 5. Press
Text: the new legend line, and the one changed character.

**Say:** "A door on a map is two things. || It's a cell you can walk through, | in a wall
you can't. || And it's a mark, | so that later a real door can be stood on it. ||| Plus
Entry gives me a new legend line. | The kind is floor, | the mark is pump door, | and the
character is a capital D. || Then I paint one cell with it, | in the middle of the west
wall. ||| Press Text, and look at what the editor wrote. || One new line in the legend, |
and one changed character in the map. | Nothing else was touched. ||"

### 6. A mark to arrive on, and the entry

**Screen:** + Entry again: dust, arrive, a. Paint cell 2, 5. Then Text: type `entry:
arrive` under `tileset:`. Back in the editor, the star on the cell.

**Say:** "The party needs somewhere to stand when it beams down. || So I make a second
mark the same way, | on open ground at the west end. ||| The mark gives that cell a name,
| and it's still dust. || Then one more line in the header. | Entry, and the name of the
mark. ||| The editor has a tool for this as well, | and it writes the cell's numbers. ||
Both of them work. | The name is better, | because it still points at the right place
after you redraw the map. ||"

### 7. Lint, and what it can't see

**Screen:** The command prompt: lint, clean. Misspell `arrive` in the entry line; lint;
undo. Type a small w into a wall; lint; undo. Then the second table on the page.

**Say:** "Lint reads your maps along with everything else. || Misspell the entry line, |
and it tells you the name is neither a mark nor a cell. || Type a letter that isn't in the
legend, | and it tells you the whole area won't load. ||| But there are things it can't
see. || Give two areas the same key, | and it says nothing at all. || Draw a row longer
than the size line says, | and the extra cells are quietly cut off. || So compare your
file with the page, one character at a time. ||"

### 8. Play it, and your turn

**Screen:** `sbs run server,engineering -m MyAway map=0`. Beam down. The Beam app: To The
Dry Gully. Walk into the pump house. Click a wall. Then the exercise.

**Say:** "Nothing in the mission leads to the gully yet. || But the ship's transporter can
put you there. ||| Beam down as usual, | then open Beam on the handheld. | There's one
other place on the list, and it's yours. || You're standing on your own mark. || Click
inside the pump house, | and you walk in through the gap you painted. ||| For the
exercise, try the other tools. | Draw a second building with the rectangle, | then break
the file on purpose and read what lint says. ||| Next time, you join this map to the yard.
||"