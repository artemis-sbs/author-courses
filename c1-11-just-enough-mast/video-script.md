# C1-11 video script - Just enough MAST

> **STATE ON 2026-10-05. Read this first; where an older note below disagrees, this is
> newer.**
>
> - **Everything this page needs is released.** The tool is `sbs` 0.12 (`sbs version`
>   says so, and `sbs update` fetches it), the library is the published v1.4.0, the VS
>   Code add-on is 0.9.4. Notes below that call the tool unreleased, say it prints
>   `0.10`, or name a build such as `f28e7f1` are history: read "`sbs` 0.12 or later".
> - **The page is written for Artemis Cosmos 1.4.0, installed from Steam or itch.io**
>   (the course owner's decision). Record on such an install, on a clean Windows
>   account, not on a developer's machine.
> - **The student's mission is `MyMission`**, made in Lecture 3 with `sbs create`, its
>   libraries brought up to date there with `sbs fetch "MyMission" --update-libs`, and
>   the game is started with `sbs run server,helm,science -m MyMission map=0` (seen
>   working in the real game: three windows, the map starts with no click).
> - **Seen in the real game since this page was measured:** the Quest Log is reached by
>   the handheld icon in a console's top bar, then Quests; selecting an arc shows its
>   description and open steps; selecting a step shows State, then an `Objective:` the
>   writer typed, then the description; a writer's sentence is drawn as typed.
> - **Lecture numbers:** 3 is "Your editor and your first run", 4 is "Markdown in twenty
>   minutes". An older note that has them the other way round predates the exchange.

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only).** The finished mission won:
> the step started, the tug arrived 20 seconds later and stayed where it was put, the way
> home was revealed, 500 credits. In the engine the hulk is scanned on arrival, so First
> Contact finishes by itself. A broken indent shows the "Mast Compiler Errors" page with
> the line and two buttons (seen). A line that fails mid-game shows the runtime error page
> (seen; its text was drawn over the engine's bar, fixed in sbs_utils `ab17f6be`). A card
> pasted into the map's lines gives a game with no station and no hulk, and no message. A
> misspelled `Art` word did not stop the engine. A curly quote in a `#` note used to stop
> the file loading; the library now reads the file as UTF-8 (`175ad4c9`) and it loads,
> in the engine too. Items 3, 4 and 5 of the not-seen list below are therefore answered.
>
> That run used the first version of this lesson's files: the template of that day plus
> Lecture 10's arc. The card it pasted is the card on the page today, word for word.

> **Re-measured 2026-10-04 (night, into the small hours of the 5th). Not run in the engine
> again.**
>
> - Library: the packaged one in `__lib__`, built at 21:16 from sbs_utils `2c7d93d1` and
>   LegendaryMissions `b20726f`. Every mock run used it. Lint reads the sbs_utils working
>   tree, which was at `8d79be5f` for the whole pass: three commits ahead of `2c7d93d1`,
>   all documentation, no library code. Starter template `60c30bc`, which is what
>   `sbs create -t amd` downloads now (the probe mission was made with it).
> - **The lesson now starts from Lecture 10's finished files**, read from
>   `c1-10-things-quests-point-at\example\` (both files), not from the untouched template.
>   So `story.mast` is 105 lines, not 100 (the template gained a Sides line, and every
>   number in Step 1's tables moved); the hulk wears `ghost_ship`; the signal on line 93
>   is Lecture 7's `ghost_ship_found`; and the student's word list at the top of
>   `mission.amd` gets two lines, typed at the end of Step 7. `example\` here is those two
>   files with this lecture's steps typed in.
> - 146 variants: Lecture 10's files untouched, each step in turn, the finished files, and
>   one change to the finished files at a time. Each was linted with the installed
>   `sbs.pyz` (164 lint runs, 11 of them a second time in a plain environment: see the
>   tool note), compiled with `sbs compile` (161 runs, to see whether it still says
>   anything lint does not: it does not), and played headless with the packaged library,
>   one at a time (147 mock runs, five of which ended a game).
> - Every line of tool output printed in a code block on the page was checked against
>   those runs by a script (`c111r\verify_page.py`): 16 lines, all found. Every row of the
>   Step 8 tables is tied to the runs that measured it by a second script
>   (`c111r\rows.py`): 67 rows, 122 variants, 260 tests on the probe's own lines. The codes
>   in a row are the codes lint printed, and a row under "What lint cannot see" or "These
>   are fine" was `clean` in every one of its runs. The 25 "begins with" rows of Step 1
>   are checked against the finished `story.mast` by the first script.
> - What changed against the page of 2026-10-03. **One check, not two.** Lint compiles the
>   story now, so Step 3 teaches that lint reads both files, and `sbs compile` is one
>   sentence. The Step 8 tables are rebuilt as mistake, game, code. Rows that said `clean`
>   under lint and now have a code: every compile error (`mast-compile`, with the line), a
>   line under `->END` and a card pasted inside a block (`mast-unreachable`), and every
>   slip with the signal's name, the short `signal_emit("tug_arrived")` and a misspelled
>   `"quest_signal"` included (`unfired-signal`). `"signal_name"` in small letters is no
>   longer an error page: the step stays open and the log gets one line. A `{word}` in the
>   map's description no longer breaks the start screen. The paragraph about a line number
>   being one too low after `Unrecognized syntax` is gone: it is right now. "Three tugs"
>   is four (measured over a longer play). The 450-credit ending is a run now, not
>   arithmetic.

> **Tool note.** The page needs an `sbs.pyz` built from sbs_cli `f26f3ff` or later. The one
> installed here is that build (file time 22:43; its `lint_cmd.py` is `f26f3ff`'s). It
> still prints version `0.10`, the same as the released one; a release as `0.11` is
> pending. The sbs_cli source moved to `d775752` while this pass ran and was not built, so
> nothing here was measured with it. With the released `0.10` this page is wrong from Step
> 3 on: that tool's lint does not compile the story, so every `mast-compile` row would read
> `clean`, and it empties both logs each time it runs. (From the first measurement of this
> lesson, on 2026-10-03, and from the list of fixes. Not measured again.)
>
> One thing about the tool that the page depends on. Lint compiles the story in a second
> process and reads what that process prints. When the environment variable
> `PYTHONIOENCODING=utf-8` is set (this pass's harness set it at first; a recording setup
> might), a compile error whose text holds a character that is not plain ASCII comes back
> as `[ERROR] line 1: the compile failed`, with no line and no reason. In a plain command
> prompt the same mistake prints the real line and `invalid character`. The curly-quote
> row of the page is from the plain environment. Record in a plain command prompt.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 10 leaves it, lint clean. Both files must match `c1-10-things-quests-point-at\example\` line for line, or the line numbers on the page are wrong: `story.mast` 105 lines, line 35 begins `    shared MISSION_DOC =`, line 54 is the `landmarks_spawn` line, line 93 says `ghost_ship_found`, line 105 is the last `->END`; `mission.amd` 170 lines |
| Files touched | `mission.amd` (one line changed, one step added, two lines in the word list) and `story.mast` (lines 25 and 26 changed, eight lines pasted at the end) |
| Library | sbs_utils `2c7d93d1` or later and LegendaryMissions `b20726f` or later, BUILT into `data\missions\__lib__` |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` folder open, `mission.amd` and `story.mast` in two tabs, line numbers showing, font size raised. Turn on View, Render Whitespace for scenes 5 and 11, so the indent can be seen |
| Command prompt | A plain one, open in `data\missions`, cleared, wide enough that one finding fits on three lines |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 7 for ten seconds, and in scene 12 with a server and a Helm console |

## Confirm on camera

What was checked, and how. "Lint" means the installed `sbs.pyz`, run from `data\missions`
on a copy of the files with that one change. "Mock" means the mission was then played
headless with the packaged library, and a probe put the ship 300 from the hulk, then 300
from the lifeboat, waited 24 seconds, and (for the finished files) put it 600 from DS 1.
It printed every object, every quest's state, the Quest Log's rows, the side's credits,
and each quest signal with the game time it was said. "Engine" is the run of 2026-10-04
in the note above. Nobody has SEEN any of this lesson on a screen except the two error
pages. If an item fails while recording, stop and fix the page.

On Lecture 10's files, before a line is typed:

1. Lint is `clean`. The map is named `AMD Sample`. (Lint, Mock.)

On the lesson's steps, typed in order:

2. After Step 2 the map's name is `Salvage Run` and its description is the new sentence.
   Lint is `clean`. (Lint, Mock.)
3. Step 3's break, the closing quote mark of line 25 deleted: lint prints the block on the
   page, word for word. `sbs compile` prints the same error as three lines and
   `FAILED: 1 compile error(s)`, and prints nothing for a good file. Played, nothing
   runs: no label of the story executes. (Lint, Mock.)
4. After Step 4 lint prints the `unfired-signal` line on the page, word for word, with
   `line 90:19`. After Step 5 it prints the same line. After Steps 6 and 7, and after
   the two word-list lines, it is `clean`. (Lint.)
5. After Step 5 alone, the tug appears as the step starts and the step stays open. After
   Step 6, the tug and the signal come in the same moment as the step starts. (Mock.)
6. Following the page's steps in order, typing each block as printed, gives
   `example\mission.amd` and `example\story.mast` byte for byte. (A script,
   `c111r\steps.py`.)

On the finished files:

7. At the start Salvage Run, Close Inspection and Quick Work are active. Wait for the Tug
   and the two steps round it are hidden. The Quest Log call returns Salvage Run with
   Close Inspection and Quick Work under it. (Mock.)
8. 300 from the lifeboat, Find the Lifeboat completes and Wait for the Tug starts. No
   object wears `tug` then, or ten seconds later. The signal `tug_arrived` is said 20.0
   seconds after the step started (20.0 to 20.2 over the 33 runs that play as the
   finished files do). Bring the Log Home starts in the same moment. (Mock, Engine.)
9. The tug: named Salvage Tug, at 5600, 0, 6000, 400 from the lifeboat, art `cargo_ship`,
   side `tsn`, wearing `tug`. It was still there 17 seconds after it arrived. (Mock,
   Engine.)
10. 600 from DS 1 the game ends carrying the `Win:` sentence, with 500 credits, and both
    logs are empty. (Mock, Engine.) With nobody near the hulk for the first two minutes,
    Quick Work fails and the game is won with 450. (Mock.)
11. `example\`, copied into a fresh mission as delivered: lint `clean`, and the same play.
    The same two files saved with Windows line endings: the same. (Lint, Mock.)
12. Step 8's break, the `signal_emit` line moved below `->END`: lint prints the block on
    the page, word for word; the tug arrives and the step never finishes. (Lint, Mock.)
13. The exercise: a second card on `quest_succeeded` for `salvage/approach` put a ship at
    600, 0, 9000 as Close Inspection completed, the first card's wait changed to 12 took
    12.0 seconds, and the game was still won with 500. (Lint, Mock.)
14. The other two words on Card 1: with Quick Work's limit cut to ten seconds, a card on
    `quest_failed_done` for `salvage/quick` ran when it failed. A card on
    `quest_succeeded` for `salvage/tug` ran when the tug's step finished. (Mock.)
15. The finished files with the exercises of Lectures 5, 7, 8 and 9 typed in: lint
    `clean`, and the two-minute quest of Lecture 8's exercise pays on top. Played two
    minutes late, the game was won with 475: the 450 and that quest's 25. (Lint, Mock.)
16. Every row of the tables in Step 8. (Lint, Mock, each row.)

Not seen, and to watch for while recording:

1. Any screen of the finished mission: the Quest Log with Wait for the Tug in it, the tug
   on Helm's map, what the `cargo_ship` art looks like. The rows the Quest Log is given
   were read in the mock; the screen was not.
2. The server's start screen with the map's name and description. The page's last
   paragraph of Step 9 sends the student there by leaving `map=0` off the `sbs run` line.
   From the mock: the map label carries the name and the sentence. Nobody has seen the
   screen, and the page does not say what to click on it. If it needs a click to go on,
   say so on camera and add it to the page.
3. The "Mast Compiler Errors" page for Step 3's break (a quote mark). It was seen for a
   broken indent. Show it in scene 7 and say what is really there. If the Attempt Rerun
   button works after the fix, say so on camera and add it to the page: it was not tried.
4. `//signal/` in place of `//shared/signal/` with consoles connected. Lint warns; the
   run had no console, and there it plays the same.
5. A long dash in the map's name. Lint is clean and the mock carries the dash in the
   name. A ship's name is folded to plain marks by the library (measured for the tug);
   a map's name is not. Nobody has looked at what the engine draws.
6. A misspelled `Art` word. The mock places the ship under that word. The engine did not
   stop (2026-10-04). Nobody has looked at what it draws.
7. What an error page looks like for each row of the second "cannot see" table. The mock
   stops the story and writes `mast.runtime.log`, which names the line (measured for all
   seven mistakes). One such page was seen in the engine.
8. Whether ten minutes is still enough. The trip was already long in Lecture 10 and this
   adds twenty seconds.

## Scenes

### 1. Cold open

**Screen:** The game. Helm's map at the lifeboat. The Quest Log shows Wait for the Tug.
The tug appears. The step shows Done.

**Say:** "That ship wasn't on the map when the game started, | and nothing in your fact
sheet can do that. || So today you open the other file, the script. || You'll read it once,
from top to bottom, | and then paste three small cards into it. || And you won't write a
line of code. |||"

### 2. Two files, two sets of marks

**Screen:** `mission.amd` and `story.mast` side by side. Highlight a `#` heading and a
`//` note in the first, a `#` note and the `//science` line in the second.

**Say:** "First, a reminder from Lecture 7. || In your fact sheet, a hash is a heading, |
and two slashes are a note. || In the script, it's the other way round. || A hash is a note,
| and two slashes start a route, | which is a block that runs when something happens. || So
a note of your own, in this file, starts with a hash. ||| You also had three rules for this
file: | change only what's between the quote marks, | never touch a quote mark itself, | and
leave the commas alone. || Today, you go a little further. ||"

### 3. Read the file: the top

**Screen:** `story.mast`, lines 1 to 30. Point at each block in turn.

**Say:** "At the top there's a note. || Then a named box, which is empty for now, | and the
word shared means every block in the file can see it. || Next, a line that reads a crew
roster, which is for Class 3. || Then three lines that make your side, | and one for the
music. || And here, at the left edge, is the map. || This is a label, which means a named
block, | and everything indented under it runs once, when the game starts. ||"

### 4. Read the file: the lines that read your file

**Screen:** Lines 31 to 79. Highlight line 35, then 54, 56 and 57, with the word in quotes
on each. Switch to `mission.amd` and show `## [Landmarks](landmarks)`. Back. Then lines
64, 68, 78 and 79.

**Say:** "Line thirty-five reads your whole fact sheet, and fills the box. || After that,
each section is handed to the thing that knows what to do with it: | landmarks, quests, and
scans. || Now look at the word in quotes: landmarks. || That's the key in your section
heading. || Last time, I said it had to be exactly that word, | and this line is why. |||
The lines for sides, for a cast, for conversations and for ruins | do nothing until your
file has those sections. || Then comes the station, and then the hulk, | where you added
ghost ship to this line yourself, back in Lecture 7. || And the last line is arrow, END, |
which says this block is finished. ||"

### 5. Read the file: the indent, and the two blocks at the bottom

**Screen:** Render Whitespace on. Show the four dots in front of each map line. Scroll to
`=== watch_for_arrival` and `//science`. Highlight lines 93 and 104. Switch to
`mission.amd`: `Done when: signal ghost_ship_found`.

**Say:** "There are three things to know, and that's all the theory. || The first is the
indent: | it's four spaces, and the lines of a block line up. || The second is arrow END: |
the block is done, and nothing under it runs. || And the third is these two blocks, which
you already know. || Each one ends by saying a name. || This one says ghost ship found, |
which is your word, from Lecture 7. ||| And the step in your fact sheet says, | done when,
signal, ghost ship found. || So that step isn't finished by reach. | It's finished by the
script, by name. || You'll paste that same line in a few minutes, | and decide for yourself
when it's said. ||"

### 6. Your first edit

**Screen:** Line 25: change `AMD Sample` to `Salvage Run`. Line 26: change the sentence.
Point at the single quote mark. Save.

**Say:** "Your mission has a title, from Lecture 3, | but the map inside it is still called
AMD Sample. || So change the words between the quotes. || The line under it is the
description. || It has one quote mark, at the start, and none at the end, | and that's how
it's meant to be. || Just keep it on one line. ||"

### 7. One check, two files

**Screen:** Command prompt. `sbs lint MyMission`: clean. Point at `1 mast` in the count
line. Delete the closing quote on line 25, save, lint again: the error under
`== story.mast (compile) ==`. Start the game with the broken file for ten seconds. Close
it. Put the quote back. Lint: clean.

**Say:** "It's one command, as always. || Look at the last line: one AMD, and one mast. ||
Lint has been reading the script every time, | it's just never had anything to say. ||| So
now I break it, by taking out one quote mark. || Lint says story dot mast, compile, line
twenty-five, | and it can't read that line. || And its last sentence says | nothing in this
mission runs until this is fixed. || Here's the game with that file: | a page headed Mast
Compiler Errors, and nothing else. || Nothing of mine is running, | and that's from one
character. || So, run lint after every change to this file. ||"

### 8. A step that waits for the script

**Screen:** `mission.amd`. Change Find the Lifeboat's `Then:` to `salvage/tug`. Type Wait
for the Tug. Highlight `Done when: signal tug_arrived`. Save. Run lint: the warning.

**Say:** "Now back to the story, | which runs hulk, lifeboat, home. || I want a wait before
home, | so the lifeboat step now reveals a new one. || And the new step is done when it
hears a signal, tug arrived, | which is my own word. || Lint says the tug step waits for the
signal tug arrived, | and nothing in the mission sends it. || You've seen this warning
before, | and it's right, because nothing does yet. ||"

### 9. Card one: when a step starts

**Screen:** `story.mast`, the very end, below line 105. Two blank lines. Paste the card.
Highlight the route line, then the address, then walk the `npc_spawn` line against line
68 and against the Lifeboat record in `mission.amd`. Save. Lint: the same warning, and
nothing about `story.mast`.

**Say:** "Go to the end of the file, | and it's always the end. || First a note, so I know
what this is, and then the route. || The game says quest started | every time a hidden step
is revealed, | and this block listens for that. || But it runs only if the step is this one,
salvage, slash, tug, | which is the address you write after reveal. ||| Then there's one
line, | and you've read this line before, | because it's how the hulk gets on the map. || It
says where, and its name, | then its side and its role, | and what it looks like. || Those
are the same facts as a landmark. | The difference is when. || And then arrow, END. ||"

### 10. Cards two and three

**Screen:** Add the `signal_emit` line above `->END`. Save. Lint: clean. Add the
`await delay_sim(20)` line under the route line. Save. Lint: clean. In `mission.amd`, add
the two lines to the word list. Save. Lint: clean.

**Say:** "Card two is the line from line ninety-three, | with my word in it, tug arrived, |
and it's lined up with the line above. || Lint is clean, because something sends the signal
now. ||| Card three is a wait, of twenty seconds. || The lines run from the top down, | so
it waits, brings the tug in, and finishes the step. || Then my word list gets a new role and
a new signal, | and lint is clean. ||"

### 11. Four mistakes

**Screen:** Render Whitespace on. (a) Delete one space in front of `npc_spawn`. Lint:
`Bad indentation`, line 113. Undo. (b) Move the `signal_emit` line below `->END`. Lint:
`mast-unreachable`, line 115. Undo. (c) Cut the card and paste it in the middle of the
map's lines. Lint: `mast-unreachable`, naming a map line below the card. Undo.
(d) Change `salvage/tug` to `salvage/tgu` on the route line. Lint: clean. Undo. Show the
"What lint cannot see" table on the page.

**Say:** "Here are four mistakes. || The first is one space short, on one line. | Lint tells
me: bad indentation, and the line. || The second is a line pasted one line too low, under
arrow END. || It's a warning this time, | and it says this line never runs. || It's only a
warning, | but it would stop my story. ||| The third is the card pasted in the middle of the
map. || It's the same warning, | but about a line of the template, | and the first thing it
says is to move that line up. || Don't do that, because that line is fine. || My card cut
the map in two, | and the game would start with no station and no hulk. || So move the card,
to the end of the file. ||| The fourth is the address, misspelled. || Lint says clean, and
there's no tug, ever. || Nothing can check that word for you. || The page has the list of
what lint cannot see. | It's short, so read it twice. ||"

### 12. Play it

**Screen:** Server and Helm. The Quest Log. Fly to the hulk. Fly to the lifeboat. Wait for
the Tug appears. Hold. The tug appears. The step shows Done, Bring the Log Home appears.
Fly home. The game ends. Then both logs, empty.

**Say:** "Out to the hulk, and on to the lifeboat. || There's the new step, and no tug, so
now I wait. ||| And there she is, the Salvage Tug. || The step is done, and home is
revealed. || So it's back to the station, and the win. || And both logs are empty. ||"

> Say what the screen actually shows. If the tug is not where the page says, or it moves,
> stop and fix the page.
>
> Seen in the real game on 2026-10-05, on a probe copy (the hulk, the lifeboat and the tug
> moved close to the ship and the reach distances widened, so nobody flew): Helm's map
> shows `Quest complete: Find the Lifeboat` and no tug; with the page's own twenty seconds
> the Salvage Tug is drawn with its name beside the lifeboat, 400 from it, and Helm shows
> `Quest complete: Wait for the Tug`; the win screen carries the `Win:` sentence; both logs
> are 0 bytes. One screenshot only: whether the tug then moves was not watched.

### 13. Your turn

**Screen:** The three cards and the exercise on the companion page.

**Say:** "So that's three cards: when, finish a step, and wait. || For your turn, paste the
first one again, | change started to succeeded, | and make something of your own arrive when
a step is finished. || Next time is the capstone: you ship a mission. ||"
