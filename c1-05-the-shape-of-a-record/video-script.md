# C1-5 video script - The shape of a record

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

> **WRITTEN FOR A TOOL THAT IS NOT RELEASED YET.** The page and this script are written
> for sbs_utils `v1.4.0` at `0c4c0fae` or later (released) and for an `sbs.pyz` built from
> sbs_cli `f28e7f1` or later (NOT released). Three things on the page need that `sbs.pyz`:
> the row "`mission.amd` deleted, renamed, or saved as `mission.amd.txt`"
> (`amd-file-missing`: the released tool prints nothing for it); the two `not checked:`
> lines in Step 7; and the last row of "If something goes wrong", which sends the student
> to `mast.runtime.log` (the released tool empties that file each time it lints). Every
> other line of lint on the page comes from the library, and the released `sbs.pyz` prints
> it letter for letter (compared on seven of the files, 2026-10-04, at both commits).
>
> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script).** The reworded body
> of First Contact is in the quest list's pane, and the new `intel` record is what Science
> has for the hulk. ONE DIFFERENCE from the mock: 2500 from the hulk the engine had filled
> `scan`, `intel` and `mat` by itself, before anything asked for a scan. `mast.runtime.log`
> empty. Nothing was looked at on a console.
>
> **Changed since this script was written (sbs_utils `ea55cd20`, not yet released when this
> note was written):** a question mark in a key and a file saved as UTF-16 no longer lose
> the whole file; both are read. The page's rows are updated. The INSTALLED `sbs lint`
> still empties `mast.runtime.log`; the fix needs the next `sbs.pyz` (CLI `801a5bb`, not
> pushed), so "read the log before you run lint" stays on the page for now.
>
> **Re-measured 2026-10-04, afternoon (sbs_utils `6103ee7d`, sbs_cli `2d84ffd`).** The
> library and the tool were fixed in answer to this lesson, so every row of the page was
> measured again: 192 variants, each linted with the command-line tool run from source
> and each played once in the mock with the packaged library. This supersedes the
> last sentence of the note above: the page no longer says "read the log before you run
> lint". What moved out of the `clean` table and now has a finding: a heading with no
> space after the hashes, a space before them, or no square brackets (`broken-heading`);
> one hash on a record in the middle of the file (`heading-level-jump`); a missing
> opening `---` or a sentence above the fence (`fence-not-opened`); ONE fence line typed
> as `--`, `***` or a long dash (`fence-shape`); one field indented (`field-indented`);
> a field typed twice (`repeated-field`); a key renamed under a `Then:` line
> (`dangling-reveal`, with the line to type). What the GAME now does differently: five
> hashes, a record above the sections and a record with one hash too many no longer lose
> the file; a missing closing `---` costs one record its text and leaves the next record
> alone; a note with spaces or a tab in front of it is skipped; `(Scans)` is read as
> `scans`; curly quotes, long dashes and accents are drawn as plain characters.
>
> **Re-measured again 2026-10-04, evening (sbs_utils `947e3f8a`, sbs_cli `f28e7f1`,
> LegendaryMissions `298ffb3`).** The tools were fixed again in answer to the afternoon's
> report, and all 204 variants were linted and played again. What the game holds is the
> same in every one of them. What lint says changed in these rows of the page: BOTH fence
> lines typed wrong (`fence-shape`) or both left out (`fence-not-opened`), which were
> `clean`; the last record's fence left open (one error, was two); a wrong closing line
> (one error, was two); an empty file (`no-headings` is an error, was a warning); the
> sentences of `duplicate-key`, `field-indented` and `unknown-scan-tab`; a capital in a
> step's key (a second warning, `never-revealed`). New row: the hashes left off a
> heading. One thing got worse that evening: a field typed below the closing `---` got a
> `fence-not-opened` error that was not true, beside the `field-below-fence` warning that
> was. It was fixed the same night (next note).
>
> **Third pass 2026-10-04, night (sbs_utils `0c4c0fae`; sbs_cli and LegendaryMissions as
> in the evening).** The evening's own defects were fixed. All 205 variants were linted
> again and five answers moved, each one explained: the untrue `fence-not-opened` error
> on a field below the closing `---` is gone (that row is back to `field-below-fence`
> alone); `duplicate-key` on a scan record no longer says the game keeps the first; a
> long dash as the closing line is quoted as typed. Spaces round the slash in a `Then:`
> line now reveal the step (played in the mock), and the page lists that as fine.
>
> **Still lint-clean and wrong (measured in the evening, the same at night; each is a
> lint gap):**
> one hash on the LAST record of the file; `Scan of: "derelict"` with plain quotes; a
> plain line below the last reading with a blank line between; a `#` line above the first
> reading; `---` between two scan records; a `#` note or a one-slash `/` note in or under
> a quest's body; a `//` note on the end of a sentence or a reading; `%` in front of a
> quest's sentence; `- ` in front of a reading; a body line that starts with `= `.

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | A fresh mission from the `amd` template, nothing edited. Its `mission.amd` has eight headings and its last line is the Derelict Materials reading |
| Starter template | The local, fixed one (`mast_starter\templates\amd`, starter repo `60c30bc`). `example\story.mast` is that template's file, unchanged |
| Library | sbs_utils `v1.4.0` at `0c4c0fae` or later, LegendaryMissions `298ffb3` or later. Every row on the page was measured on those |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` folder open, Artemis AMD extension installed, `mission.amd` in one tab, font size raised, word wrap off so a long line stays one line |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 11 with a server, a Helm console and a Science console |

## Confirm on camera

Seen in the real engine on 2026-10-04, with the template's mission or with one change to
it. These may be said as fact:

1. Where the quest list is. On any console, the handheld icon at the top, beside the crew
   member's name, opens the ePADD, and **Quests** opens the **Quest Log**. The list is on
   the left. Selecting a quest shows `State` and its text on the right. A finished quest
   shows `Done`.
2. The engine scans the hulk by itself once the ship is near. Both of the template's
   steps finish within seconds of arriving, and First Contact then shows `Done`.
3. On Science, selecting the hulk in the list on the right shows tabs `scan` and `mat`
   and one of the readings.
4. Curly quotes in a quest's description are drawn as plain `"` and `'` (seen on Helm).
5. Four hashes on Derelict Hull: all three quests are there, the hulk has both tabs and
   both readings, and `mast.runtime.log` holds one line that starts `AMD error: line 47`.
