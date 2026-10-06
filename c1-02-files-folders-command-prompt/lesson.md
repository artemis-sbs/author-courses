# Class 1, Lecture 2 - Files, folders and the command prompt

## What you will have at the end

A window open in the right folder, one command typed into it, and its answer read.

You will find the game's folder on your computer. You will find the `missions` folder
inside it. You will open a command prompt there and ask the game's own tool two
questions: which version are you, and is this computer set up? Every later lecture
begins with the words "a command prompt open in `data\missions`". After today that is
ten seconds' work.

*[Screenshot to add: File Explorer on `data\missions`, the command prompt beside it, and
the prompt line marked.]*

You install nothing in this lecture. One step may replace the tool with its newest
version. Nothing else on your computer changes.

## The video

*[Link to add when recorded.]*

## Before you start

- A computer with Windows 10 or Windows 11.
- Artemis Cosmos 1.4.0, installed from Steam or from itch.io. It is the copy you played
  in Lecture 1.
- The internet, for one step.

Words for this lecture:

| Word | Meaning |
|---|---|
| File | One named thing on your disk: a picture, a page of text, a program |
| Folder | A named box that holds files and other folders |
| Extension | The last part of a file's name, after the last dot: `.bat`, `.amd`, `.txt`. It says what kind of file it is |
| Path | The full address of a file or a folder: the drive, then every folder on the way down, joined by backslashes. `C:\Cosmos\data\missions` |
| Command prompt | A window where you type an instruction and press Enter, and the answer is printed under it |
| Current folder | The folder the command prompt is standing in. The window shows it at the start of every line |
| Command | The line you type |
| Switch | A word in a command that starts with two hyphens. It changes how the command works: `--env` |

On this page the game's folder is written `C:\Cosmos`. That is a short stand-in. Steam
or itch.io chose your folder for you, so your path is longer and may have spaces in it.
The tool does not mind spaces. Wherever this page says `C:\Cosmos`, read your own.

## Step 1 - Find the game's folder

The game's folder is the one that holds the program the game runs from. The program's
name is `Artemis3-x64-release.exe`. Windows may show it without the `.exe` on the end.
Step 3 explains why.

The app you got the game from will open the folder for you:

| You got the game from | How to open its folder |
|---|---|
| Steam | In the **Library**, right-click the game. Choose **Manage**, then **Browse local files** |
| The itch.io app | In your library, right-click the game, or click the gear beside **Launch**. Choose **Manage**, then **Open folder in Explorer** |

