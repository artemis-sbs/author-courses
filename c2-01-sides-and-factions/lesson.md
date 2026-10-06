# Class 2, Lecture 1 - Sides and factions

## What you will have at the end

Your mission has three sides where it had one.

The Breakers are scavengers who want the hulk. Their cutter waits beyond it, and Science
reads it as an enemy vessel. The Harbor Guild are friends. They keep a yard west of DS 1,
and the crew can dock there. Each side has a name, a key and a color that you wrote.

*[Screenshot to add: the Science console with the Breaker Cutter selected: its name, the
word `breaker` beside it, and the scan text.]*

You will edit two files. In `mission.amd` you add one section with three records, add two
landmarks and change two lines. In `story.mast` you paste two lines and add one word.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission from Class 1, as it stood at the end of Lecture 11: the arc **Salvage Run**,
  the lifeboat, and the tug that arrives.
- `sbs lint MyMission` says `clean`, and `sbs compile MyMission` prints nothing.
- You can start the mission with a Helm, a Science and a Comms console.

In this page the mission folder is called `MyMission`. Use your own folder's name.

Words for this lecture:

| Word | Meaning |
|---|---|
| Side | A faction: a team. Every ship and station is on one side, or on none |
| Key | The short word in round brackets after a name. A side's key is the word everything else uses to point at it |
| Relation | What two sides are to each other: enemies, allies, neutral, or nothing at all |
| Role | A label an object wears. You met it in Lecture 8 |

## Step 1 - The side you already have

Open `story.mast` and look at lines 18 to 20:

```
tsn = await prefab_spawn(prefab_side_generic, data={"key":"tsn"})
side_set_display_name(tsn, "TSN")
side_set_icon_color(tsn, "#07F")
```

Lecture 11 told you what they do: they make the side `tsn`, and give it a name and a
color. That is the only side your mission has, and everything on your map is on it.

| Thing | Where its side is written | Its side |
|---|---|---|
| DS 1 | `"tsn, station"`, on line 59 | `tsn` |
| The hulk | `"tsn, derelict"`, on line 63 | `tsn` |
| The tug | `"tsn, tug"`, in your card at the end of the file | `tsn` |
| The crew's ship | The game's settings, not this file | `tsn` |
| The lifeboat | Nowhere. A wreck needs no side | none |

Inside the quote marks, the first word is the side. The words after it are roles.

So `tsn` is the key of the crew's own side. Keep that word in mind: every step below
uses it.

Leave lines 18 to 20 as they are. From here on you write sides the way you write
everything else: as records in `mission.amd`.

## Step 2 - A Sides section, with your own side in it

Go to the very end of `mission.amd`. Leave two blank lines, then type:

```
// ---- Sides. Each record is one faction: its name, its color, and who it fights or
// stands with. `Side:` on a landmark names one of these keys.
## [Sides](sides)

### [TSN](tsn)
---
Color: #07F
---
The Terran Stellar Navy. The crew's own side.
```

| Line | Meaning |
|---|---|
| `## [Sides](sides)` | The section. Two hashes, and the key is exactly `sides` |
| `### [TSN](tsn)` | One side. Three hashes, the side's name, then its key |
| `Color: #07F` | The side's color |
| The last line | A description. It is a note for you |

Three rules for a side's key.

1. **Your own side's key is `tsn`, letter for letter.** It is the word the crew's ship and
   DS 1 already carry. A record with any other key makes a new side that nobody is on.
2. **Small letters, one word, no spaces.** `breaker`, not `Breaker` and not `the breakers`.
3. **Choose a word the crew can read.** On the Science console, a scanned ship has its
   side's key written beside its name. The key is shown, not the name in the square
   brackets.

### The color

`#07F` is a hash sign and three characters. They say how much red, how much green and how
much blue is in the color, in that order. Each character is one of
`0 1 2 3 4 5 6 7 8 9 A B C D E F`. `0` is none of it and `F` is all of it.

| You write | You get |
|---|---|
| `#F00` | Red |
| `#F80` | Orange |
| `#FF0` | Yellow |
| `#0C6` | Green |
| `#07F` | Blue |
| `#FFF` | White |

The game uses the color for the side's key, the word beside a contact's name on the Science
console. The map itself does not use it: there a contact is colored by what it is to YOU,
red for an enemy and blue for a friend. Lint does not check a color, so copy one from the
table.

