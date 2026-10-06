# Class 1, Lecture 3 - Your editor and your first run

## What you will have at the end

A mission of your own, open in an editor, and played once.

- VS Code is on your computer, with the Artemis AMD add-on in it.
- A folder named `MyMission` is in `data\missions`. One command made it.
- That folder is open in VS Code, and `mission.amd` shows in color.
- You have started the game on your mission and flown the ship from Helm.

*[Screenshot to add: VS Code with the `MyMission` folder open and `mission.amd` in front,
and beside it the Helm window of the game.]*

You write no story today. The mission you make is a small finished sample: a station, a
drifting hulk, and one quest in two steps. From Lecture 5 on you change it into your own.

## The video

*[Link to add when recorded.]*

## Before you start

- A computer with Windows 10 or Windows 11, and Artemis Cosmos 1.4.0 from Steam or
  itch.io.
- The internet, for the whole lecture. Four things are downloaded.
- A command prompt open in `data\missions` (Lecture 2).
- File name extensions shown in File Explorer (Lecture 2, Step 3).
- `sbs version` prints `0.12` or a later number (Lecture 2, Step 6).

Words for this lecture:

| Word | Meaning |
|---|---|
| Editor | A program for writing plain text files. It is to a mission what a word processor is to a letter |
| VS Code | The editor this course uses. Its full name is Visual Studio Code. It is free |
| Add-on | An extra part you put into VS Code. VS Code calls it an "extension". That is not the extension on the end of a file's name |
| Template | A small ready-made mission that a new mission is copied from |
| Library | A file of program parts that missions share. Libraries live in `__lib__`. You never open one |
| Server | The copy of the game that runs the mission. There is one |
| Console | A copy of the game that shows one station of the bridge: Helm, Science, and so on |

On this page the game's folder is written `C:\Cosmos`, as in Lecture 2. Your own path
is longer. Read your own.

## Step 1 - Get VS Code

1. In your web browser, go to `https://code.visualstudio.com/`.
2. Click the download button for Windows. A file whose name starts with
   `VSCodeUserSetup` arrives in your Downloads folder.
3. Double-click that file. Accept the agreement and click **Next** until you reach the
   page named **Select Additional Tasks**. It has five boxes:

| Box | What to do |
|---|---|
| Create a desktop icon | Your choice |
| Add "Open with Code" action to Windows Explorer file context menu | Tick it |
| Add "Open with Code" action to Windows Explorer directory context menu | Tick it. It lets you right-click a folder and open it in VS Code |
| Register Code as an editor for supported file types | Leave it as it is |
| Add to PATH (requires shell restart) | Leave it ticked |

4. Click **Next**, then **Install**, then **Finish**. VS Code opens.

This installer puts VS Code in your own Windows account. It does not ask for an
administrator's password.

The VS Code window has four parts. You will hear their names for the rest of the course.

| Part | Where | What it is for |
|---|---|---|
| Activity Bar | The narrow strip of icons down the left edge | Chooses what the panel beside it shows |
| Side Bar | The panel beside the Activity Bar | The list of your files, a search box, or the list of add-ons |
| Editor | The large area | Your files, one tab for each |
| Status Bar | The strip along the bottom | Small facts about the open file |

## Step 2 - Add the Artemis AMD add-on

The add-on is one file. You download it, then hand it to VS Code.

1. In your web browser, go to:

```
https://github.com/artemis-sbs/sbs_cli/releases/tag/amd-vscode-v0.9.4
```

2. Under the word **Assets**, click `amd-language-0.9.4.vsix`. It goes to your Downloads
   folder. If your browser says the file is not commonly downloaded, choose to keep it.
3. In VS Code, click the Extensions icon in the Activity Bar. It is the one made of four
   squares. Or press `Ctrl+Shift+X`.
