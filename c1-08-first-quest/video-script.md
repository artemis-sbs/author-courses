# C1-8 video script - Your first quest

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

> **CHECKED IN THE REAL ENGINE, 2026-10-03** (by a script, server only: the script moved
> the ship and read the results from a file. Nobody has SEEN any of this on a screen).
>
> - The quest is live at the start: active 8 seconds in.
> - It does not finish with the ship 1500 from the hulk, and it does finish at 300.
> - The side is paid 100 credits when it finishes.
>
> That run used the first version of this lesson's files: the untouched template plus
> Close Inspection. The record itself has not changed since.

> **Re-measured 2026-10-04 (evening). Not run in the engine again.**
>
> - Library: sbs_utils `v1.4.0` at `0c4c0fae` (working tree and `__lib__`, the same at the
>   start and at the end), LegendaryMissions `298ffb3`. Starter template `60c30bc`, which
>   is what `sbs create -t amd` downloads now.
> - 166 variants: the finished files, and one change to them at a time. Each was linted
>   with the installed `sbs.pyz` and then played headless with the packaged library, one
>   at a time: 184 lint runs, 169 mock runs. Every line of tool output printed in a code
>   block on the page was checked against those runs by a script
>   (`c18r\verify_page.py`).
> - The lesson now starts from Lecture 7's finished files, not from the untouched
>   template, so `example\` holds both files. The same record on the untouched template
>   lints clean and plays the same (measured). There the two slips of Step 5 print the
>   same sentences with `line 46`, not `line 52`.

> **Tool note.** The page needs an `sbs.pyz` built from sbs_cli `f28e7f1` or later. The
> one installed here was built from that commit today. It still prints version `0.10`,
> the same as the released one; a release as `0.11` is pending. One row of the page comes
> from the tool and not from the library: "Lint prints `== story.mast (compile) ==`" in
> "If something goes wrong". The released 0.10 does not check `story.mast` at all (from
> the list of fixes; not measured here with the old tool). Every other finding on the
> page comes from the library, and needs `0c4c0fae` or later: `quest-never-finishes` is
> new, and a misspelled role on a `Done when:` line used to lint clean.

Target length: 13 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. The finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 7 leaves it: both files of `c1-07-roles-and-signals\example\`, line for line. Line 52 of `mission.amd` and line 68 of `story.mast` on the page depend on that |
| Starter template | The fixed `amd` template (starter repo `60c30bc`). A fresh `sbs create -t amd` delivers it: measured today, the two files are the same |
| Library | sbs_utils `0c4c0fae` or later, LegendaryMissions `298ffb3`, as built into `data\missions\__lib__` |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` folder open, `mission.amd` and `story.mast` in tabs, font size raised |
| Command prompt | Open in `data\missions`, cleared, wide enough that one finding fits on three lines |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. It is started on camera in scene 7, as the server with a Helm console |

## Confirm on camera

What was checked, and how. "Lint" means the installed `sbs.pyz` (sbs_cli `f28e7f1`, library
`0c4c0fae`) on the finished files with that one change. "Mock" means the mission was then
played headless with the packaged library. A probe put the ship 1500 from the hulk, then
600, then 450 (or straight to 300), read every quest's state and the side's credits, and
asked the library's own two builders what the Quest Log and Available Quests are handed.
"Engine" is the 2026-10-03 run in the block at the top, or something seen on a console on
2026-10-04 by the session that fixed the tools, on Lecture 6's files. If an item fails
while recording, stop and fix the page.

1. Lint on the finished files: `clean`, and the count line. (Lint.)
2. The two slips of Step 5, word for word, with `line 52`. (Lint.) With either one the
   quest is active at the start and still active with the ship 300 from the hulk. (Mock.)
3. The quest is live at the start. (Engine, by script. Mock.)
4. It does not finish at 1500 or at 600. It finishes at 450 and at 300. (Mock. Engine, by
   script: not at 1500, done at 300.)
