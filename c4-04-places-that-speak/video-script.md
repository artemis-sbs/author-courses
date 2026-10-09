# C4-4 video script - Places that speak

> **STATE ON 2026-10-08. Read this first.**
>
> - **Everything this page needs is released.** The page is written for Artemis Cosmos
>   1.4.0, installed from Steam or itch.io, with a current tool and libraries. Record on
>   such an install.
> - **The student's mission is `MyRuin`** as Lecture 3 left it: a fresh
>   `sbs create MyRuin -t amd` mission whose `mission.amd` is
>   `c4-03-dressing-a-ruin\example\mission.amd` (141 lines). The game is started with
>   `sbs run server,helm,comms -m MyRuin map=0`.
> - **`mission.amd` only.** `story.mast` is never opened: the template reads the
>   Characters and Dialogue sections (lines 48 and 49).
> - **`example\` holds the one file that differs from the start:** `mission.amd` (199
>   lines).
> - **A DECISION IS STILL OPEN (plan item B78).** A place's own `Scene:` is opened by one
>   thing only: a crew member's suit arriving at the place. A ship does not open it, and a
>   template mission cannot put anyone in a suit until Lecture 8. So this lecture teaches
>   the place calling the SHIP through a beat, and has the student write the place's own
>   words and check them with lint. Scene 7 cannot be shown in the game. Say so, as the
>   script does.

> **Re-measured 2026-10-08, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `ae2bbf4a`). The page's steps were typed one
> at a time onto Lecture 3's finished file, with lint after each. Then the pilot's 76
> one-change variants of the finished file: each linted, each played headless. The probe
> has two parts. The ship part moves the ship to 900 and then 500 from The Altar, opens
> the call with the game's own functions and takes the answers. The suit part puts a crew
> member in a suit the way the library's own test does, ends its route at the place and
> runs one pass of the autopilot. The lesson's mission cannot do the second part itself.

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script)**, on the first
> version of this file; the records this lecture adds have not changed. All 29 lines of
> the probe's report matched the mock: no call at 900, the call at 500 in Surveyor Rook's
> name, "Mark the Gallery." lights The Niche, no second call, the ship never opens the
> place's own scene; and with a probe-made suit the scene opens on arrival, branches,
> closes, and a later arrival reads the `Scan:`. `mast.runtime.log` was empty. Nothing
> was SEEN on a console.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 3 leaves it: The Hollow with The Ring, The Way In, The Altar and The Niche. No Characters section and no Dialogue section yet. `mission.amd` has 141 lines |
| Lint | `sbs lint MyRuin` says `clean` |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library. "Engine" is the run of 2026-10-04 in the note above. If an item fails while
recording, stop and fix the page.

1. Lint is `clean` after each of Steps 2 to 6. Half way through Step 6, with `Scene:`
   typed on The Altar and the scene not yet written, lint says `dangling-scene`. (Lint.)
2. The ship 900 from The Altar: no call, and The Altar's marker is lit. At 500: one call
   is waiting, named `Surveyor Rook`, titled `A recording at the altar`. (Mock, Engine.)
3. Opened, one take is said and two answers are offered. "Play the rest." leads to the
   second scene. "Mark the Gallery." ends the call and lights The Niche's marker, with the
   ship 5300 away from it. "Shut it off." ends the call and lights nothing. (Mock,
   Engine.)
4. The ship sent away and brought back to 100 from The Altar: no second call. Marker One
   is not in the quest list before or after. (Mock, Engine.)
5. The ship on top of The Altar never opened "At the Altar", and nothing was written to
   `mast.runtime.log`. (Mock, Engine.)
6. With no number after `reach altar`, the call was waiting with the ship at The Way In,
   4082 from The Altar. (Mock.)
7. A probe-made suit arriving at The Altar opens `altar_look` for that console: one take,
   two answers. "Read the marks on the rim" leads on; "Step back" closes it. A second
   console arriving afterwards reads the `Scan:` line. The first console arriving again
   reads nothing new. A second console arriving while the scene is open joins it. (Mock,
   Engine.)
8. Every row of the three tables in Step 7: lint for all of them, and the mock for what
   the game does. (Lint, Mock.)
9. The exercise, as written: lint `clean`. The second call comes at The Niche, "Log it."
   completes What Rook Left, and What Rook Left is in the quest list from the start.
   (Lint, Mock.)

Read in the library's code, not measured: another suit within 600 of the one that arrives
is pulled into the scene; a suit flying past a place does not open its scene; the handheld
has no button that closes a place's scene; the call goes to every player ship.

Not seen by anyone. If one is not as described, stop and fix the page:

1. The Incoming Hails list on Comms with the row "Surveyor Rook - A recording at the
   altar", and when it appears as the ship enters The Vault.
2. The open call: his face, his name, the take, and the two answers below **Back**.
3. Whether the call is also drawn on the main screen.
4. The Niche turning into a gold contact on Helm's map when Comms picks "Mark the
   Gallery.", and whether Helm's map is zoomed far enough out to show it from The Vault.
5. The order of things in the tunnel: The Altar's contact first, the call after.
6. Rook's face from one game to the next. `Face: terran_male` gives a new face each game.
7. Anything at all on a crew member's handheld. The whole of Step 6 is unseen, and stays
   unseen until Lecture 8.

> Keep off camera: suits. Nothing in this recording should put a crew member outside the
> ship. And do not type `Speaker: altar`: lint and the game read that word differently,
> and the page does not teach it.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. Helm flying up the tunnel into The Vault. Cut to Comms: one row in
the Incoming Hails list, "Surveyor Rook - A recording at the altar". Open it.

**Say:** "Last time, this room had a name. | Today, it has something to say. || I flew the
ship into the Vault, | and a recording forty years old started to play. ||| I didn't write
a line of code for that. || I wrote who's speaking, what he says, | and how close the ship
has to be. ||"

### 2. Two listeners

**Screen:** The table from Step 1 of the page.

**Say:** "A place in a ruin can speak to two different listeners. || One is the ship,
which means the bridge, | and that arrives on Comms as a call. || The other is a person, |
a crew member who's gone outside in a suit and is standing there, | and that's read on
their handheld. ||| The two are written differently. || And here's the thing to know
before we start: | your crew doesn't leave the ship until a later lecture. || So today
you'll write both, and you'll play one. | The other one, lint checks for you, and it
waits. ||"

### 3. A voice

**Screen:** `mission.amd`, end of the file. Type the Characters section and Surveyor Rook.

**Say:** "A call is placed by somebody, | and a table of stone isn't a somebody. || So I
give the place a voice. || Forty years ago a survey team found this ruin, | and their
leader left recordings in it. ||| He's a character, written the way you wrote characters
in Class 2, | and his key is rook. ||"

### 4. What he says

**Screen:** Type the Dialogue section: Rook at the Altar, then The Rest of It. The second
scene's first answer is typed without `; reveal niche` for now.

**Say:** "Now the scene, and all of this is Class 2. || The speaker is his key. | When is
hail, because this is a call that comes in. || There's a title, which the crew reads
before they open it. || There are two takes, and the game picks one. ||| Then come two
answers. | One leads on to a second scene, by its key, | and one ends the call. || The
second scene has no When line and no title, | because the only way into it is that answer.
||"

### 5. The place makes the call

**Screen:** Scroll up to the Quests section. Below Study the Derelict, type Marker One.
Then show The Altar's record and point at `Roles: altar`.

**Say:** "A scene is only words on a page, until something places the call. || In Class 2
that was a beat, waiting to be revealed. | This beat waits for the ship to get somewhere.
|| It has three hashes, so it isn't a step of First Contact, | and the word Beat is on its
first line. ||| Then comes the line that matters: | starts when, reach altar, six hundred.
|| Altar is a role. | It's this word here, on the place's Roles line, | and not its key or
its name. || For the Way In those differ: | the key is way in, and the role is entrance.
||| Six hundred is how close. || The altar is in the middle of the Vault, | and the wall
is seven hundred out, | so six hundred means the ship is in the room. || Always write that
number. | Leave it out and the game uses five thousand, | which is bigger than the whole
ruin. || Last comes Action, which says who calls, | then the word hails, and then the scene. ||"

### 6. An answer that changes the map

**Screen:** Back to The Rest of It. Add `; reveal niche` to the first answer. Show The
Niche's heading and point at `(niche)`.

**Say:** "You know what an answer can do: | it can start a quest, finish one, or send a
word. || In a ruin there's one more, | which is reveal, and then a place. || Remember the
Niche, the place I hid last time. | It only showed up when the ship was nearly on top of
it. || With this answer, it shows up when Comms says so. ||| Now be careful here. | Reveal
takes the place's key, the word in round brackets, | and reach took its role. || That's
two lines, and two different words for the same place. ||"

### 7. The place's own words

**Screen:** The Altar's fence. Add `Scene: altar_look` and the `Scan:` line. Then the end
of the file: type At the Altar and The Marks.

**Say:** "Now for the other listener. || Somebody is standing at this table, and nobody's
calling them. | What they read is what they see. || On the place I add two lines. | Scene
is the key of a scene, | and Scan is one line about the place, | for whoever comes after
the scene has been played. ||| The scene itself has no fence at all. || There's no
speaker, because nobody's speaking, | and no title, because it isn't a call. || One rule
is new: | every path through a place's scene has to end in an answer with empty brackets,
| because nothing else closes it. ||| This opens when a crew member's suit arrives here,
and not when the ship does. || So I can't show it to you today, | and you can't play it
today. || We come back to it when the crew can leave the ship. ||"

### 8. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Then three breaks, each undone.
Change `reach altar 600` to `reach alter 600`, save, lint, read the warning. Change
`Scene: altar_look` to `Scene: altar_lok`, save, lint, read the warning. Change
`; reveal niche` to `; reveal nich`, save, lint: clean.

**Say:** "So I run lint, and it's clean. || Now I break the role, | and lint tells me that
nothing in the mission wears a role called alter. || That's good, because that call would
never have come. ||| Next I break the scene on the place. | Lint tells me the Altar points
at a scene that isn't there, | and that's how I check the half I can't play. ||| Now the
word after reveal, and lint says clean. || Lint doesn't check that word, | and the game
would say nothing either. | The answer would end the call, and the Niche would stay dark.
|| So read two things yourself, every time: | the word after reveal, | and that there's a
number after the role. ||"

### 9. Play it

**Screen:** Command prompt: `sbs run server,helm,comms -m MyRuin map=0`. Helm's map: The
Hollow. Fly in, through the ring, across The Nave, up the tunnel. The Altar appears on the
map. Keep going into The Vault. Cut to Comms: the row appears. Open it. Play the rest.
Mark the Gallery. Cut to Helm's map: The Niche.

**Say:** "In through the Mouth we go, and across the Nave. || Up the tunnel, and there's
the Altar on the map, | the same as last time. || Now into the room. ||| And on Comms,
there's a call: | Surveyor Rook, a recording at the altar. || I open it, and I get one of
my two takes. || I play the rest, and then I mark the Gallery. ||| Back on Helm, there's
the Niche, | and we haven't been near it. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Give the Niche a recording of its own, and words of its
own. || Make one answer finish a quest. || Then break one line where lint can see it, |
and one where it can't. ||| Next time, the crew learns something in one room, | and uses
it in another. ||"
