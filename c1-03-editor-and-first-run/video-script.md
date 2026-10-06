# C1-3 video script - Your editor and your first run

> **Rewritten 2026-10-05 for a 1.4.0 install, got from Steam or itch.io.**
>
> - Removed: the second ending of `sbs create` (old libraries), the table "Checking,
>   before the libraries are up to date", the row for a game folder named `Cosmos-1-3-7`,
>   the firewall step, and the line `[server] listening on 0.0.0.0:8765` (the tool now
>   serves its page to this machine only). An older tool or older libraries is now one
>   trouble row. Added: one trouble row for a store putting its own files back (read,
>   not tried).
> - Step 4 stays, worded as "the libraries are published again from time to time; get
>   today's once".
> - The page was measured on a stand-in, not on a 1.4.0 download: the 1.3.7 archive with
>   the released tool (`0.12`) and today's libraries in it. The page's own path and its
>   slips were run there again today. A script checks it: 36 printed lines, 9 typed
>   commands and 27 quoted messages are found word for word in today's captures. Eight
>   more are from the pilot's captures and are named in item 8 below.

> **SEEN in a real window (2026-10-04 and 2026-10-05, by the session that sent the
> pilot).**
>
> - **The game, with the page's own line.** `sbs run server,helm,science -m <mission>
>   map=0` on the developer install, the template untouched: three windows titled
>   `server`, `helm` and `science`; the prompt came back after 12 seconds and printed
>   nothing; the map started with no click; both consoles were seated; the server window
>   showed the main screen; Artemis started 3,500 from DS 1; both logs empty. The windows
>   stayed up after the shell that started them had ended. NOT seen: Science's screen;
>   closing a real Command Prompt window.
> - **VS Code 1.140.0, a fresh profile, add-on 0.9.4, the stand-in's `MyMission`.** Not
>   trusted: NO box, the band (`Restricted Mode is intended for safe code browsing. Trust
>   this folder to enable all features.` with **Manage** and **Learn More**), `Restricted
>   Mode` at the left end of the Status Bar; the file IS colored, the corner says `AMD`,
>   and the Status Bar carries `AMD: trust this folder`; clicking that opens the
>   Workspace Trust page; **Trust** removes the band and starts the checker. A **Chat**
>   panel fills the right third of a fresh window.
> - Still nobody has seen: the installer; the Extensions view and **Install from VSIX**;
>   the Outline; the wavy line of Step 5; the `sbs debug` page in a browser; anything on
>   a Steam or itch.io install.

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. `example\` is the mission exactly as
`sbs create MyMission -t amd --title "The Cold Hulk"` left it: seven files, nothing
edited. A mission made today is the same, byte for byte (compared 2026-10-05).

## Before recording

| Item | State needed |
|---|---|
| The real 1.4.0 download | On a real Steam install AND a real itch.io install of 1.4.0, check three things. (1) The folder's path. (2) A command prompt there can write files: `sbs create Test -t amd` and `sbs update` both work without an administrator. (3) What the download holds: `sbs version`, and `sbs lint Test` BEFORE any `fetch`. The page assumes `sbs create` ends `Test is ready.` and lint says plain `clean`. If lint says `ERROR: could not load sbs_utils to lint`, the download's libraries are older than its tool, and Step 3 of the page needs its second ending back |
| `sbs run` on a Steam install | The tool starts `Artemis3-x64-release.exe` itself, three times. Check that Steam lets it: that three windows open, and that Steam does not step in or start the game a fourth time. NOT KNOWN |
| VS Code | NOT installed. A fresh Windows account, so the installer, the first start and the trust question are the real ones. Write down the version |
| VS Code, the trust question | The page gives both forms. In 1.140.0 there is no box, only a band at the top. Older copies ask in a box. Record what appears, and cut the page's table to that row if only one is ever seen |
| Add-on | The newest `Artemis AMD (VS Code)` release. The page names `amd-language-0.9.4.vsix` |
| Web browser | The Windows default. Watch for a warning on the `.vsix` download |
| Port 8765 | Free. And delete `%TEMP%\cosmos_dev_runner_8765.pid` if it is there: the tool stops whatever program has the number in that file |
| Screen | Wide enough for VS Code and three game windows. The tool places the game windows itself |
| Command prompt | Open in `data\missions`, font raised |
| Internet | On for the whole recording |

## Confirm on camera

"Run" means typed through `sbs.bat` in a real `cmd.exe` by script, in the stand-in, on
2026-10-05 with tool 0.12 and current libraries, output kept. "Pilot" means run the same
way on 2026-10-04 with an earlier tool and not run again. "Read" names what it was read
from and means it was not run. "UNSEEN" means nobody has looked at it.

**The tool:**

1. `sbs templates`: the block on the page. (Run.)
2. `sbs create MyMission -t amd --title "The Cold Hulk"`: every printed line, the
   question, Enter, no library fetched, `MyMission is ready.` and `14 of its 14 libraries
   were already here and were kept as they are.` One second. (Run.) The count is the
   stand-in's. A 1.4.0 download may say another number, or fetch one or two.
3. The folder holds seven files, and they are the page's `example\` byte for byte.
   (Run: compared.)
4. `sbs fetch "MyMission" --update-libs`: one line that starts `Fetching the libraries`,
   fifteen `Fetching` lines, the last line, seven seconds. (Run.) The mission folder and
   every library were the same afterwards. (Run: compared.)
5. `sbs lint MyMission` says `clean`. `sbs doctor MyMission` ends `0 problems`. (Run.)
6. `sbs run server,helm,science -m MyMission map=0 --dry-run`: the three lines. (Run.)
7. `sbs debug MyMission --map 0`, with its page: the lines on the page, the line that
   starts `[runner] GUI server started` and ends `open http://localhost:8765/` (it has a
   long dash in the middle), twelve `[runner] mastlib:` lines, then silence until it was
   stopped. (Run. No browser was opened and no firewall window can be seen from a
   script: check on camera that none appears.) The page titled `SBS Remote GUI` was
   fetched by script in the pilot, on the developer install. What it LOOKS like is
   UNSEEN.
