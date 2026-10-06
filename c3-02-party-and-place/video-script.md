# C3-2 video script - A party and a place

Target length: 15 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Class 1 mission with the Close Inspection quest, lint clean |
| Library | A build that has `boarding_visit` and `Names: locked` (committed 2026-10-03, not yet released) |
| VS Code | `MyMission` folder open, `mission.amd` and `story.mast` in two tabs |
| Game | Closed. Started on camera in scene 7 with a server and an Engineering console |

## Confirm on camera

Checked in the real engine on 2026-10-03, with a server and an Engineering console, by a
script that called the game's own functions and read the results from a file:

- the Engineering console is Chief Okoro, with the job `engineering`, and locked;
- the party forms when Close Inspection completes, made of the crew, titled The Hulk;
- the console goes down as Chief Okoro;
- all three rooms, both ways back, and Return to the ship;
- the visit ends by itself and the console is back at Engineering.

SEEN on the real screens, 2026-10-03 (one Engineering console, driven by mouse, with the
fixes made that day - they are not released yet):

1. The top bar reads "Chief Okoro" beside the tablet icon.
2. The PADD has a Boarding Party tile once the party has formed, and the tile says The
   Hulk.
3. The app says "Going down to The Hulk", shows Chief Okoro and her job, and has one
   BEAM DOWN button.
4. BEAM DOWN turns the console into the boarding handheld (the xESS), across the whole
   screen: a bar reading Chief Okoro, engineering, The Airlock; under it the room's line
   and one button per choice.
5. Return to the ship puts the console back at Engineering with nothing to press.

NOT seen yet. If one is not as described, stop and fix the page:

6. The console picker offers no Edit button for a locked seat (the picker is behind the
   Options menu and was not opened).
7. A Science console is Dr Hale and can go down beside the Chief.

Known: the game's log gets a line for each PADD app this mission has no screen for
(`upgrade`, `cargo`, `fabricate`). It is harmless and is build item B21. A mission made
from the template before 2026-10-03 shows IMAGE NOT FOUND on every PADD tile; the
template is fixed (build item B38). The same older missions have no boarding handheld:
after BEAM DOWN they stay on the Boarding Party app.

## Scenes

### 1. Cold open (0:00 - 0:40)

**Screen:** The game. The ship alongside the hulk. The Boarding Party app: The Hulk,
Chief Okoro. BEAM DOWN. The airlock line.

**Say:** "My engineer, three rooms, and a hulk nobody has opened in years. She is the same
person on the bridge and aboard it, and all of it is text I wrote in one file. Today you
write your own."

### 2. Your crew (0:40 - 3:30)

**Screen:** `mission.amd`, end of file. Type the crew section.

**Say:** "A new section at the bottom. The word `crew` on the first line of the fence
says what it is. `Ship` says whose crew. And `Names: locked` says these are my people:
without it, a player who has saved their own name keeps it. Then one record per person:
the console they sit at, a face, and a job. Whoever sits at Engineering is the Chief,
here and aboard the hulk."

### 3. The place (3:30 - 6:40)

**Screen:** Type the Scenes section, one room at a time.

**Say:** "A room is a record. One line starting with a percent sign: what the party finds
when they walk in. Then the ways out. Words in square brackets are what the crew reads.
The key in round brackets is the room it leads to. And empty round brackets lead nowhere:
that choice ends the visit and sends everyone home."

### 4. Two rules (6:40 - 8:10)

**Screen:** Highlight "Go back to the airlock" in both rooms, then the three "Return to
the ship" lines.

**Say:** "Two rules, and they are the difference between a place and a trap. Every room
has a way back. Every room has a way home. Check them by eye, because lint only helps
with half of it: it warns if a choice points at a room that does not exist, and says
nothing about a room with no way out."

### 5. Start it (8:10 - 10:40)

**Screen:** Add `Then: signal board_hulk` to Close Inspection. Switch to `story.mast`.
Paste the two parts of the card. Highlight the three things to change.

**Say:** "Something has to say when. Our quest already knows the moment: the ship is
alongside. So the quest sends a signal when it completes, and this card listens for it.
You paste it; you do not write it. One line reads the rooms.
And one line runs the whole visit: it opens the party, starts the first room, and when
the last choice is taken it brings everyone home. Three things on the card are yours to
change: the signal name, the name of the place, and the room they arrive in."

### 6. Check it (10:40 - 11:20)

**Screen:** `sbs lint MyMission`. Show `clean`. Misspell `bridge` as `brige`, run lint,
show the warning, undo.

**Say:** "Lint. Clean. And here is the one mistake it does catch."

### 7. Play it (11:20 - 14:10)

**Screen:** Start the server and an Engineering console. Show the crew name in the top
bar. Fly inside 500. Press the tablet icon, then the Boarding Party tile. BEAM DOWN:
the handheld opens on The Airlock. Walk airlock, reactor, airlock, bridge, airlock.
Return to the ship. The console is Engineering again.

**Say:** "Engineering, and I am Chief Okoro. Alongside. The quest completes, and the
party forms. Down. The airlock. Aft. Back. Forward. Back. And home: I did not press
anything to get back here."

### 8. Your turn (14:10 - 15:00)

**Screen:** The exercise on the companion page.

**Say:** "Add a fourth room, and a third person for Helm. Give the room a way in, a way
back and a way home. Next time, everyone gets their own menu."
