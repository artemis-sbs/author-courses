# C4-2 video script - A ruin is a place

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | A mission from `sbs create -t amd`, lint clean. The Class 1 mission will do; nothing from Classes 2 or 3 is needed |
| Library | sbs_utils `f8b368ea` or later (the one with `relics_spawn`), released 2026-10-03. The mistake tables were measured at `d264bbc3` |
| Template | A `story.mast` with the `relics_spawn` line. On 2026-10-03 that template change is committed in the starter repo and NOT pushed, so a mission from `sbs create` needs the one line pasted first (the note in Step 6) |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, `story.mast` in another. AMD extension 0.9.3 or later (the one with **Artemis AMD: Show Relic Plan**) |
| Mouse | One with a middle button, if the scene 6 orbit is wanted. The Top, Front and Right buttons do not need one |
| Game | Closed. Started on camera in scene 9 with a server and a Helm console |

## Confirm on camera

Nobody has looked at any screen in this lesson. This is what was checked, and how.

**By script, in the mock, with the lesson's own files (headless run, 2026-10-03):**

- After the map starts, the ruin `hollow` is registered at `0, 0, 20000` with 3 chambers
  and 2 passages, and the space is in one joined piece.
- 534 rock props stand around the three rooms, between x -959 and 4183, y -1170 and 1161,
  z 18839 and 23529. Their middle distance from the wall is 54. About 60 of them are loose
  rock inside the rooms.
- A map marker named `The Hollow` exists at `0, 0, 20000`. The ship starts 22309 from it.
- Nothing starts containment. A ship parked on a wall prop for eight seconds was not
  pushed off it, and no collision was reported.
- Every row of both mistake tables in the lesson: by `sbs lint`, and by running the
  library on the broken file.

**By running the extension's own code outside VS Code (node), on the lesson's file:**

- The plan reads one relic, three chambers and two passages.
- The page it generates carries the labels `The Mouth`, `The Nave`, `The Vault`, the hover
  texts `The Mouth r900` and `nave - mouth: 3000u`, and the buttons Fit, Add chamber, Add
  box, Add solid, Add point, Add barrier, Rails, Delete, Top, Front, Right, Undo, Preview,
  Live.
- Changing a radius through the panel's own edit function rewrites exactly one line of the
  file.
- With no relic in the front tab the page reads `No relic in this file.`

**In the real engine (2026-10-03, sbs_utils `9a8fa4f5`, server and a Helm console):**

- By script, with the one `relics_spawn` line: `hollow` registered with 3 chambers and 2 passages in one
  piece; 534 wall props; no containment. A ship parked in The Mouth did not drift, and a
  ship put on a wall prop was not pushed off it and reported no collision.
- SEEN, one screenshot each, with the ship parked in The Mouth by the probe:
    - Helm's map draws the ruin. The wall props are tan rock blips; the two lobes of The
      Mouth and The Nave and the neck of the passage between them read as a floor plan.
      The marker **The Hollow** is drawn in blue with its name, at the middle of The
      Mouth. So item 5 below is answered for Helm.
    - The main view from inside The Mouth: asteroid-sized rocks all around the ship,
      spaced well apart, with open sky between them. It reads as a rock field, not as a
      wall. Item 6 is answered for the inside; the outside has not been looked at.
- With containment turned on by hand (not what the template does), a ship that tried to leave
  through the wall was held. That is build item B42, and it is why this lesson leaves
  containment off.

**Not seen by anyone. If one is not as described, stop and fix the page.**

1. The Relic Plan panel itself: that the command is in the palette under that name, that
   the panel opens beside the file, and what the three rooms look like in it.
2. That the panel opens tilted and **Top** gives a plan. This is what the code sets up.
3. Hovering a room shows `The Mouth r900`. The text is in the page; a tooltip has not been
   seen.
4. Clicking a room opens the numbers box at the bottom right; typing `800` in `r` and
   pressing Enter changes the file; the panel's **Undo** puts it back.
5. The marker **The Hollow** on Helm's map. It is a nav point. Which consoles draw nav
   points has not been checked.
6. The rock: that it is there, from how far away it starts to draw, and what three rooms
   made of 534 asteroids look like from outside and from inside.
7. The ship passes through the rock with no bump and no damage. The props are made
   non-solid by the library; the engine has not been watched doing it.
8. A helm officer can get a light cruiser down a passage 700 across.
9. The game does not stall while 534 props are made at the start of the map.

**Keep these off camera.** Each is a defect or a gap reported from this pilot.

- **Add chamber** (and the other Add buttons) puts the new record above the last room's
  note, so the note ends up under the new room.
- **Preview** and **Live**: the library now moves the rock with the space (checked by
  a unit test, 2026-10-03). Not watched in a running game. Leave them for a later lecture.
- Walls that hold: a ship that has been inside a ruin with containment on cannot fly out
  again (seen in the mock and by script in the real engine). The template does not turn
  containment on.

