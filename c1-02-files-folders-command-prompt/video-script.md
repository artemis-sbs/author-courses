# C1-2 video script - Files, folders and the command prompt

> **Rewritten 2026-10-05 for a 1.4.0 install, got from Steam or itch.io.**
>
> - Removed: everything the page said about an older copy of the game. The tool at 0.4,
>   the two accounts of what an old tool prints on `sbs update`, the `1 problem` branch of
>   `sbs doctor --env`, the `demosiege` example and the archive's stray files. One trouble
>   row is left: "your tool or your program parts are older than this page".
> - Added: the two store menus that open the game's folder, and a trouble row for a store
>   putting its own files back. Both are read from the stores' help pages. Nobody has
>   seen them.
> - The page was measured on a stand-in, not on a 1.4.0 download: the 1.3.7 archive with
>   the released tool (`0.12`) and today's libraries put into it. Every tool line on the
>   page was run there again today. A script checks it: 48 printed lines and 32 quoted
>   messages are found word for word in today's captures. One quoted message, `!!
>   sbs_utils   older than this sbs needs`, is from the earlier capture with 0.11; the
>   0.12 source still prints it (`doctor_cmd.py`).
> - **Still unseen: every window.** Nothing on the page has been looked at on a screen.

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. There is no `example\` folder: the lecture
makes no file.

## Before recording

| Item | State needed |
|---|---|
| The real 1.4.0 download | On a real Steam install AND a real itch.io install of 1.4.0, check three things. (1) The folder's path. Steam's default is under `C:\Program Files (x86)\Steam\steamapps\common\`. (2) A command prompt opened there from the address bar can write files: type `sbs update`, and in Lecture 3 `sbs create`. If either is refused, the page needs a step, and so does every later lecture. (3) What the download holds: the four names in the game's folder, `sbs.bat` and `sbs.pyz` in `data\missions`, which missions, and what `sbs version` and `sbs doctor` answer |
| The store menus | Steam: Library, right-click the game, **Manage**, **Browse local files**. itch.io app: right-click the game or the gear beside **Launch**, **Manage**, **Open folder in Explorer**. If a menu reads differently, fix Step 1 of the page |
| Windows account | A fresh one, so File Explorer still hides extensions |
| Python | Not installed. With Python installed, `.pyz` is a kind of file Windows knows, and both tool files read `sbs` until Step 3 |
| The tool | Type `sbs version` off camera. The page assumes `0.12` or higher. Type `sbs doctor --env` and `sbs doctor`: the page assumes both end `0 problems` |
| Internet | On, for scene 8 |
| Word processor | Open, with `sbs doctor --env` typed in it. It must have turned the two hyphens into one long dash |
| Command prompt | Not open. It is opened on camera. When it is: font raised, and wide enough that the longest row of the report does not wrap. A Steam path is long: check the `sbs_utils` row |
| Windows | Record on Windows 11. Show the Windows 10 menu for extensions as a still |

## Confirm on camera

"Run" means the command was typed through `sbs.bat` in a real `cmd.exe`, by script, in
the stand-in, on 2026-10-05 with tool 0.12, and its output was kept. "Read" means it
comes from a document or from the tool's source and was not run. "UNSEEN" means nobody
has looked at it.

1. `sbs version` prints the version and the folder. (Run.)
2. The `sbs doctor --env` block on the page. (Run.) On the recording machine these will
   differ: every path, `112 libraries`, the `browser` row (Edge on a stock machine), the
   `art` numbers, and the `git` row if git is installed. The count line changes with
   them.
3. `sbs doctor` and `sbs doctor --env` change no file. (Read: `doctor_cmd.py`. Measured
   in the first pilot on the developer install, not run again.)
4. `sbs doctor LegendaryMissions`: the mission's three rows and the last three lines.
   (Run. The row `1 sbslib, 0 mastlib, 0 media` is the stand-in's LegendaryMissions. A
   1.4.0 download may print other numbers.)
5. `sbs doctor` with no folder ends `0 problems`. NOT RUN in that state: the stand-in
   holds a 1.3.7 mission, `demosiege`, that gives `1 problem`. Check it on the real
   download. If it names a mission there, the page needs that mission's name.
6. The wrong-folder message, from the game's folder, `data`, a mission's folder and the
   Desktop. (Run.)
7. Every row of "Typing slips, in the right place". (Run.) How the window draws the long
   dash in `ERROR: not a folder:` is UNSEEN: the tool sent the byte `0x96`.
8. `cd` to another drive does nothing and says nothing; `cd /d` works; `cd ..`; `cd`
   alone prints the folder; a misspelled folder name. (Run.)
9. The tool started by its whole path from another folder runs. A path with a space
   needs quote marks. (Run.)
10. A line pasted with the prompt on it leaves an empty file named `sbs`, and `sbs`
    still runs afterwards. (Run.) How File Explorer lists that file is UNSEEN.
11. A path with spaces and brackets. (Run: the stand-in's own folder is `Artemis
    Cosmos`, and it was reached once more through a folder named `Program Files
    (x86)\Steam\steamapps\common\Artemis Cosmos`. `sbs version`, `sbs doctor --env` and
    `sbs doctor LegendaryMissions` ran as usual. That was a link in a scratch folder. It
    says nothing about whether Windows lets you write under the real `Program Files`.)
12. PowerShell: `sbs version` fails with `The term 'sbs' is not recognized...`;
    `.\sbs version` works. (Run, in Windows PowerShell 5.1 started by script.) The red
    block a real window adds is UNSEEN. Typing `cmd` there: only `cmd /c "sbs version"`
    was run. The window is UNSEEN.
13. `sbs update` from 0.12. (Run, with the internet and with it blocked: the two endings
    on the page. With the internet the two tool files came back the same, byte for
    byte.) How the window draws it is UNSEEN.
14. `sbs.pyz` missing, and `sbs.pyz` replaced by a 14-byte failed download: the two
    messages in "If something goes wrong". (Run.) The download by hand from the releases
    page is UNSEEN. A browser may warn about a `.pyz` file.
15. The row `!!  sbs_utils   older than this sbs needs`. (Run with 0.11 on 2026-10-05
    morning, with libraries as the 1.3.7 archive ships them; not run again. Read: 0.12
    prints the same words.)
16. Steam: **Manage**, **Browse local files** opens the game's folder. (Read, not seen.
    The menu names came from the course owner. The Steam Support pages fetched today
    give the default folder, `C:\Program Files (x86)\Steam\steamapps\common\`, and do
    not name this menu.)
17. itch.io app: **Manage**, then **Open folder in Explorer**. (Read, not seen. The
    app's own documentation says the Manage dialog opens "from the game's page, or from
    its right-click menu in your library", and that the app installs games to "a folder
    your user has write access to without requiring administrator rights". The button's
    name **Open folder in Explorer** is not on the pages fetched: it came from the
    course owner.)
18. A store puts its own files back. (Read, not measured. Steam Support, "Verify
    Integrity of Game Files": **Properties...**, the **Installed Files** tab, the
    **Verify integrity of game files** button. That page does not say which files it
    replaces. That it restores `sbs.bat`, `sbs.pyz` and the shipped missions, and leaves
    a folder the student made, is reasoning from "it restores the files the game shipped
    with". NOT RUN.)
19. File Explorer, all UNSEEN: the search and **Open file location**; the four names in
    the game's folder (they are the top of the 1.3.7 archive: check the download); the
    click that turns the address bar into a path; `cmd` typed there opening a command
    prompt in that folder; the two menus for **File name extensions**; what `sbs.bat`
    and `sbs.pyz` read as before and after.
20. The command prompt window, all UNSEEN: the prompt line; the up arrow; Esc;
    Backspace; paste with `Ctrl+V` or the right mouse button; copy with a drag and
    `Ctrl+C`; `cls`; `exit`; the mouse wheel; the lines `dir` prints above and below its
    list.
21. "The window stops and its title starts with `Select`". UNSEEN. The old console does
    this. Windows Terminal does not. Check which one the recording machine opens.
22. A double-click on `sbs.bat` (a window that flashes) and on `sbs.pyz` (Windows asks
    how to open it). UNSEEN. `sbs` with nothing after it only lists commands. (Run.)
23. **Open in Terminal** and Shift with a right-click give PowerShell. UNSEEN.
24. With nothing after it, `sbs fetch` asks before it replaces `LegendaryMissions`.
    (Read: `fetch_cmd.py`. NOT RUN.)

If item 2, 5, 16, 17 or 19 turns out differently on camera, stop and fix the page.

## Scenes

### 1. Cold open

**Screen:** A command prompt, already open. `sbs doctor --env`. The report prints.
Freeze on the last line.

**Say:** "This is the game telling me that my computer is ready to build missions. ||
Seventeen checks, and no problems. ||| By the end of this lecture, you'll have asked it the
same question, | and you'll know how to read the answer. || And if you've never seen a
window like this one, good, | because this lecture is for you. ||"

### 2. Files, folders, and the two windows

**Screen:** File Explorer, on any folder with a few files and a folder in it. Point at a
file, then at a folder.

**Say:** "Everything on your computer is a file, and files live in folders. || A file is one
named thing: | a picture, a page, a program. || A folder is a box with a name, | and boxes
go inside other boxes. ||| This window, File Explorer, is one way to look inside a box. ||
The command prompt is another. || Today you'll use both of them, on the same box. ||"

### 3. Find the game's folder

**Screen:** Steam, the Library. Right-click the game, **Manage**, **Browse local
files**. The game's folder. Then the itch.io app's menu as a still. Point at
`Artemis3-x64-release`, `data`, `PyRuntime`, `PyAddons`.

**Say:** "So first, where is the game? || You didn't choose its folder, the store did, | so
ask the store. || In Steam, go to the library, right-click the game, | then choose manage,
and browse local files. || In the itch app, right-click the game, | then manage, and open
folder in Explorer. ||| Either way, a window opens on the game's folder, | and you know
you're in the right place when you see these four names. || This one is the game itself. |
Data is everything it shows and plays. | And these two are helpers that it brings along. ||
Leave everything else alone. ||"

### 4. Down to missions, and what a path is

**Screen:** Double-click `data`, then `missions`. Point at the mission folders, `__lib__`
and the two `sbs` files. Click the empty part of the address bar: the path. Esc.

**Say:** "Now go into data, and then into missions. || This is where you'll work for the
whole course. || Each of these folders is one mission, | and yours will be one more, right
beside them. ||| Now look up here, at the address bar. || If I click in the empty part of
it, | the names turn into one line of text. || That line is a path, | which is the full
address of this folder. || It reads: drive C, then the folder Cosmos, | with data inside it,
and missions inside that. || So the backslash just means inside. || Write your own path
down, because you'll want it again. ||"

### 5. Show the extensions

**Screen:** Point at the file that reads `sbs`. **View**, **Show**, **File name
extensions**. The file now reads `sbs.bat`. Then the Windows 10 menu as a still.

**Say:** "There's one setting to change, and you only change it once. || Every file's name
ends in a dot and a few letters. | That's the extension, and it says what kind of file this
is. || And Windows hides it from you. ||| So this file says sbs, | when its real name is
sbs.bat. || Here's why that matters to you. || In a few lectures, you'll save a file called
mission.amd. || If Windows quietly saves it as mission.amd, dot T X T, | it still looks
right on the screen, and the game can't find it. ||| So open view, then show, and tick file
name extensions. || And now nothing is hidden. ||"

### 6. Open the command prompt, here

**Screen:** Click the empty part of the address bar. Type `cmd`. Enter. The window
opens. Zoom on the last line. Then, briefly, a PowerShell window beside it, with `PS` at
the start of its line.

**Say:** "Now for the other window. || It's the same click on the address bar, | and this
time I type C M D, and press Enter. ||| This is the command prompt. || Look at its last
line: | it's the path we just read, and then an arrow. || The path is where this window is
standing, | and the arrow means it's my turn. ||| One warning, though: Windows has a second
program that looks just like this one, | and it's called PowerShell. || You can tell it by
the letters P S at the start of the line, | and our tool won't run there. || So if you ever
see P S, type C M D, press Enter, and it goes away. ||"

### 7. Look around: dir, and four keys

**Screen:** `dir`. Point at a `<DIR>` line, at `sbs.bat`, at `sbs.pyz`. Then File
Explorer beside it: the same names. Up arrow, Enter: `dir` again.

**Say:** "Here's my first command: D I R, and Enter. || It lists what's in this folder. ||
Where a line says D I R in brackets, that's a folder. | Where it has a number, that's a
file, and the number is its size. ||| And it's the same list that File Explorer shows, |
because these are two windows onto one folder. || There are four keys to know. || Enter runs
the line. | The up arrow brings back the last line I ran. | Backspace rubs out a letter, |
and Escape clears the whole line. ||"

### 8. The first command to the tool

**Screen:** `sbs version`. Two lines. Then `sbs update`, wait, `sbs version` again.

**Say:** "The game comes with a tool for mission writers. || It's called sbs, and it lives
in this folder: | those were its two files. || A command to it is the word sbs, a space, and
then what I want. | So I'll ask it for its version. ||| Two lines come back: | its version,
and the folder it lives in, | which should be the path you wrote down. || Read the version
as two whole numbers, | so the second one counts like any other number, and a bigger one is
newer. || The page tells you the lowest one that will do. ||| The tool is mended and published again from time to time.
|| To get the newest, type sbs update, and wait for it to finish. || It says updated, and
where. | Then ask for the version again. || Do that whenever a page of this course names a
higher number than yours. ||"

### 9. Is this computer set up?

**Screen:** `sbs doctor --env`. Let it print. Highlight the last line. Then one `ok`
row, one `--` row, and the indented line under a `--` row.

**Say:** "Now the real question. || It's sbs doctor, and then a switch: two hyphens, and E N
V. || A switch changes how a command works, | and this one means, look at this computer
only. ||| It prints about thirty lines, and most of them are written for a programmer. ||
You need three things from it. || The first is the last line, which says no problems, | and
that's your answer. || The second is the mark at the start of each row. || O K means it's
fine. | Two hyphens means something extra isn't here, and that's not a fault. || Two
exclamation marks would be a problem, and you have none. ||| And the third: a line that's
set further in belongs to the row above it. || Under two hyphens, it says what the extra
thing is for. | It's not an instruction. || A few rows like that are normal on a writer's
computer. ||"

### 10. Get lost on purpose

**Screen:** `cd LegendaryMissions`. Point at the prompt line. `sbs version`: the "not
recognized" message. `cd ..`. Up arrow twice, Enter: it works.

**Say:** "Windows finds sbs in one folder only, and it's this one. || Watch what happens
somewhere else. || C D means change folder, so I'll go into a mission. || The line on the
left has changed. || Now I ask for the version, | and it says, not recognized. ||| Read that
as: there's nothing called sbs where you're standing. || And that's true, because it's one
folder up. || C D and two dots means go up one. || Then the up arrow, twice, and Enter, |
and it works again. ||| You'll see that message again. || When you do, read the start of the
line before anything else. || And if all else fails, close the window, | and open a new one
from the address bar. ||"

### 11. Three slips

**Screen:** `sbs doctr`: the error and its guess. Then the word processor: copy
`sbs doctor --env` with its long dash, paste, Enter: `not a folder`. Then the page's
tables.

**Say:** "Here are three slips, so that you've seen them once. || The first is a misspelled
command: | the tool says no such command, and guesses what I meant. || The second is a
command copied from a word processor. || It turned my two hyphens into one long dash, | and
the tool takes that dash for a folder name. || So type the hyphens here, in this window. |||
And the third you've just seen, which is the wrong folder. || The page has tables of more
than twenty slips, and each one was tried. ||"

### 12. The long report

**Screen:** `sbs doctor`. It scrolls. Scroll back with the wheel. The last lines. Go
to the `LegendaryMissions` part. Then `sbs doctor LegendaryMissions`.

**Say:** "Without the switch, doctor looks at every mission too. || It scrolls, and that's
fine, because I read the end first. || It says no problems, so I'm done. ||| Each mission
has a part like this one: | three rows, and all of them O K. || If the end ever names a
mission, I scroll up to that mission, | and I keep two rules. || The first: is it my
mission? | One that came with the game isn't mine, so I leave it. || The second: the line
under a problem suggests a command. || Don't type it just because a report told you to. |||
And never type sbs fetch on its own, | because that replaces a whole mission folder. || To
look at one mission, I put its folder's name after the command. ||"

### 13. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now do it without me. || Close both of the windows, | then find the folder, open
the prompt, and read the line. || Run doctor on one mission, and make three slips on
purpose. || Then write down your path, and your version. ||| Next time, you get an editor, |
and you make your first mission in the window you opened today. ||"