4. At the top of the Side Bar, click the three dots. Choose **Install from VSIX...**
5. Go to your Downloads folder, click `amd-language-0.9.4.vsix`, and click **Install**.
6. If VS Code asks `Do you trust the publisher "artemis-sbs"?`, click **Trust Publisher &
   Install**.

The add-on is now in the list, under **Installed**, as **Artemis AMD**.

Two things to know:

- **Do not look for it with the search box.** The add-on is not in the public list that
  the search box reads. A search for "Artemis" offers other add-ons that have nothing to
  do with this game. Install none of them.
- **A newer one may be out.** Go to `https://github.com/artemis-sbs/sbs_cli/releases`
  and look for the highest entry whose title starts `Artemis AMD (VS Code)`. The entry
  at the very top of that page may be the `sbs` tool. That is not the add-on.

## Step 3 - Make your mission

Go to the command prompt. Read the prompt line. It ends `\data\missions>`.

First ask what you can start from:

```
sbs templates
```

The top of the answer:

```
Default release line: v1.4.0  (installed in __lib__)

v1.4.0  <- default
  minimal        Minimal mission
                 One @map and a line of narration. The smallest thing that runs.
  sandbox        Sandbox mission
                 Two sides, a station in an asteroid field, player ships and raider waves.
  addon          Mastlib addon
                 A shareable addon plus a harness map to run it. Uses provides/requires.
  amd            AMD driven mission
                 Quests and science scans authored as data in a .amd fact sheet.
  ou             Open Universe mission
                 Built on the OpenUniverse engine: a whole universe authored in one .amd.
```

Five templates. This class uses `amd`. Class 5 uses `ou`. Below this block the answer
lists older versions, which have fewer templates. Leave them.

Now make the mission. Type this as one line:

```
sbs create MyMission -t amd --title "The Cold Hulk"
```

| Part | Meaning |
|---|---|
| `create` | The command: make a new mission |
| `MyMission` | The name of the new folder. No spaces |
| `-t amd` | Which template to copy |
| `--title "The Cold Hulk"` | The mission's name in the game's list of missions. Put your own title between the quote marks |

Three rules for the title: no more than 40 characters, no colon, and no quote marks
inside it.

It prints:

```
Release line: v1.4.0  (installed in __lib__)
Fetching mast_starter (v1.4.0) from https://github.com/artemis-sbs/mast_starter/archive/refs/heads/v1.4.0.zip
Command ran successfully.

Created MyMission from 'amd' (7 files)

  artemis-sbs.sbs_utils.v1.4.0.sbslib
  + 12 mastlib dependencies

Fetch these dependencies now? [Y/n]:
```

It has stopped to ask a question. Press Enter. That means yes.

If a library your mission asks for is not on your computer yet, it prints one long line
starting `Fetching` for each. The libraries came with the game, so most likely it prints
none. It ends:

```
MyMission is ready.
  14 of its 14 libraries were already here and were kept as they are.
  sbs fetch "MyMission" --update-libs   # get today's build of each (do this once)
  sbs debug MyMission          # run it in the browser
  sbs lint MyMission           # check its AMD
```

The first of the three commands it names is the next step.

Later lectures call your folder `MyMission`. Keep that name and those pages will match
your screen.

## Step 4 - Bring the libraries up to date

The libraries are mended and published again from time to time. `sbs create` kept the
ones that came with the game as they are. Get today's build of each, once:

```
sbs fetch "MyMission" --update-libs
```

| Part | Meaning |
|---|---|
| `fetch` | The command: download |
| `"MyMission"` | Your mission's folder. The tool reads the list of libraries your mission asks for |
| `--update-libs` | The libraries only. Nothing in your folder is touched |

It prints one long `Fetching` line for each library, fifteen in all, and ends:

```
Libraries are up to date. MyMission itself was not changed.
```

It took seven seconds when this page was written. One of the fifteen is the game's
shared art, and it is the slow one.

**Never leave `--update-libs` off.** Without it, `sbs fetch` does a different job: it downloads
a published mission and puts it in place of the folder with that name.