### Run lint

```
sbs lint MyMission
```

It has something to say:

```
nothing in this mission reads a section keyed `sides`, so its records are never loaded.
The story asks this file for: characters, dialogue, landmarks, quests, scans.
```

Lint is right. In Lecture 11 you read the lines of `story.mast` that read your file: one
for quests, one for scans, one for landmarks. There is no line for sides. The next step
adds it.

## Step 3 - The card: one line that reads the section

*If your `story.mast` already has a line that begins `sides_declare_amd(`, the card is
built in. Go to Step 4.*

Open `story.mast`. Find line 35. It begins `shared MISSION_DOC =`, and it is the line that
reads your whole file. Put your cursor at the END of that line and press Enter twice. Then
type these two lines. Each starts four spaces in, lined up with line 35:

```
    # The sides, if mission.amd has a Sides section. With no such section this does nothing.
    sides_declare_amd(amd_section(MISSION_DOC, "sides"))
```

| Part | Meaning |
|---|---|
| The `#` line | A comment, so that next month you know what the line is for |
| `sides_declare_amd(` | Make a side from each record it is given |
| `amd_section(MISSION_DOC, "sides")` | The section of your file whose key is `sides`. The same words as on the landmarks line, with a different key |

You change nothing on this card. It has two rules, and both are about where it goes.

1. **Below line 35.** Line 35 reads the file. A line above it has nothing to read.
2. **One of the map's lines.** Four spaces in, and above the map's `->END`.

Run both checks, as you have since Lecture 11:

```
sbs lint MyMission
sbs compile MyMission
```

Lint says `clean`. Compile prints nothing.

## Step 4 - Two more sides

Go back to the end of `mission.amd`. Below the TSN record, leave a blank line and type:

```
### [The Breakers](breaker)
---
Color: #F80
Enemies: tsn
---
Scavengers. They strip dead ships, and they do not wait for the paperwork.

### [Harbor Guild](guild)
---
Color: #0C6
Allies: tsn
---
The pilots and tug crews who work the lanes around DS 1.
```

Two lines are new.

| Line | Meaning |
|---|---|
| `Enemies: tsn` | This side and the side `tsn` are enemies |
| `Allies: tsn` | This side and the side `tsn` are allies |

After the colon comes a **key**. Two rules.

1. **Say it once.** `Enemies: tsn` on the Breakers makes the Breakers the enemy of the TSN,
   and the TSN the enemy of the Breakers. You do not write it again on the TSN record.
2. **More than one key takes a comma.** `Enemies: tsn, guild`. Never `tsn guild`, and never
   `tsn and guild`.

## Step 5 - Put something on each side

A side with nothing on it is a name in a file. Give each of yours one thing on the map.

You know the `Side:` line from Lecture 10. Then it could only say `tsn`. Now it can say
any key in your Sides section.

Scroll up to your Landmarks section. Find the last line of **The Lifeboat**, its
description. Leave one blank line below it. Then, ABOVE the `// ---- Sides` note, type:

```
### [Breaker Cutter](cutter)
---
Kind: npc
Side: breaker
Roles: cutter
Art: pirate_strongbow
Loc: 3000, 0, 11000
---
A Breaker ship, standing off until the hulk goes quiet.

### [Guild Yard](guild_yard)
---
Kind: station
Side: guild
Roles: yard
Art: starbase_civil
Loc: -6000, 0, 3000
---
The Harbor Guild's repair yard.
```

The cutter sits about 3600 beyond the hulk. The yard is about 6700 from DS 1, to the west.

One `Art` word is new. Add it to your table from Lecture 10:

| You write | It looks like | Goes with |
|---|---|---|
| `Art: pirate_strongbow` | A pirate ship | `Kind: npc` |

**Mind where these two records go.** They belong to the Landmarks section, so they sit
above the line `## [Sides](sides)`. A record typed below that line is read as a side: the
game makes a side called Breaker Cutter and puts no ship on the map.

Run lint. It says `clean`.

## Step 6 - A second station changes an old step

Lecture 10 warned you about this, in its last table. Your story ends with:

```
Done when: reach station 1000
```

`station` is a role, and the game gives it to every station. Until today DS 1 was the only
one. Now the Guild Yard wears it too. A crew could carry the log to the yard, and the game
would end there with "DS 1 knows what happened out there."

