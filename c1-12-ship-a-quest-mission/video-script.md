# C1-12 video script - Capstone: ship a quest mission

> **SEEN AND CHANGED SINCE (2026-10-05, by the session that sent the pilot):**
>
> - **The finished example was started in the real game** with
>   `sbs run server,helm,science -m <mission> map=0`. Helm's ship panel says `Kittiwake`;
>   `Marrow Station` is named on Helm's map; the Quest Log lists `The Dark Beacon` with
>   `Find the Lantern`, and `The Keeper` (`9:07 left`) with `Come Alongside` and `First on
>   Scene` (`1:07 left`). The runtime log was empty. NOT seen: the mission in the server's
>   list (the launch line skips it), the tender arriving, the win and lose sentences.
> - **`sbs lint` now reads `description.yaml`** (tool source `de32da3`, after 0.12; it
>   reaches students in the next release). A hyphen or a second colon outside quote marks
>   is an error, `description-stops-the-game`. The boxed rule in Step 3 and the row in the
>   checking table say so. This was the pilot's headline finding.
>
> **Measured 2026-10-05. When written: NOT run in the real engine, and nothing seen in a
> window.**
>
> - Tools: `sbs` 0.12 (sbs_cli `1dbb865`), library sbs_utils `1fd5e171` and
>   LegendaryMissions `b20726f` as released, in `__lib__`.
> - The lesson starts from Lecture 11's finished `mission.amd` and `story.mast` plus the
>   other five files of Lecture 3's `example\`. `example\` here is those seven files after
>   58 changes of words (`c112\build_final.py` holds the list; each old text is checked to
>   be in its file exactly once). No key is changed.
> - Student commands (`lint`, `doctor`, `docs`, `fetch --update-libs`, `debug --no-gui`)
>   were run on the stand-in student install (`SCRATCH\c12\Artemis Cosmos`, built from the
>   1.3.7 download, real PyRuntime, tool 0.12, current libraries), with a plain Windows
>   PATH. Its game program is an empty file, so no game was run there.
> - Rename and mistake variants (32) were linted with the installed tool and, where the
>   game matters, played headless with the packaged library in the developer install, one
>   at a time, by Lecture 11's probe: ship beside the hulk, beside the skiff, 24 seconds,
>   then home. One run waited out the ten minutes to the `Lose:` sentence.
> - 33 tool messages quoted on the page were checked against the captures by
>   `c112\verify_page.py`: 32 found. The 33rd (`no PDF engine found`) was produced by
>   naming a browser that does not exist, and seen once; it is not in a saved capture.
> - The printed pages were looked at as headless screenshots of the two web pages
>   (`c112\shot_prose.png`, `shot_bible.png`). The PDF itself was not opened: it is a real
>   PDF of three pages by its own header.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 11 leaves it, lint clean: `mission.amd` 185 lines, `story.mast` 115 lines, line 111 the card's route line, line 113 the `npc_spawn` line; `settings.yaml` line 70 is `    -   name: "Artemis"`; `description.yaml` lines 11 and 14 say `The Cold Hulk` |
| A finished copy | `example\` copied to a second folder, so scene 3 can cut from the first edits to the finished text |
| Tool and libraries | `sbs version` says 0.12 or later; `sbs fetch "MyMission" --update-libs` run that day |
| VS Code | Mission folder open, `mission.amd` and `story.mast` in tabs, font raised. Close it before scene 6 |
| Command prompt | A plain one in `data\missions`, cleared, wide |
| Logs and leftovers | Leave `__pycache__` and the two logs in the folder: scene 10 deletes them on camera |
| A second machine or a second install | For scene 11. With the tool that came with the game still on it, so `sbs update` is real |
| The hyphen | Decide before recording whether to SHOW the game failing on a hyphen in `description.yaml` (scene 5). It stops the game for every mission until the file is mended. If shown, mend it on camera |
| Browser | Chrome or Edge installed. Note which: the PDF line names it |

## Confirm on camera

What was checked, and how. "Lint", "Doctor", "Docs" mean the released tool run on the
stand-in. "Mock" means the mission played headless with the packaged library. Nobody has
SEEN any of this lesson in the game or in a window. If an item fails while recording,
stop and fix the page.

Make it yours:

1. Lecture 11's files, untouched: lint `clean`, won headless with 500 credits. (Lint,
   Mock.)
2. The 58 changes of words give `example\`: lint `clean`. Played: the map is named `The
   Quiet Lantern` with the new description; the objects are Marrow Station, Lantern Nine,
   The Keeper's Skiff and, 20 seconds after the step starts, Tender Osprey; the ship is
   Kittiwake; the Quest Log rows carry the nine new names; the messages read `Quest
   complete: Come Alongside` and so on; the game ends with the new `Win:` sentence and
   500 credits; both logs empty. (Lint, Mock.)
3. Nobody near anything for ten minutes: First on Scene fails at two minutes, the game
   ends with the new `Lose:` sentence. (Mock, one run.)
4. With Match Case on, none of the eight old names is anywhere in the seven files. (A
   search by script.)
5. `settings.yaml`: the name changed, with or without quote marks, gives a ship of that
   name. A lost quote mark or a lost space: lint `clean`, the ship is Artemis again, and
   `mast.runtime.log` gets one line beginning `ryaml refused`. (Lint, Mock.) NOT known:
   whether the engine writes the same line.
6. `description.yaml` with a hyphen, with a colon, or deleted: lint `clean`, doctor `0
   problems`, the mock runs. (Lint, Doctor, Mock.) That a bare hyphen stops the engine
   at start is from another session's engine measurement of 2026-09-20, not from this
   pass.

Renaming keys (Step 4), each on the finished example:

7. Replace All in both files for `salvage`, for `derelict` (plain, and whole word), for
   `tug` (plain, and whole word), and `lifeboat` in `mission.amd`: lint `clean`, won with
   500. (Lint, Mock; done by script, not by VS Code's button.)
8. Every row of the "by hand" table, and the two `clean` rows in particular: arc key
   changed through `mission.amd` only, and the waiting step's key changed in heading and
   `Then:` only. Lint `clean`; no tender after 24 seconds; the step stays active. (Lint,
   Mock.)
9. `Done when: reach lantern 500` with no role `lantern`: lint `clean`. The same line
   with `beacon`: `role-nothing-wears`. (Lint.) With every `derelict` in `mission.amd`
   changed to `lantern`, the first step never finished. (Mock.)
10. The four "safe by themselves" rows and the deleted first arc. (Lint, Mock.)

Check it:

11. `sbs doctor QuietLantern` on the stand-in: the three-row block and `20 checks: 15 ok,
    5 optional absent, 0 problems`. The untouched template mission gives the same count.
    (Doctor.) The count on a student's machine depends on what is installed.
12. Each row of the doctor table and of "What each check sees", except the cells that say
    "Not tried in the game". (Lint, Doctor, Mock.)

Print it:

13. The command on the page prints the four lines on the page and makes the two files; it
    opens no window (`--open` is the only thing that does; read in `docs_cmd.py`). (Docs.)
14. With Edge named as the browser the PDF is made too: 88,446 bytes, three pages. (Docs.)
    On a machine with only Edge the line should read `pdf (edge <version>)`: read in
    `pdf_out.py`, not seen, because this machine has Chrome.
15. The player document holds names and sentences only; without `--profile player` it
    adds `Objective`, `Reward` and `When`. No document holds the `Win:` or `Lose:`
    sentence, and the bible prints `False` for both. (Docs, text compared by script.)
16. A person with `Face:` prints as a box saying `a face`, with or without `--assets
    embed`, on the stand-in. (Docs.)

Share it:

17. The cleaned folder zips to 7,062 bytes, one folder holding seven files. (Made with
    Python's zip, not with Explorer's menu.)
18. Unpacked into the stand-in's `data\missions`: `sbs fetch "QuietLantern"
    --update-libs` fetched fifteen files in eight seconds and ended with the line on the
    page; the libraries were byte for byte what was there. Lint `clean`, doctor `0
    problems`, `sbs debug QuietLantern --no-gui --map 0` started the map and ran for 45
    seconds with both logs empty. The same under the name `Lantern From Ada`, in quotes.
    (Lint, Doctor, Mock.)
19. Every row of "What goes wrong on their side", except the last. (The stand-in.)

Not seen, and to watch for while recording:

1. Any screen of the game with this mission: the server's list with the new title and
   description, Kittiwake at Helm, the Quest Log, the readings on Science, the win and
   lose screens. Step 6's list is the mock's facts in the engine's order.
2. `sbs run server,helm,science -m QuietLantern map=0`: not run. It is Lecture 3's line
   with another folder name.
3. Renaming the folder in File Explorer with `F2`, and whether Windows refuses while a
   command prompt or VS Code has the folder open. Whether VS Code asks for trust again.
4. VS Code's Replace in Files: `Ctrl+Shift+H`, the `Aa` and `ab` buttons, the list of
   results, Replace All, Save All. The replacements were made by script.
5. The two zip menus (Windows 11 and 10), and Extract All making a folder inside a
   folder. The nested folder was made by script.
6. The PDF on a screen and on paper.
7. What the engine does with a mission that has no `description.yaml`, and with a colon
   or an apostrophe in a value there. The page says: letters, numbers, spaces, commas,
   full stops.
8. The whole friend's path on a machine with the real game: `sbs update` from the
   shipped tool, the fetch, then the game. And whether a 1.3.7 game runs a mission that
   names the v1.4.0 libraries at all.
9. Whether ten minutes is enough to fly it by hand. Lectures 10 and 11 asked the same.

## Scenes

### 1. Cold open

**Screen:** Two machines, or two windows. On one, a command prompt: the last line of
`sbs fetch`. On the other, the game starting with a mission called The Quiet Lantern.

**Say:** "That's a mission I wrote, | starting on a computer that isn't mine. || Today is
the last lecture of this class, | and there's nothing new to learn in it. || Today, you
simply finish it. ||| You make the mission yours, | you check it, you print it, | and then
you give it to someone. ||"

### 2. The plan, on paper

**Screen:** The table from Step 1, on the page. Fill the last column by hand, or show it
filled.

**Say:** "Don't start by typing. || What you've built is a shape: | go out, find a second
thing, wait, | and come home, against a clock. || Every slot in that shape has a name that a
player reads, | and a handle that the game uses. || So write your story into the slots
first. ||| Here's mine: a navigation beacon has gone dark, | its keeper is missing, and a
storm is ten minutes out. ||"

### 3. The words

**Screen:** `mission.amd`. Change the main arc's heading, `Win:`, `Lose:` and
description. Point at `(salvage)` untouched. Change one step: name, `Objective:`,
description; point at `Done when: reach derelict 500` untouched. Change one reading. Cut
to the finished file and scroll it. Then `story.mast`: lines 25, 26, 64, 68, 113.

**Say:** "There's one rule: change names and sentences, and leave every key. || The square
brackets are mine, | and the round brackets are the game's. || So my beacon is still called
derelict underneath, | and no player will ever see that word. ||| I change the win line, and
the lose line. || Then an objective, where the number in it | must still agree with the line
under it. || And then a reading. || That comes to fifty-eight changes, and not one key. |||
Then the script, which has five places, all between quote marks. || It's the first pair of
quotes on each line. || The second pair is the side and the roles, so leave it. ||"

### 4. Lint

**Screen:** `sbs lint MyMission`: clean.

**Say:** "Lint says clean, because words can't break the chain, | and that's why we change
them first. ||"

### 5. Two small files

**Screen:** `description.yaml`, lines 11 and 14. Then `settings.yaml`, line 70. Show the
boxed rule on the page.

**Say:** "Now, two files you haven't opened. || This one is what the server shows in its
list of missions, | and you change two lines in it. || And there's one rule here that
matters more than any other today: | no hyphen, and no colon, in these two values. || The
game reads this file for every mission, before it shows anything, | and a hyphen here stops
the game. || Not your mission, the game. ||| Lint reads this file now, and it stops you with
an error. || Doctor doesn't read it. || So keep to plain words, commas and full stops, | and
run lint after you change it. ||| Then the ship, on line seventy. || Change the word between
the quote marks, and nothing else. || If I break this line, my ship is Artemis again, and
nothing tells me. || I find out when I play. ||"

> If the hyphen is shown on camera: say what the screen really does, then mend the file.

### 6. Renaming a key, the safe way

**Screen:** `Ctrl+Shift+H`. `salvage` to `keeper`. Turn on `Aa` and `ab`. Scroll the
results: nine, one of them in `story.mast`. Replace All, Save All, lint: clean. Then undo
it all, change the key by hand in `mission.amd` only, lint: clean. Show the two `clean`
rows of the table.

**Say:** "You don't have to do this. || But if a key bothers you, | there's one way, and
only one: | Replace, across the whole folder, with both buttons on. || Read the list first:
there are nine places, | and look at the last one, which is in the script, on my card. || So
it's replace all, save all, and lint. | It's clean, and it works. ||| Now for the other way.
|| I change it by hand, all through the fact sheet. || Lint says clean, and it's broken. ||
The tender never comes, and the game can't be won. || The address on the card | is the one
place lint can't follow a key. ||"

### 7. The folder gets its name

**Screen:** Close VS Code. File Explorer, `data\missions`, `F2` on `MyMission`, type
`QuietLantern`. Command prompt: `sbs lint MyMission` (the error), `sbs lint
QuietLantern`.

**Say:** "Everybody in this class has a folder called My Mission. || So if you send yours to
a classmate, | it lands on top of theirs. || That's why it gets its own name, with no
spaces. || Nothing inside the files knows the folder's name. || Only I do, in every command
from now on. ||"

> Say what Windows and VS Code really do here. None of it was seen.

### 8. Check it: three checks

**Screen:** `sbs lint QuietLantern`. `sbs doctor QuietLantern`: scroll to the last block
and the count. Then the game: `sbs run server,helm,science -m QuietLantern map=0`. The
list in Step 6, item by item, speeded up. The two logs. The table "What each check sees".

**Say:** "There are three checks, | and each one sees what the others can't. || Lint asks,
is the writing right? || Doctor asks, is everything this mission needs on this computer? ||
Look for the block with my folder's name, | and then the last two words: zero problems. ||
Doctor never reads my writing. ||| And then comes the play. || There's my ship, my station,
and my beacon. | Then the skiff, the wait, and the tender. || Then home, and my win line. ||
Both logs are empty. || And then I read every sentence once more, as a reader. ||"

### 9. Print it

**Screen:** The `sbs docs` command with `--title`, `--profile player`, `--pdf`. Its four
lines. File Explorer: `__docs__`. Open the PDF. Then `sbs docs QuietLantern --lens
bible`, open the page, scroll the beats.

**Say:** "My mission is also a text, | and it takes one command. || It has a title, it says
player, which means leave out the machinery, | and it asks for a PDF. || That makes two
files, in a new folder. ||| This is for a friend who reads, | and not for a friend who
plays, | because it's the whole plot, in order. || And there's one for me, called the bible.
|| It goes beat one, beat two, | with reached from, and leads to. || If a step's in the
wrong place here, | a Then line points at the wrong place. || There's one thing it gets
wrong: | it says win, false, and lose, false. || My two sentences are fine. | It's the
printing that isn't. ||"

> Say what the PDF really looks like. It was not opened.

### 10. Share it: my side

**Screen:** The mission folder. Move the PDF out. Delete `__docs__`, `__pycache__`, the
logs. Count seven files. Up one folder. Right-click, compress. `QuietLantern.zip`.

**Say:** "A mission is a folder, | so to share it, I send the folder. || First I take out
what isn't the mission. || That's my documents, because they're the plot, | and the scratch
folder and the logs, | which come back by themselves. || That leaves seven files, | and it's
all seven, not only the two I wrote. || Then the folder itself gets zipped, | and it comes
to seven kilobytes. ||"

### 11. Share it: their side

**Screen:** The second machine. The zip opened; the folder dragged into `data\missions`.
Open it: `story.mast` is there. Command prompt: the four lines of the note. The last line
of the fetch. The game starts.

**Say:** "My friend puts the folder where mine is. || There's one check: open it, | and the
files are right there, not another folder. || Then it's four lines: is the tool new enough,
| and if it isn't, update it. || Then fetch the libraries this mission names, | because even
if they play every week, theirs may be older than mine. || And then start it. ||"

> Then show Extract All making a folder in a folder, and the fetch error. Say what Windows
> really does.

### 12. Done

**Screen:** The rubric on the page.

**Say:** "And that's the class. || The rubric on the page is what done means, | and you can
tick every line yourself. || Then do the first exercise: | send it to one person, and don't
help them. ||| Class 2 puts people in your story. ||"
