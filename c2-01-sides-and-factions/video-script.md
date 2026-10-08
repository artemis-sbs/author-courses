# C2-1 video script - Sides and factions

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyMission`** as Class 1 left it: the finished files of
>   Lecture 11 (`c1-11-just-enough-mast\example\`, two files) with the other five files
>   `sbs create MyMission -t amd` made. The game is started with
>   `sbs run server,helm,science,comms -m MyMission map=0`.
> - **The card is gone.** The first version of this lecture pasted one line into
>   `story.mast` to read a Sides section. The template has that line now (line 44 of the
>   Class 1 file), so the lecture only reads it. The one edit to `story.mast` left is a
>   word: `home` on the DS 1 line.
> - **`example\` holds the two files that differ from the start:** `mission.amd` and
>   `story.mast`.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were applied
> one at a time to the Lecture 11 example, with lint after each. Then 74 one-change
> variants of the finished files: each linted, each played headless by a probe that asks
> the game's own functions what a thing is to the crew, what the Science title would draw,
> what Comms is offered, and what Helm is offered to dock with. Every line of tool output
> printed on the page is a line a run printed (`verify_page.py` in the harness folder).
> Since the first version lint has learned the side key: a `Side:`, `Enemies:` or
> `Allies:` word that names no side is `dangling-side`, and the game writes `Side not
> found` to `mast.runtime.log`.

> **SEEN IN THE REAL ENGINE, 2026-10-04, with real Helm, Science and Comms** (on the first
> version of these files; the three sides, the two landmarks and their relations have not
> changed). On Science the hostile cutter is drawn RED and its panel reads "Breaker Cutter
> (breaker)", with side chips `tsn`, `breaker`, `guild`. On Helm the allied yard is BLUE
> like DS 1, and the crew's ship is green. So the map colors a contact by its RELATION to
> the crew, not by the side's `Color:`. The engine's own `intel` text for the cutter reads
> "The captain cannot be taunted pirate." The probe's report matched the mock: the yard's
> stock scan and its three Comms buttons, docking offered at the yard, the cutter's enemy
> scan and Hail / Taunt / Surrender now, nothing moved or fired in 30 seconds. Not seen:
> the side's color anywhere but the side word, docking carried through, a bad `Color:`.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 11 leaves it. `story.mast` must match `c1-11-just-enough-mast\example\story.mast` line for line (115 lines), or lines 18 to 20, 44, 64, 68 and 113 on the page are wrong. `mission.amd` has 185 lines and ends with The Lifeboat |
| Lint | `sbs lint MyMission` says `clean` |
| VS Code | `MyMission` folder open, `mission.amd` in one tab scrolled to the end, `story.mast` in another at line 18. The status bar (`Ln`, `Col`) in shot |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm, a Science and a Comms console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. "Engine" is the run of 2026-10-04 in the note above. If an item fails while
recording, stop and fix the page.

On the lesson's steps, typed in order:

1. Lint is `clean` after Step 2, Step 3 and Step 4. Half way through Step 5, with the step
   changed and DS 1 not yet wearing `home`, lint prints the `role-nothing-wears` line on
   the page, with `line 105`. After the word is added it is `clean`, and it stays `clean`
   through Steps 6 and 7. (Lint.)

On the finished files:

2. Three sides exist with the names, keys and colors in the file. TSN and the Breakers are
   hostile, TSN and the Guild are allied, the Breakers and the Guild are hostile. One
   `Enemies:` line sets the relation both ways. (Mock, Engine.)
3. The two functions that build the Science title return, for the cutter, the name in a
   red and the word `breaker` in `#F80`. For the yard: the name in green and `guild` in
   `#0C6`. For DS 1 and the hulk: green, and `tsn` in `#07F`. For a contact that is
   `unknown`: that word in grey, and no side word. (Mock. Engine: the red, the word.)
4. A forced scan of the cutter stores "Enemy vessel. Exercise caution." on `scan`. A
   forced scan of the yard stores "This is a friendly station." (Mock, Engine.)
5. Comms selecting the cutter is sent Hail, Taunt, Surrender now. Hail is answered "Go
   away, Artemis! You talk too much!". Comms selecting the yard is sent Hail, Build
   Weapons, Request Priority Docking. Hail is answered "Hello, Artemis. We stand ready to
   assist", the shield and hull figures, and "You have full docking privileges." (Mock,
   Engine.)