5. The side is paid 100 credits when it finishes. (Engine, by script. Mock.)
6. Where the quest list is: the handheld icon beside the crew member's name, the ePADD,
   **Quests**, the **Quest Log**, the list on the left, `State` and the text on the
   right, `Done` on a finished quest. (Engine, seen, on Lecture 6's files.) For THESE
   files the Quest Log is handed a row "Close Inspection" with `Active` under it, then
   `Done`, and a pane of `State`, `Reward | 100 credits` and the description. (Mock.
   UNSEEN on a screen.)
7. **CHANGED 2026-10-05 (library `a058ee00`, seen in the game): the Quest Log DOES show a typed `Objective:` sentence, on its own line above the description. The rest of this item is from before.** The Quest Log does not show the `Objective:` sentence. (Mock: the pane and the row
   it is handed do not hold it. Read in the code as well: nothing that draws a quest in
   this mission reads the field. The library's own field table says the quest log shows
   it. UNSEEN.) If the sentence IS on the screen when you record, correct Step 6 item 2
   and the `Objective:` row of the Step 3 table.
8. A quest with no `Starts when:` line is handed to Available Quests and not to the
   Quest Log, with `Reward: 100 credits` under its name. (Mock.) Where Available Quests
   is on the ePADD, and the Accept button: UNSEEN.
9. When a quest finishes the library sends the ship the line "Quest complete: Close
   Inspection". (Mock: the send was tapped.) Where a console shows it: UNSEEN. The page
   does not mention it.
10. Inside 2000, Find the Derelict finishes, Study the Derelict appears, and the ship's
    sensors finish it within seconds. (Engine, seen, for Lectures 6 and 7. In the mock the
    probe sends the scan.)
11. The exercise: a second quest with `Done when: 2 minutes` is active at 110 seconds and
    done at 126, with nobody flying anywhere, and its reward is paid. (Mock, the full two
    minutes.)
12. Every row of the four tables in Step 5. (Lint and Mock, one variant at a time.)
13. Other built-in verbs. `dock station`: the probe sent the signal the docking addon
    sends, and the quest finished; nobody flew a docking. `scan 1 derelict`: the probe
    sent the scan the engine's sensors make; the quest finished. `destroy 3 raiders`: NOT
    run. This mission has nothing to destroy.
14. Both logs are empty after a play of the finished files. (Mock.)
15. Nothing in VS Code was checked. The page no longer says what VS Code underlines.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game, Helm. The ship closes on a dark hulk. The Quest Log, with Close
Inspection showing `Done`.

**Say:** "That quest is mine. || Nine lines in a text file put it there. || And in the next
few minutes, you'll write your own first quest, | and you won't write any code to do it.
|||"

### 2. Where quests live

**Screen:** VS Code, `mission.amd`. Scroll to `## [Quests](quests)`. Collapse and expand
First Contact.

**Say:** "This is your fact sheet. || Two hashes make a section, | and this section is
Quests, | so everything under it is a quest, until the next section starts. || Right now it
holds one story, First Contact, in two steps. || We're going to leave that alone, | and add
one of our own underneath it. |||"

### 3. Write it

**Screen:** Cursor on the blank line above `// ---- Science scans.` Type the record, one
line at a time. Save.

**Say:** "I start with three hashes, which makes this a quest of its own. || Then a name the
crew will read, and a key. || Then I open the fence. ||| Shared means it's one quest for the
whole crew. || Starts when, at once, means it's live as soon as the game starts. || The
objective is the order, in one sentence. || Done when is the one we'll come back to. || Then
comes the reward, and I close the fence. ||| And last, one line of story, | which is the
text the crew will read. |||"

### 4. The line that matters

**Screen:** Highlight `Done when: reach derelict 500`. Then the `story.mast` tab, line 68,
with `"tsn, derelict, ghost_ship"` selected. Change nothing.

**Say:** "This is the line that matters most. || It's a verb, then a role, then a number, in
that order. ||| Reach means get close, | and five hundred is how close. || And derelict is a
role, | which you met last time. || Here's the hulk's list: | its side, and then the two
roles it wears. || The promise is the same as it was for a reading: | something has to wear
the word. ||| What's new here is the verb. || Last time, a step waited for a signal, | and
this file had to say it. || But reach is built in, | so the game does the watching itself.
|| And that's why there's nothing to change in here. |||"

### 5. Getting it wrong

**Screen:** Change `Done when:` to `When:`, save, run lint: the `quest-never-finishes`
warning. Undo. Change `derelict` to `derelect`, save, run lint: `role-nothing-wears`.
Undo. Delete the `Starts when:` line, save, run lint: `clean`. Undo. Then the page, "What
lint cannot see".

**Say:** "Here are two slips that lint catches. || The word When, on its own, means when the
quest starts, | so nothing ever finishes this quest, | and lint says exactly that. || Then
there's a role spelled wrong: | nothing wears it, and lint says that too. ||| Now here's one
it doesn't catch. || If I take out the line that says Starts when, at once, | lint still
says clean, | but the quest is only on offer. ||| The page has a table of these, | and the
ones to remember are these: | the number goes last, and nothing goes after it, | and count
your hashes. |||"

### 6. Check it

**Screen:** Command prompt: `sbs lint MyMission`. Show `clean` and the count line.

**Say:** "Now I put everything back the way it was, and run lint. || And it's clean, with no
errors and no warnings. |||"

### 7. Play it

**Screen:** Start the server and a Helm console. The handheld icon, **Quests**, the Quest
Log. Select Close Inspection. Fly to the hulk. Show the range passing 2000, then 500. The
Quest Log again.

**Say:** "Here's the Quest Log, and here's mine, | with its state, its reward, and my
description. || So now we fly. ||| At two thousand, Find the Derelict is done. || But that's
last lecture's signal, and not my quest, | so mine hasn't moved. ||| Then, inside five
hundred, | it's done, and the crew is paid. |||"

### 8. Your turn

**Screen:** The exercise on the companion page. Then the built-in verbs table.

**Say:** "Now add a second quest, one that finishes on time, | with Done when, two minutes.
|| That's just a number and a unit. ||| There are five verbs built in, | and they're all on
the page. ||| Next time we'll join quests together, | so that one leads to the next. |||"
