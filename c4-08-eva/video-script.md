# C4-8 video script - EVA

> **STATE ON 2026-10-09. Read this first.**
>
> - **Everything this page needs is released** (2026-10-09): the automatic SUIT UP at a
>   ruin's door, `<barrier key>_opened`, `<relic key>_taken`, the exosuit as the default
>   suit. The page is written for Artemis Cosmos 1.4.0, installed from Steam or itch.io,
>   with a current tool and libraries. Record on such an install.
> - **NOBODY HAS FLOWN A SUIT.** Not in this mission and not in any other. Every screen
>   in scene 9 is unseen. Record scene 9 FIRST, before anything else, and fix the page
>   where the screen differs.
> - **The student's mission is `MyRuin`** as Lecture 7 left it, with Lecture 5's Steps 2
>   to 6 done as well: `c4-07-quests-through-a-ruin\example\mission.amd` with Lecture 5's
>   records typed onto it (443 lines), and Lecture 6's `story.mast` (116 lines). Lecture
>   5's page says where each record goes; in Lecture 7's file the two quests go at the end
>   of the Quests section. The game is started with
>   `sbs run server,helm,comms -m MyRuin map=0`.
> - **`mission.amd` only.** `story.mast` is opened only if the exosuit closes a console
>   (see "If something goes wrong").
> - **`example\` holds the one file that differs from the start:** `mission.amd` (478
>   lines).
> - **THE EXOSUIT CAN CLOSE A CLIENT.** A console that first meets the hull `lm_eva_suit`
>   in the middle of a game can crash (an engine fault, reported). If it does on camera,
>   add `eva_set_suit_hull("tsn_shuttle")` below `shared MISSION_DOC = None` in
>   `story.mast` and record with the stock hull. The page has the same line.
> - **Scene 9 ends a game.** A recording take adds a line to the game's own
>   `game_results.yaml`. That is fine for a real play; say nothing about it.
> - **Two people, or one person at two consoles.** The Helm console goes outside; Comms
>   has to answer "Open the niche." while the suit is at the niche.

> **Measured 2026-10-09, in the mock.** Tool `sbs` as installed in `data\missions`,
> library as packaged in `__lib__` (sbs_utils `e84602e7`, Legendary Missions `b37a320`).
> The start was built by typing Lecture 5's steps onto Lecture 7's finished file (both
> orders: Lecture 5 last, and Lecture 5 before Lectures 6 and 7); both lint `clean`. The
> page's steps were typed one at a time onto it, with lint after each. Then 43 one-change
> variants of the finished file, each linted and most played headless.
>
> **What the script did.** A stand-in console was connected the way the mock's own
> browser bridge connects one, and sat at the ship's Comms post. From there the probe
> used what the game uses: the function behind the Boarding Party app's button (it read
> SUIT UP, and put the crew member in a suit drawn as `lm_eva_suit` at The Way In); the
> suit's own list of places (`eva_points`) and its `eva_goto`; the place's scene through
> the Act transcript and its answers; the Scan, Nav and Fire apps' own drawing functions,
> with the widget calls recorded so their words could be read; `eva_use`, which is what a
> press in the Fire app calls; the calls on Comms; and the function behind COME ABOARD.
> The ship's shot at the slab was the engine's `destroyed` event, handed to the game's
> own dispatcher.
>
> **What the script did NOT do.** It flew ONE leg with the autopilot: The Way In to The
> Altar, 4610 units, arriving between 150 and 170 seconds at Cruise. For every other leg
> it put the suit at the place and ran one autopilot pass, which is what an arrival is.
> It never reeled anything in: in the mock the suit took the bowl on contact as the bowl
> appeared (for a ship the stand-in takes a pick-up from 500 away and not from 700, and
> the tether reaches 600). No engine, no window, no person.

> **Seen in the real game's SERVER, with no console (2026-10-09, another session)**, on
> Legendary Missions' own test map: the offer at the door, the party named for the ruin,
> the suit hull, a barrier opening finishing a quest, a collected piece sending
> `<relic>_taken`. Not this mission, and no screen.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyRuin` as Lecture 7 leaves it plus Lecture 5, lint clean. `mission.amd` has 443 lines |
| `story.mast` | Lecture 6's, 116 lines, with the card |
| `story.json` | Has the line with `items` in it (Lecture 5) |
| VS Code | `MyRuin` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Logs | `mast.compile.log` and `mast.runtime.log` empty, or deleted |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console |
| People | Two, or one person who can reach both consoles |

