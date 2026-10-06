# C1-4 video script - Markdown in twenty minutes

> **This is Lecture 4, and that is settled.** It follows "Your editor and your first run"
> (Lecture 3, `c1-03-editor-and-first-run`) and uses VS Code throughout. The folder is
> `c1-04-markdown-in-twenty-minutes`. The three reasons, all from what the lecture
> needs:
>
> - A person meeting markdown has to see what a mark DOES. Notepad shows the marks and
>   nothing else. VS Code has a preview built in, beside the text, with nothing to
>   install.
> - The lecture has to say what the GAME does with each mark, and that is only worth
>   saying to somebody who has a game to look at. After the first run they do (Step 11).
> - The first file a student makes should not come with Notepad's own trap, a file saved
>   as `story-bible.md.txt`. Lectures 5 and 6 already carry a table row for that slip
>   (`mission.amd.txt`).
>
> **SEEN SINCE (2026-10-05, in the real game, by the session that sent the re-measure):**
> Step 11's nine lines in the Quest Log, on Helm, with the story `Find the Derelict`
> selected. `Orders` is a heading in a larger display font. `**drifting**` is shown with
> its stars. The two list lines are indented, each with `- ` in front, in light blue.
> `Her last word was stay.` has lost its backticks. The link is shown as typed, brackets
> and address. There is no gap where the blank lines are. Two extra lines were added for
> the look and both are shown as typed: a line holding only `#` (library `88d1c93e`; the
> day before it replaced the whole text with an error line) and `40 years ago she was
> the pride of the fleet.` Still not seen: VS Code's preview, anything Science draws,
> the caret row.
>
> **NOTHING ON THIS PAGE HAS BEEN SEEN ON A SCREEN** by the session that wrote it or by
> the session that measured it again. Not VS Code, not its preview, not the Quest Log,
> not Science. Neither session started the real engine or opened a window. What the game
> "shows" on the page is what the mock's Quest Log is SENT to draw, and what the game
> holds for Science. The lists below say which is which, and name the few things another
> session reported seeing.
>
> **Measured again on 2026-10-04 (night).** The first measurement of this page found six
> ways the Quest Log lost a writer's words (`40 years ago` drawn as `1. years ago`, a
> line that opened `[Static]` dropped whole, and four more), and that selecting the story
> First Contact showed `Select a quest from the list.` The library was changed for all of
> them (sbs_utils `0d76c0c4`, LegendaryMissions `b20726f`). The page's tables then
> described a screen that no longer exists, so every row was measured again:
>
> - Library: sbs_utils `2c7d93d1` as built into `data\missions\__lib__` (the working tree
>   was three documentation commits ahead, at `8d79be5f`; no code differs),
>   LegendaryMissions `b20726f`. The starter is `60c30bc`. The mission every file was cut
>   from is Lecture 3's `example\`, and this lecture's `example\` holds the same seven
>   files, byte for byte.
> - Tool: the installed `sbs.pyz`, built from sbs_cli `f26f3ff`. It prints `0.10`, the
>   number the public one prints. **The page needs an `sbs.pyz` built from sbs_cli
>   `f26f3ff` or later.** Step 11 starts the game on a mission whose libraries were
>   fetched with `sbs fetch "MyMission" --update-libs` (Lecture 3, Step 4), which the public
>   `0.10` does not have, and every "Lint" cell on the page is what that build prints.
> - 112 files: the untouched template and 111 with one change each. Each was linted
>   alone with the installed tool and played once in the mock with the packaged library,
>   one run at a time. (118 runs in all: two more that send the "hulk found" signal, two
>   on this lecture's own `example\` folder, one trial run, and one file run twice.) 110
>   of the files were also put through the SHIPPED Quest Log screen in-process.
> - VS Code `1.140.0` was READ (its own settings files), not run. The Artemis AMD add-on
>   was READ twice: at `0.9.3`, the one Lecture 3 names, and at `0.9.4`, which was
>   committed (sbs_cli `882e3ae`) while this pass was running.
> - The markdown rules were checked with `markdown-it-py 4.2.0` and `linkify-it-py
>   2.2.0`, the Python editions of the two libraries VS Code's preview is built on, set
>   as VS Code sets them by default. **The first measurement had link detection OFF. VS
>   Code has it ON** (`markdown.preview.linkify` defaults to `true`), so three rows of
>   "When the preview looks wrong" were wrong and are changed: a broken link shows its
>   brackets, and the bare address in it is a link all the same.
> - A script, `verify_page.py` in the measuring session's scratch folder, checks the
>   page against the runs and against the files that were read: 226 checks, 0 wrong.
>
> **What changed on the page.** The three tables under "The same marks in `mission.amd`"
> are rebuilt: 19 rows where there were 22, and the five rows that were the bugs are one
> row that says "shown as typed". Step 11's nine lines are new (two of the old five
> "results" were the bugs). `example\` now holds the whole mission as it is handed to
> Lecture 5, and Step 11's file moved to `example\step-11-only\`. "Before you start" and
> Step 11 name what Lecture 3 really teaches. The old rule "start every line with a
> letter" is gone: it was a way round a bug. And Step 1 no longer says to press `Alt+Z`:
> word wrap is already on in a `.md` file, so the key turned it off (see item 12).
>
> **Two things this pass found, both FIXED since in the library (`88d1c93e`,
> released 2026-10-05):** a line that holds a hash and nothing else replaced the whole
> description with `Document syntax issue line number 6 #`; it is now shown as typed
> (seen in the game), and the page's row, its rule and its "If something goes wrong"
> row were changed to match. And:
>
> - **The add-on's checker is silent where `sbs lint` warns `reading-wrapped`.** The
>   function the add-on shows the results of was called on all 110 files: it returned
>   nothing for the four files `sbs lint` gives that warning for. The page does not say
>   what the add-on underlines, so nothing on it is wrong. Lecture 6 should not say the
>   two agree until this is looked at.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`. The finished page is
`example\story-bible.md`. `example\mission.amd` and the six files beside it are the
mission as this lecture hands it on: untouched. The mission file for scene 11 is
`example\step-11-only\mission.amd`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` exactly as Lecture 3 leaves it: made with `sbs create MyMission -t amd --title "The Cold Hulk"`, its libraries fetched, played once, nothing edited |
| Library | sbs_utils `2c7d93d1` or later and LegendaryMissions `b20726f` or later, as built into `data\missions\__lib__`. With an older library scene 11 does not match the page |
| `sbs.pyz` | Built from sbs_cli `f26f3ff` or later. See the note at the top |
| VS Code | `MyMission` open as a folder AND TRUSTED, the Artemis AMD add-on installed, the Chat panel closed, the file list showing, no `story-bible.md` yet, font size raised |
| VS Code settings | Defaults. In particular `markdown.preview.breaks` off (scene 5 depends on it), `markdown.preview.linkify` on, and word wrap left alone: VS Code turns it ON for a `.md` file by itself and leaves it OFF for `mission.amd` |
| Word processor | Open, with this typed in it: `The "ghost ship" -- it isn't answering...` It must have made the quotes curly. Look at what it did to the two hyphens and the three dots, and say what you see |
| Browser | Not needed. If you click the link in scene 7, have one ready |
| Command prompt | Open in `data\missions`, with the Lecture 3 line already in its history, so the up arrow brings it back: `sbs run server,helm,science -m MyMission map=0` |
| Game | Closed. Scene 11 starts it with that line: three windows |
| Paste buffer | The nine lines of Step 11, from `example\step-11-only\mission.amd`, lines 31 to 39 |