A File Explorer window opens on the game's folder. With Steam the path usually ends
`\Steam\steamapps\common\` and then the game's own folder.

If neither works: in File Explorer (the yellow folder on the taskbar, or the Windows
key and `E`), click **This PC**, click in the search box, and type
`Artemis3-x64-release`. When it is found, right-click it and choose **Open file
location**.

You are in the right folder when you see these four names:

| Name | What it is |
|---|---|
| `Artemis3-x64-release` | The game itself |
| `data` | Everything the game shows and plays: art, sound, missions |
| `PyRuntime` | A helper program the game brings with it. The tool you meet today runs on it |
| `PyAddons` | A few more helper files |

There are other files beside them. Leave them alone.

## Step 2 - Go down to `missions`, and read the path

1. Double-click `data`.
2. Double-click `missions`.

This is where you will work for the whole course. Look at what is here:

| Name | What it is |
|---|---|
| `LegendaryMissions`, and other folders | One folder for each mission. Yours will be one more folder, beside these |
| `__lib__` | Program parts that missions share. You do not change it |
| Two files whose names start with `sbs` | The tool. Step 3 shows you their whole names |

Now the path. At the top of the window is the address bar. It shows the folders you came
through, one after another. Click once in the empty part of the address bar, to the
right of the last name. The names turn into one line of text:

```
C:\Cosmos\data\missions
```

That line is the path of this folder. Read it from the left: the drive `C:`, the folder
`Cosmos` on it, the folder `data` inside that, the folder `missions` inside that. The
backslash `\` means "inside".

Press Esc to put the address bar back.

Write your own path down. You will want it again.

## Step 3 - Show file name extensions

Windows hides the extension of every kind of file it knows. So a file named `sbs.bat`
is shown as `sbs`, and a file named `mission.amd.txt` is shown as `mission.amd`. The
second one costs new writers an evening: the file looks right, and the game cannot find
it.

Turn the hiding off. You do this once, and Windows remembers.

| Windows | Where the switch is, in File Explorer |
|---|---|
| Windows 11 | **View**, then **Show**, then **File name extensions** |
| Windows 10 | The **View** tab, then tick **File name extensions** |

Look at the folder again. The file that read `sbs` now reads `sbs.bat`.

| File | What it is |
|---|---|
| `sbs.bat` | Two lines of text. It starts the tool. When you type `sbs`, this is the file Windows runs |
| `sbs.pyz` | The tool itself |

These are the extensions you will meet in this class:

| Extension | Kind of file |
|---|---|
| `.amd` | Your fact sheet: quests, scans, people. Most of your writing goes here |
| `.mast` | The story file. You change a few lines of it, from cards |
| `.json`, `.yaml` | Settings |
| `.log` | Notes the game writes while it runs |
| `.txt` | Plain text. If this ends up on the end of one of the names above, the file is misnamed |
| `.bat`, `.pyz` | The tool. Do not open or rename them |

Do not double-click `sbs.bat` or `sbs.pyz`. You use them from the command prompt.

## Step 4 - Open a command prompt in `data\missions`

1. In File Explorer, be in `data\missions`.
2. Click once in the empty part of the address bar, as you did in Step 2. The path is
   highlighted.
3. Type `cmd`. It replaces the path.
4. Press Enter.

A window opens with a dark background and a few lines of text. The last line is:

```
C:\Cosmos\data\missions>
```

That is the command prompt. Opened this way, it starts in the folder you were looking
at.

Look at the start of that last line before you type anything, now and every time. If it
starts with the letters `PS`, you have a different program, called PowerShell. It looks
almost the same and it will not run the tool. Type `cmd`, press Enter, and the `PS` goes
away.

Windows offers two other ways to open a window like this: **Open in Terminal** on the
right-click menu, and Shift with a right-click. Both can give you PowerShell. Use the
address bar.

## Step 5 - Read the prompt line, and look around

```
C:\Cosmos\data\missions>
```

| Part | Meaning |
|---|---|
| `C:\Cosmos\data\missions` | The current folder: where the window is standing. It is the same path you read in Step 2 |
| `>` | "Your turn." The window is waiting for a command |

You type a command after the `>` and press Enter. Nothing happens until you press
Enter. A box on this page that holds a command shows only the words you type. Never type
the path or the `>`.

Your first command lists what is in the current folder. Type it and press Enter:

```
dir
```

It prints one line for each thing in the folder. Here are four of them:

```
10/04/2026  09:31 PM    <DIR>          LegendaryMissions
10/05/2026  10:36 AM               121 sbs.bat
10/05/2026  10:36 AM         2,756,752 sbs.pyz
10/05/2026  11:13 AM    <DIR>          __lib__
```

| On the line | Meaning |
|---|---|
| The date and time | When it was last changed. Yours differ |
| `<DIR>` | This one is a folder |
| A number | This one is a file, and that is its size |
| The last word | Its name, with its extension |

There are a few more lines above and below the list. The list itself starts with two
odd names, `.` and `..`. One dot stands for this folder, and two dots for the folder that
holds it. You use the two dots in Step 8.

It is the same list File Explorer shows you. The command prompt and File Explorer are
two windows onto one folder.

Four keys to know now:

| Key | What it does |
|---|---|
| Enter | Runs the line you typed |
| Up arrow | Brings back the last command you ran. Press it again for the one before |
| Backspace | Rubs out the character before the cursor |
| Esc | Clears the line you are typing |

To paste into the window, press `Ctrl+V`, or click the right mouse button. To copy out of
it, drag across the text with the mouse and press `Ctrl+C`.

## Step 6 - Your first command to the tool

The tool is called `sbs`. A command to it is the word `sbs`, a space, and what you want.
Type:

```
sbs version
```

The answer is two lines:

```
0.12
C:\Cosmos\data\missions
```

| Line | Meaning |
|---|---|
| `0.12` | The tool's version |
| `C:\Cosmos\data\missions` | The folder the tool lives in. It should be the path you wrote down |

Read the version as two whole numbers with a dot between them. `0.12` is "nought, twelve".
It is newer than `0.9`, which is "nought, nine".

This course needs `0.12` or a higher number. The tool that comes with 1.4.0 has one.

The tool is mended and published again from time to time. To get the newest, with the
internet on:

```
sbs update
```

It fetches the newest `sbs.bat` and `sbs.pyz` and puts them over the ones you have. It
ends with:

```
Updated sbs in C:\Cosmos\data\missions. Type `sbs version` to see the new number.
```

If the download did not work, it ends with this, and leaves the tool as it was:

```
ERROR: the new sbs could not be downloaded. Nothing was changed: the sbs you have still works. Check the internet connection and type `sbs update` again.
```

Do this whenever `sbs version` answers a number lower than a page of this course
names. Then ask `sbs version` again.

## Step 7 - Ask the tool whether this computer is set up

```
sbs doctor --env
```

`doctor` is the command. `--env` is a switch: it means "this computer only, not the
missions". The answer is about thirty lines:

```
sbs
  ok  version     0.12
  ok  running     from sbs.pyz
  ok  missions    C:\Cosmos\data\missions
