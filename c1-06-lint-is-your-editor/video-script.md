# C1-6 video script - Lint is your editor

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

> **Written for tools that are not all released yet.** Read this before recording.
>
> - Library: sbs_utils `v1.4.0` at `0c4c0fae` or later (released 2026-10-04) and
>   LegendaryMissions `298ffb3`. Every lint line on the page, and every "Lint says" cell
>   of its tables, was measured again at `0c4c0fae`. What the game does was measured for
>   every row at `947e3f8a`, and again at `0c4c0fae` for the rows the last fixes touch.
>   Break 3's second warning and the `never-revealed` row need this library: an older one
>   prints one warning for break 3.
> - Command-line tool: an `sbs.pyz` built from sbs_cli `f28e7f1` or later. **That one is
>   NOT released.** The page was measured with the tool run from source at `f28e7f1`. The
>   released `sbs.pyz` (it prints `0.10`, and so does the source: `sbs version` cannot
>   tell them apart) gets these parts of the page wrong. The right-hand column comes from
>   the first measurement of this lesson, the morning of 2026-10-04, and from the list of
>   fixes made since. It was not measured again:
>
>   | Part of the page | With the released 0.10 |
>   |---|---|
>   | Step 8, items 6 and 7; the row "`mast.runtime.log` still shows a line" | Lint empties both logs every time it runs |
>   | "If something goes wrong": `ERROR: which mission?` | `sbs lint` with no folder name reads every mission in `data\missions` as one. Do not try it |
>   | "The files" table: both `amd-file-missing` rows | Lint says `clean`, or only `0 amd` |
>   | "The files" table: the `mast-compile` row; "`clean` means four things"; the `not checked:` row | Lint does not check that the game can read `story.mast` |
>   | "Three switches": the `FAILED:` line under `--strict` | The same lines as plain lint, and nothing more |
>   | The emoji row of the Text table, when lint's output is sent to a file | A character the output cannot hold stops lint with a programmer's error |
>
>   A safe way to tell which tool is installed: make break 1, then type
>   `sbs lint MyMission --strict`. The fixed tool prints
>   `FAILED: --strict counts a warning as a failure` under the count line.

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. The finished files are in `example\`, and
they are the untouched template: this lesson ends where it began.

## Before recording

| Item | State needed |
|---|---|
| Mission | A fresh mission from the `amd` template, `MyMission`, nothing edited. Line numbers on the page depend on that |
| Starter template | The local `amd` template (starter repo `60c30bc`). `example\mission.amd` is the same file with plain line endings; the lint lines are the same either way (measured) |
| Library | sbs_utils `0c4c0fae` or later, LegendaryMissions `298ffb3`, as built into `data\missions\__lib__` |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` open, `mission.amd` in front, font size raised, the file list visible, the status bar (`Ln`, `Col`) in shot |
| Command prompt | Open in `data\missions`, cleared, wide enough that one finding fits on three lines |
| Word processor | Open, with this typed in it: `Fly out and locate the "ghost ship". It isn't answering.` It must have turned the quote marks curly |
| Logs | Leave `mast.compile.log` and `mast.runtime.log` as the last play left them. Lint does not make them and does not change them |
| Game | Closed. It is started on camera in scene 10 |

## Confirm on camera

What was checked, and how. "Run" means the command-line tool, run from source at
`f28e7f1` with the library at `0c4c0fae`, on a copy of `example\` with that one change.
"Mock" means the mission was then played headless with the packaged library, and a probe
read the quests and the scan text out of the game. "Engine" means it was seen in the real
game on 2026-10-04 by the session that fixed the tools, and reported to this one. This
pass did not start the engine.

1. The clean answer, and its four lines. (Run.)
2. Break 1 to break 5, both halves of break 5: each finding, word for word, with its line
   and column. (Run, and run again on a copy saved with Windows line endings: the same
   lines.)
3. Each fix brings back `clean`. (Run: the mended file is the untouched one.)
4. `--missing` on break 3 and on the clean file; `--missing` saying `Nothing missing` on
   a file with errors; the `FAILED:` line under `--strict`; `--format compact` printing
   nothing on a clean mission. (Run.)
5. What the game does in every row of the Step 7 tables. (Mock, one variant at a time.
   For the rows about steps, the probe also sent the two signals the template sends when
   the ship reaches the hulk and when Science scans it.)
6. Lint leaves both logs alone, and makes neither when they are not there. (Run: two logs
   of 24 and 23 bytes, the same after four lint runs; a fresh folder has no logs after
   lint.)
7. Break 5 with four hashes, played: all three quests are there, the hulk has both tabs,
   and `mast.runtime.log` holds exactly the one line on the page. (Engine, and Mock: the
   same line.) After the fix and a second play both logs are empty. (Mock.)
8. Where the quest list is: the handheld icon beside the crew member's name, the ePADD,
   **Quests**, the **Quest Log**, the list on the left, `State` and the text on the
   right. (Engine.)
9. Curly quotes in a description are drawn as plain `"` and `'`. (Engine, seen on Helm.)
   A long dash as `-`, three dots as `...`, an accent dropped, an emoji left out. (Mock:
   that is the text the game holds. UNSEEN on a screen.)
