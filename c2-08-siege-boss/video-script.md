# C2-8 video script - A Siege boss, part 1

> **STATE ON 2026-10-08. This replaces every earlier note in this file.**
>
> - Everything the page needs is released: the tool (`sbs lint common_data\bosses` works
>   with the installed one), the library and LegendaryMissions. The page is written for
>   Artemis Cosmos 1.4.0 from Steam or itch.io.
> - **Re-measured today.** 30 files: the steps typed in order, the finished file, and
>   one change to the finished file at a time. Each was linted with the installed `sbs`.
>   26 were played headless, one at a time, in a Siege run from a probe copy of
>   LegendaryMissions with its own `common_data\bosses` folder. A script
>   (`c2b\verify_page.py`) found every line of tool output on the page in those runs.
> - **How a headless game stands in for a crew.** The boss is chosen by the setting the
>   Boss line writes. Raiders are not shot: the harness takes them out of the Siege's count,
>   two at a time or all at once. So "destroyed" on the page means "left the count".
> - **Checked in the real engine on 2026-10-03**, by a script, with nobody at a console: her
>   name in the Boss list read from `common_data\bosses`, the arrival, the Morrigan and her
>   escorts, the objective granted, the win and the reward. Not run in the engine again
>   today.
> - **Seen in the real game:** Legendary Missions' start screen, Siege on the left, and the
>   Options panel on the right with a Boss line. Nothing else in this lecture has been
>   seen on a screen.
> - The `narration\` folder beside this file was generated from the older script and is
>   stale.

The companion page is `lesson.md`; the finished file is `example\corsair_queen.amd`.

## Before recording

| Item | State needed |
|---|---|
| Game | Artemis Cosmos 1.4.0, closed. Started on camera in scene 8 |
| LegendaryMissions | As it comes with the game: four bosses in `maps\bosses` |
| `common_data\bosses` | Empty, or absent (scene 4 shows making it) |
| VS Code | The `data\missions` folder open (not `LegendaryMissions`), the AMD add-on installed, font size raised, no other tabs |
| Command prompt | Open in `data\missions`, cleared, wide enough for one long warning |
| Second take of scene 9 | `Low: 90%` already saved, and a crew that can destroy two raiders |

## Confirm on camera

"Lint" is the installed tool on that exact file. "Mock" is a headless Siege from the probe
copy. "Engine" is the scripted run of 2026-10-03. If an item fails while recording, stop
and fix the page.

1. The copy, before a word is changed, earns one warning, `duplicate-boss-name`, on line 6.
   (Lint.)
2. After Steps 3 to 7 lint says `clean`, in the three lines the page prints. (Lint, after
   each step.)
3. Corsair Queen is on the Boss line's list, after the game's own four. (Mock: the list
   the drop-down is built from reads `None, Continuous, Infestation, Ragnarok, Warlord,
   Corsair Queen`. Engine: she was in it. The open list itself is unseen.)
4. `sbs run server,helm,weapons -m LegendaryMissions` stops the server at the start
   screen. (Read from the tool's help: with no `map=` nothing is started. Unseen with this
   exact line; the start screen itself has been seen.)
5. With `Low: 90%` and sixteen raiders she arrives after the second one is gone, within
   four seconds. (Mock: sixteen at the start, arrival 4.7 seconds after two left the
   count. With nobody shooting she had not arrived after 40 seconds.)
6. The Morrigan, a `kralien_dreadnought`, arrives with two fleets of three to five ships.
   (Mock: 6 to 9 escort ships over twelve arrivals. Engine: 8.)
7. Sink the Morrigan is in the Quest Log when she arrives. (Mock: granted and active.
   The Quest Log with it in is unseen.)
8. Nothing tells the crew she arrived. (Mock: nothing was sent to any ship at the
   arrival.)
9. Every raider gone ends the game with `Victory! The starbases held.` and 1,100 credits.
   (Mock and Engine. The crew is told `Quest complete: Break the Siege`, `Quest complete:
   Sink the Morrigan`, `Mission complete: Repel the Siege`.)
10. The two tables in Step 8: sixteen rows, each linted, and each played where the row
    says what the game does. (Lint, Mock.)
11. Unseen, all of it: the Copy, Paste and Rename steps in VS Code, any underline in the
    editor, the lint warning in a real command prompt, a real kill bringing her in.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** The game. A dreadnought named Morrigan among the raiders. Cut to the Quest Log
showing "Sink the Morrigan". (Reuse footage from scene 9.)

**Say:** "This is the Corsair Queen, | and she isn't in the game you installed. || I wrote
her this morning, in one small text file, | and I didn't write any code to do it. |||
By the end of this lecture, | you'll have a boss of your own in that list. ||"

### 2. What a boss is

**Screen:** Legendary Missions' start screen. Siege on the left. The Options panel on the
right, the Boss line's list open, showing the game's four bosses.

**Say:** "You played Siege in the very first lecture. || Raiders come at your starbases, |
and you win when the last raider is gone. || Now, if you choose a boss, | something worse
arrives when the raiders are nearly beaten. ||| Four bosses come with the game, | and each
one is a single file in a folder. || So if you add a file, you've added a boss. ||"

### 3. Read the Warlord

**Screen:** VS Code, the `data\missions` folder open. Open `LegendaryMissions`, `maps`,
`bosses`, `warlord.amd`. Highlight each line as it is named.

**Say:** "Here's the Warlord, and it's two records, | in the shape you already know: | a
heading, a fence, and a body. || The first record is the boss herself. || There's one word
alone on a line, the word Boss, | which says what kind of record this is. || Trigger and
Low say when she arrives: | when a quarter of the raiders are left. || Flies and Fleets
say what comes with her, | and Named is her flagship: | a name, and then which ship it is.
||| The second record is a quest, | and you wrote plenty of those in Class 1. || It
belongs to the Siege's own mission, | the crew needs it to win, | and it's done when the
Siege says every raider is gone. ||"

### 4. Make the copy

**Screen:** Right-click `warlord.amd`, Copy. Scroll to `common_data`. Right-click it, New
Folder, `bosses`. Right-click the new folder, Paste. Rename to `corsair_queen.amd`.

**Say:** "Don't edit the Warlord. Copy it. || And don't paste it back into the game's own
folder, | because that folder is replaced every time the game is updated. || Yours goes
here instead: | common data, and then a folder called bosses. ||| The Siege reads both
folders, | so a file in either one is a boss in the list. || For the file's name, | use
small letters and underscores, with no spaces. ||"

### 5. Lint it before you change a word

**Screen:** Command prompt: `sbs lint common_data\bosses`. One warning, ending
`duplicate-boss-name`.

**Say:** "Before I change anything, I'm going to run lint, | pointed at my own bosses
folder. || And it already has something to say. || My copy still has the Warlord's name, |
and the list offers bosses by name, | so only one of the two can be in it. ||| It's a true
warning, and it's the first thing we'll fix. ||"

### 6. Rename the boss and the flagship

**Screen:** Edit the heading to `# [Corsair Queen](corsair_queen)`. Edit `Named:` to
`Named: Morrigan kralien_dreadnought`. Briefly type `Iron Duke` as the name, pause on it,
then undo.