6. The closing `---` of Derelict Hull deleted: Derelict Materials is untouched, the hulk
   has no `scan` text, and the log holds one line that starts `AMD error: line 48`.
7. An arc's key renamed with the `Then:` line left alone: Find the Derelict finishes,
   Study the Derelict stays hidden, and the log names `first_contact/study`.

Checked on 2026-10-04 in the mock, by a probe that calls the game's own functions and
prints what they return. For items 5, 6 and 7 above the mock gave the same result and the
same log line, letter for letter.

8. The quest list is given a line named First Contact, a second line that reads Active,
   and, for the pane beside it, the new sentence followed by a list of its steps.
9. The hulk has readings on three tabs, `scan` (two), `mat` (one) and `intel` (one), and a
   full scan leaves the lesson's sentence on `intel`.
10. Changing a quest's name changes the line in the list and nothing else. After the first
    step is finished, the second still appears.
11. Every row of the page's tables: lint with the command-line tool run from source, and a
    headless run of that exact file with the packaged library. 204 variants in all: 201
    files with one change each, linted with Windows and with plain line endings (the
    answers were the same), and three changes to the folder (`mission.amd` deleted,
    renamed, saved as `.txt`). That was at sbs_utils `947e3f8a`. At `0c4c0fae` every
    variant (205 by then) was linted again, and only the files whose answers moved were
    played again.
12. The page's steps, typed in order on the template, give `example\mission.amd` byte for
    byte (by script). The example, with no probe in it, lints clean and runs (`labels
    59/422`, PASS) with an empty `mast.runtime.log`.