6. 400 from the yard the ship is offered the yard to dock with. 400 from the cutter
   nothing is offered. A dock request at DS 1 is accepted with the cutter far away and
   refused with the cutter 500 from the station. (Mock.)
7. After 20 seconds 400 from the cutter: the cutter has not moved, no shield value has
   changed, and no ship has a weapon target. (Mock. Engine: 30 seconds.)
8. The whole story: hulk, lifeboat, tug (300 credits with the bonus), then the yard: Bring
   the Log Home stays running. Then DS 1: the game ends with the `Win:` sentence. (Mock.)
9. Every row of the three tables in Step 8. (Lint for all, Mock for all.)
10. The exercise, step by step: a stranger with no scan record is `unknown`; with one, its
    name is white; as an enemy it is red and reads the game's text; as an ally it is green
    and reads the writer's. (Mock.)

Not seen by anyone, and to watch for while recording:

1. **Scanning.** Whether the ship's sensors read the cutter and the yard by themselves in
   range. Class 1 saw the engine scan the hulk by itself. The mock never does.
2. **The Science title** for the yard: green, with `guild` beside it. The engine run saw
   the cutter's.
3. **Docking at the Guild Yard** with Helm's own control, start to finish, and the words
   of the refusal when an enemy is close.
4. **A color that is not one** (`burnt orange`, `#F8`). The words go to the engine as
   typed. Nobody knows what it draws.
5. **A stranger with scan text**, drawn in white (the exercise, step 4).
6. Everything in VS Code.

Known, and kept out of the lesson on purpose:

- An allied SHIP gets no ready-made scan text. Only a station does. So the lesson's friend
  is a station, and the exercise adds a scan record.
