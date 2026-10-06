# C1-9 video script - Chains and trees

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

> **CHECKED IN THE REAL ENGINE, 2026-10-03** (server only, by a probe that put the ship at
> a point and wrote what it found to a file. The ship was never flown, and nobody has SEEN
> any of it on a screen).
>
> - The full win: Close Inspection and Quick Work finish near the hulk, Bring the Log Home
>   near DS 1, the arc completes, and the game ends carrying the `Win:` sentence, with 350
>   credits.
> - The bonus failing, with the story still won.
> - The deadline: the arc fails and the game ends carrying the `Lose:` sentence.
> - The wrong-heading mistake: the game is won at the hulk.
>
> The engine matched the mock on all four. That run used the first version of this
> lesson's files: the template of that day, plus Close Inspection, plus this arc. The four
> records of the arc have not changed since.

> **Re-measured 2026-10-04 (night). Not run in the engine again.**
>
> - Library: the packaged one in `__lib__`, built from sbs_utils `0c4c0fae` and
>   LegendaryMissions `298ffb3` and not rebuilt while this ran. Every mock run used it.
>   Starter template `60c30bc`, which is what `sbs create -t amd` downloads now.
> - **The library moved during the pass.** At 20:51 the working trees went to sbs_utils
>   `0d76c0c4` and LegendaryMissions `b20726f` (both about how the Quest Log draws a
>   selected row). Lint runs on the working tree, so all 143 lint runs were made again at
>   `0d76c0c4`: every one prints the same lines. Six plays were made again with the
>   working-tree sbs_utils: the same lines, but for the one difference in the next point.
> - **One thing on the page needs the new commits, built into `__lib__`.** The page says
>   to put the time limit in the arc's description. With the packaged library of this
>   pass the Quest Log's pane is given NOTHING for a selected arc (measured: an empty
>   string for First Contact and for Salvage Run). With sbs_utils `0d76c0c4` it is given
>   the arc's description, its steps that are showing, and `... more to follow`. That is
>   why the page says to write the limit in the first step's description as well: a
>   step's description is in the pane with either library.
> - The lesson now starts from Lecture 8's finished files, read from
>   `c1-08-first-quest\example\` (both files), not from the untouched template. `example\`
>   here is those two files with this lecture's six steps typed in. Lecture 8's quest is
>   not replaced and not left beside the arc: Step 2 makes it the arc's first step, word
>   for word, and it still finishes inside 500 of the hulk and still pays 100.
> - 159 variants: Lecture 8's files untouched, the six steps one at a time, the finished
>   files, and one change to the finished files at a time. Each was linted with the
>   installed `sbs.pyz` and, where the page says what the game does, played headless with
>   the packaged library, one at a time: 161 lint runs (18 of them the nine states of the
>   tool note, linted with both tools) and 131 mock runs.
> - A first pass of 155 of those variants was run on a start file the harness built
>   itself: Lecture 7's example plus Close Inspection. It differed from Lecture 8's
>   finished file by one blank line, below everything this lecture adds. Nothing on the
>   page is quoted from it. A script compared the two passes: lint printed the same lines
>   for 153 of the 155 (one differs by a line number past the arc, one by which switches
>   were run), and the probe printed the same lines for all 127 played in both.
> - Every line of tool output printed in a code block on the page was checked against
>   those runs by a script (`c19r\verify_page.py`). Every row of the Step 7 tables is tied
>   to the run that measured it by a second script (`c19r\rows.py`): the codes in the row
>   are the codes lint printed, and what the row says the game does is tested on the
>   probe's own lines.
> - The same lesson on the untouched template plus Lecture 8's quest lints clean and plays
>   the same (measured). There the findings print the same sentences six lines lower:
>   `line 59:14`, not `line 65:14`.
> - What the Quest Log holds was read with the two calls the console's own quest tab
>   makes (`quest_tab_items`, `quest_offers_tab_items`). The probe of 2026-10-03, and
>   tonight's first pass, read the raw list behind them, which also returns a step that
>   is only on offer. No console lists such a step.

> **Tool note.** The page needs an `sbs.pyz` built from sbs_cli `f28e7f1` or later. The
> one installed here was built from that commit today. It still prints version `0.10`,
> the same as the released one; a release as `0.11` is pending. One thing on the page
> comes from the tool and not from the library: "If something goes wrong" sends the
> student to `mast.runtime.log` after a play, and the released 0.10 empties both logs
> every time lint runs (from the list of fixes; not measured here). Every finding on the
> page comes from the library. Nine states of this lesson were linted with the `sbs.pyz`
> kept from before today and with the installed one, and all nine print the same. The
> library has to be `0c4c0fae` or later: `never-revealed` and `quest-never-finishes` are
> new, a `dangling-reveal` now ends with a line to write, and `reveal salvage / home`
> with spaces now works in the game.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 8 leaves it. `mission.amd` must match `c1-08-first-quest\example\mission.amd` line for line (82 lines, the Close Inspection heading on line 47), or the line numbers 65, 68 and 71 on the page are wrong |
| Lecture 8's exercise quest | Type one under Close Inspection before recording. Scene 4 needs it there to show where not to type. It sits below everything the page numbers, so 65, 68 and 71 still hold (measured with a quest keyed `watch`) |
| `story.mast` | Lecture 8's, which is Lecture 7's finished file. Never opened in this lecture |
| Library | sbs_utils `0d76c0c4` or later and LegendaryMissions `b20726f` or later, BUILT into `data\missions\__lib__`. With the older build (`0c4c0fae`, `298ffb3`) everything on the page still holds except one thing on camera: selecting Salvage Run in the Quest Log shows no description |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, font size raised, the status bar (`Ln`, `Col`) in shot |
| Command prompt | Open in `data\missions`, cleared, wide enough that one finding fits on three lines |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 10 with a server and a Helm console |

## Confirm on camera

What was checked, and how. "Lint" means the installed `sbs.pyz`, run from `data\missions`
on a copy of the files with that one change. "Mock" means the mission was then played
headless with the packaged library, and a probe put the ship 300 from the hulk, then 600
from DS 1, and printed every quest's state, the side's credits, what the Quest Log call
returned, and every line sent to the ship three ways (a ship message, a comms message, a
story dialog). "Engine" is the run of 2026-10-03 in the note above. Nobody has SEEN any
of it on a screen. If an item fails while recording, stop and fix the page.

On Lecture 8's files, before a line is typed:

1. Lint is `clean`. Close Inspection alone is active at the start, finishes inside 500 of
   the hulk, and pays 100. (Lint, Mock.)

On the lesson's steps, typed in order:

2. Lint is `clean` after each of the six steps. (Lint.)
3. In the middle of Step 3, with Bring the Log Home typed and the `Then:` line not yet,
   lint prints the `never-revealed` line on the page, word for word, with `line 68`.
   (Lint. The same line, with `line 68`, when Lecture 8's exercise quest is in the file.)

On the finished `mission.amd`:

4. At the start the arc and its two at-once steps are active and Bring the Log Home is
   hidden. The Quest Log call returns Salvage Run with Close Inspection and Quick Work
   under it, and not Bring the Log Home. (Mock.)
5. Inside 500 of the hulk: Close Inspection and Quick Work complete together, the side
   has 150 credits, and Bring the Log Home becomes active and is listed. (Mock, Engine.)
6. Inside 1000 of DS 1: Bring the Log Home completes, the side has 350, the arc
   completes, and the game ends carrying the `Win:` sentence. (Mock, Engine.)
7. The words sent to the crew: `Quest complete: Close Inspection`, `Quest complete: Quick
   Work`, `Quest complete: Bring the Log Home`, `Mission complete: Salvage Run`. (Mock.)
8. Reaching the hulk and staying there does not end the game. Going to DS 1 first
   finishes nothing. (Mock.)
9. With Lecture 8's exercise quest left in the file under the arc: lint is `clean`, the
   story plays to the same win, and that quest sits in the Quest Log beside the arc.
   (Lint, Mock.)

On a copy that differs ONLY in a time, because a headless run cannot wait minutes:

10. Quick Work fails and the story is still won, with 300 credits. (Copy: `6 seconds` in
    place of `2 minutes`.) Words sent: `Quest failed: Quick Work`. (Mock, Engine.)
11. The arc fails and the game ends carrying the `Lose:` sentence, with 0 credits.
    (Copies: `20 seconds` and, as the page says, `30 seconds`.) Words sent: `Mission
    failed: Salvage Run`. (Mock, Engine.)
12. No warning is sent before the arc's time runs out. With a 70-second clock the only
    thing sent, by any of the three ways, was `Mission failed: Salvage Run`. The probe
    can see a reminder when one is sent: with `Speaker: station` added to the arc it
    recorded two comms messages, `AUTOMATED SIGNAL - 0:59 REMAINING` and `AUTOMATED
    SIGNAL - 0:29 REMAINING - FINAL`. That line is not taught, because lint flags it
    (`dangling-speaker`). (Mock.)
13. The Quest Log's clock: the row for Salvage Run carries `9:57 left` and the row for
    Quick Work `1:57 left`, four seconds in. The pane for a selected step is given
    `State`, `Reward`, `Time left` when it has a clock (`1:57` for Quick Work), and then
    its description. The pane for a selected arc is given nothing with the packaged
    library, and the arc's description and its listed steps with sbs_utils `0d76c0c4`.
    Neither gives a `Time left` for the arc. (Mock, both libraries: that is the text the
    library hands the screen. How it is drawn is UNSEEN.)
14. The exercise: a fourth, required step, revealed by the third and finished by a timer,
    wins the game after the wait. (Mock, with `30 seconds` and with `5 seconds`.) With its
    `Then:` line forgotten, lint says `never-revealed`.
15. "Writing a time": 24 ways of writing a time were put in one file and read back from
    the game in one run. (Mock.)

Step 7:

16. Three hashes on Bring the Log Home: lint prints the `dangling-reveal` line on the
    page, word for word. Played, the game is won at the hulk. With the line lint offers,
    `Then: reveal home`, lint is `clean` and the game is still won at the hulk. (Lint,
    Mock. The Engine run made the same mistake the other way, with the steps typed below
    another quest, and the game was won at the hulk there too.)
17. Every row of the tables in Step 7: lint for all of them, and the mock for every row
    that says what the game does. (Lint, Mock, one variant at a time.)
18. "A story that cannot be finished ends one way": a misspelled `Then:` line with the
    clock set to 20 seconds. The crew reaches the hulk, waits, and the game is lost.
    (Mock.)

Not checked, and to watch for while recording:

1. Anything in the real game for THESE files. The Engine run was on the first version.
   A `Fails when:` clock and the end of the game were run there by a probe, never by a
   person.
2. Any screen: the Quest Log with an arc and its steps folded under it, where the
   "complete" and "failed" lines appear, and what the end-of-game screen shows. Lectures
   6 and 8 saw the Quest Log for other files.
3. Whether two minutes is enough to fly to the hulk. In the mock run the ship started
   3500 from DS 1 and 11476 from the hulk. If it is too tight on camera, raise the number
   on the page and here.
4. When the ten-minute clock starts if the server picks the map by hand. In the checks
   the map was started automatically and the clock was running within three seconds.
5. Flying inside 500 of the hulk and inside 1000 of DS 1 by hand.
6. First Contact finishing by itself at the hulk. The page says it does, from what
   Lectures 6 and 7 saw in the engine. The mock never scans by itself, so there only
   Find the Derelict finishes.
7. Everything in VS Code: clicking in front of the first `#`, Enter twice, `Ctrl+S`.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. The ship arrives at DS 1. A mission-complete line, then the end of
the game.

