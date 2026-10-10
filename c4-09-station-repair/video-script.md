# C4-9 video script - EVA elsewhere: a repair outside a station

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released** (2026-10-09): `Repair:` on a relic, the
>   word `<key>_repaired`, the Fire app's `Repair:` row. The page is written for Artemis
>   Cosmos 1.4.0, installed from Steam or itch.io, with a current tool and libraries.
> - **NOBODY HAS DONE A REPAIR AT A CONSOLE.** Station repair was built today. Every
>   screen in scene 8 is unseen. Record scene 8 FIRST, and fix the page where the screen
>   differs.
> - **The student's mission is `MyRuin`** as Lecture 8 left it:
>   `c4-08-eva\example\mission.amd` (478 lines) and Lecture 6's `story.mast` (116 lines).
>   The game is started with `sbs run server,helm,comms -m MyRuin map=0`.
> - **`mission.amd` only.**
> - **`example\` holds the one file that differs from the start:** `mission.amd` (526
>   lines).
> - **Why the worksite is in the same mission:** decided once, for the class. The Relics
>   section builds every relic in the file, so a second one costs four records; and two
>   doors in one mission is where a real fault shows (Step 5), which a separate mission
>   would have hidden.
> - **The exosuit can close a client** the first time it appears (an engine fault,
>   reported). Lecture 8's page has the one line that switches to a stock hull.
> - **This lecture does not end a game.**

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `e84602e7`, Legendary Missions `b37a320`).
> The page's steps were typed one at a time onto Lecture 8's finished file, with lint
> after each. Then 32 one-change variants of the finished file, each linted and most
> played headless.
>
> **What the script did.** The same as in Lecture 8: a stand-in console connected the way
> the mock's own browser bridge connects one; the function behind the Boarding Party
> app's button; the suit's own list and `eva_goto`; the Nav, Scan and Fire apps' own
> drawing functions with the widget calls recorded; `eva_use`, which is what a press in
> the Fire app calls; the function behind COME ABOARD. The suit FLEW from the airlock to
> the mast on its own autopilot (533 units, under 25 seconds). In the other variants the
> script put the suit at the job. A ship's shot at a job's marker was the engine's
> `destroyed` event, handed to the game's own dispatcher.
>
> **Where the ship starts.** The script put the ship 1400 from the airlock. Left where the
> game put it, the ship was 4342 from the airlock with this lecture's finished file, and
> 2322 with an earlier draft of it: the start is somewhere near DS 1 and not a fixed spot.

> **Seen in the real game's SERVER, with no console (2026-10-09, another session)**, on
> Legendary Missions' own test maps: a worksite built from a relic file and its repair
> jobs passing their checks. Not this mission, and no screen.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 8 leaves it, lint clean. `mission.amd` has 478 lines |
| `story.mast` | Lecture 6's, 116 lines. Opened once, read only, in scene 3 |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 8 with a server, a Helm console and a Comms console |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library, driven as described above. If an item fails while recording, stop and fix the
page.

1. Lint is `clean` after each of Steps 2 to 5, and with the exercise's two jobs. (Lint.)
2. The library builds two relics, `hollow` and `yard`. The worksite has no wall objects
   and no cloud. The names on the map are DS 1 Worksite at 0, 0, -1200 and The Hollow at
   0, 0, 19300. (Mock.)
3. With the ship 1400 from the airlock, the offer is DS 1 Worksite and the button reads
   SUIT UP. At 3300 nothing is offered. At the door of The Hollow the offer is The Hollow.
   (Mock.)
4. SUIT UP puts the crew member at 0, 0, -1200 in the room The Work Area. The suit's list
   is one row, `Survey Mast   533`. The suit flies there and stops about 260 from the
   job. (Mock.)
5. The Fire app lists `Repair: Survey Mast   260` and the line under the list ends
   `A Repair takes the tool it names.` The tether is refused. The beam starts, the banner
   reads `REPAIR - Survey Mast, 12s`, and the suit's weapons are not locked on anything.
   Fourteen seconds later the job is done, the library has sent `mast_repaired`, Raise the
   Mast is done and the side has 40. (Mock.)
6. Find the Way In is still running after all of that. (Mock.)
7. On Step 4's file, with both doors wearing `entrance` and the step at
   `reach entrance 1000`: the ship 800 from the airlock finishes Find the Way In and pays
   50; so does a suit that comes out of the airlock. (Mock.)
8. Every row of the tables in Step 6 and the five "not mistakes": lint for all of them,
   and the mock for what the game does. (Lint, Mock.)
9. The exercise: three jobs on the list; at the valve the row ends `(wrong tool)` with the
   beam in hand, WORK is offered, the banner reads `REPAIR - Coolant Valve, 6s`, and the
   roll is written to the transcript (`engineering 0, rolled 5: 5 vs 9, failure.` in one
   run, `rolled 10: 10 vs 9, success.` in another). A second try straight after a miss is
   refused; after 22 seconds it is taken. The panel is done with the tether. A shot at the
   panel's marker removes the marker and leaves the job to do. (Lint, Mock.)
10. Lecture 8's whole walk still ends in a win with 700, with the worksite in the file.
    (Mock.)

Read in the library's code, not measured: twenty seconds is the wait after a miss; a
crew member's skill number comes from their roster record's `Skills:` line; other suits
within reach with the same job add to a roll.

Not seen by anyone. If one is not as described, stop and fix the page:

1. Everything Lecture 8's script lists: the Boarding Party app, the suit's console, the
   suit, the apps.
2. DS 1 with a suit beside it. Whether the suit's route keeps clear of the station as
   drawn (the `Solid:` is a ball of 500; nobody has compared it with the model).
3. The job's marker. It is an unscaled plain sphere; nobody knows what it looks like, or
   whether it can be seen at all.
4. The Fire app's `Repair:` row and the `REPAIR` banner.
5. Whether the suit's beam is seen to fire at the mast. The suit does not lock its
   weapons on a job, on purpose; what the engine then draws is unknown.
6. The name DS 1 Worksite on Helm's map, beside the station's own name.

> Keep off camera: `Dress:` on a job. The documentation says a dressed job stays in place
> when it is done; in the mock the dressed marker was gone like a plain one. Not on the
> page.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. The ship near DS 1. A handheld: SUIT UP, DS 1 Worksite. Cut to a
suit beside the station. Cut to the Fire app: "Repair: Survey Mast", then the countdown.
Cut to the quest list: Raise the Mast, done.

**Say:** "Last time the crew went into a ruin. || Today there's no ruin at all. ||| It's
the same suit, and the same tools, | outside a station, on a repair job. || A crew member
comes out of the airlock, | flies round the hull, and welds a mast. ||| And it's one more
record than you already know. ||"

### 2. A ruin with the ruin turned off

**Screen:** The first table from Step 1 of the page, then the second.

**Say:** "A crew member can go outside wherever the game has a space to fly a suit in. ||
That's what a ruin's records are: | rooms, a way in, and places to go. ||| So a worksite
is written as a ruin, | with everything that looks like a ruin switched off. || It has no
walls, no drifting rock, and no cloud. || One room to work in, | and one solid lump where
the station is. ||| And there's one new record, the job. || It's written like the barrier
from last time, | but it's never in anybody's way. ||"

### 3. The worksite

**Screen:** `mission.amd`, Relics section. Below The Fallen Slab, type the four records:
DS 1 Worksite, The Work Area, The Station, The Airlock. Then `story.mast`, the line that
places DS 1 at 0, 0, 0, read only.

**Say:** "Here are four records. || The first is the worksite itself. | It has no Relic
line, so it's a second ruin, beside the Hollow. || It sits at zero, zero, zero, | which is
where the template puts the station. || It says walls, none, and debris, zero, | and it
has no Atmosphere line. ||| Then one round room, fifteen hundred across from the middle.
|| Then comes a solid, | which takes the middle five hundred back out, | so a suit flies
round the station and not through it. ||| And last the airlock. || It wears the role
entrance, | so it's where the suit appears, | and where suit up is measured from. ||"

### 4. When the offer is made

**Screen:** The section "When SUIT UP is offered here" on the page.

**Say:** "The rule is the one from last time. | The ship has to be within three thousand
of the entrance. ||| Now, a ship doesn't always start that close. || In my two tests it
started twenty-three hundred away, | and then forty-three hundred. || So if the app offers
nothing, fly toward the station. ||| And with two ruins in one mission, | the offer
follows the ship. || It's the worksite here, and the Hollow at the Hollow. ||"

### 5. The job

**Screen:** Below The Airlock, type Survey Mast. Highlight `Repair:` and `Clear with:`.

**Say:** "Now for the job itself. || Repair, three numbers for where, and one for how big.
|| I've put it just outside the hull, on the airlock's side. ||| It says Clear with, beam,
| so the crew member welds it. || The tools are the ones from last time: | the beam, the
tether, | or a check of somebody's skill. ||"

### 6. A quest that waits

**Screen:** Quests section. Above the Scans comment, type Raise the Mast. Highlight
`signal mast_repaired`. Then the table of three words the game sends.

**Say:** "When a job is done, the game sends a word. || It's the job's key, and then
underscore repaired. || So my quest says done when, signal, mast repaired. ||| That's
three words now that the game sends by itself. || A barrier has opened, | a job has been
repaired, | or a ruin's piece has been taken. || Lint knows all three. ||"

### 7. Two doors, one word

**Screen:** The Way In and The Airlock side by side: both `Roles: entrance`. Then Find the
Way In: `Done when: reach entrance 1000`. Then the fix: `Roles: entrance, hollow_door` and
`reach hollow_door 1000`.

**Say:** "Now here's the reason I kept this in the same mission. || I have two places with
the role entrance. | The game needs both. ||| But my story uses that word too. || The
first step says reach entrance, one thousand. || And reach doesn't know which entrance I
meant. ||| So a suit that steps out of the airlock at the station | is standing on an
entrance, | and the step finishes there. || It pays, and it sends the crew to the altar, |
before they've left home. ||| Lint can't see it. | Both lines are correct. || The cure is
a role of my own. || I add hollow door to the Way In, | and the step waits for that. ||"

### 8. Lint, and play

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Then `sbs run server,helm,comms -m
MyRuin map=0`. The handheld: Boarding Party, DS 1 Worksite, SUIT UP. Nav: Survey Mast.
Fire: the row, then the countdown. The quest list.

**Say:** "Lint is clean, so I start the game. || The Boarding Party app names the
worksite, | so I suit up. ||| There's one place on the list, the mast. | I pick it, and
the suit flies round. || On Fire, the row says Repair, Survey Mast. || I select it, I
press again, | and the banner says repair, twelve seconds. ||| And then it's done. | The
quest is finished, and I never sent the word. ||"

### 9. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Add a valve that's worked by hand, | and a panel that's
hauled into place. || Write a quest for one of them. ||| Then break one line where lint
can see it, | and one where it can't. || Next time is the last one: | the whole class, in
one episode. ||"