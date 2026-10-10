# Class 3, Lecture 15 - Boarding an enemy ship

## What you will have at the end

A pirate brigantine, the Black Gull, standing off Kesh Relay. The crew runs her down and
she strikes her colors. Comms sends a party across, and they walk her deck: a prisoner
in the brig, a gunner in the boat bay who did not agree to surrender, and the captain's
strongbox, which ends it one of three ways.

**Nobody draws that deck.** The game builds it from the ship's own plan, the one
Engineering looks at, and puts her crew aboard. You write what is on it, and you say
where each thing goes by the *kind* of room: `Mark: brig`.

*[Screenshot to add: the handheld aboard the Black Gull, with the deck beside it.]*

You change two files. In `mission.amd` you add one side, three quests, four things
aboard and four rooms. In `story.mast` you add two lines to the map, one line to the
card you have, and one new card of four lines.

Read this before you start. **Most of this lecture was measured in a stand-in for the
game**, with stand-in consoles driven by a script: 13 plays, and 33 files with one line changed. The game's
own test of this feature has been run once in the real game, by script, with one Helm
console connected: the button was offered, the deck was built from the ship's plan, and
a prize was taken. **Nobody has looked at the screen.** What the deck looks like is
unseen, and this page does not describe it.

This feature is also new, and three things about it are rough. They are on this page
where they matter, in bold, and all three are reported.

## The video

*[Link to add when recorded.]*

## Before you start

- `MyAway` as Lecture 14 left it. `sbs lint MyAway` says `clean`.
- A command prompt open in `C:\Cosmos\data\missions`.

This lecture uses five windows:

```
sbs run server,helm,comms,weapons,science -m MyAway map=0
```

Words for this lecture:

| Word | Meaning |
|---|---|
| Strike her colors | Surrender. A ship that has struck is on nobody's side |
| Prize | A ship that has struck and been claimed. She joins your side |
| Deck | The inside of a ship, as a map the party walks. The game draws it |
| Kind of room | `brig`, `cargo`, `quarters`, `bay`: what a room is for, not what it is called |
| Hold-out | Somebody aboard who goes on fighting after the ship has struck |

## Step 1 - What the game does, and what it asks for

You met the Boarding Party in Lecture 1, and a map to walk in Lecture 7. A ship's deck
is the same thing with the map made for you. The game offers it by itself. No card
opens it.

On the Comms console, with a ship selected, a button **Send a boarding party** appears
when all four of these are true. Each was tried.

| It needs | In `MyAway` | Tried by taking it away |
|---|---|---|
| The ship has struck | Step 5 makes her strike | Before she strikes Comms offers `Hail`, `Taunt` and `Surrender now` |
| Her hull has a plan | A `pirate_brigantine` has one, with rooms | See the table below |
| The `station` art is installed | It is. It is the last line of `story.json`, from the starter | With that line gone, Comms would not open on her at all |
| No other party is out | **It is not true in your mission.** The relay party is open all game | Comms answers `We cannot take a party aboard while your people are elsewhere.` |

Look at the last row. It is the one that shapes this lecture.

**One party at a time.** Your relay party opens in the first second, because the ship
starts within 6000 of the relay. And a party on a map never closes by itself. Beaming
up does not close it. Only the end of the game does, or a card. So in `MyAway` as it
stands, a ship that struck could never be boarded.

You will fix that with two lines of `story.mast` and one quest. The card that makes her
strike calls the landing party home first. A quest opens the relay again when the ship
comes back. Nothing on the ground is lost in between: packs, doors, pickups and facts
were all still there afterwards.

### Which ships have a deck

The plan comes from the hull, the last-but-one word of the line that puts a ship on the
map. The game ships 63 plans. The team that built the feature stood your kinds of room
on every one:

| Hulls | What is aboard |
|---|---|
| The three big pirates, the TSN ships, the Ximni ships, three Arvonians, some starbases | Rooms: a brig, quarters, a hold, a sickbay and more |
| Every Kralien, Torgoth, Skaraan and Biomech ship, the fighters, the freighters | A plan with engines and hallways, and no rooms |

No hull at all has a `bridge`.

One more thing about your starter, and you do not have to do anything. A hull's plan is
only loaded when its race is allowed in the mission. Your mission allows every race, so
the brigantine has hers. Legendary Missions itself allows only two, and there the
button will almost never show.