The cure is a role that only DS 1 wears. It takes two edits.

First, in `mission.amd`, find **Bring the Log Home** and change its `Done when:` line:

```
Done when: reach home 1000
```

Run lint. It tells you the half you have not done yet:

```
nothing in this mission wears a role called `home`, so `reach` matches nothing.
```

Now open `story.mast` and find the line that puts DS 1 on the map. It begins
`npc_spawn(0, 0, 0, "DS 1"`, and it is on line 62 now that your card is above it. Inside
the second pair of quote marks, after `station`, type a comma, a space and the word `home`:

```
    npc_spawn(0, 0, 0, "DS 1", "tsn, station, home", "starbase_command", "behav_station")
```

| Inside the quote marks | Meaning |
|---|---|
| `tsn` | The side. It stays first |
| `station` | A role. Keep it: docking looks for it |
| `home` | Your new role. Only DS 1 wears it |

Run both checks. Lint says `clean`. Compile prints nothing.

## Step 7 - Who is what to whom

You have three sides, so there are three pairs. Count what you have said about each.

| Pair | Said where | They are |
|---|---|---|
| TSN and the Breakers | `Enemies: tsn`, on the Breakers | Enemies |
| TSN and the Harbor Guild | `Allies: tsn`, on the Guild | Allies |
| The Breakers and the Harbor Guild | Nowhere | Nothing to each other |

**A pair nobody mentions is nothing to each other.** They are not enemies and not friends.
The game does not guess.

Scavengers and harbor pilots are not strangers. In the Breakers record, change the
`Enemies:` line:

```
Enemies: tsn, guild
```

There are three words for a relation.

| You write | The two sides are |
|---|---|
| `Enemies: guild` | Enemies |
| `Allies: guild` | Allies |
| `Neutral: guild` | Neutral. They know each other and keep apart |
| Nothing | Nothing to each other. In play this is the same as neutral |

One shortcut. `Enemies: *` means every other side in your Sides section.

### What a relation does in the game

This is what the crew meets. The words in quote marks are the game's own.

| To the crew, the side is | A station of that side | A ship of that side |
|---|---|---|
| An enemy | Science draws its name in red, with a reading that begins "Enemy". Comms can hail and taunt it. The crew cannot dock | Science draws its name in red and reads "Enemy vessel. Exercise caution." Comms is offered **Hail**, **Taunt** and **Surrender now** |
| An ally | Science draws its name in green and reads "This is a friendly station." Comms is offered **Hail**, **Build Weapons** and **Request Priority Docking**. Helm can dock | Science shows it as `unknown` until you write scan text for one of its roles. Then its name is green, and Comms is offered **Hail** |
| Neutral, or nothing | Science shows it as `unknown` until you write scan text for one of its roles. Then its name is white. Comms is offered nothing, and the crew cannot dock | The same: `unknown`, then white once it has scan text of yours. Comms is offered nothing |

Three more things follow from being enemies or allies.

- **The crew's own side counts as an ally.** DS 1 and the hulk are drawn in green.
- **An enemy close by stops docking.** With an enemy ship inside about 1500, Helm's request
  to dock is refused.
- **Being enemies does not start a fight.** The cutter sits where you put it. It does not
  move and it does not shoot. A ship needs orders for that, and a landmark has none. Ships
  that hunt come with the Siege bosses, later in this class.

## Your finished pieces

At the end of the Landmarks section of `mission.amd`:

```
### [Breaker Cutter](cutter)
---
Kind: npc
Side: breaker
Roles: cutter
Art: pirate_strongbow
Loc: 3000, 0, 11000
---
A Breaker ship, standing off until the hulk goes quiet.

### [Guild Yard](guild_yard)
---
Kind: station
Side: guild
Roles: yard
Art: starbase_civil
Loc: -6000, 0, 3000
---
The Harbor Guild's repair yard.
```

At the end of the file:

```
// ---- Sides. Each record is one faction: its name, its color, and who it fights or
// stands with. `Side:` on a landmark names one of these keys.
## [Sides](sides)

### [TSN](tsn)
---
Color: #07F
---
The Terran Stellar Navy. The crew's own side.

### [The Breakers](breaker)
---
Color: #F80
Enemies: tsn, guild
---
Scavengers. They strip dead ships, and they do not wait for the paperwork.

### [Harbor Guild](guild)
---
Color: #0C6
Allies: tsn
---
The pilots and tug crews who work the lanes around DS 1.
```

