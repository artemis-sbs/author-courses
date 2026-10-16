# C3-13 video script - What the crew sees

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 12's finished files** in `MyAway`. Four files change:
>   `mission.amd` and the three `.tiles` files. `example\` holds them.
> - **No MAST and no new field.** The student renames marks, titles, headings and item
>   keys, adds three `Scan:` lines, and writes two side stories of the Lecture 5 kind.
> - **Seen on the game 2026-10-16** (engine 1.3.15, sbs_utils `7ea2c918`): every app, the
>   Boarding Party screen, Messages and the Quest Log, in two games. What the game showed
>   that the capture did not: the handheld's first screen is a LIST of eight full-width
>   rows, not tiles; Tasks is a list with the picked quest's page under it (state, the
>   objective, the text, leads); Beam on the pad reads `No other site has a lock yet.`;
>   Messages holds the crew's mail from home beside the Report in line; Scan on the pad
>   lists the key and the kit too, once the kit is found.
> - **A pickup names the prop now** (sbs_utils `19c038f9`): Act reads `Dr Ines Hale
>   picked up Pump house key.` and `Dr Ines Hale picked up Toolbox (fuse x2).`, and after
>   Step 4 `Dr Ines Hale picked up Two fuses.`; the prop is gone from the map. Pack still
>   lists the item key: `fuse x2`, `pump key x1`. Stepping onto a found item's cell picks
>   it up, so the medical kit is never drawn under her: Act gains `Dr Ines Hale picked up
>   Medical kit.` above the key's line (re-shot 2026-10-16, sitting 4).
> - **The bar's third slot names the mark you stand ON** (re-shot, sitting 4). The cell
>   you land on in the gully reads the area's title; `arrive` / `gully mouth` shows one
>   step further, on the mark's own cell.

> **CAPTURED FROM THE APPS' OWN DRAWING CODE (mock, 2026-10-10).** The probe ran each
> app's draw function with the widget calls recorded, for stand-in consoles, on the
> packaged library (sbs_utils `ae05dac7`). Captured that way: the bar's three slots; the
> eight tiles and their one-line blurbs; every row of Crew (the roster, a person's
> detail, the buttons), Act (the transcript text, the pickup sentences, the covering
> mark), Look (`Use`, `Talk to`, `Go to`, `Further off`, the last note), Pack (items,
> `Use medkit`), Tasks (own story, party quests, `Leads`), Beam, Scan and Fire; the
> ship tablet's Boarding Party screen; the ship's quest rows; the Messages line from
> `Report in`. Before and after each fix.
>
> **Re-measured the same day on tool `sbs` 0.14 and the library released with it**
> (sbs_utils `ed811ecb`). Two things changed the lecture. The starter's marks are
> place names now (`@post`, `@yard`, `@scrub`), and the game no longer shows a mark
> that places something still hidden: on the hidden kit's cell the bar reads the
> area's title. So the step that moved two hidden things from a mark to `At:` is gone,
> and Step 2 teaches the rule. Lint now warns when an item's key is renamed in one
> place and not another (`item-nothing-gives`).

> **READ FROM SOURCE ONLY, NOT CAPTURED.** Look's limits (six in reach, four further
> off) and Tasks' four leads; that a prop's scene takes in crew within two cells (seen
> once in a capture, with two at the terminal); the `Give to` button (the probe called
> its function; the button was not drawn in a capture); which apps a rooms-only party
> has. (Two more from this list were wrong on the game and are gone from the page: Act's
> choices stand one under another, not in a wrapping row, and in these stills the first
> screen is the list alone, with no scene line above it.)

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 12's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` and the three maps in tabs, the maps in Text view |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 2 with a server, Science and Helm (two crew: Dr Hale and Lt Ross; Lt Ross stays aboard for scene 8) |

## Confirm on camera

1. Lint is `clean` after Steps 2, 3, 4, 5 and 6, warns `unfired-signal` twice after the
   two stories are typed, and is `clean` again after the two answers. (Lint.)
2. The bar's third slot reads `pad` before Step 2 and `landing pad` after it; in the
   gully, one step onto the mark's cell, it reads `arrive` before and `gully mouth` after
   (the cell you land on reads the area's title). On the hidden kit's cell it reads
   `Kesh Relay` until Marrow has told of the kit, and `scrub` after, and stepping onto
   that cell picks the kit up (`Dr Ines Hale picked up Medical kit.`). (Game, 2026-10-16.)
3. Look and Beam read `Go to Dry Gully` and `To Dry Gully` after Step 3. (Mock.)
4. After Step 4 the pack reads `pump house key x1` and the door says `pump house key
   fits`. With the door's line left stale, the key does not open it, and lint says
   `item-nothing-gives`. (Mock, Lint.)
5. Scan reads `no reading` for the tent before Step 5. (Mock.)
6. Lt Ross's Tasks app has no story before Step 7 and `Find a Place to Set Down` after.
   Dr Hale, alone with Marrow, is offered the helm answer as covering. (Mock.)
7. Chief Okoro, alone with Marrow while Dr Hale stands on the pad, is offered her
   answer as covering. (Mock.)

Seen on the game 2026-10-16: every app in the order captured; a covered choice, `Look at
that cough (covering for medical)`, on one line; the Boarding Party screen and the quest
list on a console left aboard; Relight Kesh Relay's new page (the relay drawn beside its
lead line, then the table); items 3, 5 and 6 above, and 7 with Lt Ross in the chief's
place. Item 2 waits for the bar's re-shoot. Not seen yet:

