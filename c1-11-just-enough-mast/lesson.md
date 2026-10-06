# Class 1, Lecture 11 - Just enough MAST

## What you will have at the end

Three things.

You can open `story.mast`, read it from the first line to the last, and say what each
block is for. Your map carries a name you chose. And a salvage tug that is not on the map
at the start arrives twenty seconds after the crew finds the lifeboat, while a step of
your story waits for it.

*[Screenshot to add: the Quest Log showing "Wait for the Tug", and the tug beside the
lifeboat on the Helm map.]*

You will edit two files. In `mission.amd` you add one step, and two lines to your word
list. In `story.mast` you change two lines and paste eight.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 10 left it: both files, with **Find the Lifeboat** in the arc
  **Salvage Run**.
- `sbs lint MyMission` says `clean`.
- VS Code with the mission folder open, a command prompt open in `data\missions`, and the
  game closed.

This page leans on four earlier ones, and does not explain them again.

| Lecture | What you learned there |
|---|---|
| 6 | How to read a finding from lint, and to fix the first one first |
| 7 | Your first look at `story.mast`: a note, a working line, the hulk's list, and the line that says a signal |
| 9 | `Starts when: revealed`, and `Then: reveal` with a step's address |
| 10 | A Landmarks record: the facts that put a thing on the map |

Line numbers on this page are for a `story.mast` that matches Lecture 10's finished file
line for line. It has 105 lines. If yours are a line or two out, go by what the line
begins with. The one line number this page prints for `mission.amd`, in Step 4, is for
Lecture 10's finished file as well. If you did an exercise in an earlier lecture, yours is
higher.

Words for this lecture:

| Word | Meaning |
|---|---|
| MAST | The language `story.mast` is written in. You will read it and paste it. You will not write it |
| Block | A group of lines that belong together. Its first line starts at the left edge. The lines under it are indented |
| Label | A named block. Its first line starts with two or more `=` signs, or with `@` |
| Route | A block that runs when something happens. Its first line starts with `//` |
| Indent | The spaces at the start of a line. They say which block the line belongs to |
| Recipe card | A few lines to copy, with the words to change marked |

One reminder from Lecture 7 before you read anything. Two marks you know mean something
else in this file.

| Mark | In `mission.amd` | In `story.mast` |
|---|---|---|
| `#` | A heading | A note |
| `//` | A note | The first line of a route |

So a note of your own in `story.mast` starts with `#`. Never with `//`.

Lecture 7 gave you three rules for this file: change only what is between quote marks,
never touch a quote mark, leave every comma. Today you go further. You change two whole
lines and add eight new ones. Everywhere else in the file, the three rules still hold.

## Step 1 - Read the file

Open `story.mast`. Read it with this table beside you. The line numbers are the ones
VS Code shows down the left.

| Lines | Begins with | What it is |
|---|---|---|
| 1 to 10 | `#` | A note from the person who wrote the template |
| 12 | `shared MISSION_DOC = None` | A named box, empty for now. `shared` means every block in this file can see it |
| 16 | `crew_load_amd(` | Reads a crew roster from `mission.amd`, if it has one. Class 3 |
| 18 to 20 | `tsn =` | Makes the side `tsn`, and gives it a name and a color |
| 22 | `@media/music` | Says which music the mission may play |
| 25 | `@map/amd_sample` | A label: the map. Everything indented under it runs once, when the game starts |
| 26 | `"` | The map's description |
| 27 to 30 | `metadata:` | What the server can set before the game starts. Leave it alone |
| 31 to 79 | four spaces | The map's lines. See the next two tables |
| 89 to 96 | `=== watch_for_arrival` | A label. Every two seconds it asks: is a player ship within 2000 of the hulk? When one is, it says your signal |
| 103 to 105 | `//science` | A route. It runs when Science scans something that wears `derelict` |

Now the map's lines. These are the ones that read **your** file.

| Line | Begins with | What it reads from `mission.amd` |
|---|---|---|
| 35 | `shared MISSION_DOC =` | The whole file, once. This fills the box from line 12 |
| 44 | `sides_declare_amd(` | A section keyed `sides`. Class 2 |
| 48 | `lifeforms_spawn(` | A section keyed `characters`. Class 2 |
| 49 | `dialogue_register_scenes(` | A section keyed `dialogue`. Class 2 |
| 54 | `landmarks_spawn(` | Your Landmarks section, keyed `landmarks` |
| 56 | `quest_grant_amd(` | Your Quests section, keyed `quests` |
| 57 | `science_define_scan_amd(` | Your Scans section, keyed `scans` |
| 62 | `relics_spawn(` | A Relics section. Class 4 |