10. Break 4, played: the hulk keeps its `mat` reading and has no `scan` reading. (Engine,
    and Mock.)
11. Break 5 with one hash, played: the hulk has no scan text at all, and the log holds
    the sentence of lint's first finding, word for word. (Mock only. UNSEEN.)
12. `Ctrl+G` goes to a line; with the caret just in front of the first curly mark the
    status bar shows `Ln 31, Col 24`. (Not checked on a screen. Lint's column counts from
    1: a finding at the start of a line prints `28:1`.)
13. The command prompt shows the curly marks inside lint's own message. (Not checked on a
    real console. Through a pipe they print as themselves. An emoji prints as
    `\U0001f680` when the output is sent to a file.)
14. The up arrow recalls the last command. (Not checked.)
15. The AMD extension underlines the same findings as you type. (Not checked. The page
    does not claim it. If it does, show it in scene 4 and add one sentence to the page.)
16. The `not checked:` row in "If something goes wrong". (Run, on this machine made to
    look like one that has never fetched the development library. Not seen on such a
    machine.)
17. The two lines `sbs debug` prints about `EXTRA_SHIP_DATA` and `@media/skybox`.
    (Printed by the runner that `sbs debug` starts, on the untouched example. `sbs debug`
    itself was not run in this pass.)
18. Scene 9: with the line `# remember to make this scarier` typed under a description,
    lint says `clean` and the note is part of the description the game holds. (Run and
    Mock. How the Quest Log draws it is UNSEEN.)
