# C3-7 video script - Anatomy of a long away mission

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0 from
>   Steam or itch.io, with a current tool and libraries. The `away` template is new.
> - **A second mission for the class.** The student makes `MyAway` with
>   `sbs create MyAway -t away --title "Kesh Relay"`. `MyBoarding` is left as it is.
> - **Nothing is typed.** The lecture ends with the starter untouched. `example\` holds
>   the whole starter as `sbs create` makes it, for a student who cannot run the command.
> - **The starter's setting is kept** for the rest of the class: Kesh Relay, Old Marrow,
>   the sentry. Lectures 8 to 12 add two areas and a second way to the power cell.
> - **Dawnline is not on the student's computer** and the lecture does not need it. Its
>   numbers and one area header are quoted on the page.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The starter was built by copying the released template, with
> the two title lines rewritten the way `sbs create` writes them. `sbs create` and
> `sbs fetch` were NOT run: what they download and unpack was read from the tool's own
> code. Played headless with stand-in consoles (no `--exercise`): three aboard to the
> win, three aboard to the loss, and one helm officer alone. Then 16 one-change
> variants, each linted and played. No engine, no window.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | None. `MyAway` is made on camera in scene 2. Delete any old `MyAway` first |
| Internet | On, for scene 2 |
| VS Code | Open, with no folder |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 3 with a server, Science and Weapons |

## Confirm on camera

1. `sbs create MyAway -t away --title "Kesh Relay"` ends `MyAway is ready.` and makes a
   folder with a `ground` folder in it. (Read from the tool's code. NOT run.)
2. After `sbs fetch "MyAway" --update-libs` the folder
   `__lib__\media` holds the two Cosmos-Tiles packs, unpacked. (Read from code.)
3. Lint on the fresh mission prints the three lines on the page. (Lint.)
4. Beamed down, Dr Hale holds The Caretaker's Cough and Lt Reyes holds Clear the Yard;
   the handheld has eight apps: Crew, Act, Look, Pack, Tasks, Beam, Scan, Fire. (Mock.)
5. The route on the page wins in six presses, one stun, one shot, three pickups and one
   door, and the game ends with the `Win:` sentence. The other answer at the beacon ends
   it with the `Lose:` sentence. (Mock, by script.)
6. Every row of the page's tables. (Lint, Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. ANY screen of a tile map in the game: the map beside the handheld, a click walking a
   figure, a click on a person opening a scene, the Fire app's Arm button, the art.
2. The Boarding Party tile offering Kesh Relay, and BEAM DOWN, on this template.
3. `landing.tiles` opening in the Tile Map Editor, and the **Text** button.
4. The last screen's sentence, on this template.

> Driven by script, not by a person: beaming down (the button's two calls), every walk
> and every use (a map click on the thing's cell), every answer (the handheld's answer
> call), arming and the shot.

## Scenes

### 1. Cold open

**Screen:** A console on the ground at Kesh Relay: the map, a figure walking across the
yard toward a man by a tent. Then the same yard as sixteen lines of text.

**Say:** "So far your boarding party has read its way through rooms. || Today it walks
instead. ||| This is a yard, with a caretaker, a sentry and a locked door, | and every bit
of it is in four files you can read. || You'll make it with one command, | play it through
once, | and then take it apart. ||"

### 2. A second mission

**Screen:** The command prompt. Type the `sbs create` line; Enter at the question; the
last line. Then the fetch line. Then VS Code: open the folder, trust it. Lint: clean.

**Say:** "This half of the class gets a mission of its own. || Same command as before, |
with a different template after the dash t: away. ||| Press Enter at the question, | and
it tells you the mission is ready. || Then the fetch line, once, | to bring the libraries
up to date. || That second line matters more than usual here. | This mission has no
pictures of its own. | Its map is drawn with two art packs that missions share, | and that
line is what unpacks them. ||| Open the folder, trust it, and run lint, | and it comes
back clean. ||"

### 3. Play it to the win

**Screen:** `sbs run server,science,weapons -m MyAway map=0`. Both consoles beam down.
Science clicks the man by the tent; the scene; the medic's answer. The kit appears; pick
it up. Weapons: Fire, Arm, the sentry. The cell, the keycard, the door, the beacon.

**Say:** "A server and two consoles. | The ship starts beside the relay, so nobody has to
fly. || Handheld, Boarding Party, beam down. ||| And there's the difference: | a map, and
you on it. || Click the ground to walk. | Click a person, and you walk up and talk. ||
This is a room, exactly like the ones you've written: | buttons, and one of them only a
medic is offered. ||| He mentions a medical kit, | and now it's on the map, where a moment
ago it wasn't. || The sentry is the hard part. | From the weapons console I open Fire, |
arm it, and click the sentry. || It drops a power cell. | The keycard opens the door, |
the cell goes into the beacon, | and that's the game. ||"

### 4. Four files

**Screen:** VS Code, the file list. Open the `ground` folder. The table of four files from
the page.

**Say:** "Now look at the folder. || Nine files came with it, | and four of them are the
mission. ||| Two are in a folder called ground: the map itself, | and a short list of the
kinds of ground there are. || Then the fact sheet, | which holds everything else. || And
the story file, | where one line loads the ground | and one card opens the party. ||
There's no Python here, and you won't write any. ||"

### 5. What a map is

**Screen:** `landing.tiles` in the Tile Map Editor; press Text. Highlight the header, then
the legend, then the rows. Trace the pad, the tent, the relay house, the door.

**Say:** "Click the map file and you get a picture. | Next lecture is about that picture.
|| Today press Text, and read what's underneath. ||| It has three parts. || The header
says what this area is called, | and where someone who beams down stands. || The legend
says what each character means: | a dot is dust, | a capital W is wall. || And some lines
carry an at sign and a name. | That's called a mark. | It gives a cell a name, | so a
record can say, stand here. ||| Under three dashes is the map itself. | You can find the
pad, | the tent beside it, | and the relay house with its door. || Notice what isn't here.
| No caretaker, no sentry, no key. | Only the places they stand. ||"

### 6. What a record is

**Screen:** `mission.amd`. The table of seven sections. Then the keycard record: draw a
line from `Area:` to the map's `area:` line, and from `Mark:` to the legend. Then Old
Marrow, and his `Talk scene:` to the room.

**Say:** "The fact sheet has seven sections, | and four of them you've written before. ||
Three of them are new: | props, people and hostiles. ||| Here's one of the props. | A
heading, a fence, and a line of description. || Two fields put it on the map. | Area names
the map file. | Mark names a mark in that file's legend. || And one field says what it
does. | Item means you can pick it up. ||| A person is the same shape. | And this line is
a join you already know. | It's the key of a room. || So a room on the ground is the room
you've always written, | with one difference: nobody walks into it. | It belongs to the
thing or the person that opens it. ||"

### 7. One line, one card, and the ending

**Screen:** `story.mast`. Highlight the load line. Then the card; put Lecture 2's card
beside it. Circle the three words. Then the quest with `Win:` and `Lose:`, and the two
answers.

**Say:** "In the story file, one line loads the ground. | You never change it. | A new map
is found by itself. ||| And this is the card. || Put it beside the one from Lecture 2. |
The first room is gone, | because a map has no first room. | And there's a new word: | the
area to beam down into. || Three words here are yours. | The signal, the name on the tile,
and the area. ||| Last comes the ending. || This quest carries two sentences, | one for a
win and one for a loss. || And an answer at the beacon either completes that quest, or
fails it. | That's the whole ending. ||"

### 8. Dawnline, and your turn

**Screen:** The comparison table from the page. Then Dawnline's first area header, the
`exits:` block highlighted. Then the exercise.

**Say:** "The long example of all this is a mission called Dawnline. || It doesn't come
with the game, | and you don't need it. ||| Look at the numbers. | Six maps where you have
one. | Forty-two props where you have six. || But every row is the same kind of thing as
yours. ||| One thing its maps have that yours doesn't: | a way from one map to the next. |
You'll build that in two lectures' time. || For now, change three small things, | play
each one, and put them back. ||| Next time you draw a map of your own. ||"