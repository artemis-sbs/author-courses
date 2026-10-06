# Class 1, Lecture 12 - Capstone: ship a quest mission

## What you will have at the end

Four things.

The mission you built in Lectures 3 to 11 tells **your** story: every word a player reads
is yours. It has been checked the way this class taught. It exists as a document you can
print. And another person has it on their own computer and can play it.

*[Screenshot to add: the server's list of missions with your title in it, beside the first
page of your printed story.]*

This lecture teaches no new record and no new card. It asks you to finish. You will edit
four files, type six commands you mostly know, and make one zip file.

The worked example on this page turns "The Cold Hulk" into a story called **The Quiet
Lantern**. Yours will be different. Use the example to see where each change goes.

## The video

*[Link to add when recorded.]*

## Before you start

- Your mission as Lecture 11 left it: **Salvage Run**, with **Wait for the Tug** in it.
- `sbs lint MyMission` says `clean`.
- VS Code with the mission folder open, a command prompt open in `data\missions`, and the
  game closed.
- A friend who has the game, or a second computer. Step 8 needs one.

This page leans on earlier ones and does not explain them again.

| Lecture | What you learned there |
|---|---|
| 2 | The command prompt in `data\missions`, `sbs version`, `sbs update`, and how to read `sbs doctor` |
| 3 | `sbs fetch "MyMission" --update-libs`, and the line that starts the game |
| 6 | Lint: fix the first finding first. Then play, and read the two logs |
| 7 | Roles and signals, the folder search (`Ctrl+Shift+F`), and your word list |
| 9 | An arc, `Win:` and `Lose:` |
| 11 | The lines of `story.mast`, and the three rules for changing one |

Words for this lecture:

| Word | Meaning |
|---|---|
| Name | The words in square brackets in a heading, or between quote marks in `story.mast`. A player reads them |
| Key | The word in round brackets in a heading. The game uses it. A player never reads it |
| Zip file | One file that holds a whole folder, made small. It is how a folder is sent to someone |

Line numbers on this page are for files that match Lecture 11's finished ones:
`mission.amd` 185 lines, `story.mast` 115 lines. If yours are a little out, go by what the
line begins with.

## Step 1 - Plan your story on paper

Do not start by typing. The mission you have is a shape with slots in it. Write your story
into the slots first.

| Slot | Its key or role | In the taught mission | In "The Quiet Lantern" | Yours |
|---|---|---|---|---|
| The mission | | The Cold Hulk | The Quiet Lantern | |
| The crew's ship | | Artemis | Kittiwake | |
| Home | `station` | DS 1 | Marrow Station | |
| The thing they go out to | `derelict`, `ghost_ship` | Unknown Hulk | Lantern Nine, a dark beacon | |
| The thing they find next | `lifeboat` | The Lifeboat | The Keeper's Skiff | |
| The thing that arrives later | `tug` | Salvage Tug | Tender Osprey | |
| The first arc | `first_contact` | First Contact | The Dark Beacon | |
| The main arc | `salvage` | Salvage Run | The Keeper | |
| Step 1: go there | `approach` | Close Inspection | Come Alongside | |
| Step 2: find the second thing | `boat` | Find the Lifeboat | Find the Skiff | |
| Step 3: wait | `tug` | Wait for the Tug | Wait for the Tender | |
| Step 4: go home | `home` | Bring the Log Home | Bring Her Home | |
| The bonus | `quick` | Quick Work | First on Scene | |
| Why ten minutes | | The reactor is failing | A storm is coming | |

The shape stays: go out, find a second thing, wait, come home, against a clock. What the
things ARE, who is in danger and why the clock runs is all yours.

Fill in the last column before you go on. A capstone asks for an arc of at least three
steps in a chain. This one has four, and a bonus.

## Step 2 - Make it yours: the words

**One rule for this whole step: change names and sentences. Leave every key.**

