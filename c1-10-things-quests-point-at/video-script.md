# C1-10 video script - Things quests point at

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
> a point, read what the game had scanned by itself, then asked for a full scan, and wrote
> what it found to a file. The ship was never flown, and nobody has SEEN any of it on a
> screen).
>
> - An object named The Lifeboat exists at `6000, 0, 6000`. It is a wreck with no side,
>   and it wears the role `lifeboat`.
> - The ship scans by itself. Near the hulk, with nobody at Science, the hulk had every
>   tab it then had text for (`scan`, `mat` and `bio`), each with one of the lesson's
>   readings. Near the lifeboat, the lifeboat had its `scan` tab filled and NOT its
>   `intel` tab: the `intel` reading appeared only after a full scan.
> - 300 from the hulk: Close Inspection and Quick Work complete, Find the Lifeboat becomes
>   active, Bring the Log Home stays hidden. Study the Derelict completes by itself, from
>   the automatic scan.
> - 300 from the lifeboat: Find the Lifeboat completes and Bring the Log Home becomes
>   active.
> - 600 from DS 1: the game ends carrying the `Win:` sentence, the side has 450 credits,
>   and `mast.runtime.log` is empty.
>
> That run used the first version of this lesson's files: the template of that day plus
> Lecture 9's arc. The five records this lecture adds (the bio record, the two lifeboat
> scan records, The Lifeboat, and the step Find the Lifeboat) have not changed since.
> The hulk's fourth tab, `intel`, comes from Lectures 5 and 7 and was not in that run.

> **Re-measured 2026-10-04 (night). Not run in the engine again.**
>
> - Library: the packaged one in `__lib__`, built at 21:16 from sbs_utils `2c7d93d1` and
>   LegendaryMissions `b20726f`. Every mock run used it. Lint reads the working tree,
>   which was at the same commits. While the pass ran, sbs_utils moved to `d8c971c8`: two
>   commits, three files, all documentation. No library code changed and `__lib__` was
>   not rebuilt, so nothing was run again. Starter template `60c30bc`, which is what
>   `sbs create -t amd` downloads now.
> - **The lesson now starts from Lecture 9's finished files**, read from
>   `c1-09-chains-and-trees\example\` (both files), not from the untouched template.
>   `example\` here is those two files with this lecture's steps typed in. `story.mast`
>   is Lecture 9's, byte for byte. So the hulk already has three tabs when the lecture
>   starts (`scan`, `mat`, and `intel` on the role `ghost_ship`), the new tab is its
>   fourth, and the student's word list at the top of the file gets one line.
> - 129 variants: Lecture 9's files untouched, each step in turn, the finished files, and
>   one change to the finished files at a time. Each was linted with the installed
>   `sbs.pyz` (129 lint runs, after a first lint-only pass of 102) and, where the page
>   says what the game does, played headless with the packaged library, one at a time
>   (134 mock runs).
> - Every line of tool output printed in a code block on the page was checked against
>   those runs by a script (`c110r\verify_page.py`): 11 lines, all found. Every row of
>   the Step 6 tables is tied to the run that measured it by a second script
>   (`c110r\rows.py`): 57 rows, 75 variants, 124 tests on the probe's own lines. The
>   codes in a row are the codes lint printed, and a row under "What lint cannot see" or
>   "These are fine" was `clean` in every one of its runs.
> - The finished file with the exercises of Lectures 8 and 9 typed in, and again with
>   those of Lectures 5 and 7, lints clean and plays the same (measured).
> - What changed against the page of 2026-10-03. The tables are rebuilt as mistake, game,
>   code, every row measured again. `Tab: life` is one finding, not two. A reading typed
>   above the closing fence costs that one line, not the record. A landmark typed with
>   four hashes no longer loses the whole file: it is placed, and the log gets one line.
>   A landmark with no `Kind:` line does NOT wear the role `station` with the lesson's
>   art, whatever lint's sentence says (the old page said it did). `never-revealed` now
>   fires in the middle of Step 5, and the page prints it. Most rows of "What lint
>   cannot see" are new, among them one hash on The Lifeboat and `Loc: 6,000, 0, 6,000`.

> **Tool note.** The page needs an `sbs.pyz` built from sbs_cli `f28e7f1` or later. The
> one installed here was built from that commit today. It still prints version `0.10`,
> the same as the released one; a release as `0.11` is pending. Every finding on the
> page comes from the library, not from the tool: nine states of this lesson were linted
> with the `sbs.pyz` kept from before 2026-10-04 and with the installed one, and all
> nine print the same. One thing on the page does come from the tool. The page sends the
> student to `mast.runtime.log` after a play, and the released 0.10 empties both logs
> every time lint runs (from the list of fixes; not measured here). The library has to be
> `2c7d93d1` or later for `never-revealed` to fire in Step 5. Before that commit the rule
> took the key anywhere in the file for a reveal, and the new step's own description
> ends "Find the boat." (From the commit's message; not measured with the older library.)

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 9 leaves it. `mission.amd` must match `c1-09-chains-and-trees\example\mission.amd` line for line (119 lines, ending with the Derelict Intel reading), or the line numbers 75, 77, 146 and 153 on the page are wrong |
| `story.mast` | Lecture 9's, which is Lecture 7's finished file. It must contain the line `landmarks_spawn(amd_section(MISSION_DOC, "landmarks"))`. A mission made with `sbs create -t amd` has it (starter repo `60c30bc`, pushed). Without it nothing is placed, and lint says so: `section-not-loaded` on the `## [Landmarks](landmarks)` line itself (measured). Opened in scene 2 only, to point at one line |
| Files touched | `mission.amd` only |
| Library | sbs_utils `2c7d93d1` or later and LegendaryMissions `b20726f` or later, BUILT into `data\missions\__lib__` |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, `story.mast` in a second tab for scene 2, font size raised |
| Command prompt | Open in `data\missions`, cleared, wide enough that one finding fits on three lines |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Science console |

