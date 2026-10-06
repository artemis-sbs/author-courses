# C2-9 video script - A Siege boss, part 2

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script, from a probe copy of
> LegendaryMissions).** The finished boss: arrived within 2 s of the raiders thinning,
> Morrigan and Badb with their names as roles, three fleets of one race, `Sink the Morrigan`
> ACTIVE then COMPLETE, "Victory! The starbases held.", 1,100 credits; `mast.runtime.log`
> empty. A misspelled ship key did NOT stop the engine: the ship exists with no hull roles.
> Nothing was looked at on a console.
>
> **Changed since this script was written (LegendaryMissions `abab230`):** a boss with a
> value the game cannot read (`Low: forty percent`, `Fleets: three`, `Difficulty: +two`,
> `Trigger: enemy_low`) is left out of the Boss list with one line in `mast.runtime.log`;
> it no longer stops the game or puts "Could not read this document" in the list. `Low: 40`
> is 40%. Lint names a misspelled trigger. A wrong race is written to the log. And a
> SETTING picks the boss now (`BOSS_SELECT`), so a recording can start with her chosen.
> Step 8 of the page is rewritten; re-cut the scenes that showed the error page.

Target length: 17 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished file is
`example\corsair_queen.amd`.

## Before recording

| Item | State needed |
|---|---|
| `common_data\bosses` | Holds `corsair_queen.amd` exactly as Lecture 8 finished it (`c2-08-siege-boss\example\corsair_queen.amd`), with `Low: 25%`. Nothing else |
| LegendaryMissions | A clean v1.4.0 folder, `e61b415` or later, with the four shipped bosses |
| Library | sbs_utils `98725836` or later, built into `__lib__` |
| Tools | An `sbs` that lints a shared folder (sbs_cli `fd357ee` or later). On 2026-10-04 that is committed and NOT in the downloaded `sbs.pyz`, which warns about every boss field. Every lint result on the page was produced by running the CLI from source |
| VS Code | The `data\missions` folder open, Artemis AMD extension installed, font size raised, `corsair_queen.amd` in one tab |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. It is started and restarted on camera. Siege, Difficulty 5, one player ship |
| A second window | `LegendaryMissions\mast.runtime.log` ready to open in VS Code for scene 10 |
| Takes to prepare | Scene 7 needs two arrivals of different race. Record arrivals until you have one pirate and one Kralien |

## Confirm on camera

Everything below was measured on 2026-10-04 in the mock: real Siege games played headless
from the real LegendaryMissions folder with the packaged library, 91 of them, one boss
file at a time. The boss was chosen by writing the same variable the Boss list writes.
Raiders were taken out of the count by a script. Nobody fired a shot, and **nobody has
seen any of this on a screen.** The engine has not run this lesson at all. The recording
session is that check; if an item fails, stop and fix the page.

1. With `Low: 100%` the boss arrives about four seconds into the game. (Mock: 4.5 seconds,
   three runs. Not run in the engine.)
2. With `Low: 40%` and 20 raiders she arrives at 8 left and not at 9. (Mock: no arrival
   in 7 seconds at 9; arrival 1.5 seconds after the count reached 8. Also measured: 25%
   at 5 and not 6, 90% at 18 and not 19.)
3. `Fleets: 3` brings three fleets; `0` or no line brings none. (Mock: 0, 2, 3, 5 and 6
   fleets counted.)
4. All the fleets of one arrival are one race. (Mock: 62 arrivals with two or more
   fleets, none mixed. In ten arrivals of the finished file, six were pirate and four
   Kralien.)
5. Fleet sizes at level 7: pirate 1 to 3 ships, Kralien 4 to 6. (Mock: seen 1 and 3 for
   pirate; 4, 5 and 6 for Kralien. The page's size table is read from
   `LegendaryMissions\races\*_fleets.yaml` and matched every fleet the runs produced.)
6. `Difficulty: 11` makes every fleet six ships, and `+2` in a game at 11 does the same.
   (Mock.)
7. Morrigan arrives as a `pirate_brigantine` and Badb as a `pirate_strongbow`. (Mock: both
   present with those keys. What either looks like is unseen.)