## Step 5 - Open your mission in VS Code

You open the mission's FOLDER, not one file in it.

1. In VS Code, open the **File** menu and choose **Open Folder...**
2. Go to `data\missions`. Click `MyMission` once. Click **Select Folder**.

VS Code now decides whether it trusts the folder. Until it does, your add-on only colors
the file: its checking, the outline and its other tools wait. The add-on says so itself,
with `AMD: trust this folder` near the right end of the Status Bar. What else you see
depends on your copy of VS Code:

| What you see | What to do |
|---|---|
| A box that asks `Do you trust the authors of the files in this folder?` | Click **Yes, I trust the authors**. You are the author |
| No box. A band along the top that says `Restricted Mode is intended for safe code browsing. Trust this folder to enable all features.` | Click **Manage** on that band, then the **Trust** button |
| Neither | Look at the left end of the Status Bar. If it says `Restricted Mode`, click those words, then **Trust** |

You do this once for each mission folder.

The **Trust** button is on a page named **Workspace Trust**. After you click it the page
says `You trust this folder`, the band at the top goes away, and so do the words
`Restricted Mode`. Close that page with the **X** at its top right corner.

If a panel named **Chat** fills the right side of the window, close it the same way, with
the **X** at its own top right corner. This class does not use it, and your file gets the
room.

The Side Bar now lists your mission's files. At the top of the list is the folder's name,
in capitals: `MYMISSION`. There are seven files:

| File | What it is | Will you change it? |
|---|---|---|
| `mission.amd` | Your fact sheet: the quests and what Science reads | Yes. Most of your writing goes here, from Lecture 5 |
| `story.mast` | The story file. It puts the station and the hulk in space | A few lines, from cards, in Lectures 7 and 11 |
| `description.yaml` | The title you gave, for the game's list of missions | Not in this class |
| `settings.yaml` | Settings, such as how many player ships | No |
| `story.json` | The list of libraries the mission asks for | No |
| `script.py` | Starts the mission inside the game | No |
| `__lib__.json` | The version of the libraries | No |

More files will appear here by themselves. Leave them where they are.

| Name | When it appears | What it is |
|---|---|---|
| `mast.compile.log` and `mast.runtime.log` | The first time the mission runs | Notes the game writes while it runs. Empty means it noticed nothing wrong. Lecture 6 reads them |
| `__pycache__` | The first time you run `sbs lint` | The tool's own scratch folder |

Now click `mission.amd` in the list. It opens in the Editor. Three things tell you the
add-on is working:

1. **Color.** The lines that start with `#` are a different color from the sentences.
2. **The word `AMD`** near the right end of the Status Bar. Without the add-on it says
   `Plain Text`.
3. **The outline.** At the bottom of the file list is a heading named **Outline**. Click
   it. It shows the eight headings of the file, one inside another:

```
Sample Mission
  Quests
    First Contact
      Find the Derelict
      Study the Derelict
  Scans
    Derelict Hull
    Derelict Materials
```

Now see the add-on catch a mistake.

4. Go to line 47. The line numbers are down the left edge of the Editor. The line is:

```
### [Derelict Hull](derelict_scan)
```

5. Delete the last part, `(derelict_scan)`, so that the line ends at `]`.
6. A red wavy line appears under that line. Open the **View** menu and choose
   **Problems**. The panel that opens has one line, an error on line 47. It begins:

```
there is no `(key)` after the `[Name]`
```

7. Press `Ctrl+Z`. The part you deleted comes back and the wavy line goes.

The add-on checks the file as you type. It needs no command and no save. Lecture 6
teaches you to read what it says.

Two habits for the editor:

| Habit | Why |
|---|---|
| `Ctrl+S` saves the file | VS Code does not save by itself. A round dot on a file's tab means it has changes that are not saved. The game and `sbs lint` read the saved file, not your screen |
| `Ctrl+Z` takes back the last thing you did | Press it again to go back further |