Look at line 54. The word in quotes is `landmarks`. That is why Lecture 10 told you the key
in `## [Landmarks](landmarks)` had to be exactly that word: this line asks for it. Each of
these lines does nothing when its section is not in your file.

The rest of the map's lines:

| Line | Begins with | What it does |
|---|---|---|
| 64 | `npc_spawn(` | Puts the station DS 1 on the map |
| 68 | `hulk = npc_spawn(` | Puts the hulk on the map. You know this line: in Lecture 7 you added `ghost_ship` to its list |
| 69 | `shared hulk_id =` | Keeps a note of which thing is the hulk, in a box named `hulk_id`. The block lower down uses it |
| 71 and 72 | `await task_schedule(` | Put the player ships on the map, and let them dock at the station |
| 74 | `game_end_condition_add(` | Ends the game if every player ship is destroyed |
| 78 | `task_schedule(watch_for_arrival)` | Starts `watch_for_arrival`, the block lower down |
| 79 | `->END` | Ends the map's lines |

Three things to notice. They are all you need to know about how this file works.

**The indent.** Line 25 starts at the left edge. Lines 31 to 79 start four spaces in. The
indent is what makes them part of the map. A block ends where the next line at the left
edge begins. A line that starts further in still, like line 92, belongs to the line above
it. Your cards have no such lines: every line under the first starts in the same column.

**`->END`.** It means "this block is finished". Line 79 ends the map's lines. Line 105
ends the route. A line placed under `->END`, at the same indent, never runs.

**The two blocks at the bottom.** You know both from Lecture 7. Each one ends by saying a
signal. This is line 93:

```
            signal_emit("quest_signal", {"SIGNAL_NAME": "ghost_ship_found"})
```

In `mission.amd`, the step **Find the Derelict** says `Done when: signal ghost_ship_found`.
The same word. That step is not finished by a built-in verb such as `reach`. It is
finished by the script, which says the step's signal. The lines above line 93 decide
WHEN. You will paste a line of exactly this shape in Step 6, and decide the "when"
yourself.

## Step 2 - Your first edit: the map's name

The command in Lecture 3 gave your mission its title. It did not name the map inside it.
The map is still called "AMD Sample".

Go to line 25. Change the words between the quote marks:

```
@map/amd_sample "Salvage Run"
```

Go to line 26. Change the sentence:

```
" A dying hulk, a missing lifeboat, and ten minutes to bring her log home.
```

Three rules for these two lines:

1. On line 25, keep both quote marks. Leave `amd_sample` as it is: it is the map's key.
2. Line 26 has **one** quote mark, at the start, and none at the end. That is not a typing
   mistake. Leave it so.
3. Keep the description on one line, at the left edge. Do not press Enter in the middle
   of it.

Save with `Ctrl+S`.

## Step 3 - One check, two files

Since Lecture 6 the last line of lint's answer has said `1 amd + 1 mast file(s)`. The
`1 mast` is this file. Every time you ran lint, it also asked whether the game could read
`story.mast`. It had nothing to say, because the file was never broken.

Run it now:

```
sbs lint MyMission
```

It says `clean`.

Then see what a broken story looks like, once, on purpose. Delete the second quote mark on
line 25, save, and run lint again.

```
== mission.amd ==
  clean
== story.mast (compile) ==
  [ERROR] line 25: Unrecognized syntax; no MAST node matched this line: '@map/amd_sample "Salvage Run'. The story does not compile, so NOTHING in this mission runs until this is fixed (mast-compile)

1 amd + 1 mast file(s): 1 error(s), 0 warning(s)
```

| In the message | In plain words |
|---|---|
| `== story.mast (compile) ==` | The lines below are about `story.mast`. To compile a file is to read every line of it and check that each one can be followed. The game does that before it runs anything |
| `line 25` | The line of `story.mast` |
| `Unrecognized syntax; no MAST node matched this line` | A programmer's way of saying: I cannot read this line |
| `'@map/amd_sample "Salvage Run'` | The line itself, as lint read it. Look for what is missing |
| `The story does not compile, so NOTHING in this mission runs` | What the game does about it |