## Step 2 - A side to strike

A ship is on a side. Yours is `tsn`, and `story.mast` makes it. The pirates need one.

Go to the very end of `mission.amd`. Leave two blank lines, then type:

```
// ---- Sides. The crew's own side, `tsn`, is made in story.mast. This is the other one.
// `Enemies: tsn` is said once, here, and holds both ways.
## [Sides](sides)

### [Pirates](pirate)
---
Color: #F40
Enemies: tsn
---
The crews that work the Kesh run when nobody is watching it.
```

If you took Class 2 you have written this before. If not: two hashes and the key
`sides` make the section, the record's key `pirate` is the word a ship uses to join
the side, and `Enemies: tsn` makes the two sides enemies.

Save, and run lint. It says `clean`.

## Step 3 - The ship

Open `story.mast`. Find the line that puts Kesh Relay on the map. It begins
`npc_spawn(0, 0, 0, "Kesh Relay"`. Put your cursor at the end of it and press Enter
twice. Type these two lines, lined up with the line above them:

```
    gull = npc_spawn(20000, 0, 20000, "Black Gull", "pirate, ship, gull", "pirate_brigantine", "behav_npcship")
    set_pos(gull, 6000, 0, 4000)
```

You read a line like the first one in Class 1.

| On the lines | Meaning |
|---|---|
| `20000, 0, 20000` | Where she comes FROM. Not where she is |
| `"Black Gull"` | Her name. It is on the Comms button's answer and on the Boarding Party tile |
| `pirate` | Her side: the key from Step 2. It stays first |
| `ship` | A role. Keep it: Comms looks for it |
| `gull` | Your role. A quest and a card will look for it |
| `"pirate_brigantine"` | Her hull, and so her deck |
| `6000, 0, 4000` on the second line | Where she is when the game starts: about 7,100 from your ship |

Why two places? A ship that has struck and is not boarded turns for the place she came
from, at speed, and when she gets there she is taken off the map. That is the game's
rule for every ship that strikes. So where she came from must be a long way from where
she is.

Tried for this page with one place, `6000, 0, 4000` on the first line and no second
line: she struck, and eight seconds later she was gone, with no word to anybody.

Save, and run lint: `clean`.

## Step 4 - Three quests

In `mission.amd`, find **Bring Pim Her Tablet**, the last quest in the Quests section.
Below its last line, leave a blank line and type:

```
### [Run Down the Black Gull](chase)
---
Scope: shared
Starts when: at once
Objective: Close to within 1500 of the Black Gull
Done when: reach gull 1500
Then: reveal back
---
A pirate brigantine is standing off the dark relay, waiting for a convoy that cannot see her.

### [Come Back to Kesh Relay](back)
---
Scope: shared
Starts when: revealed
Objective: Settle with the Black Gull, then come back within 3000 of Kesh Relay
Done when: reach relay 3000
Then: signal relay_reached
---
She has struck her colors. The beacon is still dark.

### [Take the Black Gull](prize)
---
Scope: shared
Starts when: at once
Objective: Board the Black Gull and take her as a prize
Done when: signal boarding_deck_take
Reward: 200 credits
---
A brigantine is worth more to the Kesh run with a navy crew aboard than as wreckage.
```

Every line is one you have written before. What matters is how they hang together.

| Quest | It waits for | When it is done |
|---|---|---|
| Run Down the Black Gull | The ship within 1500 of anything wearing the role `gull` | It reveals the next one. Step 5's card hears that |
| Come Back to Kesh Relay | The ship within 3000 of the relay again | It sends `relay_reached`: the signal that opened the relay party the first time |
| Take the Black Gull | `boarding_deck_take`: the game's own signal for a prize | 200 credits |

The numbers fit each other. She sits 7,200 from the relay. When the ship is within 1500
of her it is at least 5,700 from the relay, so the crew has to turn round and fly back
before the second quest can finish.

Save, and run lint. It has one thing to say:

```
  [WARNING] line 139:19: `prize` waits for the signal `boarding_deck_take`, and nothing in the mission sends it, so that wait never ends. Check the spelling against the line in the story that sends it (unfired-signal)
```

Lint is right, as it was in Class 1. Nothing sends that signal yet. Step 7 does.

## Step 5 - The card

Two edits in `story.mast`.

**First, the new card.** Go to the very end of the file, below the last `->END`. Leave
two blank lines and paste this, with the first lines at the left edge:

```
#
# Come Back to Kesh Relay: what happens when that step starts.
#
//shared/signal/quest_started if QUEST_ID == "back"
    boarding_visit_end()
    for gull in role("gull"):
        side_surrender(gull)
    ->END
```

It is the card you pasted in Class 1 for the tug, hearing a different step start.

| Line | Meaning |
|---|---|
| `if QUEST_ID == "back"` | Only when the step that started is this one. **Yours to change:** the key of your quest |
| `boarding_visit_end()` | One party at a time. Whoever is down at the relay is brought home, and the relay party is closed |
| `for gull in role("gull"):` | For every ship wearing this role. **Yours to change:** the role, in the quotes |
| `side_surrender(gull)` | She strikes. This line is indented twice |
| `->END` | The block is finished |

**Second, one line on the card you already have.** Find the starter's card, the block
that begins `//shared/signal/relay_reached`. Add one line above the long one:

```
    ->END if party_ship is None
    boarding_visit_end()
    boarding_visit(party_ship, boarding_ground_scenes(), title="Kesh Relay", area="landing", stories=amd_section(MISSION_DOC, "side_stories"))
```

That is the same call, for the other direction. When the ship comes back to the relay
with somebody still aboard the Gull, they are brought home and the relay opens. Without
that line the relay would never open again: the second quest would be done, and the
party it tried to open would have been refused.

Save, and run lint. It repeats its one warning from Step 4, and nothing else.

### What about "Surrender now"?

Comms had a button of that name on her all along. It is the game's own way to make a
ship strike, and it is a roll of the dice.

| Her weakest shield | What "Surrender now" did |
|---|---|
| Full | `Go climb a tree, Artemis!` Every time: above half, she always refuses |
| Set to 30 percent | `We can still defeat you, Artemis! Prepare to die!` twice in one play. In another, the second press got `OK we give up, Artemis.` |
| Under about a tenth | Better odds. But the code says a refusal down there is final: the button goes away for good. Not played |

So a crew can talk her down that way, if Weapons has done the work first. Your story
cannot count on it, and that is why the card exists. The two do not fight. A ship that
Comms talked down still had the relay party open, so Comms got `We cannot take a party
aboard while your people are elsewhere.` Then the helm closed to 1500, your card ran,
and the button worked.

## Step 6 - What is aboard

Now the part you came for. Four records, in the sections you already have.

Two words are new, and they are the whole lecture:

```
Area: deck
Mark: brig
```

`Area: deck` means the deck of whatever ship the crew boards. `Mark:` is not a mark in a
file, because there is no file. It is a kind of room.

| You write | Where it stands |
|---|---|
| `Mark: brig`, `cargo`, `quarters`, `sickbay`, `bay`, `mess`, `lab`, `airlock` | In a room of that kind |
| `Mark: entry` | Beside the place the party arrives |
| `Mark: hallway` | In a hallway |

In the Props section, below the last line of **Pim's medical kit**, leave a blank line
and type:

```
### [Captain's strongbox](strongbox)
---
Area: deck
Mark: brig
Sprite: prop:crate_shield
Scene: strongbox
Blocks: yes
Scan: Plate steel, bolted through the deck. Paper inside, and a ring of keys.
---
A strongbox bolted to the deck of the brig, where nobody would think to look for it.

### [Boarding kit](gull_kit)
---
Area: deck
Mark: entry
Sprite: prop:crate_medical
Item: medkit
Scan: A medical kit, sealed. Nobody aboard has needed it yet.
---
A medical kit on a hook beside the entry port, for whoever comes aboard the hard way.
```

In the People section, below the last line of the second **Pim**:

```
### [Mate Oduya](oduya)
---
Area: deck
Mark: brig
Sprite: fig:junker_f
Face: female
Calm: yes
Talk scene: oduya
Scan: One human. Nine days of ship's biscuit, and not hurt.
---
The mate of the convoy tender, sitting on the brig's one bench with her arms folded.
```

In the Hostiles section, below the last line of **Sump crawler**:

```
### [Gunner Brakk](brakk)
---
Area: deck
Mark: bay
Sprite: fig:hunter_f
HP: 2
Damage: 1
Notice: 4
Stun: 10
Drops: power_cell
Scan: One human, armed. Not on the list of those who struck. One power cell, slung on her back.
---
The Gull's gunner, in the boat bay, with a cutlass in her hand and the tender's beacon cell on her back.
```

