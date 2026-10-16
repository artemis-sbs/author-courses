# C3-15 video script - Boarding an enemy ship

> **STATE ON 2026-10-10. Read this first.**
>
> - **Everything this page needs is released.** Written for Artemis Cosmos 1.4.0, with a
>   current tool and libraries. The feature was released the day this was written.
> - **Starts from Lecture 14's finished files** in `MyAway`. Two files change:
>   `mission.amd` and `story.mast`. `example\` holds both.
> - **MAST: two lines in the map, one line on the starter's card, one new card of four
>   lines.** The new card is the Class 1 tug card hearing a different step.
> - **CORRECTED 2026-10-15: the three rough things are gone.** The library released the
>   same day this page was written (sbs_utils a2d63d66, then ed811ecb) places her crew so
>   that nothing aboard is ever shut in, lets a shot never remove a prop, sends
>   `boarding_deck_take` from Comms' `Take as prize`, gives way to a boarding party when
>   nobody of the landing party is on the ground, and keeps every hull's plan whatever
>   races are allowed. The finished files lint `clean` (checked with the released tool).
>   Scenes 1, 2, 6 and 8 and the matching lines of the page were corrected from the
>   library's documentation and lint. They have NOT been re-played in the mock.
> - **PLAYED IN THE GAME 2026-10-16** (server, Helm, Comms; ten stills). Corrected from
>   that play the same day: she starts about 5,000 from the ship; she is picked on the
>   Comms 2D map.
> - **PLAYED AGAIN 2026-10-16 on the strongbow** (sitting 4). Every scene's game still is
>   from that play. Once she has struck, her crew stand down: Gunner Brakk did not fight
>   (a crew member stood beside her ~15 s, no hit), so nobody was downed and the medkit
>   beat is gone. One FULL shot still drops her and her power cell. The game also stands
>   generated `Pirate crew` figures, calm, in the Plunder Hold and Crew Berths.
> - **HULL CHANGED 2026-10-16: `pirate_strongbow`, not `pirate_brigantine`.** The
>   brigantine is a light carrier (`baycount` 6, role `carrier` in the ship data), so
>   Legendary Missions launched six `Black Gull NN` fighters that shot at the ship all
>   game. The strongbow has no bay and no `carrier` role, and the same rooms (two brigs, a
>   boat bay, a plunder hold, a surgery). Checked in the mock: no carrier role, her deck
>   builds (52 x 52 tiles), the strongbox and Oduya in a brig each, the kit at the
>   arrival, Brakk in the boat bay. EVERY GAME STILL showing her needs taking again.

> **Measured 2026-10-10, in the mock**, on the packaged library (sbs_utils `ce28c951`,
> LegendaryMissions `243e0a4`), with stand-in consoles driven by a script. Walked on the
> finished files: the long play (run her down, the button, three crew aboard, the kit,
> the prisoner, the gunner and her cell, the strongbox, the prize, back to the relay,
> the beacon lit with the gunner's cell); the scuttle; the leave, and a second boarding;
> `Take as prize` on Comms; a FULL shot at the strongbox; the game's own `Surrender now`
> at full shields and at 30 percent; a party at the relay recalled in the middle of a
> conversation; a ship nobody boards, for a minute; the Beam app from her deck; a second
> ship, a freighter. 33 one-change variants linted, 30 of them played.
> **Taken from the build team's report, not re-run:** the count of 63 plans and which
> hulls have rooms; that Legendary Missions allows two races; the fighters.
> **Seen in the real game by the build team, by script, one Helm console:** the button,
> a deck planned from the hull, a prize taken. No screen was looked at.
> **Read from code, not played:** her crew is put only in living rooms, holds and
> sickbays; a refusal under a tenth of shields is final.

The companion page is `lesson.md`; the finished files are in `example\`.

## Before recording

| Item | State needed |
|---|---|
| Mission | `MyAway` with Lecture 14's files. Lint clean |
| VS Code | `MyAway` folder open; `mission.amd` and `story.mast` side by side |
| Game | Closed. Started on camera in scene 7 with a server, Helm and Comms (Lt Ross and Ens Vale go across) |

## Confirm on camera

1. Lint after Steps 2 and 3 is `clean`; after Step 4 it has one `unfired-signal`; the
   finished files are `clean`. (Lint, 2026-10-15.)
2. Before she strikes, Comms offers `Hail`, `Taunt`, `Surrender now`. After, `Take as
   prize` and `Send a boarding party`. (Game, 2026-10-16.)
3. The answer to the button is `We are hove to. Send your party across: Boarding Party,
   on the ePADD.`, shown once its header is clicked. (Game.)
4. The strongbox and the prisoner stand in a brig each, the kit one cell from the
   arrival, the gunner in the boat bay. (Game on the brigantine; mock on the strongbow.)
5. Each of the three endings does what the table says to the party, the ship, the quest
   and the relay. (Mock; the prize also in the game.)
6. With the strongbox in `Mark: quarters` it can still be reached: nothing aboard shuts
   anything in. (Library documentation; not re-played.)

Not seen yet. If one is not as described, stop and fix the page:

1. How fast she runs for home, and how long a real crew has.
2. Where a student finds `debug.log`.

Seen in the game since (2026-10-16, on the strongbow): the bar's room names as words
(`Hallway`, `Brig`, `Boat Bay`); Look's description of the strongbox; the open Comms
menu changing by itself when she strikes; her picture in the Quest Log; the strongbox and
Oduya in a brig each, Brakk in the boat bay.

## Scenes

### 1. Cold open

**Screen:** The Comms console with a ship selected, and one button: Send a boarding
party. Then a title: Boarding an enemy ship.

**Say:** "For eight lectures, you've drawn every floor your crew walked on. ||| Today
they board a ship, | and you draw nothing. || The game builds her deck from her own
plan. ||| Your job is what's on it. || A prisoner, a
gunner with the cell your beacon needs, | and a strongbox that ends it three ways. ||| It's brand new, so at the end I'll show you what to check before your crew finds it.
||"

### 2. One party at a time

**Screen:** The four conditions from the page, as a list. The fourth one circled. Then
the Comms answer, drawn: We cannot take a party aboard while your people are elsewhere.

**Say:** "The button needs four things. || A ship that has struck. | A hull with a
plan. | The station art, which your starter already has. ||| And no other party out. ||
That last one is the trouble. ||| Your relay party opens in the first second, | and a
party on a map never closes by itself. || So as your mission stands, | with anybody still
down at the relay, | Comms can't send a party to her. ||| We fix that with one rule. | When she strikes, the landing party
comes home. || When the ship comes back, the relay opens again. ||"

### 3. A side and a ship

**Screen:** The game first: the Comms console, the Black Gull picked on the 2D map, her
buttons Hail, Taunt and Surrender now. Then the Sides section typed at the end of the file.
Then two lines typed into the map in the story file, with her hull and the two sets of
numbers highlighted.

**Say:** "Here she is on the Comms console, | the Black Gull, a pirate, out past the relay.
|| Hail, taunt, or tell her to surrender. ||| In the file, first a side for her to be on. |
One record, and one line that says enemies.
||| Then the ship, in the story file. | Two lines, under the relay's own line. ||| Her hull
is a pirate raider, with no fighter bay. || A carrier brings its fighters, | and they'd
shoot at your ship all game. ||| Look at the numbers. || The first set is where she comes from. | The second is where she is.
||| That matters, because a ship that strikes and isn't boarded runs for home, | and
when she gets there she's taken off the map. || I tried it with one place. | She
struck, and eight seconds later she was gone. ||"

### 4. Three quests and a card

**Screen:** The game first: the Quest Log on Helm's ePADD, Run Down the Black Gull selected,
her picture at the top of its page. Then the three quests in the Quests section, with
their descriptions, and arrows: the first reveals the second, the second sends the relay's
signal. Then the card pasted at the end of the
story file, and one line added to the starter's card.

**Say:** "Here's the chase in the Quest Log aboard, | with her picture at the top.
||| In the file there are three quests. || Run her down, which waits for the ship to close on her. ||
Come back to the relay, which is hidden until then. || And take her, which waits for a
signal the game sends. ||| Two of them get a page for the bridge. | Her picture at the top
of the chase, | and two icon bullets on the prize. ||| The card is one you know. | It's the tug card from the first
class, | hearing a different step start. ||| It does two things. | It calls the landing
party home, and she strikes. ||| And the same line goes on your old card, | for the
trip back. ||"

### 5. Kinds of room

**Screen:** The game first: aboard the Black Gull on Helm, the strongbox in a brig. Then
one record, with two lines highlighted: Area, deck. Mark, brig. Then the table of where
the four records stood. Then the list of her room names.

**Say:** "Here's her deck, and the captain's strongbox, in her brig. ||| In the file, two
new words put it there. || Area, deck: that means whatever ship we board. |||
And mark is no longer a mark in a file, | because there is no file. || It's a kind of
room. | Brig, cargo, quarters, bay. ||| Her hold is called the plunder hold. | Her
sickbay is the surgery. || You don't need to know that. | You write the kind, and it
works on any hull. ||| And when a hull has no such room, | your thing stands in the
hallway, and the game says so once. ||"

### 6. Her own crew, and the walk

**Screen:** The game first: the deck on Helm, just beamed across. Then Mate Oduya in
her brig. Then the strongbox in its brig. Then one rule, as a card.

**Say:** "Here's her deck again. || A few of her own crew stand about on it too, | calm,
and they won't fight. ||| A calm person blocks the cell they stand on, | and so does a strongbox. || So
the game walks the deck before it puts anything down. || Nothing of yours stands in a
doorway, | or anywhere that would shut something in. ||| Where a thing stands can change
when you add a record. | What it can never do is block the way. ||| So keep one rule:
after every change to what's aboard, | go aboard and walk to each thing. ||"

### 7. Three endings

**Screen:** The game, three windows: the server, Helm and Comms. Helm closes on her. Comms presses the button. The
party beams across. Comms' Fire app armed with FULL, the gunner in sight in the boat bay.
The strongbox scene with its four answers. Then the endings table.

**Say:** "Now play it through. || Helm closes to fifteen hundred, and she strikes. || Comms
selects her, and sends a party. ||| Aboard, the gunner stands in the boat bay. || Once
the ship has struck, | her crew stand down, | and the gunner with them. ||| She still
carries the relay's cell. || Fire, full, arm, and click her, | and she drops it. ||| The
strongbox has three answers that matter. || Take her, and she joins your side, | and the quest pays. || Scuttle her, and
she's gone. || Leave her, and she runs for home. ||| Every one of them brings the party
home first. || And after every one, | the relay opens again when the ship comes back.
||"

> Builder: if the map is black, the art pack is missing: see "If something goes wrong".
> Do not touch Comms between taking the Black Gull's first menu and her strike.

### 8. What to warn your crew about

**Screen:** Lint on the finished files: clean. Then four short captions, one at a time:
A shot never removes a prop. Take as prize. The cell left behind. Beam, to Kesh Relay.

**Say:** "Lint says clean on your finished mission. || What's left to know isn't in your
file. ||| A shot never removes a prop. || The strongbox is safe from a full shot, | and so
is anything else that holds an ending. ||| Comms has its own button, take as prize. |
It finishes the same quest as your strongbox, | but nobody goes aboard to meet what you
wrote. ||| What the gunner drops is lost if nobody picks it up. ||| And from her deck,
the transporter still reaches your relay. || Know these before your crew finds them. ||"

### 9. Your turn

**Screen:** The exercise list. Then the checkpoint.

**Say:** "Now it's your turn. || Play all three endings. || Move the strongbox into the cabin,
and walk to it. || Swap her hull for a freighter, and see where everything goes.
||| Then light the beacon with the gunner's cell. || Next time, the mission is your
own. ||"