A key such as `(salvage)` or a role such as `derelict` is a handle. No screen of the game
shows it to a player. So your story about a lighthouse can keep a role called `derelict`,
and nobody who plays will ever know. Changing only the words is the one kind of change
that cannot break the chain. The example changes 58 things this way and no key at all.

Work down this list. It is everything a player or a reader sees, and where it lives.

**In `mission.amd`:**

| What | Where | How many |
|---|---|---|
| The title of the file | Line 10, in the square brackets: `# [Sample Mission](sample_mission)` | 1 |
| Arc and step names | The square brackets of each `###` and `####` heading under Quests | 9 |
| Arc and step descriptions | The sentence under each record's second `---` | 9 |
| `Objective:` lines | In the steps of the main arc | 5 |
| `Win:` and `Lose:` | In the main arc | 2 |
| Reading names | The square brackets of each heading under Scans | 6 |
| Readings | Every line that starts with `%` | 9 |
| The landmark's name and description | Under Landmarks | 2 |
| Your word list | The `// ROLE` and `// SIGNAL` lines at the top. Change what each line says the word is worn by | 6 |

For example, the main arc of the example now reads:

```
### [The Keeper](salvage)
---
Arc
Scope: shared
Starts when: at once
Fails when: 10 minutes
Win: The keeper is home, and Lantern Nine will burn again.
Lose: The storm closed over the Deep with the keeper still out there.
---
A storm front is ten minutes out. One woman keeps Lantern Nine, and she is not answering. Find her and bring her in.
```

Look at what did not change: `(salvage)`, and every word in front of a colon.

Two things to keep true as you reword:

- An `Objective:` that names a distance must still agree with its `Done when:` line.
  `Objective: Close to within 500 of Lantern Nine` sits over `Done when: reach derelict 500`.
- If a sentence names the station or the ship, use the new name everywhere. Search the
  folder for the old one (`Ctrl+Shift+F`, Lecture 7) when you think you are done, with
  the **Match Case** button (`Aa`) on. In the example, a search for `DS 1` or for `Hulk`
  finds nothing in the whole folder at the end.

**In `story.mast`:** five places, all between quote marks, by the three rules of
Lecture 7.

| Line | What | The example |
|---|---|---|
| 25 | The map's name | `@map/amd_sample "The Quiet Lantern"` |
| 26 | The map's description. One quote mark, at the start | `" A dark beacon, a missing keeper, and a storm ten minutes out.` |
| 64 | The station's name, the first words in quotes | `"Marrow Station"` |
| 68 | The hulk's name, the first words in quotes | `"Lantern Nine"` |
| 113 | The tug's name, the first words in quotes | `"Tender Osprey"` |

On lines 64, 68 and 113 change the FIRST pair of quotes only. The second pair holds the
side and the roles. Leave it.

Save both files. Run lint:

```
sbs lint MyMission
```

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

## Step 3 - Two small files: the title and the ship

Two files in your mission folder that you have not opened before. Both are short lists of
settings: a name, a colon, a value.

**`description.yaml`** is what the server shows in its list of missions. Change two lines:

```
Visible Mission Name: The Quiet Lantern
```

```
Description: A dark beacon, a missing keeper, and a storm ten minutes out.
```

They are lines 11 and 14. Leave the name in front of the colon, the colon, and one space.

> **In these two values use letters, numbers, spaces, commas and full stops. No hyphen.
> No colon. No quote mark.**
>
> This matters more than any other rule on this page. The game reads this file for every
> mission, before it shows anything. A value with a bare hyphen in it, such as
> `Half-Light`, stops the game as it starts. Not your mission: the game, whichever
> mission was asked for, with no message and nothing in any log. And once you share the
> mission, it does the same to your friend's game. `sbs lint` reads this file and stops
> you: a hyphen or a second colon outside quote marks is an error named
> `description-stops-the-game`, with the line as it should be written. `sbs doctor` does
> not read it. So lint the mission after you change this file, every time.
>
> If your title must have a hyphen, put the whole value in double quotes:
> `Visible Mission Name: "Half-Light"`. That is what `sbs create` does by itself.

