# C3-12 video script - Scenes on the ground

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries.
> - **Starts from Lecture 11's finished files** in `MyAway`. One file changes:
>   `mission.amd`. `example\` holds it.
> - **No MAST, and no new `Win:` or `Lose:`.** Both endings go through the starter's
>   quest `relight`. The student writes one losing answer, and builds a second road to
>   the starter's winning one.
> - **`discover` is shown and not used.** It works in the game and lints clean. It is
>   left out because the cistern is `beam: no`, so here it would do very little.
> - **This is the end of the taught part of the tile-map half.** After it the student has
>   three linked areas, two locked doors, a terminal, three people, two hostiles, three
>   facts, a quest that starts and ends on the ground, a win and two losses.

> **Measured 2026-10-10, in the mock.** Tool `sbs` as installed, library as packaged
> (sbs_utils `ae05dac7`). The seven steps were typed in order and linted at each one.
> The finished files were played headless with three stand-in consoles, the long way
> round to the win: the key, Marrow, the gully, the notice, Pim, the crawler, the
> tablet, the fuses, the pump, the cell, Pim at home, the beacon. A second play took the
> short answers: the sentry calmed, Pim roused, the wire bridge failed and passed, and
> the crowbar to the loss. Then 26 one-change variants, each linted, and the ones lint
> is silent about played. In the second play and the variants the stand-ins were put
> beside things, and given items and facts, by the probe.
>
> **Re-measured the same day on tool `sbs` 0.14 and the library released with it**
> (sbs_utils `ed811ecb`): lint knows `discover`; seven rows that lint was silent about
> now draw `item-nothing-gives`, `ground-verb-target` or `ground-signal-unsent` and
> moved to the first table; an answer with a malformed `take` is skipped whole and the
> scene moves on.

The companion page is `lesson.md`; the finished file is in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 11's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` in two tabs: the Quests section, and the end of the file |
| Command prompt | Open in `data\missions`, cleared |
| Game | Closed. Started on camera in scene 8 with a server, Engineering and Weapons (two crew: Chief Okoro and Lt Reyes) |

## Confirm on camera

1. Lint prints the `never-revealed` warning on the page after Step 1, adds one
   `ground-signal-unsent` warning after Step 2 and another after Step 3, and is `clean`
   after Step 4 and for the rest of the lecture. (Lint.)
2. The long way round wins: the game ends with the starter's `Win:` sentence, and the
   side has 100 credits from Pim's Tablet. (Mock, by script.)
3. The crowbar loses: the game ends with the starter's `Lose:` sentence. (Mock.)
4. Each new word, played once: the stash appears on `reveal`; the quest goes from
   waiting to active on `accepts`; the tablet leaves the pack and a fuse arrives; Pim
   leaves the gully and stands by the tent; the relay door opens on `open door`; the
   sentry stops attacking on `calm`; Pim attacks after `rouse`. (Mock.)
5. With the key in the engineer's pack, the doctor is offered `Show him the brass key`.
   (Mock.)
6. Every row of the page's tables. (Lint, Mock.)

Not seen by anyone. If one is not as described, stop and fix the page:

1. Any of these scenes on a handheld.
2. The Pack app's **Give to** button.
3. The quest log showing Pim's Tablet start and complete.
4. The last screen after a loss from the pump house.
5. Pim's Tablet's second paragraph in the Quest Log, under the first.

## Scenes

### 1. Cold open

**Screen:** Pim's scene on a handheld: `Give her the tablet`. Then the pump panel: three
answers, one of them a crowbar. Then the last screen, lost.

**Say:** "You have three maps, some things, and two people. || What you don't have yet is
a story that ties them together. ||| Today Pim wants her tablet back, | the pump wants
three fuses, | and one bad idea with a crowbar loses the whole game. || Every bit of it is
an answer in a room. ||"

### 2. The words

**Screen:** The two tables of words from the page. Highlight the ones marked NEW.

**Say:** "A choice has a condition in front of it, and outcomes behind. || You've used
both since the third lecture. ||| On a map there are two new conditions. || Holding asks
what the person answering is carrying. || Party asks what everybody on the ground is
carrying between them. ||| And there are new outcomes. || Give and take move things in and
out of a pack. || Open and reveal work on props. || Calm, rouse, dismiss and summon work
on people. ||"

### 3. A quest that waits, and two hidden records

**Screen:** The game first: the Quest Log on the Weapons console's ePADD (Lt Reyes, beamed
back up) after Pim's promise, Pim's Tablet selected. Then the Quests section: type Pim's
Tablet. Lint: the warning. Then the game: the yard on the Engineering console's map, Pim by
the tent. Then the People section: the second Pim. Then the game: the gully, the medical
kit by the rock. Then the Props section: the stash.