Python
  ok  version     3.11.1 embedded (C:\Cosmos\PyRuntime\python.exe)
  ok  paths       PYTHONPATH is ignored and site-packages is not on sys.path
      use `sbs deps install X` for optional libraries
Layout
  ok  __lib__     112 libraries
  ok  sbs_utils   sbslib: C:\Cosmos\data\missions\__lib__\artemis-sbs.sbs_utils.v1.4.0.sbslib
  ok  graphics    C:\Cosmos\data\graphics
  --  faces       cosmos_dev is not installed
      faces will print as placeholders in `sbs docs`
  ok  PyAddons    C:\Cosmos\PyAddons (with ryaml)
Tools
  --  git         not found
      needed by `sbs fetch --source`
  ok  curl        curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP
  ok  browser     chrome 154.0.8037.97 (C:\Program Files\Google\Chrome\Application\chrome.exe)
  --  weasyprint  not installed - PDFs will have no contents page numbers
      install the WeasyPrint package; pip alone cannot supply its GTK libraries
Sidecar
  --  sbs         empty (C:\Cosmos\data\missions\__pylib__)
  --  engine      empty (C:\Cosmos\PyAddons)
install
  ok  art         37 baked, 176 not yet drawn, 0 half-baked in data/graphics

17 checks: 12 ok, 5 optional absent, 0 problems
```

Most of it is written for a programmer. You need three things from it.

**First, read the last line.** It is the count.

```
17 checks: 12 ok, 5 optional absent, 0 problems
```

`0 problems` is the answer you want. Your other numbers can be one or two away from
these. If it says `1 problem`, see "If something goes wrong" below.

**Second, the mark at the start of each row.**

| Mark | Meaning | What you do |
|---|---|---|
| `ok` | Fine | Nothing |
| `--` | Something extra is not on this computer. It is not a fault | Nothing |
| `!!` | A problem | Read that row, then "If something goes wrong" below |

**Third, a line set further in belongs to the row above it.** Under a `--` row it says
what you would get if you had the extra thing. Under `ok  paths` it is a note for
programmers. Neither is an instruction to you. The five `--` rows above are normal on a
writer's computer. None of them stops you building a mission.

The words at the left edge name the parts of the report:

| Part | What it looked at | Can you act on it? |
|---|---|---|
| `sbs` | The tool: its version, and the missions folder it is working in | Yes. A low version: Step 6. A wrong folder: you are in another copy of the game |
| `Python` | The helper program in `PyRuntime` that the tool runs on. It comes with the game. You never install it and never write it | No |
| `Layout` | The folders the tool expects beside it: `__lib__`, the game's art | Only if a row has `!!`. See "If something goes wrong" |
| `Tools` | Other programs on your computer that the tool can use | No |
| `Sidecar` | Extras for programmers | No |
| `install` | The game's ship art. `0 half-baked` is the part that matters | No |

## Step 8 - Get lost on purpose, and come back

Windows finds the word `sbs` in one folder only: `data\missions`. See what happens
anywhere else.

`cd` means "change the current folder". Go into a mission's folder:

```
cd LegendaryMissions
```

Nothing is printed. Look at the prompt line: it now ends
`\data\missions\LegendaryMissions>`. Ask the tool for its version:

```
sbs version
```

```
'sbs' is not recognized as an internal or external command,
operable program or batch file.
```

Read it as: "there is nothing called `sbs` in the folder you are standing in". That is
true. `sbs.bat` is one folder up.

Go back up. Two dots mean "the folder that holds this one":

```
cd ..
```

The prompt line ends `\data\missions>` again. Now press the up arrow twice. `sbs version`
comes back. Press Enter.

```
0.12
C:\Cosmos\data\missions
```

You will see the "not recognized" message again in this course. It has two causes, and
the prompt line tells you which:

| The prompt line | The cause |
|---|---|
| Does not end in `\data\missions>` | You are in the wrong folder |
| Ends in `\data\missions>` | You misspelled the first word |

Three more commands for finding your way:

| You type | What it does |
|---|---|
| `cd` | With nothing after it: prints the current folder |
| `cls` | Wipes the window clean. Nothing is lost but the old text |
| `exit` | Closes the window |

The surest way back from anywhere is to close the window and open a new one from the
address bar, as in Step 4. You lose nothing by closing it.

## Step 9 - Check it: what the window says when you slip

Every row was typed on a copy of the game. The middle column is what came back.

**In the wrong place:**

| What you did | What the window says | The way back |
|---|---|---|
| `sbs version` with the prompt in the game's folder, in `data`, in a mission's own folder, or on the Desktop | `'sbs' is not recognized as an internal or external command, operable program or batch file.` | Read the prompt line. Open a new window from the address bar of `data\missions` |
| `sbs version` in a window whose prompt line starts with `PS` | `The term 'sbs' is not recognized as the name of a cmdlet, function, script file, or operable program.` and more | That is PowerShell. Type `cmd` and press Enter |
| `cd E:\Cosmos\data\missions`, when the prompt is on drive `C:` and the game is on drive `E:` | Nothing. The prompt line does not change | Add `/d` after `cd`: `cd /d E:\Cosmos\data\missions`. Or open the window from the address bar |
| `cd data\mission` (a folder name misspelled) | `The system cannot find the path specified.` | Check the spelling against File Explorer |
| The tool started by its whole path from another folder: `C:\Cosmos\data\missions\sbs version` | `0.12` and the path of `data\missions` | None needed. By its whole path the tool runs from any folder. The short word `sbs` runs only in `data\missions` |
| The same, when the path has a space in it and no quote marks round it | `is not recognized as an internal or external command`, after the part of the path before the space | Put quote marks round the path: `"C:\Artemis Cosmos\data\missions\sbs" version` |

**Typing slips, in the right place:**

| What you typed | What the window says | What it means |
|---|---|---|
| `sbs doctr` | `Error: No such command 'doctr'. (Did you mean one of: 'docs', 'doctor'?)` | The second word is misspelled. The two lines above the error tell you how to ask for help |
| `sbd doctor` | `'sbd' is not recognized as an internal or external command, operable program or batch file.` | The first word is misspelled. It is the same message as the wrong folder |
| `sbsdoctor` | `'sbsdoctor' is not recognized as an internal or external command, operable program or batch file.` | The space is missing |
| `SBS VERSION` | `Error: No such command 'VERSION'.` | `SBS version` works. The words after `sbs` are in small letters |
| `sbs help` | `Error: No such command 'help'.` | Type `sbs` alone for the list of commands, or `sbs doctor --help` for one command |
| `sbs doctor -env` (one hyphen) | `Error: No such option '-e'.` | A switch has two hyphens |
| `sbs doctor -- env` (a space after the hyphens) | `ERROR: not a folder: env` | No space inside a switch |
| `sbs doctor –env` (a long dash, pasted from a word processor) | `ERROR: not a folder:` and the dash with `env` | Type two plain hyphens. A word processor turns two hyphens into one long dash |
| `sbs --env doctor` | `Error: No such option '--env'.` | The switch goes after the command it belongs to |
| `sbs doctor SecretMeting` | `ERROR: not a folder: SecretMeting` | A folder name is misspelled. `sbs doctor secretmeeting` works: capitals in a folder's name do not matter |
| `sbs doctor My Mission` | `Error: Got unexpected extra argument (Mission)` | A space ends a word. A name with a space in it needs quote marks: `"My Mission"`. Better: no spaces in the name of a mission's folder |
| `dir My Mission` | `File Not Found` | The same. `dir "My Mission"` works |
| A path on a line by itself: `C:\Cosmos\data\missions` | `'C:\Cosmos\data\missions' is not recognized as an internal or external command, operable program or batch file.` | A path is not a command. Put `cd /d` and a space in front of it. A path in quote marks gets the same message, quote marks and all |

**What nothing warns you about:**

| What you did | What happens | What tells you |
|---|---|---|
| Pasted a line with the prompt still on it: `C:\Cosmos\data\missions>sbs version` | The "not recognized" message, and an empty file named `sbs`, with no extension, is left in the folder | Nothing. Delete that file in File Explorer: it is the one with no extension and no size. Leave `sbs.bat` and `sbs.pyz` |
| `cd` to a folder on another drive, without `/d` | Nothing changes | Nothing. The prompt line is the same as before |
| Opened PowerShell in place of the command prompt | The window looks the same | Only the `PS` at the start of the prompt line |
| Ran a tool that is older than a page of the course | `sbs version` answers its number and nothing more | Nothing. Compare the number with the one in Step 6 |

Spaces and brackets in the path of the game's folder are fine. `sbs version` and
`sbs doctor` were tried in a folder shaped like Steam's,
`Program Files (x86)\Steam\steamapps\common\Artemis Cosmos`, and ran as usual.

## Step 10 - Use it: the long report

Leave the switch off, and `doctor` looks at every mission as well:

```
sbs doctor
```

It starts with the report you have just read. After that comes one part for each mission
folder. The window scrolls. Use the mouse wheel to go back up.

Read the last lines first. You want `0 problems` there, as in Step 7. Then look at one
mission's part:

```
LegendaryMissions
  ok  story.json  1 sbslib, 0 mastlib, 0 media
  ok  libraries   all declared libraries present
  ok  art         0 baked, 0 not yet drawn, 0 half-baked in mission art