If the game ever stops the moment it starts, the day after you changed this file: this is
why. Take the hyphen out.

**`settings.yaml`** holds the name of the crew's own ship. Go to line 70:

```
    -   name: "Artemis"
```

Change the word between the quote marks, and nothing else on the line:

```
    -   name: "Kittiwake"
```

Do not touch the spaces at the start of the line. In this file they matter, as they do
in `story.mast`.

Lint does not read this file either. If you break it, your ship is called Artemis again
and nothing on a screen says why. The play in Step 6 is where you find out.

## Step 4 - If you want to rename a key (you do not have to)

You can skip this step. Your mission is yours without it.

If a key bothers you, it can be renamed. A key is written in several places, and all of
them have to change together. Every row below was tried on the finished example, linted,
and played without a screen.

**The safe way is one way: the editor's Replace All, across the whole folder.**

1. `Ctrl+Shift+H` opens Search with a Replace box under it.
2. Type the old word in the first box and the new word in the second.
3. Turn on the two small buttons in the first box: **Match Case** (`Aa`) and **Match
   Whole Word** (`ab` with a line under it).
4. Read the list of results before you do anything. Every line in it will change.
5. Click **Replace All**. Then `File`, `Save All`. Then run lint.

| Renamed this way, in both files | Result |
|---|---|
| The arc's key `salvage` | Works. Nine places change: the heading, four `Part of:` lines, three `Then:` lines, and the address on your card in `story.mast` |
| The role `derelict` | Works |
| The word `tug`: the step's key and the tug's role at once | Works |
| The role `lifeboat` (it is only in `mission.amd`) | Works |

**Renamed by hand, in some places and not others:**

| What was changed | What the game does | Lint says |
|---|---|---|
| The arc's key, in its heading only | The steps are cut off from the arc | Seven warnings: `dangling-reveal` and `dangling-parent`. Each one names the line |
| The arc's key everywhere in `mission.amd`, and not on the card in `story.mast` | No tug ever comes. Wait for the Tender never finishes, and the game cannot be won | **`clean`** |
| A step's key in its heading only | The step is never revealed | `dangling-reveal` |
| The key of the waiting step in its heading and in the `Then:` line that reveals it, and not on the card | No tug ever comes | **`clean`** |
| A role in `mission.amd` only, or in `story.mast` only | The first step never finishes | `role-nothing-wears` on each line that names it, and `unfired-signal` |
| A signal in one file only | The step that waits for it never finishes | `unfired-signal` |
| The key of a section: `## [Quests](story)` | No quests at all | `section-not-loaded` |

The two `clean` rows are the reason for the rule. The address in quotes on your card,
`"salvage/tug"`, is the one place lint cannot follow a key. Replace All across the folder
changes it with the rest. Your eye, working down one file, does not.

And one more row that lint misses, found while making the example:

| You wrote | What happens |
|---|---|
| A role that nothing wears, when the same word is in a ship's name. For example `Done when: reach lantern 500`, with a ship named "Lantern Nine" and no role `lantern` | Lint says `clean`. The step never finishes. With any other word (`reach beacon 500`) lint warns, as Lecture 7 showed |

So if you do rename a role to a word from your story, rename it with Replace All and
then check by eye that the ship's line in `story.mast` wears it.

**These are safe to change by themselves:**

| What | Result |
|---|---|
| The map's key on line 25: `@map/amd_sample` to `@map/quiet_lantern` | Works. `map=0` on the line that starts the game means "the first map", whatever its key |
| The key of the file's title on line 10: `(sample_mission)` | Works |
| The NAME of a section: `## [The Story](quests)` | Works. Only the key in round brackets is asked for |
| The role `tug` on the card's `npc_spawn` line alone | Works. Nothing in the mission looks for that role |

