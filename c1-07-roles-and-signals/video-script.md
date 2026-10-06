# C1-7 video script - Roles and signals

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

Target length: 18 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. The finished files are in `example\`.

> **CHECKED IN THE REAL ENGINE, 2026-10-04** (server, Helm and Science; seven cases; every
> one matched the mock's report). Two of them were run a second time, after the library
> fixes that this lesson's first report caused (sbs_utils `947e3f8a`, LegendaryMissions
> `298ffb3`): the capitals case, and the misspelled-key case, which is new.
>
> - The finished lesson: both steps and First Contact finish within seconds of the ship
>   reaching the hulk; both logs empty. **Seen on Science:** the hulk has three tabs,
>   `scan`, `intel` and `mat`, and `intel` reads "No flight plan was ever filed for this
>   ship. Somebody wanted her forgotten."
> - The role typed FIRST in the hulk's list. **Seen on Science:** the hulk is drawn grey,
>   not in the color of a friendly ship; a `ghost_ship` button appears among the filter
>   buttons; its row in the list reads `Unknown Hulk (tsn)`. The sensors still read it and
>   the quests still finish. The log holds the one `Side not found: [ghost_ship]` line.
> - The signal renamed in the notes only (line 93 still says the old word): Find the
>   Derelict never finishes, and both logs are EMPTY. Not looked at on a console. Lint now
>   reports it (`unfired-signal`).
> - The signal in capitals in both files, `Ghost_Ship_Found`: on the first run Find the
>   Derelict never finished. After the fix it FINISHES (second run). Not looked at on a
>   console.
> - The `"SIGNAL_NAME"` key misspelled on line 93 (`"SIGNAL_NAM"`): Find the Derelict stays
>   active, there is NO error page, and `mast.runtime.log` holds one line: ``Quest: a
>   `quest_signal` was sent with no name, so no quest heard it. The line is
>   `signal_emit("quest_signal", {"SIGNAL_NAME": "the_name"})` ``. Before the fix this was
>   an error page from inside LegendaryMissions (mock only; never run in the engine).
> - No comma between the two roles: the hulk has no text on any tab, Study the Derelict
>   stays active, both logs EMPTY. Not looked at on a console.
> - The exercise: DS 1 gains a `mat` tab with the new reading. Not looked at on a console.
>
> - **A role misspelled on the hulk's line** (`derelect`; the page's Step 8 break), run
>   in the engine with Science: Find the Derelict finishes, Study the Derelict stays
>   active, both logs EMPTY. **Seen on Science:** the hulk is listed as `unknown`, drawn
>   grey, with one tab, `scan`; the panel reads `unscanned contact` and offers
>   `Start Initial Scan`. The ship's sensors did not scan it by themselves.
>
> Still unseen: the Quest Log for these files (it was seen for Lecture 6's), what Science
> shows for a contact with no text or with only an `intel` reading (Step 8's break), the
> error pages, and everything in VS Code.

> **Tool note.** The page is written for an `sbs.pyz` built from sbs_cli `f28e7f1` or
> later, and for sbs_utils `0c4c0fae` or later. The command-line tool is NOT released.
> With the released `sbs.pyz` 0.10 one kind of row on the page is not true: every row that
> says `mast-compile` (a quote mark deleted, added or curly in `story.mast`: 0.10 says
> `clean`, and the story then fails to compile when it is played). Nothing else on the
> page needs the new tool; six states were linted with both and print the same. The
> signal findings come from the library, not from the tool: with the library at `0c4c0fae`
> a note in `story.mast` does not count as a line that sends a signal; a `signal_emit`
> whose first word is not `quest_signal` does not count for a quest; capitals, spaces and
> hyphens in a signal are not findings; and `Done when: signal` with no word is
> `signal-no-name`. On an older library the signal table in Step 7 is wrong in both
> directions.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 5 leaves it: the `amd` template, the reworded First Contact, and the **Derelict Intel** record. `mission.amd` must match `c1-05-the-shape-of-a-record\example\mission.amd` line for line, or the line numbers 28 and 64 on the page are wrong |
| `story.mast` | The local, fixed `amd` template's (starter repo `60c30bc`), never edited. The line numbers 64, 66 to 68, 86, 87, 93, 100, 103 and 104 on the page depend on it. `sbs create` still downloads an older one |
| Library | sbs_utils `0c4c0fae` and LegendaryMissions `298ffb3`, as released and built into `__lib__`. Lint was run again on those for every variant; the game for the signal rows that moved and for the finished files |
| `sbs` | 0.12 or later: `sbs version` prints the number, `sbs update` fetches the newest |
| VS Code | The mission folder open. `mission.amd` and `story.mast` both open in tabs, font size raised. The search panel closed, with Match Case, Match Whole Word and the regular-expression button all OFF, so turning two of them on is seen |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Command prompt | Open in `data\missions`, cleared, wide enough that one finding fits on two lines |
| Game | Closed. It is started on camera in scene 10, as the server with a Helm and a Science console |

## Confirm on camera

What was checked, and how. "Lint" means the command-line tool run from source (sbs_cli
`f28e7f1`) on the Lecture 5 files with that one change, on 2026-10-04. "Mock" means the
mission was then played headless with the packaged library (sbs_utils `947e3f8a`): a probe
read every object's side and roles, put the ship 1500 from the hulk so that the template's
own watcher had to send the signal, sent the `science_auto_scan` signal the library sends
when the engine's sensors scan a contact, and read the quest states and the text on each
Science tab. 160 variants, one at a time: the 133 of the first pass run again on the fixed
tools, and 27 new ones. At sbs_utils `0c4c0fae` all 160 were linted once more (149 answer
the same; the 11 that moved are the signal rows the fix was for), and the game was run
again for those rows and for the finished files. What ran in the real engine is in the
block at the top of this file; nothing else has, and nobody has seen the quest list for
these files or anything in VS Code.

1. The two findings in Steps 4 and 5, word for word, with `line 64` and `line 28:19`; and
   `clean` after each mend. (Lint, source and installed 0.10: identical.)
2. `clean` after only line 93 is changed, and again after the two notes. (Lint. Mock: Find
   the Derelict finishes.) With line 93 NOT changed and the notes changed, lint says
   `unfired-signal`: a note no longer counts.
3. The finished files: lint `clean`; the hulk wears `derelict` and `ghost_ship`; tabs
   `scan`, `mat`, `intel` each with text; Find, Study and First Contact complete; both logs
   empty. (Lint and mock, on the files in `example\` as shipped, with CRLF and with LF line
   endings.)
4. Every row of every table in Step 7. (Lint and mock, that exact row, with the page's
   words. Rows that say "error page" are a runtime error in the mock's log at that moment,
   and a failed verdict: the page itself is UNSEEN.)
5. Step 8's break, which is scene 9: `derelict` misspelled in the hulk's list on line 68
   (`"tsn, derelect, ghost_ship"`). Lint says `clean`; Find finishes; Study the Derelict
   appears and never finishes; the hulk keeps only its `intel` text; both logs empty. (Lint
   and mock. NOT in the engine: what Science draws for a hulk with an `intel` reading and
   no `scan` reading is unseen. The page says only that the `scan` and `mat` readings are
   lost. The case is in the probe's `engine_alternates` as `old_role_misspelled`.)
6. Every signal slip the first pass found silent is now reported, except one: two steps
   waiting for one signal. And lint no longer warns about a signal that works: spaces, a
   trailing space, capitals or hyphens. (Lint and mock.)
7. The hulk's roles include `ship`, from its model. (Mock: its roles read
   `derelict, ghost_ship, light, npc, patrol, ship, support, tsn`.)
8. The search counts: `derelict` 8 results in 2 files (3 and 5); `derelict_found` 4 (1 and
   3); `derelict_scanned` 2; after Step 4 `ghost_ship` 2; after Step 5 `derelict_found`
   none and `ghost_ship_found` 4; with the word list `derelict` 9 (4 and 5), and 8 with
   Step 8's break in. (Counted with a whole-word, case-sensitive pattern over the two
   files. NOT counted in VS Code.)
9. VS Code: `Ctrl+Shift+F` opens the search panel; the buttons are drawn `Aa` and `ab`; the
   summary line reads `8 results in 2 files`; clicking a result goes to its line; an
   unsaved file shows a dot on its tab; a search with no hits says so. (Not checked.
   Standard VS Code behavior. If the summary line is worded differently, change the page.)
10. Whether VS Code's search also looks inside `mast.runtime.log` and `mast.compile.log`.
    (Not checked. It should, and both are empty on a clean mission. If a log has lines in
    it from an earlier break, the counts on the page are too low: empty the logs first.)
11. The quest list and the Science tabs in Step 8. (The mock holds the states. The hulk's
    three tabs and its `intel` reading were SEEN on Science for these files. Where the
    quest list is, and that a finished quest shows `Done`, were seen in the Lecture 6
    pilot, on the untouched template: the Quest Log for these files is unseen.)
12. What the crew sees when the role is typed first (`"ghost_ship, tsn, derelict"`). SEEN
    on Science: the hulk is drawn grey. The mock agrees: its side is `ghost_ship`, it is
    not an ally, and `mast.runtime.log` holds one `Side not found: [ghost_ship]` line.
13. The exercise: DS 1 wears `home_port`, has a `mat` tab with the new reading, keeps the
    game's own `scan`, `status`, `intel` and `bio` text; the renamed second signal still
    finishes Study the Derelict. (Lint and mock.)

If item 9 or 11 turns out differently on camera, stop and fix the page.

## Scenes

### 1. Cold open

**Screen:** VS Code's search panel: `derelict`, `8 results in 2 files`, the two file names
with their hits under them.

**Say:** "Here's one word, and it shows up in two files, in eight places. || Until now,
you've only ever written in one of these files. || So today you'll find out what the other
one is doing with your words, | and you'll put two words of your own into both. |||"

### 2. Two files, three promises

**Screen:** `mission.amd`. Highlight the three `Scan of: derelict` lines, then the two
`Done when: signal` lines. Then the table from Step 1.

**Say:** "Your fact sheet says what the story is, | and this other file, story.mast, is what
makes it happen. || And there are five lines in your fact sheet that lean on it. ||| Scan of
derelict is a promise | that something in the game wears the word derelict. || That's called
a role, which is really just a name tag. ||| Done when, signal derelict_found, is a promise
too: | that the story will say derelict_found, out loud, at some moment. || And that's
called a signal. ||| If the other file doesn't keep those promises, | the reading is never
shown, | and the step never finishes. |||"

### 3. Open the other file

**Screen:** Click `story.mast` in the file list. Scroll it once, top to bottom, without
stopping. Then the three rules on the page.

**Say:** "So this is story.mast, | and you're not going to learn to read it today. || You
only need three rules. || Change only what's between quote marks, or in a note. || Never
delete a quote mark, and never add one. || And leave every comma right where it is. ||| One
more thing: a note in this file starts with a hash, | whereas in your fact sheet it starts
with two slashes. |||"

### 4. Find the role

**Screen:** `Ctrl+Shift+F`. Type `derelict`. Turn on `Aa` and `ab`. Point at the summary
line. Click the hit on line 68. Highlight the four quoted pieces one at a time. Then click
the hit on line 103.

**Say:** "Control, shift, F searches the whole folder. || I turn on match case, and match
whole word, | so that I get the role itself, and not every word that happens to have it
inside. || That gives me eight results. ||| Three of them are my Scan of lines. || The other
five are in the story file, | and three of those start with a hash, so they're notes. ||
That leaves just two lines that do any work. ||| This first one puts the hulk in the game.
|| It has four pieces in quotes: | the name the crew sees, then a list, | then the model,
and then how it behaves. || The list is the part that's ours. || Its first word is the side,
| and every word after that is a role. || So the hulk is on our side, and it wears derelict,
| which means that promise is kept. ||| And here's the word a second time, | in a line that
asks: when Science scans something, does it wear derelict? |||"

### 5. Find the signals

**Screen:** Search `derelict_found`: 4 results. Click line 93. Highlight `"quest_signal"`,
`"SIGNAL_NAME"`, then `"derelict_found"`. Search `derelict_scanned`: 2 results. Show line
104 under line 103.

**Say:** "This search gives me four results. || One is in my fact sheet, | two are in a
note, | and one is a working line. ||| That line has three pieces in quotes, | and only the
last one is mine. || The first two, quest signal and signal name, are fixed: | touch either
of them, and no quest hears anything. || The lines above it decide when the signal is said,
| which is when a ship comes within two thousand of the hulk. | I don't need to read those.
||| The second signal is said down here, | straight under the question about the role. |||
And one more thing: | a signal is said once, | so a step that hasn't started yet has missed
it. |||"

### 6. Name a role

**Screen:** In `mission.amd`, Derelict Intel: `Scan of: ghost_ship`. `Ctrl+S`. Lint: the
`role-nothing-wears` warning. Then `story.mast` line 68: click before the closing quote,
type `, ghost_ship`. `Ctrl+S`. Lint: `clean`.

**Say:** "In my story, this hulk is a ghost ship. || And I'm going to do this in the wrong
order, on purpose. || First I point my reading at a role that nobody wears. || Lint has read
both files, | and it tells me nothing in this mission wears a role called ghost_ship. || If
I played it now, my reading would simply be gone. ||| So now I keep the promise, on line
sixty-eight. || I click just before the closing quote, | and I type a comma, a space, and
the word, and nothing else. || And it's clean, and the hulk wears two roles now. ||| There
are four rules for a role, and they're on the page: | small letters and underscores, | the
same spelling in both files, | one thing and not many, | and in a list your word goes last,
| because the first word is the side. |||"

### 7. Rename a signal

**Screen:** `mission.amd` line 28: `Done when: signal ghost_ship_found`. Save. Lint: the
`unfired-signal` warning. Search `derelict_found`: 3 results, all in `story.mast`. Line 93:
change the last quoted word. Save. Lint: `clean`. Then lines 86 and 87. Save. Search
`derelict_found`: no results. Search `ghost_ship_found`: 4 results in 2 files.

**Say:** "Now the same again, with the signal. || My step now waits for ghost_ship_found. ||
And lint tells me that Find waits for that signal, | and nothing in the mission sends it, |
so the wait never ends. ||| So I search for the old word, | and there are three left, all in
the story file. || I do the working line first, | changing the last word in quotes, and only
that one. || And now it's clean. ||| Then I change the note, so that the note stays true, |
because lint doesn't read a note, and neither does the game. ||| And now I count. || The old
word gives me nothing, | and the new word gives me four. ||| Remember that counting, because
in two minutes you'll see why it matters. |||"

### 8. The word list

**Screen:** Under the title line of `mission.amd`, type the five `//` lines. Save. Lint:
`clean`.

