# C3-13 video script - What the crew sees

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 12's finished files** in `MyAway`. Four files change:
>   `mission.amd` and the three `.tiles` files. `example\` holds them.
> - **No MAST and no new field.** The student renames marks, titles, headings and item
>   keys, adds three `Scan:` lines, and writes two side stories of the Lecture 5 kind.
> - **NOBODY HAS SEEN ANY SCREEN IN THIS LECTURE.** No person has looked at the handheld
>   on the ground. Every statement about what an app shows is one of the two kinds
>   below. Record nothing as fact until the list under "Confirm on camera" is ticked.

> **CAPTURED FROM THE APPS' OWN DRAWING CODE (mock, 2026-10-10).** The probe ran each
> app's draw function with the widget calls recorded, for stand-in consoles, on the
> packaged library (sbs_utils `ae05dac7`). Captured that way: the bar's three slots; the
> eight tiles and their one-line blurbs; every row of Crew (the roster, a person's
> detail, the buttons), Act (the transcript text, the pickup sentences, the covering
> mark), Look (`Use`, `Talk to`, `Go to`, `Further off`, the last note), Pack (items,
> `Use medkit`), Tasks (own story, party quests, `Leads`), Beam, Scan and Fire; the
> ship tablet's Boarding Party screen; the ship's quest rows; the Messages line from
> `Report in`. Before and after each fix.

> **READ FROM SOURCE ONLY, NOT CAPTURED.** Look's limits (six in reach, four further
> off) and Tasks' four leads; that a prop's scene takes in crew within two cells (seen
> once in a capture, with two at the terminal); that the first screen shows the scene's
> line in a band that scrolls; that choices in Act are buttons in a wrapping row; the
> `Give to` button (the probe called its function; the button was not drawn in a
> capture); which apps a rooms-only party has. Layout, size, color and position were
> never captured and are not described anywhere.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 12's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` and the three maps in tabs, the maps in Text view |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 2 with a server, Helm, Comms and Science |

## Confirm on camera

1. Lint is `clean` after Steps 2, 3, 4, 5 and 6, warns `unfired-signal` twice after the
   two stories are typed, and is `clean` again after the two answers. (Lint.)
2. The bar's third slot reads `pad` before Step 2 and `landing pad` after it; on the
   hidden kit's cell it reads `cache` before and `Kesh Relay` after. (Mock, captured.)
3. Look and Beam read `Go to Dry Gully` and `To Dry Gully` after Step 3. (Mock.)
4. After Step 4 the pack reads `pump house key x1` and the door says `pump house key
   fits`. With the door's line left stale, the key does not open it. (Mock.)
5. Scan reads `no reading` for the tent before Step 5. (Mock.)
6. Lt Ross's Tasks app has no story before Step 7 and `Find a Place to Set Down` after.
   Dr Hale, alone with Marrow, is offered the helm answer as covering. (Mock.)