## Confirm on camera

How each thing was checked:

- **Mock**: the template with ONE change, run headless with the packaged library. A probe
  asks the game for the text it holds, hands the Quest Log's own pane text to a real text
  area of the pane's size, and records every line that text area sends to be drawn.
- **Screen**: the shipped Quest Log screen (`quest_tab.mast`), run in-process. The quests
  are read from the same file by the game's reader, each row of the list is selected,
  and everything the right-hand side sends is recorded. 110 files, two rows each: in 214
  of the 220 it sent what the probe's text area sent, letter for letter and rectangle
  for rectangle. The six that differ are the six files with a lone hash, where the
  screen is the one to believe (see the note at the top).
- **Lint**: the installed `sbs.pyz`, on that one file, alone.
- **Rules**: `markdown-it-py` with link detection, set the way VS Code sets its preview
  by default.
- **Read**: a settings file of VS Code or of the AMD add-on, or VS Code's documentation.
- **Checker**: the add-on's own checking function, called on the file's text. Not VS
  Code.

Measured. These may be said as fact about what the game is SENT:

1. Every row of the three tables under "The same marks in `mission.amd`", and the two
   sentences under the three rules (`2187. A bad year.` is sent as `1. A bad year.`;
   `#1 priority is the hulk.` is sent as `1 priority is the hulk.` in the heading's font).
   (Mock, 112 files. Screen, for the description column, 110 files.)
2. The Lint column: `clean` for every file but eight. `reading-wrapped`, one warning,
   in four files: a reading broken over two lines, `---` between two readings, a lone
   hash between two readings, and lines with no `%` under lines that have one.
   `non-ascii`, five warnings, in the two files with curly characters. `broken-heading`,
   an error, in the two files with words typed after a heading's key. (Lint.)
3. Step 11's six rows, on exactly those nine lines. (Mock and Screen, and Screen again
   with the row CLICKED the way the engine sends a click.) The pane is sent, in order:
   `State`, `Active`; `Orders` in font `gui-5`, color `#bbb`; the sentence with its four
   stars in the ordinary font; `- Find her.` and `- Scan her.` indented, color
   `#8FA8FF`; `Her last word was stay.`; and the link line as typed, on one line. Each
   line's rectangle starts where the one above ends.