**Say:** "The square brackets hold what the crew reads, | and the round brackets hold the
key, | which I make the same as my file's name. || Next is her flagship, | and I'm only
changing the first word, the ship's name. ||| There's one trap here. || A flagship's name
has to be one word. || If I type Iron Duke, as two words, | the game reads a ship called
Iron, | of a kind called Duke, | and there's no such kind of ship. || Lint does catch that
one, | and it shows you the line to write instead. ||"

### 7. Write her words

**Screen:** Replace the description line. Change the quest heading to
`## [Sink the Morrigan](sink_morrigan)`, change the reward to 600, replace the last line.
Replace the `//` notes at the top. Save. Run lint: `clean`.

**Say:** "Now for the part you're here for. || Under the first fence goes one line about
her. || That one's a note for you, and for anyone you give the file to, | because the game
doesn't show it to the crew. || The objective is different, | since the crew does read
that. || So it gets a new name, a new key, | what it pays, and a sentence in your own
voice. ||| Leave the five lines in the middle alone today, | and keep the word credits
after the number, | or nothing gets paid. || Then save, run lint again, | and this time it
says clean. ||"

### 8. See her in the list

**Screen:** Command prompt: `sbs run server,helm,weapons -m LegendaryMissions`. The
server's window on the start screen. The Options panel. Open the Boss line's list. Choose
Corsair Queen.

**Say:** "To see her, I start the game the way you have since Class 1, | but with Legendary
Missions as the mission, | and with no map on the end of the line. || That leaves the
server on the start screen. || Siege is on the left, | and on the right is the Options
panel, with a line called Boss. ||| And there she is, under the game's own four. || If
she's missing for you, | the file's in the wrong folder, | or the game was already running
when you saved it. ||"

### 9. Meet her

**Screen:** VS Code, change `Low: 25%` to `Low: 90%`, save. Start the game again, choose
her, start the mission. Destroy two raiders. The Morrigan arrives. Open the Quest Log.

**Say:** "At twenty-five percent, you'd fight for a long time before she showed up. || So
for testing, I set Low to ninety. || Now she comes when one raider in ten is gone, | which
here is after the second kill. ||| There's the Morrigan, with her two fleets, | and
there's my objective in the Quest Log, in my words. || Notice that nothing announced her. |
The game doesn't tell the crew a boss has arrived, | and we'll do something about that
later in the class. || When you've finished testing, | put Low back to twenty-five. ||"

### 10. Keep it safe, and your turn

**Screen:** File Explorer: `data\missions\common_data\bosses`, with `corsair_queen.amd`
in it, beside the `saves` folder.

**Say:** "This is why she lives out here. || You can update the game, | and this folder is
left alone. || It's still one file on one computer, though, | so keep a copy somewhere
else, | the way you would with a manuscript. ||| And to give her to a friend, you send
them that one file. || Now make a second boss, from your own story. || Next time, we
change the numbers. ||"
