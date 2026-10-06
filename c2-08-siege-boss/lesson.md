# Class 2, Lecture 8 - A Siege boss, part 1

## What you will have at the end

Your own boss in the Siege game's **Boss** list: a named flagship that arrives with two
escort fleets, and an objective the crew must finish to win.

*[Screenshot to add: the Siege setup screen with "Corsair Queen" chosen in the Boss list.]*

You will write no code. You will copy one short file and change the words in it.

Your boss lives in a folder of your own, outside LegendaryMissions, so updating the game
never deletes it.

## The video

*[Link to add when recorded.]*

## Before you start

You need three things from earlier lectures:

- You can open a folder in VS Code, and the Artemis AMD extension is installed.
- You can run `sbs lint` from the `data\missions` folder.
- You know the shape of a record: a heading, a fence between two `---` lines, and a body.

## Step 1 - Read the Warlord

In VS Code, choose **File**, then **Open Folder**, and open the `data\missions` folder
itself: the folder that holds `LegendaryMissions`. You need two folders inside it today,
so open the one above them both.

In the file list, open `LegendaryMissions`, then `maps`, then `bosses`, then
`warlord.amd`.

The file holds two records.

**The boss.** This is the part that says who arrives and when.

```
# [Warlord](warlord)
---
Boss
Trigger: enemies_low
Low: 25%
Flies: 50% Kralien, 50% Torgoth
Fleets: 2
Difficulty: +1
Named: Warlord kralien_dreadnought
---
A raider warlord and their honor guard warp in to break the defenders.
```

| Line | What it means |
|---|---|
| `# [Warlord](warlord)` | The name the crew sees in the Boss list, then the key |
| `Boss` | What kind of record this is |
| `Trigger: enemies_low` | The boss arrives when the raiders thin out |
| `Low: 25%` | "Thin out" means one quarter of the raiders are left |
| `Flies: 50% Kralien, 50% Torgoth` | Which races the escort fleets are drawn from |
| `Fleets: 2` | How many escort fleets arrive |
| `Difficulty: +1` | One step harder than the difficulty the game was set to |
| `Named: Warlord kralien_dreadnought` | The flagship: its name, then which ship it is |
| The last line | The boss's description |

**The objective.** This is a quest, exactly like the ones you wrote in Class 1.

```
## [Defeat the Warlord](defeat_warlord)
---
Quest
Scope: shared
State: active
Parent: siege_mission
Required: true
Done when: signal siege_won
Reward: 500 credits
---
Destroy the raider Warlord to break the siege for good.
```

| Line | What it means |
|---|---|
| `Scope: shared` | The whole crew holds this quest, not one ship |
| `State: active` | It is live the moment the boss arrives |
| `Parent: siege_mission` | It belongs to the Siege's own mission. `Parent:` is an older spelling of `Part of:` |
| `Required: true` | The crew cannot win without it |
| `Done when: signal siege_won` | The Siege sends `siege_won` when every raider is gone, the boss's ships included |
| `Reward: 500 credits` | What finishing it pays. The credits go to the crew's side |

Today you change the words. Part 2 changes the numbers.

## Step 2 - Make your copy

The bosses that come with the game are in `LegendaryMissions\maps\bosses`. Yours go
somewhere else: `data\missions\common_data\bosses`. The Siege reads both folders.

1. In the VS Code file list, right-click `warlord.amd` and choose **Copy**.
2. Scroll the file list to `common_data` and open it. If it has no `bosses` folder,
   right-click `common_data`, choose **New Folder**, and type `bosses`.
3. Right-click that `bosses` folder and choose **Paste**. A file named `warlord.amd`
   appears in it.
4. Right-click the new file, choose **Rename**, and type `corsair_queen.amd`.

Use lowercase letters and underscores, with no spaces, and keep `.amd` at the end.

Open `corsair_queen.amd`, the one in `common_data\bosses`. Every change from here on is
in this file. Leave `warlord.amd` alone.

| Folder | Whose | What an update does to it |
|---|---|---|
| `LegendaryMissions\maps\bosses` | The game's | Replaced. A file you added is gone |
| `common_data\bosses` | Yours | Left alone |

## Step 3 - Rename the boss

Change the first heading:

```
# [Corsair Queen](corsair_queen)
```

The words in square brackets are what appears in the Boss list. The word in round
brackets is the key; make it match your file name.

> **The name must be new.** If two boss files have the same name in square brackets,
> only one of them appears in the list, and it is yours: the shipped Warlord is gone from
> the list until you rename. The editor does not underline this. `sbs lint` does catch it
> (Step 8): it warns you and names the other file.

## Step 4 - Name the flagship

Change the `Named:` line:

```
Named: Morrigan kralien_dreadnought
```

The first word is the ship's name. The second word says which ship it is; leave it as it
is today.

> **The name is one word.** `Named: Iron Duke kralien_dreadnought` does not make a ship
> called "Iron Duke". The game reads it as a ship called "Iron" of a kind called "Duke",
> and there is no such ship. Write `IronDuke` or `Iron_Duke`. `sbs lint` warns about
> this one too, and shows you the corrected line.

## Step 5 - Write her entrance

Replace the description line under the fence with your own:

```
The Corsair Queen watched the siege falter from the dark. Now she brings her own ships to finish it.
```

Keep it on one line. Type plain quotes and plain hyphens; the curly quotes and long
dashes a word processor makes do not display in the game.

## Step 6 - Rename the objective