## Confirm on camera

What was checked, and how. "Lint" means the installed `sbs.pyz`, run from `data\missions`
on a copy of the files with that one change. "Mock" means the mission was then played
headless with the packaged library, and a probe put the ship 300 from the hulk, then 300
from the lifeboat, then 600 from DS 1, sent the signal the game sends when the ship's own
sensors scan a contact, then had Science scan every tab, and printed every object, every
quest's state, the side's credits and what Science would be shown. "Engine" is the run of
2026-10-03 in the note above. Nobody has SEEN any of it on a screen. If an item fails
while recording, stop and fix the page.

On Lecture 9's files, before a line is typed:

1. Lint is `clean`. The hulk has text on three tabs, `scan`, `mat` and `intel`. (Lint,
   Mock.)

On the lesson's steps, typed in order:

2. Lint is `clean` after Step 2, Step 3 and Step 4, and after Step 5. (Lint.)
3. In the middle of Step 5, with Find the Lifeboat typed and Close Inspection's `Then:`
   line not yet changed, lint prints the `never-revealed` line on the page, word for
   word, with `line 75`. (Lint.)
4. Following the page's steps in order, typing each block as printed, gives
   `example\mission.amd` byte for byte. (A script, `c110r\steps.py`.)

On the finished `mission.amd`:

5. An object named The Lifeboat is at `6000, 0, 6000`. It is scenery with no side, and
   wears the role `lifeboat`. (Mock, Engine.)
6. At the start Salvage Run, Close Inspection and Quick Work are active, and Find the
   Lifeboat and Bring the Log Home are hidden. The Quest Log call returns Salvage Run
   with Close Inspection and Quick Work under it. (Mock.)
7. 300 from the hulk: Close Inspection and Quick Work complete, the side has 150 credits,
   Find the Lifeboat becomes active and is listed. (Mock, Engine.)
8. The ship's own scan of the hulk fills `scan`, `intel`, `mat` and `bio`. (Mock. Engine
   for `scan`, `mat` and `bio`.) Asked thirty times, the hulk's `bio` tab gave each of
   the three readings (10, 12 and 8 times). (Mock.)
9. 4000 from the lifeboat, and 600 from it, Find the Lifeboat does not complete. At 450
   it does. Going to the lifeboat BEFORE the hulk finishes nothing. (Mock.)
10. 300 from the lifeboat: Find the Lifeboat completes, the side has 250, Bring the Log
    Home becomes active. The ship's own scan fills the lifeboat's `scan` tab and not its
    `intel` tab. `intel` appears after Science scans every tab. (Mock, Engine.)
11. 600 from DS 1: the game ends carrying the `Win:` sentence, with 450 credits, and both
    logs are empty. (Mock, Engine.)
