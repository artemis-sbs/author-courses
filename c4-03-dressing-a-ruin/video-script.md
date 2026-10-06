# C4-3 video script - Dressing a ruin

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 2 mission, lint clean: The Hollow with The Mouth, The Nave and The Vault. The Gallery from Lecture 2's exercise may or may not be there; scene 2 adds it |
| Files touched | `mission.amd` only |
| Template | `story.mast` MUST contain `relics_spawn(get_mission_dir_filename("mission.amd"))`. The template has it since the starter repo's 2026-10-03 change, committed and NOT yet pushed, so a mission from `sbs create` today needs the line pasted (Lecture 2, Step 6). `example\story.mast` is the current template |
| Library | Measured on the sbs_utils working tree at commit `70e4d939`, 2026-10-03, with `--use-working-tree`. The finished file was run once more at `2552ea02`, with the same result. NOT checked on the released v1.4.0. Run the finished mission once on the library a student will download |
| Art pack | None. The lesson uses only art that ships with the game. Do not pin the `ruins` pack for this recording |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 10 with a server, a Helm console and a main screen. A Science console too, if the gold contacts are to be selected |

## Confirm on camera

Nobody has looked at any screen in this lesson. This is what was checked, and how.

**By script, in the mock, with the lesson's own files (headless run, 2026-10-03, sbs_utils
`70e4d939`).** A probe counted the objects the game made, by the role each one wears.

- The finished file: lint `clean`, `sbs compile` prints nothing, the run passes with labels
  59 of 424, and `mast.runtime.log` is empty.
- The ruin builds with 3 chambers, 1 box and 3 passages. 453 scenery objects: 67
  `generic-cube` pieces round The Gallery, 1 `generic-torus`, 355 asteroids round the
  other rooms and passages, and 30 loose rocks. 62 of the rocks nearest The Vault are `plain_asteroid_9`.
- `Walls:` on the whole ruin, default dials, no ring: `rock` 448 pieces, `plates` 373,
  `blocks` 373, `ribs` 373 and 14 bars (all 14 in The Gallery), `none` 0. Each plus 60
  loose rocks.
- `Seed: 12` gave the same layout on four runs, including runs started with a different
  runner seed. `Seed: 7` and no `Seed:` line gave one other layout, the same as each other.
- `Debris:` 0, 30, none written, 200 made 423, 453, 483 and 623 objects.
- `Gaps:` 0, none written, 0.2, 0.5, 1 left 82, 77, 67, 41 and 0 pieces in The Gallery.
  The round rooms did not change. `Plate:` 200, 400, 800 made 204, 50 and 16 pieces
  there.
- `Atmosphere:` made exactly 1 nebula object, in the color written, for each of the seven
  colors. `none`, and no line, made none.
- The ring: one `generic-torus` at `1400, 0, 20000`, scale 4 on all three axes, its own
  forward axis pointing along `+x`, toward The Nave. `Facing: mouth` turned it to `-x`.
- The map marker named `The Hollow` is at `0, 0, 19300`. Without an `entrance` point it is
  at `0, 0, 20000`.
- Three invisible markers stand at the three points, each wearing its role. A ship put on
  The Altar's point turned that marker selectable and gold; the other two stayed dark.
  Put on The Niche's point, that one turned too, and The Niche joined the list of places a
  suited crew can be sent.
- Every row of both mistake tables in the lesson: by `sbs lint`, then by a headless run of
  the broken file.
- The exercise, as written: lint clean, run passes.

**By reading the code, not by measuring.**

- A marker lights when a ship is within 1200 of it (`RELIC_REVEAL_RANGE`). The probe only
  ever put the ship exactly on the point.
- The ring is 210 across at size 1. That is the number the library holds for the mesh
  (`volume_dress.py`); the mesh itself was not measured.
- A passage always wears the ruin's `Walls:`. Its name inside the library is `nave>mouth`,
  which no record can spell.
- Every piece of scenery is made non-solid and cannot be selected.
- What each style does to a round room: `plates` and `blocks` lay the same piece round
  it, thin or thick; `ribs` stretches the plate piece into bars. The probe counted the
  pieces and read which art each one uses. It cannot see a shape.
- The Relic Plan draws points (a small disc with a ring: one color for an entrance,
  another for a hidden place) and has no code for a `Prop:`.

