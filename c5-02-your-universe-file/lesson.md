# Class 5, Lecture 2 - Your universe file

## What you will have at the end

A mission of your own that runs on the Open Universe engine. Your title is in the mission
list and on the start screen. The place the crew starts has a name and a line that you
wrote. The crew can leave that place and come back to it. And a game you stop today can be
continued tomorrow.

*[Screenshot to add: the card the crew sees on arrival, reading Kestrel Relay.]*

You will write one file of your own, `kestrel_verge.amd`, and change a few marked words in
`story.mast`.

## The video

*[Link to add when recorded.]*

## Before you start

- You have finished Classes 1 and 2. You can write a record and run `sbs lint`.
- You played The Silver Reach in Lecture 1.
- VS Code with the Artemis AMD extension.
- A command prompt open in your `missions` folder.

In this page the mission folder is called `MyUniverse` and the universe is called The
Kestrel Verge. Use your own names. The exercise at the end is where you make it yours.

## Step 1 - Make the mission

```
sbs create MyUniverse -t ou --title "The Kestrel Verge"
```

`ou` is the Open Universe template. `--title` is the name in the mission list.

| Rule for the title | Why |
|---|---|
| Letters, numbers and spaces only | The title is copied into small settings files that read punctuation as instructions |
| No hyphen | A hyphen in the mission-list file stops the game from starting. Not only your mission: the whole game |
| No colon | `sbs create` refuses it, and in Step 7 it would stop your mission from loading |
| No apostrophe | The mission list may show it wrongly |
| 40 characters at most | `sbs create` refuses a longer one |

Now check what you were given:

```
sbs lint MyUniverse
```

It should say `clean`. A new mission from this template is clean before you touch it.

## Step 2 - What is in the folder

| File | What it is | Today |
|---|---|---|
| `my_universe.amd` | The universe. This is the file you write | Rename it and edit it |
| `story.mast` | Tells the game which universe file to load and what to call it | Change the marked words |
| `description.yaml` | The line in the mission list | Already has your title |
| `settings.yaml`, `story.json`, `script.py`, `__lib__.json` | The machinery | Leave them alone |

## Step 3 - Give the file your name

In VS Code, right-click `my_universe.amd` and choose **Rename**. Call it:

```
kestrel_verge.amd
```

Small letters, underscores for spaces, and `.amd` on the end.

## Step 4 - The title record

Open `kestrel_verge.amd`. The lines at the top that start with `//` are notes. Leave them.

Below the notes is one record with a single `#`. Change it to read:

```
# [The Kestrel Verge](kestrel_verge)
---
Universe
Display: The Kestrel Verge
---
Past the last relay the charts are forty years old, and nobody has come to correct them.
Three colonies were planted out here. Two still answer.
```

| Line | What it means |
|---|---|
| `# [The Kestrel Verge](kestrel_verge)` | One hash: this is the universe itself. The name in square brackets, then a key in round brackets |
| `Universe` | A word on its own line. It says what kind of record this is. Leave it |
| `Display: The Kestrel Verge` | The title again |
| The lines below the fence | What this universe is. Write it for yourself and your co-writers |

This record is the title page of your manuscript. The story tools from Class 2 print it.
**The game does not show it to players.** What players read comes from Step 6 and Step 7.

There is one `#` record in the file, and it is this one. Everything else in the file sits
under it with two hashes or three.

## Step 5 - The scenario

Directly under the title record, leave one empty line and add:

```
## [Scenario](scenario)
---
Mode: story
---
```

`Mode` says what kind of game this universe is.

| Word | Use it for |
|---|---|
| `story` | One ship, a story with an ending |
| `campaign` | One ship, a long game played over many sessions |
| `sandbox` | An open world with no ending. This is what you get if you write no `Mode` at all |
| `skirmish`, `war` | Fleets and admirals fighting each other. Leave these until Lecture 14 |

In a mission made from this template, `story`, `campaign` and `sandbox` play the same
today. The word starts to matter when the fleet game is added in Lectures 14 and 15. Write
the one that is true of your story.

The key in round brackets must be `scenario`. The game looks for that word.

## Step 6 - Name the place they start

The template already has two chapters, `## [Sides](sides)` and `## [Jobs](jobs)`. Leave
them. Lecture 3 and Lecture 6 replace them.

Go to the very end of the file and add:

```
## [Landmarks](landmarks)

### [Kestrel Relay](kestrel_relay)
---
At: 0, 0
Kind: station
---
The last relay anyone still maintains. Everything past it is rumor.
```

| Line | What it means |
|---|---|
| `## [Landmarks](landmarks)` | A chapter of named places. The key must be `landmarks` |
| `### [Kestrel Relay](kestrel_relay)` | Three hashes: one place. Its name, then its key |
| `At: 0, 0` | Which star system it is in. `0, 0` is home. Every new game starts there |
| `Kind: station` | It is a station |
| The line below the fence | What the crew is told when they arrive |

Three things happen because of this record:

1. When the crew arrives at home, a card names the system **Kestrel Relay** and shows your
   line under the name.
2. A station called Kestrel Relay is in the system. The game also puts its own station
   there, called Starbase. You will have both.