If the tab of `mission.amd` shows a dot now, press `Ctrl+S`.

## Step 6 - Check it

One command reads your whole mission and says what looks wrong. Lecture 6 is all about
it. Today, look for one word. In the command prompt:

```
sbs lint MyMission
```

```
== mission.amd ==
  clean

1 amd + 1 mast file(s): 0 error(s), 0 warning(s)
```

The word is `clean`. You have not changed anything, so there is nothing to find.

## Step 7 - Play it, in the game

A `run` command starts several copies of the game at once: one server and the consoles
you name. First ask what it would start, and start nothing. Add `--dry-run`:

```
sbs run server,helm,science -m MyMission map=0 --dry-run
```

```
  server         C:\Cosmos\Artemis3-x64-release.exe autostartserver defaultmission=MyMission map=0
  helm           C:\Cosmos\Artemis3-x64-release.exe autostartclient clientautoconnectip=127.0.0.1 map=0
  science        C:\Cosmos\Artemis3-x64-release.exe autostartclient clientautoconnectip=127.0.0.1 map=0
```

One line for each window it would open. Read the first word of each line, and
`defaultmission=MyMission` on the server's line.

| Part of the command | Meaning |
|---|---|
| `run` | The command: start the game |
| `server,helm,science` | The windows you want: the server, and two consoles. Commas between them and NO spaces |
| `-m MyMission` | Which mission: your folder's name. Leave this off and you get the game's own mission |
| `map=0` | Start the mission's first map without being asked. No hyphens and no spaces |
| `--dry-run` | Show the lines and start nothing |

Now press the up arrow, rub out `--dry-run`, and press Enter:

```
sbs run server,helm,science -m MyMission map=0
```

Three game windows open, one after another, a couple of seconds apart. The tool writes
each window's job on its title bar: `server`, `helm`, `science`. When the third is up,
the command prompt is ready for you again. The game does not need it.

In the game:

1. Go to the `helm` window. Your ship is the Artemis. She starts about 3500 from the
   station, DS 1.
2. Find the **Unknown Hulk** on Helm's map. It is 9000 from the station.
3. Fly to it. This is the sample quest: when you come within 2000 of the hulk, its first
   step, **Find the Derelict**, is done.
4. Look at the `science` window. The hulk is in its list.

You will open the quest list in Lecture 4, and take it apart in Lecture 5.

When you have looked around, close all three windows with the X in each one's corner.
Close every game window before you start the game again.

## Step 8 - The rehearsal: your mission in a web browser

There is a second way to run a mission. It needs no game windows. The tool plays the
mission itself and shows it as a page in your web browser. Use it for a quick look. Use
the game when a lecture says "play it".

```
sbs debug MyMission --map 0
```

It prints about twenty lines. Twelve of them start `[runner] mastlib:`, one for each
library. Among the rest:

```
[runner] story: C:\Cosmos\data\missions\MyMission\story.mast
[runner] running at 60 Hz  (MAST 5 Hz, physics 30 Hz background thread)
EXTRA_SHIP_DATA is off, so no mod ship data is being loaded - hulls a mod adds will not exist, and a picker or race list filtered to them will come up empty. Set EXTRA_SHIP_DATA: true to enable it.
no @media/skybox labels are loaded at all - nothing will be set. Is the add-on that declares them in story.json, or excluded by a profile?
[runner] auto-starting map: amd_sample
```

Then it stops printing, and the prompt line does not come back. That is right. The
mission is running.

Three of its lines read like faults. None of them is one.

| Line starts | What it means for you |
|---|---|
| `EXTRA_SHIP_DATA is off` | The mission uses the game's own ships and no others. Yours does |
| `no @media/skybox labels are loaded` | The sample mission does not choose a picture for the sky |
| `Elapsed time:` | How long the first moment of the mission took. A note for programmers |

One line names the page: it starts `[runner] GUI server started` and ends
`open http://localhost:8765/`.