7. Chief Okoro, alone with Marrow while Dr Hale stands on the pad, is offered her
   answer as covering. (Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. Every app, on a screen. Whether the rows are in the order captured.
2. Whether a 44 character choice fits, and how a covered choice looks.
3. The bar when a mark's name is three words long.
4. The Boarding Party screen and the quest list on a console left aboard.

## Scenes

### 1. Cold open

**Screen:** The handheld on the ground, eight tiles. Then the bar, close: a name, two
jobs, and the word `cache`.

**Say:** "For six lectures you've written records. || Your crew never sees a record. |||
What they see is this handheld. | Eight apps, and every one of them is made of your words. || Some of
those words you chose with care. || And some you typed in a hurry, as a name for
yourself. | like the last word on this bar. ||| Today we read the mission from their side, | and fix what
reads badly. ||"

### 2. The bar and the eight apps

**Screen:** The game with three consoles down. The bar. Then each tile opened once and
closed: Crew, Act, Look, Pack, Tasks, Beam, Scan, Fire. The table from the page beside
it.

**Say:** "Start with the line that's always there. | Your name, your jobs, and where you
stand. ||| Then the eight apps. || Crew is who's down here, and the way home. || Act is
the scene, and it keeps everything you've read. || Look is what's in reach, as buttons. ||
Pack is what you carry. || Tasks is your own story, and the party's. || Beam, Scan and
Fire do what they say. ||| For each one, ask a single question. | Which of my words is
this? ||"

> Builder: everything said in this scene was captured from the apps' draw functions,
> not seen. If the order of tiles or rows differs on a real screen, say what the screen
> shows.

### 3. Who is offered what

**Screen:** Two handhelds side by side at Old Marrow: the medic's, with the cough
answer; the engineer's, with the same answer marked as covering.

**Say:** "A choice with no condition goes to everybody in the scene. || A choice for a
job goes to the person with that job. ||| Now here's the surprise. | The engineer walks
up to Marrow alone. || The medic is across the yard, on the landing pad. || And he's
offered her answer, marked as covering. ||| Covering is worked out scene by scene, | from
who is standing in it. || So a job is never out of reach. | If only a medic's hands will
do, | ask for a skill instead. ||"

### 4. A mark is a word

**Screen:** The bar reading `pad`. Then the doctor walked onto the scrub by the pad: the
bar reads `cache`. Then `landing.tiles` in Text view: the two lines changed. Then the
record: `At: 6, 8`.

**Say:** "That third word on the bar is a mark from your map file. || Any mark somebody
can stand on is a word on their screen. ||| So watch what happens here. || Nobody has
asked about the medical kit yet. | And the map has just told her it's there. ||| So here are two rules. || Name a mark for the place, the way you'd say it. | Landing pad. Gully mouth.
Foot of the stairs. || And stand a hidden thing on a cell, not on a mark. ||"

### 5. Titles, and what the pack says

**Screen:** Look: `Go to The Dry Gully`. Beam: `To The Dry Gully`. The two `title:`
lines changed. Then Act: `picked up Toolbox`, and Pack: `fuse x2`, `pump key x1`. Then
the three lines that name the key, changed together.

**Say:** "An area's title is read after other words. | Go to, in Look. To, in Beam. || So
a title that starts with The reads badly twice. | and the fix is to take it off. ||| Next, the things you
pick up. || The transcript says he picked up a toolbox. | The pack says two fuses. ||| And
the key is worse. | The heading says pump house key. | The pack and the door say pump
key. || That's the item's key, with its underscore shown as a space. ||| So make the
item's key the same words as the heading. || Three lines name it, | and all three change
together. | Lint can't check that for you. ||"

### 6. Scan, and a title that is the whole task

**Screen:** Scan in the yard: the tent with `no reading`. A `Scan:` line typed into the
Tent record. Then Dr Hale's Tasks app, and the three headings changed.

**Say:** "Scan lists everything in sight, scenery too. || With no scan line and no
description, it says no reading. || So give your scenery one line each. | It's the
cheapest clue you have. ||| Now open the Tasks app. || On the ship, a quest shows its objective. | Down
here it shows a heading, a state, and a lead. ||| So on the ground the heading has to be
the instruction. || The Caretaker's Cough becomes See to Marrow's Cough. ||"

### 7. The two with nothing to do

**Screen:** Lt Ross's Tasks app: party quests only. Then the two side stories typed,
lint warning twice, the two answers typed, lint clean. Her Tasks app again.

**Say:** "Look at the mission as your helm officer. || No story of her own. | One answer
she's covering, and a panel that refuses her. ||| Two of your five crew have come down to
watch. || So give each of them a story, and one answer that finishes it. | You know every
word of this from the fifth lecture. ||| Lint warns that nothing sends the signals, | and
then the two answers put that right. ||"

### 8. What the bridge sees, and your turn

**Screen:** A console left aboard: Boarding Party, with the names of the party. Then the
quest list. Then Messages, with one line: reporting in. Then the exercise.

**Say:** "Somebody stays on the bridge. | Here's everything they get. ||| A list of who
went down. || The shared quests, as they start and finish. || And one line in Messages, |
when somebody on the ground presses Report in. ||| No scene line ever reaches the bridge.
|| So the shared quests are its only window. | Remember that for the capstone. ||| For
the exercise, play it to read, not to win. || Write down every word that makes you wince,
| and then go and fix each one. ||| Next time, we put a clock on it. ||"

> Builder: the Boarding Party screen, the quest rows and the Messages line were captured
> for a stand-in console that stayed aboard. Nobody has seen them drawn.