**Say:** "Last time, you wrote one quest, | and a quest is a task. || This is a story, with
a beginning, a middle, | and an ending you can win or lose. || It's still one text file, and
it's still no code. || And the quest you wrote last time | is going to be its first step.
|||"

### 2. A heading for the story

**Screen:** `mission.amd`. Click in front of the first `#` of `### [Close Inspection]`.
Type the Salvage Run record. Enter twice.

**Say:** "A story needs a heading, | and it's made the way every heading is: | three hashes,
a name, and a key. || Inside the fence there's one word on a line by itself, | the word Arc,
with no colon after it. || What that word says is, | I'm not a task, I'm the heading over
some tasks. ||| The rest you've seen before: | it's shared, it starts at once, | and below
the fence there's one line of story. ||"

### 3. One hash

**Screen:** Add a fourth hash to Close Inspection. Pause on it.

**Say:** "Now for the trick, and it's just one more hash. || Four hashes means, I'm a step
of the three-hash record above me. || And that's all nesting is. ||| So Close Inspection was
a quest, | and now it's step one of Salvage Run, | which gives it a full address: salvage,
slash, approach. ||"

### 4. The second step, and where not to type it

**Screen:** Scroll down to show the Lecture 8 exercise quest under Close Inspection. Point
at it. Scroll back. Click at the end of Close Inspection's description. Enter twice. Type
Bring the Log Home.