## Confirm on camera

"Lint" means the installed tool, run from `data\missions` on a folder holding the files
with that one change. "Mock" means the mission was then played headless with the packaged
library, driven as described above. If an item fails while recording, stop and fix the
page.

1. Lint is `clean` after each of Steps 2 to 6. (Lint.)
2. The ship 3100 from The Way In: nothing is offered. At 2900: the offer is The Hollow
   and the button reads SUIT UP. Back out to 3300: still offered. At 3500: withdrawn.
   (Mock.)
3. SUIT UP puts the crew member at 0, 0, 19300, in the room The Mouth, in a suit drawn as
   `lm_eva_suit`. The suit's list: The Ring Plate, The Gallery Door, The Cache, The Altar.
   (Mock.)
4. The suit arriving at The Altar: The First Marker is done (100 credits), Cut Through is
   running, "A recording at the altar" is waiting on Comms, and the scene `altar_look` is
   open on the suit with its two answers. The Scan app reads `## The Vault` and
   `**The Altar** - ` with the `Scan:` line. (Mock; the flown leg ended the same way, with
   the ring's call waiting as well.)
5. After "Mark the Gallery.": The Niche is on the suit's list. Picking it is refused, and
   Nav reads `No way through to niche from here.` (Mock.)
6. At The Gallery Door: the `Scan:` line is added to the Act transcript; Fire lists
   `The Fallen Slab   450`; the tether is refused; the beam starts, and the banner reads
   `BEAM - The Fallen Slab, 12s`. Fourteen seconds later the barrier is open, the library
   has sent `slab_opened`, Cut Through is done (200) and The Second Marker is running.
   The Niche is then accepted as a destination. (Mock.)
7. The suit at The Niche: The Second Marker is done (300), What Rook Put Back is running,
   "A second recording" is waiting, and there is no bowl. After "Open the niche.": the
   bowl is placed and taken, the hold has 1, the library has sent `hollow_taken`, the step
   is done (600) and Carry It Home is running. (Mock.)
8. COME ABOARD takes the suit away and puts the console back at its post. With the ship
   500 from DS 1 the game ends as a win with the `Win:` sentence and 700 credits. (Mock.)
9. The ship leaving to 5300 with somebody outside: the offer stays. After they are aboard:
   withdrawn. (Mock.)
10. A ship's shot at the slab opens it, sends `slab_opened` and finishes Cut Through. (Mock,
    by the `destroyed` event. Whether the ship's weapons can target the slab in the engine
    is not known.)
11. `eva_set_suit_hull("tsn_shuttle")` below `shared MISSION_DOC = None`: the suit is drawn
    as `tsn_shuttle`, and the rest is the same. (Mock.)
12. Every row of the tables in Step 7, the five "not mistakes" and the note about The
    Niche in the Fire app: lint for all of them, and the mock for what the game does.
    (Lint, Mock.)
13. The exercise: `Clear with: beam, check engineering 9` adds WORK, the banner reads
    `WORK - The Fallen Slab, 6s`; `Opens when: reach gallery_door 400` opens the slab when
    the suit is at The Gallery Door and sends the word; a suit at The Cache takes the
    canisters for the ship (hold 3, What the Survey Left done). (Lint, Mock.)
14. The same walk on the file of a student who did Lecture 5 before Lectures 6 and 7:
    lint `clean`, a win with 700. (Lint, Mock.)