**With the art pack, in the mock only** (the pack was already on this machine; `sbs fetch`
was not run). With the pack pinned in `story.json`, `EXTRA_SHIP_DATA: true` in
`settings.yaml` and `volume_kit_load("ruins")` at the top of `story.mast`:
`Walls: torgoth, plates` built 263 kit pieces round the three round rooms and passages,
and `Dress: ruins_tg_gate 1.6, generic-torus 4` placed `ruins_tg_gate` at scale 12.8.
With any one of the three missing, the same file built plates and the plain ring.

**Not seen by anyone. If one is not as described, stop and fix the page.**

1. What `rock`, `plates`, `blocks` and `ribs` look like, from inside and from outside. The
   lesson says cave, hull plating, masonry, bored shaft. Those words are the library
   documentation's.
2. That the flat pieces are plain grey. The lesson says "flat grey blocks".
3. Holes in The Gallery's walls at `Gaps: 0.2`, and that they read as damage.
4. The Vault looking any different from the other rock rooms with one asteroid shape.
5. The cloud: that it is purple, that it fills the ruin, and that the walls can still be
   seen through it. The library documentation says the game limits warp speed inside a
   nebula. The lesson does not claim it. Try it and say what happens.
6. The ring: that it is a hoop, that it stands across the tunnel and not along it, that it
   is big enough to fly through, and that the ship passes through it with no bump.
7. The ruin's name on Helm's map at the way in. Lecture 2 saw the name drawn at the middle
   of The Mouth; the new spot has not been seen.
8. The gold contact: which consoles draw it, whether its name is shown, whether it can be
   selected, and that nothing is drawn on the main screen there.
9. The contact appearing as the ship comes up the tunnel to The Vault, at about 1200 out.
10. The Relic Plan with three points on it and no ring.
11. The game starting the map without a stall. It makes 453 objects, fewer than
    Lecture 2's 534.

**Changed since this script was written (2026-10-04, library `feeedf1b`).** The page's
Step 8 was re-measured on 127 variants and rewritten. Re-cut scene 9 to match:

- `Atmosphere: Purple` is purple. A word that is not a color makes no cloud, lint names it
  (`relic-unknown-atmosphere`) and the game writes a line in `mast.runtime.log`.
- A misspelled style gets "did you mean `plates`?" (`relic-walls-word`).
- `Dress:` on a room, a dial on a room, a line below the closing `---`, a `Facing:` that
  names nothing and a point in the rock are all named by lint now.
- A misspelled `Art:` or `Dress:` KEY still lints clean from the command line. The game
  says so in `mast.runtime.log`. That is the example to show for "lint is not the last
  check".
- `Plate: 20` is clamped to 150 (740 pieces, not 20,092). Still do not type it on camera.

**Checked in the real engine:** the same 453 wall pieces and layout as the mock, the purple
cloud, the three places and their gold contacts by script; the cloud on the main screen and
the ruin's name on Science were seen. **Not seen close up:** plates, blocks, ribs, the
ring, and which consoles draw a place's name.

**Keep off camera.** Kits. Nothing in this recording should load the art pack.

## Scenes

### 1. Cold open (0:00 - 0:45)

**Screen:** The game. The ship inside The Nave: haze, rock, the ring behind, the block
walls of The Gallery off to one side. Cut to `mission.amd` at the Relics section.

**Say:** "Last time this was three balls of rock. Today it is a cave with a hall somebody
built in it, a haze, a gate, and places with names. I did not model any of it. I added
about twenty lines to the same file."

### 2. A built room (0:45 - 1:45)

**Screen:** `mission.amd`. Add The Gallery below The Vault, or show that it is there.

**Say:** "Two of today's fields only show on flat walls, so the ruin needs one box. If you
did last lecture's exercise you have it. If not, add it now. Six numbers: the middle, then
half the width, half the height, half the length. And a passage to the Nave."

### 3. What the walls are made of (1:45 - 4:15)

**Screen:** The Hollow's fence. Type `Walls: rock` under `Loc:`. Show the table of five
words from the page. Change `rock` to `plates`, then back.

**Say:** "This line goes on the ruin, and it names a look. Five words. Rock is asteroids,
and it is what you had already. Plates are flat pieces laid over every wall. Blocks are
the same with thickness. Ribs are plates with bars across them. None is no walls at all.
The game builds a wall from a few hundred small pieces: about four hundred and fifty rocks
for this ruin, or three hundred and seventy plates. I am keeping rock. This place is a
cave."

