# C2-7 video script - The story tools

> **STATE ON 2026-10-08. First version of this lecture.**
>
> - Everything the page needs is released. The page is written for Artemis Cosmos 1.4.0
>   from Steam or itch.io, a current `sbs`, and the VS Code AMD add-on.
> - **Starts from Lecture 5's finished mission**: `c2-05-hails\example\mission.amd` (the
>   whole Class 1 mission plus sides, faces and calls), with the `story.mast` of
>   `c2-01-sides-and-factions\example\` and the other files of a mission made by `sbs
>   create`. `example\` here holds the one file that differs, `mission.amd`. The lecture
>   was first measured on an older Lecture 5 file and was measured again, whole, when that
>   file changed on 2026-10-08. Lecture 6 (written 2026-10-10) is done in a COPY of the
>   mission folder, `MyStanding`, so it changes nothing this lecture reads: the student
>   comes back to `MyMission`, which is still Lecture 5's file.
> - **Measured:** the lesson's eight states of the file (start, notes, plan, each of the
>   three records written, the cut, the exercise's cut) and sixteen one-change mistakes, each through
>   `sbs lint` and `sbs lint --missing` with the installed tool. Seventeen headless plays
>   on the packaged library, one at a time, with a stand-in Comms console that opens calls
>   and chooses answers, and a reader for what the Quest Log's pane is given. `sbs docs`
>   was run for all four documents, with and without `--profile player`, and with `--pdf`;
>   the pages were read as text. A script (`c2b\verify_l7.py`) found every tool line
>   printed on the page in those runs.
> - **The four views were NOT seen.** Nobody opened VS Code. What the page says about
>   them comes from three places: the add-on's own list of commands and menus
>   (`package.json`), its source (`extension.ts`), and the DATA each view is handed. That
>   data was measured, by asking the language server's own functions for the outline,
>   timeline, graph and missing models of this lesson's file: 31 records and 12 pointers
>   at the start, 34 and 14 at the end, 5 beats, and the beat of every record the page
>   names. How any of it is drawn is unseen.
> - **Not run in the real game.** Every play was in the mock.

The companion page is `lesson.md`; the finished file is `example\mission.amd`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyMission` as Lecture 5 leaves it. `mission.amd` must match `c2-05-hails\example\mission.amd` line for line, or the line numbers 156, 160, 352, 363, 369 and 330 on the page are wrong |
| VS Code | The mission folder open and trusted, `mission.amd` in one tab, font size raised, the top right corner of the editor in shot |
| Command prompt | Open in `data\missions`, cleared, wide enough for one long warning |
| `__docs__` folder | Absent. Scene 9 makes it |
| Game | Closed. Started on camera in scene 10 with a server, a Helm and a Comms console |

## Confirm on camera

"Lint" is the installed tool on that exact file. "Mock" is a headless play. "Server" is
the language server's own answer for that file. "Read" is the add-on's source.

1. With Lecture 5's file, `--missing` says `Nothing missing`. (Lint.)
2. Four notes typed under four headings: lint is `clean`, and the Quest Log's pane is
   given no note for any record. (Lint, Mock.)
3. Holding the mouse over `report_in` in `Then: reveal report_in` shows the record's
   name, its note in slanted type, and its first line. (Server: the hover text. The box
   itself is unseen.)
4. The icons at the top right of an `.amd` editor, and their order: Outline, Timeline,
   Graph, then Resolver and Show Missing. (Read. The Resolver and Show Missing carry the
   same position number in the add-on's menu, so which of the two comes first is not
   known. Unseen.)
5. The tab names: `Story Outline`, `Story Timeline`, `AMD Story Graph`, `AMD Missing`.
   (Read.)
6. Thirty-one records in six groups, five beats, twelve arrows. (Server.)
7. The timeline has Quill Checks In and Tag the Hulk in beat 1. (Server. The bible page
   prints the same.)
8. After Step 4, `--missing` lists three things with lines 156, 352 and 160, and plain lint
   prints three warnings. (Lint.) The Missing panel's first line is built from the same
   numbers. (Server, Read.)
9. After each record of Step 6 the list is one shorter, and after the third it says
   `Nothing missing`. (Lint.)
10. With the scene cut, `--missing` lists `quill_history`, chosen from `quill_hello`, on
    line 330. Choosing that answer ends the call and DS 1 Calls stays open. (Lint, Mock.)
11. `sbs docs MyMission --lens all --title "My Mission"` prints four lines and makes four
    pages. (Run. The pages were read as text and not looked at.)