3. Kestrel Relay is written into the crew's list of charted places, so they can come back
   to it.

Keep the line under the fence on **one line**. The card shows the first line only.

This is one landmark, to give your universe a front door. Lecture 5 is the whole map.

## Step 7 - Tell the game about it

Open `story.mast`. You change four things. Do them in this order.

**1. The title.** Press `Ctrl+H`. In the first box type `My Universe`. The box should find
**4**. In the second box type your title, and press **Replace All**.

**2. The file name.** In the first box type `my_universe.amd`. It should find **2**. In
the second box type `kestrel_verge.amd`, and press **Replace All**.

If the counts are not 4 and 2, stop and look at what was found before you replace.

**3. The two lines the players read.** Find the line that starts `@map/`. The two lines
under it each start with a double quote. Replace them with two lines of your own:

```
" Past the last relay the charts are forty years old. Two colonies still answer.
" Take work at Kestrel Relay and find out what happened to the third.
```

| Rule for these lines | Why |
|---|---|
| Each starts at the left edge with a double quote and a space | Without the quote, or with spaces in front, the mission does not load |
| No curly brackets `{` `}` | They break the start screen |
| Plain keyboard characters only | The game cannot draw curly quotes or long dashes |

**4. Two lines to leave alone.** Near the top, under the `UNIVERSE_SELECT` line, are two
lines that let the crew travel. Do not change them:

```
default shared QUEST_ENGAGE_ENABLED = True
default shared WAYPOINTS_ENABLED = True
```

| Line | What it does |
|---|---|
| `QUEST_ENGAGE_ENABLED` | Puts the **Engage** button on Helm's Quests tab. Without it the crew can take a cargo run and never fly it |
| `WAYPOINTS_ENABLED` | Keeps a list of the named places the crew has been, so they can Engage a way back |

> **Not there?** Your mission was made from an older template. Type those two lines
> directly under the first `UNIVERSE_SELECT` line. Both start at the left edge, and `True`
> has a capital T.

When you are done, your title is in `story.mast` four times, spelled the same way each
time. The words `my_universe` with an underscore are still there in four places. Leave
them. They are names inside the machine, and players never see them.

## Step 8 - Check it

Two commands. The first reads your universe file. The second reads `story.mast`.

```
sbs lint MyUniverse
sbs compile MyUniverse
```

You want `clean` from the first. You want **nothing at all** from the second: when
`story.mast` is fine, `sbs compile` prints nothing and gives you the prompt back.

**What lint tells you about**

| Mistake in `kestrel_verge.amd` | What lint says |
|---|---|
| `Mode: storey` | A warning: not one of story, sandbox, skirmish, war, campaign. The game would ignore it |
| `Mode story`, with no colon | An error: expected `Label: value` |
| `### [Scenario](scenario)`, with three hashes | An error: the heading jumps from level 1 to 3 |
| `#### [Kestrel Relay](kestrel_relay)`, with four hashes | An error: the heading jumps from level 2 to 4 |
| The title record written with two hashes | An error: the heading jumps from level 0 to 2 |
| The title heading with no square brackets, or with no space after the `#` | The same error, but it names the line of the NEXT heading, not the title. Look one heading up |
| The closing `---` left off the title record | Several errors, the last one saying a fence was opened and never closed |
| `Dispaly:` | A warning: not a known field |
| A curly quote or a long dash in your prose | A warning with the line and the place in the line |
| `## [Landmarks](places)`, or the landmark written with two hashes | A warning that `Kind` is not a known field. It means the game does not see a landmark there |

Never play with a lint **error**. With a heading error the game cannot read the file at
all, and you get an empty universe.

**What lint does not tell you about**

Lint says `clean` for every one of these.

| Mistake in `kestrel_verge.amd` | What happens in the game |
|---|---|
| `# [Scenario](scenario)`, with one hash | Every chapter below it is lost: no sides, no jobs, no landmark. The game invents two factions named after your two headings |
| `## [Scenario](setup)`: any key but `scenario` | `Mode` is ignored |
| `Mode: story` written inside the title record | `Mode` is ignored |
| `## Scenario`, with no brackets and no key | `Mode` is ignored |
| `At: home`, `At: 0`, or no `At:` line | The landmark is nowhere. Home is called Home Port |
| The landmark's line written on two lines | The card shows the first line only |

So check these by eye:

- One hash on the title, two on `Scenario` and `Landmarks`, three on `Kestrel Relay`.
- The keys are `scenario` and `landmarks`, in round brackets.
- `At:` is two numbers with a comma.

**What `sbs compile` tells you about**

| Mistake in `story.mast` | What compile says |
|---|---|
| A colon in the title on the `display:` line | `mapping values are not allowed here` |
| A space in front of `display:` | The same |
| A description line with no quote at the start | `Unrecognized syntax` |
| A description line with spaces in front of it | `Bad indentation` |
| The closing quote missing after the title | `unterminated string literal` |
| The last `UNIVERSE_SELECT` line moved to the left edge, or indented with a tab | `Bad indentation` |

Each of these means nothing in the mission runs: no ship, no station. Compile also gives
the line number.