8. Step 9's rows. (Run: every row of "Making the mission", "Starting the game",
   "Starting the rehearsal" and the first two of "The libraries".) From the pilot, not
   run again: the row for `--update-libs` with the internet off; `ERROR: could not load
   sbs_utils to lint` and the `Traceback` / `ImportError` block, which need old
   libraries; the `not checked:` line, which needs one library taken away; the Outline's
   eight names and the checker's message for line 47 (the checker was spoken to by
   script; the file is the same today).
9. `sbs debug` leaves `debug.log` in the folder the prompt is in, and a run leaves
   the two log files and `__pycache__` in the mission folder. (Run.)
10. `Ctrl+C` stops the rehearsal with `[runner] stopped`. (Read: `mission_runner.py`.)
    `cmd` then asks `Terminate batch job (Y/N)?` because `sbs` is a `.bat` file. UNSEEN.

**The add-on, measured without a window (pilot):**

11. The add-on is not in the VS Code Marketplace; a search for "Artemis AMD" returns
    other add-ons. The `.vsix` installs from the command line. (Pilot, with 0.9.3.) The
    menu path on the page was NOT used.
12. The checker the add-on starts answers in under a second. For `mission.amd` as
    created it reports nothing. With `(derelict_scan)` deleted it reports one error on
    line 47. It changes no file. (Pilot.)

**VS Code, read and UNSEEN:**

13. The installer: its file name, the page **Select Additional Tasks**, the five boxes.
    (Read: Microsoft's installer source and "VS Code on Windows".) UNSEEN.
14. The words **Open Folder...**, **Select Folder**, **Open Recent**, **Problems**,
    **Output**, **Outline**, **Installed**, **Install from VSIX...**, **Rename...**,
    `Plain Text`, `You have not yet opened a folder.`, `Do you trust the publisher`,
    **Trust Publisher & Install**. (Read: the message file of VS Code 1.140.0.) Where
    each sits on screen is UNSEEN.
15. The three dots at the top of the Extensions panel hold **Install from VSIX...**;
    whether the publisher question appears for a file install. UNSEEN.
16. The row of small buttons the add-on puts at the top right of an `.amd` file (the
    page does not mention them); the folder's name in capitals at the top of the file
    list; line numbers; the red wavy line; the round dot on an unsaved tab. UNSEEN.

**The game:**

17. `sbs run server,helm,science -m MyMission map=0`: SEEN on the developer install
    (the block at the top). NOT seen on a Steam or itch.io install.
18. Each window comes up on the console it was named for. One run in two, another pilot
    saw the Helm window come up as a second Engineering console. If it happens on
    camera, close everything and add `--settle 4`.
19. The hulk is in Science's list; the first step finishes inside 2000. (Other pilots of
    this class, in the engine. Not this one.)