In `story.mast`, lines 35 to 38:

```
    shared MISSION_DOC = document_get_amd_file(get_mission_dir_filename("mission.amd"), data_parser=amd_mission_data)

    # The sides, if mission.amd has a Sides section. With no such section this does nothing.
    sides_declare_amd(amd_section(MISSION_DOC, "sides"))
```

And line 62:

```
    npc_spawn(0, 0, 0, "DS 1", "tsn, station, home", "starbase_command", "behav_station")
```

Both whole files are in `example\`.

## Step 8 - Check it

```
sbs lint MyMission
sbs compile MyMission
```

You want `clean` from the first and nothing from the second.

Every row below was made on purpose, and both the tools and the game were run. Read the
second table twice. Lint is clean for all of it, and it is where the likely mistakes are.

**Lint names these.** The words in the last column are at the end of the line lint prints.

| Mistake | What the game would do | Lint says |
|---|---|---|
| `## [Sides](side)` or `## [Factions](factions)` | Make no sides. The cutter and the yard belong to nobody | `section-not-loaded` |
| A side typed with two hashes | Lose that side and every side below it | `section-not-loaded` |
| The Sides line typed with three hashes, or left out | Make no sides | `landmark-no-art` and `unknown-field`: your sides are read as landmarks |
| The Sides line typed with one hash | Read NOTHING from your file: no quests, no landmarks, no sides | `heading-level-jump`, an error |
| The cutter and the yard typed below the Sides line | Place neither. Make two sides called Breaker Cutter and Guild Yard | `unknown-field`: `Kind` is not a known side field |
| Two sides with the same key | Make one side, with the lower record's name, color and relations. With `breaker` twice, the cutter was a friend | `duplicate-key` |
| `### [The Breakers]` (no key) | Make no Breakers. The record's lines become part of the TSN description | `suspect-heading` |
| `Enemy: tsn`, `Ally: tsn` or `Colour: #F80` | Ignore the line | `unknown-field` |
| `Enemies tsn` (no colon) | Ignore the line | An error: it expected `Label: value` |
| `Enemies:` typed below the closing `---` | Ignore the line | `field-below-fence` |
| A side's closing `---` left out | Lose every side below it | `unclosed-data-fence`, an error |
| `Sides: breaker` on the cutter | Put the cutter on no side | `unknown-field` |
| The step says `reach home 1000` and DS 1 does not wear `home` | Never finish the story | `role-nothing-wears` |
| The card is not in `story.mast`, or it says `"side"` | Make no sides | `section-not-loaded` |
| `Enemies: tsm` (a misspelled key) | Make the Breakers and the TSN nothing to each other. The cutter stays `unknown`. `mast.runtime.log` says `Side not found` | `dangling-side`, and the keys you did declare |
| `Enemies: tsn guild`, `tsn and guild` or `tsn; guild` | Make no enemies at all. The whole line is read as one key | `dangling-side`: put a comma between sides |
| `Side: braker` on the cutter | Put the cutter on no side. Science shows `unknown` and Comms is offered nothing | `dangling-side` |

**Lint says `clean` for every row of this table.** Check these by eye.

| You wrote | What happens |
|---|---|
| No `Side:` line on the cutter | The cutter is on no side. Science shows `unknown` and Comms is offered nothing |
| `Roles: cutter, breaker` in place of `Side: breaker` | The same. A role is not a side |
| The key changed in the heading and not in `Side:` or `Enemies:` | The same, for whatever still uses the old key |
| `Side: The Breakers` (the name), or `(Breaker)` with a capital in the heading | It half works. Science reads the cutter as an enemy, and an enemy close by no longer stops docking. Write the key, in small letters |
| `#### [Harbor Guild](guild)` (four hashes) | The Guild is not made. The yard is on no side |
| `### The Breakers` (no brackets at all) | No Breakers. The record's lines become part of the TSN description |
| Your own side with a new key, such as `### [TSN](navy)` | A side nobody is on. The crew's ship is still on `tsn`, so nobody is its enemy and nobody is its ally |
| `Allies: tsn` and `Enemies: tsn` in one record | Enemies |
| Two records that disagree about the same pair | The record lower in the file wins |
| `Enemies: tsn` on the TSN record itself | DS 1 reads as an enemy starbase, Comms is offered **Taunt** for it, and the crew cannot dock at home |
| `Color: F80`, `#F8` or `burnt orange` | Not known. The words go to the game as you typed them. Use the table in Step 2 |
| A scan record of your own for `cutter`, on the `scan`, `intel` or `bio` tab. Or one for `yard`, on the `scan` tab | The game's own reading is shown, not yours. Yours is used only on a tab the game has no reading for |
| DS 1 wears `home` and the step still says `reach station 1000` | The story can be finished at the Guild Yard |
| `"tsn, station home"` (no comma) | DS 1 wears one role called `station home`. The story never finishes |
| `"home, tsn, station"` (the new word first) | DS 1 is on a side called `home`, which does not exist. The crew cannot dock there |