4. After the "hulk found" signal: `State`, `Done`, and the same six lines under it. The
   list is then First Contact, Study the Derelict, Find the Derelict, in that order.
   (Mock.) That is why Step 11 says not to fly anywhere first.
5. Selecting First Contact sends its own sentence, then `Find the Derelict`, then
   `... more to follow`. Before anything is selected, and on the list's top line, the
   pane says `Select a quest from the list.` (Screen, and by a click.)
6. Step 9's table. The markdown column is Rules. The right-hand column is Mock and Lint:
   a `//` line is not in the text the game holds; `[[study]]` is held as
   `Study the Derelict`; words after a heading's key are `broken-heading`, and the game
   then has no such record.
7. The game holds `"`, `'`, `-` and `...` for the four word-processor characters, and
   lint gives one `non-ascii` warning for each. (Mock, Lint.)
8. `story-bible.md` in the mission folder changes nothing: lint still counts
   `1 amd + 1 mast file(s)` and says `clean`, the mission runs, both logs are empty. With
   curly quotes in it, the same. (Lint, Mock.)
9. The finished page is one title, three headings, two paragraphs, two lists of three,
   one link, one bold word, one slanted phrase, and no mark left over. (Rules.) The link
   answered on 2026-10-04.
10. Every row of "When the preview looks wrong" says what each line IS (a heading, a
    list that starts at 2187, an address that is a link by itself). (Rules.)
11. The add-on's checker returns nothing for the nine lines of Step 11. (Checker.)

Read, not seen. Say them, and watch that they happen:

12. `Ctrl+K` then `V` is "Open Preview to the Side", and only while the cursor is in a
    markdown file. `Alt+Z` is "View: Toggle Word Wrap". Word wrap is off by default, but
    VS Code's markdown part turns it ON for `.md` files (`"[markdown]":
    {"editor.wordWrap": "on"}`), and the add-on sets nothing for `.amd`. (Read. **The
    first version of the page had the student press `Alt+Z` in Step 1 "to turn word wrap
    on". In a `.md` file that turns it OFF.** The step is gone.)
13. A `.md` file opens as plain text, not in VS Code's "Markdown Editor". The AMD add-on
    claims `.amd`, `.mast`, `.mastlib`, `.tiles` and `.tileset`, and leaves `.md` alone.
    (Read.)
14. In a `.md` file VS Code adds the closing `]` and `)` by itself. In a `.amd` file the
    add-on does the same. (Read.)
15. A single Enter in a paragraph does not show in the preview
    (`markdown.preview.breaks` is `false`), and a bare `https://` address is made a link
    (`markdown.preview.linkify` is `true`). (Read.)
16. "Before you start" says the preview opens even in a folder VS Code does not trust.
    VS Code's documentation: "VS Code supports Markdown files out of the box", and
    "Extensions that have not opted into Workspace Trust are disabled by default in
    Restricted Mode." VS Code's own markdown part declares itself `limited` there, and
    the one thing it gives up is a style sheet named in the folder's settings. The
    add-on at `0.9.3` declares nothing, so it is switched off whole. At `0.9.4` it
    declares `limited`: color works and the checker waits for trust. (Read.)

Seen by another session and reported to this one. Not seen here:

17. Where the quest list is: the handheld icon beside the crew member's name,
    **Quests**, the **Quest Log**, the list on the left, `State` and the text on the
    right. (The engine, for Lecture 6.)
18. After the library change, selecting a story in the Quest Log shows its description,
    then its open steps, then `... more to follow`. (The engine.)
19. `sbs run server,helm,science -m <mission> map=0` opens three windows titled
    `server`, `helm` and `science`, the map starts with no click, and Helm has a crew
    name in its top bar. (The engine, for Lecture 3.)
20. VS Code `1.140.0` with the add-on: in a trusted folder the headings of `mission.amd`
    are colored, the Status Bar says `AMD`, and `1 reference(s)` sits in small type above
    two headings. Not trusted, with `0.9.3`: no color and `Plain Text`. A **Chat** panel
    fills the right third of a fresh window. (A real window, for Lecture 3. Step 9's
    sentence about small words above a heading rests on this.)

NOT checked. If one is not as described, stop and fix the page:

21. Everything VS Code draws in a `.md` file. The **New File...** entry when you
    right-click the file list. The preview opening beside the file and following what
    you type. The link being a link. An indented paragraph "in a box, in typewriter
    letters". How the preview draws any row of "When the preview looks wrong".
22. Everything the Quest Log draws. That `gui-5` in `#bbb` reads as "larger gray
    letters". That `#8FA8FF` reads as light blue. That a star is drawn as a star. That
    touching rectangles leave no gap between two paragraphs. That the link line of Step
    11 fits on one line of a real pane (it did in the mock, at 1024 by 768).
23. Everything Science draws: a star, a backtick, a hash, a tab inside a reading. The
    mock holds the characters as typed and nothing more is known. A caret above all: in
    a description the game breaks the line at a caret, and Science may do the same with
    a reading. The page says only "kept as typed".
24. What the recording machine's word processor really does to `--` and `...`. The page
    says only that it makes a long dash and joined dots. Try it before scene 9.
25. `Ctrl+Z` in scene 11 brings the nine lines back to one.
26. `State` reads `Active` when the list is opened straight after the start. (Mock. It
    stays so until the ship is within 2000 of the hulk.)
27. What the add-on draws under the nine lines of Step 11 while they are in
    `mission.amd`. Its checker returns nothing for them, so the page expects no
    underline.
28. Whether VS Code types the next hyphen or number of a list for you when you press
    Enter. Its settings file for markdown has no such rule, so the page tells the
    student to type each one.
