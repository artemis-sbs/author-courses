# C4-7 video script - Quests through a ruin

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`** as Lecture 6 left it: a fresh
>   `sbs create MyRuin -t amd` mission whose two files are
>   `c4-06-clues-side-stories-cutscenes\example\mission.amd` (296 lines) and `story.mast`
>   (116 lines). The first version of this lecture started from Lecture 4's file; the
>   class is a chain now, so the ring recording, the side story and the cutscene are in
>   the file and in the game while this lecture is played. The game is started with
>   `sbs run server,helm,comms,science -m MyRuin map=0`.
> - **`mission.amd` only.** `story.mast` is not opened.
> - **`example\` holds the one file that differs from the start:** `mission.amd` (395
>   lines).
> - **Scene 9 ends a game.** A recording take adds a line to the game's own
>   `game_results.yaml`. That is fine for a real play; say nothing about it.
> - **Do not teach the spelling in Storm's Beacon's `EPISODE_TEMPLATE.md`.** It writes
>   `State: secret` and `When: reach <role> <n>` for a step. Such a step appears when the
>   ship arrives and never finishes; lint names it (`quest-never-finishes`). The page says
>   so in its Further reading.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were typed one
> at a time onto Lecture 6's finished files, with lint after each. Then the pilot's 56
> one-change variants of the finished file, and six new walks that only exist now that
> the ring call and the side story are in the file: each linted, each played headless by
> a probe that moves the ship, opens calls with the game's own functions, forces a Science
> scan, and prints every quest's state, the quest list, the calls waiting, the side's
> credits and what the crew is told.

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script)**, on the first
> version of this file, which had no ring call and no side story; the records this
> lecture adds have not changed. All 73 report lines as in the mock: the door at 600, the
> altar at 500 finishing the step and placing the call together, "Mark the Gallery."
> lighting the niche, the niche at 300, the second call, "Take it aboard.", a win with 500
> credits; `mast.runtime.log` empty. ONE DIFFERENCE from the mock: in the engine The
> Altar's scan text was already there on the first read, so the ship's sensors scan a
> place by themselves once it is lit. Nothing was looked at on a console.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 6 leaves it, lint clean. Lecture 4's exercise NOT done (no Marker Two, no What Rook Left, no Rook at the Niche). `mission.amd` has 296 lines |
| `story.mast` | Lecture 6's, 116 lines, with the card. Never opened in this lecture |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console, a Comms console and a Science console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. "Engine" is the run of 2026-10-04 in the note above. If an item fails while
recording, stop and fix the page.

1. Lint is `clean` after each of Steps 2 to 6. Half way through Step 4, with the two
   steps typed and no `Then:` line on Find the Way In, it says `never-revealed`. (Lint.)
2. At the start the quest list holds The Hollow Survey and one step, Find the Way In. The
   other three steps and The One Who Stayed are hidden. (Mock.)
3. The ship 1500 from The Way In: nothing. At 600: Find the Way In is done, the side has
   50 credits, The First Marker is running. (Mock, Engine.)
4. At the ring: Lecture 6's call is waiting, and nothing in the survey changes. (Mock.)
5. 900 from The Altar: the step is not done. At 500: The First Marker is done (100
   credits), The Second Marker is running, and "Surveyor Rook - A recording at the altar"
   is waiting. A forced Science scan of The Altar reads the Altar Reading text. (Mock,
   Engine.)
6. "Play the rest." then "Mark the Gallery." lights The Niche. 900 from it: not done. At
   300: The Second Marker is done (200 credits), What Rook Put Back is running, and
   "Surveyor Rook - A second recording" is waiting. (Mock, Engine.)
7. With the ring call and the altar call both unanswered, the second recording is listed
   first, then the altar call, then the ring call. (Mock.)
8. "Take it aboard." closes the call, finishes the step (500 credits) and the arc, and
   ends the game as a win with the `Win:` sentence. The same with the names logged at the
   ring and the side story started and unfinished; the same with the side story finished
   and its cutscene played first. (Mock; the first of the three, Engine.)
9. With `Fails when: 20 seconds` and the ship sitting still, the game ends as a loss with
   the `Lose:` sentence. (Mock.)
10. The niche before the altar: nothing is finished. After the altar, back at the niche:
    The Second Marker finishes. "Shut it off." at the altar: The Niche stays dark, and at
    300 from it the step finishes. (Mock.)
11. Science, by a forced scan of the place's contact: before the contact lights it is
    marked as not selectable; after, it is selectable; the `scan` tab reads the Altar
    Reading text, and with the exercise's record the `intel` tab reads its text. (Mock.)
12. Every row of the tables in Step 7 and the four "not mistakes": lint for all of them,
    and the mock for what the game does. (Lint, Mock.)
13. The exercise as written (items 1, 2 and 3 together): lint `clean`. "Take it aboard."
    pays to 500 and does not end the game; back at DS 1 the game is won with 600. "Leave
    it where he put it." ends the game as a loss with the reworded sentence. (Lint, Mock.)
14. The same four steps typed directly below Marker One, where the first version of this
    page put them, play the same. (Mock.)

Read in the library's code, not measured: the game looks for `reach` every two seconds
(the page's "keep the number at 300 or more" is advice built on that); an answer's
`; reveal` makes the contact selectable the same way coming close does. Twenty minutes:
the clock was measured at 20 seconds only.

Not seen by anyone. If one is not as described, stop and fix the page:

1. The quest list on a console: The Hollow Survey with its steps under it, each new step
   appearing, and The One Who Stayed beside it.
2. Science selecting The Altar and reading the `scan` tab. In the engine the ship's own
   sensors had scanned the lit place by themselves; nobody has seen Science select one.
3. The second recording at the top of the Incoming Hails list, above the others.
4. The end screen with the `Win:` sentence, and with the `Lose:` sentence, for THIS
   mission. Class 1 saw the end screen show a quest's sentence.
5. Where the `Quest complete:` lines are drawn.
6. How long the flight takes. Nobody has flown it. If twenty minutes is tight on camera,
   say so and change the number in the page.
7. Everything Lecture 4's script lists as unseen: the call's row, the open call, The Niche
   turning gold on Helm's map.

> Keep off camera: suits, and picking anything up. And a step that finishes on a scan
> (`Done when: scan 1 altar`): Class 1, Lecture 10 already tells the student why not to
> write one.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. The quest list: The Hollow Survey, one step. Cut to Helm flying into
The Vault, then the quest list with three steps. Cut to Comms: "Take it aboard." Cut to
the end screen.

**Say:** "Last time, the ruin kept a secret. | Today, it has a story. || There are four
steps, one after another, | each in a different part of the ruin. || The crew is paid for
each one, and the last one ends the game. ||| And I didn't open the story file once. ||"

### 2. What an episode is

**Screen:** The first table from Step 1 of the page, then the second.

**Say:** "There's a shipped campaign made of ruins like this one. || Each ruin in it is one
episode, | and every episode is the same chain. || First the approach, where the crew
comes up to the way in. | Then a call, from somebody who knows the place. || Then a room,
and a call, and a room. | And at the end comes the piece, | where they take away what the
ruin was hiding. ||| You can already write every link in that chain. || What's new today
is where the last word comes from. | Nobody can leave the ship yet, | so today, Comms says
it. ||"

### 3. The heading

**Screen:** `mission.amd`, Quests section. Below The One Who Stayed, type The Hollow
Survey.

**Say:** "The story needs a heading, | and I put it below the last quest in the section.
|| It's an arc, with three hashes, | and the word Arc alone on the first line. || It
starts at once, and it fails after twenty minutes. || There's a Win sentence for when it's
finished, | and a Lose sentence for when it fails. ||| All of that is Class 1. || Nobody
warns the crew about the clock, | so I say twenty minutes in the description. ||"

### 4. The way in

**Screen:** Type Find the Way In. Then scroll to The Way In in the Relics section and
point at `Roles: entrance`, then at `(way_in)`.

**Say:** "Here's the first step. | It has four hashes, so it belongs to the arc. || And
this is the line that matters: | done when, reach entrance, one thousand. ||| Before, I
wrote that sentence in a Starts when line, to start a beat. || Here it's in a Done when
line, so it finishes a step. || The rules haven't changed. | Entrance is a role, the word
on the place's Roles line. || This place's key is way in, | and the key doesn't work here.
Lint will tell you. ||| A thousand is how close, and always write the number. || Without
it the game uses five thousand, | and the step is finished before the crew has seen the
ruin. || One more thing, for numbers inside a ruin: | the game looks every two seconds, |
so don't go below about three hundred. ||"

### 5. Room by room

**Screen:** Type The First Marker and The Second Marker. Go back to Find the Way In and
add `Then: reveal survey/first`. Scroll up to Marker One and highlight its
`reach altar 600`, then the step's.

**Say:** "Now two more steps. || Both say starts when, revealed, so they're asleep. || The
way in reveals the first, | and the first reveals the second. || It's the full address
every time: | the arc, a slash, the step. ||| Now look at this. | Reach altar, six
hundred, is in my file twice. || On the beat, it starts the call. | On the step, it
finishes the step. || They happen together, when the ship comes into the Vault: | the step is
done, and Rook is on Comms. ||| The second step sends the ship to the Niche, the place I
hid. || The crew can find it because Rook tells them, | or because they go and look. || So
if Comms shuts the recording off, | the story can still be finished. ||"

### 6. The step that waits for a word

**Screen:** Type What Rook Put Back. Add `Then: reveal survey/take` to The Second Marker.
Go to the Dialogue section and, below The Entry for Dace, type Rook at the Niche and What
It Is. Highlight `signal hollow_taken` in the step and in both answers.

**Say:** "The last step is the piece, where somebody takes the thing. || Nobody can leave
the ship today, | so this is a decision Comms makes. || The step says done when, signal,
hollow taken. | It waits for a word, and that word is mine. || And it has an Action: | the
moment the step starts, Rook calls with a second recording. ||| Now for the scene. || One
answer asks what it is, and leads to a second scene. | The other says take it aboard, |
and after the semicolon, it sends the word. || The step hears it and pays, | and it was
the last step, so the game is won. ||| Look at the ways out of this conversation. | There
are two, and both send the word. || I did that on purpose. || If I add an answer that just
hangs up, | a crew that picks it has spent the call, | and the step can never be finished.
|| The crew's way of saying not now is the Back button. ||| So why a word, and not the
way Class 2 did it? || Because the step doesn't care who says the word. | When your crew
can go and take the bowl by hand, | this step won't change by one letter. ||"

### 7. What Science reads

**Screen:** The Scans section. Type Altar Reading and Niche Reading. Then show The Altar's
fence in Relics and point at its `Scan:` line.

**Say:** "Two lectures ago I put a Scan line on the Altar. || That's for a person standing
there, | and the Science console on the ship doesn't show it. || Science reads scan
records, the ones from Class 1. ||| A place wears a role, | and a role is all a scan
record needs. || So I write Scan of, the role, a tab, and a reading. || That's one line on
the place for a person, | and one record in Scans for the ship. ||"

### 8. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Then three breaks, each undone.
Change `reach entrance 1000` to `reach way_in 1000`, save, lint, read the warning. Change
`Then: reveal survey/first` to `Then: reveal first`, save, lint, read the warning. Delete
`Part of:` and `Required:` from What Rook Put Back, save, lint: clean.

**Say:** "So I run lint, and it's clean. || Now I use the key where the role goes, | and
lint says nothing in this mission wears a role called way in. || That's good, because that
step would never have finished. ||| Next I drop the arc from a reveal line. | Lint tells
me what the step is called to the game, | and to write that. ||| Now I take these two
lines off the last step, and lint says clean. || And this one matters. || The other three
steps still say they're required, | so the game decides the arc is finished when those
three are. || The crew wins at the niche, with the last call still ringing. ||| Lint can't
see that. || So read your steps: | all of them have the two lines, or none of them do. ||"

### 9. Play it

**Screen:** Command prompt: `sbs run server,helm,comms,science -m MyRuin map=0`. The quest
list. Fly to The Hollow: the first step completes. In through The Mouth and the ring: the
ring call arrives; leave it. The Nave, up the tunnel: the second step completes, Comms has
the altar call. Science: select The Altar. Comms: open the altar call, Play the rest, Mark
the Gallery. Fly to The Gallery: the third completes, the second recording arrives at the
top of the list. Take it aboard. The end screen.

**Say:** "There's one step in the list, so I fly to the door. || It's done, and paid, and
here's the next. || In through the Mouth, and through the ring. | That's last lecture's
recording calling, and I'll leave it for now. ||| Across the Nave and up the tunnel. | The
step is done again, and Rook is calling from the altar. || On Science, I select the Altar,
and there's my reading. || On Comms, I play the rest, and I mark the Gallery. ||| Back
across the Nave, into the built room, and to the far end. || That's the third step, and a
second recording, at the top of the list. || I take it aboard. | And that's the game. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Give the Altar a second tab. || Add a fifth step that
carries the bowl home. || Give the crew a way to lose on purpose. || Then break one line
where lint can see it, | and one where it can't. ||| Next time, the crew goes outside. ||"