13. The exercise, all four parts in one file: lint clean, a `status` tab with its reading,
    three hull readings, the new title in the list.
14. Lint leaves `mast.runtime.log` and `mast.compile.log` as they were (a line written
    into each was still there after a lint run).

NOT checked. If one is not as described, stop and fix the page:

15. The `intel` tab on a real Science console. A script read the text out of the engine;
    nobody has looked at the tab.
16. The squiggly underlines in VS Code. The page says there should be none for a correct
    file. What the extension draws for each mistake was never looked at. The same goes
    for `Ln` and `Col` at the bottom of the window matching lint's two numbers.
17. How a long dash, the joined three dots, an accented letter or an emoji is drawn. Only
    curly quotes were seen. The mock holds `-`, `...`, the bare letter and nothing.
18. Whether a word processor on the recording machine really turns three hyphens into a
    long dash. Try it once before scene 9, and say what it did.
19. What a crew sees when the game found no sections (the title line deleted, or an empty
    file), and when `mission.amd` is missing. In the mock the first two give no quests and
    no readings (the deleted title leaves one `AMD error:` line in the log, the empty file
    leaves nothing), and the third stops at the line of the story that asks for the file.
20. What a `---` line, or a line that starts with `#`, looks like in a quest's
    description. The mock holds the line as typed. The Quest Log may draw it as a rule or
    as a large heading.
21. Whether the two `not checked:` lines appear on the recording machine. They appear on
    a machine that has never run `sbs debug`. Say on camera which it is.

Also capture the screenshot for the top of the page.

Scene 10 shows one mistake that lint calls `clean` today: one hash on the last record of
the file. It is reported as a lint gap. (The scene first used two hyphens on both fence
lines. Lint learned that one the same day.) If lint has learned this one by recording
day, show what it says instead, move that row on the page out of the `clean` table, and
take another row from that table for the scene: a blank line and then
`TODO: write the lifeboat next.` at the end of the file is the next best.

## Scenes

### 1. Cold open

**Screen:** The Science console. The hulk selected, the `intel` tab open, one sentence on
it.

**Say:** "I wrote that sentence. || It's one of six lines in a text file, | and those six
lines have a shape, | the same shape as every quest, every person and every place you'll
write in this course. || So today, we learn that shape once. |||"

### 2. The file

**Screen:** VS Code, `mission.amd`, top of the file. Scroll slowly to the bottom and back.

**Say:** "This is the file your story lives in. || The lines at the top start with two
slashes, | which makes them notes, and the game skips right over them. || Everything else in
here is a record, | and a record is simply one thing in your story. ||| There are five of
them in this file right now, | and by the time we finish today there'll be six. |||"

### 3. Eight headings

**Screen:** Put the cursor on each line that starts with a hash, top to bottom. Pause on
`## [Quests](quests)` and on `#### [Find the Derelict](find)`.

**Say:** "Start by finding the hashes. || There are eight lines that begin with one, | and
every one of those lines is a heading. ||| They all have the same shape: | some hashes, then
a space, | then a name in square brackets, | and then a key in round brackets. || That's the
link you learned in Lecture Four. ||| Now, the hashes tell you what's inside what. || One
hash is the title of the whole file. || Two hashes make a section, | which is a drawer for
one kind of record. || Three hashes make a record, | and four make a record that sits inside
the record above it. ||| So these two, with four hashes each, | are the steps of First
Contact. |||"

### 4. One record, three parts

**Screen:** Select the heading of Find the Derelict. Then select from the first `---` to
the second. Then select the body line.

**Say:** "Let's take one apart. || The heading gives it a name. | Then comes what I'll call
the fence: | two lines of three hyphens, and everything between them. || Inside the fence
there's one fact on each line, | a label, a colon, and a value. | Those are fields, and
they're what the game acts on. || Below the fence is the body, | which is just a sentence
for people to read. ||| So that's heading, | fence, | body. ||| You don't need to know what
these four fields do yet, | but have a look at the last one. || It points at another record,
| and it does that with a key, | because nothing ever points at a name. |||"