Put the quote mark back, save, and run lint: `clean`.

**A `story.mast` that does not compile runs nothing.** No map, no station, no ships, no
quests. Not one line of the file is used, however small the mistake. So from now on: lint
after every change to this file, before you start the game.

Lecture 2 showed you a second command in a report, `sbs compile`. It reads `story.mast`
alone. It prints the same error in another shape, and nothing at all when the file is
good. You do not need it. Lint runs it for you.

## Step 4 - A step that waits for the script

Open `mission.amd`. The story runs hulk, lifeboat, home. You are putting a wait in before
home.

First, in **Find the Lifeboat**, change the `Then:` line so it reveals the new step:

```
Then: reveal salvage/tug
```

Then leave one blank line under Find the Lifeboat's description, and type this above
**Bring the Log Home**:

```
#### [Wait for the Tug](tug)
---
Scope: shared
Starts when: revealed
Objective: Hold near the lifeboat until the tug arrives
Done when: signal tug_arrived
Reward: 50 credits
Then: reveal salvage/home
Part of: salvage
Required: true
---
DS 1 is sending a tug for the lifeboat. Stay with her until it gets here.
```

Leave one blank line after it.

One line is new for this arc: `Done when: signal tug_arrived`. No built-in verb finishes
this step. It waits to hear the signal `tug_arrived`. The word is yours to choose, by the
four rules of Lecture 7: small letters and underscores, and the same in both files.

Save. Run lint. It has something to say:

```
== mission.amd ==
  [WARNING] line 90:19: `tug` waits for the signal `tug_arrived`, and nothing in the mission sends it, so that wait never ends. Check the spelling against the line in the story that sends it (unfired-signal)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

You met this warning in Lecture 7, Step 5. Lint is right. Nothing sends that signal yet.
The next three steps build the thing that does.

## Step 5 - Card 1: when a step starts

Open `story.mast`. Go to the very end, below the last `->END` on line 105. Leave two
blank lines. Then paste this, with the first four lines at the left edge:

```
#
# Wait for the Tug: what happens when that step starts.
#
//shared/signal/quest_started if QUEST_ID == "salvage/tug"
    npc_spawn(5600, 0, 6000, "Salvage Tug", "tsn, tug", "cargo_ship", "behav_npcship")
    ->END
```

| Line | Meaning |
|---|---|
| The three `#` lines | A note, so that next month you know what this block is |
| `//shared/signal/quest_started` | A route. The game says `quest_started` each time a hidden step is revealed, and this block hears it |
| `if QUEST_ID == "salvage/tug"` | Only when the step that started is this one. It is the step's full address, the one you write after `Then: reveal` |
| The `npc_spawn` line | Puts a ship on the map |
| `->END` | The block is finished |

You have read a line like the `npc_spawn` one before: line 68 puts the hulk on the map
the same way. It holds the same facts as a Landmarks record.

| On the line | In a Landmarks record | Here |
|---|---|---|
| `5600, 0, 6000` | `Loc:` | Where. This is 400 from the lifeboat |
| `"Salvage Tug"` | The name in the heading | Its name |
| `"tsn, tug"` | `Side:`, then `Roles:` | Its side, a comma, then its role. The side comes first, as on line 68 |
| `"cargo_ship"` | `Art:` | What it looks like |
| `"behav_npcship"` | `Kind: ship` | It is a ship. Leave this word alone |

The difference is **when**. A Landmarks record is on the map from the start. This ship
arrives when the story says so.

Save. Run lint. It repeats its warning from Step 4, because nothing finishes the step yet.
It says nothing about `story.mast`: the game can read your card. If you play it now, the
tug appears the moment **Wait for the Tug** appears, and the step stays open for good.

## Step 6 - Card 2: finish a step

Put your cursor at the end of the `npc_spawn` line and press Enter. Type this on the new
line, lined up with the line above it:

```
    signal_emit("quest_signal", {"SIGNAL_NAME": "tug_arrived"})
```

It is the line you read on line 93. Only the last word in quotes is yours. It is the word
after `Done when: signal` in your step.

Save. Run lint. It says `clean`: now something sends the signal. If you play it, the tug
appears and the step shows `Done` in the same moment.