Fixed since the first draft, so no longer a thing to avoid: SHIFT-drag from or to a box
writes a `Passage to:` line, and a passage may now end on a box.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The Relic Plan, top view, three rooms and two passages. Cut to the game: the
marker on Helm's map, then rock all round the ship.

**Say:** "This is a ruin. Three rooms, two tunnels, older than anyone who could have built
it. I did not model it and I did not place a single rock. I wrote down where the empty
space is. Today you write yours."

### 2. Space, not walls (0:45 - 2:15)

**Screen:** The table from Step 1 of the companion page.

**Say:** "A ruin is hollow, so you describe the hollow. A chamber is a ball of open space:
a room. A passage is a tube of open space between two chambers: a tunnel. A box is a block
with flat sides: a built room, and you will add one yourself at the end. Whatever you do
not describe is wall."

### 3. The ruin itself (2:15 - 4:30)

**Screen:** `mission.amd`, the end of the file. Type the `## [Relics](relics)` heading and
The Hollow.

**Say:** "A new section, and its key has to be the word `relics`. Then the ruin: a name
for people, a key for the file. And one field. `Loc` is where it stands: across, height,
along. The station is at zero, zero, zero. The hulk is nine thousand along. So this is past
the hulk, on the same line. The sentence underneath is a note to myself. No player ever
reads it."

### 4. The first room (4:30 - 6:30)

**Screen:** Type The Mouth.

**Say:** "Three hashes again, the same as the ruin. Not four. A room is not written inside
the ruin; it is written beside it, and this line says whose it is. `Relic: hollow`. The
key, not the name. Then `Chamber`, four numbers. The first three say where, measured from
the ruin, so zero zero zero is the ruin's own spot. The fourth is the radius. Nine hundred,
so eighteen hundred across. My ship is about a hundred."

### 5. Two more rooms and the tunnels (6:30 - 9:00)

**Screen:** Type The Nave and The Vault.

**Say:** "The Nave is three thousand to one side, and bigger. And it has a passage: to
`mouth`, radius three fifty. That is the tunnel. I write it once, on either room. The Vault
is twenty-eight hundred further along from the Nave, with a passage back to it. So the ruin
turns a corner. Keep neighbours within about thirty-five hundred of each other."

### 6. Look at it (9:00 - 12:00)

**Screen:** `mission.amd` in front. Command palette, `Relic Plan`, **Artemis AMD: Show
Relic Plan**. Press **Top**. Hover a room, hover a passage. Click The Vault, type `800` in
`r`, show the line change in the file, press **Undo**.

**Say:** "With the file in front: Control Shift P, Relic Plan. There it is, drawn from the
file, and the game is not even running. Top looks straight down. Each square is a thousand.
Hover a room for its size; hover a tunnel for its length. Now click the Vault and make it
eight hundred. Look at the file: one line changed. The picture and the file are the same
thing. Undo, and it is back."

### 7. Nothing to paste (12:00 - 13:00)

**Screen:** `story.mast`, scrolled to the `relics_spawn` line. Highlight it. Do not edit.

**Say:** "The file says what the ruin is. And this line, which was in your mission from the
day you made it, builds every ruin the file holds: the space, the rock around it, whatever
is inside, and its name on the map. You do not touch it. No ruin in the file, and it does
nothing."

### 8. Lint (13:00 - 16:00)

**Screen:** Terminal: `sbs lint MyMission`, clean. Change `nave` to `crypt` in the Vault's
passage, lint, read the warning, undo. Then put a fourth hash on The Vault, lint: a
warning that says to give the heading three hashes. Show the plan still drawing three
rooms. Undo. Then delete the `Loc:` line, lint: clean. Undo.

**Say:** "Lint. Clean. A passage to a room that does not exist: it tells me, by name. Fix
that one, because with it the game builds no ruin at all. Now a fourth hash on the Vault.
The plan still shows three rooms. Lint is not fooled: this room is nested under the one
above it, and the game will not read it. Three hashes on the ruin, three on every room.
One thing lint cannot see. Take the Loc line away, and lint is clean, because it cannot
know where you meant. The ruin would be built on top of the station. Keep the line."

### 9. Play it (16:00 - 17:30)

**Screen:** Server and Helm. Helm's map: the marker past the hulk. Fly to it. Rock around
the ship. Through the passage to The Nave.

**Say:** "Past the hulk: The Hollow. That marker is the middle of the Mouth. And this is
my wall. It is scenery today; it will not stop me. Through the tunnel, and this is the
Nave."

### 10. Your turn (17:30 - 18:30)

**Screen:** The exercise on the companion page.

**Say:** "Add a fourth room, and make it a box: a built room with flat walls. Join it by
overlapping the room next to it. Then move it away, watch lint tell you the ruin is in two
pieces, and join it again with a passage. Next time we decide what these walls are made
of."