Every other line is one from Lectures 10 and 11. A prop is still a scene, a pickup or
scenery. A person is still calm or not.

Here is where the game stood them, on this hull, with exactly these four records:

| Record | You wrote | The room it got |
|---|---|---|
| Captain's strongbox | `Mark: brig` | `brig`. She has two brigs. This is one |
| Mate Oduya | `Mark: brig` | `brig`: the other one |
| Boarding kit | `Mark: entry` | One cell from where the party arrives |
| Gunner Brakk | `Mark: bay` | `boat-bay` |

Two things with one kind get two cells. Each record has a cell to itself.

**You wrote `bay` and the room is called `boat-bay`.** That is the point of a kind. On
this hull the hold is `plunder-hold`, the sickbay is `surgery` and the quarters are
`captains-cabin` and `crew-berths`. On another hull they have other names. You write
the kind, and it works on both.

And the power cell. It is a third way to light your beacon, and the lists you made in
Lecture 14 gain a row: `Power cell | The gunner of the Black Gull drops one | Anyone,
with one FULL shot, after a chase`.

### A kind she does not have

A brigantine has no laboratory. Tried: a thing with `Mark: lab` was stood in the
hallway, and the game said so once, in its `debug.log` file. A freighter has no rooms
at all. Tried on one, the line read:

```
boarding_deck: the deck of 'cargo_ship' has no free 'brig' for 'Captain's strongbox', 'Mate Oduya', so the hallway it is. On `Area: deck` a `Mark:` is a kind of room; this hull has: hallway, impulse, maneuver, sensor, shield, warp.
```

That is not an error. It is how one mission can board a brigantine and a freighter.
`Mark: bridge` gets the same treatment on every hull there is.

### The ship's own crew

You did not write them. Aboard the Black Gull the game put five, all calm, each named
`Pirate crew` and drawn as her race. Aboard the freighter it put twelve. Aboard a ship
that has struck they are all calm. They stand where they are put, in the cabins, the
holds and the sickbay, and they do not move.

**That is the first rough thing, and it is the one that will cost you an evening.** A
calm person blocks the cell they stand on. The game puts her crew down after your
things, anywhere in those rooms, a doorway included. So one of her crew can shut one of
your things in. And where the crew stands changes whenever you add or move a record.

Measured on this hull, each on the finished files with one line changed:

| The change | What happened |
|---|---|
| The strongbox with `Mark: quarters` | It stood in the captain's cabin. One of her crew stood inside the cabin door. Nobody could reach it, and a click on it did nothing |
| The kit with `Mark: cargo` | Reached. In an earlier draft of this page, with one more record aboard, the same line was shut in |
| Twelve more things aboard, none of them blocking | The strongbox, still `Mark: brig`, could no longer be reached |
| A box that blocks, in each of her twelve kinds of room | Five of the twelve could not be reached |

Three rules come out of that.

1. **Put what the story needs where her crew is never stood**: `entry`, `hallway`,
   `brig` or `bay`. Her crew is only put in living rooms, holds and sickbays. On this
   hull the brigs and the boat bay open straight onto the main hallway.
2. **A hostile is not shut in.** Brakk walks to the party.
3. **After every change to what is aboard, go aboard and walk to each thing.** Lint
   cannot see this, and neither can you from the file.

## Step 7 - The scenes, and three endings

At the very end of the Scenes section, below the last line of **The Remote**, leave two
blank lines and type:

```
### [The Strongbox](strongbox)
% Her papers, her letters of marque, and the keys to her magazine. Whoever holds this box holds the Black Gull.

- [Take her as a prize]() ; signal boarding_deck_take
- [Open her sea cocks]() ; signal boarding_deck_scuttle, fails prize
- [Go back to the ship]() ; signal boarding_deck_leave
- [Leave it for now]()

### [Mate Oduya](oduya)
% "Tender Halcyon, out of Kesh. We came to answer the relay's call, nine days ago, and this ship was waiting where the beacon should have been."

- [Ask what the tender was carrying](oduya_cell) ; learn tender
- [Ask who is still armed](oduya_brakk)
- [Tell her she is going home]()

### [The Spare](oduya_cell)
% "One spare beacon cell. The relay asked for it. Their gunner took it for her own share, and I do not think she knows what it is."

- [Ask her something else](oduya)
- [Tell her she is going home]()

### [The Gunner](oduya_brakk)
% "Brakk. The captain struck and the gunner did not. She is in the boat bay, aft, with a cutlass, and our cell slung on her back."

- [Ask her something else](oduya)
- [Tell her she is going home]()
```