**Say:** "First a quest that waits. || Here it is in the Quest Log, | on the ePADD of a crew
member who beamed back up. || Pim's Tablet, a hundred credits, and two paragraphs. ||| In
the file, it starts when it's revealed, | which means when an answer says so. || The
second paragraph is about who Pim is, | for whoever stayed on the ship and never met her.
|| Lint warns that nothing reveals it yet, | and that's true for now. ||| Then two things
that begin hidden. || Here's the yard on the engineer's map, near the end, | and that's
Pim, standing by the tent. || In the file she's a second record. | When somebody goes
somewhere else on a map, they're two records: | the one who leaves, and the one who
arrives. ||| And here's the gully on his map, | with a medical kit by the rock that wasn't there
before. || In the file it's a prop, | hidden until a scene shows it. ||"

### 4. Pim's scene

**Screen:** The game first: Pim's scene in the Act app on the Engineering console's
handheld (Chief Okoro), after the notice. Then the end of the file: replace Pim's two rooms
with the eight. Walk the cursor down the six answers of the first room. Then the game: the
same scene with the tablet in his pack. Lint: clean.

**Say:** "Now for her scene, | and it's where most of today's words live. ||| This is the
Act app on the engineer's handheld, | talking to Pim in the gully. || He's read the notice
by the pump house, | so he's offered a question about the spare cell. ||| In the file, that
answer is only offered if the party learned a fact, | from the notice by the door. || This
one reveals the stash. || In the next room, a promise accepts the quest. ||| And here's the
payoff, on the handheld. | He's carrying the tablet now, | and there are two new buttons.
||| In the file, the first is offered only to the one holding the tablet. || Then three
outcomes in a row, with commas: | take the tablet, complete the quest, and give a fuse.
||| The second is the mean answer. | Keep the tablet, and she's roused: | she attacks, and
the quest fails. || And when she goes home, | one answer dismisses her here | and summons
her there. ||"

### 5. The pump, with fuses

**Screen:** The game first: the pump panel in the Act app on the engineer's handheld, with
two fuses in his pack; then with three. Then replace the pump panel's rooms with the four.
Highlight `holding fuse >= 3`, then `take fuse 3`, then the two `%{party ...}` lines, then
the signal on the last room.

**Say:** "The pump needs three fuses now. || Here's the panel on the engineer's handheld,
| with two fuses in his pack. || He's offered the wire and the crowbar, and not the
lever. ||| With a third fuse the line changes, | and fitting all three is the first button.
||| In the file, look at the condition, | and at the outcome after it. || Holding three,
and take three. ||| Take always takes from the person who
answers. | So the condition in front of it is always holding, and never party. ||| The
lines at the top are different. | A line is read by everybody, | so a line asks about the
party. ||| The second answer is a gamble. | Two fuses and a bit of wire, | and a roll that
can fail. || And notice where the signal went. | Two answers lead to this room now, | so
the signal sits on its one way out. ||"

### 6. Two more uses for old rooms

**Screen:** The game first: the Yard Terminal in the Act app once the code is copied down,
with the new button. Then the Yard Terminal: add the `calm sentry` answer and its room.
Then the game: Old Marrow on the Weapons console's handheld (Lt Reyes), with the key in
Chief Okoro's pack. Then Old Marrow: add the `if party pump_key` answer and its room.

**Say:** "The starter's terminal already teaches a fact. | Give it a second use. || On the
handheld, once the code is copied down, | there's a new button under Send the door code.
||| In the file, send the sentry its update, and it's calm. | It keeps its power cell,
though, | so the party still needs another one. ||| And Marrow gets one answer about the
brass key. || Here it is on the weapons officer's handheld, | and it's the engineer who's
carrying the key. || In the file, that condition is party, | because nothing is taken, |
and it doesn't matter who picked the key up. ||"

### 7. The endings, and one more word

**Screen:** The game first: the server's last screen after the crowbar, lost. Then the
pump's `; fails relight`. Then the game: the beacon in the Act app with the spare cell in
the pack. Then the starter's beacon answer with `if holding power_cell`. Then the last
screen, won. Then Step 9: `; discover cistern`, and lint clean.

**Say:** "You wrote no Win line today, and no Lose line. || You didn't need to. | Both sit
on the starter's quest. ||| Here's the last screen after the crowbar, | and that's the
starter's Lose sentence. || Your crowbar fails that quest, | so it loses the game from two
maps away. ||| And here's the beacon, with the spare cell in the engineer's pack. || Your
spare is a power cell, | so the starter's own winning answer takes it, | and the game ends
with the starter's Win sentence. ||| One more word, discover, | tells the ship an area
exists. || It isn't in
your mission, | because the ship can't beam into your cistern anyway. ||"

### 8. Play it, and your turn

**Screen:** The game with two consoles, Engineering and Weapons: the route on the page, cut
down to its turns. The win. Then again, with the crowbar. Then the exercise.

**Say:** "Play the long way round. || The key, then Marrow, and then the gully. || Pim
asks for her tablet. || The crawler, the tablet, and back to Pim for a fuse. || Three
fuses in the pump, | then the gate, and the spare cell. || Pim opens the relay house from
her chair, | and the beacon lights. ||| Then play it again, and lose it with the crowbar.
||| For the exercise, give Marrow a use for the medical kit, | and write a second losing
answer that plays fair. ||| That's the last new word for a while. | Next time, the screen
your crew has been looking at. ||"