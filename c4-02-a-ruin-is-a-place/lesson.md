# Class 4, Lecture 2 - A ruin is a place

## What you will have at the end

An ancient ruin of your own, standing in space past the drifting hulk. It has three rooms
and two passages. You can look at its plan in the editor, find it on the map by name, and
fly to it.

*[Screenshot to add: the Relic Plan showing The Mouth, The Nave and The Vault.]*

You will write one section in `mission.amd`. You will not touch `story.mast`.

Today the ruin is only a place. What its walls are made of, what is inside it, and who
goes in wearing a suit all come in later lectures.

## The video

*[Link to add when recorded.]*

## Before you start

- A mission made with `sbs create` from the `amd` template. In this page it is called
  `MyMission`. Use your own folder's name.
- VS Code with the Artemis AMD extension, and the mission folder open in it.
- You have flown a shipped ruin and read its file (Lecture 1 of this class).
- `sbs lint MyMission` says `clean`.

## Step 1 - You describe the space, not the walls

A ruin is hollow. You do not build its walls. You say where the open space is, and
everything else is wall.

| You write | It is | Think of it as |
|---|---|---|
| `Chamber:` | A ball of open space | A room |
| `Passage to:` | A tube of open space between two chambers | A tunnel |
| `Box:` | A block of open space with flat sides | A built room. You meet it in the exercise |

Today you write three chambers and two passages.

## Step 2 - The ruin itself

Open `mission.amd`. Go to the very end of the file and add:

```
## [Relics](relics)

### [The Hollow](hollow)
---
Loc: 0, 0, 20000
---
Older than anyone who could have built it. Three rooms, as far as anyone knows.
```

| Line | What it means |
|---|---|
| `## [Relics](relics)` | A new section. The key in round brackets is `relics`. The game looks for that word (`ruins` works too) |
| `### [The Hollow](hollow)` | The ruin: its name, then its key. Rooms will point at the key |
| `Loc: 0, 0, 20000` | Where the ruin stands. Three numbers: across, height, along |
| The last line | A note for you. Players never see it |

The station in this mission is at `0, 0, 0`. The hulk is at `0, 0, 9000`. So the ruin is
on the same line, past the hulk, a little more than twice as far out.

Keep the `Loc:` line, with all three numbers. Without it the ruin is built at `0, 0, 0`,
around the station.

## Step 3 - The first room

Below the ruin, add:

```
### [The Mouth](mouth)
---
Relic: hollow
Chamber: 0, 0, 0, 900
---
The way in. Wide, and worn smooth.
```

| Line | What it means |
|---|---|
| `### [The Mouth](mouth)` | Three hashes, the same as the ruin. Not four |
| `Relic: hollow` | Which ruin this room belongs to. It is the ruin's key, not its name |
| `Chamber: 0, 0, 0, 900` | A round room. Across, height, along, then the radius |

The first three numbers are measured from the ruin's `Loc:`, not from the station. So
`0, 0, 0` means "right where the ruin is". Move the ruin later and every room moves with
it.

The radius is 900, so the room is 1800 across. For scale, the game treats your light
cruiser as a ball 100 across.

## Step 4 - Two more rooms, and the passages

Add these below The Mouth:

```
### [The Nave](nave)
---
Relic: hollow
Chamber: 3000, 0, 0, 1100
Passage to: mouth 350
---
The big room. Whatever this place was for, it happened here.

### [The Vault](vault)
---
Relic: hollow
Chamber: 3000, 0, 2800, 700
Passage to: nave 300
---
The far end. Small, round, and a long way from the door.
```

`Passage to: mouth 350` is a tunnel from this room to the room whose key is `mouth`. The
number is the tunnel's radius, so this one is 700 across.

| Rule | Why |
|---|---|
| Name the other room by its key: `mouth`, not `The Mouth` | The game reads one word |
| Write each passage once, on either of its two rooms | Twice makes two tunnels |
| Leave the radius out and you get 200 | A narrow tunnel |
| Keep rooms that share a passage within about 3500 of each other | The editor warns you when a passage is longer than 5000 |

