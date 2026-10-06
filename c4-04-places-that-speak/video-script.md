# C4-4 video script - Places that speak

> **CHECKED IN THE REAL ENGINE, 2026-10-04 (server only, by script).** All 29 lines of the
> probe's report matched the mock: no call at 900, the call at 500 in Surveyor Rook's name,
> "Mark the Gallery." lights The Niche, no second call, the ship never opens the place's
> own scene; and with a probe-made suit the scene opens on arrival, branches, closes, and a
> later arrival reads the `Scan:`. `mast.runtime.log` was empty. Nothing was SEEN on a
> console: the seven items under "Not seen by anyone" still stand.
>
> **Changed since this script was written (library `d06ccfd4`, not yet released):** lint now
> names `Scene:` on a room, a prop or the ruin (`relic-field-wrong-record`) and a scene or
> a beat typed in the Relics section (`relic-section-stray`); a misspelled `Scene:` is
> written to `mast.runtime.log`; an answer that leads nowhere in a place's scene brings the
> console back to the party. The page's Step 7 has been updated; re-cut the lint scene.
>
> **DECISION WAITING ON THE USER (B78):** a place's `Scene:` is opened only by a crew
> member in a suit, which needs Lecture 8. This lecture teaches the place calling the SHIP
> through a beat. Whether a ship should also be offered a place's own scene is a design
> call.

Target length: 19 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Lecture 3 mission, lint clean: The Hollow with The Way In, The Altar and The Niche. No Characters section and no Dialogue section yet |
| Files touched | `mission.amd` only |
| Template | `story.mast` MUST be the current `amd` template: it reads the Characters and Dialogue sections and has the `relics_spawn` line. `example\story.mast` is that file, unchanged since Lecture 3 |
| Library | Measured on the released library built into `data\missions\__lib__` on 2026-10-04 (sbs_utils `ae376b8b`), without `--use-working-tree`. Lint was the working tree at `01c6f643` |
| Art pack | None |
| VS Code | `MyMission` folder open, `mission.amd` in one tab, font size raised |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 9 with a server, a Helm console and a Comms console. A main screen too, if the call is to be shown there |

## Confirm on camera

Nobody has looked at any screen in this lesson, and the game engine was not run. This is
what was checked, and how.

**The thing to know first.** A place's `Scene:` is opened by one thing only: a crew
member's suit arriving at that place under its autopilot. A ship does not open it. A
mission from the `amd` template has no way to put anyone in a suit until Lecture 8. So the
second half of this lesson (scene 7) cannot be shown in the game on camera. Say so, as the
script does.

**By script, in the mock, with the lesson's own files (headless runs, 2026-10-04).** A
probe moved the ship, called the game's own functions and printed what they returned.

- The finished file: lint `clean`, `sbs compile` prints nothing, the run passes with labels
  59 of 422, and `mast.runtime.log` is empty. The same on the working tree.
- The ship, 900 from The Altar: no call, and The Altar's marker is lit. At 500: one call
  is waiting. Its row is made of the name `Surveyor Rook` and the title
  `A recording at the altar`.
- Opened, the speaker is Surveyor Rook, he has a face, one take is said, and two answers
  are offered. "Play the rest." leads to the second scene. "Mark the Gallery." ends the
  call and lights The Niche's marker, with the ship 5300 away from it. "Shut it off." ends
  the call and lights nothing.
- The ship sent away and brought back to 100 from The Altar: no second call.
- Marker One is not in the quest list before or after.
- The ship on top of The Altar never opened "At the Altar", and nothing was written to
  `mast.runtime.log`.
- With no number after `reach altar`, the call was waiting with the ship at The Way In,
  4082 from The Altar.
- Every row of the three tables in Step 7: by `sbs lint` on that exact file with no probe
  in the folder, then by a headless run of the broken file. 78 variants of the file and 90
  runs in all.
- The exercise, as written: lint clean. The second call comes at The Niche, "Log it."
  completes What Rook Left, and What Rook Left is in the quest list from the start.

**By script, in the mock, with a crew member put in a suit by the probe.** The lesson's
mission cannot do this itself. The probe made a suit the way the library's own test does,
ended its route at the place, and ran one pass of the autopilot.