## Step 7 - Card 3: wait

Put your cursor at the end of the line that begins `//shared/signal` and press Enter.
Type this on the new line, lined up with the lines below it:

```
    await delay_sim(20)
```

The number is seconds of game time. The lines run from the top down, so the block now
waits, then brings the tug in, then finishes the step.

Save. Run lint: `clean`.

Now keep your word list true. You have a new role and a new signal. At the top of
`mission.amd`, add the role under the `lifeboat` line:

```
// ROLE    tug               worn by the Salvage Tug, once it arrives
```

And add the signal at the end of the list:

```
// SIGNAL  tug_arrived       said twenty seconds after Wait for the Tug starts
```

Save. Run lint: `clean`.

## Your finished card

At the end of `story.mast`:

```
#
# Wait for the Tug: what happens when that step starts.
#
//shared/signal/quest_started if QUEST_ID == "salvage/tug"
    await delay_sim(20)
    npc_spawn(5600, 0, 6000, "Salvage Tug", "tsn, tug", "cargo_ship", "behav_npcship")
    signal_emit("quest_signal", {"SIGNAL_NAME": "tug_arrived"})
    ->END
```

At the top of `mission.amd`:

```
// ---- Words this file shares with story.mast. Keep this list true.
// ROLE    derelict          worn by the Unknown Hulk
// ROLE    ghost_ship        worn by the Unknown Hulk
// ROLE    lifeboat          worn by The Lifeboat, a landmark in this file
// ROLE    tug               worn by the Salvage Tug, once it arrives
// SIGNAL  ghost_ship_found  said when a ship comes within 2000 of the hulk
// SIGNAL  derelict_scanned  said when Science scans anything that wears derelict
// SIGNAL  tug_arrived       said twenty seconds after Wait for the Tug starts
```

In `mission.amd`, inside Salvage Run:

```
#### [Find the Lifeboat](boat)
---
Scope: shared
Starts when: revealed
Objective: Get within 500 of the hulk's lifeboat
Done when: reach lifeboat 500
Reward: 100 credits
Then: reveal salvage/tug
Part of: salvage
Required: true
---
Her log is not aboard, and one lifeboat cradle is empty. Find the boat.

#### [Wait for the Tug](tug)
---
Scope: shared
Starts when: revealed
Objective: Hold near the lifeboat until the tug arrives
Done when: signal tug_arrived
Reward: 50 credits
Then: reveal salvage/home
Part of: salvage
Required: true
---
DS 1 is sending a tug for the lifeboat. Stay with her until it gets here.
```

Both whole files are in `example\`.

## Step 8 - Check it

```
sbs lint MyMission
```

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

### One finding to see before you need it

The slip a pasted line makes most often is to land one line too low. Make it once, on
purpose.

In your card, move the `signal_emit` line below `->END`, so that the card's last two
lines change places. Save. Run lint.

```
== mission.amd ==
  clean
== story.mast ==
  [WARNING] line 115: this line never runs: the label ended at `->END` on line 114. If this line belongs to that label, move it above line 114. If line 114 is the end of something you pasted INTO a label, move what you pasted to the end of the file: it cut the label in two (mast-unreachable)