**What neither of them tells you about**

| Mistake in `story.mast` | What happens in the game |
|---|---|
| The title spelled two ways. One capital or one extra space is enough | The universe is not loaded. The game still starts, with no sides and no landmark |
| The file name after `universe:` is not your file's exact name | The same |
| One of the two travel lines changed or deleted | No Engage button, or no way back |
| Curly brackets in a description line | The start screen breaks |

If the game starts and your universe is not there, open the file `mast.runtime.log` in
your mission folder. When the universe could not be loaded, it says so there. If it names a
file called `sides.amd`, the title is spelled two ways.

## Step 9 - Play it

Start the game as the server with a Comms console and a Helm console, the way you did in
Lecture 1.

1. Choose your mission. The start screen shows your title and your two lines. Leave
   **Start** on **Continue**. There is nothing to continue yet, so a new game begins.
2. Press **Start Mission**. A card names the system **Kestrel Relay**, with your line.
3. On Comms, select a station and choose **Accept Cargo Run**. A cargo run is a quest to
   carry freight to another system.
4. On Helm, open the **Quests** tab. Select the cargo run and press **Engage**. The ship
   jumps to that system, and the run pays 400 credits on arrival.
5. In the Quests tab, find **Charted Locations**. Kestrel Relay is in it.
6. Stop the game. Do not go home first.

Now look at what the game kept. In your `missions` folder, open:

```
common_data\saves\universe_save_the_kestrel_verge_1.yaml
```

Near the top, `current_system` holds the two numbers of the system you stopped in.

7. Start the game again. Leave **Start** on **Continue**, and press **Start Mission**.
   You are in the system you stopped in, with the pay from the cargo run.
8. On Helm's Quests tab, select **Kestrel Relay** under Charted Locations and press
   **Engage**. You are home, and the card says so.

**What you need to know about the save**

| Fact | What it means for you |
|---|---|
| The file is named after the title in `story.mast`, in small letters with underscores, then `_1` | Change the title and the game starts a new, empty save. The old file stays where it was |
| **New Game** on the start screen replaces the save | It does not ask first |
| Two missions with the same title use the same file | Give each universe its own title. A mission left as `My Universe` shares a save with every other mission left that way |

## If something goes wrong

| What you see | Likely cause |
|---|---|
| The game will not start at all since you made the mission | A hyphen in the title. Open `description.yaml` in your mission folder and take it out of `Visible Mission Name` and `Description` |
| The start screen says My Universe | Step 7, part 1 was not done. Replace All should have reported 4 |
| The game starts, home is called Home Port, and there is no Kestrel Relay | The universe file was not loaded, or the landmark was not. Read `mast.runtime.log`. Then check the title is spelled one way, the file name after `universe:` is right, and the landmark has `At: 0, 0` |
| No ship and no station. Nothing happens | `story.mast` is broken. Run `sbs compile MyUniverse` |
| No **Engage** button on Helm's Quests tab | The two travel lines are missing or changed. See Step 7, part 4 |
| **Continue** begins a new game | The title changed since you last played, or **Start** was on **New Game** |
| **Continue** puts you somewhere you have never been | Another mission has the same title and wrote that save |
| Lint reports a heading error on a line that looks right | Look at the heading above it. The title heading is missing its square brackets, or the space after `#` |
| The start screen is broken or empty | Curly brackets in one of the two lines under `@map/` |

## Exercise

Make the universe yours.

1. Choose a title: letters, numbers and spaces.
2. Do Steps 3 to 7 again with your own names: the file name, the title record, and both
   Replace All commands. This time the first box holds `The Kestrel Verge` and
   `kestrel_verge.amd`.
3. Write your own two lines for the start screen, and your own home port: a name, a key,
   and one line.
4. Choose your `Mode`.
5. Before you play, write down the name the save file will have. Then run lint and
   compile, play, take a cargo run, stop, and look in `common_data\saves`. Were you right?
6. Break it once on purpose. Change one letter of the title on the `display:` line only.
   Run lint and compile: both are happy. Play: your universe is gone. Read
   `mast.runtime.log`. Then put the letter back.

## Checkpoint

You are done when all five are true:

- `sbs lint MyUniverse` says `clean`, and `sbs compile MyUniverse` prints nothing.
- The start screen shows your title and your two lines.
- On arrival, the card names your home port and shows your line.
- Helm's Quests tab has an **Engage** button, and Charted Locations lists your home port.
- After you stop in another system and choose **Continue**, you are in that system.

## Next

Lecture 3 replaces the two factions that came with the template with three of your own,
and says who fights whom.

## Further reading

- "Getting started" in the Open Universe writer's walkthrough. It describes adding a
  universe to the Open Universe mission itself, where the list of universes is in a file
  called `universes.mast` and you pick one from a dropdown. In your own mission the same
  entry is in `story.mast`, there is no dropdown, and the title has to match in four
  places.
- `scout_signal.amd` in the Open Universe mission: a short universe with a scenario, a
  story and one landmark, to read as a whole.
- "The AMD file format" in the library documentation: headings, fences, and how a record
  says what it is.
