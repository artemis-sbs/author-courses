# C2-8 video script - A Siege boss, part 1

Target length: 14 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished file is
`example\corsair_queen.amd`.

## Before recording

| Item | State needed |
|---|---|
| LegendaryMissions | A clean v1.4.0 folder with only the four shipped bosses in `maps\bosses` |
| `common_data\bosses` | Empty, or absent (scene 4 shows making it) |
| VS Code | The `data\missions` folder open (not `LegendaryMissions`), Artemis AMD extension installed, font size raised, no other tabs |
| Tools | An `sbs` that lints a shared folder: sbs_cli commit `fd357ee` or later, with sbs_utils `ef246a12` and LegendaryMissions `b6449c3` or later. On 2026-10-03 the sbs_cli change is committed and NOT released, so `sbs lint common_data\bosses` on a downloaded `sbs.pyz` warns about every boss field |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. It is started on camera in scene 8 |
| Second take of scene 9 | `Low: 90%` already saved, so the boss arrives within a minute |

## Confirm on camera

Items 2 to 5 were checked in the real engine on 2026-10-03 by a script, server only, with
no one at a console: the script thinned the raiders instead of shooting them, and read
the results from a file. Nobody has yet SEEN any of this on a screen. The recording
session is that check; if an item fails, stop and fix the page.

1. The Siege setup screen shows a **Boss** list under **Main**, and Corsair Queen is in it.
   (The engine's boss list does contain her; the screen itself is unseen.)
2. With `Low: 90%`, the boss arrives after the first two or three kills. (By script: 2
   seconds after 3 of 18 raiders were removed. Arrival after real kills is unseen.)
3. A ship named Morrigan arrives with two raider fleets. (By script: Morrigan, a
   `kralien_dreadnought`, with 8 escort ships.)
4. "Sink the Morrigan" appears in the crew's quest list when she does. (By script: the
   objective is granted and active. The quest list itself is unseen.)
5. Destroying every raider ends the game with the Siege victory text, and the side is
   paid the reward. (By script: objective and Siege complete; side credits rose by the
   reward.)
6. A boss file opened from `common_data\bosses` shows no squiggles, and neither does
   the shipped `warlord.amd`. (Checked 2026-10-03 by asking the editor's language server
   for its findings on both files: none on the shipped one, and only the planted
   mistakes on the other. Before that day's fix it reported six unknown fields on every
   boss file. The editor window itself is unseen.)
7. A two-word flagship name is underlined in the editor. (`sbs lint` flags it; the
   editor has not been checked.)
8. The boss in `common_data\bosses` is offered in the Boss list. (By script in the real
   engine on 2026-10-03: the Siege's boss list contained Corsair Queen read from that
   folder, and she arrived when chosen.)
9. `sbs lint common_data\bosses` prints the three lines the page shows. (Run on
   2026-10-03 with a test build of the tool; also run with the name left as `Warlord`
   and with `Fleats:`, and both warnings appeared.)

The reward and both lint warnings need a library build that includes the 2026-10-03
fixes. Record against that build or later.

Also capture the exact wording of the server screen for step 9 of the page, and the two
screenshots the page asks for.

## Scenes

### 1. Cold open (0:00 - 0:40)

**Screen:** The game. A dreadnought named Morrigan warps in with escorts. Cut to the quest
list showing "Sink the Morrigan". (Reuse footage from scene 9.)

**Say:** "This is the Corsair Queen. She is not in the game you downloaded. I wrote her
this morning, in one small text file, without writing any code. In the next fourteen
minutes you will write your own."

### 2. What a boss is (0:40 - 1:40)

**Screen:** The Siege setup screen, Boss list open, showing the four shipped bosses.

**Say:** "In Siege, raiders attack your starbases. If you choose a boss, then when the
raiders are nearly beaten, something worse arrives. Four bosses come with the game. Each
one is a single file in a folder. Add a file, and you have added a boss."

### 3. Read the Warlord (1:40 - 4:10)

**Screen:** VS Code. Open `maps`, `bosses`, `warlord.amd`. Highlight each line as it is
named.