Change the second heading, the reward, and the last line:

```
## [Sink the Morrigan](sink_morrigan)
---
Quest
Scope: shared
State: active
Parent: siege_mission
Required: true
Done when: signal siege_won
Reward: 600 credits
---
The Queen's flagship Morrigan leads the last assault. Destroy her and every raider with her.
```

Leave the five lines between `Quest` and `Reward:` exactly as they are.

## Step 7 - Fix the note at the top

Lines that start with `//` are notes to yourself. The game ignores them. Replace the four
note lines at the top with your own:

```
// The Corsair Queen - my first Siege boss. A copy of the Warlord with new names.
// She arrives when the raiders thin out, with two escort fleets and one named flagship.
```

## The finished file

```
// The Corsair Queen - my first Siege boss. A copy of the Warlord with new names.
// She arrives when the raiders thin out, with two escort fleets and one named flagship.

# [Corsair Queen](corsair_queen)
---
Boss
Trigger: enemies_low
Low: 25%
Flies: 50% Kralien, 50% Torgoth
Fleets: 2
Difficulty: +1
Named: Morrigan kralien_dreadnought
---
The Corsair Queen watched the siege falter from the dark. Now she brings her own ships to finish it.

## [Sink the Morrigan](sink_morrigan)
---
Quest
Scope: shared
State: active
Parent: siege_mission
Required: true
Done when: signal siege_won
Reward: 600 credits
---
The Queen's flagship Morrigan leads the last assault. Destroy her and every raider with her.
```

Save the file.

## Step 8 - Check it

Look at your file in VS Code. There should be no squiggly underlines.

Then, in a command prompt in `data\missions`, type:

```
sbs lint common_data\bosses
```

It checks only the bosses in your folder. You want to see:

```
== common_data\bosses\corsair_queen.amd ==
  clean

1 amd + 0 mast file(s): 0 error(s), 0 warning(s)
```

If there is a warning, read it. The three a first boss usually earns:

| Mistake | What lint says |
|---|---|
| The name in square brackets is still `Warlord` | `Warlord` is also the name of the boss in `warlord.amd` |
| A flagship name with a space in it | It tells you what the game will read, and shows the corrected line |
| A field name spelled wrong, such as `Fleats:` | `Fleats` is not a known map field |

`sbs lint LegendaryMissions` lists your bosses too, among every other file in the mission.

## Step 9 - See her in the list

1. Start the game as the server with the LegendaryMissions mission, the way you did in
   Class 1.
2. Choose the **Siege** map.
3. In the map's settings, under **Main**, open the **Boss** list.

Corsair Queen is in the list with the shipped bosses. Choose her and start the game.

The game reads both `bosses` folders when the mission starts. If you add or rename a boss
while the game is running, start the mission again to see it.

## Step 10 - Meet her sooner

At `Low: 25%` you have to destroy three quarters of the raiders before she arrives. While
you are testing, change that one line:

```
Low: 90%
```

Now she arrives as soon as one raider in ten is gone. In a siege of twenty raiders, that
is after the second kill.

When she arrives you should see:

- a ship named **Morrigan** among the raiders,
- two new raider fleets with her,
- a new objective, **Sink the Morrigan**, in the crew's quest list.

Destroy every raider, hers included, and the crew wins. The objective pays its 600
credits to the crew's side.

**Change `Low:` back to `25%` when you are done testing.**

## Keep your work safe

Your boss file is in `common_data\bosses`, not inside LegendaryMissions. An update to
LegendaryMissions replaces the LegendaryMissions folder and nothing else, so your boss
stays where it is.

It is still one file on one computer. Keep a copy somewhere else, the way you would with
a manuscript.

To give your boss to a friend, send them the `.amd` file. They put it in their own
`common_data\bosses` folder.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Your boss is not in the list | The file is not in `data\missions\common_data\bosses`, its name does not end in `.amd`, or the mission was already running when you saved it |
| Only one "Warlord" in the list and no new boss | You did not change the name in square brackets (Step 3) |
| `sbs lint common_data\bosses` warns about every line of the fence | Your copy of the tools is older than this lesson. Update with `sbs update` |
| The flagship has half its name, or does not appear | The name in `Named:` has a space in it (Step 4) |
| She never arrives | She is not chosen in the Boss list, or not enough raiders are destroyed yet (Step 10) |
| Odd symbols in her description | Curly quotes or long dashes from a word processor (Step 5) |
| A red squiggle on the first line of a fence | The word `Boss` or `Quest` was deleted or changed |

## Exercise

Make a second boss, from your own setting.

1. Copy `corsair_queen.amd` to a new file with its own name, in the same
   `common_data\bosses` folder.
2. Give the boss a new name and key.
3. Give the flagship a one-word name.
4. Write the entrance line and the objective in your own voice.
5. Pick your own reward.

## Checkpoint

You are done when all four are true:

- `sbs lint common_data\bosses` shows your file as `clean`.
- Your boss is in the Siege **Boss** list under the name you gave it.
- In a game, the flagship arrives with the name you gave it.
- The objective you wrote appears in the crew's quest list when it does.

## Next

Part 2 changes the numbers: when the boss arrives, what it flies, how many fleets, how
hard, and which ship the flagship is. Part 3 gives the boss an objective of its own that
is more than "destroy everything".

## Further reading

- "Writing a Siege boss" in the LegendaryMissions documentation: the reference for every
  boss field.
- "Quests" in the library documentation: every quest field, including the ones you left
  alone today.