1 amd + 1 mast file(s): 0 error(s), 1 warning(s)
```

| In the message | In plain words |
|---|---|
| `== story.mast ==` | The lines below are about `story.mast`. This time the game CAN read the file, so the word `(compile)` is not there |
| `the label` | Lint's word for a block |
| `ended at ->END on line 114` | Line 114 finished the block |
| `this line never runs` | Line 115 is under it, in the same block, so the game never gets to it |
| `Move it above that line` | The fix |

It is only a warning, and the mission runs. If you played it, the tug would arrive and
Wait for the Tug would never finish. Lecture 6 said it: a warning can stop your story as
surely as an error.

Move the line back above `->END`. Save. Run lint: `clean`.

### What lint says about the rest

Every row below was tried on this mission, one at a time. Lint was run. Then the game was
run without a screen, by a script that put the ship beside the hulk, then beside the
lifeboat, and waited there. The last column is the code at the end of lint's line. A
finding about a line of `story.mast` is printed under `== story.mast (compile) ==` when
the game cannot read the file, and under `== story.mast ==` when it can.

"Nothing runs" means what Step 3 said: no map, no station, no ships, no quests.

**Where the card goes:**

| Mistake | What the game does | Lint says |
|---|---|---|
| Pasted in the middle of the map's lines, at the left edge | The game starts with no station and no hulk. Every map line below your card is cut off from the map | `mast-unreachable`, a warning. It names the first map line below your card, and says to move that line up. Do not. Move the CARD, to the end of the file |
| Pasted in the middle of the map's lines, indented to match them | Nothing runs | `mast-compile`, an error. It says `Bad indentation`, and the line it names is the map line AFTER your card |
| Pasted in the middle of `watch_for_arrival` | Your card works. The template's own first step, Find the Derelict, never finishes | `mast-unreachable`, a warning. It names the line below your card |
| Pasted at the very top of the file | Nothing runs | `mast-compile`, an error. It says `Bad indentation`, at `shared MISSION_DOC = None` |
| A line of the card typed below its `->END` | That line never runs. If it is the `signal_emit` line, the tug arrives and the step never finishes | `mast-unreachable`, a warning, on that line |
| A line typed below the map's `->END` on line 79 | That line never runs | `mast-unreachable`, a warning, on that line |

**The indent:**

| Mistake | What the game does | Lint says |
|---|---|---|
| One line has three spaces, or five, or a tab, and the others have four | Nothing runs | `mast-compile`, an error. It says `Bad indentation`, on that line |
| One line at the left edge and the others indented: the `signal_emit` line, or `->END` | Nothing runs | `mast-compile`, an error. `Bad indentation`, on that line |
| The FIRST line under the route line at the left edge, the rest indented | Nothing runs | `mast-compile` three times. `Bad indentation` on each of the three lines BELOW the one you got wrong |

**The two lines of the map** (lines 25 and 26):

| Mistake | What the game does | Lint says |
|---|---|---|
| A quote mark of the map's name deleted: one, or both | Nothing runs | `mast-compile`, an error, on line 25 |
| The quote mark at the start of the description deleted | Nothing runs | `mast-compile`, an error, on line 26 |
| Enter pressed in the middle of the description | Nothing runs | `mast-compile`, an error. It names line 27, the second half of your sentence |
| The description line indented | Nothing runs | `mast-compile`, an error. It says `Bad indentation`, and names the `metadata:` block below, not your line |
| A space in the map's key: `@map/salvage run` | Nothing runs | `mast-compile`, an error, on line 25 |

**Inside a line of the card:**

| Mistake | What the game does | Lint says |
|---|---|---|
| A closing quote mark left off the tug's name, or the signal's name | Nothing runs | `mast-compile`, an error. It says `unterminated string literal`. On the `signal_emit` line you get `unfired-signal` as well |
| The closing quote mark of the address left off, or one `=` where two go | Nothing runs | `mast-compile` twice. The first names your line. The second says `line 1` and is the same mistake again: ignore its number |
| A comma left out of the `npc_spawn` line | Nothing runs | `mast-compile`, an error. It asks `Perhaps you forgot a comma?` |
| The last bracket left off a line, or the closing curly bracket | Nothing runs | `mast-compile`, an error. The line it shows has the next line stuck on the end |
| Round brackets where the curly ones go | Nothing runs | `mast-compile`, an error. It says `invalid syntax` |
| One slash at the start of the route line, or a space after the two | Nothing runs | `mast-compile`, an error. It says `invalid syntax` |
| A colon typed at the end of the route line | Nothing runs | `mast-compile`, an error. The line it shows is the colon alone |
| A note of your own that starts with `//` | Nothing runs. In this file a note starts with `#` | `mast-compile`, an error. It says `Unrecognized syntax` |
| `If` or `Await` with a capital | Nothing runs | `mast-compile`, an error |
| `END` without its arrow, or `=>END` | Nothing runs | `mast-compile`, an error |
| `await delay_sim(20 seconds)`, `await delay_sim 20`, or `wait 20` | Nothing runs. The number goes alone, inside the brackets | `mast-compile`, an error |
| Curly quote marks, pasted from a word processor, where straight ones go | Nothing runs | `mast-compile`, an error. On a line of the card it says `invalid character`. On line 25 it says `Unrecognized syntax` |
| `//signal/` with `shared/` left out | Played on the server alone, it works | `signal-side-effect-spawn`, a warning. It says the block runs once for every console. Believe it: put `shared/` back |