```

| In the report | In plain words |
|---|---|
| `LegendaryMissions` | The name of a mission's folder |
| `story.json` | The mission's list of the program parts it asks for. Your numbers may differ |
| `libraries` | Whether every part it asks for is in the `__lib__` folder |
| `art` | The mission's own ship art. Most missions have none |

If the count is not `0 problems`, the line under it says `to fix:` and names the part of
the report to scroll up to. Two rules for a `!!` row under a mission:

1. **Is it your mission?** A mission that came with the game is not yours. Leave it.
2. **Do not type a command because a report says so.** The line set further in, under a
   `!!` row, suggests a command. For a mission of your own it is usually the one you
   meet in Lecture 3, with your mission's name in it. And never type `sbs fetch` with
   nothing after it. That asks one question. If you answer yes, it replaces the whole
   `LegendaryMissions` folder with a fresh copy.

To look at one mission only, put its folder's name after the command:

```
sbs doctor LegendaryMissions
```

That prints the report on this computer, then the part for that one mission, and ends:

```
20 checks: 15 ok, 5 optional absent, 0 problems

content checks: sbs lint <folder> (AMD), sbs compile <folder> (MAST)
```

When you have a mission of your own, this is the form you will use.

The last line names two more commands, `sbs lint` and `sbs compile`. `doctor` looks at
how things are set up. It never reads your writing. `sbs lint` does, and it has a
lecture of its own.

## If something goes wrong

| What you see | Likely cause, and what to do |
|---|---|
| `'sbs' is not recognized as an internal or external command` | The prompt is not in `data\missions`, or the first word is misspelled. Read the prompt line |
| `The term 'sbs' is not recognized as the name of a cmdlet` | The window is PowerShell. Type `cmd` and press Enter |
| `sbs version` answers a number lower than `0.12`, or the report has a row `!!  sbs_utils   older than this sbs needs` | Your tool or your program parts are older than this page. Type `sbs update`. For the row, also do Lecture 3, Step 4, once you have a mission: `sbs fetch "MyMission" --update-libs` |
| The tool was current last week and now `sbs version` answers a lower number | The store put its own files back. Steam does this when you ask it to check the game's files (**Properties**, **Installed Files**, **Verify integrity of game files**), and a game update can do it too. Type `sbs update` again. The missions that came with the game are put back as well. A mission folder you made is not one of the game's files and is left alone. (Read, not tried) |
| `Error: No such command` and a word you did type | A typing slip in the second word. If it offers `Did you mean`, it is guessing well |
| `The system cannot find the path specified.` | A folder name in your command is misspelled |
| `can't open file` and a path that ends `sbs.pyz` | `sbs.bat` is here and `sbs.pyz` is not. See the next row |
| `SyntaxError`, and above it a line that is not an answer, such as `404: Not Found` | `sbs.pyz` is a failed download. In your web browser open `https://github.com/artemis-sbs/sbs_cli/releases/latest`, click `sbs.pyz` in the list named **Assets**, and move the file from your Downloads folder into `data\missions`, over the one there |
| `!!  libraries` under a mission that came with the game | Not yours. Leave it. See Step 10 |
| The top of the report has scrolled away | Turn the mouse wheel. Or use `sbs doctor --env`, which is short |
| The window stops and its title starts with `Select` | You clicked inside it. Press Esc |
| A dark window flashed and was gone | You double-clicked `sbs.bat`. It listed its commands and closed. Nothing was changed |
| Windows asks how to open the file | You double-clicked `sbs.pyz`. Choose Cancel |
| You closed the window | Open another, as in Step 4. Nothing is lost |