**Deleting the template's first arc.** If your story has no use for The Dark Beacon (it
was First Contact), delete its three records from `mission.amd`: the `###` heading and
the two `####` steps under it. Leave `story.mast` alone. Lint says `clean`, and the game
is won the same way with 500 credits. The two blocks in `story.mast` go on saying their
signals, and nothing is listening.

One warning about Replace All. It changes the word in your sentences too. In the
example, the word `find` is in `mission.amd` six times and only one of those is a key.
With both buttons on it is still found twice: the key, and a sentence. That is what step 4
of the list, read the results first, is for.

## Step 5 - Give the folder its name

Every student of this class has a folder called `MyMission`. If you send yours to a
friend who also took the class, it lands on top of theirs. So the folder gets your
mission's name before it leaves your computer.

1. Close VS Code. Close the game.
2. In File Explorer, open `data\missions`. Click `MyMission` once and press `F2`.
3. Type the new name and press Enter. Use letters and numbers only, with no spaces:
   `QuietLantern`.
4. In VS Code: `File`, `Open Folder...`, and choose the folder under its new name.

*[Not checked in a window: VS Code may show `AMD: trust this folder` in the Status Bar
again, as it did in Lecture 3, because for VS Code this is a new folder. Click it.]*

Nothing inside the seven files holds the folder's name. Measured: the same files under
three different names lint `clean` and run. What changes is what you type. From now on
every command names the new folder:

```
sbs lint QuietLantern
```

| You typed | What you get |
|---|---|
| The old name: `sbs lint MyMission` | `ERROR: not a folder: MyMission` |
| A name with a space, no quotes: `sbs lint Quiet Lantern` | `Error: Got unexpected extra argument (Lantern)` |
| A name with a space, in quotes: `sbs lint "Quiet Lantern"` | Works. So does every other command. No spaces is simply less to type |

## Step 6 - Check it

The whole checking routine of this class, in one place. Three checks, in this order.
Each one sees things the others cannot.

### Check 1 - Lint: is the writing right?

```
sbs lint QuietLantern
```

You are done with this check when it says `clean` and `0 error(s), 0 warning(s)`. Fix the
first finding first (Lecture 6).

### Check 2 - Doctor: is everything the mission needs on this computer?

```
sbs doctor QuietLantern
```

You read a doctor report in Lecture 2. With a folder's name after it, the report gets one
more block at the end, headed with that name:

```
QuietLantern
  ok  story.json  1 sbslib, 12 mastlib, 0 media
  ok  libraries   all declared libraries present
  ok  art         0 baked, 0 not yet drawn, 0 half-baked in mission art
```

Then the count. On a healthy computer its last words are `0 problems`:

```
20 checks: 15 ok, 5 optional absent, 0 problems
```

Your numbers may differ by one or two. `0 problems` is the part that matters. The rows
marked `--` are optional things you do not have, as in Lecture 2.

What doctor says for the states a finished mission can be in. Every row was tried:

| State | Doctor says |
|---|---|
| Healthy | The block above, and `0 problems` |
| The folder's name misspelled | `ERROR: not a folder: QuietLantren` and nothing else |
| A library the mission names is not on the computer | `!!  libraries   1 declared but not in __lib__:` and the file's name. Under it, the cure: `run: sbs fetch "QuietLantern" --update-libs` |
| The folder is not a mission: it holds another folder, or only some of the files | `--  story.json  not a mission folder`, and still `0 problems`. Read the row, not only the count |
| `story.json` damaged | `!!  story.json  will not parse` |

Doctor never reads your writing. A mission whose story is broken in every line still gets
`0 problems`. That is lint's job, which is why lint goes first.

### Check 3 - Play it: does the story happen?

Start the game with a Helm and a Science console, the way you did in Lecture 3:

```
sbs run server,helm,science -m QuietLantern map=0
```