12. `example\`, copied into a fresh mission as delivered: lint `clean`, and the same play.
    (Lint, Mock.)
13. The exercise: a second wreck with its own role is placed, its `scan` tab has two
    readings, the extra step does not complete 4000 away and does 300 away, pays its
    reward, and the game is still won without it. (Lint, Mock.)
14. On a copy that differs only in a time (`Fails when: 6 seconds` on Quick Work): the
    bonus fails and the story is won with 400 credits. (Mock.)
15. Every row of the three tables in Step 6, of "What lint cannot see" and of "These are
    fine". (Lint and Mock, one variant at a time. `c110r\rows.py`.)
16. Deleting the `Roles:` line prints the three `role-is-a-key` lines on the page, word
    for word, with lines 77, 146 and 153. (Lint.)

Not checked, and to watch for while recording:

1. Any screen: the Science console, how a tab is opened, how a scan in progress looks,
   whether the lifeboat's name is drawn on the map, what the `wreck` art looks like.
2. Whether Science can select a wreck at all. LegendaryMissions ships scan text for its
   own wrecks, which suggests it can.
3. A role with no `scan` tab in the real game. In the mock the ship's own scan had
   nothing to show, and the `intel` reading appeared when Science scanned every tab. The
   page says so, as a test result.
4. A misspelled `Art:` word. The mock places the object anyway. The real game may not.
   The page says it is not known.
5. A landmark with no `Kind:` line. The mock makes it with a station's behavior and the
   wreck's art, and the story still plays. What that looks like, and whether it can be
   docked with, nobody has seen.
6. The `scan` verb in the real game. In the mock a `Done when: scan 1 lifeboat` step
   completes on the ship's own scan, and a scan made before the step was revealed did not
   count. Whether the real game scans the same contact a second time by itself was not
   measured. The page tells the student to use `reach`.
7. Where the crew starts when a second station is on its side. In the mock the start
   point moved beside the new station. Not seen in the engine.
8. The time. From the start point the mock gives the ship, the trip is about 11500 to the
   hulk, 6700 on to the lifeboat and 8500 home: about 26700. At full impulse (180 a
   second, from the library's notes on speeds measured in the engine) that is about two
   and a half minutes, well inside the ten. Quick Work's two minutes: the hulk is about a
   minute away at full impulse. Neither was flown.

## Scenes

### 1. Cold open

**Screen:** The game. The Science console, the hulk selected, a tab open with the line
about the plant in a pot.

**Say:** "That sentence isn't the game's. || I wrote it, in a text file, | and it took me
about a minute. || Today you give the game two things to point at: | some words for Science
to find, | and a place on the map that wasn't there before. |||"

### 2. The idea: point at a role

**Screen:** `story.mast`, line 68, the line with `Unknown Hulk`. Highlight
`tsn, derelict, ghost_ship`. Then `mission.amd`, the line `Done when: reach derelict 500`.
Then `Scan of: derelict`.

**Say:** "You know these words already. || In Lecture 7 you gave the hulk a role of your
own, | right here in this list. || And in Lecture 8, your quest said reach derelict. || A
quest never names an object. | It names a role, and the game finds whatever wears it. |||
Scan text works the same way: Scan of, derelict. || Until now, a role always came from this
file, the script. || Today you place a thing yourself, | and you give it its role in your
own file. ||| So it's one idea: give a thing a role, | and then point at the role. ||"

### 3. The scans you have

**Screen:** `mission.amd`, the Scans section. Scroll past the three records. Point at
each `Scan of:` and `Tab:` line.

**Say:** "There are three records here. || Two came with the template, | and the third is
yours, from Lecture 5. || There's Hull, on the scan tab, Materials, on the mat tab, | and
Intel, on the role you added. || There are five tabs in all: | scan, status, intel, mat, and
bio. || Each line that starts with a percent sign is one reading, | and there are two lines
here, so the game picks one. ||"

### 4. A tab of your own

**Screen:** Below Derelict Intel, type the Derelict Life Signs record. Save. Lint:
`clean`. Then show the five rules on the companion page.

**Say:** "The hulk has three tabs, | so I'm going to give it a fourth, called bio. || It's
the same role, a different tab, | and this time three readings. ||| There are five rules for
scan text. || One reading is one line, | because if I press Enter in the middle, I've made
two readings, | and the crew gets half a sentence. || One role, spelled the way the hulk
wears it. || One record for each role and tab. || Always write a Tab line. || And no curly
brackets, at all. ||| Lint checks the first four. || The fifth it can't check, | because
curly brackets are a real feature you haven't met yet, | so the game just shows them as you
typed them. ||"

### 5. A place of your own

**Screen:** The end of the file. Type the note, the `## [Landmarks](landmarks)` line and
The Lifeboat record. Highlight `(landmarks)`. Then each of the four lines in turn. Show
the Kind, Art and Loc tables on the companion page. Then scroll to the top and add the
`lifeboat` line to the word list. Save. Lint: `clean`.