**Say:** "Step two goes here, and not at the bottom of the section. || That's because a
four-hash step belongs to the nearest three-hash heading above it, | and my quest from last
time is a three-hash heading. || So if I type below it, | my new step joins the wrong story,
| and the game is won at the first step. ||| Lint does warn about that, | and I'll show you
the warning at the end, | because it comes with a trap. || Now, this line is new: Starts
when, revealed. || It means this step is hidden and asleep, until something wakes it. ||"

### 5. The chain

**Screen:** Save. Command prompt: `sbs lint MyMission`. The `never-revealed` warning.
Highlight `Then: reveal salvage/home` inside it. Back to the file: add that line to Close
Inspection's fence. Save. Lint: `clean`.

**Say:** "Nothing wakes it yet, and lint knows that. || It read the word revealed, | went
looking for the line that reveals this step, and found none. || Now read to the end of the
warning, | because it writes the line out for me, | and the line begins Then, reveal. ||
That says, when Close Inspection finishes, start that one. || Notice it's the full address,
arc, slash, step, | and not just the word home. || And a quest gets one Then line, no more.
||| So I add it, I save, and lint says clean. || That's a chain: you finish one, and the
next begins. ||"

### 6. A step you can skip

**Screen:** Click at the end of Bring the Log Home's description. Enter twice. Type Quick
Work. Highlight `Fails when: 2 minutes`.