8. The objective Sink the Morrigan appears on arrival, completes when every raider is
   gone, and pays 600. (Mock: active on arrival; complete at the win; side credits 1,100,
   which is 600 plus the Siege's own 500 for keeping every starbase.)
9. `sbs lint common_data\bosses` prints the three lines the page shows, and prints the
   `unknown-field` warning for `Fleats:`. (Run from CLI source.)
10. With `Flies: 75% Pirates, 25% Kraliens` lint says `clean`, and the two named ships
    arrive with no fleets. (Mock. `mast.runtime.log` stays empty.)
11. With `Fleets: three` the Boss list has no Corsair Queen and has an entry called
    `Could not read this document`. (Mock: that is the list the Siege builds. The list on
    screen is unseen.)
12. With `Low: forty percent` the game stops on an error page four seconds in. (Mock: a
    page-level runtime error at 4 seconds, and game time stopped. The page is unseen.)
13. A misspelled or capitalized ship key still brings a ship named Morrigan. (Mock only.
    What the engine draws for a key it does not have is unknown. Check this one off
    camera first: it may be an empty contact, a placeholder shape, or a crash.)
14. The exercise's wave boss sends one Skaraan ship every 20 seconds, and with **Time
    Limit** 1 the game ends in a win at one minute. (Mock: waves at 23 and 43 seconds,
    victory at 63.)

Not checked at all: how a fleet or a named ship is told apart on Science, Helm or the main
screen; the wording of the Siege setup screen; whether the editor underlines any of the
mistakes in scene 10.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open (0:00 - 0:40)

**Screen:** The game. The Morrigan and the Badb arrive with three pirate fleets. (Reuse
footage from scene 9.)

**Say:** "Last time the Corsair Queen was the Warlord with a new name. She flew a Kralien
dreadnought, with Kralien escorts. This is the same file after today. She arrives when I
say, in the ships I chose, with the fleets I chose. Six lines."

### 2. The six lines (0:40 - 1:30)

**Screen:** VS Code, `corsair_queen.amd`. Highlight the first fence, line by line.

**Say:** "Here is where we left her. Everything today is between `Boss` and the closing
fence. Trigger and Low: when. Flies and Fleets: what comes with her. Difficulty: how big.
Named: her own ships. We will change them one at a time, and play after each."

### 3. The test setting (1:30 - 2:40)

**Screen:** Change `Low: 25%` to `Low: 100%`. Save. Start the game as the server, choose
Siege, choose Corsair Queen in the Boss list, start. She arrives within seconds.

**Say:** "First, make her easy to test. Low is the share of raiders still flying when she
arrives. One hundred percent means all of them, so she arrives at once. Four seconds in,
and there she is. We will put a real number back at the end."

### 4. Trigger (2:40 - 4:10)

**Screen:** Highlight `Trigger: enemies_low`. Open `LegendaryMissions\maps\bosses\continuous.amd`
beside it for a few seconds, then close it.

**Say:** "Trigger has two values. Enemies low: one arrival, when the raiders thin out.
Continuous: no arrival at all, just a new wave every so many seconds, all game. They are
different kinds of boss, and a continuous boss ignores half of this file: no named ship,
no objective, no Low. The page has a table. We stay with enemies low. One warning: if you
misspell this word, the boss never comes, and nothing tells you."

### 5. Low (4:10 - 5:40)

**Screen:** The table from Step 3 of the page, as an overlay or a second tab.

**Say:** "Low is a share of the largest number of raiders the game has seen. With twenty
raiders, twenty-five percent is five left. Forty percent is eight. Always type the
percent sign. Without it, forty means forty times the raiders, and she is there at the
start. And the game looks every four seconds, so she is never exactly on the kill."

### 6. Fleets (5:40 - 7:00)

**Screen:** Change `Fleets: 2` to `Fleets: 3`. Save. Restart the mission. Count three new
fleets.

**Say:** "Fleets is how many escort fleets come with her. A whole number, as a digit.
Zero, or no line at all, and she comes alone. How many ships are in a fleet is not on
this line. That is the next two."

### 7. Flies (7:00 - 9:40)

**Screen:** Change the line to `Flies: 75% Pirate, 25% Kralien`. Save. Restart; show a
pirate arrival. Cut to a second take; show a Kralien arrival.

**Say:** "Flies is who flies the fleets. Six races can: Kralien, Torgoth, Arvonian,
Skaraan, Ximni, Pirate. One race, and every fleet is that race. Or a mix, with a percent
on each and a comma between."

"Here is the part that surprises people. The game rolls once. All three fleets are the
same race. This is a pirate night. This is a Kralien night. You never get two of one and
one of the other. So write the mix as a story: most nights she brings her own corsairs,
and now and then she has hired Kraliens."

"And spell the race in the singular. Pirate, not pirates. We will see why in a minute."

### 8. Difficulty (9:40 - 11:40)

**Screen:** Change `Difficulty: +1` to `Difficulty: +2`. Show the size table from Step 6.
Then briefly type `Difficulty: 11`, save, restart, show fleets of six, and undo.

**Say:** "The crew picks the game's difficulty, one to eleven. Plus two means two levels
above whatever they picked. A bare number means that level, always. The level sets the
size of each fleet. At level seven a pirate fleet is one to three ships. A Kralien fleet
is four to six. At eleven, everything is six. Difficulty does not touch her named ships."

### 9. Named (11:40 - 13:40)

**Screen:** Change the line to `Named: Morrigan pirate_brigantine, Badb pirate_strongbow`.
Show the ship key table from Step 7. Save. Restart. Find both named ships.

**Say:** "Named is her own ships. Name, then ship key. You know the first rule: the name
is one word. The key comes from this table, typed exactly, lowercase with underscores. A
second ship goes after a comma. A corsair queen in a pirate brigantine, and her second in
a strongbow."

### 10. Check it, and what lint cannot see (13:40 - 15:50)

**Screen:** Command prompt: `sbs lint common_data\bosses`. Three lines, `clean`.

**Screen (insert 1):** Change `Fleets:` to `Fleats:`. Lint. Show the warning. Undo.

**Screen (insert 2):** Change the race to `Pirates`. Lint: `clean`. Restart the mission.
The two named ships arrive with no fleets. Undo.

**Say:** "Lint first. Clean. Lint reads the shape of a line. Misspell the label, and it
tells you. But it does not check what comes after the colon. Pirates, plural. Lint says
clean. And in the game, the Queen arrives with no fleets at all, and nothing is written
anywhere. So after lint, play it. The page has the whole list of what lint cannot see.
Two of them stop the game on an error page: a word where Low wants a number, and a word
after the plus sign on Difficulty."

### 11. The real arrival (15:50 - 16:30)

**Screen:** Change `Low: 100%` to `Low: 40%`. Replace the note at the top. Save. Lint.

**Say:** "Testing is over. Forty percent: the crew is winning, and the siege is not over.
And I bring the note up to date, because in a year I will not remember what plus two
meant."

### 12. Your turn (16:30 - 17:00)

**Screen:** The exercise on the page.

**Say:** "Now your own boss. Give it a race that fits its story, its own ships, and an
arrival you chose on purpose. Then make a wave boss in a second file. Next time: the
objective."