20. Closing the command prompt leaves the game running and stops the rehearsal. The
    first half was seen (the block at the top). The second is REASONED. The page marks
    both rows. Try both off camera and take the marks off.

**The stores, read and UNSEEN:**

21. Steam's **Verify integrity of game files**, or a game update, puts back the files
    the game shipped with: the tool and the shipped missions. A folder the student made
    is left alone. (Read: Steam Support names the button, under **Properties...** and
    **Installed Files**. It does not say which files are replaced. NOT RUN.)

If item 2, 7, 17 or 21 turns out differently on camera, stop and fix the page.

## Scenes

### 1. Cold open

**Screen:** VS Code on the left with `mission.amd` in color. On the right the game's Helm
window, the ship under way.

**Say:** "On the left is a mission, | and on the right is that same mission, being played.
|| An hour ago, neither of them existed. ||| In this lecture, you put an editor on your
computer, | you make a mission with one line, and you fly it. || You don't write anything
yet, | because today is about having the desk ready. ||"

### 2. Get VS Code

**Screen:** The browser at `code.visualstudio.com`. Download. Run the installer. Stop on
**Select Additional Tasks** and tick the two "Open with Code" boxes. Finish. VS Code
opens. Point at the four parts.

**Say:** "A mission is plain text, and plain text wants an editor. || A word processor
changes what you type: | it curls your quote marks and it joins your hyphens, | and the game
can read neither. ||| So we use VS Code, which is free. || You download it, and you run the
installer. || Only one page of it matters, and it's this one. | Tick both of these boxes,
and leave the rest. ||| Then there are four names to learn for this window: | the strip of
icons, the panel beside it, | the big area where your files open, | and the bar along the
bottom. ||"

### 3. The add-on

**Screen:** The browser at the release page. Click `amd-language-0.9.4.vsix`. Back in VS
Code: the Extensions icon, the three dots, **Install from VSIX...**, the file. The entry
**Artemis AMD** under Installed. Then type "Artemis" in the search box and show what it
offers. Clear it.

**Say:** "VS Code doesn't know what a mission file is, | so one add-on teaches it. || VS
Code calls an add-on an extension, | which isn't the same thing as the extension on a file's
name. ||| The add-on is one file. || I download it, and then I hand it to VS Code here: |
the three dots, and then install from V S I X. ||| One warning, though: don't search for it.
|| It isn't in this list, | and these others have nothing to do with our game. ||"

### 4. Make the mission

**Screen:** The command prompt. Point at the prompt line. `sbs templates`. Then the
`create` line, typed slowly. The question. Enter. `MyMission is ready.` Point at the
line under it: the libraries were already here. Then File Explorer: the new folder.

**Say:** "Now back to the window from last time. || Check the line first: it should end in
data, missions. || First I ask what I can start from, | and there are five templates. || We
want this one, A M D. ||| Now the line that makes a mission. || It's create, then the
folder's name, with no spaces. | Then hyphen T, and the template. || Then two hyphens,
title, | and in quote marks, the name the crew will see. ||| It stops to ask one question, |
and Enter means yes. || And there's the folder, right beside the game's own missions. ||"

### 5. Bring the libraries up to date

**Screen:** `sbs fetch "MyMission" --update-libs`. The lines scroll. The last line.

**Say:** "There's one more line, and you type it once. || Missions share program parts
called libraries. || They came with the game, | and create kept them just as they are. ||
But they're mended and published again from time to time, | so this fetches today's build of
each one. ||| Read the last line: my mission itself was not changed. || And never leave off
the end of this command, update libs, | because without it, fetch does a different job. ||"

### 6. Open the folder, and trust it