**Words that have to match:**

| Mistake | What the game does | Lint says |
|---|---|---|
| The signal's name on the card is not the one in `mission.amd` | The tug arrives, and the step never finishes | `unfired-signal` |
| `signal_emit("tug_arrived")`, the short way. Or `"quest_signal"` misspelled, or changed to your word | The same. A quest hears nothing that is not sent as `quest_signal` | `unfired-signal`, with another sentence: it gives the line to write |
| `"SIGNAL_NAME"` in small letters, or misspelled | The same. `mast.runtime.log` gets one line: "a `quest_signal` was sent with no name" | `unfired-signal` |
| A `#` in front of the `signal_emit` line, or the line left out | The same | `unfired-signal`. A note does not send anything |
| No quote marks round the signal's name | An error page when the tug is due | `unfired-signal` |
| The colon after `"SIGNAL_NAME"` left out | An error page when the tug is due | `unfired-signal` |
| `Done when: tug_arrived` (the word `signal` left out) | The tug arrives, and the step never finishes | `unknown-trigger`. Its sentence lists what you can write |
| No `Then:` line on Wait for the Tug | The step finishes, and Bring the Log Home never appears | `never-revealed`, about Bring the Log Home |

When lint names a line of `story.mast` that you did not touch, look just above it.
`Bad indentation` names the first line that no longer fits, which is often the line
after the one you got wrong.

### What lint cannot see

For every row below lint says `clean`. Both logs stay empty too.

| You wrote | What happens |
|---|---|
| An address in the route line that is not your step's: misspelled, `"tug"` with no arc and slash, `"Salvage/Tug"` with capitals, `"salvage / tug"` with spaces. Or your step has another key in `mission.amd` | The card never runs. No tug, and the step never finishes. After `Then: reveal`, lint checks an address for you. Here nothing does |
| No `if QUEST_ID == ...` on the route line | The card runs every time ANY step starts. In this story that is four tugs, and Wait for the Tug finishes early, when the first of them arrives |
| `quest_start`, `quest_activated` or `Quest_Started` where `quest_started` goes | The card never runs |
| The address of a step that says `Starts when: at once`. Or Wait for the Tug itself changed to `at once` | The card never runs. `quest_started` is said only for a step that was hidden and then revealed |
| `delay_sim(20)` with no `await`, or `await delay_sim()` with no number | No wait. The tug is there the moment the step appears |
| Find the Lifeboat still says `Then: reveal salvage/home` | Wait for the Tug never appears. Bring the Log Home appears at the lifeboat, the crew flies home, and the game does not end. Before your card was in the file lint caught this, as `never-revealed`. It cannot now: the card's own lines name `tug`, and lint takes that for the story starting the step itself |
| The card pasted twice | Two tugs |
| The side left out of the tug's list: `"tug"`. Or the role typed first: `"tug, tsn"` | The tug is on a side called `tug`, which is no side at all. The first word is the side |
| A misspelled `Art` word such as `cargo_shp` | The test places the ship all the same, and the test draws nothing. In the real game it stopped nothing. Nobody has looked at what it draws. Copy the word from Lecture 10's table |
| A long dash in the map's name | The game cannot draw that mark. In `mission.amd`, and in a ship's name, it swaps in the plain one for you. In a map's name nothing does. Nobody has looked at what the real game shows there. Type the plain mark |
| A closing quote mark typed at the end of the description on line 26 | The quote mark is shown as part of the description |
| The description line deleted | The map has no description |

Four more stop the game instead of going quiet. Lint says `clean` for them too.

| You wrote | What happens |
|---|---|
| `quest_id` in small letters, or the address with no quote marks | An error page the first time any step is revealed: here, at the hulk |
| Two numbers where the `npc_spawn` line needs three, or commas inside the numbers: `5,600` | An error page when the tug is due |
| A word outside the quote marks misspelled: `npc_spwan`, or `delay_sm` | An error page when that line's turn comes |
| `await delay_sim("20")`, the number in quote marks | An error page when the step starts |

After an error page, `mast.runtime.log` in your mission folder has the reason. It is long,
and written for programmers. Search it for the words `in file:`. The number in front of
them is the line of `story.mast` that failed.

So check five things by eye:

1. The address in quotes is the one you wrote after `Then: reveal`, in small letters, with
   no spaces.
2. The route line says `quest_started`. It has `if`, and `==` with two equals signs.
3. `await` is in front of `delay_sim`, and the number is inside the brackets.
4. The card is in the file once, at the end.
5. Find the Lifeboat's `Then:` line names `salvage/tug`.

One thing that looks wrong and is not. This works in the game, and lint agrees:

| You wrote | Lint says |
|---|---|
| The whole card indented four spaces, or only its route line | `clean`, and it plays the same. Keep the card at the left edge all the same: that is where every other route in the file starts |

### These are fine

| You wrote | Result |
|---|---|
| Every line under the route line with three spaces, or two, or a tab, or none | Works. What matters is that the lines agree with each other. Four spaces is what the file uses |
| The card pasted between two blocks, at the left edge | Works. The end of the file is still the place that cannot go wrong |
| One blank line above the card, or none | Works |
| The card without its three `#` lines | Works. Next month you will wish they were there |
| A blank line between the card's lines | Works |
| A `#` note between the card's lines, or at the end of a line | Works |
| `-> END` with a space, or `->end` in small letters | Works. Keep it as the file has it |
| The card's `->END` left off | Works. A route also ends where the next block begins. Type it anyway |
| Single quote marks round the address, or no spaces round the `==` | Works |
| The signal's name with capitals, or with a space for its underscore, in either file | Works. You saw this in Lecture 7 |
| A space before the bracket: `delay_sim (20)` | Works |
| An apostrophe in the tug's name, or curly brackets | Works. The name is kept as typed. A curly apostrophe is changed to the plain one |
| An apostrophe in the map's name. Curly brackets, an apostrophe or a quoted word in the description | Works |
| A long dash or curly quote marks inside a `#` note | Works. The game skips a note |
| Both files saved with Windows line endings | Works |

## Step 9 - Play it

Start your mission as the server with a Helm console, the way you did in Lecture 3.

1. On Helm, open the Quest Log, as you did in Lecture 8: the handheld icon at the top,
   then **Quests**. **Salvage Run** is there with two steps under it: Close Inspection and
   Quick Work.
2. Fly to the Unknown Hulk. Inside 500, Close Inspection shows `Done`, and **Find the
   Lifeboat** is now in the list.
3. Fly to The Lifeboat. Inside 500, Find the Lifeboat shows `Done`, and **Wait for the
   Tug** is now in the list. There is no tug on the map.
4. Wait. Twenty seconds later the **Salvage Tug** is on the map, 400 from the lifeboat.
   Wait for the Tug shows `Done`, and **Bring the Log Home** is now in the list.
5. Fly back to DS 1. Inside 1000, the game ends with your `Win:` sentence.
6. Close the game. Open `mast.compile.log` and `mast.runtime.log`. Both are empty.

First Contact, the template's own story, finishes its steps at the hulk too, as it has
since Lecture 9.

What the side is paid:

| Ending | Credits |
|---|---|
| Won, with the bonus | 500 |
| Won, bonus missed | 450 |

A quest of your own from Lecture 8's exercise pays its reward on top of these.

The tug does not move. It has arrived, and that is all this card does.

To see your map's new name, start the game once more with `map=0` left off the line.
The server then shows its start screen, and waits. The map is listed there as **Salvage
Run**, with your description.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| Lint prints `== story.mast (compile) ==` and an error | A line of `story.mast` cannot be read. Lint gives the line. If it names a line you did not touch, look just above it |
| A second `mast-compile` line that says `line 1` | It is the first one again. Fix the line the first one names |
| Your mission starts, and a page headed "Mast Compiler Errors" is there in place of the game | `story.mast` does not compile, and you did not run lint. Run it, and fix the line it names |
| The game was running and stopped with a page of errors | A line was wrong in a way lint cannot see. Open `mast.runtime.log` in your mission folder and search it for `in file:`. The number in front is the line. Then read the second table of "What lint cannot see" |
| Lint says `mast-unreachable` | A line is under an `->END` in the same block. If the line it names is yours, move it up. If it is the template's, your card is in the middle of a block: move the card to the end of the file |
| Lint says `unfired-signal` | The word after `"SIGNAL_NAME":` on your card is not the word after `Done when: signal`, or the `signal_emit` line is missing, is a note, or has lost its `"quest_signal"` |
| The map is still called "AMD Sample" | Line 25 was not saved |
| No station and no hulk | The card is in the middle of the map's lines. Move it to the end of the file |
| Wait for the Tug never appears | Find the Lifeboat does not say `Then: reveal salvage/tug` |
| Wait for the Tug appears, and no tug ever comes | The address in the route line is not `salvage/tug` letter for letter, or the route line says something other than `quest_started` |
| The tug comes, and the step never finishes | The `signal_emit` line is missing, is below `->END`, or does not say `"quest_signal"` and your signal's name. Lint warns about each of these |
| `mast.runtime.log` says a `quest_signal` was sent with no name | `SIGNAL_NAME` on your card is misspelled or in small letters |
| The tug is there the moment the step appears | No `await` in front of `delay_sim`, or no number in its brackets |
| Four tugs | The route line has no `if` |
| Two tugs | The card is in the file twice |