Read in the library's code, not measured: a press on a row of the Fire app selects it and
a second press uses the tool; the Crew app's button for the way home reads "Come aboard"
(the Boarding Party app's reads COME ABOARD); a hidden place joins the list when a suit
comes within 1200 of it; a miss on a WORK try makes the same console wait twenty seconds;
another suit within 600 is pulled into a place's scene.

Not seen by anyone. If one is not as described, stop and fix the page:

1. The Boarding Party app on a handheld, and its SUIT UP button.
2. The console a crew member has in a suit: the view, and the five apps.
3. The suit itself, drawn as the exosuit, and whether a console closes when it appears.
4. A suit flying a route through the ring, The Nave and the tunnel, and how long it takes.
5. The Act app with a place's scene, and the Scan app.
6. The Fire app: its rows, the two presses, the banner, and what cutting looks like.
7. The bowl appearing in the niche, and a suit taking it. Whether a suit has to touch it
   or reel it in with TETHER in the real game is NOT known: the page says both.
8. Coming aboard, and the console going back to its post.
9. The end screen for this mission.

> Keep off camera: a personal side story (`For:`). The game hands a ruin's Side Stories
> to the crew who suit up, and the story starts then. It is an optional part of
> Lecture 10, not of this lecture.
> And the place's own marker listed in the Fire app at the niche ("The Niche"): it is a
> fault, reported; do not select it.

Also capture the screenshot for the top of the page.

## Scenes

### 1. Cold open

**Screen:** The game. The ship stopped at the mouth of The Hollow. A handheld: SUIT UP.
Cut to a suit in The Nave, flying. Cut to the Fire app counting down on the slab. Cut to
the quest list: Cut Through, done.

**Say:** "For seven lectures, nobody has left the ship. || Today, at last, somebody does.
||| The ship stops at the door, | and one of the crew goes in wearing a suit. || They read
the altar, | they cut through a fallen slab, | and they bring out the bowl by hand. |||
And the part that surprised me is how little there is to write. ||"

### 2. What the game does by itself

**Screen:** The first table from Step 1 of the page. Then The Way In's record in
`mission.amd`, pointing at `Roles: entrance`. Then the table "The offer".

**Say:** "Going outside is called EVA, | and most of it is already in your mission. || The
game offers the crew a way out, at the door of any ruin you build. || It puts them in a
suit, | it gives the suit a list of your places, | and it flies the suit to the one they
pick. ||| You wrote the door in Lecture three. | It's the place with the role entrance. ||
The offer is made while the ship is within three thousand of that place, | and it's taken
back when the ship leaves. || But not while somebody is still outside. ||"

### 3. The suit

**Screen:** The table of five apps from Step 1. Then the three rules under it.

**Say:** "A crew member in a suit gets a console of their own, | with a handheld that has
five apps. || Nav is the list of places. | Act is what a place says. | Scan reads the
room. | Fire holds the tools. | And Crew is the way home. ||| There are three things to
remember. || A suit flies to places, and to nothing else. | You can't steer it by hand. ||
A hidden place isn't on the list until it's been found. || And the tools reach six
hundred, and no further. ||"

### 4. A place to stand, and a way that is shut

**Screen:** `mission.amd`, Relics section. Below The Cairn, type The Gallery Door, then
The Fallen Slab. Highlight `Barrier:` and `Clear with: beam`.

**Say:** "Now the first new record. || A barrier is a ball of blocked space. | Every way
through it is shut, until somebody opens it. ||| But look at what I type first. | It's a
place, on the near side of the door. || That's because a suit can only fly to places, |
and its cutter only reaches six hundred. || With no place beside the slab, | nobody could
ever get close enough to cut it. ||| Then the slab itself. || Barrier, three numbers for
where, and one for how big. || And Clear with, beam, | which means the suit's cutter opens
it. ||"

### 5. The slab is a step

**Screen:** Quests section. Below The First Marker, type Cut Through. Change The First
Marker's `Then:` line. Highlight `signal slab_opened`, then `(slab)` on the barrier.

**Say:** "When a barrier opens, the game sends a word. || It's the barrier's key, and then
underscore opened. | Mine is slab opened. ||| So I write a step that waits for it. || It
goes after the altar, | and the altar's step now reveals this one. || I don't send that
word anywhere. | The game sends it, | however the slab comes open. ||"

### 6. The bowl, by hand

**Screen:** Dialogue section: change both answers to `- [Open the niche.]() ; signal
niche_open`. Relics: add `Starts when: signal niche_open` and the `Scan:` line to The
Niche. Quests: change the Objective of What Rook Put Back. Delete The Bowl.

**Say:** "Last time Comms said the final word, in a call. || Since Lecture five the game
says it, when the bowl is taken. | So Comms stops saying it. ||| But there's a trap here,
and it's worth a minute. || The walls of a ruin don't hold a ship. || So a ship could fly
in and scoop up the bowl early, | before the last step was listening. || The word would be
spent, | and the story could never end. ||| So I don't let the bowl exist yet. || Comms
gets a new answer, open the niche, | and it sends a word of my own. || And the niche says
starts when, signal, that word. ||| The step is always listening before the bowl is there.
|| Then I change the objective, | and I delete the quest from Lecture five, | because the
arc does its job now. ||"

### 7. Coming home, and the clock

**Screen:** Add `Then: reveal survey/home` to What Rook Put Back. Type Carry It Home.
Change `Fails when:` to 40 minutes, and the arc's description.

**Say:** "I don't want the game to end with somebody still outside. || So taking the bowl
reveals one more step, | and that one is finished back at the station. ||| And I give the
crew more time. || A suit is slower than a ship. | In my test it took about three minutes
from the door to the altar. || So twenty minutes becomes forty. ||"

### 8. Lint

**Screen:** Command prompt: `sbs lint MyRuin`, clean. Change `signal slab_opened` to
`signal slab_open`, save, lint, read the warning, undo. Delete The Gallery Door, save,
lint: clean. Undo.

**Say:** "I run lint, and it's clean. || Now I misspell the word on the step, | and lint
says nothing sends it. || That's what I want. ||| Next I delete the place beside the slab,
| and lint says clean. || But that mission can't be finished. || The slab is out of
everyone's reach, | and no file can tell lint how far a cutter reaches. ||| So that's the
check to do by eye. | Every barrier needs a place within six hundred of it. ||"

### 9. Play it

**Screen:** `sbs run server,helm,comms -m MyRuin map=0`. Helm flies to the door. The
handheld, Boarding Party, SUIT UP. Nav: The Altar. The Act app at the altar. Scan. Comms:
Mark the Gallery. Nav: The Niche, refused. Nav: The Gallery Door. Fire: the slab. Nav: The
Niche. Comms: Open the niche. The pick-up. Crew: come aboard. Fly home. The end screen.

**Say:** "I fly to the door, and I stop the ship. || On my handheld there's a Boarding
Party app, | and its button says suit up. ||| And now I'm outside. || I pick the Altar
from the list, and the suit flies itself. ||| And here are the words I wrote four lectures
ago, | read by somebody standing in front of the table. || On Comms I mark the Gallery, |
and the Niche joins my list. || I pick it, and Nav says there's no way through. ||| So I
go to the Gallery Door. || On Fire there's the slab. | I select it, I press again, and I
wait twelve seconds. || The step is done. ||| Now for the niche. || Comms opens it, and
there's the bowl. | I take it, I come aboard, and we fly home. || And that's the game. ||"

### 10. Your turn

**Screen:** The exercise on the companion page.

**Say:** "Now it's your turn. || Let an engineer work the slab loose by hand. || Make the
slab open by itself. || Send someone out for the canisters. ||| Then break one line where
lint can see it, | and one where it can't. || Next time, the same suit goes to work
outside a station. ||"