**Screen:** **File**, **Open Folder...**, to `data\missions`, click `MyMission`, **Select
Folder**. Whatever VS Code shows about trust: answer it. The file list. Point at each of
the seven.

**Say:** "Now I open the mission in the editor, | and I open the folder, not a file. || So
it's file, open folder, | one click on my mission, and select folder. ||| VS Code now asks
whether I trust this folder. || I wrote it, so yes. || That matters more than it looks, |
because until you say yes, the add-on only colors the file, | and its checking waits. |||
There are seven files here. || This one is yours: mission.amd. || This one, you'll change a
few lines of, later on. | And the other five are plumbing. ||"

### 7. The add-on at work

**Screen:** Click `mission.amd`. Point at a colored heading, at `AMD` in the Status Bar,
open **Outline**. Go to line 47, delete `(derelict_scan)`. The wavy line. **View**,
**Problems**. `Ctrl+Z`. Then type a space, show the dot on the tab, `Ctrl+Z`, `Ctrl+S`.

**Say:** "There are three signs that the add-on is alive. || There's color, and there are
the letters A M D down here, | and there's the outline: eight headings, one inside another.
||| Now I'll break something on purpose. || On line forty-seven, I take off the part in
round brackets, | and a red wavy line appears. || It's telling me the heading has lost its
key. || Control Z, and it's mended. | And nobody typed a command. ||| There are two keys to
keep: | control Z takes back, and control S saves. || A dot on the tab means not saved, |
and the game reads the saved file, not my screen. ||"

### 8. Check it

**Screen:** The command prompt: `sbs lint MyMission`. Highlight `clean`.

**Say:** "Here's the same check, on the whole mission, from the command prompt. || There's
one word to look for, and it's clean. || This command has a lecture all to itself. ||"

### 9. Play it

**Screen:** The `run` line with `--dry-run`. Three lines. Up arrow, rub out `--dry-run`,
Enter. Three windows open. Point at each title bar. In `helm`: find DS 1 and the Unknown
Hulk, set a course, engines. In `science`: the hulk in the list. Close all three.

**Say:** "Now for the game itself. || A run line starts several copies at once: | a server,
which runs the mission, and the consoles I ask for. || I always look first. | Dry run prints
what it would start, and starts nothing. ||| So it's server, helm, science, with commas and
no spaces. || Then hyphen M and my mission, | and map equals nought, which means start the
first map without asking me. || Good. Now I run it for real. ||| Three windows open, and
each one says what it is. || Here I am at Helm. | There's the station, and there, nine
thousand beyond it, is an unknown hulk. || I fly to it, and that's the sample quest's first
step. ||| When I'm done, I close all three. | Every one of them, before I start again. ||"

### 10. The rehearsal

**Screen:** `sbs debug MyMission --map 0`. The lines. Point at the three that read like
faults. The browser at `localhost:8765`. Back to the prompt: `Ctrl+C`, `Y`.

**Say:** "There's a second way, with no game windows at all. || The tool plays the mission
itself, and shows it in my browser. ||| It prints about twenty lines, and three of them read
like trouble. || They aren't. They're printed for every new mission. || Then it goes quiet,
and the prompt doesn't come back. || That's right, because it's running. ||| So I open this
address. || This is a drawing of a console, and not the game. | It's quick, and it's enough
for a look. || To stop it, press control C, here. || And when a lecture says play it, use
the game. ||"

### 11. Four slips

**Screen:** `sbs create MyMission -t amd`: already exists. `sbs run MyMission --dry-run`:
the note. `sbs run server, helm -m MyMission map=0 --dry-run`: the blank name. Then the
page's tables.

**Say:** "Here are four slips, so that you've seen them. || The first is create, twice. | It
refuses, and that's the tool protecting your work. || The second is the mission's name where
the consoles go: | you get one window and no server, with only this note to tell you. || The
third is a space after a comma, | which gives you a window with no name, and no note at all.
||| And the fourth you've already met: | an untrusted folder, and a file that's colored but
not checked. || The page has tables of more than thirty, and each one was tried. ||"

### 12. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now make a second mission, called Practice, without the page. || Open it, trust
it, | break line forty-seven and mend it, | and then fly it with one console. ||| After
that, open My Mission again, and leave it open. || Next time, you'll learn the marks that
file is written in. ||"