The Nave is 3000 to one side of The Mouth. The Vault is 2800 further along from The Nave.
The ruin turns a corner.

## Step 5 - Look at it

Keep `mission.amd` as the tab in front. Press `Ctrl+Shift+P`, type `Relic Plan`, and choose
**Artemis AMD: Show Relic Plan**.

A panel named **Relic Plan** opens beside your file. It draws your ruin from the file
alone. The game does not need to be running.

| What you should find | What it is |
|---|---|
| **The Hollow** at the top left | The ruin's name |
| Three round shapes, labelled The Mouth, The Nave, The Vault | Your chambers |
| Two bands joining them | Your passages |
| A grid | Each square is 1000 on a side |

The panel opens looking at the ruin from an angle. Press **Top** to look straight down. That
is the plan.

Hold the pointer over a room and it tells you its name and radius: `The Mouth r900`. Hold it
over a passage and it tells you its length: `nave - mouth: 3000u`.

Now change something from the panel:

1. Click The Vault. A small box of numbers appears at the bottom right.
2. In the field marked `r`, type `800` and press Enter.
3. Look at your file. One line has changed: `Chamber: 3000, 0, 2800, 800`.
4. Press the panel's **Undo** button. The line goes back to `700`.

The panel and the file are the same thing. An edit in one is an edit in the other, and it
is always one line.

Leave **Preview** and **Live** alone for now. They belong to a later lecture.

## Step 6 - Put it in the game

There is nothing to do. Your mission already builds every ruin written in `mission.amd`.

Open `story.mast` and look for this line. Do not change it:

```
    relics_spawn(get_mission_dir_filename("mission.amd"))
```

When the map starts, that one line does four things for each ruin in the file:

| It | So that |
|---|---|
| Builds the space from your rooms and passages | The ruin is a place |
| Puts rock around the space | There is something to see |
| Places what is inside the ruin | Nothing yet. Lectures 4 and 5 fill it |
| Writes the ruin's name on the map, at its `Loc:` | Helm can find it |

A mission with no Relics section is not a mistake. The line does nothing and the mission
runs as before.

> **No such line in your `story.mast`?** Your mission was made from an older template. This
> is the one time today you paste something. Find the line that starts
> `    science_define_scan_amd(` and paste the `relics_spawn` line above, on a new line
> directly under it. It starts with four spaces. Not a tab, and not three.

## Step 7 - Check it

```
sbs lint MyMission
```

You want `clean` under `mission.amd`.

Lint catches these:

| Mistake | What lint says | What the game does |
|---|---|---|
| `Passage to: crypt 300`, and no room has the key `crypt` | `'crypt' is not a room of 'hollow'` | Builds no ruin at all |
| `Passage to: The Mouth 350` (the name, not the key) | The same warning, about `The` | Builds no ruin at all |
| `Relic: holow`, or `Relic: The Hollow` | That is not a relic in this file, so the room is dropped | The room is missing. If another room has a passage to it, no ruin at all |
| `Chambre:` | Not a known field | The same as a missing room |
| `Pasage to:` | Not a known field, and the ruin `solves into 2 separate pieces` | The ruin is built with that passage missing |
| A radius of `0` or `-700` | The radius must be positive | Builds no ruin at all |
| Three numbers where four are needed, or `700u`, or a long dash for a minus sign | `'chamber' needs 4 numbers, got 3` | The same as a missing room |
| A room that no passage reaches and that touches no other room | The ruin `solves into 2 separate pieces`. It points at the ruin's heading, not at the room | The room is there, sealed off |
| Two rooms with the same key | That key names two records | One of the two rooms is missing |
| A room written with four hashes | The room is nested under the room above it. `Give this heading 3 hashes` | That room is missing. With every room nested, no ruin at all |
| A room written with two hashes | That room, and every room below it, `is not inside a relics section` | Those rooms are missing |
| A room with no `Relic:` line | It `has a Chamber: line and no Relic: line` | That room is missing |
| `Loc:` with two numbers | `Loc: needs 3 numbers` | The ruin is built around the station |
| No colon after `Chamber` | An error | The same as a missing room |
| The closing `---` left off | An error | |