Three of those answers send a signal you did not invent. They are the game's, and each
was played:

| The answer sends | The party | The ship | Take the Black Gull | Kesh Relay |
|---|---|---|---|---|
| `boarding_deck_take` | Home, at once | Joins your side. She stayed where she was | Done. 200 credits | Opens when the ship is back within 3000 |
| `boarding_deck_scuttle` | Home first | Gone from the map | Failed, because the answer says `fails prize` | The same |
| `boarding_deck_leave` | Home | Still struck. Within seconds she turned for where she came from | Still open | The same |

`Leave it for now` sends nothing, so the party stays aboard and can come back to the
box.

After `leave` she can be boarded again while she is still on the map. Tried: twelve
seconds later Comms was offered the button again, and the second party found the deck
as the first had left it. The same goes for a ship nobody boards at all. In the
stand-in she covered about 3,200 in the first minute, and Comms could still send a
party at 4,300. How fast she runs in the real game has not been measured.

## Step 8 - Check it

```
sbs lint MyAway
```

**This is the second rough thing.** Your finished mission does not lint `clean`:

```
== mission.amd ==
  [WARNING] line 766:35: `strongbox` emits signal `boarding_deck_scuttle` but no `//signal/boarding_deck_scuttle` route was found in the mission's .mast (nor a known driver signal) (signal-no-route)
  [WARNING] line 767:36: `strongbox` emits signal `boarding_deck_leave` but no `//signal/boarding_deck_leave` route was found in the mission's .mast (nor a known driver signal) (signal-no-route)

1 amd + 1 mast file(s): 0 error(s), 2 warning(s)
```

Both warnings are wrong. The routes exist, in the game's `boarding` library, and both
answers were played and worked. The tool does not see them there. Until it does, this
mission has two warnings that you leave alone, and **two is the number to check**. A
third warning is yours.

Each row below was tried on the finished files, one change at a time.

| The mistake | What the game does | What lint says |
|---|---|---|
| `Mark: bgri` | The strongbox stands in the hallway | `tiles-deck-unknown-kind`. It asks `did you mean 'brig'?` |
| No `Mark:` line on the kit | It stands in the hallway | `tiles-deck-no-mark` |
| `At: 5, 5` on the kit | It is put on cell 5, 5, which is solid hull. Nobody can reach it | `tiles-deck-cell` |
| `Mark: captains-cabin`, a room's own name | It stands in that room on this hull, and in the hallway on any other | `tiles-deck-unknown-kind` |
| `Area: decks` | The kit is not aboard. `mast.runtime.log` in the mission folder says so | `tiles-unknown-area` |
| `Done when: signal boarding_deck_took` | Not played | `unfired-signal` |
| `; signal boarding_deck_takes` | Not played | `unfired-signal`, on the quest that waits |
| `; signal boarding_deck_scuttle fails prize`, no comma | Not played | `outcome-run-together` |
| The card's lines typed at the left edge | Nothing runs at all | `mast-compile`, an error. It says `Bad indentation` |

The first of them, as lint printed it:

```
  [WARNING] line 415:7: strongbox: 'bgri' is not a kind of room - did you mean 'brig'? On `Area: deck` a Mark: is a kind of room (airlock, bay, beam, bridge, brig, cargo, computer, conference, galley, hyper, impulse, jump, lab, lounge, maneuver, mess, production, quarters, recreation, sensor, shield, sickbay, torpedo, warp, workshop), `entry` or `hallway`; anything else stands in the hallway (tiles-deck-unknown-kind)