### 5. Two more

**Screen:** First Contact, with `Arc` highlighted. Then Derelict Hull, with the two `%`
lines highlighted.

**Say:** "Now see if you can find the same three parts here. || One line inside this fence
has no colon, and that's allowed, | because the first line of a fence can be a single word
that says what kind of record this is. ||| And here, in a scan record, | the body is two
lines that each start with a percent sign. || Each of those lines is one reading, | and
Science gets shown just one of them. |||"

### 6. What shows where

**Screen:** The table from step 4 of the page.

**Say:** "A quest's name becomes its line in the quest list, | and its body becomes the
description beside it. || A scan record's name isn't shown anywhere, | because that one's
just for you, | and its body is the reading. ||| And a key is never shown at all, | because
a key is for the game. |||"

### 7. Change the words

**Screen:** Select the body of First Contact. Type the new sentence over it.

**Say:** "Here's the first edit, | and I'm changing the words and nothing else. || It all
stays on one line, however long that line gets, | and I'm not touching the heading or the
fence. |||"

### 8. Write a record

**Screen:** End of the file. One blank line. Type the record one line at a time.

**Say:** "Now I'll write one of my own. || I start with three hashes at the left edge, and
then one space. || Next comes a name, and then a key, | which is small letters and an
underscore, with no spaces. || Then three hyphens, to open the fence. || Inside it I say
whose reading this is, which is the derelict, | and which tab it goes on, which is intel. ||
Three more hyphens close the fence, | and then comes the body, which starts with a percent
sign and stays on one line. ||| So that's six lines in all. || Now notice what I didn't do.
|| I didn't put a space in front of the hashes, | I didn't type anything after the last
round bracket, | and I didn't press the Tab key in front of a field. |||"

### 9. Three ways to break the shape

**Screen:** In the new record, take the space out after the hashes. Hold. Undo. Press Tab
in front of `Tab: intel`. Hold. Undo. Change each `---` to `--`. Hold. Undo. The command
prompt is not used in this scene.

**Say:** "There are three easy ways to get this shape wrong. || The first is leaving out the
space after the hashes. | Then it isn't a heading any more, | and my six lines become six
readings of the record above. || The second is one field pushed in from the edge. | That
glues it to the line above, | and now the reading belongs to nobody. || And the third is two
hyphens instead of three, | which isn't a fence, so there are no fields. ||| In all three
cases the game shows no intel tab, | and it doesn't stop to tell you. || So when your record
isn't in the game, | look at its shape first. |||"

### 10. Check it

**Screen:** No squiggles. Command prompt: `sbs lint MyMission`. Show `clean` and the count
line. Back in VS Code, take two of the three hashes off the heading of the new record, so
that it starts with one, and save. Run the command again: `clean` again. Put the hashes
back, save, and run it a third time.

**Say:** "First I check that there are no squiggles, | and then I run one command. || I'm
looking for a single word, and that word is clean. || The next lecture is all about this
command, | and it would've caught all three of the mistakes I just showed you. ||| There's
one warning until then, though. || If I put one hash where there should be three, | it still
says clean. || That's because with one hash this line is a title, not a record, | so the
game never reads it. ||| Clean only means the checker found nothing, | so count your hashes
yourself. |||"

### 11. Play it

**Screen:** Start the server, Helm and Science. On Helm, click the handheld icon at the
top, beside the crew member's name, then **Quests**. Select First Contact in the list on
the left. Fly to the hulk. On Science, select the hulk in the list on the right and open
`intel`.

**Say:** "I click the handheld, and then Quests, | and this is the Quest Log. || There's my
sentence, right beside First Contact. || Now for the hulk. | The ship scans it by itself
once we're close enough, | so there are three tabs here, | and the second one is mine. |||"

### 12. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Give the hulk a fourth tab, with a record of your own. || Then change the name of
First Contact, | and watch what changes and what doesn't. ||| Next time, we'll break five
things on purpose, | and read what the checker says. |||"