1. Whether a 44 character choice fits.
2. The bar when a mark's name is three words long.

## Scenes

### 1. Cold open

**Screen:** The handheld on the ground: the bar, and the list of eight apps. Then the
bar, close: a name, two jobs, and the word `arrive`.

**Say:** "For six lectures you've written records. || Your crew never sees a record. |||
What they see is this handheld. | Eight apps, and every one of them is made of your words. || Some of
those words you chose with care. || And some you typed in a hurry, as a name for
yourself, | like the last word on this bar. ||| Today we read the mission from their side, | and fix what
reads badly. ||"

### 2. The bar and the eight apps

**Screen:** The game with two consoles down, Science (Dr Hale) and Helm (Lt Ross). The bar. Then each app opened once from
the list and closed: Crew, Act, Look, Pack, Tasks, Beam, Fire. Look is shown in the yard,
where it has buttons (on the pad it has nothing in reach). The table from the page beside
it.

**Say:** "Start with the line that's always there. | Your name, your jobs, and where you
stand. ||| Then the eight apps. || Crew is who's down here, and the way home. || Act is
the scene, and it keeps everything you've read. || Look is what's in reach, as buttons. ||
Pack is what you carry. || Tasks is your own story, and the party's. || Beam, Scan and
Fire do what they say. ||| For each one, ask a single question. | Which of my words is
this? ||"

### 3. Who is offered what

**Screen:** Two handhelds at Old Marrow: the medic's, with the cough answer; the helm
officer's, with the same answer marked as covering, while the medic stands on the
landing pad six cells off.

**Say:** "A choice with no condition goes to everybody in the scene. || A choice for a
job goes to the person with that job. ||| Now here's the surprise. | The helm officer walks
up to Marrow alone. || The medic is across the yard, on the landing pad. || And she's
offered the medic's answer, marked as covering. ||| Covering is worked out scene by scene, | from
who is standing in it. || So a job is never out of reach. | If only a medic's hands will
do, | ask for a skill instead. ||"

### 4. A mark is a word

**Screen:** The bar reading `pad`. Then the doctor one step into the gully: the bar reads
`arrive`. Then the three map files in Text view, the lines changed, and the bar again:
`landing pad`, then `gully mouth`. Then the doctor on the scrub where the kit is hidden: the
bar reads `Kesh Relay`. Then the same cell after Marrow has told of the kit: the bar reads
`scrub`, the cell is empty, and Act says `Dr Ines Hale picked up Medical kit.`

**Say:** "That third word on the bar is a mark from your map file. || Any mark somebody
can stand on is a word on their screen. ||| So take one step into the gully, onto its
mark. || The bar says arrive. | That was a name for you, not for her. ||| Name a mark for the place,
the way you'd say it. | Landing pad. Gully mouth. Foot of the stairs. ||| One thing the
game does for you. || A mark with something hidden on it isn't shown at all, | until the
thing is found. || So the map never gives your secret away. ||| Once Marrow has told of
the kit, | the bar says scrub, | and stepping on it picks the kit up. ||"

### 5. Titles, and what the pack says

**Screen:** Look: `Go to The Dry Gully`. Beam: `To The Dry Gully`. The two `title:`
lines changed. Then Act: `picked up Pump house key.` and `picked up Toolbox (fuse x2).`,
and Pack: `fuse x2`, `pump key x1`. Then the three lines that name the key, changed
together.

**Say:** "An area's title is read after other words. | Go to, in Look. To, in Beam. || So
a title that starts with The reads badly twice, | and the fix is to take it off. ||| Next, the things you
pick up. || Act names each one by its heading, | the words on your record. ||| For the key,
that's the pump house key. || But the pack and the door say pump key. || That's the item's
key, with its underscore shown as a space. ||| So she picks up one thing, and carries
another. || Make the item's key the same words as the heading. || Three lines name it, |
and all three change together. | Miss one, and lint tells you. ||"

### 6. Scan, and a title that is the whole task

**Screen:** Scan in the yard: the tent with `no reading`. A `Scan:` line typed into the
Tent record. Then Dr Hale's Tasks app, and the three headings changed.

**Say:** "Scan lists everything in sight, scenery too. || With no scan line and no
description, it says no reading. || So give your scenery one line each. | It's the
cheapest clue you have. ||| Now open the Tasks app. || It's a list, and every quest in it
is a heading and a state. || The objective is on the page under the list, | for the one
quest you've picked. ||| So the heading is what the crew reads first. | Make the heading
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
quest list. Then Messages: the reporting-in line, above the crew's mail from home. Then `mission.amd`: Relight Kesh
Relay's description retyped, the ship line, the paragraphs and the table. Then the Quest Log
again, the new page. Then the exercise.

**Say:** "Somebody stays on the bridge. | Here's everything they get. ||| A list of who
went down. || The shared quests, as they start and finish. || And in Messages, one line of
yours, | when somebody on the ground presses Report in. || The rest is the crew's mail from
home. ||| No scene line ever reaches the bridge.
|| So the shared quests are its only window. | Remember that for the capstone. |||
Select a quest, and the Quest Log shows its description in full. || The starter's is one
sentence, | and for the bridge that's the whole briefing. || So give it a page. | The
relay's picture comes first, | then a table of what the ship knows from up there. ||| For
the exercise, play it to read, not to win. || Write down every word that makes you wince,
| and then go and fix each one. ||| Next time, we put a clock on it. ||"
