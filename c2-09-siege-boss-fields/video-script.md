# C2-9 video script - A Siege boss, part 2

> **STATE ON 2026-10-08. This replaces every earlier note in this file.**
>
> - Everything the page needs is released, including `sbs lint common_data\bosses`. The
>   page is written for Artemis Cosmos 1.4.0 from Steam or itch.io.
> - **Starts from Lecture 8's finished file** (`c2-08-siege-boss\example\corsair_queen.amd`).
>   `example\` here is that file with this lecture's six lines changed.
> - **Re-measured today.** 109 files: the lesson's steps typed in order, the finished
>   file, the exercise's wave boss, and one change at a time. Each was linted with the
>   installed `sbs`; 108 were played headless, one at a time, in a Siege run from a probe
>   copy of LegendaryMissions with its own `common_data\bosses`. A script
>   (`c2b\verify_page.py`) found every line of tool output on the page in those runs.
> - **What changed on the page since the pilot.** A Siege at difficulty 5 opened with 15 to
>   19 raiders in eight games (the pilot measured 12 to 20), so the table in Step 3 is now
>   worked for 16. `Low: 40` with no percent sign is read as 40%, and the page no longer
>   says otherwise. The game is started with `sbs run`, and the Boss line is in the Options
>   panel.
> - **How a headless game stands in for a crew.** The boss is chosen by the setting the Boss
>   line writes. Raiders are taken out of the Siege's count by the harness, not shot.
> - **Checked in the real engine on 2026-10-04**, by a script, from a probe copy: the
>   arrival, both named ships, three fleets, the objective, the win, 1,100 credits. Not
>   run in the engine again today.
> - **Seen in the real game:** the start screen and its Options panel with the Boss line.
>   Nothing else here has been seen on a screen.
> - The `narration\` folder beside this file was generated from the older script and is
>   stale.

The companion page is `lesson.md`; the finished file is `example\corsair_queen.amd`.

## Before recording

| Item | State needed |
|---|---|
| Boss file | `common_data\bosses\corsair_queen.amd` exactly as Lecture 8's `example\` |
| VS Code | The `data\missions` folder open, the boss file in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scenes 3 and 8, with Difficulty at 5 |
| `mast.runtime.log` | In `LegendaryMissions`, empty or deleted |

## Confirm on camera

"Lint" is the installed tool on that exact file. "Mock" is a headless Siege from the probe
copy, at difficulty 5 unless said. "Engine" is the scripted run of 2026-10-04.

1. With `Low: 100%` she arrives about four seconds in, with nothing destroyed. (Mock: 4.4
   to 4.6 seconds in seven games.)
2. `Fleets: 3` brings three fleets, `Fleets: 1` one, no `Fleets:` line none. (Mock.)
3. With `75% Pirate, 25% Kralien`, all three fleets of one arrival are one race. (Mock:
   seventeen arrivals with that line, never a mix: twelve pirate, five Kralien. That the
   roll is weighted three to one is read from the code, not counted.)
4. At level 7 a pirate fleet is one to three ships and a Kralien fleet four to six.
   (Mock: pirate arrivals of 3+3+1, 3+3+3, 3+1+1; a Kralien arrival of 5+6+5.)
5. `Difficulty: 11` makes every fleet six ships. (Mock.)
6. Two named ships arrive, the Morrigan on a `pirate_brigantine` and the Badb on a
   `pirate_strongbow`. (Mock, Engine.)
7. With the finished file and sixteen raiders she does not arrive at seven left, and does
   at six. (Mock.)
8. Every raider gone: `Victory! The starbases held.` and 1,100 credits. (Mock, Engine.)
9. Every row of the three tables in Step 8. (Lint on each; Mock on each.) The game's own
   line for a value it cannot read was captured from `mast.runtime.log`, for example
   `` `Fleets: two` is not a whole number from 0 up ``.
10. The exercise's wave boss sends one Skaraan ship every 20 seconds, and with a one
    minute time limit the game ends in a win. (Mock.)
11. Unseen, all of it: the arrival on a console, counting fleets on a map, the Quest Log,
    the Time Limit line of the Options panel.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** The game. Two named ships, Morrigan and Badb, among three small pirate fleets.
(Reuse footage from scene 8.)

**Say:** "Last time your boss was a copy of the Warlord with new names. || So she flew a
Kralien dreadnought, with Kralien escorts, | and a corsair shouldn't. ||| Today you change
six lines, one at a time, | and by the end, every number in her file is one you chose. ||"

### 2. The six lines

**Screen:** VS Code, `corsair_queen.amd`. The first fence, between the word Boss and the
closing fence line. Highlight the six lines in turn.

**Say:** "Everything today is in the first fence. || Trigger says which kind of boss she
is. | Low says when she arrives. || Fleets, Flies and Difficulty say what comes with her, |
and Named says which ships carry a name. ||| One thing before we start. || The game reads
a boss file when the mission starts, | so after every change you save, | you start the
mission again. ||"

### 3. Make her arrive at once

**Screen:** Change `Low: 25%` to `Low: 100%`. Save. Start the game, choose her on the Boss
line, start the mission. She arrives within seconds.

**Say:** "You're going to play her several times today, | and you don't want to fight for
ten minutes each time. || So set Low to a hundred percent. || Low is a share of the
raiders, | and she comes when that share or less is left. ||| A hundred percent is all of
them, so she arrives about four seconds in, | before anyone has fired a shot. || That's
your test setting, | and you put the real number back at the end. ||"

### 4. Fleets, and who flies them

**Screen:** Change `Fleets: 2` to `Fleets: 3`. Change the `Flies:` line to
`75% Pirate, 25% Kralien`.

**Say:** "Fleets is the easy one. It's a whole number, written as a digit, | and that many
escort fleets arrive with her. || Flies names a race, | and there are six that can fly a
fleet. ||| Now here's the part people get wrong. || Seventy-five percent pirate, twenty-five
Kralien, with three fleets, | doesn't give you two pirate fleets and one Kralien. || The
game rolls once, when she arrives, | and all three fleets are the same race. || So write
the mix as a story: | most nights she brings her own corsairs, | and now and then she's
hired Kraliens. ||"

### 5. Difficulty

**Screen:** Change `Difficulty: +1` to `Difficulty: +2`. Show the table of fleet sizes on
the page.

**Say:** "The crew picks a difficulty before the game, from one to eleven. || Your line
says how hard her fleets are next to that. || Plus two is two levels above the game, | so
in a game at five, her fleets are built for seven. ||| And the level decides how many
ships are in a fleet. || At seven, a pirate fleet is one to three ships, | and a Kralien
fleet is four to six. || So the night she's hired Kraliens is the hard night. ||"

### 6. Her own ships

**Screen:** Change the `Named:` line to
`Morrigan pirate_brigantine, Badb pirate_strongbow`. Show the table of ship keys.

**Say:** "Named is two words for each ship: | its name, and then which ship it is. || Last
time you changed the first word. | Today you change the second, | and you add a second
ship after a comma. ||| The second word is a ship key, | and the page has the raider ships
in a table. || Type it exactly as it's printed, in small letters, with the underscores, |
because this is the one line where a spelling mistake gets past everything. ||"

### 7. Check it, and what lint can't check

**Screen:** Command prompt: `sbs lint common_data\bosses`. `clean`. Then make the race
plural, `Pirates`, and run lint again: still `clean`. Open `mast.runtime.log` after a game.

**Say:** "Lint reads the shape of a boss line. || It knows the field names, | it knows the
two triggers, | and it knows a named ship is two words. ||| It doesn't check the other
values. || So if I write pirates, with an S, lint still says clean, | and in the game her
named ships arrive with no fleets at all. || The game does tell you, though. | It writes
one line in the runtime log, in the Legendary Missions folder, | naming the race it
couldn't find. || And for a number it can't read, | it leaves your boss out of the list
and says which line. ||"

### 8. Play it, and count

**Screen:** Start the game, Difficulty 5, Corsair Queen on the Boss line, start the
mission. Count the named ships and the fleets on the map. Start again and count again.

**Say:** "Now play it, and count what arrives. || Two named ships, the Morrigan and the
Badb. | Three new fleets, all of one race. || Then start the mission again and look a
second time, | because about one arrival in four is the Kralien one. ||| Try changing one
number and playing again. || Set the difficulty line to eleven, | and every fleet is six
ships. ||"

### 9. Her real arrival

**Screen:** Change `Low: 100%` to `Low: 40%`. Rewrite the note at the top of the file.
Save. Lint: `clean`.

**Say:** "Testing's over, so give her the number you want the crew to play. || I'm using
forty percent. || With sixteen raiders at the start, | she comes when six are left. ||
The crew's winning by then, | but the siege isn't over. ||| Then bring the note at the top
of the file up to date. || It's for you, a year from now, | when you've forgotten why she
flies what she flies. || Next time she gets objectives of her own. ||"
