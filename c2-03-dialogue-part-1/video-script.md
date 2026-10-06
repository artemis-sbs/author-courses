# C2-3 video script - Dialogue, part 1

Target length: 17 minutes. One continuous screen recording with voice-over, cut at scene
boundaries. The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | The Class 1 mission with **Close Inspection** from Lecture 8. Lint clean. No Dialogue section yet |
| Characters | Either none, or the Characters section from Lecture 2. The script types Harbormaster Quill on camera; if Lecture 2 already made her, show her and skip the typing |
| Library | A build with the fixes of 2026-10-03 evening (an `Action:` on a quest that starts at once; curly brackets in a take). Committed, not yet released |
| Template | The mission must come from the `amd` template that already reads the Characters and Dialogue sections (build item B53: fixed in the starter repo, not yet pushed). An older mission needs the two card lines this lesson used to teach |
| VS Code | `MyMission` folder open, `mission.amd` in one tab |
| Game | Closed. Started on camera in scene 8 with a server, a Helm console and a Comms console |

## Confirm on camera

Run in the real engine on 2026-10-03 with a server and a Comms console, by a script that
called the game's own functions and wrote what they returned to a file. Every line below
was the same in the engine as in the headless runs. Nobody has seen a screen.

What the runs showed:

- No call is waiting before Close Inspection completes, or at 1500 from the hulk. At 300
  the quest completes and one call is waiting.
- The words on its row are `Harbormaster Quill - About that hulk`.
- Opened, the speaker is Harbormaster Quill, she has a face, and two things are said: one
  take from the first block, then one from the second.
- Over six plays of a three-take scene, all three takes came up.
- DS 1 Calls is not in the quest list before or after.
- On the Comms console, the list is titled `Incoming Hails`
  while a call waits and `Harbormaster Quill` while it is open. Its rows are the call,
  then `Back` and `Continue`, then `Back` and `Close`. `Back` returns the call to the
  list, and it opens again from the first block with the same takes.
- That console's placement dial read `both`.

Not seen by anyone. If one of these is not as described, stop and fix the page:

1. The Incoming Hails list on a real Comms console, and where on the screen it sits.
2. The open call: her face, the title, her name, the line. The code builds all four; none
   has been seen drawn.
3. The call on the main screen as well as on Comms. The dial's default says it should be.
4. Which comes first for the crew: the "quest complete" notice or the call.
5. Her face from one game to the next. `Face: terran_female` gives a new face of that kind
   each game. If that looks wrong on camera, Lecture 2 has to teach a fixed face.
6. The second game showing a different take. It is chance, so it can take a few tries.

Known, and kept out of the lesson on purpose:

- A second voice in the same call (`@vance` after `@quill`) is drawn under the first
  speaker's name (build item B51). The lesson says one voice in a scene.
- A take that BEGINS with a curly bracket is read as a condition and never used. Curly
  brackets elsewhere in a take used to crash the screen that draws the call; that was
  seen in the engine and is fixed (B50), but has not been seen drawn since.

## Scenes

### 1. Cold open (0:00 - 0:50)

**Screen:** The Comms console. One row in the Incoming Hails list. Select it. Quill's
face and a line. Continue. A second line. Close.

**Say:** "Nobody fired a shot there. Somebody called, and said something. That is a scene:
a character, a few lines, and enough different ways to say them that it does not sound
like a recording. Today you write one, and the station calls your crew with it."

### 2. Someone to speak (0:50 - 2:30)

**Screen:** `mission.amd`, end of the file. Type the Characters section and Harbormaster
Quill. Point at `(quill)`.

**Say:** "A scene needs a speaker, and a speaker is a character. You made characters last
time. Mine is Quill, who runs traffic on the station. Look at the word in round brackets.
That is her key. From here on, nothing calls her Quill, or Harbormaster. Everything calls
her by her key. Small letters, no spaces."

### 3. The scene (2:30 - 5:15)

**Screen:** Type the Dialogue section heading, the scene heading, the fence, and three `%`
lines. Point at each fence line as it is named.

**Say:** "A new section, Dialogue. Its key is the word dialogue, in small letters, and
that matters later. Then the scene: three hashes, a name for my own use, and a key.
Speaker: her key. When: hail, which means this is a call coming in to the ship. Title:
what the call is about. The crew reads that before they answer. And then what she says."

### 4. Takes (5:15 - 7:30)

**Screen:** Highlight the three `%` lines. Then break the second one onto two lines, pause,
and undo it.

**Say:** "Three lines, each starting with a percent sign. She does not say all three. She
says one. Each of these is a take: a different way to say the same thing, and the game
picks one by chance each time. Three rules. A take is one line in the file. If I press
Enter in the middle of it, like this, I have made two takes, and one day the crew gets
half a sentence. Takes are alternatives, not a list. And plain keyboard characters only:
no curly quotes, no long dashes, and never a curly bracket at the start of a take."

### 5. A second thing (7:30 - 9:15)

**Screen:** Add `@quill` above the three takes. Add a blank line, a second `@quill`, and
two more takes.

**Say:** "So how does she say two things? Blocks. An at sign and her key starts a block.
Three takes in the first, two in the second. The game takes one from each, so this little
scene can read six ways. The crew reads the first, presses Continue, reads the second.
Her key, not her name. And one voice in a scene, for now."

### 6. Placing the call (9:15 - 11:45)

**Screen:** Scroll up to Close Inspection. Add `Then: reveal ds1_calls`. Below it, type
the DS 1 Calls record. Point at `Beat`, then at the two spaces and the dash.

**Say:** "A scene is words on a page until the story places the call. I want it to come
when the crew finishes Close Inspection. So that quest gets one more line: then, reveal
ds1_calls. And here is ds1_calls. The word Beat, alone on the first line, says this is a
moment in the story and not a job, so it stays out of the quest list. It starts when it is
revealed. And Action is what happens the moment it starts: two spaces, a dash, then who
calls, the word hails, and the key of the scene. Starts when revealed is what makes her
wait. Leave it out, and she calls the moment the game begins."

### 7. Lint (11:45 - 13:30)

**Screen:** Terminal: `sbs lint MyMission`, clean. Change `Speaker: quill` to
`Speaker: quil`, lint, show the warning, undo. Change `quill_hello` in the Action line to
`quill_helo`, lint, show the warning, undo. Change the section key to `(Dialogue)` with a
capital, lint: still clean. Undo.

**Say:** "Lint. Clean. It catches a speaker who is nobody. It catches a call to a scene
that is not there. It does not catch this: a capital letter in the section key. Clean,
and the call would never come. So four names get checked by eye: her key, the scene's
key, the beat's key, and the two section keys, which have to be exactly characters and
dialogue. The table is on the page."

### 8. Play it (13:30 - 16:00)

**Screen:** Server, Helm and Comms. Fly to the hulk, inside 500. Close Inspection
completes. On Comms: the Incoming Hails row. Select it. Continue. Close. Then restart the
mission, fly in again, and open the call a second time.

**Say:** "In close. The quest completes, and there she is: Harbormaster Quill, about that
hulk. Open it. One of my three openings. Continue. One of my two closings. Close. And
again, from the start. Same scene, and it may not read the same."

### 9. Your turn (16:00 - 16:45)

**Screen:** The exercise on the companion page.

**Say:** "You have a quest that finishes on a timer, from Lecture 8. Write a second scene,
and have that quest reveal a second beat that calls it. Next time the crew gets to answer
back."