1. The page is served by your own computer, to your own computer only.
2. In your web browser, go to:

```
http://localhost:8765/
```

3. The page's tab is named `SBS Remote GUI`. It is the tool's drawing of a console.
4. To stop: click the command prompt window and press `Ctrl+C`. It prints
   `[runner] stopped`. If it then asks `Terminate batch job (Y/N)?`, type `Y` and press
   Enter. The prompt line is back.

The rehearsal is a stand-in for the game, not the game:

| | The game (`sbs run`) | The rehearsal (`sbs debug`) |
|---|---|---|
| What you look at | The game's own windows | A page in your browser |
| The command prompt while it runs | Free | Busy until you press `Ctrl+C` |
| Sensors | Scan what is in range by themselves | Scan nothing by themselves, so a quest step that waits for a scan does not finish |
| What it is good for | Every "Play it" step in this course | A quick look, and the two log files |

`sbs debug` also leaves a file named `debug.log` in `data\missions`. Leave it.

## Step 9 - Check it: what the tools say when you slip

Every row was typed on a copy of the game. The middle column is what came back. Two kinds
of row were typed with one more word on the end: the `sbs run` rows with `--dry-run`, so
that nothing was started, and the `sbs debug` rows with `--no-gui`, which runs the
mission without the page.

**Making the mission:**

| What you typed | What the window says | What it means |
|---|---|---|
| `sbs create` | `Error: Missing argument 'NAME'.` | The folder's name goes after `create` |
| `sbs create My Mission -t amd` | `Error: Got unexpected extra argument (Mission)` | A space ends a word. Use a name with no spaces |
| `sbs create Second -t amdd` | `Error: no template 'amdd'. Available: minimal, sandbox, addon, amd, ou` | The template's name is misspelled |
| `sbs create Ninth -t AMD` | It works. Capitals do not matter in a template's name | Nothing to mend |
| `sbs create MyMission -t amd`, a second time | `Error: C:\Cosmos\data\missions\MyMission already exists and is not empty - pick another name, or move it aside` | The tool never writes over a mission. Good. `mymission` gets the same answer: capitals do not make a new name |
| The same, with the internet off | `Error: could not reach github.com/artemis-sbs/mast_starter - check the network, or pass -b` | The template is downloaded each time. No folder is made |
| `--title "Salvage: Run"` | `Error: --title rejected: a ':' makes YAML read it as a mapping` | No colon in a title |
| A title of 47 characters | `Error: --title rejected: it is 47 characters; the mission list truncates long names` | 40 at most |
| `-title "Nine"` (one hyphen) | `Error: Got unexpected extra argument (Nine)` | `--title` has two hyphens |
| `sbs creat MyMission` | `Error: No such command 'creat'. Did you mean 'create'?` | A slip in the second word |
| `sbs create Seventh -t amd`, with the prompt inside a mission's folder | `'sbs' is not recognized as an internal or external command,` | The wrong folder. Read the prompt line (Lecture 2) |
| `n` at the question | ``Skipped. Type `sbs fetch "MyMission" --update-libs` when you are ready.`` | The folder is made and no library is fetched. Step 4 fetches them |
| `sbs create Second`, with no `-t` | A numbered list of the five templates, then `Template [1]:` | Type `4` and press Enter |

**The libraries:**

| What you typed | What the window says | What it means |
|---|---|---|
| `sbs fetch "MyMision" --update-libs` | `ERROR: no mission here to read the list of libraries from: C:\Cosmos\data\missions\MyMision` | The folder's name is misspelled |
| `sbs fetch MyMission --update-libs` (no quote marks) | The same as with them | The quote marks matter only for a name with a space in it |
| `sbs fetch "MyMission" --update-libs`, with the internet off | About a minute of lines that start `Command failed` and `ERROR: Fetching`, then a list under `ERROR: these dependencies could not be fetched:` and `The mission(s) will NOT run without them.` | Nothing was changed. The libraries you had are still there, and the mission runs as it did before. Mend the connection and type it again |