**Say:** "Next comes a bonus: reach the hulk inside two minutes. || It has a Done when line,
| and it has the opposite, Fails when, | and whichever comes first decides it. || So if the
crew is quick, they're paid fifty. | If they're slow, the step fails, | and that's all that
happens. ||"

### 7. What the story needs

**Screen:** Add `Part of: salvage` and `Required: true` to Close Inspection and to Bring
the Log Home. Leave Quick Work alone.

**Say:** "As it stands, the story waits for every step, the bonus included. || So if the
bonus failed, the story could never finish. ||| That's why I say which steps count. || I add
two lines, Part of salvage, and Required true, | on these two steps, and not on the bonus.
|| And now the story is done | when the required steps are done. ||"

### 8. Two endings

**Screen:** Scroll up to show both arcs, First Contact and Salvage Run. Click into Salvage
Run. Add `Fails when:`, `Win:`, `Lose:`. Save. Lint: `clean`.

**Say:** "There are two arcs in this file, | and they start with the same three lines, | so
I make sure I'm in Salvage Run. || First comes a time limit, | then Win, with a sentence, |
and Lose, with a sentence. || Win fires when this record is finished, | and Lose fires when
it fails. ||| And here's the rule to remember: | Fails when only fails a quest. || It's Lose
that makes a failure end the game. ||| So I run lint, and it's clean. ||"

### 9. The warning with a trap

**Screen:** Take one hash off Bring the Log Home. Save. Lint: the `dangling-reveal`
warning. Highlight `line 65`, then the last words, `write Then: reveal home`. Do NOT type
it. Put the hash back. Save. Lint: `clean`.

**Say:** "Now, there's one mistake I want you to see | before you make it yourself: | one
hash too few on a step. || Lint warns me, and it's talking about line sixty-five, | which is
my Then line, and not the heading I changed. || You know that habit of lint's from Lecture
6. || But look at how the sentence ends. || It's found my step in its new place, | and it
offers me a new Then line that points there. || If I write that, lint says clean, | and the
game is won the moment the crew reaches the hulk, | because my story has only one step left.
||| The Then line was right all along, | and it was the heading that was wrong. || So, when
lint offers you a new Then line, | count the hashes on the step first. ||"

### 10. Play it: win

**Screen:** Server and Helm. The Quest Log: Salvage Run with two steps. Fly to the hulk.
The completion lines. Bring the Log Home appears. Fly to DS 1. The game ends.

**Say:** "Here's the Quest Log, with two steps showing, | and the third one still hidden. ||
So in we go, toward the hulk. || Close Inspection is done, and Quick Work is done with it.
|| And there's step three, Bring the Log Home, | so we turn for home. || And that's the win,
with my own sentence on it. ||"

### 11. Play it: lose

**Screen:** Change `10 minutes` to `30 seconds`. Start again. Do nothing. The game ends.
Change it back.

**Say:** "Now I change ten minutes to thirty seconds, | and I sit on my hands. || And it's
lost, with my other sentence. || Notice that nobody warned me. || Your crew gets no
countdown call, | so tell them the limit in the arc's description, | and tell them again in
the first step's. || And then I put ten minutes back. ||"

### 12. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: add a fourth step. || It's revealed by the third, | it's
finished by a timer, and it's required. || Then the win comes thirty seconds after they get
home. ||| Next time, we look at the things quests point at. ||"