A missing room that another room has a passage to is a passage to nowhere, and that means
no ruin at all.

Fix every one of these before you play. A warning here is not a small thing: with most of
them the game builds no ruin at all, and with the rest a room is missing or cut off.

When the game cannot build a ruin it does not stop. The rest of the mission runs, and the
reason is written to `mast.runtime.log` in your mission folder. An empty file there means
nothing went wrong.

Lint says `clean` for these, and they are still wrong:

| Mistake | What happens |
|---|---|
| No `Loc:` line at all | The ruin is built around the station. `mast.runtime.log` says so |
| A radius of `90000` | A room bigger than the whole map |

So check those two by eye.

## Step 8 - Play it

Start your mission as the server with a Helm console, the way you did in Class 1.

1. On Helm's map, look past the hulk for a marker named **The Hollow**. It is 20000 from
   the station.
2. Fly to it. The marker is at the middle of The Mouth.
3. The rock around you is the wall of the first room. Go on through the passage to The
   Nave, then turn and go on to The Vault.

The rock is scenery. It does not stop your ship, and you can fly back out through it.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The panel says `No relic in this file.` | `mission.amd` was not the tab in front when you opened the panel, or the ruin has no `Loc:` line |
| The plan is right and the game has no marker | Lint has a warning you have not fixed. Open `mast.runtime.log` in the mission folder: it says why the ruin was not built |
| Still no marker, lint is clean, and the log is empty | Your `story.mast` has no `relics_spawn` line. See the note in Step 6 |
| Rooms are missing in the game | A room has two or four hashes, or no `Relic:` line, or a misspelled `Relic:` key. Lint names each one |
| The ruin is wrapped around the station | No `Loc:` line, or it has two numbers |
| Lint says `solves into 2 separate pieces` | A room is not joined to the rest. Look for the room with no passage |

## Exercise

Add a fourth room to your ruin, and make it a built one.

1. Below The Vault, add a box that overlaps The Nave:

   ```
   ### [The Gallery](gallery)
   ---
   Relic: hollow
   Box: 3000, 0, -1600, 600, 400, 800
   ---
   A built room, with flat walls and real corners. Somebody added this later.
   ```

   A box has six numbers: where its middle is (across, height, along), then half its
   width, half its height and half its length. This one is 1200 by 800 by 1600.

2. This box has no passage. It joins the Nave by overlapping it. The Nave reaches 1100
   from its middle. This box starts 800 from the Nave's middle, so they share 300. That
   shared space is the doorway.

3. A box can have a passage too, written the same way as on a chamber. You will use one
   in step 6.

4. Open the Relic Plan and press **Top**. You should have four rooms.

5. Move the box away: change `-1600` to `-1900`. Run lint. It tells you the ruin is in 2
   pieces.

6. Leave the box where it is and join it with a tunnel instead. Add one line to its fence:
   `Passage to: nave 300`. Run lint again. It is clean, and the plan shows a band between
   the box and The Nave.

7. Give your ruin and its rooms your own names: change the words in square brackets. Leave
   the keys in round brackets alone, because `Relic:` and `Passage to:` lines point at
   them. Write your own note under each.

## Checkpoint

You are done when all four are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`.
- The Relic Plan shows every room you wrote, each one joined to the rest.
- In the game, a marker with your ruin's name is on the map where your `Loc:` says.
- When you fly to the marker, there is rock around you.

## Next

Lecture 3 dresses the ruin: what its walls are made of, and how to make a built hall look
different from a cave.

## Further reading

- "Relic interiors" in the library documentation: every field of a ruin and its rooms.
- `relics\sink.amd` in Storm's Beacon: a shipped ruin that is one enormous box.
- "The AMD file format": headings, fences, and how a record says what it is.