**Starting the game** (each with `--dry-run`):

| What you typed | What the window says | What it means |
|---|---|---|
| `sbs run server,helm -m MyMision map=0` | `note: mission folder 'MyMision' not found in C:\Cosmos\data\missions - the server will not find it either` | The folder's name is misspelled. Without `--dry-run` the windows open all the same |
| `sbs run helm -m MyMission map=0` | `note: no 'Server' in the list, so nothing is serving on 127.0.0.1 - add Server, pass --ip, or use --no-auto` | A console and no server. Put `server,` in front |
| `sbs run server,helm -m MyMission --map 0` | `Error: No such option '--map'. Did you mean '--ip'?` | For `run` it is `map=0`. The form `--map 0` belongs to `debug` |

**Starting the rehearsal:**

| What you typed | What the window says | What it means |
|---|---|---|
| `sbs debug MyMision --map 0` | `Error: not a folder: MyMision`, then `Check the spelling, and that the prompt is in data\missions (type `dir` to see the mission folders).` | The folder's name is misspelled, or the prompt is in another folder |
| `sbs debug --map 0`, with no folder name | `Error: not a mission: . has no story.mast. Name the mission's own folder, for example:  sbs debug MyMission` | Put your folder's name after `debug` |
| `sbs debug MyMission map=0` | `Error: Got unexpected extra argument (map=0)` | For `debug` it is `--map 0` |

**What nothing warns you about:**

| What you did | What happens | What tells you |
|---|---|---|
| `sbs run MyMission` | The name is taken for a console. One window opens, as a console of that name, with no server and no mission | Only the `note: no 'Server' in the list` line. The window opens all the same |
| `sbs run -m MyMission`, with no list of windows | Six windows: the server and five consoles | Nothing. Close them |
| `sbs run` with nothing after it | The same six windows, on the game's own mission | Nothing |
| A space after a comma: `sbs run server, helm -m MyMission map=0` | Two windows. The second has no console name | Nothing. With `--dry-run` its line starts with a blank |
| A console's name misspelled: `server,hlem` | A window is started for a console named `hlem` | Nothing |
| `sbs create` with no `--title` | The mission is named `AMD Sample` in the game's list, like everybody else's | Nothing. Open `description.yaml` and change the words after `Visible Mission Name:` |
| A folder name with a space, in quote marks: `sbs create "My Mission" -t amd` | It works. Every command after it needs the quote marks: `sbs lint My Mission` answers `Error: Got unexpected extra argument (Mission)` | Nothing, until then |
| The folder is not trusted in VS Code | `mission.amd` has its colors, but no wavy lines and no outline | `Restricted Mode` at the left of the Status Bar and `AMD: trust this folder` at the right. Click either |

## If something goes wrong