29. The lone hash. On the shipped screen, in-process, the pane is sent
    `Document syntax issue line number 6 #`. Do not show it on camera unless it is
    still there in the build you record with.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** VS Code. On the left, `example\story-bible.md` as text. On the right, its
preview. Hold.

**Say:** "On the left is what I typed, with nothing but a keyboard, | and on the right is
what a reader sees. || The few odd characters on the left are called marks, | and the whole
idea is called markdown. ||| You need it because the file your mission lives in is written
the same way. || And it takes about twenty minutes. ||"

### 2. What markdown is

**Screen:** A word processor with a bold button and a styles menu. Then VS Code, plain.

**Say:** "In a word processor, you make a heading by choosing a style, | and the file
remembers that in a way only the word processor can read. || In markdown, you type a hash in
front of the line, | and then anything can read it: a person, a preview, or a game. |||
Today you'll write one page, a story bible for your mission, | and you'll learn six marks.
||"

### 3. Make the file, open the preview

**Screen:** The mission folder from last lecture, open in VS Code. Right-click in the
file list, **New File...**, type `story-bible.md`. Type `# Nobody Aboard`. `Ctrl+K`, `V`.
`Ctrl+S`.

**Say:** "This is the folder you made and opened last time. || I make a new file in it, and
its name ends in dot M D. || Then I type one line: a hash, a space, and my title. ||| Now,
control K, let go, and then V, | and that opens the preview. || The hash is gone, and the
words have become a title. || This preview is part of VS Code, so it needs nothing added.
||| And then I save. || The game never reads this file. | It's mine, and nothing I type here
can break anything. ||"

### 4. A title and three headings

**Screen:** Type `## Premise`, `## People`, `## What happens`, a blank line between each.
Then delete the space in `## Premise`: the preview. Put it back.

**Say:** "Two hashes make a heading. | Three would make a smaller one, inside it. || So
count the hashes, | because in the next lecture, the number of hashes is how the game knows
what's inside what. ||| There are two rules. || The hashes start at the left edge, | and
there's one space after them. || Watch what happens without the space: | it's not a heading
any more. || So I put it back. ||"

### 5. Paragraphs

**Screen:** Type the paragraph under the title on one line. Then the Premise paragraph.
Press Enter in the middle of one: the preview. Undo. Press Tab at the start of one: the
preview. Undo.

**Say:** "A paragraph is one line, however long it is, | and word wrap folds it for me. || A
blank line ends it. ||| Now, here are two things writers do without thinking. || The first
is pressing Enter in the middle of a paragraph. || Look at the preview: it joined the halves
again, so you'd never know. || But the game doesn't join them. | It starts a new line there.
|| So the rule is, one paragraph, one line. ||| The second is the Tab key at the start. ||
Look what the preview made of that. || In markdown, an indented line is something else
altogether, | so never start a line with Tab. ||"

### 6. Two lists

**Screen:** Type the three people under `## People`. Type the three numbered lines under
`## What happens`.

**Say:** "A hyphen, a space, and a line of words make a list. || These are the people in my
story. || A number, a period, and a space make a numbered list, | for things that happen in
order. ||| Keep these three lines, | because in Lecture Eight, each one becomes a step of a
quest. || And leave a blank line above a list, and a blank line below it. ||"

### 7. One link

**Screen:** At the end of the Premise paragraph, type the sentence with the link, slowly.
Show the `]` that VS Code adds. The preview. Then `mission.amd`, line 47:
`### [Derelict Hull](derelict_scan)`.

**Say:** "A link is two pairs of brackets. || Square brackets go round the words the reader
sees, | and round brackets go round where it leads. || There's nothing between them, not
even a space. ||| VS Code typed that closing bracket for me, so I just keep going. || And in
the preview, it's a link. ||| Now look at this line from the mission file. || It's hashes, a
space, square brackets, and round brackets: | a heading with a link in it. || That's the
first line of every record you'll ever write. || In that file, though, the round brackets
hold a short name for the game, | and not a web address. ||"