**Say:** "By now I know every word these two files share, | so I write them down where I'll
see them. || That's two roles and two signals, | and where each one comes from. || Every
line starts with two slashes, | so the game skips them, and this list is just for me. |||
When there are thirty of these words, | it's how I'll spell the thirty-first the same way
twice. |||"

### 9. What lint cannot see

**Screen:** In `story.mast` line 93, change `ghost_ship_found` to `ghost_ship_fond`. Save.
Lint: the `unfired-signal` warning. Put the word back. Then line 68: change `derelict` to
`derelect`. Save. Lint: `clean`. Hold on the word. Search `derelict`: 8 results, where 9
are wanted. Put the word back. Then the "What lint cannot see" table on the page.

**Say:** "Now for the honest part. || First, a signal: I misspell it on the working line, |
and lint catches it, even though my fact sheet is fine. || That's because for a signal, |
lint looks for the line of the story that sends it. ||| Now a role: I misspell derelict in
the hulk's list, | and lint says clean. || And here's why that is. || For a role, lint only
looks for the word between quote marks, somewhere in this file, | and it found derelict down
here, on line one hundred and three. || It doesn't ask whether the word is in a list of
roles. ||| In the game, the hulk has lost two of its readings, | and the second step never
finishes, | and nothing says so. ||| The count does catch this one: | I get eight, and I
wanted nine. || The page lists the rest, | and the two to learn are that your role goes last
in the list, | and that it goes after a comma. |||"

### 10. Play it

**Screen:** Start the game as the server with Helm and Science. Helm: the quest list. Fly
to the hulk. Find the Derelict shows `Done`. Study the Derelict appears, then `Done`.
Science: select the hulk, the three tabs, open `intel`. Close the game. Open both logs:
empty.

**Say:** "The crew never sees a role or a signal. | They only see what those words connect.
|| So, Find the Derelict is done, | and that was my signal: | the story said
ghost_ship_found, and my step was waiting for it. || The sensors scan the hulk by
themselves, | so the second step finishes too. ||| And on Science there are three tabs, |
and intel is the one that's hanging on my role. || And both logs are empty. |||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's time for your own words. || Give the station a role, | and a reading on
its mat tab. || Then rename the second signal, in both files, | and add both to your list.
||| Next time it's your first quest: | a line that names a role, | and the game does the
watching itself. |||"