## Exercise

Do this without the page in front of you. Then check yourself against it.

1. Close the command prompt and File Explorer.
2. Open File Explorer and go to the game's folder, then to `data\missions`.
3. Open `LegendaryMissions`. Find the four files `story.mast`, `story.json`,
   `description.yaml` and `script.py`. Every mission has these four. Say what the
   extension of each is.
4. Go back to `data\missions`. Open a command prompt there from the address bar.
5. Read the prompt line aloud. Is there a `PS` at the start?
6. Type `dir`. Find `sbs.bat` and `sbs.pyz` in the list.
7. Type `cd LegendaryMissions`, then `dir`. Find the four files from item 3.
8. Type `cd ..` and check the prompt line.
9. Type `sbs doctor LegendaryMissions`. Find the count line. How many problems?
10. Make three slips from the tables in Step 9 on purpose. Read each message before you
    look at the table.

Write two things on the first page of your notes: the path of your `missions` folder,
and your tool's version.

## Checkpoint

You are done when all five are true:

- File Explorer shows the name `sbs.bat`, with its extension.
- You can open a command prompt whose prompt line ends `\data\missions>`, with no `PS`
  in front.
- `sbs version` prints `0.12` or a higher number, and under it the path of your
  `missions` folder.
- `sbs doctor --env` ends with `0 problems`.
- You can say what each of these is: a file, a folder, an extension, a path, the current
  folder.

## Next

Lecture 3, "Your editor and your first run", gives you an editor, VS Code, and your
first mission. You make the mission with one command, `sbs create`, typed into the
window you learned to open today. Lecture 4, "Markdown in twenty minutes", teaches the
marks your mission file is written in.

## Further reading

- "sbs - the Artemis Cosmos command-line helper", the tool's own README. Read "Getting
  the tool running" and "`sbs doctor` - check your setup". Do not try `sbs production`
  or `sbs fetch` from it yet: both replace mission folders.
- "Checking your setup: `sbs doctor` and `sbs deps`" in the library documentation, the
  part called "Reading the output".
- "The `sbs` CLI" in the library documentation: the table of commands at the top. You
  will use a handful of them in this class.