- Arriving at The Altar opens `altar_look` for that console. One take, two answers. "Read
  the marks on the rim" leads to `altar_marks`. "Step back" closes it.
- A second console arriving afterwards gets no scene. It reads the `Scan:` line.
- The first console arriving again reads nothing new.
- A second console arriving while the scene is still open joins it.
- `; reveal niche` from the place's scene lights The Niche and adds it to the places a
  suit can be sent. Before that the list is The Altar and The Way In.
- Once, with the real door and the real autopilot: a route on `relic_built` offered the
  ruin (`eva_offer`) and opened a party (`boarding_invite_crew`), `eva_go_out` put console 0
  in a suit at The Way In, and the suit flew to The Altar in about 95 seconds at the Fast
  setting. The scene opened on arrival. This is the card Lecture 8 will need. It is not in
  this lesson.

**By reading the code, not by measuring.**

- Another suit within 600 of the one that arrives is pulled into the scene
  (`eva_places.py`, `PLACE_JOIN_RADIUS`). The library's own test covers it.
- A suit flying past a place does not open its scene. Only the end of a route does
  (`eva.py`, `eva_tick`).
- The handheld has no button that closes a place's scene. Only an answer does (`xess.py`,
  `_act_app`). The probe saw a scene with no answers stay open.
- The call goes to every player ship, not only the one that reached the place, because
  the beat belongs to the whole story (`amd_action.py`, `_hails`). The lesson has one ship.
- A beat's `Show:` is `when done`, and this beat is never done, so it stays out of the
  list.

**Not seen by anyone. If one is not as described, stop and fix the page.**

1. The Incoming Hails list on Comms with the row "Surveyor Rook - A recording at the
   altar", and when it appears as the ship enters The Vault. Class 2, Lecture 3 checked
   this list in the engine by script; nobody has seen it drawn.
2. The open call: his face, his name, the take, and the two answers below **Back**.
3. Whether the call is also drawn on the main screen. The dial on Comms starts at Both.
4. The Niche turning into a gold contact on Helm's map when Comms picks "Mark the
   Gallery.", and whether Helm's map is zoomed far enough out to show it from The Vault.
5. The order of things in the tunnel: The Altar's contact first, the call after.
6. Rook's face from one game to the next. `Face: terran_male` gives a new face each game.
7. Anything at all on a crew member's handheld. The whole of Step 6 is unseen, and stays
   unseen until Lecture 8.

**Keep off camera.** Suits. Nothing in this recording should put a crew member outside
the ship. And do not type `Speaker: altar`: it works (the caller is then named The Altar,
with no face), but lint and the game read that word differently, and the page does not
teach it.

## Scenes

### 1. Cold open (0:00 - 0:50)

**Screen:** The game. Helm flying up the tunnel into The Vault. Cut to Comms: one row in
the Incoming Hails list, "Surveyor Rook - A recording at the altar". Open it.

**Say:** "Last time this room had a name. Today it has something to say. I flew the ship
into the Vault, and a recording forty years old started to play. I did not write a line of
code for that. I wrote who is speaking, what he says, and how close the ship has to be."

### 2. Two listeners (0:50 - 2:30)

**Screen:** The table from Step 1 of the page.

**Say:** "A place in a ruin can speak to two different listeners. The ship, which means
the bridge: that arrives on Comms as a call. Or a person, a crew member who has gone
outside in a suit and is standing there: that is read on their handheld. They are written
differently. And here is the thing to know before we start. Your crew does not leave the
ship until Lecture 8. So today you will write both, and you will play one. The other one
lint checks for you, and it waits."

### 3. A voice (2:30 - 3:45)

**Screen:** `mission.amd`, end of the file. Type the Characters section and Surveyor Rook.

**Say:** "A call is placed by somebody, and a table of stone is not a somebody. So I give
the place a voice. Forty years ago a survey team found this ruin, and their leader left
recordings in it. He is a character, written the way you wrote characters in Class 2. His
key is `rook`."

### 4. What he says (3:45 - 6:15)

**Screen:** Type the Dialogue section: Rook at the Altar, then The Rest of It. The second
scene's first answer is typed without `; reveal niche` for now.

**Say:** "Now the scene. All of this is Class 2. Speaker: his key. `When: hail`, because
this is a call that comes in. A title, which the crew reads before they open it. Two
takes, and the game picks one. Then two answers. One leads on to a second scene, by its
key. One ends the call. The second scene has no `When` and no title, because the only way
into it is that answer."