### 8. Bold and italic

**Screen:** Put `**` each side of `nobody`. Put `*` each side of `Not written yet:`.

**Say:** "Two stars on each side make a word bold, | and one star on each side makes it
slanted. || Use them in your story bible. || But don't use them in the mission file, | and
in three minutes you'll see why. ||"

### 9. The plain keyboard

**Screen:** The word processor, with the prepared sentence. Zoom on the quote marks.
Copy it. Paste it into `story-bible.md` under the first paragraph. Zoom. Then delete it.
The table from Step 8 of the page.

**Say:** "Everything I've typed so far is a key on my keyboard. || A word processor isn't
like that. || I typed straight quotes here, and it made them curly. | It did this to my
hyphens, and this to my three dots. || And it doesn't ask. ||| The game can draw only plain
characters. || When it reads your mission, it swaps these for the plain ones, so nothing
breaks, | and you get a warning for each one, which is Lecture Six. ||| But the habit starts
now: write game text in VS Code. || And if you bring words over from a word processor, |
type the quotes, the dashes and the dots again. ||"

### 10. The mission file with new eyes

**Screen:** `mission.amd`. Highlight in turn: a heading; the `---` under it; a `%` line;
a `//` line. Then the Step 9 table on the page.

**Say:** "Here's the file the game reads, | and you can read most of it now. || Hashes mean
a heading, and brackets mean a link. || But five marks in here aren't markdown's. ||| This
heading is the first line of a record: | a name for people, and a key for the game. || These
three hyphens would be a line across the page in markdown. | Here, they're a fence, with the
record's facts inside. || A percent sign is one reading for the Science screen. || Two
slashes are a note to myself, which the game skips. || And there's one you haven't got yet,
double square brackets, | which is a link to another record. ||| So this file is shaped like
markdown, and it isn't markdown. || The preview I opened for my story bible doesn't open for
it. | The game is what reads it. ||"

### 11. The game is not a preview

**Screen:** In `mission.amd`, select line 31, `Fly out and locate the drifting hulk.`,
and paste the nine lines. Save. The command prompt: up arrow,
`sbs run server,helm,science -m MyMission map=0`. Three windows. The `helm` window: the
handheld icon, **Quests**. Select **Find the Derelict**. Hold on the right-hand side and
point at each line. Close the three windows. `Ctrl+Z` until one line is left. Save. Then
the three tables on the page.

**Say:** "So what does the game do with marks? || I'll give this quest nine lines: | a
heading, a bold word, a list, a word in backticks, and a link, | and then I save. ||| I
start the game the way we did last time, and I don't fly anywhere. || On Helm, it's the
handheld, then Quests, | and I select Find the Derelict. ||| The heading is drawn as a
heading. || The bold word is still wearing its stars. || The list is a list. || The
backticks are gone, and the word is still there. || And the link shows every bracket and the
whole address, with nothing to click. ||| Look at the spacing, too. | I left three blank
lines, and the game left none. || A preview would have drawn all of it. | The game drew two
things, the heading and the list. || And nothing warned me, either. ||| So here are the
rules for the mission file, and they're on the page. || Write plain sentences, and keep one
paragraph to one line. || And a heading and a list are the two marks a description draws.
||| Then I close the game, and I put my line back, | because the next lecture starts from
the file as it was. ||"

### 12. Your turn

**Screen:** The exercise on the companion page. Then `my-story.md`, empty.

**Say:** "Now write the story bible for your own mission. || Give it a title, and the story
in two sentences. || Then three headings: premise, people, and what happens. || Add three
people, three things that happen, and one link. ||| Keep it, because the people become
characters in Class Two, | and the three things that happen become your first quest. || Next
time, we take one record of the mission file apart, line by line. ||"