| What you see | Likely cause, and what to do |
|---|---|
| `sbs version` answers a number lower than `0.12`, or `sbs create` does not end `MyMission is ready.`, or `sbs lint` says `ERROR: could not load sbs_utils to lint`, or a block that starts `Traceback` ends in `ImportError` | Your tool or your libraries are older than this page. Type `sbs update`, then `sbs fetch "MyMission" --update-libs` |
| It all worked last week and now gives the row above | The store put its own files back. Steam does this when you ask it to check the game's files (**Properties**, **Installed Files**, **Verify integrity of game files**), and a game update can do it too. The tool and the missions that came with the game go back to what the game shipped with. `MyMission` is not one of the game's files and is left alone. Type the two commands of the row above. (Read, not tried) |
| A line that starts `not checked:` under `clean` | One library is missing. Step 4 |
| `ERROR: not a folder: MyMision` | The folder's name is misspelled, or the prompt is not in `data\missions` |
| `ERROR: which mission? Put its folder name after the command:` | You typed `sbs lint` with nothing after it |
| `mission.amd` has no color in VS Code, and the Status Bar says `Plain Text` | The add-on is not installed (Step 2), or it is older than 0.9.4 and the folder is not trusted (look for `Restricted Mode` in the Status Bar, and do the table in Step 5). Or the file is misnamed (see the next row) |
| The file list shows `mission.amd.txt` | The file was saved from another program with `.txt` on the end. Right-click it in the file list, choose **Rename...**, and take the `.txt` off. `sbs lint` says so too: "There is a `mission.amd.txt` in the folder: the name has to END in `.amd`" |
| Color, and no wavy line when you break line 47 | The add-on's checker did not start. Do Step 4, then close VS Code and open it again. If that does not mend it, open the **View** menu, choose **Output**, and pick **Artemis AMD** in the list at the right of that panel |
| A box: `Artemis AMD: could not start the language server. Set "amd.cosmosPath" to your Cosmos install folder.` | Most often the same cause as the row above. Do Step 4 before you change any setting |
| The file list shows many folders, and the name at its top is `MISSIONS` | You opened `data\missions`, not your mission. **File**, **Open Folder...**, and choose `MyMission` |
| The Side Bar says `You have not yet opened a folder.` and offers an **Open Folder** button | You opened one file, not the folder. Click that button and choose `MyMission` |
| The game windows open on the game's own mission | `-m MyMission` is missing from the `run` line |
| The game windows open and your mission does not start by itself | `map=0` is missing from the `run` line, or the folder's name after `-m` is misspelled. Close the windows, add `--dry-run`, and read the server's line |
| A game window comes up as the wrong console | Close all the game windows and run the line again with `--settle 4` on the end. It leaves more time between windows |
| The browser says it cannot reach `localhost:8765` | The rehearsal is not running. Look at the command prompt: if the prompt line is back, start it again |
| You closed the command prompt while the rehearsal was running | The rehearsal runs inside that window, so it stops with it. Open a new prompt (Lecture 2, Step 4) *[Not checked: see the script.]* |
| You closed the command prompt while the game was running | The game windows do not need the prompt and should stay. Close them with their own X *[Not checked: see the script.]* |

## Exercise

Do it without the page, then check yourself against it.

1. Make a second mission, named `Practice`, from the `amd` template, with a title of your
   own.
2. Open the `Practice` folder in VS Code and trust it. Find your title in
   `description.yaml`.
3. Open its `mission.amd`. Break line 47 the way Step 5 does, read the error, and take
   the change back.
4. Type the `run` line for `Practice` with a server and one console, Helm, and with
   `--dry-run`. Read the two lines. Then run it without `--dry-run` and fly to the hulk.
5. Make three slips from the tables in Step 9 on purpose. Read each message before you
   look at the table.
6. Close the game. In VS Code, open your `MyMission` folder again: **File**, then
   **Open Recent**.

`Practice` is yours to break. To be rid of it, delete its folder in File Explorer.

## Checkpoint

You are done when all five are true:

- VS Code shows the seven files of `MyMission` in its file list.
- `mission.amd` is in color, and the Status Bar says `AMD`.
- `sbs lint MyMission` says `clean`, with no line under it that starts `not checked:`.
- `sbs run server,helm,science -m MyMission map=0` opens three windows, and you flew the
  ship from the one named `helm`.
- You can say which of the seven files you will write in, and which one you will change a
  few lines of.

## Next

Lecture 4 is markdown, the marks your mission file is written in. You do it in VS Code,
with your `MyMission` folder open, so leave things as they are.

## Further reading

- "sbs - the Artemis Cosmos command-line helper", the tool's own README: the parts named
  "Starting a new mission", "`sbs run` - launch the game" and "`sbs debug` - test-fly a
  mission in the browser".
- "The AMD editor for VS Code" in the Open Universe documentation: what else the add-on
  can do. You meet its story tools in Class 2.
- "Creating a mission" in the library documentation: what each file in a mission's folder
  is for.
- "Workspace Trust" in the VS Code documentation, if you want to know why VS Code asked.
