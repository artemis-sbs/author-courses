# C3-1 video script - What a boarding party is

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **This lecture makes the mission the class is built in:** `MyBoarding`, with
>   `sbs create MyBoarding -t amd --title "The Hulk"` and
>   `sbs fetch "MyBoarding" --update-libs`. Class 3 does not build on `MyMission`: Class
>   1's story ends the game in ten minutes, and Classes 2, 4 and 5 may or may not have
>   been added to it.
> - **A play-and-read lecture.** The student pastes two blocks, plays, reads, and deletes
>   both again. The first block is the Scenes section of Open Universe's
>   `quiet_shore.amd`, word for word, with one thing cut from each of its fourteen rooms:
>   the three-line fence that says `Speaker: bel`. The second is a card for `story.mast`
>   that is not from that file: it opens the scene when the ship comes inside 2000 of the
>   hulk.
> - **Open Universe is never run.** The student does not need it installed. Everything
>   quoted from it is on the page. Do not start Open Universe for this recording from a
>   folder whose saved games matter.
> - **`example\` holds two files: the mission WITH the borrowed scene and the card**
>   (`mission.amd`, 163 lines; `story.mast`, 115 lines). The lecture ends with both blocks
>   deleted, so the hand-over to Lecture 2 is the untouched `sbs create` mission.
> - **Dawnline is named and not played.** The plan had the student play it here. A
>   student may not have it, and the tile-map half of the class is not written yet.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). `sbs create` was run for real.
> Both blocks were pasted where the page says, linted, and played headless by a probe
> that moves the ship, makes the two calls the BEAM DOWN button makes on a stand-in
> console, and presses choices through the handheld page's own signal. One console at
> Helm, then three. Then 19 one-change variants. No engine, no window. Nothing in this
> lecture has been seen on a screen.

The companion page is `lesson.md`; the files with the borrowed scene are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Missions folder | No folder named `MyBoarding` yet. It is made on camera in scene 2 |
| VS Code | Open, with no folder. The Artemis AMD add-on installed |
| Command prompt | Open in `data\missions`, cleared |
| The blocks | `example\mission.amd` lines 63 to 163, and `example\story.mast` lines 108 to 115, ready to copy |
| The shipped file | Open Universe's `quiet_shore.amd` open read-only for scene 6, or use the page's own excerpts |
| Game | Closed. Started on camera in scene 4 with a server and a Helm console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. If an item fails while recording, stop and fix the page.

1. `sbs create MyBoarding -t amd --title "The Hulk"` ends `MyBoarding is ready.` and makes
   seven files; `mission.amd` has 60 lines and `story.mast` 105; lint is `clean`. (Run for
   real, with a throwaway name.)
2. With the first block pasted, lint prints the one `section-not-loaded` line on the
   page. With the card pasted too, lint is `clean`. (Lint.)
3. With the ship inside 2000 of the hulk, the first step of First Contact completes and a
   visit titled Ferrow Landing is on offer in the room `arrival`. (Mock.)
4. A lone Helm console goes down as the name the game gave it, with the job `helm`. On
   the landing field it has two choices of its own and four more that the page text marks
   `(covering for medical)`, `(covering for engineering)`, `(covering for security)` and
   `(covering for science)`. (Mock.)
5. With fewer than three things found out, Open it is not offered at the east cable; with
   three it is. Twelve presses reached the end of the last room, and the visit closed.
   (Mock.)
6. With Helm, Engineering and Science aboard: Engineering is offered the power spur and
   Science the supply run as their own, and the medic's and security's choices go to one
   console, marked as covering. (Mock.)
7. With both blocks deleted the files are the `sbs create` files, lint is `clean`, and
   finding the hulk forms no party. (Lint, Mock.)
8. Every row of "If something goes wrong", and the two slips at Stop 6. (Lint, Mock.)
9. The exercise: the new title is the visit's title; at `learned >= 5` Open it is offered
   once all five things are found; Beam back up in the first room ends the visit at one
   press and nothing is on offer afterwards. (Mock.)
10. Every excerpt in Stop 5, and every line of the pasted block, is a line of
    `quiet_shore.amd` as it stood on 2026-10-09 (211 lines). (Checked by script.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. All of scene 4 on a real screen: the Boarding Party tile on a mission made by
   `sbs create`, BEAM DOWN, the handheld's bar and buttons, and the console becoming Helm
   again. The earlier pilots of Lecture 2 saw these same screens with a different scene.
2. What the ship does while its only Helm officer is ashore. The page says to stop the
   ship first.
3. Which of a room's two lines is shown. It is picked at random, so the take will differ
   from any test run.
4. Whether Open Universe is in a student's install. The page says the student does not
   need it, and quotes everything it uses.

> One thing to know before recording with more than one console. If the visit opens while
> nobody at all is at a console, the people who join afterwards are offered no covering
> choices, and a short crew cannot open the shed. On this page the visit opens when Helm
> finds the hulk, so somebody is always seated. It is in the report as a library defect.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. A console showing the boarding party's handheld: a name, a job, a
place, one line of text and six buttons. Cut to a text file, a hundred lines long.

**Say:** "This is a boarding party. || Somebody has left the ship, | and they're standing
on a landing field, | talking to a woman who says everything is fine. ||| Nobody drew this
place. It's this: | about a hundred lines of text. ||| In this class, you write places
like it. | Today, you play one that somebody else wrote, | and then you read how it was
made. ||"

### 2. A mission for this class

**Screen:** Command prompt. Type the create line, press Enter at the question. Type the
fetch line. Open the `MyBoarding` folder in VS Code and trust it. `sbs lint MyBoarding`:
clean.

**Say:** "First, a new mission. || This class doesn't build on the one from Class 1. |
That story ends the game ten minutes in, | and a boarding party should be allowed to take
its time. ||| So I make a mission the way I did before, | and I call it My Boarding. ||
Then I bring its libraries up to date, | open the folder in the editor, and run lint. ||
It's clean, and it's the same small mission you started Class 1 with. ||"

### 3. Borrow a scene

**Screen:** `mission.amd`, the end of the file. Two blank lines. Paste the block. Scroll
through it slowly. Save. Lint: one warning. Then `story.mast`, the end of the file: paste
the card. Save. Lint: clean.

**Say:** "There's a shipped campaign with a colony in it called Ferrow Landing. || Eleven
people, a raked gravel landing field, | and an administrator with an answer for
everything. ||| I go to the very end of my fact sheet, | and I paste that colony's scene.
|| Don't read it yet. ||| Lint has one thing to say. | Nothing in this mission reads these
rooms. And that's true, | because a scene needs something to start it. ||| So I open the
story file, go to the very end, | and paste one card. || Now lint is clean. ||"

### 4. Play it

**Screen:** Command prompt: `sbs run server,helm -m MyBoarding map=0`. Fly toward the
hulk; stop inside 2000. Press the handheld icon; the Boarding Party tile; BEAM DOWN. Read
the buttons. Take one covering choice and come back. Walk in. Ask to see the east cable.
Walk back, take more readings. East cable again: Open it. The last room. Its one button.

**Say:** "I start the game with a server and a Helm console, | and I fly toward the hulk.
|| When I'm close, I stop the ship, | and I open the handheld. ||| There's a tile called
Boarding Party, and it's offering Ferrow Landing. I beam down. ||| Now this console is my
handheld. || Two of these buttons are plain. | The others say covering, | and then a job.
|| Those belong to people who aren't here, | and I'm one helm officer, so they all come to
me. I take one, | and I read what a medic would've noticed. I walk in. | I ask about the
cable. || And she won't open the shed, | because I haven't found enough to say out loud.
||| So I go back and look harder. || Three things found out, | and now the button's there.
||"

### 5. Read what you pasted

**Screen:** `mission.amd`, the pasted block, The Landing Field. Highlight in turn: the
heading and its key; the two lines that start with a percent sign; a plain choice; the
`if` on a choice; the `learn` after the semicolon; the empty brackets. Then The East
Cable: the `learned >= 3` choice and the line with curly brackets.

**Say:** "Now let's read it. || It's one section, with fourteen records in it, | and each
record is a room. ||| A room has no fence at all. || These lines, the ones that start with
a percent sign, | are what the party finds. || There are two here, | and the game showed
me one of them. ||| Each line with a dash is a choice. | The words go on a button, | and
the key in round brackets is the room it leads to. ||| This one adds a condition. | Only a
medic is offered it. || And after the semicolon, | the party learns something. ||| Then
here, at the cable, is the door. | It asks how many things the party has learned. || And
this last kind has nothing in its brackets. It leads nowhere, | and it ends the visit. ||"

### 6. Read the rest of the file

**Screen:** The shipped `quiet_shore.amd`, or the page's excerpts. Scroll: the notes at
the top, with "Every room is REVERSIBLE" highlighted; the Voices record; a room's
`Speaker:` fence; the call in the Hails section. Then the "What was cut, and why" table.

**Say:** "The shipped file is about two hundred lines, | and I pasted half of it. ||| It
opens with a page of notes, from the author to whoever comes next. || This one says every
room has to lead back as well as on, | and it says so because the first version didn't.
||| Then there's a voice, | the administrator, of the kind you'll meet in Class 2. || And
there's the call that starts the scene in that campaign, | when the ship docks at the
colony. I cut those, | and the table on the page says what went and why. ||"

### 7. Give it back

**Screen:** `mission.amd`: select from `## [Scenes](boarding)` to the end of the file,
delete. Status bar: 60 lines. `story.mast`: select from the `#` line above the card to the
end, delete. Status bar: 105 lines. Save both. Lint: clean.

**Say:** "Ferrow Landing was a loan, so now I give it back. || In the fact sheet I delete
everything from the Scenes heading to the end, | and it's sixty lines again. || In the
story file I delete the card, | and that's a hundred and five. ||| I save both, I run
lint, and it's clean. || Don't leave the card behind. Lint won't mind, | but the game will
go looking for a room that isn't there. ||"

### 8. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Before you delete it, play with it. || Change the name on the card, | and find
it on the tile. || Make the shed ask for five things, | and see how much harder the colony
gets. ||| Then answer three questions from the file alone, | with the game closed. |||
Next time, you write a place of your own: | a crew, three rooms, | and the card that
starts it. ||"