### 5. The place makes the call (6:15 - 9:30)

**Screen:** Scroll up to the Quests section. Below Study the Derelict, type Marker One.
Then show The Altar's record and point at `Roles: altar`.

**Say:** "A scene is words on a page until something places the call. In Class 2 that was
a beat waiting to be revealed. This beat waits for the ship to get somewhere. Three
hashes: it is not a step of First Contact. `Beat` on the first line. Then
`Starts when: reach altar 600`. `altar` is a role. It is this word here, on the place's
`Roles` line. Not its key, and not its name. For the Altar they happen to be the same
word. For the Way In they are not: the key is `way_in` and the role is `entrance`. And six
hundred is how close. The Vault is seven hundred from the middle to the wall, and the
altar is in the middle, so six hundred means the ship is in the room. Always write that
number. Leave it out and the game uses five thousand, which is bigger than the whole
ruin. Then `Action`, and under it who calls, the word `hails`, and the scene."

### 6. An answer that changes the map (9:30 - 11:15)

**Screen:** Back to The Rest of It. Add `; reveal niche` to the first answer. Show The
Niche's heading and point at `(niche)`.

**Say:** "You know what an answer can do: start a quest, finish one, send a word. In a
ruin there is one more. `reveal`, and then a place. Remember the Niche, the place I hid
last time. It only showed up when the ship was nearly on top of it. With this answer it
shows up when Comms says so. Now be careful: `reveal` takes the place's key, the word in
round brackets. `reach` took its role. Two lines, two different words for the same place."

### 7. The place's own words (11:15 - 14:00)

**Screen:** The Altar's fence. Add `Scene: altar_look` and the `Scan:` line. Then the end
of the file: type At the Altar and The Marks.

**Say:** "Now the other listener. Somebody is standing at this table. Nobody is calling
them. What they read is what they see. On the place, two lines. `Scene` is the key of a
scene. `Scan` is one line about the place, for whoever comes after the scene has been
played. And the scene itself: no fence at all. No speaker, because nobody is speaking. No
`When`, no title, because it is not a call. Takes and answers, the same as ever. One rule
is new: every path through a place's scene has to end in an answer with empty brackets.
Nothing else closes it. This opens when a crew member's suit arrives here. Not when the
ship does. I cannot show it to you today, and you cannot play it today. We come back to it
in Lecture 8."

### 8. Lint (14:00 - 16:00)

**Screen:** Terminal: `sbs lint MyMission`, clean. Then three breaks, each undone. Change
`reach altar 600` to `reach alter 600`, lint, read the warning. Change `Scene: altar_look`
to `Scene: altar_lok`, lint, read the warning. Change `; reveal niche` to `; reveal nich`,
lint: clean.

**Say:** "Lint. Clean. Now I break the role. It tells me nothing in the mission wears a
role called `alter`. Good: that call would never have come. Put it back. Now the scene on
the place. It tells me the Altar points at a scene that is not there. That is how I check
the half I cannot play. Put it back. Now the word after `reveal`. Clean. Lint does not
check that word, and the game would say nothing either: the answer would end the call and
the Niche would stay dark. So read two things yourself, every time: the word after
`reveal`, and that there is a number after the role."

### 9. Play it (16:00 - 18:15)

**Screen:** Server, Helm and Comms. Helm's map: The Hollow. Fly in, through the ring,
across The Nave, up the tunnel. The Altar appears on the map. Keep going into The Vault.
Cut to Comms: the row appears. Open it. Play the rest. Mark the Gallery. Cut to Helm's
map: The Niche.

**Say:** "In through the Mouth. The Nave. Up the tunnel, and there is the Altar on the
map, the same as last time. Now into the room. Comms: a call. Surveyor Rook, a recording
at the altar. Open it. One of my two takes. Play the rest. And: mark the Gallery. Back to
Helm. There is the Niche, and we have not been near it."

### 10. Your turn (18:15 - 19:00)

**Screen:** The exercise on the companion page.

**Say:** "Give the Niche a recording of its own, and words of its own. Make one answer
finish a quest. Then break one line where lint can see it and one where it cannot. Next
time: what is lying in these rooms."