12. In the game: the link is printed as `Assessor Vane`; the new answer leads to
    Quill's new scene; Report to DS 1 pays 150; The Claim appears, finishes a little over
    a minute later and pays 200. (Mock: 500 credits in all, because the probe's ship is
    put at the hulk at once and so earns Quick Work's 50 as well.)
13. Unseen, all of it: every view, the hover box, the printed pages in a browser, the PDF,
    the Quest Log with the link in it, the calls on a real Comms console.

Also capture the screenshot the page asks for.

## Scenes

### 1. Cold open

**Screen:** VS Code. `mission.amd` on the left, the Story Timeline beside it. Then the
command prompt with a three-line to-do list.

**Say:** "Your story has people in it now, and calls, and answers that start jobs. || It's
getting hard to see all of it at once. ||| So today you don't learn a new kind of record. |
You learn four ways to look at the ones you have, | and one habit that lets the tool
write your to-do list for you. ||"

### 2. Why a file isn't enough

**Screen:** `mission.amd`, scrolled slowly from top to bottom. Then the command prompt:
`sbs lint MyMission --missing`. One line of answer.

**Say:** "Thirty-one records, and twelve places where one of them points at another. ||
You can't hold all of that in your head any more, | and it's only going to grow. ||| So I'll
ask the tool a question. || It's lint, with one more word on the end: missing. || And it
says nothing's missing, | which means every pointer lands on a record that exists. || Keep
that answer in mind, | because in a few minutes we're going to break it on purpose. ||"

### 3. A note on a record

**Screen:** Type a note under `### [First Contact](first_contact)`. Then under Close
Inspection, DS 1 Calls and Report to DS 1.

**Say:** "A quest's description is written for the crew, | and it tells them what to do. ||
It doesn't say why your story needs that step, | and a note does. ||| A note is one line,
right under the heading, | that starts with an equals sign and a space. || So this one says what the mystery is for, | and this one marks the end of act one. || The crew never sees a note. || You do,
every time you hold the mouse over a pointer to that record. || And don't forget the space
after the equals sign, | because without it the line isn't a note at all. ||"

### 4. Three views

**Screen:** The top right corner of the editor. Click the first icon: Story Outline. Then
the second: Story Timeline. Then the third: the graph.

**Say:** "Now look at the top right corner of the editor, | where the add-on has put a row
of small icons. || The first one is the outline: | every record in a list, grouped by
section, with a box to search in. || The second is the timeline, | and that's the one I
use most. || It has columns called beats, | and whatever's in beat two can't happen until
something in beat one has. ||| The third is the graph, | which is a box for every record
and an arrow for every pointer. || All three redraw while you type, | and clicking a
record takes you to it in the file. ||"

### 5. What the timeline can't see

**Screen:** The Story Timeline. Point at Tag the Hulk in beat 1, then at Quill Checks In
in beat 1.

**Say:** "There's one thing you need to know before you trust it. || The timeline follows
a reveal, | and it follows an answer that leads to another scene. || But it doesn't
follow a call that a quest places, | and it doesn't follow what an answer starts. ||| So
here's Tag the Hulk in beat one, | even though that job only starts when Comms says, we'll
tag her. || Read the timeline for the chain of your quests, | and for who calls whom, read
the printed script, which is coming up. ||"

### 6. Plan act two by pointing at it

**Screen:** In Report to DS 1, add `Then: reveal claim`. Add the sentence with `[[vane]]`
to its description. In Quill Calls Back, add the second answer.

**Say:** "Here's the habit I want you to have. || Act two is three ideas: | the hulk is worth something, the
crew owns her for an hour, | and a Guild assessor called Vane wants to know her price. || I'm not
going to write any of that yet. | I'm going to point at it. ||| So this step reveals a
quest called claim, which doesn't exist. || This sentence has a link in it, | two square
brackets around a key, | for a person who doesn't exist. || And this answer leads to a
scene that doesn't exist either. ||"

### 7. The to-do list

**Screen:** Command prompt: `sbs lint MyMission --missing`. Three entries. Then the Show
Missing icon in VS Code, and the same three in a tab.

**Say:** "Now I ask the same question as before. || And this time I get three things,
referenced but not written yet. || For each one it tells me what's missing, | which record
points at it, and on which line. ||| That's my writing list for act two, | and I didn't
have to keep it anywhere. || The fourth icon in the editor shows the same list, | and
clicking a row takes me to the line. ||"

### 8. Write them, and cut one

**Screen:** Type The Claim; run `--missing`: two left. Type Assessor Vane: one left.
Type Who Else Is Asking: nothing missing. Then put `/*` and `*/` around What DS 1 Knows
and run `--missing` once more.

**Say:** "So I write them one at a time, | and ask again after each. || There are two left, then one, | and
then nothing's missing at all. ||| Now the other direction. || When you cut a
scene, don't delete it. || Put a slash and a star on a line above it, | and a star and a
slash on a line below, | and it's out of the mission and still in your file. || Then ask
what's missing. || One answer still leads to the scene I cut, | and if the crew picks it,
the call just ends, | and the story stops there. || So a cut has two halves, | and the
list tells you the second one. ||"

### 9. Print it four ways

**Screen:** Command prompt: `sbs docs MyMission --lens all --title "My Mission"`. Four
lines. File Explorer: the `__docs__` folder. Open the screenplay page, then the bible.

**Say:** "In Class 1 you printed one document. | Now print all four. || The prose one is
your story as a book, with your notes beside it. || The screenplay is every call, | with
who speaks, what they say, | and what each answer does. ||| Read that one aloud. || But
remember that where you wrote three takes, it prints three lines, | and she only ever
says one of them. || The catalog is for looking things up, | and the bible has the same
beats as the timeline, | with the same two gaps. ||"

### 10. Play act two

**Screen:** `sbs run server,helm,comms -m MyMission map=0`. Fly to the hulk. Comms: the
first call, then the second. Choose "Who else is asking about her?", then "Then log the
claim". The Quest Log: The Claim.

**Say:** "And then you play it, because a list isn't a game. || The link in my sentence is
printed as his name, Assessor Vane. || On the second call there's my new answer, |
and it leads to Quill's new scene, | which has the answer that finishes the report. |||
The Claim appears in the log, | and a minute later it pays. || Your notes aren't on any console. |
They were only ever for you. || Next time we leave this mission for a while, | and you
write a boss. ||"
