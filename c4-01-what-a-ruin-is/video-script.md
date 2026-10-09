# C4-1 video script - What a ruin is

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **This lecture makes the mission the class is built in:** `MyRuin`, with
>   `sbs create MyRuin -t amd --title "The Hollow"` and
>   `sbs fetch "MyRuin" --update-libs`. Class 4 does not build on `MyMission`: Class 1's
>   story ends the game in ten minutes, and Classes 2, 3 and 5 may or may not have been
>   added to it.
> - **A look-and-read lecture.** The student pastes one block, flies it, reads it, and
>   deletes it again. The block is Storm's Beacon's `relics\sink.amd` cut down to what a
>   template mission can build: the ruin's record, two rooms, one solid and three places,
>   word for word, plus one line the shipped file does not have (`Loc:`).
> - **Storm's Beacon is never run.** The student does not need it installed. Everything
>   quoted from it is on the page. Do not start Storm's Beacon for this recording from a
>   folder whose saved games matter.
> - **`example\` holds one file, `mission.amd`: the mission WITH the borrowed ruin in it**
>   (118 lines), so the block can be copied from a file. The lecture ends with the block
>   deleted, so the hand-over to Lecture 2 is the untouched `sbs create` mission.

> **Measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`, library
> as packaged in `__lib__` (sbs_utils `ae2bbf4a`). `sbs create` was run for real. The
> borrowed block was pasted where the page says, linted, and played headless by a probe
> that asks the library what it built and moves the ship along the page's flight. Then 18
> one-change variants: the pasting mistakes, the shipped lines left in, and the exercise.
> No engine, no window. Nothing in this lecture has been seen on a screen.

The companion page is `lesson.md`; the file with the borrowed ruin is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Missions folder | No folder named `MyRuin` yet. It is made on camera in scene 2 |
| VS Code | Open, with no folder. The Artemis AMD add-on installed |
| Command prompt | Open in `data\missions`, cleared |
| The block | `example\mission.amd` open in a second window, lines 63 to 118 ready to copy |
| The shipped file | Storm's Beacon's `relics\sink.amd` open read-only for scene 6, or use the page's own excerpts |
| Game | Closed. Started on camera in scene 4 with a server and a Helm console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. If an item fails while recording, stop and fix the page.

1. `sbs create MyRuin -t amd --title "The Hollow"` ends `MyRuin is ready.` and makes
   seven files; `mission.amd` has 60 lines; lint is `clean`. A second `sbs create` with
   the same name says `already exists and is not empty`. (Run for real, with a throwaway
   name.)
2. With the block pasted at the end of the file, lint is `clean`. (Lint.)
3. The game builds one ruin, `sink`, at `6000, 0, 12000`: two box rooms, 732 rock objects
   (682 with the drift taken out), four purple cloud objects, and one name on the map,
   `The Sink`, at `1600, 0, 12000`. Both logs empty. (Mock.)
4. The three places start dark. The inlet mouth lights with the ship on it; the near side
   with the ship 1100 away; the far side with the ship 1200 away. Each is then a
   selectable gold contact with its name in small letters, as written. (Mock.)
5. With the block deleted again the file is the `sbs create` file, lint is `clean`, and
   the game makes no ruin. (Lint, Mock.)
6. Every row of "If something goes wrong", and the two slips at Stop 6. (Lint, Mock.)
7. The shipped ruin record left whole (with `Containment:`, `Scrape band:`, `Margin:` and
   `Forbid jump:`) lints `clean` and builds the same ruin; `Dress: ruins_cv_rubble` left
   on the drift lints `clean`, places nothing, and writes one line to
   `mast.runtime.log`; `Scene:` left on a place is `dangling-scene`. (Lint, Mock.)
8. The exercise: green makes four green cloud objects; the new `Loc:` moves the name to
   `1600, 0, 20000`; the smaller room gets the five warnings the page counts, the first
   of them the line printed there, and the game still builds both rooms. (Lint, Mock.)