```

### What lint cannot see

All of these gave only the two warnings you expect. All were played.

| The mistake | What happens |
|---|---|
| The ship wears `gul`, not `gull` | She never strikes. The quest never finishes |
| `QUEST_ID == "bak"` on the card | The quest finishes, the next one appears, and she never strikes |
| No `Then: reveal back` | The same |
| `Starts when: at once` on Come Back to Kesh Relay | The same. The card only hears a step that was hidden and then revealed |
| `Starts when: signal ...` on that quest, in place of `revealed` | It sat in the quest list as `Available` and never started. The relay never opened again |
| The card without `boarding_visit_end()` | She strikes. Comms answers `We cannot take a party aboard while your people are elsewhere.` |
| No second place for the ship | She strikes, and eight seconds later she is gone |
| No `Enemies: tsn`, or no Sides section, or the key spelled `pirates` | Before she strikes, Comms cannot open on her. She still strikes and can still be boarded. With no side at all, `mast.runtime.log` says `Side not found: [pirate]` |
| A thing shut in by one of her crew | Nothing. A click on it does nothing |
| A `Mark:` for a room she does not have | The hallway, and one line in `debug.log` |

## Step 9 - Play it

```
sbs run server,helm,comms,weapons,science -m MyAway map=0
```

1. Open the quest list. **Run Down the Black Gull** and **Take the Black Gull** are
   there from the first second, beside **Relight Kesh Relay** and its clock.
2. On Comms, select the Black Gull. The buttons are `Hail`, `Taunt` and `Surrender now`.
3. Helm: fly to within 1500 of her. She is about 7,100 away.
4. She strikes. **Come Back to Kesh Relay** appears in the quest list. Anybody who was
   down at the relay is back at their console.
5. On Comms, select her again. The buttons are now `Take as prize` and `Send a boarding
   party`. Press **Send a boarding party**. She answers:

   ```
   We are hove to. Send your party across: Boarding Party, on the ePADD.
   ```

6. On each console that is going, press the handheld icon, then **Boarding Party**. It
   says `Going down to Black Gull`. Press **BEAM DOWN**.
7. You are in her hallway. The boarding kit is one step away. Take it.
8. As Dr Hale, click Mate Oduya, in a brig. Ask her both questions.
9. As Lt Reyes, find the gunner in the boat bay. Open **Fire**, choose FULL, press
   **Arm** and click her. She drops a power cell. Pick it up.
10. Click the strongbox, in the other brig. Take **Take her as a prize**.
11. Everybody is back at their console, and the ship has 200 credits. Helm: fly back to
    within 3000 of Kesh Relay. The Boarding Party tile offers **Kesh Relay** again.
12. Beam down. Lt Reyes still has the cell. Light the beacon with it.

A script walked exactly that for this page, on three stand-in consoles. Aboard her it
took 22 seconds and five presses. The beacon was lit with the gunner's cell, and the
last screen read `The beacon is lit. Every convoy on the Kesh run has its way home
again.`

What the handheld showed aboard, captured the way Lecture 13's were:

```
Dr Ines Hale | medical, science | entry
Lt Sam Reyes | security | room:boat-bay
```

The third word is the game's own name for the room, colon and all. You did not choose
it and you cannot change it.

Then play the other two endings. And then do the walk from Step 6: go aboard and walk
to every thing you wrote.

### Five more things to know before your crew finds them

**A FULL shot destroys any prop. This is the third rough thing, and you know it from
Lecture 11.** Aboard a ship it is sharper, for two reasons.

- One FULL shot at the strongbox, and there are no endings. Tried: the box was gone.
  The party beamed up one by one from the Crew app. The Gull stayed held, and Comms
  offered only `Take as prize`. The mission was not stuck: when the ship came back to
  the relay, your line on the card brought the visit to an end and opened the relay.
- A pickup under a hostile's feet is shot with her. In the first draft of this lecture
  the power cell was a pickup lying in the boat bay. Brakk walked onto its cell, the
  script fired FULL at her, and the shot destroyed the power cell and left her
  standing. She put Lt Reyes down in the next few seconds. That is why the cell is
  now something she `Drops:`.

**What a hostile drops is lost if nobody picks it up.** Tried: Brakk was put down, the
party left without the cell, and came aboard again. Brakk was still down and the cell
was not there.

**`Take as prize` on Comms skips everything you wrote.** It is the game's own button,
on every ship that has struck. Tried: she joined the crew's side at once, nobody went
aboard, and **Take the Black Gull** stayed open for the rest of the game with no
credits paid. Tell your Comms officer which button is the story.

**From her deck, the Beam app offers `To Kesh Relay`.** The transporter reaches any
area of yours that is known, whichever party is open. Tried: Dr Hale beamed from the
Gull to the landing pad, treated Marrow's cough, and beamed back to the Gull. Her side
story was not there to be finished, because a party sent by the Comms button is handed
no side stories. A line `beam: no` in the yard's map did not close it: once the gully
was known, the deck offered `To Dry Gully`. Know that it is there.

**A ship that has struck may still launch fighters.** The team that built this saw one
do it with a party aboard. In this mission, in eighty seconds, the Black Gull launched
none. A carrier may. If you board one, expect it.

### What your records remember

Your `Area: deck` records are aboard *whatever* ship the crew boards, and they keep
their state from one ship to the next. Tried with a second ship that struck, a
freighter:

| Aboard the Black Gull | Then aboard the freighter |
|---|---|
| The kit was taken | No kit |
| Brakk was put down | No Brakk |
| Mate Oduya was talked to | Mate Oduya again, in the hallway: a freighter has no brig |
| The strongbox was left | The strongbox again. **Take her as a prize** took the freighter, and finished **Take the Black Gull** |

So with one ship to board, this is what you want. With two, it is one strongbox and
one prisoner on both. A quest that waits on `boarding_deck_take` does not know which
ship was taken.

## If something goes wrong

| What you see | Why | What to do |
|---|---|---|
| She strikes and is gone a few seconds later | She struck where she was put on the map | Step 3: the far place on the first line, `set_pos` on the second |
| She never strikes | The role, the quest's key on the card, or the `Then: reveal back` line | The first four rows of "What lint cannot see" |
| Comms has no **Send a boarding party** | She has not struck. Or somebody already sent a party: the button goes away while one is aboard | Look at the Boarding Party tile on the handheld |
| `We cannot take a party aboard while your people are elsewhere.` | The relay party is open | The card is missing `boarding_visit_end()`. Or the ship has been back to the relay: one party at a time |
| Comms will not open on her after she strikes, and lint is as it should be | The `station` art is not installed | `sbs fetch "MyAway" --update-libs`. Check the last line of `"shared_media"` in `story.json` |
| A thing is aboard and cannot be clicked | One of her crew is in the way | Step 6: change its `Mark:` to `brig`, `bay`, `entry` or `hallway`, and walk it again |
| A thing is in the hallway | Her hull has no room of that kind | Nothing, if you meant to board other hulls. `debug.log` has the line |
| The party cannot end the visit | The strongbox was shot | Beam up from the Crew app, and fly back to the relay |
| Somebody is down aboard her and stays down | The others are still up. Lecture 14's rule | The boarding kit, from the Pack app |
| Lint says `mast-compile` and nothing runs | A line of the card is not indented | Four spaces, and eight on the `side_surrender` line |

## Exercise

1. Play all three endings. After each, write down what Comms is offered on the Black
   Gull.
2. Add a thing with `Mark: lab`. Play it, and find where it stands.
3. Move the strongbox to `Mark: quarters`. Go aboard and try to reach it. Put it back.
4. Change her hull to `"cargo_ship"` and go aboard. Where is everything? How many crew
   has she? Change it back.
5. The gunner's cell is a short road to the beacon. Do Lecture 14's three lists again
   with the Black Gull in them. Which party can win now that could not before?
6. Break it and read lint: `Mark: bgri`; the comma out of the scuttle answer; the
   card's lines at the left edge. Then count the warnings on the finished file.

Then answer on paper, from the two files alone:

- Which line makes her strike, and which line decides when?
- Which two lines keep the game to one party at a time?
- What is lost for good if the party leaves the Black Gull too early?

## Checkpoint

You are done when all six are true:

- `sbs lint MyAway` gives exactly the two `signal-no-route` warnings of Step 8.
- The Black Gull strikes when the ship closes on her, and Comms is offered **Send a
  boarding party**.
- You have walked to the kit, the prisoner, the gunner and the strongbox.
- You have played all three endings.
- After each of them, Kesh Relay opened again when the ship came back.
- You have lit the beacon with the gunner's cell.

## Next

Lecture 16 is your own long away mission. A ship the crew boards can be one of its
places, and you now know what that costs: a side, a ship, a card, and a walk.

## Further reading

Nothing here is needed for the next lecture.

- "Ground tile maps" in the library documentation: "Boarding a ship that has
  surrendered". It lists every word `Mark:` takes, the systems among them.
- "Sides and lifeforms" in the library documentation, for the Sides section.
- Class 2, Lecture 1, if you have not taken it: sides, colors and relations.