19. A `---` scene break in a description is kept as part of the description. (Mock: the
    quest's text holds the three hyphens. How the Quest Log draws them is UNSEEN.)
20. Break 3, played: Find the Derelict finishes, Study the Derelict never appears, and
    `mast.runtime.log` holds one line that starts `Quest: there is no quest`. (Mock. The
    same was seen in the engine for the renamed story key.)

If item 9, 11, 18 or 19 turns out differently on camera, stop and fix the page.

## Scenes

### 1. Cold open

**Screen:** The command prompt. `sbs lint MyMission`. One warning line appears. Freeze on
it.

**Say:** "This one line is the most useful sentence anyone's going to say about your mission
this week. || It tells me which file and which line, | what's wrong there, and what the game
will do about it. ||| So today you'll learn to read it, | and we'll do that by breaking your
mission in five places, on purpose. |||"

### 2. What lint is

**Screen:** A manuscript page with an editor's marks on it. Then the command prompt.

**Say:** "Lint is a program that reads your files and lists whatever looks wrong, | and it
changes nothing. || Think of the editor at a publisher: | she reads, and she marks, | and
you're the one who does the fixing. ||| The habit has four beats. || You change something,
and you save. | Then you run lint, | and you read the first line it prints. |||"

### 3. A file with nothing wrong

**Screen:** `sbs lint MyMission`. The four-line answer. Highlight the count line.

**Say:** "This is the answer you're hoping for. || There's the file, then the word clean, |
and then the count line, which says one fact sheet, one story file, | no errors, and no
warnings. ||| Read that count line every time, | even when it says clean. |||"

### 4. Break 1: a field name

**Screen:** In Find the Derelict, change `Done when:` to `Done wen:`. `Ctrl+S`. Up arrow,
Enter. Highlight the four parts of the finding, one at a time. `Ctrl+G`, `28`. Then
highlight the three parts of the sentence.

**Say:** "I'm going to misspell one field, | then save, and run lint. || And I get one
warning. ||| Every finding has four parts. || First there's the level, which here is
warning. || Then there's the place, | which is line twenty-eight, character one. || Then
comes the sentence itself. || And at the very end, in brackets, there's the code, | which is
lint's short name for this kind of mistake. ||| Now read the sentence all the way to the
end, | because it tells you three things. || First, what's wrong: Done wen is not a field a
quest has. || Next, what the game does about it: nothing reads this line. || And last, what
to write instead: did you mean Done when. ||| So I fix it, I save, | I run lint again, and
it's clean. ||| Now, that was only a warning, | so I could have played this mission. || But
with that one word misspelled, | this step can never finish. || A warning can stop your
story just as surely as an error. |||"

### 5. Break 2: words from a word processor

**Screen:** The word processor. Copy the sentence. Paste it over the description. Save,
lint. Three warnings. Point at `31:24`, `31:35`, `31:44`. Click in front of the first
curly mark: the status bar. Retype the three marks. Lint: clean. Put the first sentence
back.

**Say:** "Every writer does this next one. || I wrote my line in a word processor, | and it
quietly made my quote marks curly. || So now I get three warnings, | one for each mark. |||
All three are on line thirty-one, | and this second number tells me how far along the line
to look. || Read to the end again: | the game can't draw this mark, | so it shows the plain
one in its place. || That means the crew would still read my sentence. ||| It's a warning
all the same, | because the game only has a plain twin for some characters, | and an emoji,
for instance, is simply left out. || So I delete each mark and press the plain key, | and
it's clean again. |||"

### 6. Break 3: a key that no longer matches

**Screen:** Change `(study)` to `(examine)` on line 33. Save, lint. Two warnings.
Highlight `line 29`, go to line 29. Highlight `line 36`, go to line 36. Then
`sbs lint MyMission --missing`. Put the key back. Lint: clean.

**Say:** "This time I rename a key, on line thirty-three. || Lint complains about line
twenty-nine and line thirty-six, | and it says nothing at all about thirty-three. || So why
is that? ||| Line twenty-nine points at the old key, | and no record has that key any more,
| so nothing is revealed. || And line thirty-six is the step I renamed. | It's waiting to be
revealed, | and now nothing reveals it. ||| Those are the two ends of one broken link, | and
lint names the line that points, and the line that waits. ||| There's a second way to ask,
too. || If I run lint with the word missing on the end, | I get a list of every key I've
pointed at and haven't written yet. || While I'm drafting, that's my to-do list. ||| So I
put the key back, | and both warnings go away, and it's clean. |||"

### 7. Break 4: a fence left open

**Screen:** In Derelict Hull, delete the second `---`. Save, lint. One error. Highlight
`line 48`, then line 48 in the file, then the last words of the sentence. Type `---` back.
Lint: clean.

**Say:** "Now I delete just one line, | the three hyphens that close this fence. || And that
gets me my first error. ||| I deleted line fifty-one, | but lint names line forty-eight. ||
That's the line where the fence opens, | the fence that now never closes. || And the
sentence tells me the rest: | the lines under the fields were read as fields, | so this
record has no text. || It gives me the fix as well, | which is to add a line of three
hyphens under the last field. ||| So I type it back, and it's clean. || It's the same lesson
as the last break: | the line lint names isn't always the line I changed, | so let the
sentence tell you where to look. |||"

### 8. Break 5: the number of hashes

**Screen:** Add a fourth hash to Derelict Hull. Save, lint. One error. Remove it. Lint:
clean. Then take two hashes off, so the heading has one. Save, lint. Three findings.
Highlight only the first. Point at line 55 in the file. Type the hashes back. Lint: clean.

**Say:** "The hashes say where a record sits. || So let's give this one a hash too many, |
and that's one error. || This heading has four, | and the one it sits under has two. || And
look at what the game does about it: | it reads the heading as if it had three. || Here that
guess happens to be right, | so nothing is lost. ||| In break one, a warning stopped my
story, | and here an error costs me nothing. || So I don't judge a finding by its level. | I
read its sentence. ||| I take the extra hash off, | and now let's go the other way, down to
one hash. || And that gives me three findings. ||| This is the point where people give up, |
so here's the rule: | read the first one only. || It's about line forty-seven, the line I
changed, | and it says one hash starts a new title, so give it three. || The other two are
about line fifty-five, | which is a record I never touched, | and their advice would
actually make things worse. ||| So I put the hashes back, | and all three go at once. || Fix
the first finding, and then run lint again. |||"

### 9. What clean does not mean

**Screen:** Under the description of Find the Derelict, type a new line:
`# remember to make this scarier`. Save, lint: clean. Hold on the word. Then the "What
clean does not mean" table on the page. Delete the note. Lint: clean.

**Say:** "Now for the honest part. || I leave myself a note, | the way I would in a
manuscript, with a hash in front of it. || And lint says clean. || But in the game, my note
is part of the description the crew reads. ||| In this file, a note starts with two slashes.
||| Clean means every shape is one that lint knows, | every key that's pointed at exists, |
and the story file can be read. || It doesn't mean the mission does what I meant it to. ||
The page has a short list of the things lint can't see. |||"

### 10. The second check

**Screen:** Put four hashes on Derelict Hull. Start the game, take a console. The handheld
icon, the ePADD, Quests, the Quest Log: First Contact in the list. Close the game. Open
`mast.runtime.log`: one line. Fix, lint: clean. Open the log again: the line is still
there. Play again: the quest list. Close. Open both logs: empty.

**Say:** "Lint reads your files, | but it doesn't run them. || So the second check is to
play for a minute, | and then read the logs. ||| Here's that extra hash again, this time in
the game. || The quest list looks fine, | because the game took the hash off for me. || And
here's the log: | one line, with the line number and the fix. || That's exactly what lint
told me before I played, | which is why lint comes first. ||| So I fix it, and lint says
clean. || But the log still has its line in it, | because lint leaves the logs alone. ||
They're the game's notes on my last play. ||| So I play again, and there's my story. || This
time both logs are empty, | and that's what you want to see after every play. |||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now use it on your own words. || Rewrite the three descriptions, and the three
readings, | and after every one of them, save, run lint, and read the count line. || Then
play the mission, and read both logs. ||| Next time, we'll put names to two words you saw in
this file today: | a role, and a signal. |||"