**The card in `story.mast`:**

| Mistake | In the game | `sbs lint` | `sbs compile` |
|---|---|---|---|
| The card is below the map's `->END` | No sides | `clean` | Nothing |
| The card is above line 35 | No sides | `clean` | Nothing |
| The card is at the top of the file, at the left edge | No sides | `clean` | Nothing |
| A `#` typed in front of the `sides_declare_amd` line | No sides | `clean` | Nothing |
| `"Sides"` with a capital | No sides | `clean` | Nothing |
| The card is at the left edge, among the map's lines | Nothing runs | `clean` | `Bad indentation`, with the line |
| Three spaces in front, not four | Nothing runs | `clean` | `Bad indentation`, with the line |
| The last bracket left off | Nothing runs | `clean` | `invalid syntax`. The line it shows has the next line stuck on the end |
| Curly quote marks from a word processor | Nothing runs | A warning for each of your signals, saying nothing sends it | `invalid character`, with the line |
| `sides_declare_and(`, or no quote marks round `sides` | The game stops with an error as the map starts. `mast.runtime.log` names the line | `clean` | Nothing |
| The card pasted twice | It works | `clean` | Nothing |

For the first five rows nothing warns you at all. Check three things by eye:

1. The line that begins `sides_declare_amd(` is below the line that begins
   `shared MISSION_DOC =`.
2. It is four spaces in, and above the map's `->END`.
3. The word in quote marks is `sides`, in small letters, the same as the key in
   `## [Sides](sides)`.

## Step 9 - Play it

Start your mission as the server, with a Helm, a Science and a Comms console.

1. On Science, select the **Guild Yard**. Until the scan is done it reads `unknown`. Then
   its name is drawn in green, the word `guild` is beside it in the Guild's own green, and
   the `scan` tab says "This is a friendly station."
2. On Comms, select the Guild Yard. You are offered **Hail**, **Build Weapons** and
   **Request Priority Docking**. Press **Hail**. The yard answers "Hello, Artemis. We stand
   ready to assist", lists its shields, and says "You have full docking privileges."
3. On Helm, fly to within 600 of the yard. Helm can dock there, the same as at DS 1.
4. Fly out past the Unknown Hulk. On Science, select the **Breaker Cutter**. Its name is
   drawn in red, the word `breaker` is beside it in orange, and the `scan` tab says "Enemy
   vessel. Exercise caution."
5. On Comms, select the cutter. You are offered **Hail**, **Taunt** and **Surrender now**.
   Press **Hail**: "Go away, Artemis! You talk too much!"
6. Stay near the cutter for a while. It does not move, and nobody shoots.
7. Now finish the story: the hulk, the lifeboat, the wait for the tug. When **Bring the Log
   Home** appears, fly to the Guild Yard first. Nothing happens. Fly to DS 1. Inside 1000,
   the game ends with your `Win:` sentence.

The side is paid what it was paid in Lecture 11: 500 credits with the bonus, 450 without.

### The other tabs of an enemy ship

The cutter's `status`, `intel` and `bio` tabs are filled by the game too, and two of them
read badly: "The captain cannot be taunted ." and "A bunch of  creatures." The game is
looking for the ship's race, and a landmark has none. A scan record of your own for those
tabs does not help: on an enemy ship the game's reading replaces yours.