Play it once to a win and tick this list as you go. The names are the example's. Use
yours.

1. The ship is yours: **Kittiwake**, not Artemis.
2. On Helm, open the Quest Log (the handheld icon at the top, then **Quests**). Two arcs:
   **The Dark Beacon** with Find the Lantern, and **The Keeper** with Come Alongside and
   First on Scene.
3. The station is **Marrow Station**. Out at 9000 is **Lantern Nine**.
4. Fly to Lantern Nine. Inside 500, Come Alongside and First on Scene show `Done`, and
   **Find the Skiff** is in the list. The Dark Beacon finishes by itself here too.
5. On Science, select Lantern Nine and read each tab. The readings are your sentences.
6. Fly to **The Keeper's Skiff**. Inside 500, Find the Skiff shows `Done`, and **Wait for
   the Tender** is in the list.
7. Twenty seconds later **Tender Osprey** is on the map, and **Bring Her Home** is in the
   list.
8. Fly home. Inside 1000 of Marrow Station the game ends with your `Win:` sentence.
9. Close the game. Open `mast.compile.log` and `mast.runtime.log` in the mission folder.
   Both are empty.

Then read every sentence on the screens once more as a reader, not as the writer. This is
the only check for a wrong word.

To read your `Lose:` sentence, start the game again and leave the ship where it is for ten
minutes.

To see the title and description from Step 3, start the game once with `-m QuietLantern
map=0` left off the line. The server then shows its list of missions.

### What each check sees

Every row was tried on the example.

| Mistake | Lint | Doctor | The play |
|---|---|---|---|
| A broken line in `mission.amd` or `story.mast` | Names the line | `0 problems` | Nothing runs, or a step never finishes |
| A key changed in `mission.amd` and not on the card | `clean` | `0 problems` | No tug. Item 7 fails |
| A library missing | An error under `== story.mast (compile) ==` that begins `Cannot load file __init__.mast from library` | `!!  libraries`, with the cure | Not tried in the game |
| A quote mark lost in `settings.yaml`, or a space lost from the start of its line | `clean` | `0 problems` | The ship is Artemis again. Item 1 fails. `mast.runtime.log` has one line that begins `ryaml refused` and names the line of the file, so item 9 fails too |
| A hyphen or a colon in `description.yaml`, outside quote marks | `[ERROR] line 11: `Visible Mission Name:` has a hyphen in a value that is not in quote marks. ...` `(description-stops-the-game)` | `0 problems` | A hyphen stops the game as it starts. See Step 3 |
| `description.yaml`, `settings.yaml` or `__lib__.json` missing from the folder | `clean` | `0 problems` | Not tried in the game |
| `script.py` missing from the folder | An error: `No module named 'script'` | `0 problems` | Not tried in the game |
| An old name left in a sentence | `clean` | `0 problems` | Only your eye, on the last read |

## Step 7 - Print it

Your mission is also a text. One command turns `mission.amd` into a page laid out for
paper:

```
sbs docs QuietLantern --title "The Quiet Lantern" --profile player --pdf
```

| Part | Meaning |
|---|---|
| `sbs docs QuietLantern` | Make a document from the mission in this folder |
| `--title "The Quiet Lantern"` | The title on the first page. Without it the title is the folder's name, `QuietLantern` |
| `--profile player` | Leave out the machinery. What is printed is names and sentences: no `Scope:`, no `Then:`, no keys |
| `--pdf` | Make a PDF file as well as a web page |

It answers in about two seconds:

```
--pdf: using --assets link (art referenced from __docs__); pass --assets none for a text-only PDF
prose         1 files -> ...\data\missions\QuietLantern\__docs__\The Quiet Lantern-prose.html
            pdf (chrome 154.0.8037.97) -> ...\data\missions\QuietLantern\__docs__\The Quiet Lantern-prose.pdf  (0.1 MB, no bookmarks (sbs deps install pypdf))
              the only engine available
```