### 4. One room that differs (4:15 - 6:30)

**Screen:** Type `Walls: blocks` in The Gallery's fence. Then `Art: plain_asteroid_9` in
The Vault's.

**Say:** "Say only where it changes. The Gallery was built later, so the Gallery gets
blocks. Every room without a line of its own takes the ruin's. So do the tunnels, always.
Now the Vault. `Art` names the piece itself. The game has six asteroid shapes, numbered six
to eleven, and a rock wall mixes them. With this line the Vault is cut from one. `Art`
picks the piece. `Walls` picks the look."

### 5. Three dials (6:30 - 8:45)

**Screen:** Back to The Hollow. Type `Seed: 12`, `Debris: 30`, `Gaps: 0.2`. Show the
`Gaps:` table from the page.

**Say:** "Three dials, all on the ruin. Seed decides which rock goes where. The same
number builds the same ruin every time, so your players and you are looking at the same
place. Debris is the loose rock drifting inside the rooms. Sixty if you say nothing. I
want thirty. Gaps is how much of a built wall is missing. It is a number from nought to
one, not a percentage. Nought point two is one piece in five. It only touches flat walls,
so here that is the Gallery. One is no wall at all, and so is two."

### 6. Haze (8:45 - 9:45)

**Screen:** Type `Atmosphere: purple` in The Hollow's fence. Show the list of seven
colors.

**Say:** "One more line on the ruin. Atmosphere fills the whole place with one cloud.
Seven colors, in small letters. Leave the line out, or write none, for no cloud."

### 7. A set piece (9:45 - 12:00)

**Screen:** End of the file. Type The Ring. Then show the short list of shapes, and the
two list lines from "What an art pack adds".

**Say:** "A new kind of record. Three hashes, and `Relic: hollow`, like a room. But this
is a prop: a thing standing in the ruin. `Prop` is where. Fourteen hundred along is the
middle of the first tunnel. `Dress` is what, and how big: a ring, four times its size,
which makes it a little wider than the tunnel. `Facing` is which way it looks: at the
Nave. A prop takes no space. You fly through it. These plain shapes come with the game.
Real gates and statues come in an art pack, in sets called kits. Your mission does not
have the pack yet. But you can write a list, and the game takes the first word it knows.
Today that is the ring."

### 8. Named places (12:00 - 14:30)

**Screen:** Type The Way In, The Altar and The Niche. Then the table from Step 7.

**Say:** "Last kind of record: a point. A named spot. Three numbers, inside a room. And
roles, which say what it is for. One role means something to the game: entrance. The name
of the ruin on the map moves to this point. Any other role is a word of mine. The Altar,
in the middle of the Vault. The game stands an invisible marker there, and when a ship
gets close it turns into a contact with this name. The Niche is the same, and hidden.
Hidden is for a crew in suits, later in this class. For a ship it changes nothing."

### 9. Lint (14:30 - 16:30)

**Screen:** Terminal: `sbs lint MyMission`, clean. Change `Walls: blocks` to
`Walls: bloks`, lint, read the warning, undo. Delete a number from The Altar's `Point:`,
lint, read the warning, undo. Change `Dress: generic-torus 4` to `Dress: generic-tortus 4`,
lint: clean. Undo.

**Say:** "Lint. Clean. A misspelled style: it tells me, and lists the five. A point with
two numbers: it tells me the place will not be made. Now the name of the ring. Clean. Lint
does not check that word today, and the game would simply build no ring. So read your
`Dress` and `Art` lines yourself, letter by letter."

### 10. Play it (16:30 - 18:00)

**Screen:** Server, Helm and the main screen. Helm's map: The Hollow. Fly in. The ring.
The Nave. Up the tunnel to The Vault until The Altar appears. Back, and into The Gallery.

**Say:** "The name is at the way in now. Inside: the haze. The ring, across the tunnel.
Through it. The Nave. Up to the Vault, and there: The Altar, on the map, because I am
close enough. And the Gallery: built walls, with pieces missing."

### 11. Your turn (18:00 - 18:45)

**Screen:** The exercise on the companion page.

**Say:** "Change the Gallery to ribs and take more of it away. Put something on the altar:
a point can be dressed too. Add a hidden place of your own. Then break one line where lint
can see it and one where it cannot. Next time, a place says something when the crew
arrives."