## Your recipe cards

Three cards. Keep them. Later classes hand you more, and every one of them is pasted the
same two ways: a block at the end of the file, or a line inside a block, lined up with
its neighbors.

**Card 1 - When.** A block at the end of `story.mast`:

```
//shared/signal/quest_started if QUEST_ID == "salvage/tug"
    (your lines go here)
    ->END
```

| Change | To |
|---|---|
| `quest_started` | `quest_started`: the step starts. Only for a step with `Starts when: revealed` |
| | `quest_succeeded`: the step is finished. Any step |
| | `quest_failed_done`: the step failed |
| `salvage/tug` | The step's full address, in small letters, with no spaces |

**Card 2 - Finish a step.** A line inside a block, with `Done when: signal tug_arrived`
on the step:

```
    signal_emit("quest_signal", {"SIGNAL_NAME": "tug_arrived"})
```

| Change | To |
|---|---|
| `tug_arrived` | The word after `Done when: signal` on your step |

**Card 3 - Wait.** A line inside a block:

```
    await delay_sim(20)
```

| Change | To |
|---|---|
| `20` | A number of seconds |

And one line that is not a card of its own, because a Landmarks record does the same job
at the start of the game. Use it inside Card 1 for a ship that arrives later:

```
    npc_spawn(5600, 0, 6000, "Salvage Tug", "tsn, tug", "cargo_ship", "behav_npcship")
```

| Change | To |
|---|---|
| `5600, 0, 6000` | Where. Three plain numbers |
| `Salvage Tug` | Its name |
| `tug` | Its role. Keep `tsn, ` in front of it |
| `cargo_ship` | An `Art` word from Lecture 10 |

## Exercise

Make something of your own arrive when a step is **finished**.

1. At the end of `story.mast`, leave two blank lines and paste Card 1 again.
2. Change `quest_started` to `quest_succeeded`, and the address to `salvage/approach`.
3. Give it one line: the `npc_spawn` line, with a name of your own, a role of your own,
   and `600, 0, 9000` for the place. That is beside the hulk.
4. Add a note above it, with `#`, that says what the block is for.
5. In your first card, change the wait from 20 to a number of your own.
6. Add your new role to the word list at the top of `mission.amd`.
7. Run lint. Then play it: your ship arrives as Close Inspection shows `Done`.

## Checkpoint

You are done when all six are true:

- `sbs lint MyMission` answers `clean`, with `0 error(s), 0 warning(s)`.
- You can point at a block of `story.mast` and say whether it is a label or a route, and
  where it ends.
- Wait for the Tug appears when the crew reaches the lifeboat, and not before.
- Twenty seconds later the tug is on the map, the step shows `Done`, and Bring the Log
  Home appears.
- Reaching DS 1 ends the game with your `Win:` sentence.
- After the play, `mast.compile.log` and `mast.runtime.log` are both empty.

## Next

Lecture 12 is the capstone: a three-step arc of your own, packaged and shared.

## Further reading

- "Quests" in the library documentation, the part called "Signals": the signals a quest
  sends and the ones it listens for.
- "Signal routes" in the library documentation: what `//shared/signal` means, and why the
  word `shared` is there.
- "The `sbs` CLI" in the library documentation, the part called "Does the story compile,
  and does every line run". It is about the two findings you met today.
- "The MAST language": an overview for the curious. Nothing in this course needs it.