9. Every excerpt in Stop 5 is copied from Storm's Beacon's `relics\sink.amd` as it stood
   on 2026-10-08 (348 lines). The two quest steps that send a crew to The Sink are in
   `stormsbeacon.amd` (`sink_go`, `sink_dive`). (Read, not run.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. All of scene 4. The Sink has never been flown, in the mock or in the engine: the probe
   moved the ship. In particular: what a box room 5200 across looks like from inside in
   rock, whether the far wall can be seen at all, how thick the haze is with four clouds,
   and what the drift looks like as 50 rocks.
2. The name **The Sink** on Helm's map. Lecture 2's ruin was seen there, drawn in blue.
3. The three places turning into contacts, and their small-letter names on the map.
4. The game starting the map without a stall. It makes 739 objects, more than any other
   lecture in this class.
5. Whether Storm's Beacon is in a student's install. The page says the student does not
   need it, and quotes everything it uses.

> If the big room reads badly on camera (too dark, too empty), say so in the voice-over
> rather than changing the block: it is the shipped ruin's own shape.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. Helm's map with a named place past the hulk. Cut to the main screen:
purple haze and rock. Cut to a text file, fifty lines long.

**Say:** "This is a ruin. || It's a place a ship can fly inside, | and it's older than
anyone who could have built it. || Nobody modeled it in a drawing program. ||| It's this:
about fifty lines of text. || In this class, you write one of your own. | Today, you fly
one that somebody else wrote, | and then you read how it was made. ||"

### 2. A mission for this class

**Screen:** Command prompt. Type the create line, press Enter at the question. Type the
fetch line. Open the `MyRuin` folder in VS Code and trust it. `sbs lint MyRuin`: clean.

**Say:** "First, a new mission. || This class doesn't build on the one from Class 1. |
That story ends the game ten minutes in, | and a ruin takes longer than that to fly. || So
I make a mission the way I did in Class 1, and I call it My Ruin. ||| Then I bring its
libraries up to date, | open the folder in the editor, and run lint. || It's clean, and
it's the same small mission you started Class 1 with. ||"

### 3. Borrow a ruin

**Screen:** `mission.amd`, the end of the file. Two blank lines. Paste the block from the
page. Scroll through it slowly. Save. Lint: clean.

**Say:** "There's a shipped campaign that's built out of ruins, | and one of its smallest
is called The Sink. || It's one enormous flooded room, with a hole in one end. ||| I go to
the very end of my file, | and I paste a cut-down copy of it. || Don't read it yet. | Just
save, and run lint, and it's clean. || One line in there isn't in the shipped file, | and
that's the line that says where the ruin stands. ||"

### 4. Fly it

**Screen:** Command prompt: `sbs run server,helm -m MyRuin map=0`. Helm's map: find The
Sink. Fly to the name. Fly down the inlet into the big room. Fly round the drift to the
far side.

**Say:** "I start the game with a server and a Helm console. || And there on the map,
past the hulk and off to one side, is The Sink. || The name sits at the mouth of the way
in, so that's where I fly. ||| Now I'm in the inlet, a long narrow room, | and there's the
haze. || And here it opens out, into a room five thousand across. ||| There's a mass
hanging in the middle of it. | I fly round that, | and I'm on the far side. || Notice the
names that turned up on the map as I came near. | Those are places, and you'll write
those too. ||"

### 5. Read what you pasted

**Screen:** `mission.amd`, the pasted block. Highlight each record's deciding line in
turn: no `Relic:` line on The Sink, `Box:` twice, `Solid:`, `Point:` three times. Then
highlight `Relic: sink` on every record.

**Say:** "Now let's read it, as a list. || It's one section, with seven records in it. ||
The first record is the ruin itself. || The next two say Box, and each of those is a room
with flat sides. || This one says Solid, and it's the mass in the middle, | which takes
space away. || And these three say Point, and each one is a named place. ||| Now look at
what every record but the first has in common. | It says Relic, and then sink, | which is
the ruin's key. || That's how a room says which ruin it belongs to. ||| And notice what
isn't here. | Nobody wrote a wall. || The file says where the open space is, | and the
game puts rock around it. ||"

### 6. Read the rest of the file

**Screen:** The shipped `sink.amd`, or the page's excerpts. Scroll: a place with `Scene:`
and `Scan:`, the scene it names, a place with `Item:`, the item, the hidden place, a side
story with `For:`, a cutscene shot. Then the "What was cut, and why" table.

**Say:** "The shipped file is about three hundred and fifty lines, | and I pasted fifty
or so. || The rest is what this class teaches. ||| Here, a place has a scene, | a
conversation of the kind you wrote in Class 2. || Here, a place holds a thing the crew can
find. || This place is hidden, until somebody hears it from across the room. || This is a
small story for one member of the crew. | And this is what the main screen shows as the
ship arrives. ||| Most of that isn't for the ship at all. | It's for people who leave the
ship in suits, | and that comes late in this class. || So I cut it, | and the table on the
page says what went and why. ||"

### 7. Give it back

**Screen:** `mission.amd`. Select from `## [Relics](relics)` to the end of the file.
Delete. Save. Lint: clean. Show the status bar: 60 lines.

**Say:** "The Sink was a loan, so now I give it back. || I select everything from the
Relics heading to the end of the file, | and I delete it. || I save, I run lint, and it's
clean. ||| The file is sixty lines long again, | and that's where the next lecture starts.
||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Before you delete it, play with it. || Change the color of the haze. | Move the
whole ruin somewhere else, and find it again. || Make the big room smaller, | and read
what lint tells you about that. ||| Then put the game away, | and answer three questions
from the file alone. ||| Next time, you write a ruin of your own, | starting from an empty
page. ||"
