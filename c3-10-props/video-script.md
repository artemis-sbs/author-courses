# C3-10 video script - Props

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 9's finished files** in `MyAway`. Two files change:
>   `mission.amd` (eight props, three rooms) and `ground\cistern.tiles` (three marks).
>   `example\` holds those two.
> - **No MAST at all.** `Opens with: signal` and `Hidden until:` are heard by the
>   library itself. The signal is sent by an answer in a room.
> - **Lint does not read a door.** `Opens with:`, `Item:`, `Needs:` and `Hidden until:`
>   are not checked against anything. The page says so, and gives a pencil check.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The eight steps were typed in order and linted at each one.
> The finished files were played headless with two stand-in consoles: the key, the door,
> the toolbox, the notice twice, the panel refused and used, the gauge, the gate, the
> lever, the cell. A door check was played with the die fixed, to pass and to fail. Then
> 22 one-change variants, each linted, and the ones lint is silent about played with the
> stand-in put beside the thing by the probe. No engine, no window.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 9's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` at the end of the Props section; `cistern.tiles` in a second tab |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 8 with a server, Engineering and Science |

## Confirm on camera

1. Lint is `clean` after Steps 1 to 5, prints the `signal-no-route` warning on the page
   after Step 6, and is `clean` again after Step 7. (Lint.)
2. The door opens for the engineer while the doctor carries the key, with the words
   `pump key fits`. (Mock.)
3. A check that makes its number says `Chief Okoro - engineering 4, rolled 4: 8 vs 8,
   success.`; one that does not says `failure.`, and the next click rolls again. (Mock,
   the die fixed by the probe.)
4. The toolbox puts two fuses in a pack. The notice opens its room once; the second
   click gives its description. (Mock.)
5. The panel tells the doctor `You would need engineering for that.` (Mock.)
6. The gauge is read from the walkway, two cells away. The gate says `will not open from
   here`. After the lever, the gate is open and the cell is on the map at 16, 2. (Mock.)
7. Every row of the page's tables. (Lint, Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. A door's picture changing when it opens.
2. The Pack app's list, and how a count is written.
3. The Scan app's words for a prop.
4. Where on the handheld the words `pump key fits` appear.
5. The three + Entry forms and paint clicks in `cistern.tiles` (read from the add-on's
   source, as in Lecture 8).

## Scenes

### 1. Cold open

**Screen:** The pump house door, shut. A figure walks up to it; it opens. Inside, a panel.
Below, a gate across a walkway, and water.

**Say:** "Your maps have places on them. || Today they get things: | a locked door and its
key, | hung on a tent peg, | and a panel only an engineer may touch. ||| Every one of them
is a few lines in the fact sheet, | and what a thing does depends on which lines it has.
||"

### 2. What a prop does

**Screen:** The table of four questions from the page. Then the first record typed: the
pump house key. Highlight `Item:`.

**Say:** "When somebody clicks a prop, | the game asks four questions in order. || May
this person use it at all? || Is it a door, and shut? || Is it something to pick up? ||
Does it open a scene? ||| It stops at the first yes. | And if there's no yes at all, | it
shows the description. ||| So here's the simplest prop there is. | One line says Item, |
and a name I made up. || Click it, and it's in your pack and off the map. ||"

### 3. A door

**Screen:** Type the pump house door. Highlight `Blocks: yes`, then `Opens with:`. The
table of four terms.

**Say:** "Now the door, on the mark you painted two lectures ago. || Blocks, and then yes,
| means nobody walks through it while it's shut. || And Opens with lists the ways it
opens, | with commas between them. ||| A key opens it when anybody in the party is
carrying one, | not just the one at the door. || A check is a roll: | a ten sided die,
plus a skill, against a number. || And cut means a shot from the weapon. ||| Two warnings
about checks. || Write the key first, | because the terms are tried in order. || And a
check can be tried again at once, | so a door with a check on it will always open in the
end. ||"

### 4. Two more pickups, and a notice

**Screen:** Type the toolbox; highlight `Qty: 2`. Type the notice; highlight `Scene:` and
`Once: yes`.

**Say:** "The toolbox is a pickup worth two. | That's the line that says Qty. ||| The
notice opens a scene. | Scene, and the key of a room, | the same join you saw on the
starter's terminal. || And it has one more line: | Once, and then yes. || The room opens
the first time, | and after that a click only shows the description. ||| Be careful with
that one. | It counts the room opening, | not what anyone answered. ||"

### 5. A terminal with a Needs

**Screen:** Type the pump panel. Highlight `Needs: engineering`, then `Scan:`.

**Say:** "The pump panel is a terminal too, | with one new line. || Needs, and a job. |||
Anyone else who clicks it is told they'd need engineering, | and gets nothing more. ||
That's stricter than a choice in a room. | A choice for a missing job gets covered by
somebody else. | Nobody covers for a Needs. ||| So never put the only way through your
story behind one. || Scan is the simple one. | It's what the scanner says about the thing,
| when a crew member can see it. ||"

### 6. Their rooms, and a true warning

**Screen:** The end of the file: type the three rooms. Save; lint. The one warning.

**Say:** "Three short rooms at the end of the file. | You know how to write these. || The
notice teaches a fact. || And the lever's answer sends a signal. ||| Lint warns that
nothing hears that signal. | That's true for the moment. | The next step is what hears it.
||"

### 7. A gate, a hidden cell and a gauge

**Screen:** `cistern.tiles`: three + Entry forms and three painted cells. Then
`mission.amd`: type the sluice gate, the spare cell and the gauge. Lint: clean.

**Say:** "Three marks in the cistern first, | one new legend line and one click each. |||
The sluice gate is a door with only one way to open. | Opens with, signal, and a name. ||
Nobody on the ground can force it. || The spare cell says Hidden until, | and the same
name. | It isn't on the map at all until that signal is sent. ||| So one answer in the
pump house does two things downstairs. | It opens the gate, | and it uncovers the cell.
||| The gauge stands out in the water. | Reach, and the number two, | lets a crew member
use it from two cells away. ||| And lint is clean again, | because something hears the
signal now. ||"

### 8. What lint can't see, and play it

**Screen:** The second table on the page. Then the game: the key, the door, the notice
twice, the panel as the doctor and as the engineer, the lever, the gate.

**Say:** "A warning before you play. || Lint doesn't read a door. || Misspell the key's
name, or the signal's, | and it says clean, | and the door never opens. ||| So check doors
with a pencil. | For each way a door opens, | write down where that key or that signal
comes from. ||| Then play it with two consoles. || The doctor carries the key, | and the
engineer opens the door. || The doctor can't work the panel, and the engineer can. ||| For
the exercise, add a second key somewhere it can never be reached, | and say why that's a
mistake. ||| Next time, somebody to talk to, | and something that bites. ||"