# C4-6 video script - Clues, side stories and cutscenes

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`** as Lecture 4 left it, without Lecture 4's
>   exercise: a fresh `sbs create MyRuin -t amd` mission whose `mission.amd` is
>   `c4-04-places-that-speak\example\mission.amd` (199 lines). Lecture 5 (things to
>   take aboard) can be done before or after this one; nothing here depends on it. The game is started with
>   `sbs run server,helm,comms -m MyRuin map=0`.
> - **This lecture hands the student a recipe card** (R13 in the plan): one line in the
>   map block of `story.mast` and a three-line block at its end. Nothing a writer can put
>   in `mission.amd` starts a cutscene today.
> - **`example\` holds the two files that differ from the start:** `mission.amd` (296
>   lines) and `story.mast` (116 lines).
> - **Side stories for one person are not in this lecture.** Storm's Beacon's Side Stories
>   sections hold `For:` quests, which are handed to a crew member who goes into the ruin
>   in a suit. The page shows one and says where one is typed: Lecture 10's exercise.
>   What the student builds is a side story for the ship: an ordinary quest that a clue
>   starts.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were typed one
> at a time onto Lecture 4's finished files, with lint after each. Then the pilot's
> one-change variants of the two finished files: each linted, each played headless by a
> probe that moves the ship, opens calls with the game's own functions, and records what
> the card played, to which console, which object each console rode, and the words put on
> a screen. Where a cutscene is involved the run was started the way a server starts a
> map, so that the server's window is a main screen as it is in the game.

> **SEEN IN THE REAL ENGINE, 2026-10-04**, on the first version of these files; the
> records this lecture adds have not changed. The probe's report matched the mock's line
> for line. The cutscene was WATCHED on the main screen (the server's window, seven
> pictures two seconds apart):
>
> - Black bars across the top and the bottom for the whole cutscene.
> - Under shot 1, in a dark band low on the screen: `The Altar` in blue, and below it
>   `The tally on the rim stops at forty-one.` in white. Under shot 2: `The Cairn` and
>   `Forty-one stones. One for each day.` Each line fitted on one line.
> - The camera does ride a place: no crash and no black screen. What it shows is the rock
>   and the walls around the place, and in shot 2 the crew's own ship in the distance. The
>   place's marker itself is not a thing you can see.
> - When it ends the main screen is back on the ship's own view.
> - `Quest complete: The One Who Stayed` is drawn at the left of the main screen and stays
>   up through the cutscene.
> - One wart: the main screen's ship panel (top left) stays up during the cutscene and
>   reads the SUBJECT: the name `The Altar`, then `The Cairn`, with `Energy 0`.
> - With NO console connected, the game's own "connect a client" notice covers the middle
>   of the main screen and the captions are behind it.
> - Helm and Comms do not change during the cutscene. On Helm's map the places are drawn
>   as named contacts in yellow among the rock of the walls.
>
> Not looked at: the cone on The Cairn, and the third answer on Comms (the probe answers
> the calls by itself).

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 4 leaves it, lint clean: The Hollow with The Ring, The Way In, The Altar and The Niche, Surveyor Rook, Marker One, Rook at the Altar, The Rest of It. Lecture 4's exercise NOT done. `mission.amd` has 199 lines, or the line numbers 267 and 65 on the page are wrong |
| `story.mast` | The template's, 105 lines, `relics_spawn` on line 62 |
| VS Code | `MyRuin` folder open, `mission.amd` and `story.mast` in two tabs, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 10 with a server, a Helm console and a Comms console. The server's window must be showing the main screen. At least one console must be connected before the cutscene |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. "Engine" is the run of 2026-10-04 in the note above. If an item fails while
recording, stop and fix the page.

1. Lint is `clean` after every step except the two the page shows, both in Step 7: with
   the Cutscenes section typed and no map line, the `section-not-loaded` line printed
   there, with `line 267`; with the `Then:` line typed and no block, the `signal-no-route`
   line printed there, with `line 65`. (Lint.)
2. At the ring a call is waiting, "Surveyor Rook - A recording at the ring", with the
   answers "Log the names." and "Shut it off.". "Log the names." puts `names` on the list
   of what the crew knows. (Mock, Engine.)
3. At the altar, with the names logged, the call offers three answers. With the ring call
   shut off, two. (Mock, Engine.)
4. "Play the entry keyed to Dace." leads to the entry. "Mark the side room." lights The
   Cairn, starts The One Who Stayed (it is then in the quest list as Active), and goes on
   to The Rest of It, where "Mark the Gallery." lights The Niche. (Mock, Engine.)
5. 900 from the cairn: nothing. 300 from it: The One Who Stayed is done, the crew is told
   `Quest complete: The One Who Stayed`, and the card plays the cutscene to one console,
   the server. (Mock, Engine.)
6. The cutscene on that console: black bars go up; the console rides The Altar for 4
   seconds with the name `The Altar` and the line `The tally on the rim stops at
   forty-one.`; then The Cairn for 6 seconds with `The Cairn` and `Forty-one stones. One
   for each day.`; then it is put back on the ship. The lens was 540 from the altar, and
   went from 1440 to 540 from the cairn. (Mock, Engine.)
7. The two lines the page prints from `mast.runtime.log`, word for word. (Mock.)
8. The crew that shuts the ring recording off: no entry, no side room, no side story, and
   flying into The Crypt does nothing. The crew that opens the altar call first, presses
   Back, logs the names and opens it again: still two answers. (Mock.)
9. With both calls waiting, the altar call is listed above the ring call. With
   `Priority: 5` on Rook at the Ring, the ring call is listed first. (Mock.)
10. Every row of the tables in Step 8 and the "not mistakes": lint for all of them, and
    the mock for what the game does. (Lint, Mock.)
11. The exercise as written, items 1 to 3 together: lint `clean`; the crew that knows
    hears the second take and the crew that does not hears the first; the side is paid
    150; the cutscene has three shots and lasts fourteen seconds. (Lint, Mock.)

Read in the library's code, not measured: the crew has no way to skip a cutscene; what
was learned is kept until the mission is restarted; a call's lines and answers are fixed
the first time each scene is opened; a line that does not fit is split against that
screen's width (the 45 letters on the page are the mock's screen).

Not seen by anyone. If one is not as described, stop and fix the page:

1. The cone on The Cairn, and whether a ship in The Crypt can see it.
2. The third answer on Comms, between the other two.
3. Whether a ship flying the passage at full impulse is caught by `reach plate 500`. The
   ship was moved, not flown.
4. Everything Lecture 4's script lists as unseen: the call's row, the open call, a place
   turning into a contact after an answer.

> Keep off camera: `Lens:` and `Move:` on a shot (they are spots in the whole map, and a
> writer who types numbers measured from the ruin puts the camera twenty thousand away),
> and a Side Stories section (lint warns about it, wrongly for a ruin; it is typed in
> Lecture 10's exercise).

> Say the wart out loud in scene 10. The ship panel in the corner of the main screen reads
> `The Altar` and `Energy 0` during the cutscene. A viewer will take it for a mistake in
> the file. It is not, and the page says so in Step 9.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. Comms: the altar call with three answers. Cut to Helm's map, a new
contact. Cut to the main screen: black bars, a caption. Cut back to the bridge.

**Say:** "Last time, the ruin could talk. | Today, it keeps a secret. || A crew that
listens at the door gets one more answer further in. || That answer opens a side room, |
and a small story of its own. ||| And when they find what's in the room, | the main screen
stops being a window, | and becomes a film, for ten seconds. ||"

### 2. What a clue is

**Screen:** The table from Step 1 of the page. Then the four rules, one at a time.

**Say:** "A clue is something the crew learns in one place | that changes what happens in
another. || You've already written one, | when Mark the Gallery put a place on the map. ||
Today there are two new words. || Learn, on an answer, writes a word down for this crew. |
And learned, on another answer, counts the words. ||| It can count them, | or it can
ask for one word by name. || What's learned in a call goes on one list, for the whole game. || And here's the rule
that shapes everything: | the game reads the count when the crew opens the scene, and only
then. || If they open a call too early, | going away and coming back doesn't help. || So
the clue has to come first on the road. ||"

### 3. The first clue

**Screen:** `mission.amd`. Type The Ring Plate below The Niche. Type Marker Zero below
Marker One. Type Rook at the Ring below The Rest of It. Highlight `; learn names`.

**Say:** "Every ship flies through the ring, | so the first clue goes there. || It takes a
place, on the same spot as the ring, | with a role of its own, plate. || It takes a beat,
the same as last time: | when a ship is within five hundred of the plate, Rook calls. ||
And it takes the scene, with one take and two answers. ||| Here's the new part. | After
Log the names there's a semicolon, | and then learn names. || Names is my word, and the
crew never sees it. | What they see is Log the names. ||"

### 4. The clue opens an answer

**Screen:** Rook at the Altar. Add the middle answer. Highlight `if learned >= 1`. Type
The Entry for Dace.

**Say:** "Now the altar gets one new answer, | between the two that are there. || It says
play the entry keyed to Dace, | and after the round brackets comes a condition: | if
learned is at least one. || So a crew that knows nothing gets two answers, | and a crew
that logged the names gets three. ||| The answer leads to a new scene. || It has one take:
| Dace didn't come out, and there's a cairn in a side room. || And it has one answer,
which leads on to The Rest of It, | so this crew still hears the main recording. ||"

### 5. A side room, and the place in it

**Screen:** Relics section. Type The Crypt and The Cairn. Then add `; reveal cairn` to
Mark the side room. Highlight `cairn` in the heading and in the answer.

**Say:** "He said a side room, so there has to be one. || It's a chamber, six hundred,
with a passage to the Nave, | and that's Lecture 2. || In the middle of it there's a
place, with a cone standing on it, | and that's Lecture 3. ||| Now the answer shows it,
with reveal cairn. || That's the key of the place, and not crypt. | A room isn't a place,
and lint won't tell you. ||"

### 6. The side story

**Screen:** Quests section. Type The One Who Stayed below Marker Zero. Add `, accepts
stayed` to the answer. Then the "other kind" table from the page, with the Storm's Beacon
record above it.

**Say:** "A side story is a quest that isn't part of the main story. || It has three
hashes. | It starts when revealed, so it's asleep and out of the list. || And it's done
when a ship is within four hundred of the cairn. ||| The answer starts it, with a comma
and then accepts stayed. || That's two things after one semicolon. ||| Now, in the game's
shipped ruins you'll find a section called Side Stories, | and those are a different
animal. || Each one says For, and a job. | They belong to one person, | and they're handed
over when that person leaves the ship in a suit. || So leave that section for now. | You'll
type one at the end of the class, in Lecture 10. ||"

### 7. The cutscene: what you write

**Screen:** The end of `mission.amd`. Type the Cutscenes section: the cutscene, then the
two shots. Highlight `Cutscene: cairn_scene` on each shot, then `Subject:`, then
`Framing:`, then the line under each fence.

**Say:** "A cutscene is a list of shots. || It's a new section, and its key has to be
cutscenes. || The first record is the cutscene itself, | with its key, and Letterbox yes
for the black bars. || Then there's one record for each shot. ||| A shot says which
cutscene it belongs to. | It says what the camera looks at, | and that's a role, the same
word I write after reach. || It says how near: close, medium or wide. | Two words with a
comma make a move, from wide to close. || It says how many seconds. || And Overlay, lower
third, puts words at the bottom: | a name, and under the fence, the line. ||| Everywhere
else in this file, that line is my own note. | Here, the crew reads it. || So keep the
cutscene short, because the crew can't skip it, | and keep each line short too. ||"

### 8. The card

**Screen:** Command prompt: `sbs lint MyRuin`, the `section-not-loaded` warning. Switch to
`story.mast`. Paste the two lines under `relics_spawn`. Lint: clean. Back to `mission.amd`:
add `Then: signal cairn_found` to The One Who Stayed. Lint: the `signal-no-route` warning.
`story.mast` again: scroll to the end, paste the block. Lint: clean.

**Say:** "I run lint first. || It says nothing in this mission reads a section keyed
cutscenes. | It's right, and the end of its sentence is the fix: | add the line that reads
it. ||| That's a card, in two parts. || Part one goes in the map block, | under the line
that builds the ruin, | and I don't change a letter of it. || Lint is clean now. | The
section is read, and still nothing plays it. ||| So the quest has to say when, | with
Then, signal, cairn found. || That's my word, and lint warns again: | the word is sent,
and nothing hears it. || Part two goes at the very end of the story file. | When that word
is sent, it plays the cutscene with this key, on every main screen. || Two things in it
are mine, the word and the key. | And lint is clean. ||"

### 9. Lint

**Screen:** Three breaks, each undone. Change `if learned >= 1` to `if learned => 1`,
save, lint, read the warning. Change `Subject: cairn` to `Subject: carin`, save, lint:
clean; then show the line from `mast.runtime.log` on the page. Change
`Overlay: lower_third` to `Overlay: lowerthird`, save, lint: clean.

**Say:** "Now for three breaks. || First, I turn the sign round, | and lint tells me that
it can't read that condition. || That's good, because that answer would never have been offered.
||| Next, I misspell a subject, and lint says clean. || Lint reads the outside of a
cutscene, | and not the inside of a shot. || That shot would be left out, | and the game
does say so, in one line, in its log, after you've played. ||| Last, I misspell the
overlay. | It's clean again, and this time nothing says anything: | the shot plays with no
words. || There's a table on the page of the ones nothing tells you about. | Read it
before you play. ||"

### 10. Play it

**Screen:** Command prompt: `sbs run server,helm,comms -m MyRuin map=0`. Fly to The
Hollow, through the ring: the call. Log the names. On to The Vault: the call, three
answers. The entry, Mark the side room, Mark the Gallery. Helm's map. The quest list. Back
across The Nave into The Crypt. The main screen: the bars, the altar and its two lines,
the cairn and its two lines, the ship's view again. Point at the panel in the top left
corner while it reads `The Altar`.

**Say:** "Through the ring we go, and there's Rook, at the ring. | I log the names. ||
Across the Nave and up the tunnel, | and there's Rook at the altar, with my third answer.
|| I take the entry for Dace, and I mark the side room. | Then the rest of it, and I mark
the Gallery. ||| There's a new contact on the far side of the Nave, | and a new quest in
the list. || So back down, straight across, and into the side room. ||| And there it goes.
|| The bars come up. | The altar: the tally on the rim stops at forty-one. || The cairn:
forty-one stones, one for each day. || And then we're back. ||| One thing you'll notice is that
panel in the corner. | It says The Altar, energy zero. || It's the ship's own panel,
reading whatever the camera is on. | It isn't in my file, and I can't take it away. ||"

### 11. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Give Rook a line that only a crew who knows will hear. ||
Pay for the side story, and add a third shot. || Then break one line where lint can see
it, | and one where it can't. ||| Next time, the main story. ||"