**Say:** "Here is the Warlord. Two records, the shape you already know: a heading, a
fence, a body. The first record is the boss. `Boss` says what kind of record it is.
`Trigger` and `Low` say when she arrives: when a quarter of the raiders are left. `Flies`
and `Fleets` say what comes with her. `Difficulty: +1` makes her one step harder than
the game. `Named` is her flagship: a name, then which ship it is."

"The second record is a quest. You wrote these in Class 1. It belongs to the Siege's own
mission, the crew needs it to win, and it is done when the Siege says the raiders are all
gone."

### 4. Make the copy (4:10 - 5:00)

**Screen:** Right-click `warlord.amd`, Copy. Scroll to `common_data`. Right-click it, New
Folder, `bosses`. Right-click the new folder, Paste. Rename to `corsair_queen.amd`.

**Say:** "Never edit the Warlord. Copy it. And not into the game's folder. The game's
folder is replaced every time the game is updated. Yours is here: common data, bosses.
The Siege reads both. Lowercase, underscores, no spaces, and keep `.amd` on the end."

### 5. Rename the boss and the flagship (5:00 - 7:30)

**Screen:** Edit the heading to `# [Corsair Queen](corsair_queen)`. Edit `Named:` to
`Named: Morrigan kralien_dreadnought`.

**Say:** "Square brackets are what the crew reads. Round brackets are the key; match your
file name."

**Screen:** Briefly type `Named: Iron Duke kralien_dreadnought`, pause on it, then undo.

**Say:** "Two traps. Lint catches both, and you will see that in a minute, but know them
now. First: if you forget to change the name in square brackets, you get two Warlords
and the list shows only one. Second: the flagship's name is one word. Type 'Iron Duke'
and the game reads a ship called Iron, of a kind called Duke. There is no such ship."

### 6. Write her words (7:30 - 9:30)

**Screen:** Replace the description line. Change the quest heading to
`## [Sink the Morrigan](sink_morrigan)`, change the reward to 600, and replace the last
line. Replace the `//` notes at the top.

**Say:** "Now the part you are here for. One line for her entrance. Then the objective:
a new name, a new key, what it pays, and what you want the crew to read. Leave the five
lines in between alone today. Plain quotes and plain hyphens only; the game cannot draw
the curly kind."

### 7. Check it (9:30 - 10:40)

**Screen:** The saved file with no squiggles. Then the command prompt:
`sbs lint common_data\bosses`. Three lines: the file name, `clean`, and the count.

**Screen (insert):** Briefly restore the `Iron Duke` line, run lint, show the warning and
its suggested fix, then undo and run lint again.

**Say:** "Two checks. No squiggles in the editor. Then lint, pointed at my own folder, so
it checks my bosses and nothing else. You want the word 'clean'. Here is what it says if
I put 'Iron Duke' back: it tells me what the game will read, and what to write instead."

### 8. See her in the list (10:40 - 11:40)

**Screen:** Start the game as the server with LegendaryMissions. Choose Siege. Open the
Boss list. Choose Corsair Queen.

**Say:** "Start the server, choose Siege, open the Boss list. There she is. If she is
not, the file is in the wrong folder, or the mission was already running when you saved.
The list is read when the mission starts."

### 9. Meet her (11:40 - 13:20)

**Screen:** VS Code, change `Low: 25%` to `Low: 90%`, save. Restart the mission. Play:
destroy two or three raiders. The Morrigan arrives. Open the quest list.

**Say:** "At twenty-five percent you would fight for a long time before she shows up. For
testing, set it to ninety. Now she comes after the first kills. There is the Morrigan,
there are her escorts, and there is your objective, in your words. Put `Low` back to
twenty-five when you are done."

### 10. Keep it safe, and your turn (13:20 - 14:00)

**Screen:** File Explorer: `data\missions\common_data\bosses`, with
`corsair_queen.amd` in it, beside the `saves` folder.

**Say:** "This is why she lives here. Update the game and this folder is left alone. It
is still one file on one computer, so keep a copy, the way you would with a manuscript.
Now make a second boss, from your own story. The page has the steps and a checklist. Next
time, we change the numbers."