**Say:** "Everything on the map so far came from the script file, | but this one is mine. ||
It's a new section, with two hashes, | and its key is this word: landmarks. || Then comes a
record, | and its name is the name the object gets. || Kind says what sort of thing it is: |
a wreck, a ship, or a station. || Roles is the label it wears. || This is the line lint has
been telling you about since Lecture 7, | and it's the line that matters, | because it's the
word everything else points at. ||| Art is what it looks like. | Lint can't check that word,
so copy it. || And Loc is where it sits: | three numbers, in plain digits, | with no comma
inside a number. || The station is at zero, zero, zero, | and the hulk is at zero, zero,
nine thousand. || The middle number is height, so leave it at zero. || Mine goes here, off
to one side. ||| And then one line in my word list, | so that the list stays true. ||"

### 6. Words for the lifeboat

**Screen:** Back in the Scans section, type the two lifeboat records above the Places
note. Save. Lint: `clean`.

**Say:** "The lifeboat wears a role, | so it can have scan text: Scan of, lifeboat. || A
scan tab comes first, always, and then intel. || And that's the whole trick: | the place and
the words never mention each other. || They both mention the role. |||"

### 7. Point the story at it

**Screen:** The Quests section. Type Find the Lifeboat below Close Inspection. Save. Lint:
the `never-revealed` warning, line 75. Then change Close Inspection's `Then:` line to
`salvage/boat`. Save. Lint: `clean`. Highlight `reach lifeboat 500`.

**Say:** "Now for the story. || I add a new step, between the hulk and home, | and it's
revealed, like last time. || I run lint before I go on, | and it says the step waits to be
revealed, and nothing reveals it. || You saw that one in Lecture 9. || So I make one change
up here: | Close Inspection now reveals the boat, and not home. || And it's clean, so the
chain runs hulk, boat, home. ||| Now look at this line: | Done when, reach, lifeboat, five
hundred. || That's a verb, a role, and a distance. || It's the role, from the Roles line,
and not the name. || I gave the key the same word on purpose, | and the next scene shows
why. ||"

### 8. Lint

**Screen:** The command prompt. Delete the `Roles:` line, lint: three `role-is-a-key`
warnings, lines 77, 146 and 153. Undo. Change `Tab: bio` to `Tab: life`, lint: one
warning, `unknown-scan-tab`. Undo. Change `Scan of: derelict` to `Scan of: derelicts` on
the new record, lint: nothing wears a role called `derelicts`. Undo. Delete the `Loc:`
line, lint: placed at zero, zero, zero. Undo. Change the section key to `places`, lint:
nothing in this mission reads a section keyed `places`. Undo. Lint: `clean`.

**Say:** "This is the one to remember. || I take out the Roles line, | and I get three
warnings, | one for every line that pointed at the role. || Each one says the same thing: |
lifeboat is the landmark's key, | and this line looks for a role. || The key in the round
brackets is not a role. ||| So I put the line back. || Next, a tab that isn't one of the
five, and lint tells me. || Then a plural: nothing wears a role called derelicts, | and that
tab would never have appeared. || With no Loc line, the lifeboat would be sitting inside the
station. || And for a section the story never asks for, | lint reads the story too, | and
tells me which keys it does ask for. ||| There are two things it can't see, and they're on
the page: | one hash on the lifeboat's heading, | and a comma inside a number. || Check
those two by eye. ||"

### 9. Play it

**Screen:** Server, Helm and Science. The Quest Log: the handheld icon, then Quests. Fly
to the hulk. Science: select the hulk, open the tabs. Find the Lifeboat is in the list.
Fly to the lifeboat. Science: select it, open its tabs. The step shows `Done`. Fly home.
The game ends.

**Say:** "The Quest Log has two steps showing, | so it's out to the hulk. || Close
Inspection is done, and there's the new step, Find the Lifeboat. || At Science I select the
hulk, | and there's my fourth tab, with one of my three readings. || Now for the lifeboat, |
which is on the map because I wrote four lines. || At Science again, I pick the boat off the
map, | and those are my words on its scan tab. || Its intel tab is one that Science has to
scan for, | and then that's mine too. || In we go, and the step is done. || Then it's home,
and that's the win. ||"

> Say what the screen actually shows about scanning. If the hulk's tabs are already filled
> before Science does anything, say so: the ship scans what is in range by itself. If the
> lifeboat's `intel` tab is empty until Science scans it, say that too: the lifeboat is on
> no side, so the ship's own sensors fill only its first tab.
>
> Seen in the real game on 2026-10-05 (probe: the lifeboat put 1500 off to one side): the
> hulk's four tabs were filled with nobody at Science; the lifeboat is a white icon on
> Science's map with no name drawn and was not in the contact list, and clicking it selects
> it; its `scan` tab was filled; its `intel` tab showed a `Start Intel Scan` button, and the
> reading came after it was pressed. The Say block above says so.

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn: place a second thing of your own, | give it a role, and give
the role some words, | and add a step the crew can take or leave. || Next time, we open the
script file. ||"