One tab is still yours. The game has no reading for `mat`, so a scan record with
`Scan of: cutter` and `Tab: mat` is shown as you wrote it.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The cutter or the yard stays `unknown` on Science, however long you wait | It is on no side, or its side is nothing to yours. Work down this list: the card is missing or in the wrong place (Step 3); the `Side:` word is not the side's key; the `Enemies:` or `Allies:` line has a misspelled key or no comma; the side's heading has four hashes |
| Comms is offered nothing for the cutter | The same list. Comms has nothing to say to a contact Science has not identified |
| The crew cannot dock at the Guild Yard | The Guild is not your ally. Check `Allies: tsn` and the yard's `Side: guild` |
| The crew cannot dock at DS 1 either, and DS 1 reads as an enemy | The TSN record names `tsn` as its own enemy. Or, on line 62, `home` was typed before `tsn` |
| Nothing is where it should be: no cutter, no yard | The two landmarks are below the `## [Sides](sides)` line. Move them up into the Landmarks section |
| No quests at all | A heading in `mission.amd` jumps a level. Run lint: it is an error, not a warning |
| The story ends at the Guild Yard | The step still says `reach station 1000` |
| The story never ends | The step says `reach home 1000` and DS 1 does not wear `home`. Look for the comma on line 62 |
| The mission starts and there is no map to pick, or a page of errors | `story.mast` does not compile. Run `sbs compile MyMission` |
| The game stops with an error as the map starts | The card is misspelled. `mast.runtime.log` in your mission folder names the line |

## Your recipe card

One card. It joins the three from Lecture 11.

**Card 4 - Sides.** A line inside the map's block, below the line that begins
`shared MISSION_DOC =`:

```
    sides_declare_amd(amd_section(MISSION_DOC, "sides"))
```

There is nothing on it to change. It reads the section keyed `sides`, and it does nothing
when your file has no such section.

And one edit you can now make to any `npc_spawn` line, on any card:

| Inside the second pair of quote marks | Change it to |
|---|---|
| The first word, `tsn` | The key of any side in your Sides section |
| The words after it | Roles, with a comma between them |

## Exercise

Add a faction of your own, and watch the crew's view of it change.

1. At the end of the Sides section, write a third side: a name, a key and a color of your
   own. Give it no `Enemies:` line and no `Allies:` line.
2. In the Landmarks section, above the `// ---- Sides` note, give it one ship: `Kind: npc`,
   `Side:` with your key, a role of your own, `Art: cargo_ship`, and a `Loc:` of your own.
3. Run both checks, then play. On Science your ship reads `unknown`, and it stays that way.
   A stranger tells Science nothing.
4. Give it a voice. In the Scans section, write a scan record for its role, as you did in
   Lecture 10: `Scan of:` your role, `Tab: scan`, and one `%` line. Play again. Now Science
   shows its name in white, your key beside it in your color, and your reading.
5. Add `Enemies: tsn` to your side. Play. The name is red, the reading is the game's own
   "Enemy vessel. Exercise caution.", and Comms is offered **Taunt**.
6. Change the line to `Allies: tsn`. Play. The name is green, your reading is back, and
   Comms is offered **Hail**.
7. Keep the relation your story needs.

## Checkpoint

You are done when all five are true:

- `sbs lint MyMission` shows `mission.amd` as `clean`, and `sbs compile MyMission` prints
  nothing.
- Science shows the Breaker Cutter's name in red, with `breaker` beside it, and reads
  "Enemy vessel. Exercise caution."
- Science shows the Guild Yard's name in green, with `guild` beside it, and the crew can
  dock there.
- Comms is offered **Taunt** for the cutter and **Request Priority Docking** for the yard.
- Bring the Log Home does not finish at the Guild Yard, and does finish at DS 1.

## Next

Lecture 2 puts people in the story: three characters, each with a face.

## Further reading

- "Sides, lifeforms & faces" in the library documentation. Its first half is script. The
  part headed "Declaring sides as data" is the one for you: it explains `*`, and two more
  words, `players` and `civilians`. Do not paste its `sides_load_amd` line. That line reads
  a whole file of sides, and pointed at `mission.amd` it makes a side out of your mission's
  title.
- `maps\sides.amd` in the LegendaryMissions folder: the three sides of the stock game, in a
  file of their own.
- "Sides - who lives here" in the Open Universe writer's guide. Its `Character:`,
  `Disposition:`, `Home:` and `Flies:` lines belong to Open Universe, which is Class 5. In
  a mission like yours lint calls each one an unknown field, and `Disposition: foe` makes
  nobody an enemy. Lint lets `Values:` through. That line belongs to reputation, which is
  Lecture 6.
