# C2-10 video script - A Siege boss, part 3

> **STATE ON 2026-10-08. This replaces every earlier note in this file.**
>
> - Everything the page needs is released. The page is written for Artemis Cosmos 1.4.0
>   from Steam or itch.io.
> - **Starts from Lecture 9's finished file** (`c2-09-siege-boss-fields\example\`).
>   `example\` here holds the boss file as this lecture leaves it, and the hook's folder
>   with its one file.
> - **Re-measured today**, in a probe that is a small missions folder of its own: a copy of
>   LegendaryMissions in the shape `sbs fetch` leaves, its own `common_data\bosses`, and a
>   copy of the packaged libraries, so the installed `sbs lint` reads it as it reads a
>   student's. The lesson's thirteen steps were typed in order and linted after each, with
>   a game at each "play it" (11 games). The 92 boss-file variants and the 26 hook-file
>   variants of the pilot were linted and played again, one game at a time.
> - **What changed on the page since the pilot.**
>   - The card is checked with `sbs lint LegendaryMissions`, which now reads the story the
>     way the game does. `sbs compile` is gone from the page. On a copy nobody has touched
>     that command ends `0 error(s), 2 warning(s)`: both warnings are in files that came
>     with the game. The page says so in Step 9.
>   - Five card mistakes that used to need `sbs compile` are now `mast-compile` errors from
>     lint. Three that lint said nothing about are now `unfired-signal`: the short
>     `signal_emit`, a file named `__init__.mast.txt`, and the folder gone.
>   - A `Hook:` that names a label that is not there no longer stops the game. She arrives
>     without her hook and `mast.runtime.log` says so. The exercise and two rows of "If
>     something goes wrong" said the game stops; they are corrected.
> - **The hook's home is still an open decision** (plan item B87). The card lives in a
>   folder inside LegendaryMissions, and an update of LegendaryMissions replaces that
>   whole folder. The page teaches the card and says plainly what an update does: the boss
>   stays in the list, arrives without her hook, her reserve ship never comes, and lint
>   warns that Her Reserve waits for a signal nothing sends (all four measured).
> - **A ship is "sunk" by the harness**, which makes the calls the game's own kill route
>   makes and then removes the ship. The mock's own kill cannot finish a `destroy`
>   objective. A real kill finishing one was seen by script in the engine on 2026-10-04.
> - **Seen in the real game:** the start screen, the Options panel and its Boss line, and
>   the Quest Log on a console. Nothing in this lecture has been seen on a screen.
> - **2026-10-15, for the video:** the narration is regenerated. Scenes 2, 3, 4, 7, 8 and 9
>   show each thing in the game first, on its console (the Quest Log on Helm's handheld,
>   the red line in Helm's ship's log, Science, the end screen), then the
>   line that makes it. The storyboard is `narration\storyboard.py`.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Boss file | `common_data\bosses\corsair_queen.amd` exactly as Lecture 9's `example\` |
| LegendaryMissions | As it comes with the game. No `corsair_queen` folder in it yet |
| VS Code | The `data\missions` folder open, font size raised |
| Command prompt | Open in `data\missions`, cleared, tall enough for the end of a long listing |
| Game | Closed. Difficulty 5 each time it is started |
| A crew for scene 11 | Two people who can sink a brigantine at difficulty 5, or the scene is cut to the arrival |

## Confirm on camera

"Lint" is the installed tool. "Mock" is a headless Siege from the probe copy.

1. Sink the Morrigan with `Done when: destroy 1 morrigan` finishes when she is sunk and
   pays 600 then; the game is won only when every raider is gone, 1,100 in all. (Mock.)
2. The bonus pays 300 and can be skipped: 1,400 with it. (Mock.)
3. With `Fails when: 30 seconds`, `Fatal: true` and `Lose:`, sitting still ends the game
   32 seconds after she arrives, with the `Lose:` sentence and 500 credits. (Mock.)
4. With a `Win:` line the game ends in the same moment the Morrigan is sunk, with that
   sentence. (Mock.)
5. `Hook: biomech_infestation` brings eight BioMechs with her. (Mock.)
6. A folder `corsair_queen` holding `__init__.mast` inside LegendaryMissions is found:
   the story has one more label, and `The Corsair Queen has entered the sector.` is sent
   to the crew's ships in red as she arrives. (Mock.)
7. `sbs lint LegendaryMissions` ends `8 amd + 20 mast file(s): 0 error(s), 2 warning(s)`
   with the card in place and one boss file. (Lint.)
8. The Nemain is on the map ten seconds after the Queen, at 0, 0, 28000, and moving; Her
   Reserve finishes, Sink the Nemain appears. (Mock.)
9. With the real numbers: she arrives at 6 of 16, the Nemain 90 seconds later, and a full
   win pays 1,800. (Mock.)
10. With the folder taken away: she arrives, no sentence, no Nemain, a line in
    `mast.runtime.log`, and `sbs lint common_data\bosses` warns `unfired-signal`. (Mock,
    Lint.)
11. Every row of the four mistake tables. (Lint on each; Mock on each row that says what
    the game does.)
12. Unseen, all of it: New Folder and New File in VS Code, the sentence on a console, the
    Nemain on a map, the Quest Log with her objectives, the game's page of errors. Also the
    objectives' pages: a 3D ship at the top of three of them, and the two icon bullets on
    the Morrigan's (read in the library's text area code only).

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** The game, Helm: the red line "The Corsair Queen has entered the sector." in the
ship's log under the left panel. Then the Quest Log on Helm's handheld with three
objectives. (Reuse footage from scene 11.)

**Say:** "Your boss arrives, and she has the right ships. || But all she asks of the crew
is, destroy everything, | and she says nothing at all. ||| Today she gets objectives of
her own, a way to lose, | and a third ship she's been holding back. || Most of it is
lines you already know, | and one small part is a card. ||"

### 2. How a Siege ends

**Screen:** The game first: the Quest Log on Helm's handheld in a Siege with no boss: Repel the
Siege, Break the Siege, Hold the Starbases, Break It in Time. Then VS Code:
`LegendaryMissions\maps\siege_quests.amd`. Highlight the four headings, then `Parent:
siege_mission` in the student's own file.

**Say:** "First, read how a Siege ends, | because your objectives hang on it. || In the Quest
Log, on Helm's handheld, | a Siege already has quests of its own, before any boss arrives. || And here are the same quests in their file, four of them. || The top one wins the game when it's finished. | Under it is
Break the Siege, which wants every raider gone, | and two more that lose the game. ||| Now
look at your own objective. || It says its parent is that top quest. || So with Required
on it, | it's one more thing the crew has to finish before they can win. | And without
Required, it's a bonus. ||"

### 3. Make it mean what it says

**Screen:** The Quest Log on Helm's handheld, Sink the Morrigan selected (Lecture 9's file). Then
in the second fence, replace the `Done when:` line with `Objective: Destroy the Morrigan`
and `Done when: destroy 1 morrigan`.

**Say:** "Here's my objective in the Quest Log, called Sink the Morrigan, | but it's finished when every
raider is gone. || Let's make it honest, with two lines. || The Objective line is the order
the crew reads in the Quest Log, | and Done when, destroy one morrigan. ||| That last word is
a role, | and the Siege gives every named ship its own name as a role, in small letters. ||
So whatever you wrote on the Named line | is a word you can use here. ||"

### 4. A bonus, and a way to lose

**Screen:** The Quest Log on Helm's handheld: Sink the Badb selected, the Badb drawn in 3D at the
top of its page (the finished file). Then type the Sink the Badb record at the end of the file, its first line the ship:
`[](ship://pirate_strongbow) The Badb, the Queen's second ship`. Then add `Fails when:
30 seconds`, `Fatal: true` and the `Lose:` line to Sink the Morrigan. Play: sit still; the game ends: the end screen with the `Lose:` sentence. The Quest Log: the Morrigan's page, her ship, the order and the two icon lines. Back in the
file: the new objective and the Morrigan's page, with her ship line and the two icon
bullets.

**Say:** "Here's a second objective in the Quest Log, on Helm's handheld, | for her second ship,
with the Badb drawn in 3D at the top. || In the file, it has no Required line, | so it
pays if they do it and it doesn't matter if they don't. || Its description starts with the
ship itself, | the same key as on my Named line, | and the words after it are her caption,
| which the game draws above her. ||| After that comes a clock. || Fails when,
thirty seconds, which is a test number. | Then Fatal, set to true, | and a Lose line, with the
sentence the crew reads when it's over. || Use those three lines together, every time. || And then I play
it and I don't touch anything, | and half a minute after she arrives, | the game ends, | and the end screen has my sentence on it. || Then I set the real limit, ten minutes, | and I say so in the objective, |
because the game doesn't warn the crew as the time runs down. ||| And I give the Morrigan's description a page. || Here's how the crew reads it in the
Quest Log, and then the lines that make it. || Her ship at the top, then the order, | and a short list
where each item starts with an icon. || An hourglass for the ten minutes, | and a skull
for what happens when they run out. || Lint doesn't read icon names, | so copy them from
the list on the page. ||"

### 5. A hook that is already written

**Screen:** In the first fence, add `Hook: biomech_infestation`. Play: BioMechs arrive with her:
Science, the `biomech` chip on, its rows (they read `unknown` until scanned).

**Say:** "Some things no line in a boss file can say, | and a ship that turns up later is
one of them. || For those, a boss has one more line, called Hook. || It names a block of
script, | and the Siege runs that block once, when she arrives. ||| One hook comes with
the game, so try it. || And on Science, the biomech chip lists a swarm of them, | with no script written by me. ||
They aren't her story, though. | So now we write her own. ||"

### 6. Where a hook lives

**Screen:** VS Code file list. Right-click `LegendaryMissions`, New Folder,
`corsair_queen`. Right-click it, New File, `__init__.mast`. Then the page's two-row table.

**Say:** "This is the one awkward thing in the lecture. || Your boss file lives in common
data, where an update never touches it. || But a hook is script, | and script has to be
inside the Legendary Missions folder. ||| So I make a folder of my own in there, | with
one file in it, | named with two underscores, the word init, two more underscores, dot
mast. || I haven't changed any file that came with the game. || But an update replaces
that whole folder, mine included, | so keep a copy of it somewhere else. ||"

### 7. The smallest hook

**Screen:** The game first: Helm, the red line in the ship's log (from scene 11). Then paste the
seven-line card. Change the `Hook:` line in the boss file to
`corsair_queen_hook`. Command prompt: `sbs lint common_data\bosses`, then `sbs lint
LegendaryMissions`. Point at `0 error(s), 2 warning(s)`.

**Say:** "Here's what we're making first: | a red line on Helm, under the panel on the left,
| as she arrives. || And here's the smallest hook there is. || A label, which is three equals signs and a
name. | One line that says a sentence to every crew ship. | And the line that ends it. ||
Then the boss file names that label, letter for letter. ||| Now there are two things to
check, so there are two commands. || The first reads my boss file, as always. || The
second reads all of Legendary Missions, my card included, | the way the game will. || Read the last line it prints, | and you want it to say zero errors. || The two warnings are in files that came with the
game, | so they're not yours and you leave them alone. ||"

### 8. Hold a ship in reserve

**Screen:** The game first: Science, the Nemain selected on the map (from scene 11). Then add the
four lines to the card: the wait, the guard, the long ship line, the
signal. Highlight the four things to change on the ship line.

**Say:** "Next comes a third ship of hers: | ten seconds after the Queen, | the Nemain arrives, here on
Science. || To make her, the card grows by four lines. || A wait, which is one of your cards from
Class 1. | A line that stops if the game's already over. | One long line that brings in
a named ship. | And your finish a step card, which sends a signal. ||| On the ship line
you change four things and nothing else: | where she appears, her name, which ship she
is, | and her name again in small letters, which is her role. ||"

### 9. The objectives the hook drives

**Screen:** The Quest Log on Helm's handheld: Her Reserve done, Sink the Nemain new (from scene
11). Then type Her Reserve and Sink the Nemain at the end of the boss file. Highlight
`Then: reveal sink_nemain` and `Starts when: revealed`.

**Say:** "A signal finishes a step, and a step can reveal another. | That's the chain from
Class 1. || So in the Quest Log, Her Reserve waits for the signal, | and when it's done, Sink the Nemain
appears in the list. ||| Two things here catch people. || In a boss file, the address after reveal is
the key alone, with no slash. || And the hidden step says, starts when revealed, | and
does not also say, state active. ||"

### 10. Check it

**Screen:** Both lint commands. Then put a mistake in the card (delete a quote mark) and
run `sbs lint LegendaryMissions`: the `mast-compile` error. Undo.

**Say:** "Run both of them again. || And look at what a mistake in the card costs you. || I'll take
out one quote mark. || Lint gives me an error that ends, mast compile, | with the file and
the line. ||| If I played that, nothing in Legendary Missions would run. | No Siege, and
no other map either. || Your Class 1 cards were in your own mission. | This one's inside
the game's, | so run that second command every time you touch it. ||"

### 11. Play it

**Screen:** Start the game, Difficulty 5, Corsair Queen, start the mission. Helm: the red
sentence. The Quest Log on Helm's handheld: three objectives; Sink the Morrigan's page.
Ten seconds later, Science: the Nemain, selected on the map. The Quest Log: Sink the Nemain.

**Say:** "And now she arrives and says so, | in red, on Helm. || On Helm's
handheld, three objectives are in the Quest Log, | and
the fourth isn't there yet. || When I open Sink the Morrigan, | there's her ship, the clock,
and what it costs. || Ten seconds later, there's the Nemain on Science, | Her Reserve is done, and the fourth one appears. ||| Then put the real numbers back: | forty percent, ten minutes, and ninety seconds on the card. ||"

### 12. Keep it safe

**Screen:** VS Code's file list: the boss file in `common_data\bosses`, then the card in
`LegendaryMissions\corsair_queen`. Then the command prompt: with the folder gone, `sbs lint
common_data\bosses` warns `unfired-signal`.

**Say:** "Your boss is now two things in two places. || The file is safe from an update, and the folder isn't. || After an update she's still in the list, | and she arrives
without her hook: | no sentence, and no reserve ship. ||| Lint tells you about it, too. | It warns
that Her Reserve is waiting for a signal nothing sends. || So keep a copy of that folder, |
and put it back after every update. || Next time is the last lecture of the class, | and
she gets a voice. ||"