- `players` and `civilians` in a relation line.
- `Done when: reach breaker 2000` works in the game (a side's key is also a role) and lint
  calls it a role nothing wears.
- The TSN record is not needed for the game to work: lines 18 to 20 of `story.mast` make
  the side. The page says so, and keeps the record so all three sides are in one place.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The Science console. Select the Breaker Cutter: its name in red, `breaker`
beside it, "Enemy vessel. Exercise caution." Select the Guild Yard: green, `guild`,
"This is a friendly station." Cut to Helm docking at the yard.

**Say:** "In Class 1, everything on your map was on one side, and it was yours. || Today
the map gets politics. || These people want your hulk, | and these people will fix your
ship. ||| That's three short records in your file, | and one line that says who is whose
enemy. ||"

### 2. The side you already have

**Screen:** `story.mast`, lines 18 to 20 highlighted. Then line 64, line 68 and line 113:
highlight the first word inside the quote marks each time. Then line 44.

**Say:** "You read these three lines in Lecture 11. || They make a side called t s n, | and
they give it a name and a color. || Now look where else that word turns up. || It's on the
line for DS 1, | it's on the line for the hulk, | and it's on your tug. ||| Inside the
quote marks, the first word is the side, | and the words after it are roles. || So t s n
is the key of your own side. | Hold on to that word. ||| One more line, further down. ||
In Lecture 11 this one was marked for Class 2. || It reads a section called sides from
your fact sheet, | and you haven't written one yet. ||"

### 3. A Sides section

**Screen:** `mission.amd`, the end of the file. Two blank lines. Type the note, the
section line, the TSN record. Point at the key. Show the color table on the page.
Command prompt: `sbs lint MyMission`, clean.

**Say:** "So let's write one. || Sides are records, like everything else in this file. ||
The section is two hashes, the word Sides, | and a key that has to be exactly that word,
in small letters. || Then one record for each side: | three hashes, a name, and a key. |||
My own side goes first, | and its key is t s n, | because that's the word my ship already
carries. || Then a color, which is a hash sign and three characters, | for red, green and
blue. || Zero means none of it, and F means all of it. || I save, I run lint, and it's
clean. ||"

### 4. Two more sides

**Screen:** Below the TSN record, type The Breakers, then Harbor Guild. Highlight
`Enemies: tsn`, then `Allies: tsn`. Save. Lint: clean.

**Say:** "Now the people who aren't me. || First the Breakers, with the key breaker, in
orange. || And here's the line that matters: | Enemies, and then my key. ||| Then the
Harbor Guild, with the key guild, in green, | and the line Allies, and my key. || What
comes after the colon is always a key, never a name. || And I only say it once. || Enemies
on the Breakers makes them my enemy, | and it makes me theirs. | I don't go back and write
it on my own record. ||"

### 5. Something on each side

**Screen:** Scroll up to the Landmarks section. Below The Lifeboat, above the Sides note,
type the Breaker Cutter and the Guild Yard. Highlight the two `Side:` lines. Lint: clean.

**Say:** "A side with nothing on it is just a name in a file. || So I give each of them
one thing on the map, | and I do it with landmarks, the way you did in Lecture 10. || A
ship for the Breakers, out past the hulk, | and a station for the Guild, west of DS 1. ||
The Side line takes the side's key. ||| Now watch where I'm typing. || These two go in the
Landmarks section, | above the Sides heading. || If I type a landmark below that heading,
| the game reads it as a side called Breaker Cutter, | and it puts no ship anywhere. ||"

### 6. A second station

**Screen:** The step Bring the Log Home, `Done when: reach station 1000` highlighted.
Change it to `reach home 1000`. Save. Lint: the `role-nothing-wears` warning. `story.mast`,
line 64: add `, home` inside the quote marks. Save. Lint: clean.

**Say:** "Lecture 10 warned you about this next part. || My story ends with the words
reach station. || Station is a role, and every station wears it, | and I've just built a
second station. || So the crew could carry the log to the Guild, and win. ||| The cure is
a role that only DS 1 wears. || In the step, I write reach home. || Lint says nothing
wears a role called home, | which is true, because I'm only half done. || So I go to line
sixty-four, where DS 1 is made. || Inside the quote marks, after station, | I type a
comma, a space, and the word home. || The side stays first, and the roles follow it. ||
And now lint is clean. ||"

### 7. Who is what to whom

**Screen:** The three-pair table on the page. Then change the Breakers' line to
`Enemies: tsn, guild`. Then the table "What a relation does in the game".

**Say:** "Three sides make three pairs. || Me and the Breakers are enemies, | and me and
the Guild are allies. || But about the Breakers and the Guild, nobody said a word. ||| And a pair
nobody mentions is nothing to each other. | The game doesn't guess. || Scavengers and
harbor pilots aren't strangers, | so I add the Guild's key after mine, with a comma
between. ||| So what does a relation buy you? || An enemy reads as an enemy on Science, |
and Comms can taunt it. || A friendly station lets you dock. || And here's the one thing
it doesn't buy you: a fight. || The cutter has no orders, so it'll just sit there. ||"

### 8. Lint, and what lint cannot see

**Screen:** Command prompt. In the Breakers, change `Enemies: tsn, guild` to
`Enemies: tsm`: lint, `dangling-side`. Undo. Take the `Side:` line off the cutter: lint,
clean. Undo. Then give Harbor Guild a fourth hash: lint, clean. Undo. Show the table
"What lint cannot see" on the page.

**Say:** "Now let's break it on purpose. || I misspell my own key after Enemies, | and
lint catches it. || It says that word isn't a side in this mission, | and it lists the
keys I did declare. ||| But watch this one. || I take the Side line off the cutter
altogether, | and lint says clean. || And a fourth hash on the Guild's heading is clean as
well. ||| In the game, those two look the same. || The thing reads as unknown on Science,
for good, | and Comms has nothing to say to it. || So when a contact stays unknown, | look
for its Side line first, | and then count the hashes on its side. ||"

### 9. Play it

**Screen:** Server, Helm, Science and Comms. Science: select the Guild Yard, wait for the
scan. Comms: select it, press Hail. Helm: fly inside 600 and dock. Undock. Fly past the
hulk. Science: select the Breaker Cutter. Comms: select it, press Hail. Hold near the
cutter for ten seconds. Then cut to the end of the story: Bring the Log Home showing, the
ship at the Guild Yard, nothing; the ship at DS 1, the win.

**Say:** "Here's the yard on Science. || It's unknown until the scan is done, | and then
it's green, with the word guild beside it. || On Comms I hail them, | and they tell me I
have full docking privileges. || And Helm can dock. ||| Now the other one. || It's red,
with the word breaker beside it, | and it reads enemy vessel, exercise caution. || I hail
it, and it tells me to go away. || And then it just sits there, | because being enemies
doesn't start a fight. ||| One last thing: I carry the log to the yard, and nothing
happens. || I carry it to DS 1, and we're home. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: write a faction of your own, with one ship. || Say nothing
about it, and Science calls it unknown. || Give it a scan record, and it has a name. ||
Then make it an enemy, and then a friend, | and watch the name change color. ||| Next
time, we meet the people who fly these ships. ||"