(Where this page prints `...`, yours has the full path of your game's folder.)

Read it as three facts. The first line is a note, not a problem. Two files were made, and
each line that has `->` in it says where. And the words in brackets on the PDF's line say
which browser made the PDF: `chrome` or `edge` and a version number. No window opens.
`no bookmarks` and `the only engine available` are notes too.

Both files are in a new folder inside your mission, called `__docs__`. Open it in File
Explorer and double-click the PDF.

What is in it, for this mission: a contents list, then every arc and step with its
description, every reading, and the landmark. Three pages.

**Who gets which document.**

| Reader | Command | Why |
|---|---|---|
| A friend who will READ your story: another writer, an editor | The command above | Names and sentences only |
| A friend who will PLAY it | No document. Send the mission (Step 8) | The document prints every hidden step and every reading, in order. It is the whole plot |
| You, checking your chain | `sbs docs QuietLantern --lens bible` | See below |

The second command makes `QuietLantern-bible.html`. It lays the main arc out as numbered
beats, one step in each. Under each step are two lines: `reached from`, and `leads to`.
Read down the beats. Each step from the second on should be reached from the one before
it, and the last should lead nowhere. A step in the wrong beat, or one with no `reached
from`, is a `Then:` line pointing at the wrong place.

The bible is written for the person who built the mission, and it uses its own words for
your fields. Read them like this:

| It prints | You typed |
|---|---|
| `GOAL` | `Done when:` |
| `PARENT` | `Part of:` |
| `THEN`, `SCOPE`, `REQUIRED` | The same words |

Four things to know before you rely on a printed copy. All four were measured.

- **Your `Win:` and `Lose:` sentences are not in any document.** The bible prints `WIN
  False` and `LOSE False` where they should be. Your sentences are fine and the game uses
  them. The printing is wrong. Check those two by playing.
- The `player` document leaves out `Objective:` and `Reward:` lines as well. Leave
  `--profile player` off and they are printed, along with a `When` line for each step.
- A PDF needs Chrome or Edge on the computer. Every Windows computer has Edge. If
  neither is found the answer is `ERROR: no PDF engine found - need a Chromium browser or
  the weasyprint CLI`, and the web page is still made.
- This mission has no faces in it. When you add people in Class 2: on a computer set up
  the way this class set up yours, a person's face is printed as an empty box with the
  words `a face` in it. `sbs doctor` says so in advance, in its row
  `--  faces       cosmos_dev is not installed`.

## Step 8 - Share it

A mission is a folder. To give it to someone, you send the folder, and they put it where
yours is. There is no upload and no account.

### Your side: clean it, zip it

Close the game and VS Code. Open your mission folder in File Explorer.

**1. Take your PDF out.** Move it from `__docs__` to your Documents folder.

**2. Delete what is not the mission.** Any of these that are there:

| Delete | What it is | Why it should not travel |
|---|---|---|
| `__docs__` (a folder) | Your printed documents | The whole plot, in order |
| `__pycache__` (a folder) | A scratch folder that lint and the game make | Made again when needed |
| `mast.compile.log`, `mast.runtime.log` | The two logs | Made again by every run |
| `debug.log` | A long log from the rehearsal run, `sbs debug` | It holds the full path of your game's folder, with your Windows user name in it. It may be in `data\missions` instead. That copy is not in your zip |

Every one of them comes back by itself when it is needed. Run lint and `__pycache__` is
there again (measured).

**3. Count what is left.** Seven files, and nothing else:

```
__lib__.json
description.yaml
mission.amd
script.py
settings.yaml
story.json
story.mast
```

Send all seven. You wrote two of them and changed two more, and the mission does not run
without the others.

**4. Zip the folder.** Go up to `data\missions`. Right-click the `QuietLantern` folder
itself, not the files inside it. On Windows 11 choose **Compress to**, then **ZIP File**.
On Windows 10 choose **Send to**, then **Compressed (zipped) folder**. You get
`QuietLantern.zip` beside the folder. It is tiny: the example's is 7 KB.

*[The two menus were not checked in a window.]*

**5. Send `QuietLantern.zip`**, by email or any way you send a file. Send this note with
it.

### The note for your friend

```
This is a mission for Artemis Cosmos. To play it:

1. Open File Explorer and go to the game's folder, then data, then missions.
2. Put the QuietLantern folder from the zip file in there. Check it: when you open
   data\missions\QuietLantern you must see story.mast at once, not another folder.
3. Click in the address bar of that missions window, type cmd and press Enter.
4. Type each of these lines and press Enter after each:

   sbs version
   sbs update
   sbs fetch "QuietLantern" --update-libs
   sbs run server,helm,science -m QuietLantern map=0

If sbs version says 0.12 or a later number, you can skip sbs update.
```

Change `QuietLantern` to your folder's name in four places.

### Their side: what happens

This was done from start to finish on a second, clean copy of the game: the zip file
unpacked into `data\missions`, then the commands.

The third command fetches the libraries your mission names: fifteen files, two printed
lines for each. On a fast connection it took eight seconds. Its last line is:

```
Libraries are up to date. QuietLantern itself was not changed.
```

After it, on that copy, `sbs lint QuietLantern` said `clean`, `sbs doctor QuietLantern`
said `0 problems`, and the mission started and ran with both logs empty.

Your friend needs that third command even if they play the game every week. A mission
runs on the libraries on the computer it is played on, and theirs may be months older
than yours.

### What goes wrong on their side

Every row was tried on the second copy.

| What happened | What they see | The cure |
|---|---|---|
| The zip was unpacked with **Extract All**, which makes a folder inside a folder: `data\missions\QuietLantern\QuietLantern` | `sbs fetch` says `ERROR: no mission here to read the list of libraries from:` and `(a mission folder holds a file called story.json)` | Move the inner folder up into `data\missions`, and delete the empty outer one |
| The same, and they run lint | `== QuietLantern\mission.amd ==`, then `clean`. Lint is wrong to sound pleased. The folder name in front of `mission.amd` is the sign | The same |
| The same, and they run doctor | `--  story.json  not a mission folder`, and `0 problems` | The same |
| Their tool is the old one that came with the game | `Error: No such option '--update-libs'.` | `sbs update`, then the line again |
| They gave the folder another name | Everything works, under that name. They type their name for it in the last two lines | None needed |
| You sent only `mission.amd` and `story.mast` | `sbs fetch` gives the `no mission here` error | Send all seven files |
| The game stops the moment it starts, for every mission | Nothing. No message | A hyphen in your `description.yaml`. They delete the `QuietLantern` folder to get their game back. You fix Step 3 and send it again |

### If you use GitHub

If you already keep your writing on GitHub, there is a second way. Put the seven files at
the top of a repository named for the mission, on a branch called `main`. Your friend
then types `sbs fetch QuietLantern -u yourname` and answers `y` to one question. That
fetches the mission and its libraries together. This page did not try it, and nothing in
this class needs it. The zip file is the way that was measured.

## If something goes wrong

| What you see | Likely cause |
|---|---|
| `ERROR: not a folder: MyMission` | You renamed the folder in Step 5. Use the new name |
| `Error: Got unexpected extra argument` | The folder's name has a space in it. Put the name in quotes, or rename the folder |
| Lint is `clean`, the tug never comes, and the game cannot be won | A key was renamed in `mission.amd` and not on the card. Line 111 of `story.mast` must hold the step's address exactly as `Then: reveal` has it |
| Lint is `clean` and the first step never finishes | A role in a `reach` line that nothing wears. See the row about a ship's name in Step 4 |
| `role-nothing-wears`, or `dangling-reveal`, after a rename | The key was changed in some places only. Undo, and use Replace All |
| The ship is still called Artemis | `settings.yaml` was not saved, or line 70 lost a quote mark or a space. `mast.runtime.log` says which line |
| The game stops as it starts, with no message | A hyphen in `description.yaml`. Step 3 |
| The server's list still says The Cold Hulk | `description.yaml` was not saved |
| An old name on a screen | A sentence you missed. Search the folder for the old name |
| `ERROR: no PDF engine found` | Neither Chrome nor Edge was found. The web page was still made: open it and print it from the browser |
| The printed title is `QuietLantern`, one word | `--title "..."` was left off the command |
| The bible says `WIN False` | Nothing you did. See Step 7 |
| `ERROR: could not load sbs_utils to render` | `sbs docs` was pointed at a folder that is not a mission. Check the name, and that the folder holds `story.json` |
| `!!  libraries` in the doctor report | Type the line doctor prints under it |
| Your friend's `sbs fetch` says `no mission here` | A folder inside a folder, or files missing. See Step 8 |

## The capstone rubric

"Done" means every line here is ticked. Each one is something you can check yourself.

**It is yours**

- [ ] The paper plan from Step 1 has every row filled in.
- [ ] A folder search with **Match Case** on, for each old name in turn (`Cold Hulk`,
      `Salvage`, `DS 1`, `Hulk`, `Lifeboat`, `Tug`, `Artemis`, `Sample`), finds nothing.
      The keys `salvage`, `lifeboat` and `tug` are in small letters, so they are not
      found, and they stay.
- [ ] `description.yaml` has your title and your one line, with no hyphen and no colon in
      either.
- [ ] The folder has your mission's name, with no spaces.
- [ ] The word list at the top of `mission.amd` is true: each line names the thing that
      wears the role today.

**It is checked**

- [ ] `sbs lint` on your folder answers `clean`, with `0 error(s), 0 warning(s)`.
- [ ] `sbs doctor` on your folder ends in `0 problems`, and its last block has three `ok`
      rows.
- [ ] You played it to a win, and all nine items of the list in Step 6 were true.
- [ ] You let the clock run out once and read your `Lose:` sentence.
- [ ] After the play, both logs are empty.

**It is printed**

- [ ] `__docs__` holds a PDF with your title on its first page.
- [ ] You read the bible's beats, and each step is reached from the one before it.

**It is shared**

- [ ] The folder holds exactly seven files before you zip it.
- [ ] The zip file opens to ONE folder, and the seven files are inside that.
- [ ] Another person, or you on a second computer, put it in `data\missions`, typed the
      four lines of the note, and reached the first step.

## Exercise

Three, in order of nerve.

1. **Hand it over for real.** Send the zip and the note to one person. Do not help them.
   Write down every place they got stuck. Each one is a line your note needs.
2. **Send the document to a reader.** Send the PDF to someone who will never play. Ask
   them one question: at which step did you stop caring? Rewrite that step's description.
3. **Rename one key the safe way.** Pick the key that fits your story least. Rename it
   with Replace All as Step 4 describes. Lint, then play to a win. Then send the mission
   again.

## Checkpoint

You are done with Class 1 when the rubric is ticked to the last line. The short form:

- `sbs lint` is `clean` and `sbs doctor` says `0 problems`, for a folder with your
  mission's name.
- The game, played to a win, shows your names and your sentences from the first screen to
  the last, and both logs are empty afterwards.
- A PDF of your story exists.
- The mission started on a computer that is not yours.

## Next

Class 2 puts people in your story: sides, a cast with faces, conversations, and a boss
with a voice. It starts from the mission you just shipped.

## Further reading

- "Printing a mission: `sbs docs`" in the library documentation: the four kinds of
  document, and the options this page did not use.
- "The `sbs` CLI" in the library documentation, the parts on `sbs doctor` and
  `sbs fetch`.
- The tool's own README, the part called "Recipes".
